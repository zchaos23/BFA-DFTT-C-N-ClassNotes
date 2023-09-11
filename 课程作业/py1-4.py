# 十进制转十六进制内的进制
def base10_conversion(number, base):
    if base > 16:
        print('你输入的基数大于 16')
        exit()
    else:
        pass

    hexdict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}    # 十进制以上时，位数对应的字母表示
    remainer = []   # 创建列表，用来存储余数

    while (number//base) != 0:  # 当商不为零时，持续执行除法，获取余数
        remainer.append(number % base)
        number = (number//base)
    remainer.append(number)     # 当商为零时，将最后的余数加入余数列表

    digits = ''    # 将得到的余数转换为新进制下的位数
    for digit in remainer:  # 遍历余数列表的每个数
        if digit in hexdict:    # 当基数大于十时，将位数转换为字母表示
            digit = hexdict[digit]
        else:
            pass
        digits = str(digit) + digits    # 最终转换完成的结果为每位数字符串的结合

    return digits   # 回传转换结果


number = input('请输入想要转换的十进制数值：')
base = input('请输入想要转换到的进制基数（最高支持十六进制）：')

try:
    print('十进制数 {} 转换到 {} 进制的值为: {} '.format(number, base, base10_conversion(int(number), int(base))))
except:
    print('转换失败，请检查报错信息')
