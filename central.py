from critical_strike import CriticalStrike
from damage_block import DamageBlock
from damage_calculator import calculate_total_damage
from flat_damage_bonus import FlatDamageBonus
from hero import Hero
from item import Item
from magical_damage import MagicalDamage
from percentage import Percentage
from percentage_damage_bonus import PercentageDamageBonus
from physical_damage import PhysicalDamage
from physical_damage import PhysicalDamage
from ui_unit_test_injector import UIUnitTestInjector
import ast
import tkinter

#TODO print in window
#TODO print queued previous with data of situation
#TODO implement true strike (evasion bypassing)
#TODO implement evasion stopping conditional procs

class Central(tkinter.Frame):

    #The smallest difference of time expressed in Dota.
    TIME_SAMPLE_INCREMENT = 0.01

    MAX_ITEM_COUNT = 6

    PLACEHOLDER_HERO_NAME = "NONE"

    STANDARD_BASE_ATTACK_TIME = 1.7

    VALID_HERO_LEVELS = ["1", "2", "3", "4", "5", 
                            "6", "7", "8", "9", "10", 
                            "11", "12", "13", "14", "15", 
                            "16", "17", "18", "19", "20", 
                            "21", "22", "23", "24", "25"]

    ATTACKER_SELECT_DEFAULT = "Select an attacker"
    ATTACKER_CRIT_SOURCE_DEFAULT = "Select attacker crit source"
    ATTACKER_PERCENT_BONUS_DEFAULT = "Enter attacker percent damage bonuses here as percentage values separated by commas for percent bonuses NOT from items (eg: Venge aura, wolf aura)"
    ATTACKER_FLAT_BONUS_DEFAULT = "Enter attacker flat damage bonuses as integers separated by commas for bonus damage NOT from items (eg: static link)"

    DEFENDER_SELECT_DEFAULT = "Select a defender"
    DEFENDER_BLOCK_SOURCE_DEFAULT = "Select defender block source"

    HERO_LEVEL_DEFAULT = "Enter hero level"
    ITEM_DEFAULT = "Select an item or leave this box unchanged"
    GENERAL_DAMAGE_MULTIPLIER_DEFAULT = "Enter general damage multipliers as percentage values separated by commas (eg: Bristleback, Bloodrage)"

    AGILITY_TO_ARMOR_CONVERSION_FACTOR = 0.16
    INTELLIGENCE_TO_SPELL_AMP_CONVERSION_FACTOR = 0.07
    ETHEREAL_BLADE_DAMAGE_MULTIPLIER = Percentage("200%")
    ETHEREAL_BLADE_USED_INDICATOR = ["Ethereal Blade (active used on target)"]

    def __init__(self, master, unit_test_attribute_injector=None):
        if unit_test_attribute_injector is None:
            tkinter.Frame.__init__(self,
                              master,
                              width=1500,
                              height=1000)
            self.master.title("Damage calculator")
            self.pack_propagate(0)
            self.pack()

            self.init_attacker_bonus_inputs()
            self.init_block_source_variables()
            self.init_crit_source_variables()
            self.init_general_damage_multipliers()
            self.init_hero_choices()
            self.init_hero_items()
            self.init_hero_level_buttons()
            self.init_time_box()
            self.init_initiation_devices()

            self.format_buttons()
        else:
            print("Injecting unit test values in Central object")
            self.inject_unit_test_values(unit_test_attribute_injector)

    def inject_unit_test_values(self, injector):
        if injector is None:
            return
        assert isinstance(injector, UIUnitTestInjector)
        #Constructor path designed to allow unit testing
        #StringVar() constructor signature is __init__(self, master=None, value=None, name=None) 
        #Source: http://epydoc.sourceforge.net/stdlib/Tkinter.StringVar-class.html
        self.attacker_hero_choice = tkinter.StringVar(None, injector.get_attacker_hero_name())
        self.defender_hero_choice = tkinter.StringVar(None, injector.get_defender_hero_name())
        self.attacker_level_choice = tkinter.StringVar(None, injector.get_attacker_hero_level())
        self.defender_level_choice = tkinter.StringVar(None, injector.get_defender_hero_level())
        self.attacker_item_choices = []
        items = injector.get_attacker_item_choices()
        for item in items:
            self.attacker_item_choices.append(tkinter.StringVar(None, item))
        self.defender_item_choices = []
        items = injector.get_defender_item_choices()
        for item in items:
            self.defender_item_choices.append(tkinter.StringVar(None, item))
        self.attacker_percent_var = tkinter.StringVar(None, injector.get_attacker_percent_var())
        self.attacker_flat_var = tkinter.StringVar(None, injector.get_attacker_flat_var())
        self.defender_block_var = tkinter.StringVar(None, injector.get_defender_block_var())
        self.attacker_crit_var = tkinter.StringVar(None, injector.get_attacker_crit_var())
        self.general_damage_multipliers = tkinter.StringVar(None, injector.get_general_damage_multipliers())


    def init_hero_choices(self):
        with open('hero_names.txt', 'r') as f:
            hero_names = f.readlines()
        hero_names = [hero_name.replace("\n", "") for hero_name in hero_names]

        self.attacker_hero_choice = tkinter.StringVar()
        self.attacker_hero_choice.set(Central.ATTACKER_SELECT_DEFAULT)

        self.attacker = tkinter.OptionMenu(self,
                                      self.attacker_hero_choice,
                                      *hero_names)

        self.defender_hero_choice = tkinter.StringVar()
        self.defender_hero_choice.set(Central.DEFENDER_SELECT_DEFAULT)
        self.defender = tkinter.OptionMenu(self,
                                      self.defender_hero_choice,
                                      *hero_names)

    def init_hero_items(self):
        with open('item_names.txt', 'r') as f:
            item_names = f.readlines()
        item_names = [item_name.replace("\n", "") for item_name in item_names]

        self.attacker_item_choices = []
        self.attacker_item_buttons = []
        for i in range(Central.MAX_ITEM_COUNT):
            self.attacker_item_choices.append(tkinter.StringVar())
            self.attacker_item_choices[i].set(Central.ITEM_DEFAULT)
            self.attacker_item_buttons.append(tkinter.OptionMenu(self, self.attacker_item_choices[i], *item_names))

        self.defender_item_choices = []
        self.defender_item_buttons = []
        for i in range(Central.MAX_ITEM_COUNT):
            self.defender_item_choices.append(tkinter.StringVar())
            self.defender_item_choices[i].set(Central.ITEM_DEFAULT)
            self.defender_item_buttons.append(tkinter.OptionMenu(self, self.defender_item_choices[i], *item_names))


    def init_attacker_bonus_inputs(self):
        self.attacker_percent_var = tkinter.StringVar()
        self.attacker_percent_damages = tkinter.Entry(self, width=134,
                                  textvariable=self.attacker_percent_var)
        self.attacker_percent_var.set(Central.ATTACKER_PERCENT_BONUS_DEFAULT)

        self.attacker_flat_var = tkinter.StringVar()
        self.attacker_flat_damages = tkinter.Entry(self, width=105,
                                  textvariable=self.attacker_flat_var)
        self.attacker_flat_var.set(Central.ATTACKER_FLAT_BONUS_DEFAULT)

    def init_block_source_variables(self):
        with open('block_sources.txt', 'r') as f:
          block_sources = f.readlines()
        block_sources = [block_source.replace("\n", "") for block_source in block_sources]
        self.defender_block_var = tkinter.StringVar()
        self.defender_block_option = tkinter.OptionMenu(self,
                                      self.defender_block_var,
                                      *block_sources)
        self.defender_block_var.set(Central.DEFENDER_BLOCK_SOURCE_DEFAULT)

    def init_crit_source_variables(self):
        with open('critical_strike_sources.txt', 'r') as f:
          crit_sources = f.readlines()
        crit_sources = [crit_source.replace("\n", "") for crit_source in crit_sources]
        self.attacker_crit_var = tkinter.StringVar()
        self.attacker_crit_option = tkinter.OptionMenu(self,
                                      self.attacker_crit_var,
                                      *crit_sources)
        self.attacker_crit_var.set(Central.ATTACKER_CRIT_SOURCE_DEFAULT)

    def init_general_damage_multipliers(self):
        self.general_damage_multipliers = tkinter.StringVar()
        self.general_damage = tkinter.Entry(self,  width=92,
                                  textvariable=self.general_damage_multipliers)
        self.general_damage_multipliers.set(Central.GENERAL_DAMAGE_MULTIPLIER_DEFAULT)

    def init_hero_level_buttons(self):
        self.attacker_level_choice = tkinter.StringVar()
        self.attacker_level_set = tkinter.Entry(self, width=17,
                                  textvariable=self.attacker_level_choice)
        self.attacker_level_choice.set(Central.HERO_LEVEL_DEFAULT)

        self.defender_level_choice = tkinter.StringVar()
        self.defender_level_set = tkinter.Entry(self, width=18,
                                  textvariable=self.defender_level_choice)
        self.defender_level_choice.set(Central.HERO_LEVEL_DEFAULT)

    def init_time_box(self): #TODO sanitize
        self.attack_time = tkinter.StringVar()
        self.attack_time.set("1")
        self.attack_time_box = tkinter.Entry(self, width=15,
                                  textvariable=self.attack_time)

    def init_initiation_devices(self):
        self.calculate_button = tkinter.Button(self,
                                   text='Calculate',
                                   command=self.calculate_total_damage)


    def format_buttons(self):
        self.attacker.pack(side=tkinter.TOP, anchor="w")
        self.attacker_level_set.pack(side=tkinter.TOP, anchor="w")
        for i in range(Central.MAX_ITEM_COUNT):
            self.attacker_item_buttons[i].pack(side=tkinter.TOP, anchor="w")
        self.attacker_percent_damages.pack(side=tkinter.TOP, anchor="w")
        self.attacker_flat_damages.pack(side=tkinter.TOP, anchor="w")
        self.attacker_crit_option.pack(side=tkinter.TOP, anchor="w")

        self.defender.pack(side=tkinter.TOP, anchor="e")
        self.defender_level_set.pack(side=tkinter.TOP, anchor="e")
        for i in range(Central.MAX_ITEM_COUNT):
            self.defender_item_buttons[i].pack(side=tkinter.TOP, anchor="e")
        self.defender_block_option.pack(side=tkinter.TOP, anchor="e")

        self.general_damage.pack(side=tkinter.TOP)

        self.calculate_button.pack(side=tkinter.BOTTOM)

        self.attack_time_box.pack(side=tkinter.BOTTOM)

    def calculate_total_damage(self):
        single_sample_damage = self.calculate_damage_for_single_sample()
        time_between_attacks = self.calculate_time_between_attacks() * Central.STANDARD_BASE_ATTACK_TIME
        attack_timeframe = int(self.attack_time.get())

        print("Damage from one attack instance: " + str(single_sample_damage))
        print("Time between damage instances: " + str(time_between_attacks))
        print("Specified attack timeframe: " + str(attack_timeframe))

        number_of_attack_instances = 1
        while (attack_timeframe >= time_between_attacks):
            number_of_attack_instances += 1
            attack_timeframe -= time_between_attacks

        print("\n\nTotal damage: " + str(number_of_attack_instances * single_sample_damage))


    def calculate_time_between_attacks(self):
        base_attack_time = self.attacker_hero.get_base_attack_time()
        attack_speed_sum = 100 + self.attacker_hero.get_agility() + (self.attacker_hero.get_agility_gain() * (self.attacker_level - 1))

        #Add attack speed grwoth from agi in items and attack speed in items
        for item in self.attacker_items:
            attack_speed_sum += item.get_agility()
            attack_speed_sum += item.get_attack_speed()

        attacks_per_second = 0.01 * (attack_speed_sum * (Central.STANDARD_BASE_ATTACK_TIME / base_attack_time))

        return round(1 / attacks_per_second, 2)

 
    def calculate_damage_for_single_sample(self):  
        #Initiate both heroes
        self.attacker_hero = Central.create_hero(self.attacker_hero_choice.get())
        self.attacker_level = Central.create_hero_level(self.attacker_level_choice.get())

        defender_hero = Central.create_hero(self.defender_hero_choice.get())
        defender_level = Central.create_hero_level(self.defender_level_choice.get())


        print(self.attacker_hero.get_hero_name() + " attacking " + defender_hero.get_hero_name() + "...")

        damage_sources = []
        attacker_spell_amp_sources = []
        attacker_base_damage = self.attacker_hero.get_expected_attack_damage()
        attacker_primary_attr = self.attacker_hero.get_primary_attr()

        #Derive items for attacker and defender and determine if one of them has activate ethereal state on
        self.attacker_items, defender_items, ethereal_used_offensively = self.derive_items()

        party_is_ethereal = Central.determine_party_is_ethereal((self.attacker_items + defender_items))

        #Get primary attribute gain and damage based on primary attribute for right click or e-blade projectile
        attacker_str_gain, attacker_agi_gain, attacker_int_gain = Central.calculate_stat_gains_above_starting_stats_attacker(self.attacker_hero,
                                                                                                                                self.attacker_level,
                                                                                                                                self.attacker_items)
        primary_stat_sum, primary_stat_gain = Central.determine_primary_stat_sum(self.attacker_hero, attacker_str_gain, attacker_agi_gain, attacker_int_gain)

        if not party_is_ethereal:
            damage_sources.append(PhysicalDamage(attacker_base_damage + primary_stat_gain))
        elif party_is_ethereal and  ethereal_used_offensively:
            damage_sources.append(MagicalDamage(primary_stat_sum * Central.ETHEREAL_BLADE_DAMAGE_MULTIPLIER.get_percentage_multiple()))

        attacker_spell_amp_sources.append(Percentage(str(((attacker_int_gain + self.attacker_hero.get_intelligence()) * Central.INTELLIGENCE_TO_SPELL_AMP_CONVERSION_FACTOR))))

        #Derive all modifiers based on all items in the interaction
        attacker_percentage_bonuses, attacker_flat_bonuses = Central.integrate_attacker_bonuses(self.attacker_percent_var.get(), self.attacker_flat_var.get())

        defender_armor, defender_base_magic_resistance, defender_strength = Central.target_base_defenses(defender_hero, defender_level)

        if not party_is_ethereal:
            attacker_percentage_bonuses, attacker_flat_bonuses, damage_sources, defender_armor, defender_evasion_quantities = Central.integrate_right_click_based_item_properties(self.attacker_items, 
                                                                                                                                                                                    defender_items, 
                                                                                                                                                                                    damage_sources, 
                                                                                                                                                                                    attacker_percentage_bonuses, 
                                                                                                                                                                                    attacker_flat_bonuses, 
                                                                                                                                                                                    defender_armor)
        else:
            damage_sources = [damage_source for damage_source in damage_sources if not isinstance(damage_source, PhysicalDamage)]
            attacker_flat_bonuses = []
            defender_evasion_quantities = []
        damage_sources, attacker_spell_amp_sources, defender_magic_resistances, defender_spell_shield_quantities = Central.integrate_non_right_click_based_item_properties(damage_sources,
                                                                                                                                                            self.attacker_items, 
                                                                                                                                                            defender_items,
                                                                                                                                                            attacker_spell_amp_sources)


        #Derive crit, block, and general damage multipliers
        #The below sections will be reworked once multiple crit souces support has been added
        attacker_crit_sources = []
        if self.attacker_crit_var.get() != Central.ATTACKER_CRIT_SOURCE_DEFAULT:
            attacker_crit_sources = Central.derive_singular_source_item("critical_strike_metadata", self.attacker_crit_var.get())

        defender_block_sources = []
        if self.defender_block_var.get() != Central.DEFENDER_BLOCK_SOURCE_DEFAULT:
            defender_block_sources = Central.derive_singular_source_item("block_source_metadata", self.defender_block_var.get(), False)

        general_damage_multipliers = Central.create_list_of_values(self.general_damage_multipliers.get(), Central.GENERAL_DAMAGE_MULTIPLIER_DEFAULT)


        #Calculate damage output
        total_damage = calculate_total_damage(damage_sources, 
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
                                                general_damage_multipliers)

        print(total_damage)
        return total_damage



    def calculate_stat_gains_above_starting_stats_attacker(attacker_hero, attacker_level, attacker_items):
        attacker_str_gain = (attacker_hero.get_strength_gain() * (attacker_level - 1))
        attacker_agi_gain = (attacker_hero.get_agility_gain() * (attacker_level - 1))
        attacker_int_gain = (attacker_hero.get_intelligence_gain() * (attacker_level - 1))
        for item in attacker_items:
            attacker_str_gain += item.get_strength()
            attacker_agi_gain += item.get_agility()
            attacker_int_gain += item.get_intelligence()

        return attacker_str_gain, attacker_agi_gain, attacker_int_gain

    def create_hero_level(hero_level):
        return int(hero_level) if hero_level in Central.VALID_HERO_LEVELS else 1

    def create_hero(hero_name):
        with open("hero_metadata", "r") as f:
            all_hero_metadata = ast.literal_eval(f.read())
            return Hero(all_hero_metadata[(hero_name if hero_name in all_hero_metadata else Central.PLACEHOLDER_HERO_NAME)])

    def create_list_of_values(value_string, default_string, generate_percentage=True):
        values_returned = []
        if value_string != default_string:
            values = [final_value for final_value in [value.replace(" ", "") for value in value_string.split(",")] if final_value != ""]
            for value in values:
                try:
                    values_returned.append((Percentage(value) if generate_percentage else int(value)))
                except:
                    print("\nInvalid " + ("percentage" if generate_percentage else "integer") + " given: " + value + ". Skipping over value.")
        return values_returned

    def derive_items(self):
        with open("item_metadata", "r") as f:
            all_item_metadata = ast.literal_eval(f.read())

        ethereal_used_offensively = False
        attacker_items = []
        for item in self.attacker_item_choices:
            item_name = item.get()
            ethereal_used_offensively = ethereal_used_offensively or (Central.ETHEREAL_BLADE_USED_INDICATOR[0] == item_name)
            if item_name in all_item_metadata:
                attacker_items.append(Item(all_item_metadata[item_name]))

        defender_items = []
        for item in self.defender_item_choices:
            item_name = item.get()
            if item_name in all_item_metadata:
                defender_items.append(Item(all_item_metadata[item_name]))

        return attacker_items, defender_items, ethereal_used_offensively

    def derive_singular_source_item(metadata_file_name, source_name, critical_strike=True):
        singular_source_list = []
        with open(metadata_file_name, "r") as f:
            source_metadata = ast.literal_eval(f.read())
        if source_name in source_metadata:
            item_entry = source_metadata[source_name]
            singular_source_list.append(CriticalStrike(Percentage(item_entry["crit chance"]), Percentage(item_entry["crit multiplier"])) if critical_strike else DamageBlock(item_entry["block amount"], Percentage(item_entry["block chance"])))
        return singular_source_list

    def determine_party_is_ethereal(items):
        for item in items:
            if item.get_is_ethereal() or item.get_target_ethereal():
                return True
        return False

    def determine_primary_stat_sum(hero, str_gain, agi_gain, int_gain):
        primary_attr = hero.get_primary_attr()
        if primary_attr == "STR":
           return hero.get_strength() + str_gain, str_gain
        elif primary_attr == "AGI":
            return hero.get_agility() + agi_gain, agi_gain
        elif primary_attr == "INT":
            return hero.get_intelligence() + int_gain, int_gain
        else:
            return 0, 0

    def integrate_attacker_bonuses(percentage_input, flat_input):
        percentages_to_create_bonuses = Central.create_list_of_values(percentage_input, Central.ATTACKER_PERCENT_BONUS_DEFAULT)
        #Negative attacker percentage bonuses are not allowed and are pruned here
        #Percentage bonus is None when bad input is encountered
        attacker_percentage_bonuses = [PercentageDamageBonus(percentage_bonus) for percentage_bonus in percentages_to_create_bonuses if percentage_bonus is not None and percentage_bonus.get_percentage_multiple() >= 0]

        flat_bonuses = Central.create_list_of_values(flat_input, Central.ATTACKER_FLAT_BONUS_DEFAULT, False)
        #flat bonus is None when bad input is encountered
        attacker_flat_bonuses = [FlatDamageBonus(flat_bonus) for flat_bonus in flat_bonuses if flat_bonus is not None] 

        return attacker_percentage_bonuses, attacker_flat_bonuses

    def integrate_right_click_based_item_properties(attacker_items, defender_items, damage_sources, attacker_percentage_bonuses, attacker_flat_bonuses, defender_armor):
        defender_evasion_quantities = []
        for item in attacker_items:
            attacker_percentage_bonuses.append(item.get_damage_percentage_boost())
            attacker_flat_bonuses.append(FlatDamageBonus(item.get_damage()))
            damage_sources.append(item.get_conditional_proc().get_conditional_expected_damage_instance())
            damage_sources.append(item.get_manabreak())
            damage_sources.append(PhysicalDamage(item.get_physical_burst()))
            defender_armor += item.get_armor_of_target()

        for item in defender_items:
            defender_armor += (item.get_agility() * Central.AGILITY_TO_ARMOR_CONVERSION_FACTOR)
            defender_armor += item.get_armor()
            defender_evasion_quantities.append(item.get_evasion())

        return attacker_percentage_bonuses, attacker_flat_bonuses, damage_sources, defender_armor, defender_evasion_quantities

    def integrate_non_right_click_based_item_properties(damage_sources, attacker_items, defender_items, attacker_spell_amp_sources):
        defender_magic_resistances = []
        defender_spell_shield_quantities = []
        for item in attacker_items:
            attacker_spell_amp_sources.append(item.get_spell_amp())
            defender_magic_resistances.append(item.get_target_magic_resist())
            damage_sources.append(MagicalDamage(item.get_magic_burst()))

        for item in defender_items:
            defender_magic_resistances.append(item.get_magic_resistance())
            defender_spell_shield_quantities.append(item.get_magic_barrier())

        return damage_sources, attacker_spell_amp_sources, defender_magic_resistances, defender_spell_shield_quantities

    def target_base_defenses(defender, defender_level):
        defender_armor = defender.get_base_armor() + (defender.get_agility_gain() * (defender_level - 1) * Central.AGILITY_TO_ARMOR_CONVERSION_FACTOR)
        defender_base_magic_resistance = defender.get_base_magic_resistance()
        defender_strength = defender.get_strength() + defender.get_strength_gain() * (defender_level - 1)
        return defender_armor, defender_base_magic_resistance, defender_strength


    def run(self):
        self.mainloop()