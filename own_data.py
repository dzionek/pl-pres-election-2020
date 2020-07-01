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

map_margin = {"r":0,"t":0,"l":0,"b":0}
