from magical_damage import MagicalDamage
from percentage import Percentage
from physical_damage import PhysicalDamage
from pure_damage import PureDamage

class ConditionalProc():

	DAMAGE_TYPES = ['physical', 'magical', 'pure']

	def __init__(self, proc_damage, proc_chance, proc_type):
		assert isinstance(proc_chance, Percentage)
		assert isinstance(proc_damage, int) or isinstance(proc_damage, float)
		assert isinstance(proc_type, str) and proc_type in ConditionalProc.DAMAGE_TYPES
		self.proc_chance = proc_chance
		self.proc_damage = proc_damage
		self.proc_type = proc_type

	def get_expected_damage(self):
		return self.proc_damage * self.proc_chance.get_percentage_multiple()

	def get_conditional_expected_damage_instance(self):
		expected_damage = self.get_expected_damage()
		if self.proc_type == ConditionalProc.DAMAGE_TYPES[0]:
			return PhysicalDamage(expected_damage)
		elif self.proc_type == ConditionalProc.DAMAGE_TYPES[1]:	
			return MagicalDamage(expected_damage)
		elif self.proc_type == ConditionalProc.DAMAGE_TYPES[2]:
			return PureDamage(expected_damage)