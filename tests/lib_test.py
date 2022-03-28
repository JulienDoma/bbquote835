from webbrowser import get
from bbquote.lib import get_quote

def test_type():
    assert type(get_quote()) == tuple
    
def test_len():
    assert len(get_quote()) > 0