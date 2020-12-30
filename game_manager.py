
import json
import random

import consts
import data_creation


class DataPacket:
    """
    holds the data of a single message in the protocol
    """

    def __init__(self, msg_type, msg_data):
        self.msg_type = msg_type
        self.msg_data = msg_data


class BattleshipsGameManager:
    """
    handles battleships game logic
    """

    def __init__(self):
        self.hit_counter = 0

    def play_turn(self, msg_type: str, msg_data: str) -> DataPacket:
        """
        play a single turn (get the opponent's message and return a response)
        :param msg_type: the opponent's message type
        :param msg_data: the opponent's message content
        :return: the new response
        """

        if consts.MsgTypes.INIT == msg_type:
            pass # do nothing
        elif consts.MsgTypes.SHOOT == msg_type:
            msg_data = json.loads(msg_data)
            hit = self.check_hit(msg_data['location-x'], msg_data['location-y'])
            if hit:
                return DataPacket(hit, '')
            # no hit - your turn
            guess_x, guess_y = self.get_guess()
            return DataPacket(consts.MsgTypes.SHOOT, data_creation.create_shoot_msg_data(guess_x, guess_y))
        elif consts.MsgTypes.HIT == msg_type:
            guess_x, guess_y = self.get_guess()
            return DataPacket(consts.MsgTypes.SHOOT, data_creation.create_shoot_msg_data(guess_x, guess_y))
        elif consts.MsgTypes.HIT_SINK == msg_type:
            guess_x, guess_y = self.get_guess()
            return DataPacket(consts.MsgTypes.SHOOT, data_creation.create_shoot_msg_data(guess_x, guess_y))
        elif consts.MsgTypes.INVALID == msg_type:
            guess_x, guess_y = self.get_guess()
            return DataPacket(consts.MsgTypes.SHOOT, data_creation.create_shoot_msg_data(guess_x, guess_y))
        elif consts.MsgTypes.FIN == msg_type:
            return DataPacket(consts.MsgTypes.FIN, '')

        return DataPacket(consts.MsgTypes.INVALID, 'unrecognized message type')

    def check_hit(self, location_x, location_y):
        """
        check if there is a battleship in a single location
        :param location_x: the location on the x axis
        :param location_y: the location on the y axis
        :return: the hit type if there was a hit, None otherwise
        """
        # randomly decide if there was a hit, TODO: implement an actual battleships game if you can
        if 1 == random.randint(0, 1):
            self.hit_counter += 1
            if 3 == self.hit_counter:
                return consts.MsgTypes.HIT_SINK
            if 5 == self.hit_counter:
                return consts.MsgTypes.FIN
            return consts.MsgTypes.HIT
        # there was no hit
        return None

    def get_guess(self):
        """
        get the player's guess
        :return: the guess
        """
        # random guess, TODO: implement an actual battleships game if you can
        return random.randint(1, 10), random.randint(1, 10)
