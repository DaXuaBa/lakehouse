from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from backend.db.model import User
from backend.db.db_run import *
from fastapi.responses import JSONResponse
from backend.utils.strava import *
from backend.utils.hash import *
from backend.schema import *

def create_user(request: UserBase, db: Session):
    user = get_user_by_username(request.username,db)
    id = get_id_by_student_id(request.student_id,db)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Tên đăng nhập đã tồn tại')
    elif id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Mã số sinh viên đã tồn tại')
    else:
        try:
            new_user = User(
                USER_NAME = request.username,
                PASSWORD = request.password,
                STUDENT_ID=request.student_id,
                FULL_NAME=request.full_name,
                GENDER=request.gender,
                ORG_NAME=request.org_name,
                ORG_NAME_CHILD=request.org_name_child,
                YEAR_STUDY=request.year_study
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            response = {
                "status": 200,
                "detail": "Tạo người dùng thành công!",
                "Tài khoản": new_user.USER_NAME,
                "Mssv": new_user.STUDENT_ID,
                "Họ và Tên": new_user.FULL_NAME,
                "Strava": new_user.STRAVA_ID,
            }
            return response
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Execution fail')
    
def get_all_user(db: Session):
    return db.query(User).all()

def get_user_by_username(username: str, db: Session):
    try: 
        user = db.query(User).filter(User.USER_NAME == username).first()
        if not user:
            return None
        return user
    except :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Execution fail')
    
def get_id_by_student_id(student_id: str, db: Session):
    try: 
        id = db.query(User).filter(User.STUDENT_ID == student_id).first()
        if not id:
            return None
        return id
    except :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Execution fail')
    
def get_user_by_stravaId(strava_id: int, db: Session):
    user = db.query(User).filter(User.STRAVA_ID == strava_id).first()
    if not user:
        return None
    return user    
    
def add_info_strava(code: str, db: Session, current_user: User):
    try:
        strava_info = exchange_authorization_code(code)
        if get_user_by_stravaId(strava_info['athlete']['id'], db):
            raise HTTPException(status_code=409, detail='Đã đăng ký Strava với tài khoản này')
        
        current_user.STRAVA_ID = strava_info['athlete']['id']
        current_user.STRAVA_ACCESS_TOKEN = strava_info['access_token']
        current_user.STRAVA_REFRESH_TOKEN = strava_info['refresh_token']
        current_user.STRAVA_FULL_NAME = strava_info['athlete']['firstname'] + ' ' + strava_info['athlete']['lastname']
        current_user.STRAVA_IMAGE = strava_info['athlete']['profile_medium']
        db.commit()
        
        response = {
            "message": "Kết nối thành công",
            "strava_userid": current_user.STRAVA_ID,
            "strava_fullname": current_user.STRAVA_FULL_NAME,
            "strava_image": current_user.STRAVA_IMAGE
        }
        return JSONResponse(content=response, status_code=200)
    except HTTPException as http_error:
        db.rollback()
        raise http_error
    except Exception as e:
        db.rollback()
        response = {
            "message": "Kết nối thất bại"
            }
        return JSONResponse(content=response, status_code=400) 