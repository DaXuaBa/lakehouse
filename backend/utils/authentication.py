from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from jose import JWTError
from sqlalchemy.orm.session import Session
from backend.db.database import get_db
from backend.db.model import User
from backend.utils import oauth2
from backend.db.db_user import get_user_by_username
from backend.utils.hash import Hash

router = APIRouter(
  prefix='/auth',
  tags=['authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        connection = db.connection().connection
        cursor = connection.cursor()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Không thể kết nối đến database.')
    try:
        user = get_user_by_username(request.username, db)
        if not user:
            raise HTTPException(status_code=400, detail="Tài khoản không hợp lệ")
        if not Hash.verify(user.PASSWORD, request.password):
            raise HTTPException(status_code=400, detail="Mật khẩu không chính xác")
        access_token = oauth2.create_access_token(data={'sub': user.USER_NAME})
        refresh_token = oauth2.create_refresh_token(data={'sub': user.USER_NAME})
        return {
            'accessToken': access_token,
            'refreshToken': refresh_token,
            'Tài khoản': user.USER_NAME,
            'Họ và Tên': user.FULL_NAME,
            "Strava": user.STRAVA_ID
            }
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Refresh token đã hết hạn hoặc không hợp lệ')
    finally:
        cursor.close()
        connection.close()