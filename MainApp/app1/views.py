from django.shortcuts import render
import csv
from django.http import HttpResponse
# Create your views here.
def some_view(request):
    response =HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="NIFTY_F1_Xm8mAtb.csv"'},

    )
    return response