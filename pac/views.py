from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import GeeksModel
from .forms import GeeksForm

 
# Create your views here.

###Create View

# def create_view(request):
#     form = GeeksForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
        
#     context ={
#         'form': form,
#     }
#     return render(request, 'create_view.html', context)

# ###Retrieve View
# def list_view(request):
#     project = GeeksModel.objects.all()
#     context = {
#         'project': project
#     }
    
#     return render(request, 'list_view.html', context)


# def detail_view(request,id):
#     project = GeeksModel.objects.get(id=id)
#     context={   'project': project }
    
#     return render(request, 'detail_view.html', context)

# ###Update View
# def update_view(request,id):
#     obj = get_object_or_404(GeeksModel,id=id)
#    
    
#     form = GeeksForm(request.POST or None,instance = obj)
    
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect('/'+id)
    
#     context ={
#         'form': form,
#     }
#     return render(request, 'update_view.html', context)
    
    
# ##Delete View

# def delete_view(request,id):
#     obj = get_object_or_404(GeeksModel,id=id)
#     if request.method == 'POST':
#         obj.delete()
#         return HttpResponseRedirect('/')
#     return render(request, 'delete_view.html')


############CLASS BASED VIEWS ##############################################################################       
from django.views.generic.edit import CreateView ,UpdateView,DeleteView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
class GeeksCreate(CreateView):
    model = GeeksModel
    fields = ['title', 'description']
class GeeksList(ListView):
 
    # specify the model for list view
    model = GeeksModel
    
 
class GeeksDetailView(DetailView):
    # specify the model to use
    model = GeeksModel
    
    
class GeeksUpdateView(UpdateView):
    # specify the model you want to use
    model = GeeksModel
 
    # specify the fields
    fields = [
        "title",
        "description"
    ]
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"
    
    
class GeeksDeleteView(DeleteView):
    # specify the model you want to use
    model = GeeksModel
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"