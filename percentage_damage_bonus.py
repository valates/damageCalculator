from percentage import Percentage

class PercentageDamageBonus():

	def __init__(self, percentage_bonus):
		assert isinstance(percentage_bonus, Percentage)
		self.bonus = percentage_bonus

	def get_bonus(self):
		return self.bonus.get_percentage_multiple()

	def get_bonus_as_percentage(self):
		return self.bonus