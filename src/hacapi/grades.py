from colorama import Fore
from . import session
from bs4 import BeautifulSoup
import json
import pandas as pd

def returnHTML():
    urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"

    session_requests = session.session_requests

    result = session_requests.get(urls, headers=dict(referer=urls))

    soup = BeautifulSoup(result.text, "html.parser")

    grades_html = soup.find_all(class_="sg-header-heading sg-right")

    name_html = soup.findAll('a', {"class": ["sg-header-heading"]})

    return grades_html, name_html


def initializeClasses(grades_html, names_html):
    class1 = 0
    try:
        class1 = str(grades_html[0])
        class1 = class1[116:121]
    except IndexError:
        print("Enter a valid six digit Student ID and password!")
        exit(0)

    class2 = "0"
    try:
        class2 = str(grades_html[1])
        class2 = class2[116:121]
        if class2 == "":
            class2 = "0"
    except IndexError:
        pass

    class3 = "0"
    try:
        class3 = str(grades_html[2])
        class3 = class3[116:121]
        if class3 == "":
            class3 = "0"
    except IndexError:
        pass

    class4 = "0"
    try:
        class4 = str(grades_html[3])
        class4 = class4[116:121]
        if class4 == "":
            class4 = "0"
    except IndexError:
        pass

    class5 = "0"
    try:
        class5 = str(grades_html[4])
        class5 = class5[116:121]
        if class5 == "":
            class5 = "0"
    except IndexError:
        pass

    class6 = "0"
    try:
        class6 = str(grades_html[5])
        class6 = class6[116:121]
        if class6 == "":
            class6 = "0"
    except IndexError:
        pass

    class7 = "0"
    try:
        class7 = str(grades_html[6])
        class7 = class7[116:121]
        if class7 == "":
            class7 = "0"
    except IndexError:
        pass

    class8 = "0"
    try:
        class8 = str(grades_html[7])
        class8 = class8[116:121]
        if class8 == "":
            class8 = "0"
    except IndexError:
        pass

    class_name_1 = "No class"
    try:
        class_name_1 = (str(names_html[0].text)).strip()
        index_of_deletion = class_name_1.index("-")
        class_name_1 = (class_name_1[index_of_deletion + 4:]).strip()
    except IndexError:
        pass

    class_name_2 = "No class"
    try:
        class_name_2 = (str(names_html[1].text)).strip()
        index_of_deletion = class_name_2.index("-")
        class_name_2 = (class_name_2[index_of_deletion + 4:]).strip()
    except IndexError:
        pass

    class_name_3 = "No class"
    try:
        class_name_3 = (str(names_html[2].text)).strip()
        index_of_deletion = class_name_3.index("-")
        class_name_3 = (class_name_3[index_of_deletion + 4:]).strip()
    except IndexError:
        pass

    class_name_4 = "No class"
    try:
        class_name_4 = (str(names_html[3].text)).strip()
        index_of_deletion = class_name_4.index("-")
        class_name_4 = (class_name_4[index_of_deletion + 4:]).strip()
    except IndexError:
        pass
    class_name_5 = "No class"
    try:
        class_name_5 = (str(names_html[4].text)).strip()
        dash_index = class_name_5.index("-")
        class_name_5 = (class_name_5[dash_index + 4:]).strip()
    except IndexError:
        pass

    class_name_6 = "No class"
    try:
        class_name_6 = (str(names_html[5].text)).strip()
        dash_index = class_name_6.index("-")
        class_name_6 = (class_name_6[dash_index + 4:]).strip()
    except IndexError:
        pass

    class_name_7 = "No class"
    try:
        class_name_7 = (str(names_html[6].text)).strip()
        dash_index = class_name_7.index("-")
        class_name_7 = (class_name_7[dash_index + 4:]).strip()
    except IndexError:
        pass

    class_name_8 = "No class"
    try:
        class_name_8 = (str(names_html[7].text)).strip()
        dash_index = class_name_8.index("-")
        class_name_8 = (class_name_8[dash_index + 4:]).strip()
    except IndexError:
        pass

    return [class_name_1, class_name_2, class_name_3, class_name_4, class_name_5, class_name_6, class_name_7,
            class_name_8], [class1, class2, class3, class4, class5, class6, class7, class8]


def returnCurrentGrades():
    # Creates a session to maintain credentials

    session.return_to_current()

    html = returnHTML()

    grades_html = html[0]
    name_html = html[1]

    classes = initializeClasses(grades_html, name_html)

    class_names = classes[0]
    class_grades = classes[1]
    
    try:
        class_grades_ = [i.replace("%", "") for i in class_grades]
    except:
        class_grades_ = 0
        print("FAILIURE")

    class_grades = []    
    for i in class_grades_: # type: ignore
        try:
            class_grades.append(float(i))
        except:
            print("\n" + Fore.RED + "ERROR: " + Fore.RESET + "Could not convert " + i + " to a float." + "\n")
            class_grades.append(float(0))
    
    names_ = []
    grades_ = []

    for i in range(len(class_names)):

        names_.append(class_names[i])
        grades_.append(class_grades[i])

    return (names_, grades_)
def returnQuarterGrade(quarter):
    session_requests = session.session_requests
    
    urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"
            
    with open(f'payloads/{quarter}.json', 'r') as file:
        json_str = file.read()
    json_obj = json.loads(json_str)

    specific_quarter = session_requests.post(urls, data=json_obj,headers=dict(referer=urls))

    soup = BeautifulSoup(specific_quarter.text, "html.parser")

    grades_html = soup.find_all(class_="sg-header-heading sg-right")

    name_html = soup.findAll('a', {"class": ["sg-header-heading"]})

    classes = initializeClasses(grades_html, name_html)

    class_names = classes[0]
    class_grades = classes[1]

    try:
        class_grades_ = [i.replace("%", "") for i in class_grades]
    except:
        class_grades_ = 0
        print("FAILIURE")

    class_grades = []    
    for i in class_grades_: # type: ignore
        try:
            class_grades.append(float(i))
        except:
            print("\n" + Fore.RED + "ERROR: " + Fore.RESET + "Could not convert " + i + " to a float." + "\n")
            class_grades.append(float(0))
    
    names_ = []
    grades_ = []

    for i in range(len(class_names)):

        names_.append(class_names[i])
        grades_.append(class_grades[i])

    return (names_, grades_)