from starlette.requests import Request as StarletteRequest
from fastapi import APIRouter, Request, Depends
from fastapi import HTTPException
from backend.schema import WebhookResponse
from sqlalchemy.orm import Session
from backend.db.database import get_db

router = APIRouter(
  prefix='/webhook',
  tags=['webhook']
)
VERIFY_TOKEN = "STRAVA"

@router.get('/')
def verify_webhook(request: Request):
    starlette_request = StarletteRequest(request.scope, request.receive)
    query_params = starlette_request.query_params

    hub_verify_token = query_params.get('hub.verify_token')
    hub_challenge = query_params.get('hub.challenge')
    hub_mode = query_params.get('hub.mode')

    if hub_mode == 'subscribe' and hub_verify_token == VERIFY_TOKEN:
        return {"hub.challenge": hub_challenge}
    else:
        raise HTTPException(status_code=403)

@router.post('/')
async def process_webhook(request: Request, db: Session = Depends(get_db)):
    from db.db_run import update_run_eventwebhook, add_run_eventwebhook
    request_body = await request.json()
    res = WebhookResponse(**request_body)
    if res.aspect_type=='update':
        await update_run_eventwebhook(res,db)
    else :
        await add_run_eventwebhook(res,db)
    return {"status": 200}
