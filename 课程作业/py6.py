import random


def random_birthday_list(num):
    birthdayList = []
    for n in range(num):
        birthdayList.append(random.randint(0, 364))
    return birthdayList


def birthday_paradox(birthdayList):
    for d in birthdayList:
        if birthdayList.count(d) > 1:
            return True
    return False


randomTimes = [100, 1000, 10000, 100000]

for t in randomTimes:
    count = 0
    for i in range(t):
        if birthday_paradox(random_birthday_list(23)):
            count += 1
    result = count/t
    print("随机{}次，23个人中至少两个人生日相同的概率为：{}".format(t, result))
