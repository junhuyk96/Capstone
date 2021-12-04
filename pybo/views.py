from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    """
    pybo 목록 출력
    """
    return render(request, 'pybo/main_list.html')

def contact_create(request):
    """

    사용자 메세지 저장
    """

    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.save()
            return redirect('pybo:index')
    else:
        form=ContactForm()
    context={'form': form}
    return render(request, 'pybo/main_list.html', context)