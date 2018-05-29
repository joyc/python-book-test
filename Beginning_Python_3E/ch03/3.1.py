# 根据指定的宽度打印格式化小票
width = int(input('输入宽度: '))

price_width = 10
item_width = width - price_width

header_tmpl = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
tmpl = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print('-' * width)

print(header_tmpl.format('商 品', '价 格'))

print('·' * width)

print(tmpl.format('面  粉', 6.5))
print(tmpl.format('韭  菜', 3.5))
print(tmpl.format('鸡  蛋', 10.0))
print(tmpl.format('虾  仁', 18.6))
print(tmpl.format('酱  油', 12))

print('-' * width)