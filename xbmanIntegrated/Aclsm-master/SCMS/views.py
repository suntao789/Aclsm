#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Create your views here.
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect,StreamingHttpResponse
from django.contrib import auth
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from Integrated.plugins.Decorators import Perm_verification
import json
import models
import code
import froms
import os,tarfile

@login_required
@Perm_verification(perm='ansible')
def index(request):
    containerd,mainnn,business = code.index(request)
    return render(request, 'scms/index.html',{"containerd": containerd,"mainnn": mainnn,"business": business},
                      context_instance=RequestContext(request))


@login_required
@Perm_verification(perm='ansible')
def help(request):
    return render(request, 'scms/help.html',context_instance=RequestContext(request))

@login_required
@Perm_verification(perm='ansible')
def adddevice(request):
    if request.method == "POST":
        data = code.pcmanage_post(request)
        return HttpResponse(json.dumps(data))

@login_required
@Perm_verification(perm='ansible')
def pcmanager(request):
    if request.method == 'GET':
        contacts,group_list = code.pcmamage_get(request)
        return render(request,'scms/PcManagement.html', {"topics": contacts,'group_list':group_list},
                      context_instance=RequestContext(request))

@login_required
@Perm_verification(perm='ansible')
def deldevice(request):
    if code.del_device(request):
        return HttpResponse(json.dumps('true'))

@login_required
@Perm_verification(perm='ansible')
def groupmodify(request):
    if request.method == "POST":
        if code.group_post(request):
            return HttpResponseRedirect("/scms/groupmodify/")
        else:
            contacts = code.group_get(request)
            return render(request, 'scms/group-conf.html',
                          {"topics": contacts,  'zhuangtai': True},
                          context_instance=RequestContext(request))
    elif request.method == 'GET':
        contacts = code.group_get(request)
        return render(request, 'scms/group-conf.html', {"topics": contacts},
                      context_instance=RequestContext(request))

@login_required
@Perm_verification(perm='ansible')
def delgroup(request):
    if code.del_group(request):
        return HttpResponse(json.dumps('true'))

@login_required
@Perm_verification(perm='ansible')
def editgroup(request):
    if code.edit_group(request):
        return HttpResponseRedirect("/scms/groupmodify/")

@login_required
@Perm_verification(perm='ansible')
def confile(request):
    if request.method == "POST":
        if code.config_post(request):
            return HttpResponseRedirect("/scms/confile/")
        else:
            contacts,profile_list,nginx_list,tomcat_list = code.config_get(request)
            return render(request, 'scms/confile.html',
                          {"contacts": contacts,"profile_list":profile_list,"nginx_list":nginx_list,"tomcat_list":tomcat_list,'zhuangtai': True},
                          context_instance=RequestContext(request))
    elif request.method == 'GET':
        contacts,profile_list,nginx_list,tomcat_list = code.config_get(request)
        return render(request, 'scms/confile.html', {"contacts": contacts,"profile_list":profile_list,"nginx_list":nginx_list,"tomcat_list":tomcat_list},
                      context_instance=RequestContext(request))
    return render(request, 'scms/confile.html')

@login_required
@Perm_verification(perm='ansible')
def editconf(request):
    if request.method == "POST":
        if code.config_edit(request):
            return HttpResponseRedirect("/scms/confile/")

@login_required
@Perm_verification(perm='ansible')
def delconf(request):
    if code.del_config(request):
        return HttpResponse(json.dumps('true'))



@login_required
@Perm_verification(perm='ansible')
def page(request):
    if request.method == "POST":
            if code.pageadd(request):
                return HttpResponseRedirect("/scms/page/")
            else:
                pass
    elif request.method == 'GET':
        contacts = code.pageget(request)
        return render_to_response('scms/pageapp.html', {'uf': froms.headImg(),'contacts':contacts},
                                  context_instance=RequestContext(request))

def delpage(request):
    if code.del_page(request):
        return HttpResponse(json.dumps('true'))

@login_required
@Perm_verification(perm='ansible')
def nginxpush(request):
    if request.method == "POST":
        if code.nginxpush_post(request):
            contacts, config, group = code.nginxpush_get(request)
            return render_to_response('scms/flot.html', {'contacts': contacts, 'config': config, 'group': group,'zhuangtai':True},
                                      context_instance=RequestContext(request))
    elif request.method == 'GET':
        contacts,config,group = code.nginxpush_get(request)
        return render_to_response('scms/flot.html', {'contacts':contacts,'config':config,'group':group,'zhuangtai':False},
                                  context_instance=RequestContext(request))

@login_required
@Perm_verification(perm='ansible')
def tomcatpush(request):
    if request.method == "POST":
        if code.tomcatpush_post(request):
            contacts, config, group = code.tomcatpush_get(request)
            return render_to_response('scms/morros.html',
                                      {'contacts': contacts, 'config': config, 'group': group, 'zhuangtai': True},
                                      context_instance=RequestContext(request))
    elif request.method == 'GET':
        contacts, config, group = code.tomcatpush_get(request)
        return render_to_response('scms/morros.html',{'contacts':contacts,'config':config,'group':group},
                                  context_instance=RequestContext(request))

@login_required
@Perm_verification(perm='ansible')
def nginxinstall(request):
    if request.method == "POST":
        if code.ninstall_post(request):
            contacts, config, group = code.ninstall_get(request)
            return render_to_response('scms/nginxinstall.html',
                                      {'contacts': contacts, 'config': config, 'group': group, 'zhuangtai': True},
                                      context_instance=RequestContext(request))
    elif request.method == 'GET':
        contacts, config, group = code.ninstall_get(request)
        return render_to_response('scms/nginxinstall.html', {'contacts':contacts, 'config':config, 'group':group},
                                  context_instance=RequestContext(request))

@login_required
@Perm_verification(perm='ansible')
def tomcatinstall(request):
    if request.method == "POST":
        if code.tinstall_post(request):
            contacts, config, group = code.tinstall_get(request)
            return render_to_response('scms/tomcatinstall.html',
                                      {'contacts': contacts, 'config': config, 'group': group, 'zhuangtai': True},
                                      context_instance=RequestContext(request))
    elif request.method == 'GET':
        contacts, config, group = code.tinstall_get(request)
        return render_to_response('scms/tomcatinstall.html', {'contacts':contacts, 'config':config, 'group':group},
                                  context_instance=RequestContext(request))

@login_required
@Perm_verification(perm='ansible')
def generate(request):
    return HttpResponse(code.code_generate(request))

@login_required
@Perm_verification(perm='ansible')
def tasks_tables(request):
    contacts = code.tasks_get(request)
    return render_to_response('scms/tasks.html',{"topics": contacts},
                              context_instance=RequestContext(request))

@login_required
@Perm_verification(perm='ansible')
def cmdrun(request):
    if request.method == "POST":
        data = code.cmdrun(request)
        return HttpResponse(json.dumps(data))
    elif request.method == 'GET':
        #使用tomcatinstall的方法获取机器和组
        contacts, config, group = code.tinstall_get(request)
        return render_to_response('scms/forms.html',{'contacts':contacts, 'group':group},
                                  context_instance=RequestContext(request))

@login_required
@Perm_verification(perm='ansible')
def playbook(request):
    contacts = models.Playbook.objects.all()
    return render_to_response('scms/playbook.html',{'uf': froms.headImg(),'contacts':contacts},
                              context_instance=RequestContext(request))
@login_required
@Perm_verification(perm='ansible')
def playbook_upload(request):
    if request.method == "POST":
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        try:
            os.mkdir(os.path.join(project_dir, 'upload'))
        except OSError,e:
            pass
        myFile = request.FILES.get("myfile", None)
        if os.path.exists(os.path.join(project_dir, 'upload', myFile.name)):
            return HttpResponse(json.dumps((False,'文件已存在！')))
        destination = open(os.path.join(project_dir ,'upload', myFile.name), 'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        os.mkdir(os.path.join(project_dir ,'upload', myFile.name.split('.')[0]))
        tar = tarfile.open(os.path.join(project_dir ,'upload', myFile.name))
        tar.extractall(os.path.join(project_dir ,'upload', myFile.name.split('.')[0]))
        tar.close()
        os.system('chmod -x %s'%os.path.join(project_dir ,'upload', myFile.name.split('.')[0],'inventory'))
        models.Playbook.objects.create(name=myFile,description=request.POST.get('description')
                                       ,basedir=os.path.join(project_dir,'upload',myFile.name))
        return HttpResponse(json.dumps((True,'上传成功！')))

@login_required
@Perm_verification(perm='ansible')
def delplaybook(request):
    if code.del_playbook(request):
        return HttpResponse(json.dumps('true'))

@login_required
@Perm_verification(perm='ansible')
def down_playbook(request):
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    filename = models.Playbook.objects.filter(id=request.GET.get('id'))
    response = StreamingHttpResponse(file_iterator(filename[0].basedir))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename[0].name)
    return response

@login_required
@Perm_verification(perm='ansible')
def roles(request):
    if request.method == "POST":
        data = code.roles_task(request)
        return HttpResponse(json.dumps(data))
    elif request.method == 'GET':
        contacts = code.roles()
        return render_to_response('scms/roles.html',{'contacts':contacts},
                                  context_instance=RequestContext(request))
#文件推送功能
# @login_required
# def filepush(request):
#     if request.method == 'GET':
#         contacts, config, group = code.tinstall_get(request)
#         return render_to_response('filepush.html', {'contacts': contacts, 'group': group},
#                                   context_instance=RequestContext(request))