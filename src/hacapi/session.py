# Used to save a common session to speed up the process of logging in and accessing information in HAC

import requests
from lxml import html

session_requests = requests.session()


def session_init(username, password):
    global session_requests

    login_url = 'https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f'

    result = session_requests.get(login_url)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='__RequestVerificationToken']/@value")))[0]

    login_payload = {
        "VerificationOption": "UsernamePassword",
        "Database": "10",
        "LogOnDetails.Password": password,
        "__RequestVerificationToken": authenticity_token,
        "LogOnDetails.UserName": username
    }
    session_requests.post(login_url, data=login_payload, headers=dict(referer=login_url))

    
def reset_session():
    global session_requests

    session_requests = requests.session()


def return_to_current():
    global session_requests

    urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"

    session_requests.get(urls, headers=dict(referer=urls))

