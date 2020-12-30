

class MsgTypes:
    """
    holds every message type
    """

    INIT = 'init'
    SHOOT = 'shoot'
    HIT = 'hit'
    HIT_SINK = 'hit-sink'
    INVALID = 'invalid'
    FIN = 'fin'


class Communication:
    """
    holds communication related consts
    """

    PORT = 80
    SERVER_HOST = '127.0.0.1'


class GameRules:
    """
    holds game rules related consts
    """

    BOARD_LEN = 10
