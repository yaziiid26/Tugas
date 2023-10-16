import requests
from bs4 import BeautifulSoup
# Membutuhkan instalasi requests dan bs4 library
# python3 -m venv venv
# ./venv/Scripts/activate
# pip install bs4 requests

print("-"*20)
judul = "Web Analis"
print(judul.upper())
print("-"*20)

url_receive = input("URL : ")
date_receive = input("Date : ")

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url_receive, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select_one(' title ').text
og_description = soup.select_one('meta[property="og:description"]')
og_image = soup.select_one('meta[property="og:image"]')

desc = og_description['content']
image = og_image['content']

print("-"*20)
print("inputan diterima")
print("-"*20)
print(f"URL: {url_receive}\nJudul: {title}\nDeskripsi: {desc}\nGambar: {image}\nDate: {date_receive}")