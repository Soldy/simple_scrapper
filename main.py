"""
Simple scrapper main loop
"""
import json
import scrapper

with scrapper.ScrapperLayer() as scrap:
    file = open('out.json', 'w')
    file.write(json.dumps(scrap.pageGet("https://wltest.dns-systems.net/")))
    file.close()
