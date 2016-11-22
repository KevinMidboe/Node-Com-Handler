import json
from collections import OrderedDict

json_string = '{"movie_title": "Interstellar", "progress": "82.3", "state": "Playing", "player": "Safari"}'

parsed_json = json.loads(json_string)

print(parsed_json)
# {'state': 'Playing', 'movie_title': 'Interstellar', 'player': 'Safari', 'progress': '82.3'}

print(parsed_json['movie_title'], parsed_json['state'])
# {'progress': '82.3', 'player': 'Safari', 'movie_title': 'Interstellar', 'state': 'Playing'}
d = {
	'Title': 'Interstellar',
    'Prog': '82.23',
    'State': 'Playing',
    'Player': 'Safari',
    'User': 'KevinMidboe'
}

d['Device'] = 'iPhone'

packed_json = json.dumps(d, sort_keys=True)

print(packed_json)
# {"Device": "iPhone", "Player": "Safari", "Prog": "82.23", "State": "Playing", "Title": "Interstellar", "User": "KevinMidboe"}

parsed_json = json.loads(packed_json, object_pairs_hook=OrderedDict)

print(parsed_json)
# OrderedDict([('Device', 'iPhone'), ('Player', 'Safari'), ('Prog', '82.23'), ('State', 'Playing'), ('Title', 'Interstellar'), ('User', 'KevinMidboe')])

print(parsed_json['Title'], parsed_json['Device'])
# OrderedDict([('Device', 'iPhone'), ('Player', 'Safari'), ('Prog', '82.23'), ('State', 'Playing'), ('Title', 'Interstellar'), ('User', 'KevinMidboe')])

for a, b in parsed_json.items():
	print(a + '\t', b)
	True
	# Device	 iPhone
	# Player	 Safari
	# Prog	 82.23
	# State	 Playing
	# Title	 Interstellar
	# User	 KevinMidboe

plex_dict = {"plex" : {}}
plex_dict["plex"] = {"plex_info": {}, "plex_playing": {}}

print(plex_dict)

plex_dict["plex"]["plex_info"] = {'Cur': '2', 'Load': '0.05 0.05 0.05 1/262 15997'}

print(plex_dict)

plex_dict['plex']['plex_playing'].update( 
	{'Title' : 'Interstellar',
		'Prog' : '82.2%',
		'State': 'Playing',
		'Player': 'Safari',
		'User': 'KevinMidboe'}
)

plex_dict['plex']["plex_playing"].update( 
	{'Title' : 'Robo Cop 2',
		'Prog' : '34.8%',
		'State': 'Paused',
		'Player': 'LG TV',
		'User': 'MajElg'}
)

print('\n' + str(plex_dict))
# {'plex': {'Prog': '82.2%', 'State': 'Playing', 'User': 'KevinMidboe', 'Title': 'Interstellar', 'Player': 'Safari'}}

# plex_json = json.loads(json.dumps(plex_dict))

# print(plex_json['plex'].get('Title'))
# # Interstellar

# for key, value in plex_json['plex'].items():
# 	True
# 	print(key + '\t', value)
# 	# Title	 Interstellar
# 	# Prog	 82.2%
# 	# State	 Playing
# 	# Player	 Safari
# 	# User	 KevinMidboe