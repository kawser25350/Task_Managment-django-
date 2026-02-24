from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def add_author(request):

    if request.method == 'POST':
        author_form=forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('author')
    author_form=forms.AuthorForm()
    return render(request, 'pages/author_add_author.html',{'form':author_form})

def author(request):
    return render(request, 'pages/author_home.html')