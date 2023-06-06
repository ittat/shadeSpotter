# 爬取彩妆品牌的页面数据

### list

- lorealparis 欧莱雅巴黎
- channel 香奈儿
- dior 迪奥
- givenchy 
- maybelline
- ysl


导出数据格式
{
    brand: string,
    <!-- 产品类型： 唇膏 -->
    type: "lipstick"
    series: string,
    series_url:string,
    <!-- 唇膏颜色 -->
    color: string
    <!-- 唇膏编号名称 -->
    name: string
    url?:string
}