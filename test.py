"""
" pytest
"""
import pytest
import scrapper

offers_list = []
def test_offerget():
    """ offer  """
    global offers_list
    with scrapper.ScrapperLayer() as scrap:
        offers_list = scrap.pageGet("https://wltest.dns-systems.net/")
    return True
@pytest.mark.skipif(not test_offerget(), reason='scrapp failed')
def test_offersize():
    """ response size test  """
    global offers_list
    assert len(offers_list) == 6
@pytest.mark.skipif(not test_offerget(), reason='scrapp failed')
def test_nofailed():
    """ searching failed in result  """
    global offers_list
    for i in range(6):
        assert ('failed' in offers_list[i]) is False
@pytest.mark.skipif(not test_offerget(), reason='scrapp failed')
def test_hasprice():
    """ price exist check """
    global offers_list
    for i in range(6):
        assert ('price' in offers_list[i]) is True
@pytest.mark.skipif(not test_offerget(), reason='scrapp failed')
def test_correctorder():
    """ order check """
    global offers_list
    for i in range(5):
        assert offers_list[i]['price'] > offers_list[i+1]['price']
