
import json

import consts


def wrap_msg_with_http(msg_type, data):
    return f"""POST / HTTP/1.1
type: {msg_type}

{data}"""


def create_shoot_msg(location_x: int, location_y: int) -> str:
    return wrap_msg_with_http(
        consts.MsgTypes.INIT,
        json.dumps({
            "location-x": location_x,
            "location-y": location_y
        })
    )


def create_init_msg() -> str:
    return wrap_msg_with_http(
        consts.MsgTypes.INIT,
        json.dumps({})
    )


def create_hit_msg() -> str:
    return wrap_msg_with_http(
        consts.MsgTypes.HIT,
        json.dumps({})
    )


def create_hit_sink_msg() -> str:
    return wrap_msg_with_http(
        consts.MsgTypes.HIT_SINK,
        json.dumps({})
    )


def create_invalid_msg() -> str:
    return wrap_msg_with_http(
        consts.MsgTypes.INVALID,
        json.dumps({})
    )


def create_fin_msg() -> str:
    return wrap_msg_with_http(
        consts.MsgTypes.FIN,
        json.dumps({})
    )
