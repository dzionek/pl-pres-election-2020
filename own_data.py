"""
Module with constants used in the analysis.
"""

from plotly.express import colors

candidates = [
	'Robert BIEDROŃ',
	'Krzysztof BOSAK',
	'Andrzej Sebastian DUDA',
	'Szymon Franciszek HOŁOWNIA',
	'Marek JAKUBIAK',
	'Władysław Marcin KOSINIAK-KAMYSZ',
	'Mirosław Mariusz PIOTROWSKI',
	'Paweł Jan TANAJNO',
	'Rafał Kazimierz TRZASKOWSKI',
	'Waldemar Włodzimierz WITKOWSKI',
	'Stanisław Józef ŻÓŁTEK'
]

candidates_colors = {
    'Robert BIEDROŃ' : colors.sequential.Reds,
    'Krzysztof BOSAK' : colors.sequential.Greys,
    'Andrzej Sebastian DUDA' : colors.sequential.Blues,
    'Szymon Franciszek HOŁOWNIA' : colors.sequential.YlOrBr,
    'Marek JAKUBIAK' : colors.sequential.Purples,
    'Władysław Marcin KOSINIAK-KAMYSZ' : colors.sequential.Greens,
    'Mirosław Mariusz PIOTROWSKI' : colors.sequential.matter,
    'Paweł Jan TANAJNO' : colors.sequential.PuBu,
    'Rafał Kazimierz TRZASKOWSKI' : colors.sequential.Oranges,
    'Waldemar Włodzimierz WITKOWSKI' : colors.sequential.YlOrRd,
    'Stanisław Józef ŻÓŁTEK' : colors.sequential.tempo
}

poland_center = {
	"lat": 52,
	"lon": 19.1451
}

poland_zoom = 5.2

opacity = 0.8

map_margin = {
	"r":0, "t":0, "l":0, "b":0
}

parties_2019 = [
	'KOALICYJNY KOMITET WYBORCZY KOALICJA OBYWATELSKA PO .N IPL ZIELONI - ZPOW-601-6/19',
	'KOMITET WYBORCZY PRAWO I SPRAWIEDLIWOŚĆ - ZPOW-601-9/19'
]

simplify_party_dict = {
	'KOALICYJNY KOMITET WYBORCZY KOALICJA OBYWATELSKA PO .N IPL ZIELONI - ZPOW-601-6/19': 'Koalicja Obywatelska',
	'KOMITET WYBORCZY PRAWO I SPRAWIEDLIWOŚĆ - ZPOW-601-9/19': 'Prawo i Sprawiedliwość'
}

parties_to_candidates = {
	'Koalicja Obywatelska': 'Rafał Kazimierz TRZASKOWSKI',
	'Prawo i Sprawiedliwość': 'Andrzej Sebastian DUDA' 
}

parties_2019_colors = {
	'KOALICYJNY KOMITET WYBORCZY KOALICJA OBYWATELSKA PO .N IPL ZIELONI - ZPOW-601-6/19': candidates_colors['Rafał Kazimierz TRZASKOWSKI'],
	'KOMITET WYBORCZY PRAWO I SPRAWIEDLIWOŚĆ - ZPOW-601-9/19': candidates_colors['Andrzej Sebastian DUDA']
}
