from sqlmodel import Field, SQLModel

#pelaajat
class PlayerBase(SQLModel):
    name: str

class PlayerDB(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class PlayerCreate(PlayerDB):
    pass

#eventit
class EventBase(SQLModel):
    type: str
    detail: str

class EventDB(EventBase, table=True):
    id: int = Field(primary_key=True)
    type: str
    detail: str
    timestamp: str
    player_id: int

class EventCreate(EventBase):
    pass