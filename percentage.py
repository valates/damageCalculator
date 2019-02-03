class Percentage():

	def __init__(self, percentage):
		assert(isinstance(percentage, str))
		percentage_as_float_multiplier = (float(percentage.replace("%", ""))/100)
		self.percentage_multiplier = percentage_as_float_multiplier

	def get_percentage_multiple(self):
		return self.percentage_multiplier

	def get_string_representation(self):
		return ((str) (self.percentage_multiplier * 100)) + "%"