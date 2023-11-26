"""
" Link Processor
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class LinkProcessor:
    def readLink(self, link)->list:
        out = {}
        out['text'] = link.text
        out['href'] = link.get_attribute("href")
        if link.get_attribute("title") != "":
            out['title'] = link.get_attribute("title")
        return out
    def read(self, driver:webdriver)->list:
        out = []
        for link in driver.find_elements(By.TAG_NAME, "a"):
            extra = self.readLink(link)
            if extra['href'] != "" and extra['href'] is not None:
                out.append(extra)
        return out
    def __init__(self):
        self._data = {}
