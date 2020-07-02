"""
Utility functions for the analysis.
"""

from own_data import simplify_party_dict


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

def get_last_name(full_name: str) -> str:
    """Get the last name from full name.
	
	Args:
		full_name: The full official name.

	Return:
		The last name in title case format.

    """
    return full_name.split(' ')[-1].title()
