#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2023 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import itertools
import sys

PY2 = sys.version_info.major == 2


if PY2:
    try:
        import _winreg as winreg
    except ImportError:
        winreg = None

    MAXINT = sys.maxint
    MININT = -sys.maxint - 1

    MAXFLOAT = sys.float_info.max
    MINFLOAT = sys.float_info.min

    string_types = str, unicode
    integer_types = int, long

    filter = itertools.ifilter
    map = itertools.imap
    range = xrange
    zip = itertools.izip
    long = long

    cmp = cmp

    bytes = bytes
    bstr = bytes

    from io import StringIO

    from urllib2 import urlopen, ProxyHandler, build_opener, install_opener
    from urllib import quote as urlquote

    def iterkeys(d): return d.iterkeys()

    def itervalues(d): return d.itervalues()

    def iteritems(d): return d.iteritems()

    def keys(d): return d.keys()

    def values(d): return d.values()

    def items(d): return d.items()

    import Queue as queue

else:
    try:
        import winreg
    except ImportError:
        winreg = None

    MAXINT = sys.maxsize
    MININT = -sys.maxsize - 1

    MAXFLOAT = sys.float_info.max
    MINFLOAT = sys.float_info.min

    string_types = str,
    integer_types = int,

    filter = filter
    map = map
    range = range
    zip = zip
    long = int

    def cmp(a, b): return (a > b) - (a < b)

    def bytes(x): return x.encode('utf-8')

    def bstr(x): return str(x)

    from io import StringIO

    from urllib.request import (urlopen, ProxyHandler, build_opener,
                                install_opener)
    from urllib.parse import quote as urlquote

    def iterkeys(d): return iter(d.keys())

    def itervalues(d): return iter(d.values())

    def iteritems(d): return iter(d.items())

    def keys(d): return list(d.keys())

    def values(d): return list(d.values())

    def items(d): return list(d.items())

    import queue as queue


# This is from Armin Ronacher from Flash simplified later by six
# 为什么用这个方法，而不是直接继承类
# 答：
# 调用这个方法时,并不会触发metaclass类的__new__方法, 只有子类__new__时，调用
# 1. 所以，这个方法方便延迟调用，如果用 type(name,bases,args),会立即调用
# 2. 因为延迟调用，系统调用时会带上继承者的属性信息[重要]
def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class metaclass(meta):

        #这个方法，子类加载时会调用
        def __new__(cls, name, this_bases, d):
            #返回一个类
            return meta(name, bases, d)
        
  
    #__new__ 是一个静态方法

    # str('temporary_class2222') 指定类名。这将成为类的属性。__name__
    # type.__new__ 第一个参数必须是 type 的子类， 因为要用 type 类的 __new__方法
    # 第2个参数是类名
    # type.__new__ 和 type(name,parent,attr)
    # 区别是， type.__new__ 指定一个type类的__new__方法来调用，生成新的class
    return type.__new__(metaclass, str('temporary_class'), (), {})
