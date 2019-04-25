f=open('student_bmi_source.txt','a') #创建新文件，用来储存程序运行结束后的数据
base=open('student_bmi_source.txt','rb')#读取文件
record_list = {} #创建空的字典，用来储存学生信息
for line in base:
    if len(line)==0: #行为空代表已读完文件，跳出循环
        break
    else:#若行非空，则读取到字典中
        item=line.strip().split(':')  #读取每一行时用分隔符：来区分名字和bmi数值
        record_list[item[0]]=item[1] #将名字作为key，bmi作为value
base=open('student_bmi_source.txt','wb')
base.seek(0)  #此行为配合清空文件，具体原理尚未弄清
base.truncate() #将文件清空
base.close()#清空后关闭文件
initial_page=input('欢迎进入清华大学学生信息管理系统：登陆请按\'Y\',退出请按其他任意键：\n') #登陆界面
while initial_page=='Y' or initial_page=='y':  #判断用户是否进行登陆
    print('欢迎来到主界面：\n')
    menu=('1.录入','2.查询','3.修改','4.删除','5.预览','6.退出') #显示菜单选项
    for i in menu:
        print(i)
    order=input('\n请输入您想要进行的操作序号：')
    numbers=('1','2','3','4','5','6')
    if order in numbers: #判断用户序号是否选择正确
        print('\n正在为您提供服务，请稍候：')
        while order=='1': #判断是否进行录入操作
            name=input('\n请输入您的姓名：')  #信息输入：姓名
            height=int(input('\n请输入您的身高(cm)：'))/100 #信息输入：身高
            weight=int(input('\n请输入您的体重(kg)：'))#信息输入：体重
            bmi=float('%.2f'%(weight/(height**2))) #计算出BMI
            print('\n您的BMI指数为：%.2f'%bmi) #在窗口显示BMI
            record_list[name]=bmi #记录姓名和对应的BMI指数
            exit=input('\n录入成功！请按\'Y\'键继续录入，按其他任意键返回主菜单') #继续录入or退出
            if exit!='Y':
                break
            else:
                continue
        while order=='2':
            name=input('\n请输入您要查询的学生姓名：')
            if name in record_list:
                print('\n正在查询，请稍候\n')
                if record_list[name]<=18.5:
                    print('%s的BMI指数为%.2f,体重偏瘦'%(name,record_list[name]))
                elif record_list[name]<=24:
                    print('%s的BMI指数为%.2f,体重标准，注意保持噢！'%(name,record_list[name]))
                elif record_list[name]<=27:
                    print('%s的BMI指数为%.2f,体重偏胖，小心饮食！' % (name, record_list[name]))
                elif record_list[name]<=32:
                    print('%s的BMI指数为%.2f,体重肥胖，注意减肥！' % (name, record_list[name]))
                else:
                    print('%s的BMI指数为%.2f,体重严重肥胖，警告！' % (name, record_list[name]))
                exit=input('\n查询完毕！请按\'Y\'键继续查询，按其他任意键返回主菜单') #继续查询or退出
                if exit =='Y':
                    continue
                else:
                    break
            else:
                print('\n您要查询的姓名不存在')
                exit=input('\n请按\'Y\'键继续查询，按其他任意键返回主菜单')
                if exit=='Y':
                    continue
                else:
                    break
        while order=='3':
            name=input('\n请输入您要修改的学生姓名：')
            if name in record_list:
                height=int(input('\n请输入身高（cm）:'))/100
                weight=int(input('\n请输入体重（kg）:'))
                bmi=float('%.2f'%(weight/(height2)))
                record_list[name]=bmi
                exit=input('\n您的信息已修改完毕，按\'Y\'继续修改，按其他任意键返回主菜单')
                if exit=='Y':
                    continue
                else:
                    break
            else:
                print('\n您要修改的学生不存在，请重新输入')
                continue
        while order=='4':
            name=input('\n请输入您要删除的学生姓名：')
            if name in record_list:
                record_list.pop(name)
                exit=input('\n删除成功，请按\'Y\'继续删除，按其他任意键返回主菜单')
                if exit=='Y':
                    continue
                else:
                    break
            else:
                exit2=input('\n查无此人，请按\'Y\'继续删除，按其他任意键返回主菜单')
                if exit2=='Y':
                    continue
                else:
                    break
        while order=='5':
            print(record_list)
            exit=input('\n预览完毕，请按任意键返回主菜单')
            break
        if order=='6':
            print('\n感谢您的使用，再见！')
            break
    else:
        print('\n您输入的序号有误，请重新输入')
        continue

#将数据写到文件里
source=open('student_bmi_source.txt','wb') #打开文件，使用wb为write模式，b代表binary模式
for key,value in record_list.items():
    str_value=str(value) #value为数值，要写到文件中就得转化为str
    info=key+':'+str_value+'\n'#将每个学生的信息合为一个字符串
    b_info=bytes(info,encoding='utf-8')#前面设置binary，此处进行转化，将str变为binary
    source.write(b_info)
source.close()