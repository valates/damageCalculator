from attack_modifier import AttackModifier
from magical_damage import MagicalDamage

class Manabreak(AttackModifier):

	def __init__(self, mana_burn):
		assert isinstance(mana_burn, int) or isinstance(mana_burn, float)
		self.mana_burn = round(mana_burn)

	def get_effect(self):
		return MagicalDamage(self.mana_burn)