import os, sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

import config.config as CONFIG


class Filter(object):
    def __init__(self):
        self.cold_array = CONFIG.COLD_GOODS + CONFIG.COLD_SKINS

    '''
    @Description:判断str字符串中是否包含array中任意元素
    '''

    def contains_item(self, str):
        flag = False
        for element in self.cold_array:
            if str.find(element) >= 0:
                flag = True
        return flag


# if __name__ == '__main__':
#     instance = Filter()
#     result = instance.contains_item('森林 DDPAT')
#     print(result)
