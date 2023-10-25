import requests
from lxml import html
from bs4 import BeautifulSoup
# from . 
import payloads  # Assuming payloads module exists in the same directory.
import pandas as pd
import re


class Account:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session_requests = requests.session()

        login_url = 'https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f'
        result = self.session_requests.get(login_url)
        tree = html.fromstring(result.text)
        authenticity_token = list(set(tree.xpath("//input[@name='__RequestVerificationToken']/@value")))[0]
    
        self.login_payload = {
            "VerificationOption": "UsernamePassword",
            "Database": "10",
            "LogOnDetails.Password": password,
            "__RequestVerificationToken": authenticity_token,
            "LogOnDetails.UserName": username
        }
        self.session_requests.post(login_url, data=self.login_payload, headers=dict(referer=login_url))
        
    def reset(self):
        self.__init__(self.username, self.password)

    # Function that only works internally and not meant to be accessed by the user
    def _initialize_classes(self, grades_html, names_html):
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
    def return_current_grades(self):
        # Creates a session to maintain credentials
        self.return_to_current()
        html_data = self._return_html(quarter=None)

        grades_html = html_data[0]
        name_html = html_data[1]

        classes = self._initialize_classes(grades_html, name_html)

        class_names = classes[0]
        class_grades = classes[1]

        class_grades_ = [i.replace("%", "") for i in class_grades]
        class_grades = []
        for i in class_grades_:
            try:
                class_grades.append(float(i))
            except ValueError:
                print("\n" + "ERROR: Could not convert " + i + " to a float." + "\n")
                class_grades.append(float(0))

        names_ = []
        grades_ = []

        for i in range(len(class_names)):
            names_.append(class_names[i])
            grades_.append(class_grades[i])

        return names_, grades_

    def return_quarter_grade(self, quarter):
        # Work Here
        # Creates a session to maintain credentials

        html_data = self._return_html(quarter= quarter)
        print(html_data)

        grades_html = html_data[0]
        name_html = html_data[1]

        classes = self._initialize_classes(grades_html, name_html)

        class_names = classes[0]
        class_grades = classes[1]

        class_grades_ = [i.replace("%", "") for i in class_grades]
        class_grades = []
        for i in class_grades_:
            try:
                class_grades.append(float(i))
            except ValueError:
                print("\n" + "ERROR: Could not convert " + i + " to a float." + "\n")
                class_grades.append(float(0))

        names_ = []
        grades_ = []

        for i in range(len(class_names)):
            names_.append(class_names[i])
            grades_.append(class_grades[i])

        return names_, grades_

    def _return_html(self, quarter):
        urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"

        if quarter is None:
            result = self.session_requests.get(urls, headers=dict(referer=urls))
            soup = BeautifulSoup(result.text, "html.parser")

            grades_html = soup.find_all(class_="sg-header-heading sg-right")
            name_html = soup.findAll('a', {"class": ["sg-header-heading"]})

            return grades_html, name_html
        else:
            if quarter == 1:
                json_obj = payloads.payload1
            elif quarter == 2:
                json_obj = payloads.payload2
            elif json_obj == 3:
                json_obj = payloads.payload3
            else:
                json_obj = payloads.payload4
            
            specific_quarter = session_requests.post(urls, data=json_obj,headers=dict(referer=urls))
            
            soup = BeautifulSoup(specific_quarter.text, "html.parser")

            h1 = soup.find_all(class_="sg-header-heading sg-right")

            h2 = soup.findAll('a', {"class": ["sg-header-heading"]})


    def return_to_current(self):
        urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"
        self.session_requests.get(urls, headers=dict(referer=urls))
    
    def return_quarter_assignments_html(self, quarter):

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

        specific_quarter = self.session_requests.post(urls, data=payload, headers=dict(referer=urls))

        df = pd.read_html(specific_quarter.text)
        index_list = []

        for i in range(len(df)):
            if len(df[i].columns) == 10:
                index_list.append(i)

        html_list = []

        for i in index_list:
            html_list.append(df[i].to_html())

        return html_list


    def return_quarter_assignments_df(self, quarter):

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

        specific_quarter = self.session_requests.post(urls, data=payload, headers=dict(referer=urls))
        df = pd.read_html(specific_quarter.text)

        index_list = []
        df_list = []

        for i in range(len(df)):
            if len(df[i].columns) == 10:
                index_list.append(i)

        for i in index_list:
            df_list.append(df[i])

        return df_list


    def return_current_assignments_df(self):
        self.return_to_current()

        urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"

        result = self.session_requests.get(urls, headers=dict(referer=urls))
        df = pd.read_html(result.text)

        index_list = []
        df_list = []

        for i in range(len(df)):
            if len(df[i].columns) == 10:
                index_list.append(i)

        for i in index_list:
            df_list.append(df[i])

        return df_list


    def return_current_assignments_html(self):
        self.return_to_current()

        urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"

        result = self.session_requests.get(urls, headers=dict(referer=urls))
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
    def return_weighted_gpa(self):
        
        urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Transcript.aspx"
        
        result = self.session_requests.get(urls, headers=dict(referer=urls))
        print("result achieved")
        gpa = ""
        # Read HTML content from the file

        html_content = result.text

        soup = BeautifulSoup(html_content, "html.parser")

        # Find the table with the specified ID
        target_table = soup.find("table", {"id": "plnMain_rpTranscriptGroup_tblCumGPAInfo"})

        # If the table is found, find the span within the table
        if target_table:
            target_span = target_table.find("span", {"id": "plnMain_rpTranscriptGroup_lblGPACum1"})
            
            # If the span is found, extract the text content and save it to the variable "gpa"
            gpa = target_span.text.strip()
       
        return float(gpa)


    def return_college_gpa(self):
        
        urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Transcript.aspx"
        
        result = self.session_requests.get(urls, headers=dict(referer=urls))
        
        print("result achieved")

        gpa = ""
        # Read HTML content from the file

        html_content = result.text

        soup = BeautifulSoup(html_content, "html.parser")

        # Find the table with the specified ID
        target_table = soup.find("table", {"id": "plnMain_rpTranscriptGroup_tblCumGPAInfo"})

        # If the table is found, find the span within the table
        if target_table:
            target_span = target_table.find("span", {"id": "plnMain_rpTranscriptGroup_lblGPACum2"})
            
            # If the span is found, extract the text content and save it to the variable "gpa"
            gpa = target_span.text.strip()
       
        return float(gpa)

    def quarter_test(quarter):


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


    def get_username(self):
        return self.username
