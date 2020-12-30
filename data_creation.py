
import json


def create_shoot_msg_data(location_x: int, location_y: int) -> str:
    """
    get a location and create a serialized data to send
    :param location_x: the location on the x axis
    :param location_y: the location on the y axis
    :return: the serialized string
    """

    return json.dumps({
            "location-x": location_x,
            "location-y": location_y
        })
