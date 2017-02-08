#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-02-08 14:00:04
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-02-08 23:19:53

from requests import get
try:
	from plexSearch import plexSearch
except ImportError:
	from plex.plexSearch import plexSearch

tmdbBaseURL = "https://api.themoviedb.org/3/"

def checkPlexExistance(tmdb, plex):
	# THIS IS ONLY COMPARED ON YEAR
	yearList = [movie["year"] for movie in plex]
	print(yearList)

	for movie in tmdb["movies"]:
		print(movie["year"])
		movie["exists"] = movie["year"] in str(yearList)
	
	return tmdb

def createTMDBResultList(resContent):
	movies = []
	tvshows = []

	for res in resContent["results"]:
		if res["media_type"] == "movie":
			id = res["id"]
			title = res["original_title"]
			year = res["release_date"][:4]
			poster_path = res["poster_path"]

			movies.append({"id": id, "title": title, "year": year, "poster_path": poster_path})

		elif res["media_type"] == "tv":
			id = res["id"]
			name = res["original_name"]
			year = res["first_air_date"][:4]
			poster_path = res["poster_path"]

			tvshows.append({"id": id, "title": name, "year": year, "poster_path": poster_path})

	return { "movies": movies, "tvshows": tvshows }


def tmdbSearch(query, page=1):
	requestType = "search/multi?"
	requestAPI = "api_key=" + "9fa154f5355c37a1b9b57ac06e7d6712"
	requestQuery = "&query=" + str(query)
	requestLanguage = "&language=en.US"
	requestPage = "&page="+str(page)

	url = tmdbBaseURL + requestType + requestAPI + requestQuery + requestLanguage + requestPage
	print(url)

	response = get(url)
	if response.status_code == 200:
		resContent = response.json()

		plexSearchRes = plexSearch(query)
		tmdbSearchRes = createTMDBResultList(resContent)

		return checkPlexExistance(tmdbSearchRes, plexSearchRes)


if __name__ == "__main__":
	import sys
	print(sys.argv)
	if len(sys.argv) > 2:
		print(tmdbSearch(sys.argv[1], int(sys.argv[2])))
	elif len(sys.argv) > 1:
		print(tmdbSearch(sys.argv[1]))
	else:
		print(tmdbSearch("star+wars",1))