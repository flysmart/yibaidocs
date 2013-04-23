# coding=utf-8
import datetime
from django.db import models
from django.utils.encoding import force_unicode
from tinymce.models import HTMLField

class ProjectCode(models.Model):
    code = models.CharField(max_length=20)
    desc = models.CharField(max_length=400, null=True, blank=True)
    available = models.BooleanField(default=True)
    create_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code.encode('utf-8')
    def __unicode__(self):
        return force_unicode(self.code)
    class Admin:
        pass


class Application(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    desc = models.CharField(max_length=400)
    create_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.encode('utf-8')
    def __unicode__(self):
        return force_unicode(self.name)
    class Admin:
        pass

list_snippet_template = '''<table width="100%" border="0" cellspacing="0" cellpadding="0" class="doc_list_table">
<colgroup><col class="tbF1"><col class="tbF2"><col></colgroup>
<tbody><tr>
<th colspan="3" scope="col"><span>登录接口</span>
</th></tr>
<tr>
<td rowspan="1" style="width:20%">验证登录</td>
<td style="width:35%"><a href="/doc/1/" title="login">auth.jsp</a></td>
<td style="width:45%">验证用户身份</td>
</tr>
</tbody>
</table>
'''

class APICategory(models.Model):
    app = models.ForeignKey(Application, unique=False)
    name = models.CharField(max_length=20)
    code  =  models.CharField(max_length=20)
    list_snippet = HTMLField(default=list_snippet_template)
    create_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.encode('utf-8')
    def __unicode__(self):
        return force_unicode('%s-%s' %(self.app.name,self.name))
    class Admin:
        pass

input_parameters_template = '''<table class="parameters">
   <tbody>
    <tr>
     <th width="30%">&nbsp;</th>
     <th width="10%">必选</th>
     <th width="15%">类型及范围</th>
     <th width="45%">说明</th>
    </tr>
    <tr>
     <td>username</td>
     <td>true</td>
     <td>string</td>
     <td>用户代码，相当于一般系统的登录用户名。</td>
    </tr>
    <tr>
     <td>password </td>
     <td>true</td>
     <td>string</td>
     <td>密码。</td>
    </tr>
    <tr>
     <td>captcha </td>
     <td>true</td>
     <td>string</td>
     <td>验证码。</td>
    </tr>
   </tbody>
  </table>
  '''

return_sample_data_template = '''{
    "status" : 1,
    "message" : "登录成功"
}
'''

return_data_desc_template = '''<table class="parameters">
   <tbody>
    <tr>
     <th width="30%">返回值字段</th>
     <th width="20%">字段类型</th>
     <th width="55%">字段说明</th>
    </tr>
    <tr>
     <td>status</td>
     <td>int</td>
     <td>1为成功，<br />0为失败，<br />-1为服务器异常，<br />-2为登录失效</td>
    </tr>
    <tr>
     <td>message</td>
     <td>string</td>
     <td>相关提示信息，如失败之后的异常等，有可能为空值。</td>
    </tr>
   </tbody>
  </table>
  '''

class APIDoc(models.Model):
    app = models.ForeignKey(Application, unique=False)
    category = models.ForeignKey(APICategory, unique=False)
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    data_type = models.CharField(max_length=20)
    calling_method = models.CharField(max_length=20)
    authentication_required = models.BooleanField(default=False)
    input_parameters = HTMLField(default=input_parameters_template)
    return_sample_data = HTMLField(default=return_sample_data_template)
    return_data_desc = HTMLField(default=return_data_desc_template)
    notes = models.CharField(max_length=800)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now_add=True)

    def save(self, *args,**kwargs):
        self.update_datetime = datetime.datetime.now()

        super(APIDoc,self).save(*args,**kwargs)

    def __str__(self):
        return self.name.encode('utf-8')
    def __unicode__(self):
        return force_unicode(self.name)
    class Admin:
        pass