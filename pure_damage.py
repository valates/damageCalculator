from damage import Damage

class PureDamage(Damage):

	def __init__(self, damage_amount):
		super().__init__(damage_amount)

	def get_damage_quantity(self):
		return super().get_damage_quantity()