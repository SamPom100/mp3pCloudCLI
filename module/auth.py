import requests, os, sys
from . import constants

def generate_auth_code():
    url = f"https://api.pcloud.com/userinfo?getauth=1&username={constants.username}&password={constants.password}"
    response = requests.request("GET", url)
    if "error" in response.json():
        print(response.json())
        print("[Auth] - Error generating auth code. Bad credentials.")
        sys.exit(1)
    auth_code = response.json().get("auth")
    print("[Auth] - Generated a new auth code")
    return auth_code

def save_auth_code(auth_code):
    file_path = __get_filepath()
    with open(file_path, "w") as f:
        f.write(auth_code)
    
def get_auth_code():
    file_path = __get_filepath()
    with open(file_path, "r") as f:
        return f.read()
    
def __get_filepath():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = "auth_code.txt"
    file_path = os.path.join(script_dir, filename)

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")
    
    return file_path