from percentage import Percentage

STRENGTH_MAGIC_RESISTANCE_PERCENT_MULTIPLIER = Percentage("0.08%")

def get_total_magic_resistance(base_magic_resistance, strength, magic_resistances):
	"""
	>>> zero_percent = Percentage("0%")
	>>> get_total_magic_resistance(zero_percent, 0, [])
	0.0
	>>> get_total_magic_resistance(zero_percent, 100, []) #100 strength ==> 8% spell resistance from strength
	0.08
	>>> base_hero_resistance = Percentage("25%")
	>>> level_four_counterspell_resistance = Percentage("45%")
	>>> cloak_resistance = Percentage("15%")
	>>> get_total_magic_resistance(base_hero_resistance, 0, [level_four_counterspell_resistance, cloak_resistance])
	0.65
	>>> get_total_magic_resistance(base_hero_resistance, 54, [level_four_counterspell_resistance, cloak_resistance]) #Verified in game value with level 25 AM no items
	0.66
	>>> get_total_magic_resistance(base_hero_resistance, 0, [level_four_counterspell_resistance, cloak_resistance, 5, 7, 'a', None])
	0.65
	"""
	assert isinstance(base_magic_resistance, Percentage)
	assert isinstance(strength, int) or isinstance(strength, float)
	total_magic_resistance = (1 - base_magic_resistance.get_percentage_multiple()) * (1 - strength * STRENGTH_MAGIC_RESISTANCE_PERCENT_MULTIPLIER.get_percentage_multiple())
	for resistance in magic_resistances:
		#Simply no-op if the list has a non-percentage object in it
		if isinstance(resistance, Percentage):
			resistance_percentage_multiple = resistance.get_percentage_multiple()
			assert resistance_percentage_multiple <= 1.0
			total_magic_resistance *= (1 - resistance_percentage_multiple)
	#In game magic resistance is expressed as integer percentages, so we don't go beyond 2 significant digits for our multiplier
	return round((1 - total_magic_resistance), 2)

def effect_hp_against_magic(health, base_magic_resistance, strength, magic_resistances):
	"""
	#The below are all benchmark examples double checked against the wiki
	>>> zero_percent = Percentage("0%")
	>>> effect_hp_against_magic(1000, zero_percent, 0, [])
	1000
	>>> imaginary_percent = Percentage("10%")
	>>> effect_hp_against_magic(1000, zero_percent, 0, [imaginary_percent])
	1111
	>>> imaginary_percent = Percentage("25%")
	>>> effect_hp_against_magic(1000, zero_percent, 0, [imaginary_percent])
	1333
	>>> imaginary_percent = Percentage("50%")
	>>> effect_hp_against_magic(1000, zero_percent, 0, [imaginary_percent])
	2000
	>>> imaginary_percent = Percentage("75%")
	>>> effect_hp_against_magic(1000, zero_percent, 0, [imaginary_percent])
	4000
	>>> imaginary_percent = Percentage("100%")
	>>> effect_hp_against_magic(1000, zero_percent, 0, [imaginary_percent])
	inf
	>>> imaginary_percent = Percentage("-10%")
	>>> effect_hp_against_magic(1000, zero_percent, 0, [imaginary_percent])
	909
	>>> imaginary_percent = Percentage("-25%")
	>>> effect_hp_against_magic(1000, zero_percent, 0, [imaginary_percent])
	800
	>>> imaginary_percent = Percentage("-50%")
	>>> effect_hp_against_magic(1000, zero_percent, 0, [imaginary_percent])
	666
	>>> imaginary_percent = Percentage("-75%")
	>>> effect_hp_against_magic(1000, zero_percent, 0, [imaginary_percent])
	571
	>>> imaginary_percent = Percentage("-100%")
	>>> effect_hp_against_magic(1000, zero_percent, 0, [imaginary_percent])
	500
	"""
	assert isinstance(health, int)
	total_magic_resistance = get_total_magic_resistance(base_magic_resistance, strength, magic_resistances)
	if (total_magic_resistance == 1):
		return float("inf")
	#Dota never expresses health as a non-integer so we cast
	return (int) (health / (1 - get_total_magic_resistance(base_magic_resistance, strength, magic_resistances)))

def get_armor_damage_multiplier(armor):
	"""
	#The below are all benchmark examples double checked against the wiki
	>>> round(get_armor_damage_multiplier(-5), 3)
	1.228
	>>> round(get_armor_damage_multiplier(-10), 3)
	1.377
	>>> round(get_armor_damage_multiplier(-20), 3)
	1.559
	>>> round(get_armor_damage_multiplier(-40), 3)
	1.738
	>>> round(get_armor_damage_multiplier(-60), 3)
	1.825
	>>> round(get_armor_damage_multiplier(0), 3)
	1.0
	>>> round(get_armor_damage_multiplier(5), 3)
	0.772
	>>> round(get_armor_damage_multiplier(10), 3)
	0.623
	>>> round(get_armor_damage_multiplier(20), 3)
	0.441
	>>> round(get_armor_damage_multiplier(40), 3)
	0.262
	>>> round(get_armor_damage_multiplier(60), 3)
	0.175
	"""
	assert isinstance(armor, int) or isinstance(armor, float)
	return (1 - ((0.052 * armor) / (0.9 + 0.048 * abs(armor))))

def effect_hp_against_physical(health, armor):
	"""
	#The below are all benchmark examples double checked against the wiki
	>>> effect_hp_against_physical(1000, -40)
	575
	>>> effect_hp_against_physical(1000, -30)
	600
	>>> effect_hp_against_physical(1000, -20)
	641
	>>> effect_hp_against_physical(1000, -10)
	726
	>>> effect_hp_against_physical(1000, 0)
	1000
	>>> effect_hp_against_physical(1000, 10)
	1604
	>>> effect_hp_against_physical(1000, 20)
	2268
	>>> effect_hp_against_physical(1000, 30)
	3000
	>>> effect_hp_against_physical(1000, 40)
	3810
	"""
	assert isinstance(health, int)
	return (int) (round((health / get_armor_damage_multiplier(armor)), 1))

if __name__ == "__main__":
    import doctest
    doctest.testmod()