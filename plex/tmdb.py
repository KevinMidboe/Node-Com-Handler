#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-02-08 14:00:04
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-02-16 17:08:08

import requests
from pprint import pprint
try:
	from plexSearch import plexSearch
except ImportError:
	from plex.plexSearch import plexSearch

apiKey = "9fa154f5355c37a1b9b57ac06e7d6712"


def tmdbSearch(query, page=1):
	payload = {"api_key":apiKey, "query":str(query), "language":"en.US", "page":str(page), }
	header = {'Accept': 'application/json'}

	try:
		r = requests.get("https://api.themoviedb.org/3/search/multi", params=payload, headers=header)
	except requests.exceptions.ConnectionError:
		return {"errors": "Could not connecting to: tmdb.com"}
	except requests.exceptions.Timeout:
		return {"errors": "Request timed out."}
	except requests.exceptions.TooManyRedirects:
		return {"errors": "Too many redirects, do you full network access?"}

	if r.status_code == 401:
		return {"errors": "api key is not valid."}
	elif r.status_code == 404:
		return {"errors": "Please check url. (404)"}
	elif r.status_code == requests.codes.ok and r.json()['total_results'] == 0:
		return {"errors": "No results found."}
	

	return r.json()


if __name__ == "__main__":
	import sys
	print(sys.argv)
	if len(sys.argv) > 2:
		pprint(tmdbSearch(sys.argv[1], int(sys.argv[2])))
	elif len(sys.argv) > 1:
		pprint(tmdbSearch(sys.argv[1]))
	else:
		pprint(tmdbSearch("star+wars",1))