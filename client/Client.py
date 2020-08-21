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
        self.category_knife = CONFIG.CATEGORY_GROUP['刀']
        self.category_hands = CONFIG.CATEGORY_GROUP['手套']
        self.category_ak47 = CONFIG.CATEGORY_GROUP['AK-47']
        self.category_m4a4 = CONFIG.CATEGORY_GROUP['M4A4']
        self.category_m4a1 = CONFIG.CATEGORY_GROUP['M4A1']
        self.category_awp = CONFIG.CATEGORY_GROUP['AWP']

        self.quality_unusual = CONFIG.QUALITY['星普通']
        self.quality_unusual_strange = CONFIG.QUALITY['星暗金']

        self.quality_normal = CONFIG.QUALITY['普通']
        self.quality_strange = CONFIG.QUALITY['暗金']

        self.exterior_new_factory = CONFIG.EXTERIOR['崭新出厂']
        self.exterior_few_break = CONFIG.EXTERIOR['略有磨损']

        self.exterior_source = CONFIG.EXTERIOR['无涂装']

    '''
    所有品质、所有磨损，饰品结果
    '''

    def get_goods(self):
        array = []
        for num in range(1, 30):
            # 调用方法，根据类别获取所有饰品，不分品质，不分磨损
            array += api_instance.get_goods_by_category_group(self.category_knife, '', '', num)
        return array

    '''
    崭新普通刀
    '''

    def get_unusual_knives(self):
        array = []
        for num in range(1, 4):
            # 调用方法，根据类别获取所有饰品
            array += api_instance.get_goods_by_category_group(self.category_knife, self.quality_unusual, self.exterior_new_factory, num)

        # 无涂装饰品集合
        # array += api_instance.get_goods_by_category_group(self.category_group_name, '', self.exterior_source, 1)
        return array

    '''
    崭新暗金刀
    '''

    def get_unusual_strange_knives(self):
        array = []
        for num in range(1, 4):
            array += api_instance.get_goods_by_category_group(self.category_knife, self.quality_unusual_strange, self.exterior_new_factory, num)
        return array

    '''
    手套
    '''

    def get_hands(self):
        return api_instance.get_goods_by_category_group(self.category_hands, self.quality_unusual, self.exterior_few_break, 1)

    '''
    崭新暗金AK-47
    '''

    def get_strange_ak47(self):
        return api_instance.get_goods_by_category(self.category_ak47, self.quality_strange, self.exterior_new_factory)

    '''
       崭新暗金M4A4
    '''

    def get_strange_m4a4(self):
        return api_instance.get_goods_by_category(self.category_m4a4, self.quality_strange, self.exterior_new_factory)
    '''
       崭新暗金M4A1
    '''

    def get_strange_m4a1(self):
        return api_instance.get_goods_by_category(self.category_m4a1, self.quality_strange, self.exterior_new_factory)

    '''
       崭新暗金AWP
    '''

    def get_strange_awp(self):
        return api_instance.get_goods_by_category(self.category_awp, self.quality_strange, self.exterior_new_factory)


if __name__ == "__main__":
    instance = Client()
    # 调用API获取数据
    # unusual_knife_array = instance.get_unusual_knives()
    # unusual_strange_knife_array = instance.get_unusual_strange_knives()
    # hands_array=instance.get_hands();
    # ak47_array = instance.get_strange_ak47();
    # m4a4_array = instance.get_strange_m4a4();
    # awp_array = instance.get_strange_awp();
    m4a1_array = instance.get_strange_m4a1();

    # 计算充值比例数据
    # result_knife_array = rate_instance.generate_result_4_category(unusual_knife_array)
    # result_strange_knife_array = rate_instance.generate_result_4_category(unusual_strange_knife_array)
    # result_hand_array=rate_instance.generate_result_4_category(hands_array)
    # result_ak47_array = rate_instance.generate_result_4_category(ak47_array)
    # result_m4a4_array = rate_instance.generate_result_4_category(m4a4_array)
    # result_awp_array = rate_instance.generate_result_4_category(awp_array)
    result_m4a1_array = rate_instance.generate_result_4_category(m4a1_array)

    # 写文件
    # io_instance.write_rate_file(result_knife_array, CONFIG.RATE_FILE)
    # io_instance.write_rate_file(result_strange_knife_array, CONFIG.RATE_STRANGE_FILE)
    # io_instance.write_rate_file(result_hand_array,CONFIG.HANDS_FILE)
    # io_instance.write_rate_file(result_ak47_array, CONFIG.AK47_FILE)
    # io_instance.write_rate_file(result_m4a4_array, CONFIG.M4A4_FILE)
    # io_instance.write_rate_file(result_awp_array, CONFIG.AWP_FILE)
    io_instance.write_rate_file(result_m4a1_array, CONFIG.M4A1_FILE)

    # result_array_on_beg = rate_instance.generate_result_on_beg_4_category(result_array)
    # io_instance.write_rate_file(result_array_on_beg,CONFIG.RATE_BEG_FILE)

    # 所有
    # good_array = instance.get_goods()
    #
    # 扔求购充值比例数据
    # result_bet=rate_instance.generate_beg_result(good_array)
    # io_instance.write_rate_file(good_array,CONFIG.RATE_BEG_FILE)
