from pyshorteners import Shortener
from pyperclip import copy as clipcopy, paste as clippaste
from requests import get

def validator(input_string):
    try:
        response = get(input_string)
        return True
    except:
        return False

def input_url():
    copied_url = clippaste()
    choice = 'n'
    if validator(copied_url):
        choice = input("Is this the url you want to shorten: {}\n(Yy/Nn)".format(copied_url)).lower()
        if choice == 'y':
            return copied_url
    
    if choice!='y':
        url= input('\n Enter the url you want to shorten (https://www.example.com): ')
        if validator(url):
            return url
        else:
            print("Invalid Url")
            return ""

def url_shortener():
    shortener = Shortener()
    url = input_url()
    try:
        shortened_url = shortener.tinyurl.short(url)
        print("Here's your shortened url : ",shortened_url, "\nURL copied to clipboard")
        clipcopy(shortened_url)
    except:
        print("{} -> It can't be shortened.".format(url))

if __name__ == "__main__":
    url_shortener()