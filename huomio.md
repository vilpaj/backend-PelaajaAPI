Muista poistaa venv kansio ennen palautusta!

pip install fastapi uvicorn
pip install sqlmodel

#teko aloitettu rest03 mukaan, itselle helpompi
#kovakoodatut jutut (testausta varten):
players = {
    1:{"id": 1, "name": "Reijo", "events": [
        {
        "id": 1,
        "type": "level_started",
        "detail": "level_1212_001",
        "timestamp": "2023-01-10 14:35:01",
        "player_id": 1
        }
    ]},
    2:{"id": 2, "name": "Veijo", "events": [
        {
        "id": 2,
        "type": "level_solved",
        "detail": "level_1212_002",
        "timestamp": "2023-01-13 12:01:22",
        "player_id": 2 
        },
        {
        "id": 3,
        "type": "level_started",
        "detail": "level_1213_001",
        "timestamp": "2023-01-13 12:05:30",
        "player_id": 2
        } 
    ]},
    3:{"id": 3, "name": "Maija", "events":[]}
}

players = {
    1:{"id": 1, "name": "Reijo"},
    2:{"id": 2, "name": "Veijo"},
    3:{"id": 3, "name": "Maija"}
}

events = [
    {
        "id": 1,
        "type": "level_started",
        "detail": "level_1212_001",
        "timestamp": "2023-01-10 14:35:01",
        "player_id": 1
    },
    {
        "id": 2,
        "type": "level_solved",
        "detail": "level_1212_002",
        "timestamp": "2023-01-13 12:01:22",
        "player_id": 2
    },
    {
        "id": 3,
        "type": "level_started",
        "detail": "level_1213_001",
        "timestamp": "2023-01-13 12:05:30",
        "player_id": 2
    }        
]