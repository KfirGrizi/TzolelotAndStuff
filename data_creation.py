
import json


def create_empty_msg_data() -> str:
    return json.dumps({})

def create_shoot_msg_data(location_x: int, location_y: int) -> str:
    return json.dumps({
            "location-x": location_x,
            "location-y": location_y
        })


def create_init_msg_data() -> str:
    return create_empty_msg_data()


def create_hit_msg_data() -> str:
    return create_empty_msg_data()


def create_hit_sink_msg_data() -> str:
    return create_empty_msg_data()


def create_invalid_msg_data() -> str:
    return create_empty_msg_data()


def create_fin_msg_data() -> str:
    return create_empty_msg_data()
