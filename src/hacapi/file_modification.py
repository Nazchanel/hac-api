
import json
import pandas as pd
import requests
from lxml import html

def clear_files():
    for i in range(9):
        name = f"class{i}.html"
        f = open(f"templates/{name}", "w")
        f.write("")
        f.close()
def returnGradeTables(username, password, logged_in, quarter):
  login_url = 'https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f'

  session_requests = requests.session()

  urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"

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

  # Logs in
  session_requests.post(login_url, data=login_payload, headers=dict(referer=login_url))

  initial_html = session_requests.get(urls, headers=dict(referer=urls))

  if logged_in:
    with open(f'static/payloads/{quarter}.json', 'r') as file:
        json_str = file.read()
    json_obj = json.loads(json_str)

    specific_quarter = session_requests.post(urls, data=json_obj,headers=dict(referer=urls))
    df = pd.read_html(specific_quarter.text)
  else:
      result = session_requests.get(urls, headers=dict(referer=urls))
      df = pd.read_html(result.text)
  
  index_list = []
  for i in range(len(df)):
      if len(df[i].columns) == 10:
          index_list.append(i)
  
  j = 1
  for i in index_list:
      name = f"class{j}.html"
      f = open(f"templates/{name}", "w")
      f.write(df[i].to_html())
      f.close()
      j+=1