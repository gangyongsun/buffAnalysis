import requests, time, os, sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

import config.config as CONFIG


class API(object):
    def __init__(self):
        # 游戏名
        self.game = 'csgo'

        # 价格排序
        self.sort_by = 'price.desc'

        # 系统默认当前页为1
        self.default_current_page = 1

        # 每页数量
        self.page_size = 80

        # 获取多个饰品信息API URL
        self.goods_url = CONFIG.GOODS_API_URL

        # 获取单个饰品信息API URL
        self.good_url = CONFIG.GOOD_API_URL

        # steam获取求购价格的API URL
        self.beg_price_url_on_steam = CONFIG.BEG_PRICE_URL_ON_STEAM

        # 请求头
        self.header_set = CONFIG.HEADER_SET

    '''
    @description: 根据[饰品类别组名]获取信息
    @category_group: 刀、手套饰品类别组名
    @quality:饰品品质
    @exterior:皮肤外观磨损
    @page_num:页数
    '''

    def get_goods_by_category_group(self, category_group, quality, exterior, page_num):
        timestamp = int(round(time.time() * 1000))
        conditions = {
            'game': self.game,
            'page_num': page_num,
            'page_size': self.page_size,
            'category_group': category_group,
            'sort_by': self.sort_by,
            'quality': quality,
            'exterior': exterior,
            '_': timestamp
        }
        # request get 请求
        result = requests.get(self.goods_url, headers=self.header_set, params=conditions)
        return result.json()['data']['items']

    '''
    @description: 根据[饰品类别]获取信息
    @weapon_category: 饰品类别(蝴蝶刀，沙漠之鹰，AK47等具体的类别)
    @quality:饰品品质
    @exterior:皮肤外观磨损
    '''

    def get_goods_by_category(self, weapon_category, quality, exterior):
        timestamp = int(round(time.time() * 1000))
        conditions = {
            'game': self.game,
            'page_num': self.default_current_page,
            'page_size': self.page_size,
            'category': weapon_category,
            'sort_by': self.sort_by,
            'quality': quality,
            'exterior': exterior,
            '_': timestamp
        }
        # request get 请求
        result = requests.get(self.goods_url, headers=self.header_set, params=conditions)
        return result.json()['data']['items']

    '''
    @description:根据ID获取饰品信息
    @good_id:饰品ID
    '''

    def get_good_info(self, good_id):
        timestamp = int(round(time.time() * 1000))
        condition = {
            'game': self.game,
            'goods_id': good_id,
            'page_num': self.default_current_page,
            'sort_by': 'default',
            'mode': '',
            'allow_tradable_cooldown': 1,
            '_': timestamp
        }
        # request get 请求
        result = requests.get(self.good_url, headers=self.header_set, params=condition)
        return result.json()['data']

    '''
    @description:获取求购价格
    '''

    def get_steam_beg_price(self, goods_id_on_steam):
        condition = {
            "country": "CN",
            "language": "schinese",
            "currency": 23,
            "item_nameid": goods_id_on_steam,
            "two_factor": 0
        }

        # request get 请求
        result = requests.get(self.beg_price_url_on_steam, params=condition)
        return result.json()['buy_order_graph'][0][0]

if __name__ == '__main__':
    instance = API()
    print(instance.get_steam_beg_price('29338512'))
