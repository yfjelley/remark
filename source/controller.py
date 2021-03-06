# -*- coding:utf-8 -*-

import sys
import random
import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.escape
import importlib
import requests
import traceback

import model

class controller(tornado.web.RequestHandler):
    """ 基类
    """

    dicViewData = {} # 模板输出数据

    _GET = False
    _POST = False

    rquests = requests
    operatStatus = 0

    strViewPath = ''
    escape = tornado.escape
    dicConfig = {}

    def initialize(self, _config = None):
        ''' 初始化
        '''
        self.dicConfig = self.application.settings
        if _config:
            for key, value in _config.items():
                self.dicConfig[key] = value

        self.model = model.Model()
        self.model.init(self.dicConfig)
        self.session_init()
    
    def on_finish(self):
        # print 'on_finish'
        self.model.finish()

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        """ 接受GET请求
            固定参数a，如果a有值，调用同名方法，如果a没有值，调用index方法
        """
        
        strAction = self.I('a')
        strAction = strAction if strAction else 'index'

        # 请求类型
        self._GET = True

        if strAction:
            if not self.dicConfig['debug']:
                try:
                    method = eval('self.' + strAction)
                    method()
                except Exception, e:
                    print e
                    self.redirect('/error')
            else:
                method = eval('self.' + strAction)
                method()

        return


    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """ 接受POST请求
            固定参数a，如果a有值，调用同名方法，如果a没有值，调用index方法
        """

        strAction = self.I('a')
        strAction = strAction if strAction else 'index'

        # 请求类型
        self._POST = True

        if strAction:
            if not self.dicConfig['debug']:
                try:
                    method = eval('self.' + strAction)
                    method()
                except Exception, e:
                    print e
                    self.redirect('/error')
            else:
                method = eval('self.' + strAction)
                method()

        return


    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def rquest(self, strUrl, strType, dicData):
        """ 发起请求

        @params strUrl string 请求地址
        @params strType string 请求类型，可以是GET，POST
        @params dicData dict 发送数据
        """

        if strType == 'POST':
            res = self.rquests.post(strUrl, dicData)
            return res.text

        if strType == 'GET':
            res = self.rquests.get(strUrl, dicData)
            return res.text

        return 'type error, must POST or GET'


    def display(self, strViewName, strViewPath = '', className=''):
        """ 输出模板
            调用模板输出，使用当前类名为模板目录

        @params strViewName string 调用模板名称
        @params dicData dict 输出数据
        """

        strViewPath = strViewPath if strViewPath else self.strViewPath

        if self.dicViewData and self.operatStatus==0:
            self.dicViewData['moduleOpera'] = 200
        elif self.operatStatus==1:

            self.dicViewData['moduleOpera'] = 403

        try:
            if not className:
                self.render("%s/%s/%s.html" % (strViewPath, self.__class__.__name__, strViewName), controller = self.__class__.__name__, **self.dicViewData)
            else:
                self.render("%s/%s/%s.html" % (strViewPath, className, strViewName), controller = className, **self.dicViewData)
        except Exception, e:
            if self.dicConfig['debug']:
                print "-------------------------- debug ------------------------------"
                print (strViewPath, self.__class__.__name__, strViewName)
                print e
                print traceback.format_exc()
                print "-------------------------- debug -------------------------------"
            else:
                self.redirect('/700')


    def I(self, strKey, defaulVal = ''):
        """ 获取请求参数
            如果只有一个值，将其转为字符串，如果是list，保留list类型

        @params strKey string 参数名称
        """

        try:
            lisValue = self.request.arguments[strKey]
            if len(lisValue) > 1:
                lisValueStrip = []
                for item in lisValue:
                    lisValueStrip.append(item.strip())

                return lisValueStrip
            else:
                return lisValue[0].strip()
        except Exception, e:
            return defaulVal


    def II(self, strKey):
        """ 获取请求参数
            只返回list类型

        @parmas strKey string 参数名称
        """

        try:
            lisValue = self.request.arguments[strKey]

            lisValueStrip = []
            for item in lisValue:
                lisValueStrip.append(item.strip())

            return lisValueStrip
        except Exception, e:
            return ''

    def importService(self, strServiceName, strServiceParam = {}):
        """ 加载服务类

        @params strServiceName string 服务类名
        @params strServiceParam string 服务类参数
        """
        
        strServiceParam['host'] = self.request.host

        try:
            service = importlib.import_module('service.' + strServiceName)
            return service.service(self.model, strServiceParam)
        except Exception, e:
            print e
            return None

    def session_init(self):
    
        self.strSessionTableName = 'sessions'
        
        self.session_id = self.session_get_id()
        if not self.session_id:
            self.session_id = self.session_set_id()

    def session_set_id(self):
        """ 设置session id
        """

        strChrset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWSYZ"
        
        lisSession = []
        for i in range(16):
            strItem = random.choice(strChrset)
            lisSession.append(strItem)

        strSessionId = ''.join(lisSession)

        self.set_secure_cookie('session_id', strSessionId)

        return strSessionId

    def session_get_id(self):
        """ 获取session id
        """
        
        strSessionId = self.get_secure_cookie('session_id')

        return strSessionId

    def session_set(self, strKey, strValue):
        """ 设置session

        @params strKey string 索引
        @params strValue string 值
        """
        
        if not strKey:
            return None

        try:
            self.model.insert(self.strSessionTableName, {
                'key': 'session_id, k, v, create_time',
                'val': '"%s", "%s", "%s", "%s"' % (
                    self.session_id,
                    strKey,
                    strValue,
                    int(time.time())
                )
            })
            self.model.db.commit()
            return True
        except Exception, e:
            print e
            return False

    def session_get(self, strKey):
        """ 获取session

        @params strKey string 索引
        """
        
        dicSession = self.model.find(self.strSessionTableName, 'first', {
            'condition': 'session_id = "%s" and k = "%s"' % (self.session_id, strKey)
        })
        
        if not dicSession:
            return None

        if not self.session_check_overtime(dicSession['create_time']):
            return None

        return dicSession['v']

    def session_get_all(self):
        """ 获取session_id对应的所有值
        """

        dicSession = {}


        tupSession = self.model.find(self.strSessionTableName, 'list', {
            'condition': 'session_id = "%s"' % self.session_id
        })
        if not tupSession:
            return None

        for item in tupSession:
            dicSession[item['k']] = item['v']

        return dicSession

    def session_clear(self, strKey = None):
        """ 清除session

        @params strKey string 索引，为空即全部清除
        """

        strCondition = 'session_id = "%s"' % self.session_id

        if strKey:
            strCondition = strCondition + ' and k = "%s"' % strKey

        try:
            self.model.delete(self.strSessionTableName, {
                'condition': strCondition
            })
            self.model.db.commit()
            return True
        except Exception, e:
            print e
            self.model.db.rollback()
            return False
            
    def session_check_overtime(self, intCreateTime):
        """ 检查过期时间

        @params intCreateTime int 创建时间
        """

        intNow = int(time.time())

        if intCreateTime + self.intOverTime >= intNow:
            return False

        return True


class server(object):
    """ 启用服务
    """

    def start(self, lisRoute, dicSetting):
        app = tornado.web.Application(lisRoute, **dicSetting)
        app.listen(dicSetting['port'], address = dicSetting['address'])
        tornado.ioloop.IOLoop.instance().start()


class error(controller):
   """ 错误处理
   """

   def index(self):
       self.display('404', '../view')

