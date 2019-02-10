from central import Central
from ui_unit_test_injector import UIUnitTestInjector
import tkinter

def test_empty_initalization():
	"""
	>>> damage = test_empty_initalization()
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	0
	>>> damage
	0
	"""
	injector = UIUnitTestInjector("", "", "", "", [], [], "", "", "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_hero_choice_initalization_attacker_only():
	"""
	>>> damage = test_hero_choice_initalization_attacker_only()
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage
	60
	"""
	injector = UIUnitTestInjector("Bloodseeker", "", "", "", [], [], "", "", "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_hero_choice_initalization_defender_only():
	"""
	>>> damage = test_hero_choice_initalization_defender_only()
	Injecting unit test values in Central object
	Placeholder attacking Phantom Assassin...
	0
	>>> damage
	0
	"""
	injector = UIUnitTestInjector("", "Phantom Assassin", "", "", [], [], "", "", "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_hero_choice_initalization_both():
	"""
	>>> damage = test_hero_choice_initalization_both()
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	47
	>>> damage
	47
	"""
	injector = UIUnitTestInjector("Bloodseeker", "Phantom Assassin", "", "", [], [], "", "", "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_bad_hero_names_sanitized():
	"""
	>>> damage = test_bad_hero_names_sanitized()
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	0
	>>> damage
	0
	"""
	injector = UIUnitTestInjector("acrslnvciw3ina", "fac4soexuntcl", "", "", [], [], "", "", "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_hero_level_scaling(attacker_level, defender_level):
	"""
	>>> damage = test_hero_choice_initalization_both()
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	47
	>>> damage
	47
	>>> damage = test_hero_level_scaling("1", "1")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	47
	>>> damage
	47
	>>> damage = test_hero_level_scaling("1", "1")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	47
	>>> damage
	47
	>>> damage = test_hero_level_scaling("5", "1")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	58
	>>> damage
	58
	>>> damage = test_hero_level_scaling("17", "1")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	91
	>>> damage
	91
	>>> damage = test_hero_level_scaling("17", "11")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	71
	>>> damage
	71
	>>> damage = test_hero_level_scaling("17", "25")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	53
	>>> damage
	53
	"""
	injector = UIUnitTestInjector("Bloodseeker", "Phantom Assassin", attacker_level, defender_level, [], [], "", "", "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_default_level_values_round_to_one():
	"""
	>>> damage1 = test_hero_level_scaling("1", "1")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	47
	>>> damage1
	47
	>>> damage2 = test_hero_level_scaling("1", "1")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	47
	>>> damage1 == damage2
	True
	"""
	injector = UIUnitTestInjector("Bloodseeker", "Phantom Assassin", Central.HERO_LEVEL_DEFAULT, Central.HERO_LEVEL_DEFAULT, [], [], "", "", "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_bad_level_input_sanitized():
	"""
	>>> damage = test_bad_level_input_sanitized()
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	47
	>>> damage
	47
	"""
	injector = UIUnitTestInjector("Bloodseeker", "Phantom Assassin", "-7", "awxcesvtdb", [], [], "", "", "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_percent_bonus(percent_bonus):
	"""
	>>> damage = test_hero_choice_initalization_both()
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	47
	>>> damage = test_percent_bonus("0")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	47
	>>> damage = test_percent_bonus("5%")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	49
	>>> damage = test_percent_bonus("5")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	49
	>>> damage = test_percent_bonus("5.0")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	49
	>>> damage = test_percent_bonus("5.0%")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	49
	>>> damage = test_percent_bonus("5.0%,17.9,26%")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	70
	>>> damage = test_percent_bonus("x,5.0%,17.9,26%")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	<BLANKLINE>
	Invalid percentage given: x. Skipping over value.
	70
	"""
	injector = UIUnitTestInjector("Bloodseeker", "Phantom Assassin", "", "", [], [], percent_bonus, "", "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_percent_stacking_values(percent_bonus):
	"""
	>>> damage = test_percent_stacking_values("0,0,0,0,0,0,0")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> test_percent_stacking_values("1,1,1,1,1") == test_percent_stacking_values("5")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	63
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	63
	True
	>>> damage = test_percent_stacking_values("1,2,3,4")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	66
	>>> damage = test_percent_stacking_values("100, 100, 100, 100, 100")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	360
	>>> damage = test_percent_stacking_values("-100") #Negative attacker percentages do not exist and are banned
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_percent_stacking_values("-1")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_percent_stacking_values("-1000")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	"""
	injector = UIUnitTestInjector("Bloodseeker", "", "", "", [], [], percent_bonus, "", "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_flat_bonus(flat_damage):
	"""
	>>> damage = test_hero_choice_initalization_both()
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	47
	>>> damage = test_flat_bonus("0")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	47
	>>> damage = test_flat_bonus("21")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	63
	>>> damage = test_flat_bonus("21, 21")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	80
	>>> damage = test_flat_bonus("21, 21,")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	80
	>>> damage = test_flat_bonus(",21, 21,")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	80
	>>> damage = test_flat_bonus("x")
	Injecting unit test values in Central object
	Bloodseeker attacking Phantom Assassin...
	<BLANKLINE>
	Invalid integer given: x. Skipping over value.
	47
	"""
	injector = UIUnitTestInjector("Bloodseeker", "Phantom Assassin", "", "", [], [], "", flat_damage, "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_percentage_bonus_affects_primary_stat_but_not_flat_bonus(hero_level, percentage_bonus, flat_bonus):
	"""
	>>> damage = test_percentage_bonus_affects_primary_stat_but_not_flat_bonus("0", "0", "0")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_percentage_bonus_affects_primary_stat_but_not_flat_bonus("2", "0", "0")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	64
	>>> damage = test_percentage_bonus_affects_primary_stat_but_not_flat_bonus("2", "100", "0")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	127
	>>> damage = test_percentage_bonus_affects_primary_stat_but_not_flat_bonus("2", "", "14")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	78
	>>> damage = test_percentage_bonus_affects_primary_stat_but_not_flat_bonus("2", "100", "14")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	141
	"""
	injector = UIUnitTestInjector("Bloodseeker", "", hero_level, "", [], [], percentage_bonus, flat_bonus, "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_expected_block_value_used(block_source):
	"""
	>>> damage = test_expected_block_value_used("")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_expected_block_value_used("Stout Shield (melee)")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	50
	>>> damage = test_expected_block_value_used("Stout Shield (ranged)")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	56
	>>> damage = test_expected_block_value_used("Crimson Guard active")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	0
	"""
	injector = UIUnitTestInjector("Bloodseeker", "", "", "", [], [], "", "", block_source, "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_invalid_block_source_provided(block_source):
	"""
	>>> damage = test_invalid_block_source_provided("")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_invalid_block_source_provided("abcde")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	"""
	injector = UIUnitTestInjector("Bloodseeker", "", "", "", [], [], "", "", block_source, "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_block_damage_applies_after_attack_multipliers(hero_level, percentage_bonus, flat_bonus, block_source):
	"""
	>>> damage = test_block_damage_applies_after_attack_multipliers("0", "0", "0", "")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_block_damage_applies_after_attack_multipliers("0", "0", "0", "Crimson Guard active")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	0
	>>> damage = test_block_damage_applies_after_attack_multipliers("2", "0", "0", "")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	64
	>>> damage = test_block_damage_applies_after_attack_multipliers("2", "0", "0", "Crimson Guard active")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	4
	>>> damage = test_block_damage_applies_after_attack_multipliers("2", "100", "0", "")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	127
	>>> damage = test_block_damage_applies_after_attack_multipliers("2", "100", "0", "Crimson Guard active")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	67
	>>> damage = test_block_damage_applies_after_attack_multipliers("2", "", "14", "")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	78
	>>> damage = test_block_damage_applies_after_attack_multipliers("2", "", "14", "Crimson Guard active")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	18
	>>> damage = test_block_damage_applies_after_attack_multipliers("2", "100", "14", "")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	141
	>>> damage = test_block_damage_applies_after_attack_multipliers("2", "100", "14", "Crimson Guard active")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	81
	"""
	injector = UIUnitTestInjector("Bloodseeker", "", hero_level, "", [], [], percentage_bonus, flat_bonus, block_source, "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_expected_crit_value_used(crit_source):
	"""
	>>> damage = test_expected_crit_value_used("")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_expected_crit_value_used("Drunken Brawler (guaranteed crit) level 4")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	156
	>>> damage = test_expected_crit_value_used("Drunken Brawler (non-guaranteed crit) level 4")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	137
	"""
	injector = UIUnitTestInjector("Bloodseeker", "", "", "", [], [], "", "", "", crit_source, "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_invalid_crit_value_provided(crit_source):
	"""
	>>> damage = test_invalid_crit_value_provided("")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_invalid_crit_value_provided("Drunken Brawler (guaranteed crit) level 4")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	156
	>>> damage = test_invalid_crit_value_provided("Drunken Brawler (zzzzz) level 4")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	"""
	injector = UIUnitTestInjector("Bloodseeker", "", "", "", [], [], "", "", "", crit_source, "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_crit_comes_before_block_in_formula(block_source, crit_source):
	"""
	>>> damage = test_crit_comes_before_block_in_formula("", "")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_crit_comes_before_block_in_formula("Stout Shield (melee)", "Drunken Brawler (guaranteed crit) level 4")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	146
	>>> damage = test_crit_comes_before_block_in_formula("Crimson Guard active", "Drunken Brawler (guaranteed crit) level 4")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	96
	"""
	injector = UIUnitTestInjector("Bloodseeker", "", "", "", [], [], "", "", block_source, crit_source, "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_general_multipliers_inputs(general_multipliers):
	"""
	>>> damage = test_general_multipliers_inputs("")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_general_multipliers_inputs("100")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_general_multipliers_inputs("200")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	120
	>>> damage = test_general_multipliers_inputs("200%")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	120
	>>> damage = test_general_multipliers_inputs("50, 50%")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	15
	>>> damage = test_general_multipliers_inputs("50, 50%,33")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	5
	>>> damage = test_general_multipliers_inputs("50, 50%,33x")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	<BLANKLINE>
	Invalid percentage given: 33x. Skipping over value.
	15
	>>> damage = test_general_multipliers_inputs(",50,,, 50%,,33,")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	5
	>>> damage = test_general_multipliers_inputs(",,,,,,       ,, ,,, ,,,, ,")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	"""
	injector = UIUnitTestInjector("Bloodseeker", "", "", "", [], [], "", "", "", "", general_multipliers)
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_general_multipliers_last_in_formula(crit_source, block_source, general_multipliers):
	"""
	>>> damage = test_general_multipliers_last_in_formula("", "", "")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_general_multipliers_last_in_formula("Stout Shield (melee)", "", "")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	50
	>>> damage = test_general_multipliers_last_in_formula("Stout Shield (melee)", "Drunken Brawler (guaranteed crit) level 4", "")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	146
	>>> damage = test_general_multipliers_last_in_formula("Stout Shield (melee)", "Drunken Brawler (guaranteed crit) level 4", "50%")
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	73
	"""
	injector = UIUnitTestInjector("Bloodseeker", "", "", "", [], [], "", "", crit_source, block_source, general_multipliers)
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def item_injector(attacker, defender, attacker_items, defender_items):
	injector = UIUnitTestInjector(attacker, defender, "", "", attacker_items, defender_items, "", "", "", "", "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

def test_multiple_items_stack(attacker_items, defender_items):
	"""
	>>> damage = test_multiple_items_stack([], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_multiple_items_stack(["Claymore"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	81
	>>> damage = test_multiple_items_stack(["Claymore", "Claymore", "Claymore", "Claymore", "Claymore"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	165
	"""
	return item_injector("Bloodseeker", "", attacker_items, defender_items)

def test_items_affect_correct_hero(attacker_items, defender_items):
	"""
	>>> damage = test_multiple_items_stack([], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_multiple_items_stack(["Claymore"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	81
	>>> damage = test_multiple_items_stack([], ["Claymore"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_multiple_items_stack([], ["Ring of Protection"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	54
	>>> damage = test_multiple_items_stack(["Ring of Protection"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	"""
	return item_injector("Bloodseeker", "", attacker_items, defender_items)

def test_armor_modifies_damage(attacker_items, defender_items):
	"""
	>>> damage = test_armor_modifies_damage([], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_armor_modifies_damage(["Blight Stone"], [""])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	66
	>>> damage = test_armor_modifies_damage([], ["Ring of Protection"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	54
	>>> damage = test_armor_modifies_damage(["Ring of Protection", "Blight Stone"], ["Ring of Protection"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	"""
	return item_injector("Bloodseeker", "", attacker_items, defender_items)

def test_stat_boosts_on_placeholder_heroes(attacker_hero, attacker_items, defender_items):
	"""
	>>> damage = test_stat_boosts_on_placeholder_heroes("", [], [])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	0
	>>> damage = test_stat_boosts_on_placeholder_heroes("", ["Iron Branch"], [])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	0
	>>> damage = test_stat_boosts_on_placeholder_heroes("", ["Claymore"], [])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	21
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- STR is primary attribute", ["Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, STR variant attacking Placeholder...
	21
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- STR is primary attribute", ["Iron Branch", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, STR variant attacking Placeholder...
	22
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- STR is primary attribute", ["Ogre Axe", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, STR variant attacking Placeholder...
	31
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- STR is primary attribute", ["Blade of Alacrity", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, STR variant attacking Placeholder...
	21
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- STR is primary attribute", ["Staff of Wizardry", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, STR variant attacking Placeholder...
	21
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- AGI is primary attribute", ["Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, AGI variant attacking Placeholder...
	21
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- AGI is primary attribute", ["Iron Branch", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, AGI variant attacking Placeholder...
	22
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- AGI is primary attribute", ["Ogre Axe", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, AGI variant attacking Placeholder...
	21
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- AGI is primary attribute", ["Blade of Alacrity", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, AGI variant attacking Placeholder...
	31
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- AGI is primary attribute", ["Staff of Wizardry", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, AGI variant attacking Placeholder...
	21
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- INT is primary attribute", ["Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, INT variant attacking Placeholder...
	21
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- INT is primary attribute", ["Iron Branch", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, INT variant attacking Placeholder...
	22
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- INT is primary attribute", ["Ogre Axe", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, INT variant attacking Placeholder...
	21
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- INT is primary attribute", ["Blade of Alacrity", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, INT variant attacking Placeholder...
	21
	>>> damage = test_stat_boosts_on_placeholder_heroes("NONE- INT is primary attribute", ["Staff of Wizardry", "Claymore"], [])
	Injecting unit test values in Central object
	Placeholder, INT variant attacking Placeholder...
	31
	>>> damage = test_stat_boosts_on_placeholder_heroes("Beastmaster", [], [])
	Injecting unit test values in Central object
	Beastmaster attacking Placeholder...
	66
	>>> damage = test_stat_boosts_on_placeholder_heroes("Beastmaster", ["Ogre Axe"], [])
	Injecting unit test values in Central object
	Beastmaster attacking Placeholder...
	76
	>>> damage = test_stat_boosts_on_placeholder_heroes("Beastmaster", ["Blade of Alacrity"], [])
	Injecting unit test values in Central object
	Beastmaster attacking Placeholder...
	66
	>>> damage = test_stat_boosts_on_placeholder_heroes("Beastmaster", ["Staff of Wizardry"], [])
	Injecting unit test values in Central object
	Beastmaster attacking Placeholder...
	66
	>>> damage = test_stat_boosts_on_placeholder_heroes("Bloodseeker", [], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_stat_boosts_on_placeholder_heroes("Bloodseeker", ["Ogre Axe"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_stat_boosts_on_placeholder_heroes("Bloodseeker", ["Blade of Alacrity"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	70
	>>> damage = test_stat_boosts_on_placeholder_heroes("Bloodseeker", ["Staff of Wizardry"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_stat_boosts_on_placeholder_heroes("Chen", [], [])
	Injecting unit test values in Central object
	Chen attacking Placeholder...
	53
	>>> damage = test_stat_boosts_on_placeholder_heroes("Chen", ["Ogre Axe"], [])
	Injecting unit test values in Central object
	Chen attacking Placeholder...
	53
	>>> damage = test_stat_boosts_on_placeholder_heroes("Chen", ["Blade of Alacrity"], [])
	Injecting unit test values in Central object
	Chen attacking Placeholder...
	53
	>>> damage = test_stat_boosts_on_placeholder_heroes("Chen", ["Staff of Wizardry"], [])
	Injecting unit test values in Central object
	Chen attacking Placeholder...
	63
	"""
	return item_injector(attacker_hero, "", attacker_items, defender_items)


def test_percentage_boost_not_boost_item_damage(attacker_items, defender_items):
	"""
	>>> damage = test_percentage_boost_not_boost_item_damage([], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_percentage_boost_not_boost_item_damage(["Vladmir's Offering (melee)"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	71
	>>> damage = test_percentage_boost_not_boost_item_damage(["Vladmir's Offering (melee)", "Eye of Skadi"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	100
	>>> damage = test_percentage_boost_not_boost_item_damage(["Vladmir's Offering (melee)", "Eye of Skadi", "Claymore"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	121
	"""
	#Vlads gives 2 to all stats, hence why the numbers are slightly higher than a 15% increase
	return item_injector("Bloodseeker", "", attacker_items, defender_items)

def test_magic_burst_and_magic_resistance_items(attacker_items, defender_items):
	"""
	>>> damage = test_magic_burst_and_magic_resistance_items([], [])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	0
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 1"], [])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	0
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 1 (burst used)"], [])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	304
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 2 (burst used)"], [])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	381
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 3 (burst used)"], [])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	458
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 4 (burst used)"], [])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	535
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 5 (burst used)"], [])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	613
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 1 (burst used)"], ["Cloak"])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	259
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 1 (burst used)"], ["Cloak", "Cloak"])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	219
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 1 (burst used)"], ["Cloak", "Cloak", "Cloak"])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	186
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 1 (burst used)"], ["Pipe of Insight (magic barrier from ally, no aura)"])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	4
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 2 (burst used)"], ["Pipe of Insight (magic barrier from ally, no aura)"])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	81
	>>> damage = test_magic_burst_and_magic_resistance_items(["Dagon 3 (burst used)"], ["Pipe of Insight (magic barrier from ally, no aura)"])
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	158
	"""
	#NOTE: These dagon values are slightly over 75% of their base magic burst because the int from dagon
	#causes the placeholder hero to get some spell amp
	return item_injector("", "", attacker_items, defender_items)

def test_percentage_attack_modifiers_dont_increase_magic_damage(attacker_items):
	"""
	>>> damage = test_percentage_attack_modifiers_dont_increase_magic_damage([])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_percentage_attack_modifiers_dont_increase_magic_damage(["Vladmir's Offering (melee)"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	71
	>>> damage = test_percentage_attack_modifiers_dont_increase_magic_damage(["Vladmir's Offering (melee)", "Dagon 1"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	77
	>>> damage = test_percentage_attack_modifiers_dont_increase_magic_damage(["Vladmir's Offering (melee)", "Dagon 1 (burst used)"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	385
	"""
	return item_injector("Bloodseeker", "", attacker_items, [])

def test_ethereal_state(attacker_items, defender_items): #TODO ethereal state number seems lower than should be?
	"""
	>>> damage = test_ethereal_state([], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_ethereal_state(["Ghost Sceptre"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	65
	>>> damage = test_ethereal_state([], ["Ghost Sceptre"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	57
	>>> damage = test_ethereal_state(["Ethereal Blade"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	100
	>>> damage = test_ethereal_state([], ["Ethereal Blade"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	43
	>>> damage = test_ethereal_state(["Ethereal Blade (active used by ally)"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	0
	>>> damage = test_ethereal_state([], ["Ethereal Blade (active used by ally)"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	0
	>>> damage = test_ethereal_state(["Ethereal Blade (active used by ally)", "Claymore"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	0
	>>> damage = test_ethereal_state(["Claymore"], ["Ethereal Blade (active used by ally)"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	0
	>>> damage = test_ethereal_state(["Ghost Sceptre (active used)"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	0
	>>> damage = test_ethereal_state([], ["Ghost Sceptre (active used)"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	0
	>>> damage = test_ethereal_state(["Ethereal Blade (active used on target)"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	217
	>>> damage = test_ethereal_state([], ["Ethereal Blade (active used on target)"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	0
	>>> damage = test_ethereal_state(["Dagon 1 (burst used)"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	373
	>>> damage = test_ethereal_state(["Ethereal Blade (active used on target)", "Dagon 1 (burst used)"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	664
	>>> damage = test_ethereal_state(["Ethereal Blade (active used on target)", "Mjollnir (static charge triggered)"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	431
	>>> damage = test_ethereal_state(["Ethereal Blade (active used on target)", "Mjollnir"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	217
	"""
	return item_injector("Bloodseeker", "", attacker_items, defender_items)


def test_conditional_procs(attacker_items):
	"""
	>>> damage = test_conditional_procs(["Monkey King Bar"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	169
	>>> damage = test_conditional_procs(["Monkey King Bar (zero procs)"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	112
	>>> damage = test_ethereal_state(["Ethereal Blade (active used on target)", "Monkey King Bar"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	217
	"""
	return item_injector("Bloodseeker", "", attacker_items, [])


def test_mana_burn(attacker_items):
	"""
	>>> damage = test_mana_burn(["Diffusal Blade"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	80
	>>> damage = test_mana_burn(["Diffusal Blade (with manabreak)"])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	111
	>>> damage = test_ethereal_state(["Ethereal Blade (active used on target)", "Diffusal Blade"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	262
	>>> damage = test_ethereal_state(["Ethereal Blade (active used on target)", "Diffusal Blade (with manabreak)"], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	262
	"""
	return item_injector("Bloodseeker", "", attacker_items, [])

def test_flat_bonuses_influeced_by_crit(attacker_items, crit_source_name):
	"""
	>>> damage = test_flat_bonuses_influeced_by_crit(["Shadow Blade (exiting invis)"], "")
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	197
	>>> damage = test_flat_bonuses_influeced_by_crit(["Shadow Blade (exiting invis)"], "Drunken Brawler (guaranteed crit) level 1")
	Injecting unit test values in Central object
	Placeholder attacking Placeholder...
	276
	"""
	injector = UIUnitTestInjector("", "", "", "", attacker_items, [], "", "", "", crit_source_name, "")
	ui = Central(tkinter.Tk(), injector)
	return ui.calculate_damage_for_single_sample()

#TODO
#Evasion only works on right clicks, dodges conditional procs but not magic burst
#Evasion is not apply to attacker when its their evasion



#TO DEPRECATE WHEN CENTRAL IS REWORKED TO ACCOMODATE MULTIPLE CRIT AND BLOCK SOURCES
def test_no_crit_from_crit_items(attacker_items, defender_items):
	"""
	>>> damage = test_no_crit_from_crit_items([], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_no_crit_from_crit_items(["Daedalus"], [""])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	140
	"""
	return item_injector("Bloodseeker", "", attacker_items, defender_items)

def test_no_block_from_block_items(attacker_items, defender_items):
	"""
	>>> damage = test_no_block_from_block_items([], [])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	>>> damage = test_no_block_from_block_items(["Stout Shield"], [""])
	Injecting unit test values in Central object
	Bloodseeker attacking Placeholder...
	60
	"""
	return item_injector("Bloodseeker", "", attacker_items, defender_items)


if __name__ == "__main__":
    import doctest
    doctest.testmod()