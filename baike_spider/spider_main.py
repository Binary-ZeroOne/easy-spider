'''
    爬虫调度器程序，也是主入口文件
'''

import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    # 初始化各个对象
    def __init__(self):
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # 下载器
        self.parser = html_parser.HtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器

    # 爬虫调度方法
    def craw(self, root_url):
        # 记录当前爬取的是第几个URL
        count = 1
        # 将入口页面的url添加到url管理器里
        self.urls.add_new_url(root_url)

        # 启动爬虫的循环
        while self.urls.has_new_url():
            try:
                # 获取待爬取的url
                new_url = self.urls.get_new_url()

                # 每爬取一个页面就在控制台打印一下
                print("craw", count, new_url)

                # 启动下载器来下载该url的页面内容
                html_cont = self.downloader.download(new_url)

                # 调用解析器解析下载下来的页面内容，会得到新的url列表及新的数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                # 将新的url列表添加到url管理器里
                self.urls.add_new_urls(new_urls)

                # 收集解析出来的数据
                self.outputer.collect_data(new_data)

                # 当爬取到1000个页面时则停止爬取
                if count == 1000:
                    break

                count += 1

            except:
                # 爬取时出现异常则在控制台中输出一段文字
                print("craw failed")

        # 输出处理好的数据
        self.outputer.output_html()


# 判断本模块是否作为入口文件被执行
if __name__ == "__main__":
    # 目标入口页面的URL
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)
