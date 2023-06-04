"""
" Offer Processor
"""
import re
import copy
from selenium import webdriver
from selenium.webdriver.common.by import By

def _priceRegExp(text:str, multi:int)->float:
    """ Regular expectation helper function. DRY regarding."""
    return float(multi*int(100*float(re.findall(r'\d+\.\d+', text)[0])))/100

class OfferProcessor:
    """ offer processor class """
    def _fail(self, name:str)->None:
        """ Fail manager function for debugging purposes. """
        self._errors[name]=True
        self._failed = True
    def _clean(self)->None:
        """ fail cleanup before every item """
        self._failed = False
        self._errors = {
            'title_header' : False,
            'title_tag' : False,
            'discount' : False,
            'price_holder' : False,
            'price' : False
        }
    def _priceHolder(self, package:webdriver)->webdriver:
        """ price holder processor. S.O.L.I.D. regarding."""
        price_holder = package.find_elements(By.CLASS_NAME,"package-price")
        if len(price_holder) < 1:
            self._fail('price_holder')
        return price_holder[0]
    def _title(self, element : webdriver)->str:
        header = element.find_elements(By.CLASS_NAME,"header")
        if len(header) < 1:
            self._fail('title_header')
            return ''
        tag = header[0].find_elements(By.TAG_NAME,"h3")
        if len(tag) < 1:
            self._fail('title_tag')
            return ''
        return tag[0].text
    # annual price
    def _price(self, element : webdriver)->float:
        price_element = element.find_elements(By.CLASS_NAME,"price-big")
        if len(price_element) < 1:
            self._fail('price')
            return 0
        if "per year" in element.text.lower():
            return _priceRegExp(price_element[0].text, 1)
        if "per month" in element.text.lower():
            return _priceRegExp(price_element[0].text, 12)
        self._fail('price')
        return 0
    # annual discount
    def _discount(self, element : webdriver):
        discount_element = element.find_elements(By.TAG_NAME,"p")
        if len(discount_element) < 1:
            return 0
        if "monthly price" in discount_element[0].text.lower():
            return _priceRegExp(discount_element[0].text, 12)
        if "yearly price" in discount_element[0].text.lower():
            return _priceRegExp(discount_element[0].text, 1)
        self._fail("discount")
        return 0
    def _package(self, package:webdriver)->dict:
        out={}
        self._clean()
        price_holder = self._priceHolder(package)
        out['title'] = self._title(package)
        if self._errors['price_holder'] is False:
            out['price'] = self._price(price_holder)
            out['discount'] = self._discount(price_holder)
        if self._failed:
            out['failed'] = True
            out['debug'] = copy.deepcopy(self._errors)
        return out
    def read(self, driver:webdriver)->list:
        """ element reader """
        out = []
        bounds = []
        order = []
        for package in driver.find_elements(By.CLASS_NAME, "package"):
            print(package)
            bounds.append(self._package(package))
        order = sorted(range(len(bounds)), key = lambda i: bounds[i]['price'],reverse=True)
        for i in order:
            out.append(bounds[i])
        return out
    def __init__(self):
        self._data = {}
        self._failed = False
        self._errors = {}
        self._clean()
