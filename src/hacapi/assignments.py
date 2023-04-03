import pandas as pd
from . import session
from . import payloads

def returnQuarterAssignmentsHTML(quarter):
    session_requests = session.session_requests
    
    urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"
        
    initial_html = session_requests.get(urls, headers=dict(referer=urls))
    
    payload = {}

    if quarter == 1:
        payload = payloads.payload1
    elif quarter == 2:
       payload = payloads.payload2
    elif quarter == 3:
        payload = payloads.payload3
    elif quarter == 4:
      payload = payloads.payload4

    specific_quarter = session_requests.post(urls, data=payload,headers=dict(referer=urls))

    df = pd.read_html(specific_quarter.text)    
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
      
    payload = {}
    if quarter == 1:
        payload = payloads.payload1
    elif quarter == 2:
       payload = payloads.payload2
    elif quarter == 3:
        payload = payloads.payload3
    elif quarter == 4:
      payload = payloads.payload4

    specific_quarter = session_requests.post(urls, data=payload,headers=dict(referer=urls))
    df = pd.read_html(specific_quarter.text)

    index_list = []
    df_list = []

    for i in range(len(df)):
      if len(df[i].columns) == 10:
          index_list.append(i)

    for i in index_list:
      df_list.append(df[i])

    return df_list

def returnCurrentAssignmentsDataFrame():
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
def returnCurrentAssignmentsHTML():
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

    html_list = []

    for i in index_list:
      html_list.append(df[i].to_html())

    return html_list
