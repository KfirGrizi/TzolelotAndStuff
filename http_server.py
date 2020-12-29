
from http.server import HTTPServer, BaseHTTPRequestHandler
import  json

import consts


class PacketData:
    def __init__(self, headers, text: bytes):
        self.headers = headers
        self.text = text


class BattleshipsServerPeer:
    def __init__(self):
        pass

    def handle(self, msg_type, text) -> PacketData:
        print(f"type: '{msg_type}'\ntext: '{text}'")
        if consts.MsgTypes.INIT == msg_type:
            return PacketData({'type': consts.MsgTypes.INIT}, b'cool init, thanks')
        return PacketData({'type': consts.MsgTypes.FIN}, b"i don't speak your language")


class BattleshipsHTTPRequestHandler(BaseHTTPRequestHandler):
    battleships_server_peer = BattleshipsServerPeer()
    def do_POST(self):
        # get data length
        length = int(self.headers.get('Content-length', 0))

        # get the data
        data = json.loads(self.rfile.read(length).decode())

        # handle the request and generate the response
        msg_type = self.headers.get('type', 0)
        res = BattleshipsHTTPRequestHandler.battleships_server_peer.handle(msg_type, data)

        # send a 200 OK response
        self.send_response(200)

        # send headers
        for header_name, header_value in res.headers.items():
            self.send_header(header_name, header_value)
        self.end_headers()

        # send response text
        self.wfile.write(res.text)


def main():
    server_address = ('', consts.Communication.PORT)
    httpd = HTTPServer(server_address, BattleshipsHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
