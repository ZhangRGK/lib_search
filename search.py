#!/usr/bin/env python
# encoding=utf-8

import tornado.web
import tornado.ioloop
import sys
import random
import os


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("user_id"):
            self.set_secure_cookie("user_id", str(random.randint(100, 10000)))
            self.write("API Searching!")
        else:
            self.write("Come on Template!")

    def post(self):
        pass


settings={
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "rui_zhao_together"
}

application = tornado.web.Application([(r"/", SearchHandler),
                                     (r"/static/(.*)", tornado.web.StaticFileHandler, dict(path = settings["static_path"]))], **settings)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        port = sys.argv[1]
    else:
        port = 8888

    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
