"""
" processor class
"""
from selenium import webdriver
from processor_helper import fullShot
from processor_helper import scrollDown
from processor_harmony import HarmonyProcessor
from processor_meta import MetaProcessor
from processor_link import LinkProcessor
from processor_title import TitleProcessor
from processor_table import TableProcessor
from processor_form import FormProcessor

class Processor:
    def read(self, driver:webdriver)->dict:
        scrollDown(driver);
        fullShot(driver);
        out = {}
        out['harmony'] = self._harmony.read(driver)
        out['url'] = driver.current_url
        out['title'] = self._title.read(driver)
        out['meta'] = self._meta.read(driver)
        out['form'] = self._form.read(driver)
        out['links'] = self._link.read(driver)
        out['tables'] = self._table.read(driver)
        print(out)
        return out
    def __init__(self):
        self._harmony  = HarmonyProcessor()
        self._title = TitleProcessor()
        self._meta  = MetaProcessor()
        self._form = FormProcessor()
        self._link  = LinkProcessor()
        self._table = TableProcessor()
