from django.shortcuts import render, redirect, HttpResponse
from . import models


# Create your views here.
# 出版社列表
def publisher_list(request):
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, 'publisher/publisher_list.html', {'publisher_list': ret})


# 添加出版社
def add_publisher(request):
    if request.method == 'POST':
        name = request.POST.get('publisher_name')
        models.Publisher.objects.create(name=name)
        return redirect('/publisher_list/')
    return render(request, 'publisher/add_publisher.html')


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
    return render(request, 'publisher/edit_publisher.html', {"edit_id": edit_id})


# 书籍列表
def book_list(request):
    ret = models.Book.objects.all().order_by("id")
    return render(request, 'book/book_list.html', {'book_list': ret})


# 添加书籍
def add_book(request):
    if request.method == "POST":
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        models.Book.objects.create(title=new_title, publisher_id=new_publisher_id)
        return redirect('/book_list/')
    ret = models.Publisher.objects.all()
    return render(request, 'book/add_book.html', {"publisher_list": ret})


# 删除书籍
def del_book(request):
    del_id = request.GET.get('id', None)
    if del_id:
        del_obj = models.Book.objects.filter(id=del_id)
        del_obj.delete()
        return redirect('/book_list/')
    else:
        return HttpResponse("删除失败")


# 修改书籍
def edit_book(request):
    if request.method == "POST":
        # 1.拿到html视图中的id和name
        ret_id = request.POST.get("book_id")
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")

        # 2.查询数据库，再赋新值，再更新数据库
        ret_obj = models.Book.objects.get(id=ret_id)
        ret_obj.title = new_title
        ret_obj.publisher_id = new_publisher_id
        ret_obj.save()
        return redirect('/book_list/')

    edit_id = request.GET.get("id")
    ret = models.Publisher.objects.all()
    return render(request, 'book/edit_book.html', {"publisher_list": ret, "edit_id": edit_id})


# 作者
def author_list(request):
    ret = models.Author.objects.all().order_by('id')
    return render(request, 'author/author_list.html', {"author_list": ret})


def add_author(request):
    if request.method == "POST":
        new_author = request.POST.get("author_name")
        models.Author.objects.create(name=new_author)
        return redirect("/author_list/")
    ret = models.Author.objects.all()
    return render(request, 'author/add_author.html', {"author_list": ret})


def del_author(request):
    del_id = request.GET.get('id', None)
    if del_id:
        del_obj = models.Author.objects.filter(id=del_id)
        del_obj.delete()
        return redirect('/author_list/')
    else:
        return HttpResponse("删除失败")


def edit_author(request):
    if request.method == 'POST':
        ret_id = request.POST.get('author_id')
        new_name = request.POST.get('author_name')

        ret_obj = models.Author.objects.get(id=ret_id)
        ret_obj.name = new_name
        ret_obj.save()
        return redirect('/author_list/')
    edit_id = request.GET.get('id')
    return render(request, 'author/edit_author.html', {"edit_id": edit_id})
