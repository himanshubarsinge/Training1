from django.shortcuts import render
from basic_app/forms import FormName
# Create your views here.


def index(request):
    return render(request, 'basic_app/index.html')

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_temps.html')

def sign_up(request):

    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation succes")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

            form.save()


    return render(request, 'basicapp/sign_up.html', context={'form':form})
