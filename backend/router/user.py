from fastapi import APIRouter, Depends, HTTPException, status
from backend.schema import UserBase
from backend.db.database import get_db
from sqlalchemy.orm import Session
from backend.db.db_user import *
from backend.utils.validation import *
from typing import List
from backend.utils.oauth2 import get_current_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('/register')
def register_user(request: UserBase, db: Session = Depends(get_db)):
    if not request.username or not request.student_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Yêu cầu điền đầy đủ Tài khoản và Mã số sinh viên')
    else:
        if not request.password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Cần phải nhập đẩy đủ mật khẩu')
        if not is_valid_username(request.username):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Tài khoản không hợp lệ')
        if not request.student_id.isdigit() or len(request.student_id) != 8:
            return {"error": "Mã số sinh viên không chính xác"}
    request.password=Hash.bcrypt(request.password)
    return create_user(request, db)

@router.get('/all', response_model=List[UserDisplay])
def get_all_user_router(db: Session = Depends(get_db)):
    return get_all_user(db)

@router.post('/authorize-code')
def add_info_from_strava(authorizecode: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):          
    return add_info_strava(authorizecode, db, current_user)