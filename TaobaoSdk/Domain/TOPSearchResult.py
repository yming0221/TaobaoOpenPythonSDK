#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 搜索返回的结果类
# @author wuliang@maimiaotech.com
# @date 2013-09-22 16:52:26
# @version: 0.0.0

from copy import deepcopy
from datetime import datetime
import os
import sys
import time
import types

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

if __getCurrentPath() not in sys.path:
    sys.path.insert(0, __getCurrentPath())


        
from TOPPaginator import TOPPaginator

        
from VideoItem import VideoItem


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">搜索返回的结果类</SPAN>
class TOPSearchResult(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()

        self.__kargs = deepcopy(kargs)
        
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">分页信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">TOPPaginator</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # </UL>
        self.paginator = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">视频列表</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">VideoItem</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # </UL>
        self.video_items = None
        
        self.__init(kargs)

    def toDict(self, **kargs):
        result = deepcopy(self.__kargs)
        for key, value in self.__dict__.iteritems():
            if key.endswith("__kargs"):
                continue
            if value == None:
                if kargs.has_key("includeNone") and kargs["includeNone"]:
                    result[key] = value
                else:
                    continue
            else:
                result[key] = value
        return result
        
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
                if not isinstance(value, basestring):
                    return _jsonEnode(value)
                else:
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
            
            "paginator": "TOPPaginator",
            
            "video_items": "VideoItem",
        }
        levels = {
            
            "paginator": "Object",
            
            "video_items": "Object Array",

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
            pythonType = getattr(
                sys.modules[os.path.basename(
                os.path.dirname(os.path.realpath(__file__))) + "." + nameType], 
                nameType)

        level = levels[name]
        if "Array" in level:
            return (pythonType, True)
        else:
            return (pythonType, False)
        
    def __init(self, kargs):
        
        if kargs.has_key("paginator"):
            self.paginator = self._newInstance("paginator", kargs["paginator"])
        
        if kargs.has_key("video_items"):
            self.video_items = self._newInstance("video_items", kargs["video_items"])
