from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request,"sign-in-page.html")

def checkUser(request):
    if request.method == "POST":
        print(request)
        print(request.POST.values())

    return HttpResponse("what")


def signup(request):
    return render(request,"sign_up_page.html")




def password(request):
    return render(request,"password_page.html")





def resetpassword(request):
    return render(request,"reseting_password_page.html")


"""

class Human:

    height = 110
    weight = 120
    
    
    
    def run(self):
        print("running")
        
    def walk(self):
        print("walking")
        
kumar = Human()
kumar.height
kumar.weight
kumar.run()
kumar.walk()
"""
