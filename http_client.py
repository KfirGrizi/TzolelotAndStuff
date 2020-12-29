
import requests
import json

import consts


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
    payload = json.dumps({
        "test data": "nice value"
    })

    headers = {
        'Content-Type': 'application/json',
        'type': consts.MsgTypes.INIT
    }
    client = BattleshipsClient('127.0.0.1')
    response = client.communicate(headers, payload)
    print(f"== HEADERS =======\n{response.headers}\n")
    print(f"== TEXT ==========\n{response.text}")


if __name__ == '__main__':
    main()
