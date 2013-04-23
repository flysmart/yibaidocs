# coding=utf-8
import datetime
from django.db import models
from django.utils.encoding import force_unicode
from django.contrib.auth.models import User
from tinymce.models import HTMLField

from doc.models import Application

schedule_table = '''<table class="schedule_tbl">
    <tbody>
    <tr>
        <th scope="row">奥特曼</th>
        <td>
            <h3>SSO设计和环境搭建</h3>
            <div class="s_list">1、用户表结构建立。 <img src="/static/images/ok.png" /></div>
            <div class="s_list">2、相关Django views, templates编写。</div>
            <div class="s_list">3、部分代码重构。</div>
            <div class="s_list">4、钢贸环境没弄好之前，我们自己的开发环境的搭建。</div>
            <div class="s_notes">
             备注：<br />
              a) 备注1。<br />
              b) 备注2。<br />
              c) css文件冲突解决方案，在新的css文件里都加上前缀，如果有全局定义的样式，改为自定义class覆盖。
            </div>
        </td>
    </tr>
    <tr class="odd">
        <th scope="row">金钢</th>
        <td>
            <h3>表结构设计，分表研究</h3>
            <div class="s_list">1、资源表结构横向切分设计，根据不同的供应商分不同的资源库。</div>
            <div class="s_list">2、资源表纵向分切，</div>
            <div class="sub_s_list">2.1、可供资源再按品牌在Oracle中分区。</div>
            <div class="sub_s_list">2.2、已经采购的资源放入历史资源池。</div>
            <div class="s_list">3、读取方式确定。</div>
        </td>
    </tr>
    </tbody>
    </table>'''

class WorkingDay(models.Model):
    app = models.ForeignKey(Application, unique=False)
    year = models.IntegerField(default=datetime.datetime.now().year)
    month = models.IntegerField(default=datetime.datetime.now().month)
    day = models.IntegerField(default=datetime.datetime.now().day)
    desc = models.CharField(max_length=400, blank=True,null=True)
    schedule_table = HTMLField(default=schedule_table)
    create_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc.encode('utf-8')
    def __unicode__(self):
        return force_unicode(self.desc)
    class Meta:
        ordering = ['-year', '-month', '-day']
    class Admin:
        pass

class Feedback(models.Model):
    user = models.ForeignKey(User, unique=False)
    nick_name = models.CharField(max_length=40)
    working_day = models.ForeignKey(WorkingDay, unique=False)
    feedback = HTMLField()
    create_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc.encode('utf-8')
    def __unicode__(self):
        return force_unicode(self.feedback)
    class Meta:
        ordering = ['-create_datetime',]
    class Admin:
        pass
