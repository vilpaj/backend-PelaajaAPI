from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session
from database.models import PlayerBase, PlayerDB, EventDB, EventBase
from database import players_crud, events_crud
from database.database import get_session
from typing import List

router = APIRouter(prefix="/players", tags=["Players"])

#hae pelaajat
@router.get("/", response_model=List[PlayerDB])
def get_players(session: Session = Depends(get_session)):
    return players_crud.get_players(session)

#lisää pelaaja
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerBase, session: Session = Depends(get_session)):
    player = players_crud.create_player(session, player_in)
    if not player:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return player

#hae pelaaja ID, sanakirja muoto
@router.get("/{id}", response_model=dict)
def get_playerID(id: int, session: Session = Depends(get_session)):
    player = players_crud.get_player(session, id)
    if not player:
            raise HTTPException(status_code=404)
    if player:
        player_events = events_crud.fetch_playerID(session, id)
        #sanakirja, pelaajan tiedot ja tapahtumat
        player_data = {
            "id": player.id,
            "name": player.name,
            "events": player_events
        }
        return player_data

hardcoded_eventtype = ["level_started", "level_solved"]

#hae pelaaja ID event
@router.get("/{id}/events", response_model=List[EventDB] | None)
def get_player_event(id: int, type: str | None = None, session: Session = Depends(get_session)):
    player_events = events_crud.fetch_playerID(session, id)
    if player_events is None:
        raise HTTPException(status_code=404)
    if type:
        if type not in hardcoded_eventtype:
            raise HTTPException(status_code=400)
        filtered_event = [event for event in player_events if event.type == type]
        if not filtered_event:
            raise HTTPException(status_code=404)
        return filtered_event
    else:
        return player_events or []

#luo uusi event pelaajalle
@router.post("/{id}/events", status_code=status.HTTP_201_CREATED)
def create_player_event(id: int, event_in: EventBase, session: Session = Depends(get_session)):
    return players_crud.create_player_event(session, id, event_in)