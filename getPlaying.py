import xml.etree.ElementTree as ET
import os

def getXML_file():
	os.system('curl --silent midboe.ddns.net:32400/status/sessions > testXml.xml')

def main():
	getXML_file()

	tree = ET.parse('testXml.xml')
	root = tree.getroot()

	print('\tCur: \t', root.get('size'), '\n')

	for video in root.findall('Video'):
		parentName = video.get('grandparentTitle')
		name = video.get('title')
		user = video.find('User').get('title')
		state = video.find('Player').get('state')

		print('\tTitle: \t', name, '\n\tSeries: ', parentName, '\n\tState: \t', state, '\n\tUser: \t', user, '\n')
		

main()
