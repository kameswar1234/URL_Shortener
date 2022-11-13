from django.shortcuts import render
import pyshorteners


# Create your views here.

url= input('Enter the url: ')


def shortenurl(url):
    s= pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenurl(url)
