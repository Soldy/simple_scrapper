"""
" Processor helper
"""
import re
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
