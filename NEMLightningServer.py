'''
Distributed under the MIT License, see accompanying file LICENSE.txt
'''
import tornado.web
import tornado.httpserver 
import tornado.ioloop 
import tornado.options
import tornado.locale 
import os.path

from ConfigParser import SafeConfigParser
from tornado.options import define, options

#api
from handlers.ApiHandler import BlockAfterHandler


parser = SafeConfigParser()
parser.read("settings.INI")

define("port", default=parser.get("blockexplorer", "port"), help="run on the given port", type=int)

if __name__ == '__main__':

    tornado.options.parse_command_line()

    settings = {
        "template_path": os.path.join(os.path.dirname(__file__), "templates"), 
        "static_path" : os.path.join(os.path.dirname(__file__), 'static'),
        "cookie_secret": "doEx8QhSQv+CUoZjKDevtL/5VODeEkUFgbWyv7PO0O4", #define your own here !
        "xsrf_cookies": True,
        "debug": False,
        "gzip":True,
    }

    #define the url endpoints
    app = tornado.web.Application(
        [        
         #apis
         #initiate channel
         (r'/api/block-after', ChannelHandler),

         #send transaction
         (r'/api/block-after', TransactionHandler),
         
        ], 
        **settings
    )
    
    server = tornado.httpserver.HTTPServer(app, xheaders=True) 
    server.bind(options.port, '127.0.0.1')
    print "port: ", options.port
    server.start()
    
    tornado.ioloop.IOLoop.instance().start()
