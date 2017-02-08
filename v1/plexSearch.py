#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-02-08 14:00:04
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-02-08 14:06:48

from requests import get

plexBaseURL = "http://10.0.0.41:32400/"

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
			if cType == "movie" or cType == "show":
				title = child["title"]
				year = child["year"]
				rating = child["rating"]
				art = child["art"]
				thumb = child["thumb"]

				if cType == "movie":
					for mediaInfo in child["_children"]:
						if mediaInfo["_elementType"] == "Media":
							container = mediaInfo["container"]
							resolution = mediaInfo["videoResolution"]
							bitrate = mediaInfo["bitrate"]
							videoCodec = mediaInfo["videoCodec"]
							videoFrameRate = mediaInfo["videoFrameRate"]

							media.append({"title":title, "year":year, "rating":rating, "container":container,
							 "resolution":resolution, "bitrate":bitrate, "videoCodec":videoCodec, 
							 "videoFrameRate":videoFrameRate, "art":art, "thumb":thumb})

				if cType == "show":
					seasons = child["childCount"]
					episodes = child["leafCount"]

					media.append({"title":title, "year":year, "seasons":seasons, "episodes":episodes, "rating":rating,
						"art":art, "thumb":thumb})

		return media



if __name__ == "__main__":
	print(plexSearch("star+wars"))