from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template

def login(request): # Vista login
    #urlcss = './core/plantillas/css/login.css'
    #doc_externo=open('./core/plantillas/login.html')
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #ctx=Context({"css":urlcss})
    #documento=plt.render(ctx)

    doc_externo=get_template('index.html')
    documento=doc_externo.render({})
    return HttpResponse(documento)

def home(request): # Vista Home
    
    doc_externo=open('./core/plantillas/login.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)