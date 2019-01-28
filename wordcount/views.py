from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    # return render(request , 'home.html' , {'hi_there' : 'This is me'})
    return render(request , 'home.html' , {'hi_there' : 'This is me'})
# def def count(request):
def about(request):
    # return render(request , 'home.html' , {'hi_there' : 'This is me'})
    return render(request , 'about.html' , {'message' : 'This is About Page.'})
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    sorted_words = sorted(worddict.items() , key = operator.itemgetter(1) , reverse = True)
    return render(request , 'count.html' , {'fulltext' : fulltext , 'count' : len(wordlist) , 'sortedword':sorted_words})
