
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
df = pd.read_excel('./dior.xlsx')

# 将“color_no”列重命名为“name”，并添加一个名为“brand”的新列，值为“channel”
df['brand'] = 'dior'
df['type'] = 'lipstick'

# 将“color_no”列重命名为“name”
df = df.rename(columns={'title': 'name'})
df = df.rename(columns={'s_title': 'series'})
# df = df.rename(columns={'color_img-src': 'color'})
df = df.rename(columns={'item-href': 'series_url'})

# 处理每个“color_img-src”，将其颜色转换为 HEX 码
for i, row in df.iterrows():
    img_url = row['img-src']
    df.at[i, 'color'] = ""
    if pd.isna(img_url):
        continue
    if not re.match(r'^https?://', img_url):
        print(f"Invalid URL: {img_url}")
        continue
    try:
        response = requests.get(img_url)
        
        img = Image.open(BytesIO(response.content)).convert('RGBA')
        # small_image = img.resize((80, 80))
        # result = small_image.convert(
        #     "P", palette=Image.ADAPTIVE, colors=1
        # )

        # palette = result.getpalette()
        # color_counts = sorted(result.getcolors(), reverse=True)
        # colors = list()
        # print(color_counts)
        # print(result)
        # b, g, r = img[20, 20]     # 获取b, g, r
        src_strlist = img.load()
        rgba = src_strlist[20, 20]
        # rgba = (255, 0, 0)

       
        rgb = rgba[:3]
        hexcode = '#%02x%02x%02x' %  rgb
        print(hexcode) # 输出：FF0000

    

        df.at[i, 'color'] = hexcode

        # color = colors.to_hex(tuple(round(c * 255) for c in colorsys.rgb_to_hsv(*tuple(c / 255.0 for c in img.getpixel((0, 0)))))).lstrip('#')
        # df.at[i, 'color'] = color
    except Exception as e:
        print(f"Error processing image: {img_url}: {e}")
        df.at[i, 'color'] = ""

# 选择导出的列
df = df[['brand','type','series','series_url','name','color']]

# 将数据保存为 JSON 文件，只包含“name”和“series”字段
with open('dior.json', 'w',encoding='utf-8') as f:
    json.dump(df.to_dict(orient='records'), f,ensure_ascii=False)


