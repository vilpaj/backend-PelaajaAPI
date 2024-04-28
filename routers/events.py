from fastapi import APIRouter, Depends
from database import events_crud
from database.models import EventDB
from database.database import get_session
from sqlmodel import Session

router = APIRouter(prefix="/events", tags=["Events"])

#hae events-type
@router.get("/", response_model=list[EventDB])
def get_events(*, session: Session = Depends(get_session), event_type: str | None = None):
    return events_crud.get_events(session, event_type)