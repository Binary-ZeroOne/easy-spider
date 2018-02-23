'''
    输出器，将解析后的数据输出到网页上
'''


class HtmlOutputer(object):
    def __init__(self):
        # 存储解析后的数据
        self.datas = []

    def collect_data(self, data):
        '''
        收集数据
        :param data:
        :return:
        '''
        if data is None:
            return

        self.datas.append(data)

    def output_html(self):
        '''
        将收集的数据以html的格式输出到html文件中，我这里使用了Bootstrap
        :return:
        '''
        # 写入到一个output.html文件里
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write("<!DOCTYPE html>")
        fout.write("<html>")
        fout.write('<head>')
        fout.write('<meta charset="UTF-8" />')
        fout.write(
            '<link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"/>')
        fout.write('</head>')
        fout.write("<body>")
        fout.write(
            '<div style="width: 1000px;margin: auto" class="bs-example" data-example-id="bordered-table" ><table class="table table-bordered table-striped" >')
        fout.write(
            '<thead><tr style="height: 70px;font-size: 20px"><th style="text-align: center;vertical-align: middle;width: 60px">#</th><th style="text-align: center;vertical-align: middle;width: 150px">URL & 标题</th><th style="text-align: center;vertical-align: middle;">简介</th></tr></thead><tbody>')

        num = 0
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<th style='text-align: center;vertical-align: middle;' scope='row'>%d</th>" % num)
            fout.write("<td style='text-align: center;vertical-align: middle;'><a href=%s>%s</a></td>" % (
                data['url'], data['title']))
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
            num += 1

        fout.write("</tbody></table></div>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
