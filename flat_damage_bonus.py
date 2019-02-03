class FlatDamageBonus():
	#A flat bonus can be POSITIVE OR NEGATIVE (static link)

	def __init__(self, flat_bonus):
		assert(isinstance(flat_bonus, int))
		self.bonus = flat_bonus

	def get_bonus(self):
		return self.bonus