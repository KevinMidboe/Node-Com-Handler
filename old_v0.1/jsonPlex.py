import json
import xml.etree.ElementTree as ET
from collections import OrderedDict


def plex():
	# XML parsing, creates a tree and saves the root node as root
	tree = ET.parse('plex.xml')
	root = tree.getroot()

	plex_dict = OrderedDict()
	i = 0
	# The root node named MediaContainer has a size variable that holds number of active processes.
	# If this is '0' then there are none playing, no need to compute.
	if (root.get('size') != '0'):

		# Get load of CPU and I/O
		plex_dict['load'] = '0.05 0.05 0.05 1/262 15997'
		plex_dict['cur'] = root.get('size')

		# Goes through all the 'video' elements in MediaContainer
		for video in root.findall('Video'):
			playing_dict = OrderedDict()
			if (video.get('type') == 'movie'):
				playing_dict['title'] = video.get('title')

			elif (video.get('type') == 'episode'):
				playing_dict['title'] = video.get('title')
				playing_dict['series'] = video.get('grandparentTitle')

			playing_dict['progress'] = "{0:0.1f}".format(float(video.find('TranscodeSession').get('progress')))
			playing_dict['state'] = video.find('Player').get('state')
			playing_dict['player'] = video.find('Player').get('platform')
			playing_dict['user'] = video.find('User').get('title')

			plex_dict[i] = playing_dict
			i+=1

		return plex_dict
	else: 
		return 'Null playing'

plex_dict = plex()


# plex_dict = {
# 	"Load": '0.05 0.05 0.05 1/262 15997',
# 	"Cur":  '2',
# }

# playing_1 = {'Playing': 'Interstellar', 
# 	'State': 'Playing', 'Prog': '58.6',
# 	'Device': 'iPhone', 'User': 'KevinMidboe'}

# playing_2 = {'Playing': 'Home Alone', 
# 	'State': 'Stopped', 'Prog': '32.9',
# 	'Device': 'Samsung TV', 'User': 'MajElg'}

# # print(playing_1, playing_2)

# i = 5

# plex_dict[i] = playing_1
# plex_dict.update(playing_2)

# print(plex_dict)

# plex_dict["Playing"][0].update({'State' : 'Playing'})
print(plex_dict)
json_plex = json.loads(json.dumps(plex_dict))
print(json_plex)
# print(json_plex['Playing'][0])

for key, item in plex_dict.items():
	print(str(key) + '\t', str(item) + '\n')
	try:
	    key = int(key)
	    # print(item)
	except ValueError:
	    pass  # it was a string, not an int.


