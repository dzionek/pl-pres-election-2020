def comma_to_dot(comma_number: str) -> float:
	"""Transform the decimal separator from comma to dot."""
	return float(comma_number.replace(',', '.'))
