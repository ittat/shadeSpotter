
# {
#     brand: "dior",
#     type: "lipstick"
#     series: string,
#     series_url:string,
#     color: string
#     name: string
#     url?:string
# }


# title_zh --> series
# color_no --> name
# color_img-src --> img --> color
# item jump-href ---> series_url

import pandas as pd
import json
import requests
from io import BytesIO
from PIL import Image
import matplotlib.colors as colors
import colorsys
import binascii
import re



# 读取 Excel 文件
df = pd.read_excel('./lorealparis.xlsx')

# 将“color_no”列重命名为“name”，并添加一个名为“brand”的新列，值为“channel”
df['brand'] = 'lorealparis'
df['type'] = 'lipstick'

# 将“color_no”列重命名为“name”
df = df.rename(columns={'title_no': 'name'})
df = df.rename(columns={'items': 'series'})
df = df.rename(columns={'color': 'color'})
df = df.rename(columns={'items-href': 'series_url'})

# 选择导出的列
df = df[['brand','type','series','series_url','name','color']]

# 将数据保存为 JSON 文件，只包含“name”和“series”字段
with open('lorealparis.json', 'w',encoding='utf-8') as f:
    json.dump(df.to_dict(orient='records'), f,ensure_ascii=False)


