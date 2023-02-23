from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import processor

class Scrapper:
   def pageGet(self, url)->list:
       self._driver.get(url)
       return self._processor.read(self._driver)
   def close(self):
       self._driver.close()
   def __init__(self):
       self._chrome_options = Options()
       self._chrome_options.add_argument("--headless")
       self._processor = processor.OfferProcessor()
       self._driver = webdriver.Chrome(options=self._chrome_options)

class ScrapperLayer:
   def __exit__(self, exc_type, exc_value, traceback):
       self._scrapper.close()
   def __enter__(self):
       self._scrapper = Scrapper()
       return self._scrapper
