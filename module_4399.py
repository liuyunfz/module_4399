# -*- coding: utf-8 -*-
import requests,json,time
from lxml import etree
from urllib import parse
#判断登录状态
def __judge_sign_data(data):
    selector = etree.HTML(data)
    if selector.xpath("//*[@id='Msg']") != []:
        sign_error =selector.xpath("//*[@id='Msg']")
        #print(sign_error[0].text.strip())
        return {"id":2,"msg":sign_error[0].text.strip()}
    elif selector.xpath("/html/body/script[2]") != []:
        #print("登录成功")
        return {"id":0,"msg":"登录成功"}
    else:
        #print("需要验证码")
        return {"id":1,"msg":"需要验证码"}
#登录账号，返回uid与cookie
def sign_in(usernames,password,captcha=""):
    data=r"loginFrom=uframe&postLoginHandler=default&layoutSelfAdapting=true&externalLogin=qq&displayMode=undefined&layout=vertical&appId=my&gameId=&css=%2F%2Fs1.img4399.com%2Fbase%2Fcss%2Fptlogin.css%3F431c76e&redirectUrl=&sessionId=captchaReqddf4cf8217f50404217&mainDivId=popup_login_div&includeFcmInfo=false&userNameLabel=4399%E7%94%A8%E6%88%B7%E5%90%8D&userNameTip=%E8%AF%B7%E8%BE%93%E5%85%A54399%E7%94%A8%E6%88%B7%E5%90%8D&welcomeTip=%E6%AC%A2%E8%BF%8E%E5%9B%9E%E5%88%B04399&username={0}&password={1}&inputCaptcha={2}".format(usernames,password,captcha)
    try:
        rsp = requests.post("http://ptlogin.4399.com/ptlogin/login.do?v=1",data=data,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36","Host": "ptlogin.4399.com","Accept-Encoding": "gzip, deflate","Referer":"http://ptlogin.4399.com/ptlogin/loginFrame.do?postLoginHandler=default&redirectUrl=&displayMode=popup&css=&appId=www_home&gameId=&username=liuyunfz&externalLogin=qq&password=&mainDivId=popup_login_div&autoLogin=false&includeFcmInfo=false&qrLogin=true&v=1564145136161","Connection":"keep-alive","Cache-Control":"max-age=0","Origin":"http://ptlogin.4399.com","Upgrade-Insecure-Requests":"1","Content-Type":"application/x-www-form-urlencoded","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","Accept-Language":"zh-CN,zh;q=0.9","Cookie":r"UM_distinctid=16be1237f3d330-0026f1ba77007-e343166-1fa400-16be1237f3e8d7; _gprp_c=\"\"; Qnick=; _4399tongji_vid=156311428638372; _4399stats_vid=15631142873775485; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1562850329,1563114258,1563190247; ptusertype=my.4399_login; Puser=liuyunfz; Xauth=80b197113153cacc4d59b638f294d8a2; Pnick=%E9%A5%B0%E9%9D%9E; Uauth=4399\|1\|2019718\|my.#my.my\|1563421044972\|fd0b9e06776a854c6a80194081f5ea00; home4399=yes; USESSIONID=ec2acf31-7106-4f84-a85e-32a89421c6dd"},timeout=3)
        status = __judge_sign_data(rsp.text)
        if status["id"] == 0:
            global username,cookieStr,userid
            cookieStr = ''        
            for item in rsp.cookies:
                cookieStr = cookieStr + item.name + '=' + item.value + ';'
            username = parse.unquote(rsp.cookies["Pnick"])
            Pauth = rsp.cookies["Pauth"]
            split_pauth = Pauth.split("|")
            userid = split_pauth[0]
            return {"id":0,"msg":"登录成功",'userid':userid,'username':username,'cookie':cookieStr}
        elif status['id'] == 1:
            return {"id":1,"msg":"需要验证码"}
        else:
            return {"id":2,"msg":status['msg']}
        
    except TimeoutError:
        #print("time faild")
        return {"id":3,"msg":"timeout"}
    except:
        #print("sign error")       
        return {"id":4,"msg":"something error"}
#群组首页签到
def daily_sign(cookie):
    url = "http://my.4399.com/plugins/sign/set-t-{0}".format(int(time.time()*1000))
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
        return sign_json

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
        '''
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
        '''
        return rsp_grade
    except:
        return 2
        #print("information_grade error")
#获取粉丝与关注等信息
def information_fans(uid):
    try:
        url="http://my.4399.com/forums/user-info?uid={0}&withMedal=1&_AJAX_=1".format(uid)
        headers={
            "Host":"my.4399.com",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Cache-Control":"max-age=0",
            "Cookie":"",
            "Connection":"keep-alive"
        }
        rsp = requests.get(url=url,headers=headers)
        rsp_json = json.loads(rsp.text)
        #print(rsp_json)
        if rsp_json["code"] == 100:            
            followed = rsp_json.get("result").get("num_been_followed")
            num_feed = rsp_json.get("result").get("num_feed")
            avatar = rsp_json.get("result").get("avatar")
            num_follow = rsp_json.get("result").get("num_follow")                  
            return {"id":0,'followed':followed,'num_follow':num_follow,'num_feed':num_feed,'avatar':avatar}
        else:
            return {"id":1,'result':rsp_json}
            #print("fans error")
        
        #return rsp_json
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
#独家游戏签到
def sign_djyx(cookie:str):
    url = "http://huodong.4399.com/2016/djyx/ajax.php"
    try:
        sign_headers={
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection':'keep-alive',
        'Content-Length':'32',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':cookie,
        'Host':'huodong.4399.com',
        'Origin':'http://huodong.4399.com',
        'Referer':'http://huodong.4399.com/2016/djyx/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }
        rsp = requests.post(url,headers=sign_headers,timeout=2,data='act=sign&rand=0.1416582288761603')
        return (rsp.json())
    except:
        return "error"
#群组签到
def sign_grade(cookie:str,tagid:int):
    url = "http://my.4399.com/forums/grade-signIn"
    try:
        sign_headers={
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection':'keep-alive',
        'Content-Length':'27',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':cookie,
        'Host':'my.4399.com',
        'Origin':'http://my.4399.com',
        'Referer':'http://my.4399.com/forums/mtag-84526',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }
        rsp = requests.post(url,headers=sign_headers,timeout=2,data='sign=1&tagid={0}&_AJAX_=1'.format(str(tagid)))
        return (rsp.json())
    except:
        return "error"
#获取已关注的群组信息
def information_group(cookie:str,uid:int):
    try:
        headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Connection':'keep-alive',
            'Cookie':cookie,
            'Host':'my.4399.com',
            'Referer':'http://my.4399.com/u/352612664/index',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        rsp = requests.get(url="http://my.4399.com/u/{0}/mtag".format(uid),headers=headers)
        rsp.encoding="utf-8"        
        selector=etree.HTML(rsp.text)
        data_list=selector.xpath('//*[@id="j-mtaglist"]/li')
        information_group_list=[]
        for i in data_list: 
            dict_group={'title':i.xpath('./div[1]/a/text()')[0],'img':i.xpath('./div[2]/a/img/@src')[0],'level':i.xpath('./div[2]/div/div[1]/i/@class')[0][2:],'experience':i.xpath('./div[2]/div/div[1]/text()')[2].strip()}
            information_group_list.append(dict_group)      
        return information_group_list
    except:
        return "error"
#帖子点赞
def operate_flower(cookie:str,tid:int,captcha="",captchaid=""):
    url="http://my.4399.com/forums/operate-click"
    headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '60',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': cookie,
    'Host': 'my.4399.com',
    'Origin': 'http://my.4399.com',
    'Referer': 'http://my.4399.com/forums/thread-53382781',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
    data = "tid={0}&clickid=14&captchaid={2}&captcha={1}&guide=0&_AJAX_=1".format(tid,captcha,captchaid)
    rsp = requests.post(url=url,data=data,headers=headers)
    rsp_json = json.loads(rsp.text)
    return rsp_json
#获取积分_玩游戏（每日上限五次）
def get_integral_playgame(game_id:str,cookie:str):
        #game_list=['211324','211421','211338','211257','211305']
    try:
        url="http://my.4399.com/credit/earnScore-gameCredit?game_id={0}".format(game_id)
        headers={
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Connection':'keep-alive',
            'Cookie':cookie,
            'Host':'my.4399.com',
            'Referer':'http://my.4399.com/jifen/earnScore',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        rsp=requests.get(url=url,headers=headers)
        return rsp.json
    except:
        return 'error'

