from . import session
import pandas as pd
import re


def return_weighted_gpa():
    session_requests = session.session_requests
    urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Transcript.aspx"

    result = session_requests.get(urls, headers=dict(referer=urls))

    df = pd.read_html(result.text)

    gpa_text = df[0].loc[3, 0]

    # Define a regular expression pattern to match the Weighted GPA
    pattern = r'Weighted GPA\s+(\d+\.\d+)'
    # Use re.search() to find the first occurrence of the pattern in the string
    match = re.search(pattern, gpa_text)
    # If a match was found, return the Weighted GPA as a float; otherwise, return None
    return float(match.group(1)) if match else None


def return_college_gpa():
    session_requests = session.session_requests

    urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Transcript.aspx"

    result = session_requests.get(urls, headers=dict(referer=urls))

    df = pd.read_html(result.text)

    gpa_text = df[0].loc[3, 0]
    pattern = r'College GPA\s+(\d+\.\d+)'
    match = re.search(pattern, gpa_text)
    if match:
        return float(match.group(1))
    else:
        return None
