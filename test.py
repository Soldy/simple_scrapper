import pytest
import scrapper

offers_list = []
def test_offerget():
    global offers_list
    with scrapper.ScrapperLayer() as scrap:
        offers_list = scrap.pageGet("https://wltest.dns-systems.net/")
    return True
@pytest.mark.skipif(not test_offerget(), reason='scrapp failed')
def test_offersize():
    global offers_list
    assert len(offers_list) == 6
def test_nofailed():
    global offers_list
    for i in range(6):
        assert ('failed' in offers_list[i]) == False
def test_hasprice():
    global offers_list
    for i in range(6):
        assert ('price' in offers_list[i]) == True
def test_correctorder():
    global offers_list
    for i in range(5):
        assert offers_list[i]['price'] > offers_list[i+1]['price'] 
