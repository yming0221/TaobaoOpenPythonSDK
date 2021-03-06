#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 查询Detail详情, 根据DataTemplateDetailCriteriaVO信息查询<br/> justQueryParamNotInput 为true时， 则查询出来的Detail详情,只是参数没有填入的列表(（Detail中的Attribute中的ParamKey是调用其他匹配接口必填的值，按照其他接口的规范填入即可）)<br/> 默认分页查询，每页10条记录。如果查询总条数，needRetPage = true<br/> DataTemplateDetailCriteriaVO <ul> <li>attrId(Long):AttributeVO的唯一标识</li> <li>templateId(Long 必填参数):数据模板的唯一标识</li> <li>name(String):数据模板详情的名称</li> <li>id(Long):根据模板唯一标识去查询</li> <li>pageSize:分页大小（最大值30）</li> <li>currentPage:当前页码</li> <li>needRetPage(Boolean 默认False):是否返回总条数</li> <li>justQueryParamNotInput（Boolean 默认False）:是否只查询每天如PK的详情列表</li> </ul>
# @author wuliang@maimiaotech.com
# @date 2013-09-22 16:52:53
# @version: 0.0.0

from datetime import datetime
import os
import sys
import time

_jsonEnode = None
try:
    import demjson
    _jsonEnode = demjson.encode
except Exception:
    try:
        import simplejson
    except Exception:
        try:
            import json
        except Exception:
            raise Exception("Can not import any json library")
        else:
            _jsonEnode = json.dumps
    else:
        _jsonEnode = simplejson.dumps

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))
    
__parentPath = os.path.normpath(os.path.join(__getCurrentPath(), os.path.pardir))
if __parentPath not in sys.path:
    sys.path.insert(0, __parentPath)


    
from Domain.PageResult import PageResult

    

## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Response: 查询Detail详情, 根据DataTemplateDetailCriteriaVO信息查询<br/> justQueryParamNotInput 为true时， 则查询出来的Detail详情,只是参数没有填入的列表(（Detail中的Attribute中的ParamKey是调用其他匹配接口必填的值，按照其他接口的规范填入即可）)<br/> 默认分页查询，每页10条记录。如果查询总条数，needRetPage = true<br/> DataTemplateDetailCriteriaVO <ul> <li>attrId(Long):AttributeVO的唯一标识</li> <li>templateId(Long 必填参数):数据模板的唯一标识</li> <li>name(String):数据模板详情的名称</li> <li>id(Long):根据模板唯一标识去查询</li> <li>pageSize:分页大小（最大值30）</li> <li>currentPage:当前页码</li> <li>needRetPage(Boolean 默认False):是否返回总条数</li> <li>justQueryParamNotInput（Boolean 默认False）:是否只查询每天如PK的详情列表</li> </ul></SPAN>
# <UL>
# </UL>
class HanoiDatatemplateDetailQueryResponse(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()

        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">请求的返回信息,包含状态等</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">dict</SPAN>
        # </LI>
        # </UL>
        self.responseStatus = None

        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">请求的响应内容</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>        
        self.responseBody = None

        self.code = None

        self.msg = None

        self.sub_code = None

        self.sub_msg = None

        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">如果查询时需要分页，则返回分页的信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">PageResult</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # </UL>
        self.page_result = None
        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">返回的是Detail详情列表：<br/> paramsMap:创建数据模板时，填入PK的值<br/> attr:AttributeVO的json格式<br/> dataTemplateId:数据模板的唯一标识<br/> id:数据模板详情的唯一标识<br/> name:数据模板详情的名称<br/></SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.values = None
    
        self.__init(kargs)

    def isSuccess(self):
        return self.code == None and self.sub_code == None
    
    def _newInstance(self, name, value):
        types = self._getPropertyType(name)
        propertyType = types[0]
        isArray = types[1]
        if propertyType == bool:
            if isArray:
                if not value:
                    return []
                return [x for x in value[value.keys()[0]]]
            else:
                return value
        elif propertyType == datetime:
            format = "%Y-%m-%d %H:%M:%S"
            if isArray:
                if not value:
                    return []
                return [datetime.strptime(x, format) for x in value[value.keys()[0]]]
            else:
                return datetime.strptime(value, format)
        elif propertyType == str:
            if isArray:
                if not value:
                    return []
                return [x for x in value[value.keys()[0]]]
            else:
                #like taobao.simba.rpt.adgroupbase.get, response.rpt_adgroup_base_list is a json string,but will be decode into a list via python json lib 
                if not isinstance(value, basestring):
                    #the value should be a json string 
                    return _jsonEnode(value)
                return value
        else:
            if isArray:
                if not value:
                    return []
                return [propertyType(x) for x in value[value.keys()[0]]]
            else:
                return propertyType(value)
        
    def _getPropertyType(self, name):
        properties = {
            
            "page_result": "PageResult",
            
            "values": "String",
        }
        levels = {
            
            "page_result": "Object",
            
            "values": "Basic",
        }
        
        nameType = properties[name]
        pythonType = None
        if nameType == "Number":
            pythonType = int
        elif nameType == "String":
            pythonType = str
        elif nameType == 'Boolean':
            pythonType = bool
        elif nameType == "Date":
            pythonType = datetime
        elif nameType == 'Field List':
            pythonType == str
        elif nameType == 'Price':
            pythonType = float
        elif nameType == 'byte[]':
            pythonType = str
        else:
            pythonType = getattr(sys.modules["Domain.%s" % nameType], nameType)
        
        # 是单个元素还是一个对象
        level = levels[name]
        if "Array" in level:
            return (pythonType, True)
        else:
            return (pythonType, False)

    def __init(self, kargs):
        
        if kargs.has_key("page_result"):
            self.page_result = self._newInstance("page_result", kargs["page_result"])
        
        if kargs.has_key("values"):
            self.values = self._newInstance("values", kargs["values"])
        if kargs.has_key("code"):
            self.code = kargs["code"]
        if kargs.has_key("msg"):
            self.msg = kargs["msg"]
        if kargs.has_key("sub_code"):
            self.sub_code = kargs["sub_code"]
        if kargs.has_key("sub_msg"):
            self.sub_msg = kargs["sub_msg"]
