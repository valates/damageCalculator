from percentage import Percentage

class DamageBlock():
	#If two instances of damage block both proc, the one with the higher block value takes priority
	#TODO logic for probability table with the procs

	def __init__(self, block_amount, block_chance):
		assert isinstance(block_amount, int)
		assert isinstance(block_chance, Percentage)
		self.block_amount = block_amount
		self.block_chance = block_chance

	def get_block_amount(self):
		return self.block_amount

	def get_block_chance(self):
		return self.block_chance

	def get_expected_damage_block(self):
		return self.get_damage_block_with_chosen_proc_chance(self.block_chance)

	def get_pessimistic_damage_block(self):
		#If we assume 100% of our attacks proc the block on the defender
		return self.block_amount

	def get_damage_block_with_chosen_proc_chance(self, percentage_proced):
		#If we assume X% of our attacks proc the block on the defender,
		#where X is provided by the requester
		assert isinstance(percentage_proced, Percentage)
		return (int) (self.block_amount * percentage_proced.get_percentage_multiple())