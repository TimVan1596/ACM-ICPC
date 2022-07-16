# 找出最长有效（格式正确且连续）括号子串的长度
def get_max_str_len(s):
    old = []
    length = 0
    # 栈(先考虑开头合法的情况)
    stack = []
    for index, c in enumerate(s):
        if c == '(':
            stack.append(c)
        # 只包含 '(' 和 ')' 的字符串
        elif len(stack) > 0:
            stack.pop()
            length += 2
        else:
            old.append(length)
            length = 0
    old.append(length)

    # 取各个分段最大的情况
    return max(old)


if __name__ == '__main__':
    # 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度
    # 输入：s = "(()"
    # 输出：2
    # 解释：最长有效括号子串是 "()"
    # s = "(()"
    s = "()(())())()(())"
    # s = ""
    print(get_max_str_len(s))

    pass
