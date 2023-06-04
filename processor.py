"""
" processor class
"""
from selenium import webdriver
from processor_meta import MetaProcessor
from processor_link import LinkProcessor
from processor_title import TitleProcessor
from processor_table import TableProcessor

class Processor:
    def read(self, driver:webdriver)->dict:
        out = {}
        out['url'] = driver.current_url
        out['title'] = self._title.read(driver)
        out['meta'] = self._meta.read(driver)
        out['links'] = self._link.read(driver)
        out['tables'] = self._table.read(driver)
        print(out)
        return out
    def __init__(self):
        self._title = TitleProcessor()
        self._meta  = MetaProcessor()
        self._link  = LinkProcessor()
        self._table = TableProcessor()
