from fastapi import HTTPException
from sqlmodel import Session, select
from .models import PlayerDB, PlayerCreate, EventCreate, EventDB
from datetime import datetime

#hae pelaajat
def get_players(session: Session):
    return session.exec(select(PlayerDB)).all()

#lisää pelaaja
def create_player(session: Session, player_in: PlayerCreate):
    player_db = PlayerDB.model_validate(player_in)
    session.add(player_db)
    session.commit()
    session.refresh(player_db)
    return player_db

#hae pelaaja ID
def get_player(session: Session, id: int):
#rajoitetaan tulokset, palautetaan eka joka löytyy
    return session.exec(select(PlayerDB).filter(PlayerDB.id == id)).first()

#luo uusi event pelaajalle
def create_player_event(session: Session, player_id: int, event_in: EventCreate):
    player_exist = session.exec(select(EventDB).filter(EventDB.player_id == player_id)).first()
    if not player_exist:
        raise HTTPException(status_code=404)
    if event_in.type not in ["level_started", "level_solved"]:
        raise HTTPException(status_code=400)
    if event_in.detail.startswith("level_") or len(event_in.detail) != 13:
        raise HTTPException(status_code=422)
    event = EventDB(**event_in.model_dump(), player_id=player_id, timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    session.add(event)
    session.commit()
    session.refresh(event)
    return event