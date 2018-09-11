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
        verbose_name = '保修信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
