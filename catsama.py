import random
import string
import numpy as np, numpy.random
from mastodon import Mastodon

# 随机生成num个中文字符并输出为list
def GBK2312(num):
    str = ''
    if num == 0:
        return str
    for i in range(1,num+1):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x}{body:x}'
        str = str + bytes.fromhex(val).decode('gb2312')
    return list(str)

# 随机生成num个数字并输出为list
def listNum(num):
    nums = []
    while len(nums) < num:
        i = random.randint(0,9)
        nums.append(i)
    return list(str(nums))

# 生成猫猫语
def predictfuture():
    # 随机生成n个数字
    numN = random.randint(0,9)
    num = listNum(numN)
    # 随机生成n个字母
    src_letters = string.ascii_letters
    letN = random.randint(0,26)
    letters = random.sample(src_letters,letN)
    # 随机生成n个特殊字符
    spN = random.randint(0,6)
    src_special = string.punctuation
    special = random.sample(src_special,spN)
    # 随机生成n个汉字
    chN = random.randint(0,26)
    chinese = GBK2312(chN)
    # 合并所有随机生成的内容
    ran_list = num + letters + special + chinese
    # 随机打乱生成的内容
    random.shuffle(ran_list)
    # print(ran_list)
    # list转str
    temp = ''.join(ran_list)
    numS = numN + letN + spN + chN
    # 填补可能出现的所有类型字符都为0或随机长度为0的情况
    ABC_list = ['Enjolras', 'Combeferre', 'Jean prouvaire', 'Feuilly', 'Courfeyrac',' Bahorel', 'Lesgle or Laigle', 'Joly', 'Grantaire']
    friendABC = random.randint(0, len(ABC_list)-1)
    # 输出猫猫语
    if numS == 0:
        catsama = ABC_list[friendABC]
    else:
        catl = random.randint(0,numS)
        if catl == 0:
            catsama = ABC_list[friendABC]
        else:
            catsama = temp[0:catl]
    return catsama

mastodon = Mastodon(
    access_token = 'mybot_usercred.secret',
    api_base_url = 'https://musain.cafe',
)

content = predictfuture() +', miao!'
# print(content)

mastodon.status_post(content)
