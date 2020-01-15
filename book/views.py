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