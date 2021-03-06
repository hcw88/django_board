from django.shortcuts import render
from googletrans import Translator

# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        text = request.POST.get('before')
        if text:
            f = request.POST.get('from')
            t = request.POST.get('to')

            translator = Translator()
            if not f or not t:
                f = "en"
                t = "ko"
                trans = translator.translate(text, dest="ko")
            else : 
                trans = translator.translate(text, src=f, dest=t)
            context.update ({
                'before' : text,
                'after' : trans.text,
                'from' : f,
                'to' : t,
            })
    return render(request, "trans/index.html", context)


    
# from googletrans import Translator
 
 
# text1 = "안녕하세요. 저는 학생입니다."
 
# translator = Translator() 
# trans1 = translator.translate(text1, src='ko', dest='ja')

# print("English to Japanese: ", trans1.text)
