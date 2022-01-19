from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from.models import Campaña
# Create your views here.

def home(request):
        nombres = Campaña.objects.all()
        if len(nombres)>0:
            data = {'message':"Success",'nombres':nombres }
        return render(request, 'api/home.html', data)

class BeliveoCampaings(View):
    

    def get(self,request):
        statuscampaña = list(Campaña.objects.values())
        if (statuscampaña) is True:
            status = { 'message':"1",'statuscampaña':statuscampaña}
        else:
            status = {'message':"0",'statuscampaña':statuscampaña}
        return JsonResponse(status)



    def post(self,request):
        pass