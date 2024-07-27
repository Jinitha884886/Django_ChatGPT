from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def chatbot(request):
    if request.method == "POST":
        message = request.POST.get('message')
        reponse = "This is my response"
        return JsonResponse({'message':message, 'response':reponse})
    return render(request, "chatbot.html")