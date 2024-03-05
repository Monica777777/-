# 替换字符
def replace_chars(string, k_num):
    result = ""
    seen_chars = []
    for i, char in enumerate(string):
        if char in seen_chars[-k_num:]:  # 对每个字母向前查找k位 若出现重复项 则替换
            result += "-"
        else:
            result += char
        seen_chars.append(char)  # 没有重复的则添加进字符串中
    return result


if __name__ == '__main__':
    input_string, k = input("INPUT:").split()  # 输入字符串和数字
    output_string = replace_chars(input_string, int(k))
    print("OUTPUT:", output_string)  # 输出替换结果
