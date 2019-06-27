#!/usr/bin/python
# coding:utf-8

import requests

params = {
	"action": "query",
	"list": "search",
	"srsearch": "",
	"format": "json",
	"sroffset": 10,
}
url = "https://en.wikipedia.org/w/api.php"


if __name__ == '__main__':
    keyword = raw_input('Keyword : ')
    params['srsearch'] = keyword
    s = requests.Session()
    totalhits = 11
    while params['sroffset'] < totalhits:
	    ret = s.get(url, params=params)
	    for r in ret.json()['query']['search']:
	    	print
	    	print r['title'].encode('utf-8')
	    	print r['snippet'].encode('utf-8')
	    	print
	    totalhits = ret.json()['query']['searchinfo']['totalhits']
	    params['sroffset'] = ret.json()['continue']['sroffset'] if 'continue' in ret.json() else totalhits
