import requests
import selectorlib
import time
import sqlite3
URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
connection = sqlite3.connect('dd.db')

def scrape(url):
    response = requests.get(url, headers=HEADERS, verify=False)  # Disabling SSL verification (not recommended for production)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)["tours"]
    return value
def read(extracted):
    row = extracted.split(",")
    row = [i.strip() for i in row]
    band,city,date = row
    cursor = connection.cursor()
    cursor.execute('select * from events where band=? AND city=? AND date=?' ,(band, city, date))
    rows = cursor.fetchall()
    print(rows)

def store(extracted):
    row = extracted.split(",")
    row = [i.strip() for i in row]
    cursor = connection.cursor()
    cursor.execute('insert into events (band, city, date) values (?, ?, ?)', row)
    connection.commit()
def send_email():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = ""
    receiver_email = ""
    password = "password"

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
    
      
        if extracted != "No upcoming tours":
            row= read(extracted)
            if not row:
                store(extracted)
                send_email(message="new text found")
        time.sleep(2)


