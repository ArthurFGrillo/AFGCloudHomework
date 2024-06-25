from django.http import HttpResponse

def home(request):
    return HttpResponse("Arthur Friço Grillo: Atividade de Cloud Computing & Site Reliability Engineering")
