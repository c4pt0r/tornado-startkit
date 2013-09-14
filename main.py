#encoding=utf-8
import tornado.web
import tornado.ioloop
import router
from views import *

application = tornado.web.Application(router.route.get_routes())

if __name__ == '__main__':
    application.listen(8089)
    tornado.ioloop.IOLoop.instance().start()
