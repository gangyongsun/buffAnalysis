import os, sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

import config.config as CONFIG


if '42760' in CONFIG.BUFF_VS_STEAM:
    print(True)
else:
    print(False)
