
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


def extract_color(color_style):
    hex_regex = r'#([0-9a-fA-F]+)'
    rgb_regex = r'rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)'
    hex_match = re.search(hex_regex, color_style)
    rgb_match = re.search(rgb_regex, color_style)
    if hex_match is not None:
        return hex_match.group(0)
    elif rgb_match is not None:
        r, g, b = rgb_match.groups()
        return '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))
    else:
        return None

# 读取 Excel 文件
df = pd.read_excel('./givenchy.xlsx')

# 将“color_no”列重命名为“name”，并添加一个名为“brand”的新列，值为“channel”
df['brand'] = 'givenchy'
df['type'] = 'lipstick'

# 将“color_no”列重命名为“name”
df = df.rename(columns={'title': 'name'})
df = df.rename(columns={'items': 'series'})
# df = df.rename(columns={'color_img-src': 'color'})
df = df.rename(columns={'items-href': 'series_url'})



# 处理每个“color_img-src”，将其颜色转换为 HEX 码
for i, row in df.iterrows():
    sytle = row['sytle']
    hexcode = extract_color(sytle)

    df.at[i, 'color'] = hexcode

    # rgb = rgba[:3]
    # hexcode = '#%02x%02x%02x' %  rgb
    # print(hexcode) # 输出：FF0000


# 选择导出的列
df = df[['brand','type','series','series_url','name','color']]

# 将数据保存为 JSON 文件，只包含“name”和“series”字段
with open('givenchy.json', 'w',encoding='utf-8') as f:
    json.dump(df.to_dict(orient='records'), f,ensure_ascii=False)


