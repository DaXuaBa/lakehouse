from pydantic import BaseModel
from typing import Any, Dict, Optional

class UserBase(BaseModel):
    username: str
    password: Optional[str] =None
    student_id:str
    full_name: str
    gender : str
    org_name:str
    org_name_child:str
    year_study:str
    class Config:
        from_attributes = True

class UserDisplay(BaseModel):
    STUDENT_ID:str
    FULL_NAME:str
    GENDER : str
    ORG_NAME:str
    ORG_NAME_CHILD:str
    YEAR_STUDY:str
    class Config:
        from_attributes = True

class WebhookResponse(BaseModel):
    aspect_type: str
    event_time: int
    object_id: int
    object_type: str
    owner_id: int
    subscription_id: int
    updates: Dict[str, Any]
