#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-02-08 14:00:04
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-02-08 22:50:17

from requests import get

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
	requestType = "search?"
	requestQuery = "query=" + str(query)
	header = {'Accept': 'application/json'}

	url = plexBaseURL + requestType + requestQuery
	response = get(url, headers=header)

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
	tiss = plexSearch("star+wars")
	for al in tiss:
		if (al['year']==2015):
			print('thishsihis')