from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
"""
class Category(models.Model):  # 文章种类
    title = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    # def get_absolute_url(self):
    #    return reverse('shop:product_list_by_category',
    #                  args=[self.slug])
    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

"""

class Artical(models.Model):
    # 多对一
    #category = models.ForeignKey(Category, related_name='title')
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField('标题',max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts')
    body = models.TextField('内容')
    image = models.ImageField(upload_to='image/%Y/%m/%d',
                              blank=True)
    #是否编辑推荐
    tuijian = models.BooleanField('是否推荐')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

