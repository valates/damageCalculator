class Percentage():

	def __init__(self, percentage):
		assert isinstance(percentage, str)
		assert percentage != "" #Empty string cannot be converted to a float
		percentage_as_float_multiplier = (float(percentage.replace("%", ""))/100)
		self.percentage_multiplier = percentage_as_float_multiplier

	def get_percentage_multiple(self):
		return self.percentage_multiplier

	def get_string_representation(self):
		return ((str) (self.percentage_multiplier * 100)) + "%"