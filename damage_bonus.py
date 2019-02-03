from abc import ABC, abstractmethod

class DamageBonus(ABC):

	@abstractmethod
	def __init__(self, bonus):
		pass

	@abstractmethod
	def get_bonus(self):
		pass