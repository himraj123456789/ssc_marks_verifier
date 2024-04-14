import streamlit as st

# Streamlit code goes here
st.write("Hello, World!")





from bs4 import BeautifulSoup
import requests

#URL ="https://ssc.digialm.com//per/g27/pub/2207/touchstone/AssessmentQPHTMLMode1//2207O2258/2207O2258S24D305873/16552731167542966/3201602995_2207O2258S24D305873E1.html#"
#URL="https://ssc.digialm.com//per/g27/pub/2207/touchstone/AssessmentQPHTMLMode1//2207O2258/2207O2258S24D305873/16552731127036548/3201603059_2207O2258S24D305873E1.html"
#URL="https://ssc.digialm.com//per/g27/pub/2207/touchstone/AssessmentQPHTMLMode1//2207O2258/2207O2258S12D237246/16552735052315268/3201601766_2207O2258S12D237246E1.html"
URL="https://ssc.digialm.com//per/g27/pub/2207/touchstone/AssessmentQPHTMLMode1//2207O2258/2207O2258S52D342010/16552561125634920/3201007443_2207O2258S52D342010E1.html"

r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

counter=0
correct_ans=[]
for name in soup.find_all("td", class_="rightAns"):
    salary = name.parent.find_all('td')[-1]  # last cell in the row
    data=name.get_text()[0]
    correct_ans.append(data)
    counter=counter+1
    

# Your answer 
m=0
counter1=0
your_answer=[]
for name in soup.find_all("td", class_="bold"):
    
    #time.sleep(1)
    
    if(m==5):
        your_answer.append(name.get_text())
        m=0
        counter1=counter1+1

    else:
        
        m=m+1



marks=0
mk=0
for i in range(0,len(correct_ans)):

    if(correct_ans[i]==your_answer[i]):
        marks=marks+2
        #mk=mk+1
    if(correct_ans[i]!=your_answer[i] and your_answer[i]!=' -- '):
        marks=marks-0.5
        mk=mk+1
print("-----------------",mk)
print("your marks is   --->   ",marks)
print(correct_ans)
print(your_answer)

st.write(your_answer)


st.write("-----------------",mk)

















