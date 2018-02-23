'''
    下载器，用于下载目标网页的内容
'''

from urllib import request


class HtmlDownloader(object):
    def download(self, url):
        '''
        下载url地址的页面内容
        :param url: 需要下载的url
        :return: 返回None或者页面内容
        '''
        if url is None:
            return None

        response = request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()
