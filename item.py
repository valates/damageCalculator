from percentage import Percentage
from critical_strike import CriticalStrike

class Item():

	def __init__(self, item_metadata):
		self.armor = item_metadata["armor"] if "armor" in item_metadata else 0
		self.damage = item_metadata["damage"] if "damage" in item_metadata else 0
		self.health = 0
		self.mana = 0
		self.evasion = Percentage("0")
		self.attack_speed = item_metadata["attack speed"] if "attack speed" in item_metadata else 0
		self.strength = item_metadata["strength"] if "strength" in item_metadata else 0
		self.agility = item_metadata["agility"] if "agility" in item_metadata else 0
		self.intelligence = item_metadata["intelligence"] if "intelligence" in item_metadata else 0
		self.move_speed_percentage_boost = Percentage("0")
		self.move_speed_boost = 0
		self.health_regen = 0
		self.mana_regen = 0
		self.magic_resistance = Percentage(item_metadata["magic resist"]) if "magic resist" in item_metadata else Percentage("0")
		self.lifesteal = Percentage("0")
		self.armor_of_target = item_metadata["armor of target"] if "armor of target" in item_metadata else 0
		self.spell_amp = Percentage("0")
		self.lifesteal = Percentage("0")
		self.healing_boost = Percentage("0")
		self.health_regen_boost = Percentage("0")
		self.attack_range = 0
		self.mana_regen_boost = Percentage("0")
		self.critical_strike = CriticalStrike(Percentage("0"), Percentage("0"))
		self.status_resistance = Percentage("0")
		self.mana_loss_reduction = Percentage("0")
		self.spell_lifesteal = Percentage("0")
		self.cast_range_extension = 0
		self.magic_barrier = 0
		self.magic_burst = 0
		self.max_health_change_per_second = Percentage("0")
		self.physical_burst = 0
		self.mana_break = None #TODO mana break implementation
		self.is_ethereal = False
		self.target_ethereal = False
		self.conditional_proc = None #TODO CONDITIONAL PROC OBJECT

	def get_armor(self):
		return self.armor

	def get_damage(self):
		return self.damage

	def get_magic_resistance(self):
		return self.magic_resistance

	def get_strength(self):
		return self.strength

	def get_agility(self):
		return self.agility

	def get_intelligence(self):
		return self.intelligence

	def get_armor_of_target(self):
		return self.armor_of_target