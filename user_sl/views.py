from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request,"sign-in-page.html")



def signup(request):
    return render(request,"sign_up_page.html")




def password(request):
    return render(request,"password_page.html")





def resetpassword(request):
    return render(request,"reseting_password_page.html")

