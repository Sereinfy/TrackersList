# coding=utf-8
import urllib.request
import os
import wget

url_file_path = os.getcwd()
print("当前文件路径：", url_file_path)
url_path = os.path.join(url_file_path, 'main_url.txt')
if os.path.exists(url_path):
    print("检测到文件")
    print("--------------------")
else:
    print("文件不存在！正在创建中......")
    main_url = "https://raw.githubusercontent.com/Sereinfy/TrackersList/main/main/main_url.txt"
    wget.download(main_url, url_path)
    print("OK!")
    print("--------------------")

print("读取URL中......")
result = []
with open(url_path, 'r') as f:
    for line in f:
        result.append(list(line.strip('\n').split(',')))
url_number = len(result)
print("OK!")
print("URL列表：", result)
print("--------------------")

file_path = os.getcwd()
trackers_path = os.path.join(file_path, 'trackers.txt')
print("正在输出trackers至trackers.txt")
if os.path.exists(trackers_path):
    print("文件存在！正在删除原始内容......")
    with open(trackers_path, 'r+') as files:
        files.truncate(0)
    print("OK!")
    print("--------------------")
else:
    print("文件不存在！正在创建中......")
    file_trackers = open(trackers_path,'w')
    print("OK!")
    print("--------------------")

trackers_list = []
for url_line in open(url_path):
    print(url_line)
    try:
        headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        req = urllib.request.Request(url=url_line,headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        trackers_list.append(html)
        with open(trackers_path, 'a') as f:
            f.writelines(html)
            print("OK!")
        try:
            os.remove(url_path)
        except OSError as e:
            print(e)
        else:
            print("File is deleted successfully")
    except:
        continue

def remove_duplicates():
    print("--------------------")
    print("正在准备去重中...")
    output_trackers_path = os.path.join(file_path, 'output_trackers.txt')
    f_read=open(trackers_path,'r')
    f_write=open(output_trackers_path,'w')
    data=set()
    for a in [a.strip('\n') for a in list(f_read)]:
        if a not in data:
            f_write.write(a+'\n')
            data.add(a)
    f_read.close()
    f_write.close()
    print("OK!")
remove_duplicates()