# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# from django.utils.six import


# Create your models here.

class Category(models.Model):
    """
    Django 要求模型必须继承 models.Model 类。
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    Django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 标题
    title = models.CharField(max_length=70)
    # 主体
    body = models.TextField()
    # 创建时间
    created_time = models.DateTimeField()
    # 修改时间
    modified_time = models.DateTimeField()
    # 摘录
    excerpt = models.CharField(max_length=200, blank=True)
    # 分类
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 标签
    tags = models.ManyToManyField(Tag, blank=True)
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'title': self.title})

    class Meta:
        ordering = ['-created_time']