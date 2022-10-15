
from .http_requester import HttpRequester

def test_request_from_page():
    #url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
    #response_context = '<h1>OlaMundo</h1>'
    #requests_mock.get(url, status_code=200, text=response_context)

    http_requester = HttpRequester()
    request_response = http_requester.request_from_page()
    print('AAAAAAAAAAAAAAAAAAAAAA')
    print(request_response)
    