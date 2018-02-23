'''
    url管理器，管理并存储待爬取的url。

    url管理器需要维护两个列表，一个是
    待爬取的url列表，另一个是已爬取的
    url列表。
'''


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 待爬取的url列表
        self.old_urls = set()  # 已爬取的url列表

    def add_new_url(self, url):
        '''
        向管理器中添加新的url，也就是待爬取的url
        :param url: 新的url
        :return:
        '''
        # url为空则结束
        if url is None:
            return

        # 该url不在两个列表中才是新的url
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        向管理器中批量添加新的url
        :param urls: 新的url列表
        :return:
        '''
        if urls is None or len(urls) == 0:
            return

        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        '''
        判断管理器中是否有待爬取的url
        :return: True 或 False
        '''
        return len(self.new_urls) != 0

    def get_new_url(self):
        '''
        从url管理器中获取一个待爬取的url
        :return: 返回一个待爬取的url
        '''
        # 出栈一个url，并将该url添加在已爬取的列表中
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)

        return new_url
