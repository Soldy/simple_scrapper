"""
" Harmony Processor
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class HarmonyProcessor:
    def readClassCount(self, driver:webdriver):
        for harmony in driver.find_elements(By.XPATH, ".//*"):
            try:
               harmony.get_attribute("class")
            except:
               continue
            if harmony.get_attribute("class") in self._classes:
                self._classes[harmony.get_attribute("class")] += 1
            else:
                self._classes[harmony.get_attribute("class")] = 1
            self.readClassCount(harmony)
    def readTagCount(self, driver:webdriver):
        for harmony in driver.find_elements(By.XPATH, ".//*"):
            try:
               harmony.tag_name
            except:
               continue
            if harmony.tag_name in self._tags:
                self._tags[harmony.tag_name] += 1
            else:
                self._tags[harmony.tag_name] = 1
            self.readTagCount(harmony)
    def readHeadTagCount(self, driver:webdriver):
        for harmony in driver.find_elements(By.XPATH, ".//*"):
            try:
               harmony.tag_name
            except:
               continue
            if harmony.tag_name in self._head_tags:
                self._head_tags[harmony.tag_name] += 1
            else:
                self._head_tags[harmony.tag_name] = 1
            self.readHeadTagCount(harmony)
    def read(self, driver:webdriver)->dict:
        self.readClassCount(driver.find_elements(By.TAG_NAME, "body")[0])
        self.readTagCount(driver.find_elements(By.TAG_NAME, "body")[0])
        self.readHeadTagCount(driver.find_elements(By.TAG_NAME, "head")[0])
        return {
            'head_tags' : self._head_tags,
            'tags' : self._tags,
            'classes' : self._classes
        }
    def __init__(self):
        self._classes = {}
        self._tags = {}
        self._head_tags = {}
        self._class_error = []
