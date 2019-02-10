class UIUnitTestInjector():

    def __init__(self, attacker_hero_name, defender_hero_name, attacker_hero_level, defender_hero_level,
                    attacker_item_choices, defender_item_choices, attacker_percent_var, attacker_flat_var,
                    defender_block_var, attacker_crit_var, general_damage_multipliers):
        #Sanity check input strings and prune out all bad input values from input lists so the Central object
        #doesn't have to sanity check
        assert isinstance(attacker_hero_name, str)
        self.attacker_hero_name = attacker_hero_name
        assert isinstance(defender_hero_name, str)
        self.defender_hero_name = defender_hero_name
        assert isinstance(attacker_hero_level, str)
        self.attacker_hero_level = attacker_hero_level
        assert isinstance(defender_hero_level, str)
        self.defender_hero_level = defender_hero_level
        assert isinstance(attacker_item_choices, list)
        self.attacker_item_choices = [item_choice for item_choice in attacker_item_choices if isinstance(item_choice, str)]
        assert isinstance(defender_item_choices, list)
        self.defender_item_choices = [item_choice for item_choice in defender_item_choices if isinstance(item_choice, str)]
        assert isinstance(attacker_percent_var, str)
        self.attacker_percent_var = attacker_percent_var
        assert isinstance(attacker_flat_var, str)
        self.attacker_flat_var = attacker_flat_var
        assert isinstance(defender_block_var, str)
        self.defender_block_var = defender_block_var
        assert isinstance(attacker_crit_var, str)
        self.attacker_crit_var = attacker_crit_var
        assert isinstance(general_damage_multipliers, str)
        self.general_damage_multipliers = general_damage_multipliers

    def get_attacker_hero_name(self):
        return self.attacker_hero_name

    def get_defender_hero_name(self):
        return self.defender_hero_name

    def get_attacker_hero_level(self):
        return self.attacker_hero_level

    def get_defender_hero_level(self):
        return self.defender_hero_level

    def get_attacker_item_choices(self):
        return self.attacker_item_choices

    def get_defender_item_choices(self):
        return self.defender_item_choices

    def get_attacker_percent_var(self):
        return self.attacker_percent_var

    def get_attacker_flat_var(self):
        return self.attacker_flat_var

    def get_defender_block_var(self):
        return self.defender_block_var

    def get_attacker_crit_var(self):
        return self.attacker_crit_var

    def get_general_damage_multipliers(self):
        return self.general_damage_multipliers