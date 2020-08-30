from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="icon.ico",
        timeout=20

    )

# function to get data from the URL
def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        myHtmlData = getData("https://www.worldometers.info/coronavirus/country/india/")
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myStringData = ""
        for item in soup.find_all(attrs={'class': 'maincounter-number'}):
            myStringData += item.get_text()

        myList = myStringData.split()
        notifyme("Corona Virus Update Of India", f"Total Cases : {myList[0]}\nDeaths : {myList[1]}\nRecovered : {myList[2]}")
        time.sleep(3600)
