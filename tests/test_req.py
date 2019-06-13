from package.client import Client

def test_get():
    client = Client()
    assert "Python" in client.get('http://python.org')