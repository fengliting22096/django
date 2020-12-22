from django.db import models
import time
import hashlib
# Create your models here.
class bind(models.Model):
    bind_id = models.CharField(max_length=256)
    data_time = models.DateTimeField(auto_created=True)


class cookie(models.Model):
    bind = models.ForeignKey(bind, on_delete=models.CASCADE,blank=True, null=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class token(models.Model):
    timestamp = str(int(time.time()))
    secret = '123456'
    code = timestamp + secret
    signature = hashlib.md5(code.encode(encoding='utf8')).hexdigest().upper()
    token = models.CharField(signature, max_length=256)
    def __str__(self):
        return self.signature

class timestamp(models.Model):
    def __str__(self):
        return str(int(time.time()))

class Product(models.Model):
 productname = models.CharField('产品名称',max_length=64) # 产品名称
 productdesc = models.CharField('产品描述',max_length=200) # 产品描述
 producter = models.CharField('产品负责人',max_length=200) # 产品负责人
 create_time = models.DateTimeField('创建时间',auto_now=True) # 创建时间，自动获取# 当前时间
 class Meta:
  verbose_name = '产品管理'
  verbose_name_plural = '产品管理'
 def __str__(self):
  return self.productname