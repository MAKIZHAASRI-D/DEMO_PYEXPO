from django.shortcuts import render # type: ignore

def Homepage(request):
    context={
        "name":"Sharmily",
        "number":[1,2,3,4,5],
        "marks": {
            "tamil":100,
            "english":99,
            "maths":95
        }
    }
    return render(request,'index.html',context)
# Create your views here.
