"""
" Processor helper
"""
import re
import time
from selenium import webdriver

def getAttributes(tag:webdriver)->dict:
    """Get all attributes"""
    out = {}
    attributes = re.findall(
        """([a-z]+-?[a-z]+_?)='?"?""",
        tag.get_attribute("outerHTML")
    )
    for attr in attributes:
        out[attr] = tag.get_attribute(attr)
    return out


def scrollDown(driver:webdriver)->int:
    last = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        height = driver.execute_script("return document.body.scrollHeight")
        if height == last:
            break
        last = height

def minHeight(driver:webdriver)->int:
    size = driver.execute_script("return document.body.offsetHeight")

    if 1080 > size:
        size = 1080
    return size

def fullShot(driver:webdriver)->dict:
    driver.set_window_size(1920, 1080)
    driver.set_window_size(
       1920,
       minHeight(driver)
    )
    try:
        driver.find_element_by_tag_name('body').screenshot("image.png");
    except:
        driver.save_screenshot("image.png");

