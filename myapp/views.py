from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactRegistration
from .models import ContactBook
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
# Create your views here.

# This Class Will Add new Item and Show All Items
class ContactAddShowView(TemplateView):
  template_name = 'myapp/addandshow.html'
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    fm = ContactRegistration()
    stud = ContactBook.objects.all()
    context = {'stu':stud, 'form':fm}
    return context
  
  def post(self, request):
    fm = ContactRegistration(request.POST)
    if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      no = fm.cleaned_data['number']
      add = fm.cleaned_data['address']
      reg = ContactBook(name=nm, email=em, number=no , address=add)
      reg.save()
    return HttpResponseRedirect('/')

# This Class will Update/Edit
class ContactUpdateView(View):
  def get(self, request, id):
    pi = ContactBook.objects.get(pk=id)
    fm = ContactRegistration(instance=pi)
    return render(request, 'myapp/update.html', {'form':fm})
  
  def post(self, request, id):
    pi = ContactBook.objects.get(pk=id)
    fm = ContactRegistration(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
    return render(request, 'myapp/update.html', {'form':fm})

# This Class will Delete
class ContactDeleteView(RedirectView):
  url = '/'
  def get_redirect_url(self, *args, **kwargs):
    del_id = kwargs['id']
    ContactBook.objects.get(pk=del_id).delete()
    return super().get_redirect_url(*args, **kwargs)