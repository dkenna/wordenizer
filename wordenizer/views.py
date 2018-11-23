from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from wordenizer import random_words

maxw = 200

def get_words(request, wordcount = 1):
    wordcount = int(wordcount) # sure to get an int here
    if wordcount > maxw: wordcount = maxw # max items
    words = random_words.get_words(wordcount, to_dict=True)
    return JsonResponse(words)
    
def get_404(request):
    return JsonResponse(status=404, data={
        'status': 'false',
        'error': 'not found'
    })
