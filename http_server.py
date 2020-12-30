
from http.server import HTTPServer, BaseHTTPRequestHandler

import consts
import game_manager


class BattleshipsHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    handles a single message from the opponent and returns a single message
    """

    battleships_game_manager = game_manager.BattleshipsGameManager()
    should_stop = False
    def do_POST(self):
        """
        handles a POST request - in this protocol it represent a message from the opponent
        """

        # get data length
        length = int(self.headers.get('Content-length', 0))

        # get the data
        data = self.rfile.read(length).decode()

        # handle the request and generate the response
        msg_type = self.headers.get('type', 0)
        print(f'got {msg_type}: {data}')
        res = BattleshipsHTTPRequestHandler.battleships_game_manager.play_turn(msg_type, data)

        if consts.MsgTypes.FIN == msg_type:
            print("VICTORY!!!!!!")
            BattleshipsHTTPRequestHandler.should_stop = True

        # send a 200 OK response
        self.send_response(200)

        self.send_header('Content-Type', 'application/json')
        # send type header
        self.send_header('type', res.msg_type)
        self.end_headers()

        # send response text
        self.wfile.write(res.msg_data.encode())

        print(f'sent {res.msg_type}: {res.msg_data}')
        # don't print lost message if won
        if not BattleshipsHTTPRequestHandler.should_stop and consts.MsgTypes.FIN == res.msg_type:
            print("Just lost smh...")
            BattleshipsHTTPRequestHandler.should_stop = True

    def log_message(self, format, *args):
        """
        handles logging, does nothing, since we don't want any logs to appear
        """

        return # disable logging to console, there is no better way :(


def main():
    """
    activate a battleships player (HTTP server side)
    """

    server_address = ('', consts.Communication.PORT)
    httpd = HTTPServer(server_address, BattleshipsHTTPRequestHandler)
    while not BattleshipsHTTPRequestHandler.should_stop:
        httpd.handle_request()


if __name__ == '__main__':
    main()
