#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-02-08 14:00:04
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-02-08 14:06:48

from requests import get

tmdbBaseURL = "https://api.themoviedb.org/3/"

def tmdbSearch(query, page=1):
	requestType = "search/multi?"
	requestAPI = "api_key=" + "9fa154f5355c37a1b9b57ac06e7d6712"
	requestQuery = "&query=" + str(query)
	requestLanguage = "&language=en.US"
	requestPage = "&page="+str(page)

	url = tmdbBaseURL + requestType + requestAPI + requestQuery + requestLanguage + requestPage
	# url = "https://api.themoviedb.org/3/search/multi?include_adult=false&query=home%20alone&language=en-US&api_key=9fa154f5355c37a1b9b57ac06e7d6712"

	response = get(url)
	print(response.status_code)
	if response.status_code == 200:
		return response.content

if __name__ == "__main__":
	print(tmdbSearch("Big bang"))