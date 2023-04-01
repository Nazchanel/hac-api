from login import login, getTime
import requests
from colorama import Fore

def initializeClasses(a, b):
    class1 = 0
    try:
        class1 = str(a[0])
        class1 = class1[116:121]
    except IndexError:
        print("Enter a valid six digit Student ID and password!")
        exit(0)

    class2 = "0"
    try:
        class2 = str(a[1])
        class2 = class2[116:121]
        if class2 == "":
            class2 = "0"
    except IndexError:
        pass

    class3 = "0"
    try:
        class3 = str(a[2])
        class3 = class3[116:121]
        if class3 == "":
            class3 = "0"
    except IndexError:
        pass

    class4 = "0"
    try:
        class4 = str(a[3])
        class4 = class4[116:121]
        if class4 == "":
            class4 = "0"
    except IndexError:
        pass

    class5 = "0"
    try:
        class5 = str(a[4])
        class5 = class5[116:121]
        if class5 == "":
            class5 = "0"
    except IndexError:
        pass

    class6 = "0"
    try:
        class6 = str(a[5])
        class6 = class6[116:121]
        if class6 == "":
            class6 = "0"
    except IndexError:
        pass

    class7 = "0"
    try:
        class7 = str(a[6])
        class7 = class7[116:121]
        if class7 == "":
            class7 = "0"
    except IndexError:
        pass

    class8 = "0"
    try:
        class8 = str(a[7])
        class8 = class8[116:121]
        if class8 == "":
            class8 = "0"
    except IndexError:
        pass

    class_name_1 = "No class"
    try:
        class_name_1 = (str(b[0].text)).strip()
        index_of_deletion = class_name_1.index("-")
        class_name_1 = (class_name_1[index_of_deletion + 4:]).strip()
    except IndexError:
        pass

    class_name_2 = "No class"
    try:
        class_name_2 = (str(b[1].text)).strip()
        index_of_deletion = class_name_2.index("-")
        class_name_2 = (class_name_2[index_of_deletion + 4:]).strip()
    except IndexError:
        pass

    class_name_3 = "No class"
    try:
        class_name_3 = (str(b[2].text)).strip()
        index_of_deletion = class_name_3.index("-")
        class_name_3 = (class_name_3[index_of_deletion + 4:]).strip()
    except IndexError:
        pass

    class_name_4 = "No class"
    try:
        class_name_4 = (str(b[3].text)).strip()
        index_of_deletion = class_name_4.index("-")
        class_name_4 = (class_name_4[index_of_deletion + 4:]).strip()
    except IndexError:
        pass
    class_name_5 = "No class"
    try:
        class_name_5 = (str(b[4].text)).strip()
        dash_index = class_name_5.index("-")
        class_name_5 = (class_name_5[dash_index + 4:]).strip()
    except IndexError:
        pass

    class_name_6 = "No class"
    try:
        class_name_6 = (str(b[5].text)).strip()
        dash_index = class_name_6.index("-")
        class_name_6 = (class_name_6[dash_index + 4:]).strip()
    except IndexError:
        pass

    class_name_7 = "No class"
    try:
        class_name_7 = (str(b[6].text)).strip()
        dash_index = class_name_7.index("-")
        class_name_7 = (class_name_7[dash_index + 4:]).strip()
    except IndexError:
        pass

    class_name_8 = "No class"
    try:
        class_name_8 = (str(b[7].text)).strip()
        dash_index = class_name_8.index("-")
        class_name_8 = (class_name_8[dash_index + 4:]).strip()
    except IndexError:
        pass

    return [class_name_1, class_name_2, class_name_3, class_name_4, class_name_5, class_name_6, class_name_7,
            class_name_8], [class1, class2, class3, class4, class5, class6, class7, class8]
def returnGrades(usr, pswd, dly, quarter):
# Creates a session to maintain credentials
    session_requests = requests.session()

    current_time = getTime()

    username = usr
    password = pswd

    # Will be in use for checking
    delay = dly

    login_url = 'https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f'

    html = login(session_requests, login_url, password, username, quarter=quarter)
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

    return (names_, grades_, current_time)