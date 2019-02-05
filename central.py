import tkinter
import ast
from hero import Hero
from item import Item
from physical_damage import PhysicalDamage
from damage_calculator import calculate_total_damage
from damage_block import DamageBlock
from critical_strike import CriticalStrike
from percentage import Percentage
from flat_damage_bonus import FlatDamageBonus
from percentage_damage_bonus import PercentageDamageBonus

class Central(tkinter.Frame):

    ATTACKER_SELECT_DEFAULT = "Select an attacker"
    ATTACKER_LEVEL_DEFAULT = "Enter attacker level"
    ATTACKER_CRIT_SOURCE_DEFAULT = "Select attacker crit source"
    ATTACKER_PERCENT_BONUS_DEFAULT = "Enter attacker percent damage bonuses here as percentage values separated by commas for percent bonuses NOT from items (eg: Venge aura, wolf aura)"
    ATTACKER_FLAT_BONUS_DEFAULT = "Enter attacker flat damage bonuses as integers separated by commas for bonus damage NOT from items (eg: static link)"

    DEFENDER_SELECT_DEFAULT = "Select a defender"
    DEFENDER_LEVEL_DEFAULT = "Enter defender level"
    DEFENDER_BLOCK_SOURCE_DEFAULT = "Select defender block source"

    ITEM_DEFAULT = "Select an item or leave this box unchanged"
    GENERAL_DAMAGE_MULTIPLIER_DEFAULT = "Enter general damage multipliers as percentage values separated by commas (eg: Bristleback, Bloodrage)"

    AGILITY_TO_ARMOR_CONVERSION_FACTOR = 0.16

    def __init__(self, master):
        tkinter.Frame.__init__(self,
                          master,
                          width=1500,
                          height=1000)
        self.master.title("Damage calculator")
        self.pack_propagate(0)
        self.pack()

        with open('hero_names.txt', 'r') as f:
          hero_names = f.readlines()
        hero_names = [hero_name.replace("\n", "") for hero_name in hero_names]

        with open('item_names.txt', 'r') as f:
          item_names = f.readlines()
        item_names = [item_name.replace("\n", "") for item_name in item_names]

        with open('critical_strike_sources.txt', 'r') as f:
          crit_sources = f.readlines()
        crit_sources = [crit_source.replace("\n", "") for crit_source in crit_sources]

        with open('block_sources.txt', 'r') as f:
          block_sources = f.readlines()
        block_sources = [block_source.replace("\n", "") for block_source in block_sources]
 
        #Attacker options
        self.attacker_hero = tkinter.StringVar()
        self.attacker_hero.set(Central.ATTACKER_SELECT_DEFAULT)
        self.attacker_item1_choice = tkinter.StringVar()
        self.attacker_item1_choice.set(Central.ITEM_DEFAULT)
        self.attacker_item2_choice = tkinter.StringVar()
        self.attacker_item2_choice.set(Central.ITEM_DEFAULT)
        self.attacker_item3_choice = tkinter.StringVar()
        self.attacker_item3_choice.set(Central.ITEM_DEFAULT)
        self.attacker_item4_choice = tkinter.StringVar()
        self.attacker_item4_choice.set(Central.ITEM_DEFAULT)
        self.attacker_item5_choice = tkinter.StringVar()
        self.attacker_item5_choice.set(Central.ITEM_DEFAULT)
        self.attacker_item6_choice = tkinter.StringVar()
        self.attacker_item6_choice.set(Central.ITEM_DEFAULT)
        self.attacker = tkinter.OptionMenu(self,
                                      self.attacker_hero,
                                      *hero_names)
        self.attacker_item1 = tkinter.OptionMenu(self,
                                      self.attacker_item1_choice,
                                      *item_names)
        self.attacker_item2 = tkinter.OptionMenu(self,
                                      self.attacker_item2_choice,
                                      *item_names)
        self.attacker_item3 = tkinter.OptionMenu(self,
                                      self.attacker_item3_choice,
                                      *item_names)
        self.attacker_item4 = tkinter.OptionMenu(self,
                                      self.attacker_item4_choice,
                                      *item_names)
        self.attacker_item5 = tkinter.OptionMenu(self,
                                      self.attacker_item5_choice,
                                      *item_names)
        self.attacker_item6 = tkinter.OptionMenu(self,
                                      self.attacker_item6_choice,
                                      *item_names)

        self.attacker_crit_var = tkinter.StringVar()
        self.attacker_crit_option = tkinter.OptionMenu(self,
                                      self.attacker_crit_var,
                                      *crit_sources)
        self.attacker_crit_var.set(Central.ATTACKER_CRIT_SOURCE_DEFAULT)

        # Attacker text entry variables
        self.attacker_level = tkinter.StringVar()
        self.attacker_level_set = tkinter.Entry(self, width=17,
                                  textvariable=self.attacker_level)
        self.attacker_level.set(Central.ATTACKER_LEVEL_DEFAULT)

        self.attacker_percent_var = tkinter.StringVar()
        self.attacker_percent_damages = tkinter.Entry(self, width=134,
                                  textvariable=self.attacker_percent_var)
        self.attacker_percent_var.set(Central.ATTACKER_PERCENT_BONUS_DEFAULT)

        self.attacker_flat_var = tkinter.StringVar()
        self.attacker_flat_damages = tkinter.Entry(self, width=105,
                                  textvariable=self.attacker_flat_var)
        self.attacker_flat_var.set(Central.ATTACKER_FLAT_BONUS_DEFAULT)


        #Defender options
        self.defender_hero = tkinter.StringVar()
        self.defender_hero.set(Central.DEFENDER_SELECT_DEFAULT)
        self.defender_item1_choice = tkinter.StringVar()
        self.defender_item1_choice.set(Central.ITEM_DEFAULT)
        self.defender_item2_choice = tkinter.StringVar()
        self.defender_item2_choice.set(Central.ITEM_DEFAULT)
        self.defender_item3_choice = tkinter.StringVar()
        self.defender_item3_choice.set(Central.ITEM_DEFAULT)
        self.defender_item4_choice = tkinter.StringVar()
        self.defender_item4_choice.set(Central.ITEM_DEFAULT)
        self.defender_item5_choice = tkinter.StringVar()
        self.defender_item5_choice.set(Central.ITEM_DEFAULT)
        self.defender_item6_choice = tkinter.StringVar()
        self.defender_item6_choice.set(Central.ITEM_DEFAULT)
        self.defender = tkinter.OptionMenu(self,
                                      self.defender_hero,
                                      *hero_names)
        self.defender_item1 = tkinter.OptionMenu(self,
                                      self.defender_item1_choice,
                                      *item_names)
        self.defender_item2 = tkinter.OptionMenu(self,
                                      self.defender_item2_choice,
                                      *item_names)
        self.defender_item3 = tkinter.OptionMenu(self,
                                      self.defender_item3_choice,
                                      *item_names)
        self.defender_item4 = tkinter.OptionMenu(self,
                                      self.defender_item4_choice,
                                      *item_names)
        self.defender_item5 = tkinter.OptionMenu(self,
                                      self.defender_item5_choice,
                                      *item_names)
        self.defender_item6 = tkinter.OptionMenu(self,
                                      self.defender_item6_choice,
                                      *item_names)

        self.defender_block_var = tkinter.StringVar()
        self.defender_block_option = tkinter.OptionMenu(self,
                                      self.defender_block_var,
                                      *block_sources)
        self.defender_block_var.set(Central.DEFENDER_BLOCK_SOURCE_DEFAULT)

        # Defender text entry variables
        self.defender_level = tkinter.StringVar()
        self.defender_level_set = tkinter.Entry(self, width=18,
                                  textvariable=self.defender_level)
        self.defender_level.set(Central.DEFENDER_LEVEL_DEFAULT)



        #General damage multipliers
        self.general_damage_multipliers = tkinter.StringVar()
        self.general_damage = tkinter.Entry(self,  width=92,
                                  textvariable=self.general_damage_multipliers)
        self.general_damage_multipliers.set(Central.GENERAL_DAMAGE_MULTIPLIER_DEFAULT)

        # Calculation button
        self.calculate_button = tkinter.Button(self,
                                   text='Calculate',
                                   command=self.print_damage_sum)

        #Create the buttons
        self.attacker.pack(side=tkinter.TOP, anchor="w")
        self.attacker_level_set.pack(side=tkinter.TOP, anchor="w")
        self.attacker_item1.pack(side=tkinter.TOP, anchor="w")
        self.attacker_item2.pack(side=tkinter.TOP, anchor="w")
        self.attacker_item3.pack(side=tkinter.TOP, anchor="w")
        self.attacker_item4.pack(side=tkinter.TOP, anchor="w")
        self.attacker_item5.pack(side=tkinter.TOP, anchor="w")
        self.attacker_item6.pack(side=tkinter.TOP, anchor="w")
        self.attacker_percent_damages.pack(side=tkinter.TOP, anchor="w")
        self.attacker_flat_damages.pack(side=tkinter.TOP, anchor="w")
        self.attacker_crit_option.pack(side=tkinter.TOP, anchor="w")

        self.defender.pack(side=tkinter.TOP, anchor="e")
        self.defender_level_set.pack(side=tkinter.TOP, anchor="e")
        self.defender_item1.pack(side=tkinter.TOP, anchor="e")
        self.defender_item2.pack(side=tkinter.TOP, anchor="e")
        self.defender_item3.pack(side=tkinter.TOP, anchor="e")
        self.defender_item4.pack(side=tkinter.TOP, anchor="e")
        self.defender_item5.pack(side=tkinter.TOP, anchor="e")
        self.defender_item6.pack(side=tkinter.TOP, anchor="e")
        self.defender_block_option.pack(side=tkinter.TOP, anchor="e")

        self.general_damage.pack(side=tkinter.TOP)

        self.calculate_button.pack(side=tkinter.BOTTOM)

 
    def print_damage_sum(self):  
        #TODO CRITS ARE BUGGED ... sometimes.......

        #ew. reformulate
        if self.attacker_level.get() != Central.ATTACKER_LEVEL_DEFAULT:
            attacker_level_as_int = (int) (self.attacker_level.get())  
            attacker_level = attacker_level_as_int if (attacker_level_as_int >= 1) and (attacker_level_as_int <= 25) else 1
        else:
            attacker_level = 1

        if self.defender_level.get() != Central.DEFENDER_LEVEL_DEFAULT:
            defender_level_as_int = (int) (self.defender_level.get())
            defender_level = defender_level_as_int if (defender_level_as_int >= 1) and (defender_level_as_int <= 25) else 1
        else:
            defender_level = 1

        with open("placeholder_hero_metadata", "r") as f:
            placeholder_hero_metadata = ast.literal_eval(f.read())

        with open("hero_metadata", "r") as f:
            all_hero_metadata = ast.literal_eval(f.read())

            if self.attacker_hero.get() in all_hero_metadata:
                attacker_hero = Hero(all_hero_metadata[self.attacker_hero.get()])
            else:
                attacker_hero = Hero(placeholder_hero_metadata)

            if self.defender_hero.get() in all_hero_metadata:
                defender_hero = Hero(all_hero_metadata[self.defender_hero.get()])
            else:
                defender_hero = Hero(placeholder_hero_metadata)

        print(attacker_hero.get_hero_name() + " attacking " + defender_hero.get_hero_name() + "...")

        with open("item_metadata", "r") as f:
            all_item_metadata = ast.literal_eval(f.read())

        attacker_items = []
        for item in [self.attacker_item1_choice, self.attacker_item2_choice, self.attacker_item3_choice,
                        self.attacker_item4_choice, self.attacker_item5_choice, self.attacker_item6_choice]:
            item_name = item.get()
            if item_name in all_item_metadata:
                attacker_items.append(Item(all_item_metadata[item_name]))


        defender_items = []
        for item in [self.defender_item1_choice, self.defender_item2_choice, self.defender_item3_choice,
                        self.defender_item4_choice, self.defender_item5_choice, self.defender_item6_choice]:
            item_name = item.get()
            if item_name in all_item_metadata:
                defender_items.append(Item(all_item_metadata[item_name]))



        damage_sources = [] #Reformulate
        attacker_hero_damage = attacker_hero.get_expected_attack_damage()
        attacker_primary_attr = attacker_hero.get_primary_attr()
        if attacker_primary_attr == "STR":
            attacker_hero_damage += (attacker_hero.get_strength_gain() * (attacker_level - 1))
            for item in attacker_items:
                attacker_hero_damage += item.get_strength()
        elif attacker_primary_attr == "AGI":
            attacker_hero_damage += (attacker_hero.get_agility_gain() * (attacker_level - 1))
            for item in attacker_items:
                attacker_hero_damage += item.get_agility()
        elif attacker_primary_attr == "INT":
            attacker_hero_damage += (attacker_hero.get_intelligence_gain() * (attacker_level - 1))
            for item in attacker_items:
                attacker_hero_damage += item.get_intelligence()
        damage_sources.append(PhysicalDamage(attacker_hero_damage))

        percentages_to_create_bonuses = self.generate_list_of_values(self.attacker_percent_var.get(), Central.ATTACKER_PERCENT_BONUS_DEFAULT)
        attacker_percentage_bonuses = [PercentageDamageBonus(percentage_bonus) for percentage_bonus in percentages_to_create_bonuses if percentage_bonus is not None] #percentage bonus is None when bad input is encountered

        flat_bonuses = self.generate_list_of_values(self.attacker_flat_var.get(), Central.ATTACKER_FLAT_BONUS_DEFAULT, False)
        attacker_flat_bonuses = [FlatDamageBonus(flat_bonus) for flat_bonus in flat_bonuses if flat_bonus is not None] #flat bonus is None when bad input is encountered
        for item in attacker_items:
            attacker_flat_bonuses.append(FlatDamageBonus(item.get_damage()))

        attacker_crit_sources = []
        if self.attacker_crit_var.get() != Central.ATTACKER_CRIT_SOURCE_DEFAULT:
            with open("critical_strike_metadata", "r") as f:
                crit_source_metadata = ast.literal_eval(f.read())
            crit_source = crit_source_metadata[self.attacker_crit_var.get()]
            attacker_crit_sources.append(CriticalStrike(Percentage(crit_source["crit chance"]), Percentage(crit_source["crit multiplier"])))
            print("\nAttacker boosted by crit source " + self.attacker_crit_var.get())

        defender_block_sources = []
        if self.defender_block_var.get() != Central.DEFENDER_BLOCK_SOURCE_DEFAULT:
            with open("block_source_metadata", "r") as f:
                block_source_metadata = ast.literal_eval(f.read())
            block_source = block_source_metadata[self.defender_block_var.get()]
            defender_block_sources.append(DamageBlock(block_source["block amount"], Percentage(block_source["block chance"])))
            print("\nDefender shielded by block source " + self.defender_block_var.get())

        defender_armor = defender_hero.get_base_armor() + (defender_hero.get_agility_gain() * (defender_level - 1) * Central.AGILITY_TO_ARMOR_CONVERSION_FACTOR)
        defender_base_magic_resistance = defender_hero.get_base_magic_resistance()
        defender_strength = defender_hero.get_strength() + defender_hero.get_strength_gain() * (defender_level - 1)
        defender_magic_resistances = []
        for item in defender_items:
            defender_armor += (item.get_agility() * Central.AGILITY_TO_ARMOR_CONVERSION_FACTOR)
            defender_armor += item.get_armor()
            defender_armor += item.get_strength()
            defender_magic_resistances.append(item.get_magic_resistance())

        general_damage_multipliers = self.generate_list_of_values(self.general_damage_multipliers.get(), Central.GENERAL_DAMAGE_MULTIPLIER_DEFAULT)

        total_damage = calculate_total_damage(damage_sources, attacker_percentage_bonuses, attacker_flat_bonuses, attacker_crit_sources, 
                            defender_block_sources, defender_armor, defender_base_magic_resistance, defender_strength, defender_magic_resistances,
                            general_damage_multipliers)
        print("\nTotal damage from attacker to defender: " + str(total_damage))

    def generate_list_of_values(self, value_string, default_string, generate_percentage=True):
        values_returned = []
        if value_string != default_string:
            values = value_string.split(",")
            if isinstance(values, str):
                values = [values]
            for value in values:
                print(value)
                try:
                    if generate_percentage:
                        safe_value = Percentage(value)
                    else:
                        safe_value = (int) (integer_string)
                    values_returned.append(safe_value)
                except:
                    print("\nInvalid " + ("percentage" if generate_percentage else "integer") + " given: " + value + ". Skipping over value.")
        return values_returned

    def run(self):
        self.mainloop()
 
app = Central(tkinter.Tk())
app.run()