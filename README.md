# module_4399
一个囊括了基本所有4399网络协议的储存库，主要使用语言为Python，基于Requests模块，欢迎star或提交issue。<br>
## 已有功能
- [4399群组登录](#4399登录)
- [4399群组积分抽奖](#积分抽奖)
- [4399独家游戏签到](#独家游戏签到)
- [4399群组信息获取](#群组信息获取)
- [4399群组首页签到](#4399群组首页签到)
- [4399群组帖子表态](#群组帖子表态)
- [4399群组等级信息获取](#获取群组等级信息)
- [4399群组粉丝及关注信息获取](#获取粉丝与关注信息)<br>
## 暂未添加功能
- ~~4399群组hash验证~~
- ~~4399群组关注~~<br>
## 第三方Python库
- requests
- lxml
## 已发布在第三方平台上的教程    

- [4399登录详解](https://www.coolapk.com/feed/13068295?shareKey=YWFjNWViNjYxYTRhNWQ5NTYxNmE~&shareUid=1256119&shareFrom=com.coolapk.market_9.5)
- [利用cookie爬取4399单个群组的用户数据](https://www.coolapk.com/feed/13102437?shareKey=MzA5Y2ZmNmI3YTc5NWQ5NTY2MmY~&shareUid=1256119&shareFrom=com.coolapk.market_9.5)
- [爬取4399全站用户](https://www.coolapk.com/feed/13180495?shareKey=ZGFmODg4ZWIwM2E5NWQ5NTY2NzQ~&shareUid=1256119&shareFrom=com.coolapk.market_9.5)
- [4399HASH实战破解](https://blog.6yfz.cn/tutorial/python-spider-4399-hash.html)   <br>
## **功能解析**
### 4399登录
	方法名:sign_in  
|需要参数|参数类型|说明                  |
|:- |:- |:-|
|usernames  |str |登录账户的用户名   |
|password  |str | 登录账户的密码    |
|captcha   |str |验证码，可空       |

	返回数据（type:json）   
|key|说明                              |
|:-  |:-   |
|id  |登录状态返回，0-登录成功  ；1-需要验证码  ；2-其他错误，通过msg返回具体内容   |
|msg  | 登录的具体状态描述                     |
|userid|用户的id，仅在登录成功时返回                         |
|username|用户的论坛名，仅在登录成功时返回                         |
|cookie|账号登录cookie，仅在登录成功时返回                        |   

**[⬆ Back to Index](#已有功能)**
### 4399群组首页签到
	方法名:daily_sign  
|需要参数|参数类型|说明                              |
|:-  |:-|:-   |
|cookie   |str   |需要签到用户的账户cookie，可通过登录函数返回   |

	返回数据（type:json）  
返回的为官方json，请自行尝试分析。  

**[⬆ Back to Index](#已有功能)**
###  获取群组等级信息
	方法名：information_grade  
|需要参数|参数类型|说明                              |
|:-  |:-|:-   |
|cookie   |str    |需要获取等级信息的用户cookie，可通过登录函数返回   |  

	返回数据（type:json）  
返回的为官方json，请自行尝试分析。  

**[⬆ Back to Index](#已有功能)**  
### 获取粉丝与关注信息
	方法名：information_fans
|需要参数|参数类型|说明                              |
|:-  |:-|:-   |
|uid   |str    |需要获取相关信息的用户UID，此API无需cookie，但部分用户会出现NONE问题   |

	返回数据（type:json）   
|key|说明                              |
|:-  |:-   |
|id  |查询状态返回，0-查询成功  ；1-其他未知错误，通过result返回具体错误信息  |
|followed  | 被查询用户的粉丝数                     |
|num_follow| 被查询用户的关注数                        |
|num_feed|被查询用户的动态数                         |
|avator|被查询用户的头像地址（注意头像地址需要在登录状态下才可访问，否则会出现403错误）    |  
|result|仅在出错时返回result，且出错时以上key除id外全部不返回|  

**[⬆ Back to Index](#已有功能)**  

### 积分抽奖
	方法名：Lottery
|需要参数|参数类型|说明                              |
|:-  |:-|:-   |
|cookie   |str    |需要抽奖的账号cookie   |

	返回数据（type:json or NONE） 
>本方法已对返回数据进行了筛选，如果未抽中奖品则返回NONE，如果已抽中则返回官方json，如果需要获取其他信息，如：积分花费。请自行重写本功能。  
>以下为官方返回json的说明  
  
|key|说明                              |
|:-  |:-   |
|name  |奖品名称  |
|num  | 奖品数量                     |
|src| 奖品描述，即对应奖品的图片地址                       |
|msg|获奖提示，如：恭喜您获得【1积分】                      |
|time|获奖时间，格式为YYYY-MM-DD    |    

**[⬆ Back to Index](#已有功能)**  
  
### 独家游戏签到
	方法名：sign_djyx
|需要参数|参数类型|说明                              |
|:-  |:-|:-   |
|cookie   |str    |需要签到的账号cookie   |

	返回数据（type:json） 
>直接返回官方数据，以下为官方返回json的说明  
  
|key|说明                              |
|:-  |:-   |
|key  |签到的状态，成功返回suc，失败返回error  |
|ljuan  | 返回账号当前的礼劵数，仅在成功后返回  |
|msg| 错误信息，仅在失败后返回     |   

**[⬆ Back to Index](#已有功能)**  
  
### 群组信息获取
	方法名：information_group
|需要参数|参数类型|说明                              |
|:-  |:-|:-   |
|cookie   |str    |任意账号cookie（读取他人主页信息必须已登录） |
|uid   |int    |需要获取群组信息的用户UID   |

	返回数据（type:list）  
>	根据每个群组一个dict，统一储存在list中进行返回  
	以下是dict中的key值说明
 
|key|说明                              |
|:-  |:-   |
|title  |群组名称  |
|img  | 群组的贴图地址  |
|level| 群组等级     |   
|experience| 群组具体经验信息     |  

**[⬆ Back to Index](#已有功能)**  
  
### 群组帖子表态
	方法名：operate_flower
|需要参数|参数类型|说明                              |
|:-  |:-|:-   |
|cookie   |str    |要表态账号的cookie |
|tid   |int    |需要表态的帖子tid   |
|captcha   |str    |验证码，可空   |
|captchaid   |str    |验证码id，可空   |

	返回数据（type:json）  
>	返回官方json，以下是官方json的说明
 
|key|说明                              |
|:-  |:-   |
|code  |表态状态。  100-成功  98-需要验证码  159-已参与表态|
|result  | 成功时返回空串，已表态时返回None，需要验证码时将返回以下两个参数  |
|msg  | 表态状态具体信息返回 |
|:-  |:-   |
|id| 验证码id，仅在需要验证码时返回，处于result目录下     |   
|img| 验证码地址，仅在需要验证码时返回，处于result目录下     |  

**[⬆ Back to Index](#已有功能)**  
## **展望**
⭐⭐⭐
未来会以md教程的方式实现4399群组的全站爬取
⭐⭐⭐
