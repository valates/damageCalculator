from attack_modifier import AttackModifier
from percentage import Percentage

class CriticalStrike(AttackModifier):

	def __init__(self, crit_chance, crit_multiplier):
		assert isinstance(crit_chance, Percentage)
		assert isinstance(crit_multiplier, Percentage)
		self.crit_chance = crit_chance
		self.crit_multiplier = crit_multiplier

	def get_effect(self):
		return [self.crit_chance, self.crit_damage]

	def get_average_dps_increase(self):
		return self.crit_chance.get_percentage_multiple() * self.crit_multiplier.get_percentage_multiple()

	def get_specified_dps_increase(self, proc_percentage):
		assert isinstance(proc_percentage, Percentage)
		return proc_percentage.get_percentage_multiple() * self.crit_multiplier.get_percentage_multiple()
		