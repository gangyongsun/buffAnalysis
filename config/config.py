# BUFF饰品购买价格阈值
PRICE_THRESHOLD = 6000

# Steam充值比例上限阈值
CHARGE_RATE_UPPER_THRESHOLD = 0.75

# Steam充值比例下限阈值
CHARGE_RATE_BOTTOM_THRESHOLD = 0.58

# 饰品刀
KNIVES_DICT = {'鲍伊猎刀': 'weapon_knife_survival_bowie', '蝴蝶刀': 'weapon_knife_butterfly', '弯刀': 'weapon_knife_falchion', '折叠刀': 'weapon_knife_flip',
               '穿肠刀': 'weapon_knife_gut', '猎杀者匕首': 'weapon_knife_tactical', 'M9刺刀': 'weapon_knife_m9_bayonet', '刺刀': 'weapon_bayonet',
               '爪子刀': 'weapon_knife_karambit', '暗影双匕': 'weapon_knife_push', '短剑': 'weapon_knife_stiletto', '熊刀': 'weapon_knife_ursus',
               '折刀': 'weapon_knife_gypsy_jackknife', '锯齿爪刀': 'weapon_knife_widowmaker', '海豹短刀': 'weapon_knife_css', '系绳匕首': 'weapon_knife_cord',
               '求生匕首': 'weapon_knife_canis', '流浪者匕首': 'weapon_knife_outdoor', '骷髅匕首': 'weapon_knife_skeleton'}

# 皮肤外观磨损
EXTERIOR = {'崭新出厂': 'wearcategory0', '略有磨损': 'wearcategory1', '久经沙场': 'wearcategory2', '破损不堪': 'wearcategory3', '战痕累累': 'wearcategory4',
            '无涂装': 'wearcategoryna'}

# 冷门刀
COLD_GOODS = ['短剑', '鲍伊猎刀', '暗影双匕', '折刀', '求生匕首', '流浪者匕首', '系绳匕首', '骷髅匕首']
# '鲍伊猎刀',


# 冷门皮肤
COLD_SKINS = ['屠夫', '大马士革钢', '夜色', '蓝钢', '自动化 (崭新出厂)', '传说 (崭新出厂)', '深红之网 (崭新出厂)', '黑色层压板', '致命紫罗兰', '表面淬火', '枯焦之色', '澄澈之水', '自由之手', '噩梦之夜', '人工染色', '狩猎网格',
              '北方森林', '都市伪装',
              '森林 DDPAT']

# 饰品类别
CATEGORY_GROUP = {'手套': 'hands', '刀': 'knife', '手枪': 'pistol', '步枪': 'rifle', 'AK-47': 'weapon_ak47','M4A4':'weapon_m4a1','M4A1':'weapon_m4a1_silencer','AWP':'weapon_awp'}

# 饰品品质
QUALITY = {'星普通': 'unusual', '星暗金': 'unusual_strange', '普通': 'normal', '暗金': 'strange'}

# 获取所有商品API URL
GOODS_API_URL = 'https://buff.163.com/api/market/goods'

# 获取单个商品销售信息的API URL
GOOD_API_URL = 'https://buff.163.com/api/market/goods/sell_order'

# steam获取求购价格的API URL
BEG_PRICE_URL_ON_STEAM = "https://steamcommunity.com/market/itemordershistogram"

# cookie
COOKIE = 'Device-Id=vNaSW7KuNh3amaqwYhsB; _ga=GA1.2.500118338.1592976292; _ntes_nnid=9e967cc09b4c7176c9568d8f3fb616a9,1594276321247; _ntes_nuid=9e967cc09b4c7176c9568d8f3fb616a9; Locale-Supported=zh-Hans; game=csgo; nts_mail_user=undefined:-1:0; UM_distinctid=173b38387f65d5-0a068e03df22d6-15366656-1aeaa0-173b38387f79eb; mail_psc_fingerprint=e144f94053fb38a0cd9128af88fbef68; r_ntcid=730:57; unbind_steam_result=; steam_info_to_bind=; _gid=GA1.2.1661433803.1597642676; _gat_gtag_UA_109989484_1=1; NTES_YD_SESS=7jAOvTCVALd2.x3.SbVPIyH_FMHknW8CvSeWk7I0gCT06KYile1XdTUQWpV.j19CDl94tch6HqYfFWT1GI5MQsAmJ._Xp2TIDlWgJdYK6HiV79B5VHZpChcQXiJBA1A0gwhSbfiVRrZwS4qnJ6KtR_JZ4bDhQKP0RuFc_0.oltPzOxTbg11VCmjoX0uw3VQtUe4vkEA4XaaeJf162FAuM_RLtYBjf9hHHh5KBHXnC2sfN; S_INFO=1597642686|0|3&80##|13381039880; P_INFO=13381039880|1597642686|1|netease_buff|00&99|bej&1597580024&netease_buff#bej&null#10#0#0|&0|null|13381039880; session=1-NhrUr3lmGvKsfFAAZrRj7vwAeEmpSJXrmMorLThiVZ7f2045864611; csrf_token=ImJhNzliMzEyYzAzNzU3Mzk2YzdjYzQ4MGRkYTE2OGVkNzYyMDNhNzAi.EhupRg.Zh1PmioqZbkS_gGB3ZO2PWw0qVs'

# header设置
HEADER_SET = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'buff.163.com',
    'Pragma': 'no-cache',
    'Referer': 'https://buff.163.com/market/?game=csgo',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': COOKIE
}

# 文件生成目录
RATE_FILE = './rate.txt'
RATE_STRANGE_FILE = './rate_strange.txt'
HANDS_FILE = './hands.txt'
AK47_FILE = './AK47.txt'
M4A4_FILE = './M4A4.txt'
M4A1_FILE = './M4A1.txt'
AWP_FILE = './AWP.txt'
RATE_BEG_FILE = './beg.txt'

# 编码
ENCODING = 'utf-8-sig'

# buff饰品ID与Steam饰品ID的对应dict
BUFF_VS_STEAM = {'42463': '140067676',
                 '43033': '1339834',
                 '759581': '176000241',
                 '760300': '176002898',
                 '42614': '49473120',
                 '42555': '175881163',
                 '773858': '176092096',
                 '762747': '176019026',
                 '43701': '9680063',
                 '33812': '1322028',
                 '42532': '17368647',
                 '43265': '9685972',
                 '769535': '176043082',
                 '43774': '9646037',
                 '773721': '176091941',
                 '42734': '156249199',
                 '43389': '15005298',
                 '42530': '14977515',
                 '43334': '139691721',
                 '43000': '1322331',
                 '43017': '29285555',
                 '43104': '156338219',
                 '769500': '176042753',
                 '759462': '176000070',
                 '42551': '175880584',
                 '759828': '176001942',
                 '43497': '9681945',
                 '43575': '9646079',
                 '42579': '14971872',
                 '44245': '1386626',
                 '43087': '29565592',
                 '42926': '175880992',
                 '42760': '1322526',
                 '42636': '175880775',
                 '42893': '9635180',
                 '43110': '29338512',
                 '43011': '156758007',
                 '42998': '29217386',
                 '769563': '176042797',
                 '759572': '176000152',
                 '42361': '1358684',
                 '42495': '175880618',
                 '42512': '139924030',
                 '42670': '175880563',
                 '759672': '176000753',
                 '769503': '176042698',
                 '42434': '29490947',
                 '759399': '176000189',
                 '42950': '175880465',
                 '773696': '176091942',
                 '43052': '1285128'}
