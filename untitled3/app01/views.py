# coding=utf-8
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from app01 import models
from django.http import FileResponse
import random
from PIL import Image, ImageDraw,ImageFont
import os
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import time
from dwebsocket.decorators import accept_websocket #引入dwbsocket的accept_websocket装饰器
import json
import uuid

def login(request):#登录



    if request.method=='POST':

        user = request.POST.get('user')

        pwd = request.POST.get('pwd')
        value = request.POST.get("codevalue")
        value2 = request.session.get("verCode")



        #if user== 'qq' and pwd== '123':




            #return render(request,'logo2.html')


        if models.User.objects.filter(username=user, password=pwd) :
        # if models.User.objects.filter(username=user, password=pwd):
            if  value.lower()==value2.lower():




                response = redirect('/son/')
                request.session['is_login'] = True
                # response = redirect('/abc/')

                # 创建cookie
                request.session["user"] =user
                request.session.set_expiry(0)

                return response
            else:
                return HttpResponse('您输入的验证码有误，请重新输入')

            # return redirect('/back/')
            # return render(request,'file1.html')
            # return render(request,'login1.html')
            # return redirect('https://www.baidu.com/')

            # return HttpResponse('登录成功')

            # return redirect('/index/')

        else:
            return HttpResponse('您输入的密码有误，请重新输入')
    return render(request, 'log3.html')

def reglink(request):
    if request.method=='POST':

        user = request.POST.get('user')

        pwd = request.POST.get('pwd')
        value = request.POST.get("codevalue")
        value2 = request.session.get("verCode")

        if models.User.objects.filter(username=user):
            return HttpResponse('用户名已存在')
            #return render(request, 'logo3.html', {'error':'用户名已经存在，请更换用户名'})
        if len(user)<5:
            return HttpResponse('用户名必须大于五位数')
        if len(pwd) <5:
            return HttpResponse('密码必须大于五位数')
        if models.User.objects.create(username=user, password=pwd) and value.lower()==value2.lower():

            return HttpResponse('注册成功')

    return render(request, 'logo3.html')
def yanzheng(request):
    image = Image.new("RGB", (200, 70),createcolor())
    imageDraw = ImageDraw.Draw(image, "RGB")
    imageFont = ImageFont.truetype("AGENCYR.TTF", size=50)
    # imageDraw.text((5,10),"i love you!",fill=createcolor(),font=imageFont)
    import io
    charsource = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    sum = ""
    for i in range(4):
        ch = random.choice(charsource)
        imageDraw.text((15 + i * 50, 10), ch, fill=createcolor(), font=imageFont)
        sum += ch
    # 通过session记录这个验证码并且设置过期时间为60秒
    request.session["verCode"] = sum
    request.session.set_expiry(60)
    # 画麻子
    for i in range(2000):
        x = random.randint(0, 200)
        y = random.randint(0, 70)
        imageDraw.point((x, y), fill=createcolor())

    # 创建一个字节流
    byteIO = io.BytesIO()
    # 把图片放在字节流里面去
    image.save(byteIO, "png")
    return HttpResponse(byteIO.getvalue(), "image/png")


def createcolor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return (red, green, blue)
def son(request):

    is_login = request.session.get("user")
    if not is_login:
        return redirect('/login/')
    else:


        user=request.session.get('user',default='')
        request.session["user"] = user
        sq=models.User.objects.get(username=user)
        a=models.User.objects.get(username=user).id
        sa=models.text.objects.filter(pd_id=a)
        buy=models.buy.objects.filter(pd_id=a)
        sell=models.sell.objects.filter(pd_id=a)
        p = Paginator(sa, 10)
        p1 =Paginator(buy, 10)
        p2=Paginator(sell, 10)
        #
        # new = request.GET.get('page')
        # new1 = request.GET.get('page1')
        # new2 = request.GET.get('page2')
        # try:
        #     page = p.page(new)
        #     page1=p1.page(new1)
        #     page2=p2.page(new2)
        # except PageNotAnInteger:
        #     page = p.page(1)
        #     page1 = p1.page(1)
        #     page2 = p2.page(1)
        # except EmptyPage:
        #     page = p.page(p.num_pages)
        #     page1 = p1.page(p1.num_pages)
        #     page2 = p2.page(p2.num_pages)








        # return render(request, 'son.html', {'user': sq,'wordtoo':page,'p':p,'buy':page1,'sell':page2,'p1':p1,'p2':p2})
        return render(request, 'son.html',
                      {'user': sq,'wordtoo':sa,'buy':buy,'sell':sell,'p':p,'p1':p1,'p2':p2})

def logout(request):

    # if not request.session.get('is_login', None):
    #
    #     return redirect("/login/")
    request.session.flush()

    return redirect("/login/")






def me(request):
    user = request.session.get('user',default='')
    request.session["user"] = user
    a=models.User.objects.get(username=user)
    # info='请完善各项资料才能购买(包括头像)'



    return render(request,'帐号设置.html',{'a':a})
def xiugai(request):


    user = request.session.get('user',default='')
    request.session["user"] = user
    a = models.User.objects.get(username=user)






    if request.method=='POST':


        name=request.POST.get('wo')
        jianjie=request.POST.get('jianjie')
        files=request.FILES.get('f1')
        youxiang=request.POST.get('youxiang')
        qq=request.POST.get('qq')
        try:

            qg = open('G:/英雄时刻/untitled3/static/' + files.name, 'wb+')
            qg.write(files.read())


            models.User.objects.filter(username=user).update(name=name,jianjie=jianjie,img=files,youxiang=youxiang,qq=qq)
            info='修改成功'
        except:
            models.User.objects.filter(username=user).update(name=name, jianjie=jianjie,  youxiang=youxiang,
                                                             qq=qq)
            info = '修改成功'

        return render(request,'修改资料.html',{'a': a,'info':info})
        # return redirect('/abc/')







    return render(request,'修改资料.html',{'a': a})



def fabu(request):

    user=request.session.get('user',default='')
    request.session["user"] = user
    a=models.User.objects.get(username=user)
    if request.method=='POST':
        name=request.POST.get('name')
        jianjie=request.POST.get('jianjie')
        price=request.POST.get('jiange')
        img=request.FILES.get('f1')




        try:

            q = open('G:/英雄时刻/untitled3/static/'+ img.name, 'wb+')
            q.write(img.read())



            s=models.text.objects.create(name=name,jianjie=jianjie,price=price,img=img,pd_id=models.User.objects.get(username=user).id)
        except:
            s = models.text.objects.create(name=name, jianjie=jianjie, price=price,
                                           pd_id=models.User.objects.get(username=user).id)
        # q = open('G:/英雄时刻/untitled3/static/'  + models.text.objects.get(name=name).img.name, 'wb+')
        # q.write(img.read())
        info='发布成功'

        return render(request,'发布.html',{'user':a,'info':info})



    return render(request,'发布.html',{'user':a})


def neirong(request):

    user = request.session.get('user', default='')
    request.session["user"] = user
    a = models.User.objects.get(username=user)
    s=models.text.objects.all()
    p=Paginator(s,5)

    new = request.GET.get('page')
    try:
        page=p.page(new)
    except PageNotAnInteger:
        page=p.page(1)
    except EmptyPage:
        page=p.page(p.num_pages)

    if request.GET.get('id'):
        id=request.GET.get('id')

        username=models.User.objects.get(username=user)
        buy_use_name=username.name

        buy_name=models.text.objects.get(id=id).name

        prime=models.text.objects.get(id=id).price
        if username.qq==None:
            info='请先修改资料'
            return render(request, '内容管理.html', {
                'user': a,
                'all': page, 'p': p, 'info': info})
        else:
            lianxi=username.qq
            buy_id=username.id

            sell_id=models.text.objects.get(id=id)
            sell_id_usernameid=sell_id.pd_id
            sell_name=sell_id.name

            sell_username=models.User.objects.get(id=sell_id_usernameid).name
            sell_lianxi=models.User.objects.get(id=sell_id_usernameid).qq
            models.buy.objects.get_or_create(pd_id=buy_id, name=buy_name, username=sell_username, price=prime, lianxi=sell_lianxi)
            models.sell.objects.create(pd_id=sell_id_usernameid,name=sell_name,username=buy_use_name,price=prime,lianxi=lianxi)
            models.text.objects.get(id=id).delete()
            info='购买成功,联系方式是:'+sell_lianxi
            # print(sell_id_usernameid)

            return render(request, '内容管理.html', {
            'user': a,
            'all': page,'p':p,'info':info,})

    return render(request, '内容管理.html', {
        'user': a,
        'all': page,'p':p})
def zixun(request):
    user = request.session.get('user', default='')
    request.session["user"] = user
    a = models.User.objects.get(username=user)

    return render(request, '在线咨询.html', {'a': a})

def dels(request):
    id=request.GET.get('id')
    s=models.text.objects.get(id=id).delete()
    return redirect('/son/')


def tupian(request):
    return render(request,'tupian.html')

def editor(request):
    user = request.session.get('user', default='')
    request.session["user"] = user
    a = models.User.objects.get(username=user)
    s=request.GET.get('id')
    # info = '须知:图像必须上传'


    if request.method=='POST':


        name = request.POST.get('name')
        jianjie = request.POST.get('jianjie')
        price = request.POST.get('jiange')
        try:
            img = request.FILES.get('f1')

            q = open('G:/英雄时刻/untitled3/static/' + img.name, 'wb+')
            q.write(img.read())
            new=models.text.objects.filter(id=s).update(name=name,jianjie=jianjie,price=price,img=img)
            return redirect('/son/')
        except:
            new = models.text.objects.filter(id=s).update(name=name, jianjie=jianjie, price=price)
            return redirect('/son/')

    return render(request,'修改.html',{'user':a})



def select(request):

    a=request.GET.get('ggbody')

    c=models.text.objects.filter(name__icontains=a)
    user = request.session.get('user', default='')
    s = models.User.objects.get(username=user)
    request.session["user"] = user
    p = Paginator(c, 5)

    new = request.GET.get('page')
    try:
        page = p.page(new)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(p.num_pages)


    return render(request,'内容管理.html',{
        'user': s,
        'all': page,'p':p})


def file1(request):
    if request.method == 'POST':
        files = request.FILES.get('f1')
        f=open('G:/英雄时刻/untitled3/static/'+files.name,'wb+')
        f.write(files.read())
        print(files.name)
    return render(request,'file1.html')

from django.contrib import messages

def abc(request):
    messages.success(request, "哈哈哈")
    return render(request,'弹窗.html')
def newlogin(request):
    return render(request,'login.html')
def see(request):
    user = request.session.get('user', default='')
    request.session["user"] = user
    a = models.User.objects.get(username=user)
    if request.GET.get('ggbody'):
        print(11)
        all=models.User.objects.get(username=request.GET.get('ggbody'))

        return render(request, '查开.html', {'user': a, 'all': all})




    return render(request,'查开.html',{'user':a})
def look(request):
    user = request.session.get('user', default='')
    request.session["user"] = user
    a = models.User.objects.get(username=user)
    if request.GET.get('ggbody'):
        try:
            now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            all = models.User.objects.get(username=request.GET.get('ggbody'))


            return render(request, '查开.html', {'user': a, 'all': all,'time':now})
        except:
            pass
    return render(request, '查开.html', {'user': a})
def see2(request):
    try:
        user = request.session.get('user', default='')
        request.session["user"] = user
        a = models.User.objects.get(username=user)
        id=request.GET.get('id')
        u_id=models.User.objects.get(id=id)
        sa = models.text.objects.filter(pd_id=id)
        buy = models.buy.objects.filter(pd_id=id)
        sell = models.sell.objects.filter(pd_id=id)
    except:
        pass


    return render(request, '查看2.html', {'user': a,'wordtoo':sa,'buy':buy,'sell':sell,'a':u_id})
clients={}
def to_chat(request):
    user = request.session.get('user', default='')
    request.session["user"] = user

    a = models.User.objects.get(username=user)
    return render(request,'聊天.html',{'user': a})
def test(request):
    return render(request,'Chat.html')

def msg_send(request):
    msg = request.POST.get("txt")
    useridto = request.POST.get("userto")
    useridfrom = request.POST.get("userfrom")
    type=request.POST.get("type")
    #发来{type:"2",msg:data,user:user},表示发送聊天信息，user为空表示群组消息，不为空表示要发送至的用户
    if type == "1":
        #群发
        for client in clients:
            clients[client].send(json.dumps({"type": 1, "data": {"msg": msg, "user": useridfrom}}).encode('utf-8'))
    else:
        # 私聊，对方显示
        clients[useridto].send(json.dumps({"type": 1, "data": {"msg": msg, "user": useridfrom}}).encode('utf-8'))
        # 私聊，自己显示
        clients[useridfrom].send(json.dumps({"type": 1, "data": {"msg": msg, "user": useridfrom}}).encode('utf-8'))
    return HttpResponse(json.dumps({"msg":"success"}))
@accept_websocket
def chat(request):

    # 判断是不是ws请求
    if request.is_websocket():

        # 保存客户端的ws对象，以便给客户端发送消息,每个客户端分配一个唯一标识
        userid=str(uuid.uuid1())[:8]
        clients[userid] = request.websocket
        # 判断是否有客户端发来消息，若有则进行处理，表示客户端与服务器建立链接成功
        while True:
            '''获取消息，线程会阻塞，
            他会等待客户端发来下一条消息,直到关闭后才会返回，当关闭时返回None'''
            message=request.websocket.wait()
            if not message:
                break
            else:
                msg=str(message, encoding = "utf-8")
                print(msg)
                #1、发来test表示链接成功
                if msg == "test":
                    print("客户端链接成功："+userid)
                    #第一次进入，返回在线列表和他的id
                    request.websocket.send(json.dumps({"type":0,"userlist":list(clients.keys()),"userid":userid}).encode("'utf-8'"))
                    #更新所有人的userlist
                    for client in clients:
                        clients[client].send(json.dumps({"type":0,"userlist":list(clients.keys()),"user":None}).encode("'utf-8'"))

    #客户端关闭后从列表删除
    if userid in clients:
        del clients[userid]
        print(userid + "离线")
        # 更新所有人的userlist
        for client in clients:
            clients[client].send(
                json.dumps({"type": 0, "userlist": list(clients.keys()), "user": None}).encode("'utf-8'"))

def index(request):
    user = request.session.get('user', default='')
    request.session["user"] = user
    a = models.User.objects.get(username=user)
    if request.POST.get('uzi'):
        print(request.POST.get('uzi'),request.POST.get('ggboy'))

    try:
        if request.method=='GET':
            id=request.GET.get('id')
            answer_d=models.User.objects.get(id=id)

            if not models.chat.objects.filter(pd_id=a.id,user_name=user,answer=answer_d.username,img=answer_d.img):
                models.chat.objects.create(pd_id=a.id,user_name=user,answer=answer_d.username,img=answer_d.img)



        c=models.chat.objects.filter(user_name=user) or models.chat.objects.filter(answer=user)
        # print(c)
        return render(request, 'index.html', {'user': a,'all':c})
    except:
        pass
    # models.chat.objects.values('user_name').order_by('user_name').distinct()
    c = models.chat.objects.filter(user_name=user) or models.chat.objects.filter(answer=user)
    # print(c)

    return render(request,'index.html',{'user': a,'all':c})