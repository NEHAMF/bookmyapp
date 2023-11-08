from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import BookForm,BookModelForm
from myapp.models import Book


# Create your views here.
class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form=BookModelForm()
        return render(request,"book_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            # Employees.objects.create(**form.cleaned_data)
            print("created")
            return render(request,"book_add.html",{"form":form})
        else:
          return render(request,"book_add.html",{"form":form})
        

class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=Book.objects.all()
        return render(request,"book_list.html",{"data":qs})
    def post(self,request,*args,**kwargs):
        name=request.POST.get("box")
        qs=Book.objects.filter(name=name)
        return render(request,"book_list.html",{"data":qs})
    
    
class BookDetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)    
        return render(request,"book_detail.html",{"data":qs})
    
class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Book.objects.get(id=id).delete()
        return redirect("book-all")    
    
class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Book.objects.get(id=id)
        form=BookModelForm(instance=obj)
        return render(request,"book_edit.html",{"form":form})  
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Book.objects.get(id=id)
        form=BookModelForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("book-detail",pk=id)
        else: 
            return render(request,"book_edit.html")

