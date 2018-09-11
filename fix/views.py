from django.shortcuts import HttpResponse, render
from django.views.generic.base import View
from .models import *
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
        res = Fix(name=name, college=college, place=place, goods=goods, file1=file1, detail=detail)
        res.save()
        return HttpResponse('<script>alert("提交成功！"); window.location.href="/fix/";</script>')
