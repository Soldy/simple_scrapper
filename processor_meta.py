"""
" Meta info Processor
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from processor_helper import getAttributes

class MetaProcessor:
    def read(self, driver:webdriver)->list:
        out = []
        for meta in driver.find_elements(By.TAG_NAME, "meta"):
            out.append(getAttributes(meta))
        return out
    def __init__(self):
        self._data = {}
