
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
        pass

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
        :return: the hit type if there was a hit, invalid type if the cords are invalid, None otherwise
        """

        if not (1 <= location_x <= consts.GameRules.BOARD_LEN and 1 <= location_y <= consts.GameRules.BOARD_LEN):
            return consts.MsgTypes.INVALID
        print(f"the enemy attacked [{location_x}, {location_y}]")
        is_hit = input(
            f"was this a hit? did you lose? enter '{consts.MsgTypes.HIT}', '{consts.MsgTypes.HIT_SINK}', '{consts.MsgTypes.FIN}' or 'no' (don't lie to me):")
        while is_hit not in [consts.MsgTypes.HIT, consts.MsgTypes.HIT_SINK, consts.MsgTypes.FIN, 'no']:
            print('that\'s not even an option!')
            is_hit = input(
                f"was this a hit? did you lose? enter '{consts.MsgTypes.HIT}', '{consts.MsgTypes.HIT_SINK}', '{consts.MsgTypes.FIN}' or 'no' (don't lie to me):")
        if is_hit in [consts.MsgTypes.HIT, consts.MsgTypes.HIT_SINK, consts.MsgTypes.FIN]:
            return is_hit
        return None

    def get_guess(self):
        """
        get the player's guess
        :return: the guess
        """

        cords = input("Enter your guess (<x> <y>): ").split()
        if 2 != len(cords):
            return 0, 0 # invalid cords, user will be notified
        try:
            return int(cords[0]), int(cords[1])
        except ValueError as e:
            return 0, 0 # invalid cords, user will be notified
