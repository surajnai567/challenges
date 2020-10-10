from socketserver import TCPServer, BaseRequestHandler, ThreadingTCPServer
from threading import Thread

buffer_size = 10
host = []
number_of_workers_thread = 10


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('start listining')
        message = ''
        mes_len = 0
        new_msg = True
        print('got the connection: {}'.format(self.request))
        while True:
            data = self.request.recv(buffer_size)
            if new_msg:
                mes_len = int(data.decode('utf-8'))
                new_msg = False
            message += data.decode('utf-8')
            if len(message) - buffer_size == mes_len:
                self.request.send(message.encode('utf-8'))
                print(self.client_address, message)
                new_msg = True
                mes_len = 0
                message = ''


if __name__ == '__main__':
    server = TCPServer(('', 80), EchoHandler)
    for i in range(number_of_workers_thread):
        thread = Thread(target=server.serve_forever)
        thread.daemon = True
        thread.start()

    server.serve_forever()