def py4_1():
    plaincode = input("请输入密文：")
    for p in plaincode:
        if ord("a") <= ord(p) <= ord("z"):
            print(chr(ord("a") + (ord(p) - ord("a") - 3) % 26), end='')
        else:
            print(p, end='')


def py4_2():
    line = input("请输入一行字符：")
    zh_count = 0
    en_count = 0
    digit_count = 0
    space_count = 0
    other_count = 0

    for char in line:
        if '\u4e00' <= char <= '\u9fff':
            zh_count += 1
        elif char.isalpha() and char.isascii():
            en_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    print("中文字符个数：", zh_count)
    print("英文字符个数：", en_count)
    print("数字个数：", digit_count)
    print("空格个数：", space_count)
    print("其它字符个数：", other_count)


py4_1()
print('\n')
py4_2()
