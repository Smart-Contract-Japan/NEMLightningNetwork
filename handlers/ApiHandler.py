'''
Distributed under the MIT License, see accompanying file LICENSE.txt
'''
import tornado.gen
import ujson
import re
import tornado.websocket
import collections
import zlib
from itertools import izip_longest
import time

class ChannelHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		response = yield self.api.getBlocksAfter(int(self.get_argument('height')))
		self.write(response.body)
		self.finish()
		
class TransactionHandler(tornado.web.RequestHandler):
	def get(self):
		self.write(zlib.decompress(self.redis_client.zrange('blocks', 0, 2, 'desc')[0]))
		self.finish()
