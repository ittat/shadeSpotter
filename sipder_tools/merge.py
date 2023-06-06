# merge 全部品牌数据

import json
import os

data = []
for i in ['lorealparis','channel','ysl','dior','givenchy','maybelline']:
    filename = f"{i}/{i}.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data += json.load(f)

# 将合并后的数据写入 db.json 文件中
with open('db.json', 'w',encoding='utf-8') as f:
    json.dump(data, f,ensure_ascii=False)