from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.decorators.http import require_http_methods, require_GET
from django.views.decorators.csrf import csrf_exempt


from wordenizer import random_words

maxw = 200

def ensure(obj,cond): return cond(obj)

@require_GET
@csrf_exempt
def get_words(request, wordcount = 1):
    try:
        wordcount = int(wordcount)
        if wordcount > maxw: wordcount = maxw # max items
        words = random_words.get_words(wordcount, to_dict=True)
        return JsonResponse(words)
    except Exception as e:
        print(e.message)
        return get_400(request)
    
def get_json_http_error(request,status,msg):
    return JsonResponse(status=status, data={
        'status': 'error',
        'error': msg
    })

@csrf_exempt
def get_404(request):
    return get_json_http_error(request, 404,"not ffffound")

@csrf_exempt
def get_400(request):
    return get_json_http_error(request, 400, "bad requesssst")

@csrf_exempt
def get_405(request):
    return get_json_http_error(request, 400, "bad meth")
