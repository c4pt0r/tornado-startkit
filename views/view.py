import tornado.web
import router

@router.route("/view")
class ViewHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")
