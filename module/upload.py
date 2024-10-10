import requests, os
from . import auth, constants

def upload_file(fileName, filePath):
    auth_code = get_active_auth_code()    
    url = f"https://api.pcloud.com/publink/upload?auth={auth_code}&folderid={constants.folder_id}&code={constants.folder_code}"    

    response = requests.request("POST", url, files=[('',(fileName ,open(filePath,'rb'),''))])    
    
    if (response.json().get("result") == 0):
        print("[Upload] - File uploaded successfully")
    else:
        print("[Upload] - Error uploading file. Response: ", response.text)
        return Exception("[Upload] Error uploading file")

def get_active_auth_code(runtimes=0):   
    saved_auth_code = auth.get_auth_code()
    
    if user_is_auth(saved_auth_code):
        return saved_auth_code
    else:
        new_auth_code = auth.generate_auth_code()
        auth.save_auth_code(new_auth_code)
        if runtimes > 2:
            raise Exception("[Auth] Trouble getting new auth code. Check credentials.")
        return get_active_auth_code(runtimes + 1)

def user_is_auth(auth_code):
    response = requests.request("GET", f"https://api.pcloud.com/userinfo?auth={auth_code}")
    if response.text.__contains__("error"):
        return False
    else:
        return True