import os, sys
import prettytable as pt

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

import config.config as CONFIG

from common.Filter import Filter

filter = Filter()


class IOUtil(object):
    def __init__(self):
        self.rate_file = CONFIG.RATE_FILE
        self.rate_strange_file = CONFIG.RATE_STRANGE_FILE
        self.encoding = CONFIG.ENCODING

    '''
    @Description:写文件
    '''

    def write_rate_file(self, good_array, file):
        # 文件句柄
        file_handle = open(file, "w", encoding=self.encoding)

        ## 按行添加数据
        tb = pt.PrettyTable()

        ## 自定义表格输出样式
        ### 设定左对齐
        tb.align = 'l'

        ### 设定边框连接符为'*"
        tb.junction_char = "*"

        ### 设定左侧不填充空白字符
        tb.left_padding_width = 0

        #写文件头
        tb.field_names = ["饰品名称", "饰品ID(BUFF)", "充值比例"]

        for good in good_array:
            name = good['name']  # 饰品名称
            good_id = good['id']  # 饰品ID(BUFF)
            charge_rate = good['charge_rate']  # 充值比例
            if not filter.contains_item(name):
                tb.add_row([name, good_id, charge_rate])

        print(tb)
        file_handle.write(tb.get_string())
        file_handle.close()
