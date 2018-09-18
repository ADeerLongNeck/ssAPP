# coding=utf-8
import xadmin
from .models import *


class FixAdmin(object):
    list_display = ['name', 'college', 'place', 'goods', 'detail']
    search_display = ['name', 'college', 'place', 'goods', 'detail']
    list_filter = ['name', 'college', 'place', 'goods', 'detail']


class ActivityAdmin(object):
    list_display = ['id', 'name', 'types', 'creator_id', 'person', 'place', 'detail', 'sign_count']
    search_display = ['name', 'types', 'creator_id', 'person', 'place', 'detail', 'sign_count']
    list_filter = ['name', 'types', 'creator_id', 'person', 'place', 'detail', 'sign_count']


class TicketAdmin(object):
    list_display = ['activity_id', 'person_id', 'is_sign']
    search_display = ['activity_id', 'person_id', 'is_sign']
    list_filter = ['activity_id', 'person_id', 'is_sign']


xadmin.site.register(Fix, FixAdmin)
xadmin.site.register(Activity, ActivityAdmin)
xadmin.site.register(Ticket, TicketAdmin)

