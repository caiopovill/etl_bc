from .http_requester import HttpRequester

def test_request_from_page(requests_mock):
    url = 'https://www.bcb.gov.br/controleinflacao/apresrelinf'
    response_context = '<h1>OlaMundo</h1>'
    requests_mock.get(url, status_code=200, text=response_context)

    http_requester = HttpRequester()
    request_response = http_requester.request_from_page()
    print()
    print(request_response)
    