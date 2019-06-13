import requests

class Client():

    def get(self, url):
        with requests.Session() as session:
            return session.get(url).text
