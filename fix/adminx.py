# coding=utf-8
import xadmin
from .models import *


class FixAdmin(object):
    list_display = ['name', 'college', 'place', 'goods', 'detail']
    search_display = ['name', 'college', 'place', 'goods', 'detail']
    list_filter = ['name', 'college', 'place', 'goods', 'detail']


xadmin.site.register(Fix, FixAdmin)
