from django.shortcuts import render, redirect, HttpResponse
from . import models


# Create your views here.
def publisher_list(request):
    ret = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list': ret})


def add_publisher(request):
    if request.method == 'POST':
        name = request.POST.get('publisher_name')
        models.Publisher.objects.create(name=name)
        return redirect('/publisher_list/')
    return render(request, 'add_publisher.html')


def del_publisher(request):
    # 1.从get请求的参数里面拿到将要删除的数据的ID值
    del_id = request.GET.get('id', None)
    # 如果能取到id值
    if del_id:
        del_obj = models.Publisher.objects.filter(id=del_id)
        del_obj.delete()
        # 返回删除后的页面，跳转到出版社的列表页，查看是否删除成功
        return redirect('/publisher_list/')
    else:
        return HttpResponse("删除失败")


def edit_publisher(request):
    if request.method == 'POST':
        # 1.拿到html视图中的id和name
        ret_id = request.POST.get('id')
        new_name = request.POST.get('name')

        # 2.查询数据库，再赋新值，再更新数据库
        id_obj = models.Publisher.objects.get(id=ret_id)
        id_obj.name = new_name
        id_obj.save()

        return redirect("/publisher_list/")
    #
    # 获取要编辑的出版社
    # edit_id = request.GET.get('id')
    # ret = models.Publisher.objects.get(id=edit_id)
    return render(request, 'edit_publisher.html')