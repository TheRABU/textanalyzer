from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("about us here")


def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'default')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')


    # Initialize the analyzed text variable
    # analyzed = djtext

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (fullcaps== "on"):
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = " "
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char.upper()
        params = {'purpose':'New line removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = " "
        for index, char  in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]== " ":
                pass
            else:
                analyzed = analyzed + char.upper()
        params = {'purpose':'Extra Space removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # Calculate character count if the checkbox is checked
    else:
        if charcount == "on":
            for char in djtext:
                character_count = len(djtext)
                response_text = f"Character Count: {character_count}"
                return HttpResponse(response_text)

            params = {'purpose': 'Text Analysis', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)






def removepunc(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    #Analyze the text
    return HttpResponse("remove punc")


def capfirst(request):
    return HttpResponse("Capitalize First")

def newlineremove(request):

    return HttpResponse("capitalize first")

def spaceremove(request):

    return HttpResponse("space remover")

def charcount(request):

    return HttpResponse("charcount ")


def ex1(request):
    s = ''' Navigation Bar <br> </h2>
    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
    <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s)
