from attack_modifier import AttackModifier

class Lifesteal(AttackModifier):

	LIFESTEAL_EFFECT_NAME = "lifesteal"

	@abstractmethod #TODO
	def __init__(self, lifesteal_percent):
		self.lifesteal_percent = lifesteal_percent

	def get_effect(self):
		return self.lifesteal_percent.get_percentage_multiple()

	def get_effect_type(self):
		return LIFESTEAL_EFFECT_NAME