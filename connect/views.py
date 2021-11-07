from django.template import loader
from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView 
from .models import ConnectModel
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


# Create your views here.
class ConnectList(ListView):
    template_name = 'list.html'
    model = ConnectModel



class ConnectDetail(DetailView):
    template_name = 'detail.html'
    model = ConnectModel

class ConnectCreate(CreateView):
    template_name = 'create.html'
    model = ConnectModel
    fields = ('title', 'memo','myimage','level','level_b')
    success_url = reverse_lazy('list')
   


class ConnectDelete(DeleteView):
    template_name = 'delete.html'
    model = ConnectModel
    success_url = reverse_lazy('list')

class ConnectUpdate(UpdateView):
    template_name = 'update.html'
    model = ConnectModel
    fields = ('title', 'memo','myimage','level')
    success_url = reverse_lazy('list')


class ConnectMember(ListView):
    template_name = 'member.html'
    model = ConnectModel







def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username,'',password)
        return render(request, 'signup.html', {'some':100})

    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    
    return render(request, 'login.html')

def goodfunc(request,pk):
    template = loader.get_template('../connect_app/templates/member.html')
    post = ConnectModel.objects.get(pk=pk)
    post.save()
    image = post.myimage
    context = {'m_image':image}
    # detail_url = '/post/' + 'image' + '/'
    # return redirect(image)
    return HttpResponse(template.render( context, request))

