
import hashlib

class UrlBuilder:
	def __init__(self, securitySalt, bbbServerBaseUrl):
		self.securitySalt 		= securitySalt
		self.bbbServerBaseUrl 	= bbbServerBaseUrl
	def buildUrl(self, method="", params="", append=True):
		'Builds an API method URL that includes the url + params + its generated checksum.'
		return "{}api/{}{}".format(self.bbbServerBaseUrl, method, self.buildQs(method, params) if append else "")
	def buildQs(self, method, params):
		'Builds a query string for an API method URL that includes the params + its generated checksum.'
		return "{}&checksum={}".format(params, hashlib.sha1("{}{}{}".format(method, params, self.securitySalt)))