from kafka import KafkaProducer
from datetime import datetime
import time
from json import dumps
import random
import pandas as pd
from configparser import ConfigParser

conf_file_name = "X:\\2023-24\\Nam_4_HK1\\tieu_luan_chuyen_nganh\\making\making\\kafka_producer_consumer\\stream_app.conf"
config_obj = ConfigParser()
config_read_obj = config_obj.read(conf_file_name)

# Kafka Cluster/Server Details
kafka_host_name = config_obj.get('kafka', 'host')
kafka_port_no = config_obj.get('kafka', 'port_no')
kafka_topic_name = config_obj.get('kafka', 'input_topic_name')

KAFKA_TOPIC_NAME_CONS = kafka_topic_name
KAFKA_BOOTSTRAP_SERVERS_CONS = kafka_host_name + ':' + kafka_port_no

if __name__ == "__main__":
    print("Kafka Producer Application Started ... ")

    kafka_producer_obj = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS_CONS,
                                       value_serializer=lambda x: dumps(x).encode('utf-8'))
    type_list = ['Run', 'Hike', 'Ride', 'Swim', 'Walk']
    data = pd.read_csv("./student.csv")

    student_list = data['student'].tolist()
    
    message = None
    for i in range(100):
        i = i + 1
        message = {}
        print("Preparing message: " + str(i))
        event_datetime = datetime.now()

        message["run_id"] = i
        student_id = None
        name = None
        gender=None
        org_name = None
        org_name_child = None
        year_study=None
        student = None
        student = random.choice(student_list)
        student_id = student.split(",")[0]
        name = student.split(",")[1]
        gender = student.split(",")[2]
        org_name = student.split(",")[3]
        org_name_child = student.split(",")[4]
        year_study = student.split(",")[5]
        message["student_id"] = student_id
        message["name"] = name
        message["gender"] = gender
        message["org_name"] = org_name
        message["org_name_child"] = org_name_child
        message["year_study"] = year_study
        message["average_speed"] = round(random.uniform(1.001, 10.999), 3)
        message["max_speed"] = round(random.uniform(1.001, 10.999), 3)

        both_none = random.choice([True, False])
        if both_none:
            # Cả hai đều là None
            message["average_heartrate"] = None
            message["max_heartrate"] = None
        else:
            # Cả hai đều khác None
            average_heartrate = random.uniform(1.001, 10.999)
            message["average_heartrate"] = round(average_heartrate, 3)

            max_heartrate = random.uniform(1.001, 10.999)
            message["max_heartrate"] = round(max_heartrate, 3)
            
        message["distance"] = round(random.uniform(1.5, 12.5), 1)
        message["elapsed_time"] = int(random.uniform(111, 8000))
        message["moving_time"] = int(random.uniform(111, 8001))
        message["total_elevation_gain"] = round(random.uniform(3.5, 1000.5), 1)
        message["elev_high"] = round(random.uniform(35.5, 1330.5), 1)
        message["type"] = random.choice(type_list)
        message["start_date_local"] = event_datetime.strftime("%Y-%m-%d %H:%M:%S")
        message["kudos_count"] = int(random.uniform(0, 20))
        
        print("Message: ", message)

        kafka_producer_obj.send(KAFKA_TOPIC_NAME_CONS, message)
        time.sleep(2)

    print("Kafka Producer Application Completed. ")
