from django.shortcuts import HttpResponse, render
from django.views.generic.base import View
from .models import *
import json


# Create your views here.


class FixView(View):
    def get(self, request):
        return render(request, 'fixform.html')

    def post(self, request):
        name = request.POST.get('name', '')
        college = request.POST.get('college', '')
        place = request.POST.get('place', '')
        goods = request.POST.get('goods', '')
        file1 = request.FILES.get('file1', '')
        detail = request.POST.get('detail', '')
        types = request.POST.get('types', '')
        res = Fix(name=name, college=college, place=place, goods=goods, file1=file1, detail=detail, types=types)
        res.save()
        return HttpResponse('<script>alert("提交成功！"); window.location.href="/fix/";</script>')


class ActivityView(View):
    def get(self, request):
        user_id = request.GET.get('user_id', None)
        if not user_id:
            return HttpResponse('请登陆后再试')
        return render(request, 'active.html', {'user_id': user_id})

    def post(self, request):
        creator_id = request.POST.get('user_id', '')
        name = request.POST.get('name', '')
        types = request.POST.get('type', '')
        place = request.POST.get('place', '')
        person = request.POST.get('person', '')
        detail = request.POST.get('detail', '')
        times = request.POST.get('times', '')
        res = Activity(name=name, person=person, types=types, place=place, detail=detail, sold_ticket=0, times=times,
                       creator_id=creator_id)
        res.save()
        return HttpResponse(
            '<script>alert("提交成功！"); window.location.href="/activity_list/?user_id=%s"</script>' % creator_id)


# 我的活动
class ActivityMineView(View):
    def get(self, request):
        user_id = request.GET.get('user_id', None)
        if not user_id:
            return HttpResponse('请登陆再试')
        res = []
        res_temp = Ticket.objects.filter(person_id=user_id)
        for i in res_temp:
            res2 = Activity.objects.filter(id=i.activity_id)
            if len(res2) > 0:
                res.append(res2[0])
        for i in res:
            i.exist = i.person - i.sold_ticket
            res2 = Ticket.objects.filter(person_id=user_id, activity_id=i.id)
            if len(res2) > 0:
                i.is_select = 1
            else:
                i.is_select = 0
        return render(request, 'active_mine.html', {'res': res, 'user_id': user_id})


# 活动列表
class ActivityListView(View):
    def get(self, request):
        user_id = request.GET.get('user_id', None)
        if not user_id:
            return HttpResponse('请登陆再试')
        res = Activity.objects.all()
        for i in res:
            i.exist = i.person - i.sold_ticket
            res2 = Ticket.objects.filter(person_id=int(user_id), activity_id=i.id)
            if len(res2) > 0:
                i.is_select = 1
            else:
                i.is_select = 0
        return render(request, 'active_list.html', {'res': res, 'user_id': user_id})


# 我领取的票
class ActivityTicketView(View):
    def get(self, request):
        user_id = request.GET.get('user_id', None)
        if not user_id:
            return HttpResponse('请登陆再试')
        res = []
        res_temp = Ticket.objects.filter(person_id=user_id)
        for i in res_temp:
            res2 = Activity.objects.filter(id=i.activity_id)
            if len(res2) > 0:
                res2[0].is_sign = i.is_sign
                res2[0].image = i.image
                res.append(res2[0])
        return render(request, 'active_ticket.html', {'res': res, 'user_id': user_id})


# 领票api
class GetTicketView(View):
    def get(self, request):
        user_id = request.GET.get('user_id', None)
        id = request.GET.get('id', None)
        try:
            user_id = user_id.split('=')[1]
            activity = Activity.objects.get(id=id)
            if activity.sold_ticket >= activity.person:
                return HttpResponse(
                    '<script>alert("来晚了，票已经被抢完了"); window.location.href="/activity_list/?user_id=%s"</script>' % user_id)
            check_res = Ticket.objects.filter(person_id=user_id, activity_id=id)
            if len(check_res) > 0:
                return HttpResponse(
                    '<script>alert("您已经领过该票了"); window.location.href="/activity_list/?user_id=%s"</script>' % user_id)
            res = Ticket(person_id=user_id, activity_id=id, is_sign=0)
            res.save()
            res = Ticket.objects.filter(person_id=user_id, activity_id=id)[0]
            import qrcode
            img = qrcode.make(res.id)
            path = "upload/qr/" + str(res.id) + '_' + user_id + '.png'
            img.save(path)
            res.image = "qr/" + str(res.id) + '_' + user_id + '.png'
            res.save()
            new_sold_ticket = activity.sold_ticket + 1
            activity.sold_ticket = new_sold_ticket
            activity.save()
            return HttpResponse(
                '<script>alert("恭喜你领票成功"); window.location.href="/activity_list/?user_id=%s"</script>' % user_id)
        except Exception as e:
            print(e)
            return HttpResponse(HttpResponse('<script>alert("出错了，请重试"+e);</script>'))


# 验票api
class CheckTicketView(View):
    def post(self, request):
        ticket_id = request.POST.get('ticket_id', None)
        creator_id = request.POST.get('creator_id', None)
        if not ticket_id or not creator_id:
            return HttpResponse(0)
        ticket = Ticket.objects.get(id=ticket_id)
        activity_id = ticket.activity_id
        if Activity.objects.get(id=activity_id).creator_id == creator_id:
            if ticket.is_sign == 0:
                ticket.is_sign = 1
                ticket.save()
                return HttpResponse(1)
            else:
                return HttpResponse(2)
        else:
            return HttpResponse(0)


# chart
class ChartView(View):
    def get(self, request):
        xianluguzhang = Fix.objects.filter(types='线路故障').count()
        zuoyisunhuai = Fix.objects.filter(types='座椅损坏').count()
        shebeiguzhang = Fix.objects.filter(types='设备故障').count()
        menchuangsunhuai = Fix.objects.filter(types='门窗损坏').count()
        dimiansunhuai = Fix.objects.filter(types='地面损坏').count()
        gonggongsheshisunhuai = Fix.objects.filter(types='公共设施损坏').count()

        return render(request, 'chart.html',
                      {'xianluguzhang': xianluguzhang, 'zuoyisunhuai': zuoyisunhuai, 'shebeiguzhang': shebeiguzhang,
                       'menchuangsunhuai': menchuangsunhuai, 'dimiansunhuai': dimiansunhuai, 'gonggongsheshisunhuai': gonggongsheshisunhuai})


# Index
class IndexView(View):
    def get(self, request):
        res = Index.objects.all()
        return render(request, 'index.html', {'res': res})


# content
class ContentView(View):
    def get(self, request):
        id = request.GET.get('id')
        res = Index.objects.get(id=id)
        return render(request, 'content.html', {'res': res})
