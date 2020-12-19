from urllib.request import urlopen
from requests import get

def validator(input_string):
    try:
        response = get(input_string)
        return True
    except:
        return False

def headers(page):

    headers=page.headers
    print(headers)
    file = open("headers.txt", "w")
    file.write(str(headers))
    file.close()
    print("Headers Saved as headers.txt")

def source_code(page):
    print("\n"*5)
    source_code=page.read()
    print(source_code)
    file = open("source_code.html", "w")
    file.write(str(source_code))

if __name__ == "__main__":
    url=input("Enter url: ")
    if validator(url):
        page=urlopen(url)
        headers(page)
        source_code(page)
    else:
        print("Invalid Url")
