# coding=utf-8
import urllib2
import time
import pycurl
import StringIO

from django.conf import settings

headers = {
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
          }

def get_url_data(url):
    req = urllib2.Request(url = url, headers = headers)
    return_data = urllib2.urlopen(req).read()
    return return_data

def post_url_data(url, data):

    crl = pycurl.Curl()
    crl.setopt(pycurl.VERBOSE,1)
    crl.setopt(pycurl.FOLLOWLOCATION, 1)
    crl.setopt(pycurl.MAXREDIRS, 5)
    #crl.setopt(pycurl.AUTOREFERER,1)
     
    crl.setopt(pycurl.CONNECTTIMEOUT, 60)
    crl.setopt(pycurl.TIMEOUT, 300)
    #crl.setopt(pycurl.PROXY,proxy)
    crl.setopt(pycurl.HTTPPROXYTUNNEL,1)
    #crl.setopt(pycurl.NOSIGNAL, 1)
    crl.fp = StringIO.StringIO()
    #crl.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6")
    crl.setopt(pycurl.USERAGENT, "yibai docs.")
     
    # Option -d/--data <data>   HTTP POST data
    crl.setopt(crl.POSTFIELDS,  data) 
    crl.setopt(pycurl.URL, url)
    
    crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
    
    crl.perform()
    
    return_value = crl.fp.getvalue()
     
    return return_value
    