#coding:utf-8
import re
import csv


with open('E:/code/vscode_Pythoncode/Spider/source2.txt','r',encoding='UTF-8') as f:
    source=f.read()


result_list=[]
username_list=re.findall('img username="(.*?)" class=',source,re.S)
content_list=re.findall('d_post_content j_d_post_content " style="display:;">(.*?<)',source,re.S)
content_list=[str(i) for i in content_list]
content_list=''.join(content_list)
content_list=re.findall('            (.*?)<',content_list,re.S)


reply_time_list=re.findall('楼</span><span class="tail-info">(.*?)</span></div>',source,re.S)
floor_list=re.findall('</a></span><span class="tail-info">(.*?楼)</span><span class=',source,re.S)
floor_list=[str(i) for i in floor_list]
floor_list=''.join(floor_list)
floor_list=re.findall('\\d*?楼',floor_list,re.S)
for i in range(len(username_list)):
    result={
        'floor':floor_list[i],
        'username':username_list[i],
        'content':content_list[i],
        'reply_time':reply_time_list[i]
    }
    result_list.append(result)


with open('e:/code/vscode_Pythoncode/Spider/tieba.csv','a',encoding='gbk',newline='') as f :
    writer=csv.DictWriter(f,['floor','username','content','reply_time'])
    writer.writeheader()
    writer.writerows(result_list)
