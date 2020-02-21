from django.db import models

# Create your models here.

class AreaInfo(models.Model):
    title=models.CharField(max_length=20)
    parea=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

#富文本测试用
from tinymce.models import HTMLField
class TextTest(models.Model):
    hcontent=HTMLField()