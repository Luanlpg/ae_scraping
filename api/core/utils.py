import requests

from bs4 import BeautifulSoup as bs4
from lxml import etree

class ScrapingService():
    def __init__(self, url):
        self.url = url
        self.document = requests.get(url)
        self.output = {'feed': []}

    def parse(self):
        xml = etree.XML(self.document.content)
        itens = xml.iter('item')
        for item in itens:
            self.output['feed'].append(self.register_item(item))
        return self.output

    def register_item(self, item):
        item_dict = {
            'title': None,
            'link': None,
            'description': []
            }
        links = []

        for new in item.iter():

            # lxml
            if new.tag == 'title':
                item_dict['title'] = new.text
            elif new.tag == 'link':
                item_dict['link'] = new.text
            elif new.tag == 'description':

                # BeautifulSoup
                soup = bs4(new.text.replace('![CDATA[', '').replace(']]', ''), 'html.parser')
                for tag in soup.find_all():
                    if tag.name == 'a':
                        links.append(tag['href'])
                    elif tag.name == 'img':
                        item_dict['description'].append({'type': 'image', 'content': tag['src']})
                    elif tag.name == 'p':
                        item_dict['description'].append({'type': 'text', 'content': tag.text})

        item_dict['description'].append({'type': 'links', 'content': links})

        return item_dict
