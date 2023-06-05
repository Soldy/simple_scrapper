"""
" Form Processor
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

class FormProcessor:
    def readForm(self, form)->list:
        out = []
        for input_ in form.find_elements(By.TAG_NAME, "input"):
            extra = self.readInput(input_)
            out.append(extra)
        return out
    def readInput(self, input_)->list:
        out = {}
        if input_.get_attribute("value") != "" and input_.get_attribute("value") is not None:
            out['value'] = input_.get_attribute("value")
        if input_.get_attribute("praceholder") != "" and input_.get_attribute("praceholder") is not None:
            out['placeholder'] = input_.get_attribute("placeholder")
        if input_.get_attribute("name") != "" and input_.get_attribute("name") is not None:
            out['name'] = input_.get_attribute("name")
        if input_.get_attribute("type") != "" and input_.get_attribute("type") is not None:
            out['type'] = input_.get_attribute("type")
        return out
    def read(self, driver:webdriver)->list:
        out = []
        for form in driver.find_elements(By.TAG_NAME, "form"):
            extra = self.readForm(form)
            out.append(extra)
        return out
    def __init__(self):
        self._data = {}
