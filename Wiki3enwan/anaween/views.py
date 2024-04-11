from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.shortcuts import redirect
from django.core.paginator import Paginator
from .forms import enwaanForm
from django.views.generic import DetailView
from .forms import EditForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def Home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        enwaanSearch = enwaan.objects.filter(الأسم_والمنطقة__icontains=q)
    else:
        enwaanSearch = enwaan.objects.all()
    if enwaanSearch.count() == 0:
        return render(request, 'noresult.html')
    paginator=Paginator(enwaanSearch,8)
    page_number=request.GET.get('page')
    enwaanSearch=paginator.get_page(page_number)
    context = {'enwaanSearch':enwaanSearch}
    return render(request, 'Home.html', context)

def add_enwaan(request):
    form = enwaanForm
    if request.method == 'POST':
        form = enwaanForm(request.POST)
        if form.is_valid() & enwaan.objects.filter(الأسم_والمنطقة__icontains=form.data.get("الأسم_والمنطقة")).exists():
            form.add_error('الأسم_والمنطقة', 'الأسم والمنطقة موجود بالفعل')
        elif form.is_valid():
            form.save()
            response = redirect('Home')
            return response
    context = {'form':form}
    return render(request, 'add-enwaan.html', context)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class enwaanEditView(LoginRequiredMixin,DetailView):
    model = enwaan
    template_name = 'edit_enwaan.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()  # Retrieve the object based on slug
        form = EditForm(instance=obj)
        context['form'] = form
        return context

    def post(self, request, slug):
        obj = self.get_object()
        form = EditForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("enwaan_detail",slug)  # Replace with your success URL pattern name
        else:
            context = {'form': form, 'enwaan': obj}
            return render(request, self.template_name, context)
        
class enwaanDetailView(DetailView):
    model = enwaan
    template_name = 'enwaan_detail.html'
    context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here
        enwaanSearch = enwaan.objects.all()[:10]
        context["enwaanSearch"] = enwaanSearch
        # Add any additional context data here        
        return context
    
