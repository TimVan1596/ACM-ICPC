import re
text = 'Love your parents. We are too busy growing up yet we forget that they are already growing.'
#********** Begin *********#
#1.匹配字符单词 Love
print(re.findall(r'Love',text))
#2.匹配以 w 开头的完整单词
print(re.findall(r'\b[w][a-zA-Z]{0,}\b',text))
#3.查找三个字母长的单词（提示：可以使用{m,n}方式）
print(re.findall(r'\b[a-zA-Z]{3}\b',text))
#********** End **********#