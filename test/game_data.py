import json
from uuid import uuid4

GAME_INPROGRESS = 1
GAME_COMPLETED = 4

GAME_KEY = uuid4()
PLAYER_KEY_1 = uuid4()
PLAYER_KEY_2 = uuid4()

CREATE_RESPONSE = json.dumps({'key': str(GAME_KEY)})

LOBBY_RESPONSE = json.dumps({'name': 'Player Name', 'key': str(PLAYER_KEY_1)})

PLAYER_WINNER = {
    'key': str(PLAYER_KEY_1),
    'name': 'player winner',
    'winner': True
}

PLAYER_LOSER = {
    'key': str(PLAYER_KEY_2),
    'name': 'player loser',
    'winner': False
}

GAME_COMPLETED_PLAYER_O_WINS = {
    'size_x': 3,
    'size_y': 3,
    'cells': [],
    'name': 'anything',
    'player_x': {
        'name': 'player x',
        'winner': False
    },
    'player_o': {
        'name': 'player o',
        'winner': True
    },
    'state': GAME_COMPLETED
}

GAME_COMPLETED_3X3_PLAYER_O_WINS = {
    'name': 'something',
    'player_x': {
        'name': 'player 1',
        'winner': False
    },
    'player_o': {
        'name': 'player 2',
        'winner': True
    },
    'size_x': 3,
    'size_y': 3,
    'cells': [
        {'x': 0, 'y': 0, 'value': 2},
        {'x': 2, 'y': 2, 'value': 1}
    ],
    'state': GAME_COMPLETED
}

GAME_COMPLETED_2X3_PLAYER_O_WINS = {
    'name': 'something',
    'player_x': {
        'name': 'player 1',
        'winner': False
    },
    'player_o': {
        'name': 'player 2',
        'winner': True
    },
    'size_x': 2,
    'size_y': 3,
    'cells': [
        {'x': 0, 'y': 0, 'value': 2},
        {'x': 1, 'y': 2, 'value': 1}
    ],
    'state': GAME_COMPLETED
}

GAME_INPROGRESS_NO_MOVES_YET = {
    'size_x': 1,
    'size_y': 1,
    'cells': [],
    'name': 'anything',
    'player_x': {
        'name': 'player x',
        'winner': False
    },
    'player_o': {
        'name': 'player o',
        'winner': False
    },
    'state': GAME_INPROGRESS
}

GAME_INPROGRESS_2X2 = {
    'size_x': 2,
    'size_y': 2,
    'cells': [
        {'x': 0, 'y': 0, 'value': 2},
        {'x': 1, 'y': 1, 'value': 2}
    ],
    'name': 'anything',
    'player_x': {
        'name': 'player x',
        'winner': False
    },
    'player_o': {
        'name': 'player o',
        'winner': False
    },
    'state': GAME_INPROGRESS
}
