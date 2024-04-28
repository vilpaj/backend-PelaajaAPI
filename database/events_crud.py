from sqlmodel import Session, select
from fastapi import HTTPException
from datetime import datetime
from .models import EventDB
from typing import List

hardcoded_eventtype = ["level_started", "level_solved"]

#hae pelaaja ID
def fetch_playerID(session: Session, player_id: int) -> list[EventDB]:
    db_events = session.exec(select(EventDB).filter(EventDB.player_id == player_id)).all()
    return db_events

#luo uusi event pelaajalle
def create_playerID_event(session: Session, player_id: int, event_type: str, detail: str):
    new_event = EventDB(
        type=event_type,
        detail=detail,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
        player_id=player_id
    )
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return new_event

#hae events-type
def get_events(session: Session, event_type: str | None = None) -> List[EventDB]:
    added_events = session.exec(select(EventDB)).all()
    if event_type is None:
        return added_events
    elif event_type not in hardcoded_eventtype:
        raise HTTPException(status_code=400)
    else:
        return [event for event in added_events if event.type == event_type]
    

#poista event
def delete_event(session: Session, id: int):
    event = session.get(EventDB,id)
    if event is None:
        raise HTTPException(status_code=404, detail=f'VIRHE')
    session.delete(event)
    session.commit()
    return {"message": f'POISTETTU {id}'}