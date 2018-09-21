"""ssAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static
import xadmin
from fix.views import *

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('fix/', FixView.as_view(), name='fix'),
    path('activity/', ActivityView.as_view(), name='activity'),
    path('activity_mine/', ActivityMineView.as_view(), name='activity_mine'),
    path('activity_list/', ActivityListView.as_view(), name='activity_list'),
    path('activity_ticket/', ActivityTicketView.as_view(), name='activity_ticket'),
    path('get_ticket/', GetTicketView.as_view(), name='get_ticket'),  # 领票
    path('check_ticket/', CheckTicketView.as_view(), name='check_ticket'),  # 验票
    path('chart/', ChartView.as_view()),
]

urlpatterns += static('upload/', document_root=settings.MEDIA_ROOT)
