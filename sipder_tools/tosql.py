import json

# 从JSON文件读取数据
with open('db.json', 'r') as f:
    data = json.load(f)

# 构建INSERT语句的模板
template = "INSERT INTO `shadespotter` (brand, type, series, series_url, name, color) VALUES ('{brand}', '{type}', '{series}', '{series_url}', '{name}', '{color}');"

# 生成SQL初始化脚本
sql_script = ''
for item in data:
    sql_script += template.format(**item) + "\n"

# 将SQL初始化脚本写入文件
with open('db.sql', 'w',encoding='utf-8') as f:
    # 写入SQL脚本头部
    f.write("DROP TABLE IF EXISTS `shadespotter`;\n")
    f.write("CREATE TABLE `shadespotter` (\n")
    f.write("  `id` int(50) unsigned NOT NULL AUTO_INCREMENT,\n")
    f.write("  `brand` varchar(150) NOT NULL COMMENT '品牌名称',\n")
    f.write("  `type` varchar(50) DEFAULT NULL COMMENT '产品类型',\n")
    f.write("  `series` varchar(150) DEFAULT NULL COMMENT '产品系列',\n")
    f.write("  `series_url` varchar(500) DEFAULT NULL COMMENT '产品系列url',\n")
    f.write("  `name` varchar(100) DEFAULT NULL COMMENT '产品名称',\n")
    f.write("  `color` varchar(20) DEFAULT NULL COMMENT '颜色',\n")
    f.write("  `create_time` bigint(50) DEFAULT NULL COMMENT '更新时间',\n")
    f.write("  `del_status` tinyint(4) DEFAULT '0' COMMENT '是否删除 -1：已删除   0：正常',\n")
    f.write("  PRIMARY KEY (`id`)\n")
    # f.write("  UNIQUE KEY `name` (`name`)\n")
    f.write(") ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COMMENT='彩妆色彩数据库';\n\n")
    # 写入生成的SQL初始化脚本
    f.write(sql_script)
