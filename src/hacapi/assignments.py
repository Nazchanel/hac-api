
import json
import pandas as pd
from . import session

def returnQuarterAssignmentsHTML(quarter):
    session_requests = session.session_requests
    
    urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"
        
    initial_html = session_requests.get(urls, headers=dict(referer=urls))
    
    with open(f'payloads/{quarter}.json', 'r') as file:
        json_str = file.read()
    json_obj = json.loads(json_str)

    specific_quarter = session_requests.post(urls, data=json_obj,headers=dict(referer=urls))

    df = pd.read_html(specific_quarter.text)

    specific_quarter.html = df.to_html()
    
    index_list = []

    for i in range(len(df)):
      if len(df[i].columns) == 10:
          index_list.append(i)
    
    html_list = []

    for i in index_list:
      html_list.append(df[i].to_html())

    return html_list


def returnQuarterAssignmentsDataFrame(quarter):
    session_requests = session.session_requests
    
    urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"
        
    with open(f'payloads/{quarter}.json', 'r') as file:
        json_str = file.read()
    json_obj = json.loads(json_str)

    specific_quarter = session_requests.post(urls, data=json_obj,headers=dict(referer=urls))
    df = pd.read_html(specific_quarter.text)

    index_list = []
    df_list = []

    for i in range(len(df)):
      if len(df[i].columns) == 10:
          index_list.append(i)

    for i in index_list:
      df_list.append(df[i])

    return df_list

def returnCurrentAssignments():
    session_requests = session.session_requests
    session.return_to_current()
    
    urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"

    result = session_requests.get(urls, headers=dict(referer=urls))
    df = pd.read_html(result.text)

    index_list = []
    df_list = []

    for i in range(len(df)):
      if len(df[i].columns) == 10:
          index_list.append(i)

    for i in index_list:
      df_list.append(df[i])

    return df_list 
