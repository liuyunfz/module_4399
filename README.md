# module_4399
一个囊括了基本所有4399网络协议的储存库，主要使用语言为Python，基于Requests模块，欢迎star或提交issue。<br>
## **已有功能**
- 4399群组登录
- 4399群组首页签到
- 4399群组等级判断
- 4399群组粉丝及关注判断
- 4399群组积分抽奖<br>
## **暂未添加功能**
- ~~4399群组hash验证~~
- ~~4399群组帖子鲜花~~
- ~~4399群组关注~~<br>
## **第三方Python库**
- requests
- lxml
## **已发布在第三方平台上的教程**    

- [4399登录详解](https://www.coolapk.com/feed/13068295?shareKey=YWFjNWViNjYxYTRhNWQ5NTYxNmE~&shareUid=1256119&shareFrom=com.coolapk.market_9.5)
- [利用cookie爬取4399单个群组的用户数据](https://www.coolapk.com/feed/13102437?shareKey=MzA5Y2ZmNmI3YTc5NWQ5NTY2MmY~&shareUid=1256119&shareFrom=com.coolapk.market_9.5)
- [爬取4399全站用户](https://www.coolapk.com/feed/13180495?shareKey=ZGFmODg4ZWIwM2E5NWQ5NTY2NzQ~&shareUid=1256119&shareFrom=com.coolapk.market_9.5)
- [4399HASH实战破解](http://blog.6yfz.cn/%E5%AE%9E%E6%88%984399%E7%A0%B4%E8%A7%A3HASH%E9%AA%8C%E8%AF%81.html)   <br>
## **功能解析**
### 1. 4399登录
方法名:sign_in  
|需要参数|参数类型|说明                  |
|:- |:- |:-|
|username  |string |登录账户的用户名   |
|password  |string | 登录账户的密码    |
|captcha   |string |验证码，可空       |
  
返回数据（type:json）  
|key|说明                              |
|:-  |:-   |
|id  |登录状态返回，0-登录成功  ；1-需要验证码  ；2-其他错误，通过msg返回具体内容   |
|msg  | 登录的具体状态描述                     |
|userid|用户的id，仅在登录成功时返回                         |
|username|用户的论坛名，仅在登录成功时返回                         |
|cookie|账号登录cookie，仅在登录成功时返回                         |
  
### 2. 4399群组首页签到
方法名:daily_sign  
|需要参数|参数类型|说明                              |
|:-  |:-|:-   |
|cookie   |string    |需要签到用户的账户cookie，可通过登录函数返回   |
  
返回数据（type:json）  
返回的为官方json，请自行尝试分析。
### 3. 剩余功能，下次添加
## **展望**
⭐⭐⭐
未来会以md教程的方式实现4399群组的全站爬取
⭐⭐⭐
