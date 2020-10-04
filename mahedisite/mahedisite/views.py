#I have created this file- Mahedi Hassan
from typing import Dict

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def navigation(request):
    s=''' <h1>Navigation Bar</h1>  
    <a href="https://www.youtube.com/">Go to you tube
	</a><br/>
	<a href="https://www.codewithharry.com/">Django by Harry bhai
	</a><br/>
	<a href="https://www.rediff.com/">Go to rediff
	</a><br/>
	<a href="https://www.google.com/">Google anything!
	</a><br>
	<a href="https://www.python.org/">Python.com
	</a>'''
    return HttpResponse(s)


def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':djtext,'analyzed_text':analyzed}
        djtext=analyzed
    if uppercase=="on":
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': djtext, 'analyzed_text': analyzed}
        djtext=analyzed
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char !="\r":
                analyzed=analyzed+char
        params = {'purpose': djtext, 'analyzed_text': analyzed}
        djtext=analyzed
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
    if (charcount=="on"):
        onlychar=djtext.replace(" ","")
        length=len(onlychar)
        params = {'purpose': djtext, 'analyzed_text': length}
        

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and uppercase != "on"):
        return HttpResponse("please select any operation and try again")
    return render(request,'analyze.html',params)








'''
def capfirst(request):
    return HttpResponse("This is capfirst <a href='/'>Back</a>")

def spaceremove(request):
    return HttpResponse("This is spaceremove <a href='/'>Back</a>")

def charcount(request):
    return HttpResponse("This is charcount <a href='/'>Back</a>")

'''



