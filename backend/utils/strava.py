from fastapi import HTTPException
import requests
from sqlalchemy.orm import Session
from backend.db.model import User
client_id = "116867"
client_secret = "9b0fed222ce18d140313c23c11946345b74c60f6"

def get_all_activities(access_token):
    url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def exchange_authorization_code(authorization_code: str):
    url = "https://www.strava.com/oauth/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": authorization_code,
        "grant_type": "authorization_code"
    }
    response = requests.post(url, data=payload)
    data = response.json()
    return data

def exchange_authorization_code_at(authorization_code:str):
    url = "https://www.strava.com/oauth/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": authorization_code,
        "grant_type": "authorization_code"
    }
    response = requests.post(url, data=payload)
    data = response.json()
    access_token = data['access_token']
    return access_token

def revoke_access_token(db: Session, current_user: User):
    try:
        url = "https://www.strava.com/oauth/deauthorize"
        params = {"access_token": current_user.STRAVA_ACCESS_TOKEN}
        response = requests.post(url, params=params)
        if response.status_code == 200:
            current_user.STRAVA_ID=None
            current_user.STRAVA_ACCESS_TOKEN=None
            current_user.STRAVA_REFRESH_TOKEN=None
            current_user.STRAVA_FULL_NAME=None
            db.commit()
            res = {
                "message":"Hủy kết nối thành công"
                }
            return res
        else:
            res = {
                "message":"Hủy kết nối thất bại"
                }
            return res
    except :
        response = {
            "message":"Xảy ra lỗi"
        }
        return response

def get_activity_info_by_id(object_id: int, access_token: str):
    base_url = "https://www.strava.com/api/v3/activities/"
    url = f"{base_url}{object_id}"
    headers = {
        "Authorization": "Bearer " + access_token
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        activity_info = response.json()
        return activity_info
    else:
        print("Error:", response.status_code)
        return None


def refresh_strava_token(refresh_token: str):
    url = "https://www.strava.com/api/v3/oauth/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        data = response.json()
        access_token = data.get("access_token")
        new_refresh_token = data.get("refresh_token")
        return access_token, new_refresh_token
    else:
        return None
