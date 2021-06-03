import tornado.web
import tornado.ioloop
import tornado.httpserver
from handlers import *

class Application(tornado.web.Application):
    ORCHESTRATOR_PATH = ''
    ES_PATH = 'http://localhost:5601'


    def __init__(self):

        handlers_list = [
            (r"/", basicRequestHandler),
            (r"/exec/([a-zA-Z0-9]+)", pikaRequestHandler),
            (r"/blog", staticRequestHandler),
            (r"/isEven", queryStringRequestHandler),
            (r"/exec/([a-zA-Z0-9]+)", elasticRequestHandler),
        ]

        tornado.web.Application.__init__(self, handlers_list)


def main():
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application, max_buffer_size=10485760000)
    http_server.listen(8001)
    print("Started")
    tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
    main()

