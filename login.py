from datetime import datetime
import pytz
from bs4 import BeautifulSoup
from lxml import html
import json

def login(session_requests, login_url, password, username, quarter):
    urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"
    result = session_requests.get(login_url)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='__RequestVerificationToken']/@value")))[0]

    payload = {
        "VerificationOption": "UsernamePassword",
        "Database": "10",
        "LogOnDetails.Password": password,
        "__RequestVerificationToken": authenticity_token,
        "LogOnDetails.UserName": username
    }
    session_requests.post(
        login_url,
        data=payload,
        headers=dict(referer=login_url)
    )

    if quarter == None:
        result = session_requests.get(urls, headers=dict(referer=urls))

        soup = BeautifulSoup(result.text, "html.parser")

        h1 = soup.find_all(class_="sg-header-heading sg-right")

        h2 = soup.findAll('a', {"class": ["sg-header-heading"]})
    else:
        with open(f'static/payloads/{quarter}.json', 'r') as file:
            json_str = file.read()
        json_obj = json.loads(json_str)

        specific_quarter = session_requests.post(urls, data=json_obj,headers=dict(referer=urls))
        
        soup = BeautifulSoup(specific_quarter.text, "html.parser")

        h1 = soup.find_all(class_="sg-header-heading sg-right")

        h2 = soup.findAll('a', {"class": ["sg-header-heading"]})

    return h1, h2
def getTime():
    my_date = datetime.now(pytz.timezone('US/Central'))
    return my_date.strftime("%m/%d/%Y %I:%M:%S %p")
