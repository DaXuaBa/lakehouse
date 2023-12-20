import json
from kafka import KafkaProducer
from sqlalchemy.orm.session import Session
from backend.db.model import *
from backend.schema import *
from backend.utils.strava import *

KAFKA_TOPIC_NAME_CONS = "runinput"
KAFKA_BOOTSTRAP_SERVERS_CONS = "34.16.163.230:9092"              
producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS_CONS, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        
def format_seconds(seconds:str):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return formatted_time

def get_run_by_stravarunid(object_id : str, db: Session):
    run = db.query(Run).filter(Run.STRAVA_RUN_ID == object_id).first()
    return run

def update_run_eventwebhook(res :WebhookResponse, db: Session):
    run = get_run_by_stravarunid(res.object_id, db)
    if res.updates.get('title'):
        run.NAME = res.updates['title']
    if res.updates.get('type'):
        run.TYPE = res.updates['type']
    db.commit()

def add_run_eventwebhook(res :WebhookResponse, db: Session):
    user = db.query(User).filter(User.STRAVA_ID == res.owner_id).first()
    existing_run = db.query(Run).filter(Run.STRAVA_RUN_ID == res.object_id).first()
    if existing_run:
        return 200
    activity = get_activity_info_by_id(res.object_id, user.STRAVA_ACCESS_TOKEN)
    if activity == None:
        access_token, new_refresh_token = refresh_strava_token(user.STRAVA_REFRESH_TOKEN)
        activity = get_activity_info_by_id(res.object_id, access_token)
        user.STRAVA_ACCESS_TOKEN = access_token
        user.STRAVA_REFRESH_TOKEN = new_refresh_token
    
    start_date_local = datetime.strptime(activity['start_date_local'], '%Y-%m-%dT%H:%M:%SZ')
    new_run = Run(
            USER_ID=user.USER_ID,
            STRAVA_RUN_ID=activity.get('id'),
            NAME=activity.get('name'),
            AVERAGE_SPEED=activity.get('average_speed'),
            MAX_SPEED=activity.get('max_speed'),
            AVERAGE_HEARTRATE=activity.get('average_heartrate'),
            MAX_HEARTRATE=activity.get('max_heartrate'),
            DISTANCE=(activity.get('distance') or 0) / 1000,
            ELAPSED_TIME=format_seconds(activity.get('elapsed_time')),
            MOVING_TIME=format_seconds(activity.get('moving_time')),
            TOTAL_ELEVATION_GAIN=activity.get('total_elevation_gain'),
            ELEV_HIGH=activity.get('elev_high'),
            TYPE=activity.get('type'),
            CREATED_AT=start_date_local,
            KUDOS_COUNT=activity.get('kudos_count')
        )
    db.add(new_run)
    db.commit()
    db.refresh(new_run)
    if new_run:
        data ={
            "student_id":user.STUDENT_ID,
            "name": user.FULL_NAME,
            "gender": user.GENDER,
            "org_name": user.ORG_NAME,
            "org_name_child": user.ORG_NAME_CHILD,
            "year_study": user.YEAR_STUDY,
            "average_speed": new_run.AVERAGE_SPEED,
            "max_speed": new_run.MAX_SPEED,
            "average_heartrate": new_run.AVERAGE_HEARTRATE,
            "max_heartrate": new_run.MAX_HEARTRATE,   
            "distance": new_run.DISTANCE,
            "elapsed_time": new_run.ELAPSED_TIME,
            "moving_time": new_run.MOVING_TIME,
            "total_elevation_gain": new_run.TOTAL_ELEVATION_GAIN,
            "elev_high": new_run.ELEV_HIGH,
            "type": new_run.TYPE,
            "start_date_local": new_run.CREATED_AT.strftime("%Y-%m-%d %H:%M:%S"),
            "kudos_count": new_run.KUDOS_COUNT
        }
        producer.send(KAFKA_TOPIC_NAME_CONS, value=data)
    else:
        print("Không có hoạt động nào phù hợp.")
    return 200
