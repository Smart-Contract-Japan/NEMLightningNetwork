'''
Distributed under the MIT License, see accompanying file LICENSE.txt
'''
import tornado.gen
import json
import re
import tornado.websocket
import collections
import zlib
from itertools import izip_longest
import time
from binascii import hexlify, unhexlify
from NemConnect import NemConnect
from Account import Account

class ChannelHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self, privkey, cosignatoriesJSON): # cosignatoriesJSON should be a json array
		# response = yield self.api.getBlocksAfter(int(self.get_argument('height')))
		# self.write(response.body)

		c = NemConnect('bigalice3.nem.ninja', 7890)
		a = Account(privkey)
		cosignatories = json.loads(cosignatoriesJSON)
		print " [+] PREPARING MULTISIG CREATE"
		ok, j = c.multisigCreatePrepare(a.getHexPublicKey(), cosignatories)

		print ok, j

		self.write("created ms account for " + account1 + " and " + account2) #TODO: do it for real
		self.finish()
		
class TransactionHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		response = yield self.api.getBlocksAfter(int(self.get_argument('height')))
		self.write(response.body)
		self.finish()


