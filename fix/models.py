from django.db import models

# Create your models here.


class Fix(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=50)
    college = models.CharField(verbose_name='学院', max_length=50)
    place = models.CharField(verbose_name='故障地点', max_length=100)
    goods = models.CharField(verbose_name='故障物品', max_length=100)
    file1 = models.ImageField(upload_to='fix', max_length=100, verbose_name='照片')
    detail = models.CharField(verbose_name='描述信息', max_length=500)

    class Meta:
        verbose_name = '报修信息'
        verbose_name_plural = verbose_name
        db_table = 'fix'
        app_label = "fix"

    def __str__(self):
        return self.name


class User(models.Model):
    stuid = models.CharField(verbose_name='用户id', max_length=255)
    password = models.CharField(max_length=255)
    realname = models.CharField(max_length=255)
    nikename = models.CharField(max_length=255)
    face = models.TextField()
    classid = models.CharField(max_length=255)
    is_teacher = models.IntegerField()
    phone = models.CharField(max_length=255)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        db_table = 'user'
        app_label = "fix"

    def __str__(self):
        return self.stuid


class Activity(models.Model):
    name = models.CharField(verbose_name='活动名称', max_length=100)
    types = models.CharField(verbose_name='活动类型', max_length=100)
    creator_id = models.CharField(verbose_name='创建人id', max_length=100)
    person = models.IntegerField(verbose_name='活动人数')
    sold_ticket = models.IntegerField(verbose_name='已售票数')
    times = models.DateField(verbose_name='活动时间')
    place = models.CharField(verbose_name='活动地点', max_length=100)
    detail = models.CharField(verbose_name='描述', max_length=500)
    sign_count = models.IntegerField(verbose_name='已签到人数', default=0)

    class Meta:
        verbose_name = '活动信息'
        verbose_name_plural = verbose_name
        db_table = 'activity'
        app_label = "fix"

    def __str__(self):
        return self.name


class Ticket(models.Model):
    activity_id = models.IntegerField(verbose_name='活动id')
    person_id = models.IntegerField(verbose_name='领取人id')
    is_sign = models.IntegerField(verbose_name='是否签到', default=0)
    image = models.CharField(verbose_name='二维码信息', max_length=200)

    class Meta:
        verbose_name = '票务信息'
        verbose_name_plural = verbose_name
        db_table = 'ticket'
        app_label = "fix"

    def __str__(self):
        return str(self.activity_id)



