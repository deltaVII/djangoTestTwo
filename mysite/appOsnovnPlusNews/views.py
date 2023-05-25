from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Posts
import datetime
# обработка ссылок

# основная страница
def man(request):
    posts = Posts.objects.order_by('-id')[:3]
    data = {
        'posts': posts
    }
    return render(request,'osnovn/main.html', data)
# страница посвящённая постам
def post(request):
    # оставил это в дань уважения
    '''
    count = Company.objects.count()
    
    posts=[]
    name = [Company.objects.get(id = i).companyName for i in range(count - 2, count + 1)]
    nomer = [Company.objects.get(id = i).companyNumber for i in range(count - 2, count + 1)]
    post = [Company.objects.get(id = i).companyPost for i in range(count - 2, count + 1)]
    for i in range(2,-1,-1):
        posts.append([name[i],nomer[i],post[i]])
    
    print(posts,'-'*20)
    posts = [[Company.objects.get(id=i)] for i in range(count,count-3,-1)]
    '''
    posts = Posts.objects.order_by('-id')[:3]
    data = {
        'posts': posts
    }
    return render(request,'Osnovn/post.html', data)

# страница создания постов
def form(request):
    
    if request.method == 'POST':
        form = dict(request.POST)
        Posts(name=str(form['name'][0]), textPost=str(form['post'][0]), date=str(datetime.datetime.now())).save()

        return HttpResponseRedirect('form')
    if request.method == 'GET':
        return render(request,'Osnovn/form.html')
        
# страницы с динамическим URL с постами
def idPosts(request, post_id):
    data = {
        'data': Posts.objects.order_by('id')[post_id-1:post_id]
    }
    return render(request, 'Osnovn/idPosts.html', data)
