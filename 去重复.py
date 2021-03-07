import os
import sys
import time
import send2trash          #删除到回收站


path =  sys.path[0]  #所在的根目录
print(path)

content_list = []  #文件列表
dup_files = []     #删除列表

for root, dirs, files in os.walk(path):
    for file in files:
        file_path = os.sep.join([root,file]) #文件路径
        file_name, file_type = os.path.splitext(file) 
        if len(content_list)>=1:    #列表有2个了开始比较
            print('当前文件',file_name,file_type)


            #mov检查              #mov后一个是原件,前一个是大体积版本
            if file_type == '.MOV' or file_type == '.mov':
                if file_name.split('_')[-1] == 'HEVC':
                    print('     这是个mov原件 检查重复',file_path)
                    if '.MOV' == content_list[-1].split('\t')[-1]:
                        print('     上一个是mov文件,检查是否重复')
                        print('     本文件名称',file_name.split('_')[-2])
                        print('     上一个文件地址',content_list[-1])
                        print('     上一个文件名称',(content_list[-1].split('\t')[-2]).split('_')[-1])
                        if file_name.split('_')[-2] == (content_list[-1].split('\t')[-2]).split('_')[-1]:
                            print('     名称相同,确认重复')
                            dup_files.append(content_list[-1].split('\t')[0])
                            print('     添加上一个 去删除列表',content_list[-1].split('\t')[0])
                    

            #jpg检查上一个是否原件           #jpg前一个是原件,后一个是大体积版本
            if file_type == '.JPG' or file_type == '.jpg':
                print('这是个jpg',file_path,'检查是否重复')
                print('     上个文件',content_list[-1].split('\t')[-2],content_list[-1].split('\t')[-1])
                if file_name == content_list[-1].split('\t')[-2]: #判断当前音频内容与上一个文件的音频内容是否相等
                    print('     和上一个文件名相同')
                    if '.HEIC' == content_list[-1].split('\t')[-1]:
                        print('     上一个文件是heic文件')
                        dup_files.append(file_path)      #将需要删除的重复音频放入dup_files列表中
                        print('     添加当前文件  删除列表')
                else:
                    print('     没有重复下一个')
                    
        content_list.append(file_path+'\t'+file_name+'\t'+file_type) #将文件名称与内容放入content_list当中

        #time.sleep( 1 )    #用于测试的时候逐条看行为是否正确
print(dup_files)



#---------删掉 删除列表的文件
#!!!确认程序行为正确了  解除这段注释
#!!!make sure program does what you want,uncomment this part
'''
for dup_file in dup_files:
    if os.path.exists(dup_file): #判断是否存在重复的音频
        send2trash.send2trash(dup_file)
        
'''