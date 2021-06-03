
import tornado.web
from publisher import execute
import requests
class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!!!!!!")

class pikaRequestHandler(tornado.web.RequestHandler):
    def get(self,message):
        execute(f"Sent {message}")

class elasticRequestHandler(tornado.web.RequestHandler):
    def get(self, id):
        requests.get(f"http://localhost:5601/controller/_doc/{id}")
        self.write("Querying tweet with id " + id)

class queryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument("n"))
        r = "odd" if n % 2 else "even"
        
        self.write("the number " + str(n) + " is " + r)


class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")