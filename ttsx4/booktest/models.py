from django.db import models

# Create your models here.

#管理器是模型类的属性，用于将对象与数据表映射
class BookInfoManager(models.Manager):
    def get_queryset(self):
        # return super(BookInfoManager,self).get_queryset().filter(isDelete=False)
        return super().get_queryset().filter(isDelete=False)    #修改管理器返回的原始查询集：重写get_queryset()方法

    def create_book(self,btitle,bpub_date):    # _init _方法已经在基类models.Model中使用，在自定义模型中无法使用。方法二：在自定义管理器中添加一个方法。推荐使用此方法
        b=BookInfo()
        b.btitle=btitle
        b.bpub_date=bpub_date
        b.bread=0
        b.bcommet=0
        b.isDelete=False
        return b

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0)
    bcommet=models.IntegerField(null=False)
    isDelete=models.BooleanField(default=False)
    class Meta():
        db_table='bookinfo'    #元信息db_table：定义数据表名称，推荐使用小写字母，数据表的默认名称

    books1=models.Manager()    #为模型类指定管理器，且django不再为模型类生成名为objects的默认管理器。即models.Manager() 代替了objects()
    books2=BookInfoManager()   #修改了原始管理器

    @classmethod
    def create(cls,btitle,bpub_date):    # _init _方法已经在基类models.Model中使用，在自定义模型中无法使用。方法一：在模型类中增加一个类方法
        b=BookInfo()
        b.btitle=btitle
        b.bpub_date=bpub_date
        b.bread=0
        b.bcommet=0
        b.isDelete=False
        return b

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=1000)
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

class UserInfo(models.Model):
    uname=models.CharField(max_length=10)
    upwd=models.CharField(max_length=40)
    isDelete=models.BooleanField()

class AreaInfo(models.Model):
    title=models.CharField(max_length=20)
    parea=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)