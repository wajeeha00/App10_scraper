import requests
import selectorlib
import time
URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

def scrape(url):
    response = requests.get(url, headers=HEADERS, verify=False)  # Disabling SSL verification (not recommended for production)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)["tours"]
    return value
def read(extracted):
    with open("data.txt", "r") as f:
        data = f.read()
        return data
def store(extracted):
    with open("data.txt", "a") as f:
        f.write(extracted + "\n")
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
    
        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email(message="new text found")
        time.sleep(2)


