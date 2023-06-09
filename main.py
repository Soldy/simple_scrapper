"""
" Simple scrapper main
"""
import sys
import json
import scrapper


log = []
with scrapper.ScrapperLayer() as scrap:
    file = open('out.json', 'w')
    result = {}
    result['url'] = sys.argv[1]
    result['out'] = scrap.pageGet(sys.argv[1])
    log.append(result)
    file.write(json.dumps(log))
    file.close()
