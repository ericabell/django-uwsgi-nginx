from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class BasicView(View):
    def get(self, request):
        return HttpResponse('this worked')


class MyFormView(View):
    def get(self, request):
        form = NameForm()
        return render(request, 'name.html', {'form': form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            # process form data here

            return HttpResponse('form data processed')
        return HttpResponse('form data was not valid')
