'''
    解析器，解析下载好的网页内容
'''
import re
import urllib.parse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        '''
        解析下载好的网页内容
        :param page_url: 页面url
        :param html_cont: 网页内容
        :return: 返回新的url列表及解析后的数据
        '''
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        '''
        得到新的url列表
        :param page_url:
        :param soup:
        :return:
        '''
        new_urls = set()

        # 词条页面URL：/item/name/id 或者 /item/name/，例：/item/C/7252092 或者 /item/Guido%20van%20Rossum
        links = soup.find_all('a', href=re.compile(r"/item/.*"))
        for link in links:
            new_url = link['href']
            # 拼接成完整的url
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        解析数据，并返回解析后的数据
        :param page_url:
        :param soup:
        :return:
        '''
        # 使用字典来存放解析后的数据
        res_data = {}

        # url
        res_data['url'] = page_url

        # 标题标签格式：<dd class="lemmaWgt-lemmaTitle-title"><h1>***</h1>***</dd>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # 简介标签格式：<div class="lemma-summary" label-module="lemmaSummary">***</div>
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data
