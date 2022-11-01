from hashlib import new 
import requests
from bs4 import BeautifulSoup 
import smtplib

def trimitere_email():
    server=smtplib.SMTP('mail.x-it.ro',26)
    server.starttls()
    server.login("data_scraping@coneasorin.ro","stiinte216_2022")
    server.sendemail("data_scraping@coneasorin.ro","01alex.buta1@gmail.com","Subject:Pretul a scazut\n\nPretul a scazut la 1800 lei")
    print ("Email trimis")
    server.quit()

def data_scraping():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-256gb-5g-deep-purple-mq9x3rx-a/pd/DJDY4LMBM/?X-Search-Id=70fbed0fdc2bc5d4db3f&X-Product-Id=101075770&X-Search-Page=1&X-Search-Position=2&X-Section=search&X-MB=0&X-Search-Action=view")
    soup=BeautifulSoup(req.text, 'html.parser')
    price=soup.find('p', attrs={'class':'product-new-price'}).text
    new_price=price[0:5]
    new_price=new_price.replace(".","")
    new_price=int(new_price)
    if(new_price<7799):
        trimitere_email()
        print("Avem o modificare de pret!!!")
    else:
            print("Pretul nu a scazut")
        