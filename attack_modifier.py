from abc import ABC, abstractmethod

class AttackModifier(ABC):

	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def get_effect(self):
		pass