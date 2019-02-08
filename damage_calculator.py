"""
Damage =
{ [Main Damage × (1 + Σ Percentage Bonuses) + Flat Bonuses]
× Crit Multiplier - Blocked Damage }
× Armor Multipliers
× General Damage Multipliers (bristle passive, centaur ult)
"""

from critical_strike import CriticalStrike
from damage_block import DamageBlock
from effective_hp import get_armor_damage_multiplier, get_total_magic_resistance
from flat_damage_bonus import FlatDamageBonus
from magical_damage import MagicalDamage
from percentage import Percentage
from percentage_damage_bonus import PercentageDamageBonus
from physical_damage import PhysicalDamage
from pure_damage import PureDamage

def calculate_total_damage(damage_sources, 
							attacker_percentage_bonuses, 
							attacker_flat_bonuses, 
							attacker_crit_sources, 
							attacker_spell_amp_sources,
							defender_block_sources, 
							defender_armor, 
							defender_evasion_quantities, 
							defender_base_magic_resistance, 
							defender_strength, 
							defender_magic_resistances, 
							defender_spell_shield_quantities, 
							general_damage_multipliers):
	"""
	>>> pure_damage = PureDamage(5000)
	>>> damages = [pure_damage]
	>>> zero_percent = Percentage("0%")
	>>> calculate_total_damage(damages, [], [], [], [], 0, zero_percent, 1000, [], [])
	5000
	"""
	assert isinstance(damage_sources, list)


	physical_damages = [damage_source for damage_source in damage_sources if isinstance(damage_source, PhysicalDamage)]
	if len(physical_damages) > 0:
		phyical_damage_after_multipliers = calculate_physical_damage(physical_damages,
																		attacker_percentage_bonuses, 
																		attacker_flat_bonuses, 
																		attacker_crit_sources,
																		defender_block_sources, 
																		defender_armor, 
																		defender_evasion_quantities,
																		general_damage_multipliers)
	else: 
		phyical_damage_after_multipliers = 0

	magical_damages = [damage_source for damage_source in damage_sources if isinstance(damage_source, MagicalDamage)]
	if len(magical_damages) > 0:
		magical_damage_after_multipliers = calculate_magical_damage(magical_damages,
																		attacker_spell_amp_sources,
																		defender_base_magic_resistance, 
																		defender_strength,
																		defender_magic_resistances,
																		defender_spell_shield_quantities)
	else:
		magical_damage_after_multipliers = 0

	pure_damage = 0
	pure_damages = [damage_source for damage_source in damage_sources if isinstance(damage_source, PureDamage)]
	for pure_damage_source in pure_damages:
		pure_damage += pure_damage_source.get_damage_quantity()

	return int((phyical_damage_after_multipliers + magical_damage_after_multipliers + pure_damage))


def calculate_physical_damage(damage_sources, 
								attacker_percentage_bonuses, 
								attacker_flat_bonuses, 
								attacker_crit_sources, 
								defender_block_sources, 
								defender_armor,
								defender_evasion_quantities, 
								general_damage_multipliers):
	"""
	>>> damage1 = PhysicalDamage(49)
	>>> damage2 = PhysicalDamage(51)
	>>> damages = [damage1, damage2]
	>>> calculate_physical_damage(damages, [], [], [], [], 0, [])
	100
	>>> calculate_physical_damage(damages, [], [], [], [], -60, [])
	183
	>>> calculate_physical_damage(damages, [], [], [], [], 60, [])
	17
	>>> hundred_percent = Percentage("100%")
	>>> hundred_percent_bonus_damage = PercentageDamageBonus(hundred_percent)
	>>> calculate_physical_damage(damages, [hundred_percent_bonus_damage], [], [], [], -60, [])
	365
	>>> ten_percent = Percentage("10%")
	>>> ten_bonus_damage = PercentageDamageBonus(ten_percent)
	>>> calculate_physical_damage(damages, [ten_bonus_damage], [], [], [], -60, [])
	201
	>>> flat_bonus1 = FlatDamageBonus(13)
	>>> flat_bonus2 = FlatDamageBonus(7)
	>>> flat_bonuses = [flat_bonus1, flat_bonus2]
	>>> calculate_physical_damage(damages, [], flat_bonuses, [], [], 0, [])
	120
	>>> calculate_physical_damage(damages, [hundred_percent_bonus_damage], flat_bonuses, [], [], 0, [])
	220
	>>> always_blocker = DamageBlock(20, hundred_percent)
	>>> calculate_physical_damage(damages, [], [], [], [always_blocker], 0, [])
	80
	>>> calculate_physical_damage(damages, [], flat_bonuses, [], [always_blocker], 0, [])
	100
	>>> fake_bristle = Percentage("50%")
	>>> calculate_physical_damage(damages, [], [], [], [], 0, [fake_bristle])
	50
	>>> calculate_physical_damage(damages, [], [], [], [always_blocker], 0, [fake_bristle])
	40
	>>> fifty_percent = Percentage("50%")
	>>> half_blocker = DamageBlock(20, fifty_percent)
	>>> calculate_physical_damage(damages, [], [], [], [half_blocker], 0, [])
	90
	>>> half_blocker2 = DamageBlock(40, fifty_percent)
	>>> two_hundred_percent = Percentage("200%")
	>>> crit_chance = CriticalStrike(hundred_percent, two_hundred_percent) 
	>>> calculate_physical_damage(damages, [hundred_percent_bonus_damage], flat_bonuses, [crit_chance], [always_blocker], 0, [fake_bristle])
	205
	"""
	assert isinstance(damage_sources, list)
	assert isinstance(attacker_percentage_bonuses, list)
	assert isinstance(attacker_flat_bonuses, list)
	assert isinstance(attacker_crit_sources, list)
	assert isinstance(defender_block_sources, list)
	assert isinstance(defender_armor, int) or isinstance(defender_armor, float)
	assert isinstance(general_damage_multipliers, list)

	damage_source_sum = 0
	for damage_source in damage_sources:
		damage_source_sum += damage_source.get_damage_quantity()

	percentage_bonuses_sum = 0
	for percent_bonus in attacker_percentage_bonuses:
		if isinstance(percent_bonus, PercentageDamageBonus):
			percentage_bonuses_sum += percent_bonus.get_bonus()

	flat_bonus_sum = 0
	for flat_bonus in attacker_flat_bonuses:
		if isinstance(flat_bonus, FlatDamageBonus):
			flat_bonus_sum += flat_bonus.get_bonus()

	physical_damage = (damage_source_sum * (1 + percentage_bonuses_sum)) + flat_bonus_sum

	#TODO block and crit logic for multiple sources
	if len(attacker_crit_sources) > 0:
		physical_damage *= attacker_crit_sources[0].get_average_dps_increase() #Placeholder, this logic makes no sense when we do multi-crit source scenarioes

	if len(defender_block_sources) > 0:	
		physical_damage -= defender_block_sources[0].get_expected_damage_block() #Placeholder, makes no sense in multi block scenarios

	physical_damage = 0 if physical_damage < 0 else physical_damage #Verified in game that when damage block > damage of attacker it sets to 0

	#Multiply by armor factor
	physical_damage *= get_armor_damage_multiplier(round(defender_armor))

	#Factor in general damage multipliers
	for damage_multiplier in general_damage_multipliers:
		if isinstance(damage_multiplier, Percentage):
			physical_damage *= damage_multiplier.get_percentage_multiple()

	evasion_stacking_result = 1
	for evasion_source in defender_evasion_quantities:
		evasion_stacking_result *= (1 - evasion_source.get_percentage_multiple())

	#Rather than speculating on odds of missing, we use expected values to use evasion with our damage
	return round(physical_damage * evasion_stacking_result)

def calculate_magical_damage(damage_sources, 
								attacker_spell_amp_sources, 
								defender_base_magic_resistance, 
								defender_strength, 
								defender_magic_resistances, 
								defender_spell_shield_quantities):
	"""
	>>> magical_damage1 = MagicalDamage(49)
	>>> magical_damage2 = MagicalDamage(51)
	>>> magical_damages = [magical_damage1, magical_damage2]
	>>> zero_percent = Percentage("0%")
	>>> calculate_magical_damage(magical_damages, zero_percent, 0, [])
	100
	>>> calculate_magical_damage(magical_damages, zero_percent, 100, []) #100 strength ==> 8% spell resistance from strength
	92
	>>> base_hero_resistance = Percentage("25%")
	>>> level_four_counterspell_resistance = Percentage("45%")
	>>> cloak_resistance = Percentage("15%")
	>>> calculate_magical_damage(magical_damages, base_hero_resistance, 0, [level_four_counterspell_resistance, cloak_resistance])
	35
	"""
	assert isinstance(damage_sources, list)
	assert isinstance(defender_base_magic_resistance, Percentage)
	assert isinstance(defender_strength, int) or isinstance(defender_strength, float)
	assert isinstance(defender_magic_resistances, list)

	magic_damage = 0
	for damage_source in damage_sources:
		magic_damage += damage_source.get_damage_quantity()

	spell_amp_multiplier_sum = 1
	for spell_amp in attacker_spell_amp_sources:
		spell_amp_multiplier_sum += spell_amp.get_percentage_multiple()

	magic_damage *= spell_amp_multiplier_sum

	for spell_shield in defender_spell_shield_quantities:
		magic_damage -= spell_shield

	if magic_damage < 0:
		magic_damage = 0

	return round(magic_damage * (1 - get_total_magic_resistance(defender_base_magic_resistance,
																defender_strength,
																defender_magic_resistances)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()