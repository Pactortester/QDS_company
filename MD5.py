# 由于MD5模块在python3中被移除
# 在python3中使用hashlib模块进行md5操作

import hashlib

# 待加密信息


number = input('请输入待加密信息:')

# 创建md5对象
hl = hashlib.md5()

# Tips
# 此处必须声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
hl.update(number.encode(encoding='utf-8'))

print('MD5加密前为:' + number)
print('MD5加密后为:' + hl.hexdigest())