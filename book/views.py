from django.shortcuts import render, redirect, HttpResponse
from . import models


# Create your views here.
# 出版社列表
def publisher_list(request):
    ret = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list': ret})


# 添加出版社
def add_publisher(request):
    if request.method == 'POST':
        name = request.POST.get('publisher_name')
        models.Publisher.objects.create(name=name)
        return redirect('/publisher_list/')
    return render(request, 'add_publisher.html')


# 删除出版社
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


# 编辑出版社
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

    # 获取要编辑的出版社
    edit_id = request.GET.get('id')
    return render(request, 'edit_publisher.html', {"edit_id": edit_id})


# 书籍列表
def book_list(request):
    ret = models.Book.objects.all()
    return render(request, 'book_list.html', {'book_list': ret})


# 添加书籍
def add_book(request):
    if request.method == "POST":
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        models.Book.objects.create(title=new_title, publisher_id=new_publisher_id)
        return redirect('/book_list/')
    ret = models.Publisher.objects.all()
    return render(request, 'add_book.html', {"publisher_list": ret})
