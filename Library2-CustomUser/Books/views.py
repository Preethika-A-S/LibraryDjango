from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

from Books.models import Book
def home(request):
    context={'name':'Arun','age':27}
    return render(request,'home.html',context)

@login_required
def add_books(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        l=request.POST['l']
        pa=request.POST['pa']

        c=request.FILES.get('i')
        f=request.FILES.get('f')

        b=Book.objects.create(title=t,author=a,price=p,language=l,pages=pa,cover=c,pdf=f)   #creates a new record inside table Book
        b.save()   #saves the record inside table
        return view_books(request)
    return render(request,'add.html')

def view_books(request):
    k=Book.objects.all()    #Read all records from table Books and assigns it to k
    return render(request,'view.html',{'Book':k})

def detail(request,p):
    k=Book.objects.get(id=p)
    return render(request,'detail.html',{'book':k})

@login_required
def edit(request,e):
    k = Book.objects.get(id=e)

    if(request.method=="POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['p']
        k.language=request.POST['l']
        k.pages=request.POST['pa']

        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES.get('i')

        if(request.FILES.get('f') == None):
            k.save()
        else:
            k.cover = request.FILES.get('f')

        k.save()
        return view_books(request)

    return render(request,'edit.html',{'book':k})


@login_required
def delete(request,i):
    k=Book.objects.get(id=i)
    k.delete()
    return view_books(request)

def search(request):
    k=None   #initialise k as None
    if(request.method=="POST"):
        query=request.POST['q']  #get the input key from form
        print(query)
        if query:
            k=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))  #it checks the key in title and author field of every records.  (it uses in the conditions or/and)
            #filter function returns only the matching records
    return render(request,'search.html',{'book':k})