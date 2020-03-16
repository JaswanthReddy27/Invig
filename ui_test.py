from selenium import webdriver
import time
import sys


def load(i,cur):
    print("loading "+order[i]+" -> "+order[i+1],end=" ")

    while(driver.current_url==cur):
        print(".",end=" ")
        
        time.sleep(0.5)
    print("Test Passed")

old_stdout = sys.stdout

log_file = open("message.log","w")

sys.stdout = log_file




EXE_PATH = 'E:\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=EXE_PATH)
#abcd="https://jaswanthreddy27.github.io/Invig/"
abcd="http://localhost//Software2/"

order=['login.html','admins.html','view.html','admin_home.html','view.html', 'exams.html','notify.html','login.html','loginhm.html','profile.html','loginhm.html','notify.html','login.html']
i=0
cur=abcd+order[i]
driver.get(cur)
un="cb.tc.3"
password="Rammohan1"



print("Admin Login")
#login ->admin
cur=abcd+order[i]
email_field = driver.find_element_by_id('un')
email_field.send_keys("cb.tc.ad")

password_field = driver.find_element_by_id('pass')
password_field.send_keys("side")

login = driver.find_element_by_id('sub').click()
load(i,cur)
i+=1

#Admin -> view
time.sleep(3)
cur=abcd+order[i]
view = driver.find_element_by_id('vieww').click()
load(i,cur)
i+=1

#view -> admin_home
time.sleep(3)
cur=abcd+order[i]
faculty = driver.find_element_by_id('facc').click()
load(i,cur)
i+=1

#admin_home to view
time.sleep(3)
cur=abcd+order[i]
upper = driver.find_element_by_id('upper').click()
time.sleep(2)
home = driver.find_element_by_id('backk').click()
load(i,cur)
i+=1

#view to exam
time.sleep(3)
cur=abcd+order[i]
faculty = driver.find_element_by_id('exmm').click()
load(i,cur)
i+=1


#exam 
time.sleep(3)
cur=abcd+order[i]
faculty = driver.find_element_by_id('opp').click()
time.sleep(2)
faculty = driver.find_element_by_id('close').click()
time.sleep(3)

#exam to notify
upper = driver.find_element_by_id('upper').click()
time.sleep(2)
home = driver.find_element_by_id('notifyy').click()
load(i,cur)
i+=1


#notify
time.sleep(3)


#notify to logout
upper = driver.find_element_by_id('upper').click()
time.sleep(2)
home = driver.find_element_by_id('logout').click()
load(i,cur)
i+=1


print("\nUser Login...Overview")

#login -> homepage
email_field = driver.find_element_by_id('un')
email_field.send_keys(un)


password_field = driver.find_element_by_id('pass')
password_field.send_keys(password)

login = driver.find_element_by_id('sub').click()
load(i,cur)

i+=1

#homepage -> profile
cur=abcd+order[i]
time.sleep(2)
profile = driver.find_element_by_id('profilee').click()
load(i,cur)
i+=1





#profile -> homepage
cur=abcd+order[i]
time.sleep(3)
upper = driver.find_element_by_id('upper').click()
time.sleep(1)
home = driver.find_element_by_id('homee').click()
load(i,cur)
i+=1

#homepage -> notify
cur=abcd+order[i]
notifyy = driver.find_element_by_id('notifyy').click()
load(i,cur)
i+=1

#notify -> login
cur=abcd+order[i]
time.sleep(3)
upper = driver.find_element_by_id('upper').click()
time.sleep(1)
home = driver.find_element_by_id('logout').click()
load(i,cur)
i+=1


sys.stdout = old_stdout

log_file.close()

time.sleep(2)
driver.close()