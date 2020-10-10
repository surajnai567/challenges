import tornado.web
import tornado.websocket
import tornado.ioloop

clients = []


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("New client connected")
        clients.append(self)
        #self.write_message("You are connected")

    def on_message(self, message):
        print(message, self)
        for s in clients:
            s.write_message(message)

    def on_close(self):
        print(
        "Client disconnected")


application = tornado.web.Application([
    (r'/', WebSocketHandler,),
])

if __name__ == "__main__":
    application.listen(8080, "192.168.99.1")
    tornado.ioloop.IOLoop.instance().start()