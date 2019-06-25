from django.shortcuts import render,HttpResponse
from .models import tag_user,user_3,items,user_analyze3,User_image,rank_all,blog
import sys
sys.path.append(r'F:\biyesheji\user-portrait')
import testing
def hello(request):
    result = tag_user.objects.filter(user = 'scrollie')
    context = {}
    context['hello'] = 'hello World!'
    context['influence'] = result[0].influences
    return render(request,'index.html',context)

def base(request):
    pass
    return render(request, 'base.html')

def users(request):
    q = request.POST.get('content')
    print('1111')
    print(q)
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request,'users.html',{'error_msg':error_msg})
    post_list = tag_user.objects.filter(user = q)
    print(post_list)
    if not post_list :
        error_msg = '该开发者录入ing，请稍后查询该开发者'
        testing.main(q)
        return render(request, 'index.html', {'error_msg': error_msg})
    else:
        print("dskdnk")
        data ={}
        data['tag_user']=post_list
        user_list = user_3.objects.filter(login = q)
        data['user_list']=user_list
        rank_list = rank_all.objects.filter(login=q)
        data['rank_list'] = rank_list
        item_list = items.objects.filter(owner = q)
        data['item_list'] = item_list
        blog_list = blog.objects.filter(login=q)
        data['blog_list'] = blog_list
        analyze_list = user_analyze3.objects.filter(login=q)
        data['analyze_list'] = analyze_list
        image_url = User_image.objects.filter(login=q)
        data['image'] = image_url
        return render(request, 'users.html',{'error_msg':error_msg,'data':data})

def rank(request):
    data = {}
    print("112")
    analyze_list = rank_all.objects.all()
    data['rank_list'] = analyze_list.order_by('score_rank')
    user_list = user_3.objects.all()
    data['user_list']=user_list
    image_url = User_image.objects.all()
    data['image'] = image_url
    return render(request, 'rank.html', data)

def about(request):
    pass
    return render(request, 'about.html')



