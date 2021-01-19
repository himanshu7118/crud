from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import View,DetailView,ListView,DeleteView,UpdateView,CreateView,TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'hello/index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'hello/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'hello/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principle','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principle','location')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('hello:list')
