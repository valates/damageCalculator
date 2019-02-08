from percentage import Percentage

class Hero():
	def __init__(self, hero_metadata):
		self.agility = hero_metadata["agility"]
		self.agility_gain = hero_metadata["agility gain"]
		self.base_attack_max = hero_metadata["attack max"] #Factors in level 1 primary attribute
		self.base_attack_min = hero_metadata["attack min"] #Factors in level 1 primary attribute
		self.base_attack_time = hero_metadata["BAT"]
		self.base_magic_resistance = Percentage(hero_metadata["base magic resist"])
		self.base_regen = hero_metadata["base regen"] #DOES NOT include regen due to STR
		self.hero_name = hero_metadata["hero name"]
		self.intelligence = hero_metadata["intelligence"]
		self.intelligence_gain = hero_metadata["intelligence_gain"]
		self.primary_attr = hero_metadata["primary attr"]
		self.starting_armor = hero_metadata["starting_armor"] #Factors in base armor AND armor gained from agility
		self.strength = hero_metadata["strength"]
		self.strength_gain = hero_metadata["strength gain"]

	def get_hero_name(self):
		return self.hero_name

	def get_primary_attr(self):
		return self.primary_attr

	def get_strength(self):
		return self.strength

	def get_strength_gain(self):
		return self.strength_gain

	def get_agility(self):
		return self.agility

	def get_agility_gain(self):
		return self.agility_gain

	def get_intelligence(self):
		return self.intelligence

	def get_intelligence_gain(self):
		return self.intelligence_gain

	def get_base_armor(self):
		return self.starting_armor

	def get_base_attack_min(self):
		return self.base_attack_min

	def get_base_attack_max(self):
		return self.base_attack_max

	def get_expected_attack_damage(self):
		return (self.base_attack_min + self.base_attack_max) / 2

	def base_regen(self):
		return self.base_regen

	def get_base_magic_resistance(self):
		return self.base_magic_resistance

	def get_base_attack_time(self):
		return self.base_attack_time