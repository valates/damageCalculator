from attack_modifier import AttackModifier

class Bash(AttackModifier):

	BASH_EFFECT_NAME = "bash"

	@abstractmethod #TODO
	def __init__(self, bash_chance, bash_duration):
		self.bash_chance = bash_chance
		self.bash_duration = bash_duration

	def get_effect(self):
		return [self.bash_chance, self.bash_duration]

	def get_effect_type(self):
		return BASH_EFFECT_NAME