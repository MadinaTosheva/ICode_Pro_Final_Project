import  requests



class BaseApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()


    def _url (self, path):
        return f'{self.base_url}{path}'