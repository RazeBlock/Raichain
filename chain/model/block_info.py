from chain.model.chain import SearchChain 
from chain.model.rai_raw import raw_rai

class Block:

	def __init__(self, block_hash):
		account = SearchChain({"action": "block_account", "hash": block_hash})
		self.account = account.info['account']
		self.hash = block_hash

	def get_info(self):
		command = { "action": "block", "hash": self.hash }
		block = SearchChain(command)
		return block.info
