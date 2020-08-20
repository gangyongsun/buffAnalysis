import os, sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

import config.config as CONFIG
from api.API import API

'''生成结果'''
api_instance = API()


class GenerateResult(object):
    def __init__(self):
        self.threshold = CONFIG.PRICE_THRESHOLD
        self.upper_threshold = CONFIG.CHARGE_RATE_UPPER_THRESHOLD
        self.bottom_threshold = CONFIG.CHARGE_RATE_BOTTOM_THRESHOLD
        self.buff_vs_steam = CONFIG.BUFF_VS_STEAM

    '''
    @Description:扔求购比例计算
    '''

    def generate_beg_result(self, items):
        result_array = []
        for item in items:
            good_id = item['id']  # 商品ID
            sell_num = item['sell_num']  # 在售数量
            name = item['name']  # 商品名称

            # 1.首先获取最低价格
            sell_min_price = item['sell_min_price']
            # 1.1.先进行阈值过滤
            if float(sell_min_price) <= self.threshold:
                # 2.steam市场饰品价格页面
                steam_market_url = item['steam_market_url']

                # TODO : 3.调用API获得求购价格
                steam_beg_price = 10000

                # 4.计算扔求购的充值比例
                # 计算充值比例
                if float(steam_beg_price) > 0:
                    charge_rate = format(float(sell_min_price) / float(steam_beg_price) / 0.87, '.2f')
                    # 充值比例区间判断
                    if float(charge_rate) <= self.upper_threshold:
                        child = {
                            'id': good_id,
                            'name': name,
                            'sell_num': sell_num,
                            'sell_min_price': sell_min_price,
                            'steam_price_cny': steam_beg_price,
                            'charge_rate': charge_rate
                        }
                        result_array.append(child)
        result_array.sort(key=lambda x: x["charge_rate"])
        return result_array

    '''
    @Description:生成结果信息，不需要调用查看商品详情的API
    @ps:推荐使用
    '''

    def generate_result_4_category(self, items):
        result_array = []
        for item in items:
            # 1.首先获取最低价格
            sell_min_price = item['sell_min_price']
            # 1.1.先进行阈值过滤
            if float(sell_min_price) <= self.threshold:
                good_id = item['id']  # 商品ID
                sell_num = item['sell_num']  # 在售数量
                name = item['name']  # 商品名称

                goods_info = item['goods_info']  # 商品信息概览
                steam_price_cny = goods_info['steam_price_cny']  # steam价格

                # 计算充值比例
                if float(steam_price_cny) > 0:
                    # 充值比例区间判断
                    charge_rate = format(float(sell_min_price) / float(steam_price_cny) / 0.87, '.2f')
                    if self.bottom_threshold <= float(charge_rate) <= self.upper_threshold:
                        child = {
                            'id': good_id,
                            'name': name,
                            'sell_num': sell_num,
                            'sell_min_price': sell_min_price,
                            'steam_price_cny': steam_price_cny,
                            'charge_rate': charge_rate
                        }
                        result_array.append(child)
        result_array.sort(key=lambda x: x["charge_rate"])
        return result_array

    '''
    @Description:根据求购价格，计算充值最佳饰品
    '''

    def generate_result_on_beg_4_category(self, items):
        result_array = []
        for item in items:
            buff_id = str(item['id'])
            sell_min_price = item['sell_min_price']
            if buff_id in self.buff_vs_steam:
                # 根据dict获取对应的饰品在steam的ID
                good_id_on_steam = self.buff_vs_steam[buff_id]
                print(good_id_on_steam)
                # 调用API获取steam求购价格
                steam_beg_price = api_instance.get_steam_beg_price(good_id_on_steam)
                # 计算充值比例
                beg_charge_rate = format(float(sell_min_price) / float(steam_beg_price) / 0.87, '.2f')
                print(beg_charge_rate)
                item['beg_charge_rate'] = beg_charge_rate
                result_array.append(item)
            else:
                print('no exist for:', buff_id)
        result_array.sort(key=lambda x: x["charge_rate"])
        return result_array

    '''
    @Description:生成结果，调用查看商品详情的API，为了获取buff求购价格
    '''

    def generate_result(self, items):
        result_array = []

        for item in items:
            # 1.首先获取最低价格
            sell_min_price = item['sell_min_price']
            # 1.1.先进行阈值过滤
            if float(sell_min_price) <= self.threshold:
                good_id = item['id']  # 商品ID
                sell_num = item['sell_num']  # 在售数量
                # 1.1.1.根据商品ID获取信息
                data = api_instance.get_good(good_id)

                # 1.1.1.1.获取商品信息概览
                goods_infos = data['goods_infos'][str(good_id)]
                # 1.1.1.1.1.获取商品名称
                name = goods_infos['name']
                # 1.1.1.1.2.获取steam价格
                steam_price_cny = goods_infos['steam_price_cny']

                # 1.1.1.2.在售商品信息
                goods_items = data['items']
                # 1.1.1.2.1.求购价格
                lowest_bargain_price = goods_items[0]['lowest_bargain_price']
                #  1.1.1.2.2.最低出售价格
                price = goods_items[0]['price']

                # 计算充值比例
                if float(steam_price_cny) > 0:
                    # 充值比例区间判断
                    charge_rate = format(float(sell_min_price) / float(steam_price_cny) / 0.87, '.2f')
                    if self.bottom_threshold <= float(charge_rate) <= self.upper_threshold:
                        child = {
                            'id': good_id,
                            'name': name,
                            'sell_num': sell_num,
                            'price': price,
                            'steam_price_cny': steam_price_cny,
                            'lowest_bargain_price': lowest_bargain_price,
                            'charge_rate': charge_rate
                        }
                        result_array.append(child)
        result_array.sort(key=lambda x: x["charge_rate"])
        return result_array
