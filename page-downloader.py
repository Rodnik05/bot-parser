import requests
from bs4 import BeautifulSoup

def main():
    #getting the webpage and turning it into a string
    webpage = requests.get('https://olimpiada.ru/article/992').text

    #saving the webpage, just in case
    with open('webpage','w') as file:
        file.write(webpage)

if __name__ == 'main':
    main()