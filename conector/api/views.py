from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from.models import Campaña
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


@login_required
def home(request):
        nombres = Campaña.objects.all()
        if len(nombres)>0:
            data = {'message':"Success",'nombres':nombres }
        return render(request, 'api/home.html', data)



class BeliveoStatus(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'login'

    def get(self,request):
        statuscampaña = list(Campaña.objects.values())
        if (statuscampaña) is True:
            status = { 'message':"1",'statuscampaña':statuscampaña}
        else:
            status = {'message':"0",'statuscampaña':statuscampaña}
        return JsonResponse(status)





def welcome(request):

    return render(request, 'api/welcome.html')