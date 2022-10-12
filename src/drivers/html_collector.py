from typing import List,Dict
from bs4 import BeautifulSoup
class HtmlCollector:

    @classmethod
    def collect_essential_information(cls, html: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html, 'html.parser')

        relatorio_ipca = soup.find(class_="container main")
        relatorio_ipca_href = relatorio_ipca.find_all(class_="accordion")

        essential_information = []
        for relatorios in relatorio_ipca_href:
            names = relatorios.contents[0]
            links = relatorios.get('href')
            essential_information.append(

                {'mes':names,
                 'link':links}
            )
        return essential_information
    