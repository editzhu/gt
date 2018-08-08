import tornado.ioloop
import tornado.web
import urllib
import json
import os

from __init__ import detector

class FileUploadHandler(tornado.web.RequestHandler):
    def post(self):
        file_metas = self.request.files.get('image', None)
        if not file_metas:
            self.finish({'res':1003})

        for meta in file_metas:
            filename = meta['filename']

            img_string = meta['body']
            img_string = img_string.rstrip('\n')
            my_answer = detector.infer(img_string)#not decode base 64
            # return result
            post_data = {'res':0, 'detector_results':my_answer}
            body = urllib.urlencode(post_data)
            self.finish(post_data)

def make_app():
    return tornado.web.Application([
        (r"/scan/", FileUploadHandler)
    ])

if __name__ == "__main__":
    app = make_app()

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
