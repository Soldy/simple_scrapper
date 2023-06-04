"""
Simple scrapper main
"""
import sys
import json
import scrapper

with scrapper.ScrapperLayer() as scrap:
    file = open('out.json', 'w')
    file.write(json.dumps(scrap.pageGet(sys.argv[1])))
    file.close()
