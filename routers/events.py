from fastapi import APIRouter, Depends
from database import events_crud
from database.models import EventDB
from database.database import get_session
from sqlmodel import Session

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/", response_model=list[EventDB])
def get_events(*, session: Session = Depends(get_session), event_type: str | None = None):
    return events_crud.get_events(session, event_type)

#event poisto
@router.delete("/{id}")
def delete_event(*, session: Session = Depends(get_session), id: int):
    return events_crud.delete_event(session, id)