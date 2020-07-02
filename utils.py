"""
Utility functions for the analysis.
"""

simplify_party_dict = {
	'KOALICYJNY KOMITET WYBORCZY KOALICJA OBYWATELSKA PO .N IPL ZIELONI - ZPOW-601-6/19': 'Koalicja Obywatelska',
	'KOMITET WYBORCZY PRAWO I SPRAWIEDLIWOŚĆ - ZPOW-601-9/19': 'Prawo i Sprawiedliwość'
}


def comma_to_dot(comma_number: str) -> float:
	"""Transform the decimal separator from comma to dot.
	
	Args:
		comma_number: number as a string with comma as a decimal separator

	Return:
		The dot-separated number corresponding to the given one.

	"""
	return float(comma_number.replace(',', '.'))


def simplify_party(full_party: str) -> str:
	"""Get the simplified name of the party

	Args:
		full_party: The official name of the party from the National Electoral Commission.

	Return:
		The simplified name of the party.

	"""
	if full_party not in simplify_party_dict.keys():
		return full_party
	else:
		return simplify_party_dict[full_party]
