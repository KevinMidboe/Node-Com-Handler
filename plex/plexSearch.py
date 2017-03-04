#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-02-08 14:00:04
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-02-18 11:37:08

import requests
from pprint import pprint

plexBaseURL = "http://10.0.0.41:32400/"

def getMovieInfo(item):
	title = item["title"]
	year = item["year"]
	rating = item["rating"]
	art = item["art"]
	thumb = item["thumb"]

	for mediaInfo in item["_children"]:
		if mediaInfo["_elementType"] == "Media":
			container = mediaInfo["container"]
			resolution = mediaInfo["videoResolution"]
			bitrate = mediaInfo["bitrate"]
			videoCodec = mediaInfo["videoCodec"]
			videoFrameRate = mediaInfo["videoFrameRate"]

	return {"title":title, "year":year, "rating":rating, "container":container, 
		"resolution":resolution, "bitrate":bitrate, "videoCodec":videoCodec,
		"videoFrameRate":videoFrameRate, "art":art, "thumb":thumb}

def getShowInfo(item):
	media = []

	title = item["title"]
	year = item["year"]
	rating = item["rating"]
	art = item["art"]
	thumb = item["thumb"]
	seasons = item["childCount"]
	episodes = item["leafCount"]

	return {"title":title, "year":year, "seasons":seasons, "episodes":episodes, "rating":rating,
		"art":art, "thumb":thumb}



def plexSearch(query):
	payload = {"query":query, "type":"1,2"}
	header = {'Accept': 'application/json'}
	r = requests.get(plexBaseURL+"search",params=payload, headers=header)

	rObject = r.json()["MediaContainer"]
	if (r.status_code != requests.codes.ok or rObject["size"] == 0):
		return {"errors": "Nothing found for query: " + query}

	return rObject["Metadata"]


## MAJOR TODO
# Seems to be a change in the return obj.
# This looks way more like json. Need to re-write all this.
# IDEA: Send the size and resolution for comaprison
# No this is for a admin page. OR maybe a github project for 
# people wanting to update movies. MAJOR IDEA HERE NOW! :D
def plexXMLSearch(query):
	print(query)
	requestType = "search?"
	requestQuery = "query=" + str(query)
	header = {'Accept': 'application/json'}

	url = plexBaseURL + requestType + requestQuery
	response = requests.get(url, headers=header)

	pprint(response.json())
	if response.status_code == 200:
		resContent = response.json()
		media = []

		for child in resContent["_children"]:
			cType = child["type"]
			if cType == "movie":
				media.append(getMovieInfo(child))
			elif cType == "show":
				media.append(getShowInfo(child))

		return media



if __name__ == "__main__":
	# print(plexSearch("star+wars"))
	pprint(plexSearch("star"))
