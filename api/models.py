from django.db import models

# Create your models here.
class bookUser(models.Model):
    userName=models.CharField('用户名',max_length=100,default='no_name')
    password=models.CharField('密码',max_length=100,default='123456')
    bookrack=models.CharField('书架',max_length=200,default='')

    def __str__(self):
        # return '%d: %s' % (self.pk, self.userName)
        return self.userName

class bookSearch(models.Model):
    source_name=models.CharField('源名称',max_length=30)
    # search_requests=models.CharField('源搜索规则',max_length=200,default='url="",method="", data="", charset=""')
    requests_url=models.CharField('网址',max_length=100)
    requests_method=models.CharField('访问方式post或get',max_length=10,default='get')
    requests_data=models.CharField('访问数据',max_length=100)
    requests_charset=models.CharField('网站编码',max_length=10,default='utf-8')
    # search_filter=models.CharField('源搜索结果过滤',max_length=200,default='bookName="",bookAuthor="",bookNewestChapterName="",bookUpdateTime="",bookUrl=""')
    # search_key=models.CharField('源搜索键',max_length=200,default='')
    # search_value=models.CharField('源搜索值',max_length=200,default='')
    search_key=models.TextField('源搜索键')
    search_value=models.TextField('源搜索值')

    
    def __str__(self):
        return self.source_name

class bookIntroduce(models.Model):
    source_name=models.CharField('源名称',max_length=30)
    requests_method=models.CharField('访问方式post或get',max_length=10,default='get')
    requests_data=models.CharField('访问数据',max_length=100,default='{}')
    requests_charset=models.CharField('网站编码',max_length=10,default='utf-8')
    introduce_key=models.TextField('源小说介绍键')
    introduce_value=models.TextField('源小说介绍值')
    def __str__(self):
        return self.source_name

class bookList(models.Model):
    source_name=models.CharField('源名称',max_length=30)
    requests_url=models.CharField('域名',max_length=100)
    requests_method=models.CharField('访问方式post或get',max_length=10,default='get')
    requests_data=models.CharField('访问数据',max_length=100,default='{}')
    requests_charset=models.CharField('网站编码',max_length=10,default='utf-8')
    list_kv=models.TextField('源小说列表url和章节名')
    def __str__(self):
        return self.source_name


class bookContent(models.Model):
    source_name=models.CharField('源名称',max_length=30)
    requests_method=models.CharField('访问方式post或get',max_length=10,default='get')
    requests_data=models.CharField('访问数据',max_length=100,default='{}')
    requests_charset=models.CharField('网站编码',max_length=10,default='utf-8')
    content_kv=models.TextField('源小说章节内容')
    def __str__(self):
        return self.source_name


class bookSource(models.Model):
    name=models.CharField('小说源名字',max_length=40)
    host=models.CharField('源网站网址',max_length=50)
    sourceEncoding=models.CharField('编码方式',max_length=10,default='utf-8')
    # 搜索页面
    searchUrl=models.CharField('搜索链接',max_length=100)
    searchMethod=models.CharField('访问方式',max_length=10,default='get')
    searchPostParams=models.CharField('POST参数',max_length=100,default='{}')
    