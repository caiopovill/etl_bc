'https://www.bcb.gov.br/controleinflacao/apresrelinf'

from typing import Dict
import requests

class HttpRequester:

    def __init__(self) -> None:
        self.__url = 'https://www.bcb.gov.br/controleinflacao/apresrelinf'

    def request_from_page(self) -> Dict[int, str]:
        response = requests.get(self.__url, timeout=10)
        print(response.text)
        return {
            "status_code": response.status_code,
            "html": response.text
        }
        