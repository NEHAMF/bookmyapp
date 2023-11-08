from django import forms
from myapp.models import Book
class BookForm(forms.Form):
 name=forms.CharField()
 author=forms.CharField()
 page_no=forms.IntegerField()
 price=forms.IntegerField()

class BookModelForm(forms.ModelForm):

    class Meta:
        model=Book
        fields="__all__"
        
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "page_no":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            
        }