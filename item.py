from conditional_proc import ConditionalProc
from critical_strike import CriticalStrike
from manabreak import Manabreak
from percentage import Percentage
from percentage_damage_bonus import PercentageDamageBonus

class Item():

	def __init__(self, item_metadata):
		self.agility = item_metadata["agility"] if "agility" in item_metadata else 0
		self.armor = item_metadata["armor"] if "armor" in item_metadata else 0
		self.armor_of_target = item_metadata["armor of target"] if "armor of target" in item_metadata else 0
		self.attack_range = 0
		self.attack_speed = item_metadata["attack speed"] if "attack speed" in item_metadata else 0
		self.cast_range_extension = 0
		if "conditional proc" in item_metadata:
			conditional_data = item_metadata["conditional proc"]
			self.conditional_proc = ConditionalProc(conditional_data["proc damage"], Percentage(conditional_data["proc chance"]), conditional_data["proc damage type"])
		else:3
			self.conditional_proc = ConditionalProc(0, Percentage("0"), "physical")
		self.critical_strike = CriticalStrike(Percentage("0"), Percentage("0"))
		self.damage = item_metadata["damage"] if "damage" in item_metadata else 0
		self.damage_percentage_boost = PercentageDamageBonus(Percentage((item_metadata["damage percent bonus"] if "damage percent bonus" in item_metadata else "0")))
		self.evasion = Percentage((item_metadata["evasion"] if "evasion" in item_metadata else "0"))
		self.healing_boost = Percentage("0")
		self.health = 0
		self.health_regen = 0
		self.health_regen_boost = Percentage("0")
		self.intelligence = item_metadata["intelligence"] if "intelligence" in item_metadata else 0
		self.is_ethereal = item_metadata["is ethereal"] if "is ethereal" in item_metadata else False
		self.lifesteal = Percentage("0")
		self.lifesteal = Percentage("0")
		self.magic_barrier = item_metadata["magic barrier"] if "magic barrier" in item_metadata else 0
		self.magic_burst = item_metadata["magic burst"] if "magic burst" in item_metadata else 0
		self.magic_resistance = Percentage(item_metadata["magic resist"]) if "magic resist" in item_metadata else Percentage("0")
		self.mana = 0
		self.mana_loss_reduction = Percentage("0")
		self.mana_regen = 0
		self.mana_regen_boost = Percentage("0")
		self.manabreak = Manabreak((item_metadata["manabreak"] if "manabreak" in item_metadata else 0))
		self.max_health_change_per_second = Percentage("0")
		self.move_speed_boost = 0
		self.move_speed_percentage_boost = Percentage("0")
		self.physical_burst = item_metadata["physical burst"] if "physical burst" in item_metadata else 0
		self.spell_amp = Percentage((item_metadata["spell amp"] if "spell amp" in item_metadata else "0"))
		self.spell_lifesteal = Percentage("0")
		self.status_resistance = Percentage("0")
		self.strength = item_metadata["strength"] if "strength" in item_metadata else 0
		self.target_ethereal = item_metadata["target ethereal"] if "target ethereal" in item_metadata else False
		self.target_magic_resist = Percentage((item_metadata["target magic resist"] if "target magic resist" in item_metadata else "0"))

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

	def get_manabreak(self):
		return self.manabreak.get_effect()

	def get_is_ethereal(self):
		return self.is_ethereal

	def get_target_ethereal(self):
		return self.target_ethereal

	def get_target_magic_resist(self):
		return self.target_magic_resist

	def get_magic_burst(self):
		return self.magic_burst

	def get_physical_burst(self):
		return self.physical_burst
		
	def get_magic_barrier(self):
		return self.magic_barrier

	def get_spell_amp(self):
		return self.spell_amp

	def get_evasion(self):
		return self.evasion

	def get_conditional_proc(self):
		return self.conditional_proc

	def get_damage_percentage_boost(self):
		return self.damage_percentage_boost 