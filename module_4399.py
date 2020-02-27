# -*- coding: utf-8 -*-
import requests,json,time,sqlite3
from lxml import etree
from urllib import parse
#链接数据库
def link_db(uid,name,pw,cookie):
    cnt = sqlite3.connect('C:/Users/ly/Desktop/py_temporary/account_4399/account_4399.db')
    cur = cnt.cursor()#创建游标
    #print(cur.execute(".tables"))
    print(cur.execute("INSERT INTO MAIN VALUES ({0},'{1}','{2}','{3}');".format(uid,name,pw,cookie)))
    #cnt.execute("DELETE from MAIN where UID=2968726696;")
    account = cur.execute("SELECT * FROM MAIN;")
    #print(cur.fetchall())
    for row in account:
        print ("UID = ", row[0])
        print ("USERNAME = ", row[1])
        print ("PASSERWORD = ", row[2])
        print ("COOKIE = ", row[3], "\n")
    cnt.commit()
#判断登录状态
def judge_sign_data(data):
    selector = etree.HTML(data)
    if selector.xpath("//*[@id='Msg']") != []:
        sign_error =selector.xpath("//*[@id='Msg']")
        print(sign_error[0].text.strip())
        return 1
    elif selector.xpath("/html/body/script[2]") != []:
        print("登录成功")
        return 0
    else:
        print("需要验证码")
        return 2
#登录账号，返回uid与cookie
def sign_in(passername,passerword,captcha=""):
    data=r"loginFrom=uframe&postLoginHandler=default&layoutSelfAdapting=true&externalLogin=qq&displayMode=undefined&layout=vertical&appId=my&gameId=&css=%2F%2Fs1.img4399.com%2Fbase%2Fcss%2Fptlogin.css%3F431c76e&redirectUrl=&sessionId=captchaReqddf4cf8217f50404217&mainDivId=popup_login_div&includeFcmInfo=false&userNameLabel=4399%E7%94%A8%E6%88%B7%E5%90%8D&userNameTip=%E8%AF%B7%E8%BE%93%E5%85%A54399%E7%94%A8%E6%88%B7%E5%90%8D&welcomeTip=%E6%AC%A2%E8%BF%8E%E5%9B%9E%E5%88%B04399&username={0}&password={1}&inputCaptcha={2}".format(passername,passerword,captcha)
    try:
        rsp = requests.post("http://ptlogin.4399.com/ptlogin/login.do?v=1",data=data,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36","Host": "ptlogin.4399.com","Accept-Encoding": "gzip, deflate","Referer":"http://ptlogin.4399.com/ptlogin/loginFrame.do?postLoginHandler=default&redirectUrl=&displayMode=popup&css=&appId=www_home&gameId=&username=liuyunfz&externalLogin=qq&password=&mainDivId=popup_login_div&autoLogin=false&includeFcmInfo=false&qrLogin=true&v=1564145136161","Connection":"keep-alive","Cache-Control":"max-age=0","Origin":"http://ptlogin.4399.com","Upgrade-Insecure-Requests":"1","Content-Type":"application/x-www-form-urlencoded","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","Accept-Language":"zh-CN,zh;q=0.9","Cookie":r"UM_distinctid=16be1237f3d330-0026f1ba77007-e343166-1fa400-16be1237f3e8d7; _gprp_c=\"\"; Qnick=; _4399tongji_vid=156311428638372; _4399stats_vid=15631142873775485; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1562850329,1563114258,1563190247; ptusertype=my.4399_login; Puser=liuyunfz; Xauth=80b197113153cacc4d59b638f294d8a2; Pnick=%E9%A5%B0%E9%9D%9E; Uauth=4399\|1\|2019718\|my.#my.my\|1563421044972\|fd0b9e06776a854c6a80194081f5ea00; home4399=yes; USESSIONID=ec2acf31-7106-4f84-a85e-32a89421c6dd"},timeout=3)
        #print(rsp.text)
        if judge_sign_data(rsp.text) == 0:
            global cookieStr,username,userid
            cookieStr = ''        
            for item in rsp.cookies:
                #print(item.name,"   :    ",item.value)
                cookieStr = cookieStr + item.name + '=' + item.value + ';'
            username = parse.unquote(rsp.cookies["Pnick"])
            Pauth = rsp.cookies["Pauth"]
            split_pauth = Pauth.split("|")
            userid = split_pauth[0]
            return [userid,cookieStr]
        else:
            return 1
        
    except TimeoutError:
        print("time faild")
        return 2
    except:
        print("sign error")       
        return 3
#群组首页签到
def daily_sign(cookie):
    url = "http://my.4399.com/plugins/sign/set-t-{0}".format(int(time.time()*1000))
    print(url)
    try:
        sign_headers={
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Connection":"keep-alive",
        "Host":"my.4399.com",
        "Referer":"http://my.4399.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        "Cookie":cookie
        }
        rsp = requests.get(url,headers=sign_headers)
        sign_json = json.loads(rsp.text)
        if sign_json["code"] == 100:
            return 0
        else:
            return sign_json["result"]

    except:
        return 1
#获取群组等级信息
def information_grade(cookie):
    try:
        url = "http://my.4399.com/jifen/async-user?t=1563163288000&keys%5B%5D=credit&keys%5B%5D=grade&keys%5B%5D=growth&keys%5B%5D=next&keys%5B%5D=upgrade_percent&keys%5B%5D=next_grade&keys%5B%5D=upgrade_growth&keys%5B%5D=grade_percent"
        headers={
            "Host":"my.4399.com",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Cookie":cookieStr
        }
        rsp = requests.get(url=url,headers=headers,timeout=3)       
        rsp_grade = json.loads(rsp.text)
        #print(rsp_grade["code"])
        
        if rsp_grade["code"] == 100:            
            grade = rsp_grade["result"]["grade"]
            credit = rsp_grade["result"]["credit"]
            growth = rsp_grade["result"]["growth"]
            grade_next = rsp_grade["result"]["next"]
            upgrade_percent = rsp_grade["result"]["upgrade_percent"]            
            return([grade,credit,growth,grade_next,upgrade_percent])
        else:
            return 1 
            #print("grade error") 
    except:
        return 2
        #print("information_grade error")
#获取粉丝与关注等信息
def information_fans(uid):
    try:
        url="http://my.4399.com/forums/user-info?uid={0}&withMedal=1&_AJAX_=1".format(userid)
        headers={
            "Host":"my.4399.com",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive"
        }
        rsp = requests.get(url=url,headers=headers)
        rsp_json = json.loads(rsp.text)
        if rsp_json["code"] == 100:            
            followed = rsp_json["result"]["num_been_followed"]
            num_feed = rsp_json["result"]["num_feed"]
            avatar = rsp_json["result"]["avatar"]
            num_follow = rsp_json["result"]["num_follow"]                    
            return([followed,num_follow,num_feed,avatar])
        else:
            return 1
            #print("fans error")
    except:
        return 2
        #print("information_fans error")
#积分抽奖
def Lottery(cookie:str):
    url = "http://my.4399.com/jifen/lottery-draw?callback=jQuery17203331212748551664_{0}&callback=LotteryDraw.getPrize&_={0}".format(int(time.time()*1000))
    #print(url)
    try:
        sign_headers={
        'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection':'keep-alive',
        'Cookie':cookie,
        'Host':'my.4399.com',
        'Referer':'http://my.4399.com/jifen/activity-i-31e3d0ed909fd9fe8ede6601e0f816e5-f-1649066526',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }
        #requests.get(url="http://my.4399.com/jifen/activity-invite-code-31e3d0ed909fd9fe8ede6601e0f816e5-fid-1649066526",headers=sign_headers)
        rsp = requests.get(url,headers=sign_headers,timeout=2)
        return (json.loads(rsp.text[21:-2])['result']['res'].get("res"))
    except:
        return "error"
