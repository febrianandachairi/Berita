from django.shortcuts import render, redirect

# Create your views here.
import requests
from .form import *
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

API_KEY = '89fd392f3e194f1d9fcbcb09ef9d6901'


def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    context = {'blogs': BeritaApiBaru.objects.all()}
    return render(request, 'home.html', context)


def login_view(request):
    return render(request, 'login.html')


def berita_detail(request, id):
    context = {}
    try:
        blog_obj = BeritaApiBaru.objects.filter(id=id).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'berita_detail.html', context)


def see_berita(request):
    context = {}

    try:
        blog_objs = BeritaModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_berita.html', context)

@login_required
def add_berita(request):
    context = {'form': BlogForm}

    if request.method == 'POST':
        form = BlogForm(request.POST)
        print(request.FILES)
        input_nama_berita = request.POST.get('name')
        input_link = request.POST.get('link')
        input_contentsnippet = request.POST.get('contentsnippet')
        input_isodate = request.POST.get('isoDate')
        input_image = request.POST.get('image')

        BeritaApiBaru.objects.create(
            title = input_nama_berita,
            link  = input_link,
            contentSnippet = input_contentsnippet,
            isoDate = input_isodate,
            image = input_image,
        )
        
        return redirect('/add-berita/')
    
    return render(request, 'add_berita.html', context)

@login_required
def berita_update(request, id):
    template_name = 'update_berita.html'
    get_berita = BeritaApiBaru.objects.get(id=id)
    
    if request.method == 'POST':
        input_nama_berita = request.POST.get('name')
        input_link = request.POST.get('link')
        input_contentsnippet = request.POST.get('contentsnippet')
        input_isodate = request.POST.get('isoDate')
        input_image = request.POST.get('image')
        
        
        # Bagian Mengedit Data
        get_berita.title = input_nama_berita
        get_berita.link  = input_link
        get_berita.contentSnippet = input_contentsnippet
        get_berita.isoDate = input_isodate
        get_berita.image = input_image
        get_berita.save()
        
        print("Update/Edit Data")
    
        return redirect(tabel_berita_api)
    context = {
        'title' : 'Ini Halaman Edit Data reksadana',
        'berita_api' : get_berita,
    }
    return render(request, template_name, context)

@login_required
def berita_delete(request, id):
    try:
        blog_obj = BeritaApiBaru.objects.get(id=id)
        blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('tabel_berita_api')


def register_view(request):
    return render(request, 'register.html')


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def post(request):
    return render(request, 'post.html')

def news(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&country=id&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']



    context = {
        'articles' : articles
    }

    return render(request, 'news.html', context)

def tabel_akun(request):
    context = {}

    try:
        blog_objs = User.objects.all()
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'tabel_akun.html', context)

def tabel_berita_api(request):
    context = {}

    try:
        blog_objs = BeritaApiBaru.objects.all()
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'tabel_berita_api.html', context)

@login_required
def berita_api_baru(request):
    x_market = requests.get('https://berita-indo-api.vercel.app/v1/cnbc-news/market')
    data_market = x_market.json()#print the response text (the content of the requested file):
    for i in data_market["data"]:
        title_berita = i['title']
        link_berita = i['link']
        contentSnippet_berita = i['contentSnippet']
        isoDate_berita = i['isoDate']
        image_berita = i['image']['large']
        get_kategori = KategoriBerita.objects.get(name='Market')
        
        get_berita = BeritaApiBaru.objects.filter(title=title_berita)
        if get_berita.exists():
            jenis_berita = get_berita.first()
            jenis_berita.title = title_berita
            jenis_berita.link = link_berita
            jenis_berita.contentSnippet =  contentSnippet_berita
            jenis_berita.isoDate = isoDate_berita
            jenis_berita.image = image_berita
            jenis_berita.kategori = get_kategori
            jenis_berita.save() 
       
        else: 
            BeritaApiBaru.objects.create(
               title = title_berita,
               link = link_berita,
               contentSnippet = contentSnippet_berita,
               isoDate = isoDate_berita,
               image = image_berita,
               kategori = get_kategori,
               
            ) 
    x_news = requests.get('https://berita-indo-api.vercel.app/v1/cnbc-news/news')
    data_news = x_news.json()#print the response text (the content of the requested file):
    for i in data_news["data"]:
        title_berita = i['title']
        link_berita = i['link']
        contentSnippet_berita = i['contentSnippet']
        isoDate_berita = i['isoDate']
        image_berita = i['image']['large']
        get_kategori = KategoriBerita.objects.get(name='News')
        
        get_berita = BeritaApiBaru.objects.filter(title=title_berita)
        if get_berita.exists():
            jenis_berita = get_berita.first()
            jenis_berita.title = title_berita
            jenis_berita.link = link_berita
            jenis_berita.contentSnippet =  contentSnippet_berita
            jenis_berita.isoDate = isoDate_berita
            jenis_berita.image = image_berita
            jenis_berita.kategori = get_kategori
            jenis_berita.save() 
       
        else: 
            BeritaApiBaru.objects.create(
               title = title_berita,
               link = link_berita,
               contentSnippet = contentSnippet_berita,
               isoDate = isoDate_berita,
               image = image_berita,
               kategori = get_kategori,
               
            )
             
    return redirect(tabel_berita_api)

@login_required
def about_us(request):
    return render(request, 'about_us.html')

@login_required
def user_delete(request, id):
    try:
        blog_obj = User.objects.get(id=id)
        blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('tabel_akun')
