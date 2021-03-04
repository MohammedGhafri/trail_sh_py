dict =[{'name':'mohd','password':'1234'},{'name':'abed','password':'14'},{'name':'sharaf','password':'5478'},{'name':'thaer','password':'96321'}]

if {'password':'1234','name':'mohd'} in dict:
    print('Exist')
else:
    print('DNE')

import pyautogui as pag
pag.alert(text="Hello World", title="The Hello World Box")