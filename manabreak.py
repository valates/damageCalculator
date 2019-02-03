from attack_modifier import AttackModifier

class Manabreak(AttackModifier):

	MANABREAK_EFFECT_NAME = "manabreak"

	@abstractmethod #TODO
	def __init__(self, mana_burn):
		self.mana_burn

	def get_effect(self):
		return self.mana_burn

	def get_effect_type(self):
		return MANABREAK_EFFECT_NAME