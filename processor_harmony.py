"""
" Harmony Processor
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class HarmonyProcessor:
    def readLoop(self, driver:webdriver):
        for harmony in driver.find_elements(By.XPATH, ".//*"):
            self.readClass(harmony)
            self.readTag(harmony)
            self.readId(harmony)
    def readClass(self, driver:webdriver):
        _class = ''
        try:
           _class = driver.get_attribute("class")
        except:
           return _class
        if _class in self._classes:
            self._classes[_class] += 1
        else:
            self._classes[_class] = 1
        self._class_order.append(_class)
        return _class
    def readTag(self, driver:webdriver):
        _tag = ''
        try:
           _tag = driver.tag_name
        except:
           return _tag
        if _tag in self._tags:
            self._tags[_tag] += 1
        else:
            self._tags[_tag] = 1
        self._tag_order.append(_tag)
        return _tag
    def readHeadTag(self, driver:webdriver):
        _tag = ''
        try:
           _tag = driver.tag_name
        except:
           return _tag
        if _tag in self._tags:
            self._head_tags[_tag] += 1
        else:
            self._head_tags[_tag] = 1
        return _tag
    def readId(self, driver:webdriver):
        _id = ''
        try:
           _id = harmony.get_attribute("id")
        except:
           return _id
        if _id in self._ids:
            self._ids[_id] += 1
        else:
            self._ids[_id] = 1
        self._id_order.append(_id)
        return _id
    def read(self, driver:webdriver)->dict:
        self.readLoop(driver.find_elements(By.TAG_NAME, "body")[0])
        self.readHeadTag(driver.find_elements(By.TAG_NAME, "head")[0])
        return {
            'head_tags' : self._head_tags,
            'tag_order' : self._tag_order,
            'tags' : self._tags,
            'ids' : self._ids,
            'id_order' : self._id_order,
            'class_order' : self._class_order,
            'classes' : self._classes
        }
    def __init__(self):
        self._class_order = []
        self._classes = {}
        self._tag_order = []
        self._tags = {}
        self._hybrid_order = []
        self._ids = {}
        self._id_order = []
        self._head_tags = {}
        self._class_error = []
