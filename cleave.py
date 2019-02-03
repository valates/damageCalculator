from attack_modifier import AttackModifier

class Cleave(AttackModifier):

	CLEAVE_EFFECT_NAME = "cleave"

	@abstractmethod #TODO
	def __init__(self, cleave_percent):
		self.cleave_percent = cleave_percent

	def get_effect(self):
		return self.cleave_percent

	def get_effect_type(self):
		return CLEAVE_EFFECT_NAME