import re

itext = re.finditer(r'\d+','12 edueduedu44coder deducoder, 11skdh   ds 12')      #匹配所有的数字
for i in itext:
    print(i)
    print(i.group())
    print(i.span())   #span()返回一个元组包含匹配 (开始,结束) 的位置