import os
import json

from langchain_openai import ChatOpenAI

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagePlaceHolder
)

from langchain_core.chat_history import(
    BaseChatMessageHistory  #parent class 
)

from langchain_core_messages import (
    message_to_dict, #serialization -- converting message object to dict 
    messages_from_dict #desrialzation-- converting dict to Langchain messages object
)

from langchain_core.runnables.history import(
    RunnableWithMessageHistory
)


#1.  Storage configuration
USERS_FILE = "users.json"  #users json file name

HISTORY_FOLDER ="chat_history"  #directory name

os.makedirs(  #make directory
    HISTORY_FOLDER, 
    exists_ok = True #checks if folder exits, if no then creates it
)


#2. Load Users
def load_users():
    if not os.path.exists(USERS_FILE): #os.path will check the current working directoy + HISTORY_FOLDER.
        return {}   #if does not exists, then return empty dict

    with open(USERS_FILE,"r") as file:  # else open the file in read mode. When we use with open() , we no need to close the file explicitly, It will closed automatically
        return json.load(file) #load()  will convert the json to dict 

#3. Save Users
def save_users(users){
    with open(USERS_FILE , "w") as file:
        json.dump(users, file,indent =2)

#4. User signup
def signup(users):
    print("\n  --- SIGN UP ----")
    name = input("Enter name:  ").strip()
    username = input("Enter username :  ").strip().lower()
    password = input("Enter password : ")

    if not name or not username or not password :
        print("All fields are required")
        return

    if not username.replace("_","").isalnum():
        print("Use only numbers, alphabets and _ ")
        return

    if(username in users)
        print("Username already exists")

    users[username] = {
        "name" : name
        "password" : password
    }

    save_users(users)

    print("Sign up successful")
}

#5. Login 
def login(users):
    print("\n ---- Login ----")
    username = input("Enter the username:  ").strip().lower()
    password = input("Enter the password:  ")

    if username not in users:
        print("Invalid username")
        return None
    
    if(users[username]["password"]) == password:
        print("Login successful!!!")
        return username
    
    print("Incorrect password")
    return None

#6. File Chat Message History
class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id):
        self.file_path = os.path.join(
            HISTORY_FOLDER,
            session_id + ".json"
        )
    
    #Read chat history
    @property 
    def messages(self)
    