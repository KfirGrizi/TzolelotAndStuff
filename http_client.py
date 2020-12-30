
import requests
import json

import consts
import game_manager


class PacketData:
    def __init__(self, headers, text: bytes):
        self.headers = headers
        self.text = text


class BattleshipsClient:
    def __init__(self, host):
        self.host = host

    def communicate(self, headers, data):
        url = f'http://{self.host}:{consts.Communication.PORT}'
        response = requests.post(url, headers=headers, data=data)
        return PacketData(response.headers, response.text)


def main():
    battleships_game_manager = game_manager.BattleshipsGameManager()
    payload = json.dumps({})
    headers = {
        'Content-Type': 'application/json',
        'type': consts.MsgTypes.INIT
    }
    client = BattleshipsClient('127.0.0.1')
    response = client.communicate(headers, payload)
    print('sent init')
    while True:
        msg_type = response.headers['type']
        print(f'got {msg_type}: {response.text}')
        if consts.MsgTypes.FIN == msg_type:
            print("VICTORY!!!!!!")
            break
        request = battleships_game_manager.play_turn(msg_type, response.text)
        headers['type'] = request.msg_type
        response = client.communicate(headers, request.msg_data)
        print(f'sent {request.msg_type}: {request.msg_data}')
        if consts.MsgTypes.FIN == request.msg_type:
            print("Just lost smh...")
            break


if __name__ == '__main__':
    main()
