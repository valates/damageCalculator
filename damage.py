from abc import ABC, abstractmethod

class Damage(ABC):

	@abstractmethod
	def __init__(self, damage_amount):
		assert isinstance(damage_amount, int) or isinstance(damage_amount, float)
		self.damage_amount = round(damage_amount)

	def get_damage_quantity(self):
		return self.damage_amount