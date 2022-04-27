import requests 

class RequestsHelper :
    def __init__(self) -> None:
        pass
    
    def Get(self, url) :
        return requests.get(url)