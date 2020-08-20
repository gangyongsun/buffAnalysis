'''
@Author: SunYongang
@Date: 2020-07-04 21:55:46
@LastEditTime: 2020-07-07 23:18:17
@LastEditors: Please set LastEditors
@Description: Get knife price
@FilePath: \PyRestful\RestFulClient.py
'''
import os, sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

import config.config as CONFIG

from api.API import API
from api.GenerateResult import GenerateResult
from common.IOUtil import IOUtil

api_instance = API()
rate_instance = GenerateResult()
io_instance = IOUtil()


class Client(object):
    def __init__(self):
        self.category_group_name = CONFIG.CATEGORY_GROUP['刀']
        self.quality_unusual = CONFIG.QUALITY['普通']
        self.quality_unusual_strange = CONFIG.QUALITY['暗金']
        self.exterior = CONFIG.EXTERIOR['崭新出厂']
        self.exterior_source = CONFIG.EXTERIOR['无涂装']


    '''
    所有品质、所有磨损，饰品结果
    '''
    def get_goods(self):
        array = []
        for num in range(1, 30):
            # 调用方法，根据类别获取所有饰品，不分品质，不分磨损
            array += api_instance.get_goods_by_category_group(self.category_group_name, '', '', num)
        return array

    '''
    普通品质、崭新，饰品结果
    '''
    def get_unusual_goods(self):
        array = []
        for num in range(1, 4):
            # 调用方法，根据类别获取所有饰品
            array += api_instance.get_goods_by_category_group(self.category_group_name, self.quality_unusual, self.exterior, num)

        # 无涂装饰品集合
        # array += api_instance.get_goods_by_category_group(self.category_group_name, '', self.exterior_source, 1)
        return array

    '''
    暗金品质、崭新，饰品结果
    '''

    def get_unusual_strange_goods(self):
        array = []
        for num in range(1, 4):
            array += api_instance.get_goods_by_category_group(self.category_group_name, self.quality_unusual_strange, self.exterior, num)
        return array


if __name__ == "__main__":
    instance = Client()
    # 调用API获取数据
    unusual_array = instance.get_unusual_goods()
    unusual_strange_array = instance.get_unusual_strange_goods()

    # 计算充值比例数据
    result_array = rate_instance.generate_result_4_category(unusual_array)
    result_strange_array = rate_instance.generate_result_4_category(unusual_strange_array)


    io_instance.write_rate_file(result_array, CONFIG.RATE_FILE)
    io_instance.write_rate_file(result_strange_array, CONFIG.RATE_STRANGE_FILE)

    # result_array_on_beg = rate_instance.generate_result_on_beg_4_category(result_array)
    # io_instance.write_rate_file(result_array_on_beg,CONFIG.RATE_BEG_FILE)



    # 所有
    # good_array = instance.get_goods()
    #
    #扔求购充值比例数据
    # result_bet=rate_instance.generate_beg_result(good_array)
    # io_instance.write_rate_file(good_array,CONFIG.RATE_BEG_FILE)

