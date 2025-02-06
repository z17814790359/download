import requests

def get_pictures(url,path):
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'}
    re=requests.get(url,headers=headers)
    print(re.status_code)#查看请求状态，返回200说明正常
    with open(path, 'wb') as f:#把图片数据写入本地，wb表示二进制储存
                for chunk in re.iter_content(chunk_size=128):
                    f.write(chunk)

input1 = input("请输入链接：")
print ("你输入的内容是: ", input1)
input2 = input("请输入类型：")
print ("你输入的内容是: ", input2)

file = open("number.txt", "r")  # 打开文件
number = file.read()  # 读取文件中的内容
file.close()  # 关闭文件
number2 = number.split(' ')

i=0
while i<len(number2):
   url=input1 + number2[i]
   path=input2 + number2[i] + '.jpg'
   i=i+1
   print(url,path,i)
   get_pictures(url,path)
