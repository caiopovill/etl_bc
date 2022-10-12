from .html_collector import HtmlCollector
from .mocks.http_requester_mock import mock_requester_from_page


def test_collect_essential_information():
    http_request_response = mock_requester_from_page()

    html = HtmlCollector()
    essential_information = html.collect_essential_information(http_request_response['html'])
    print()
    print(essential_information)
    