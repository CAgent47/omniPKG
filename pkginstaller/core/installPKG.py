import shutil
import json

def setPackageManager(manager):
    if shutil.which(manager):
        return manager

user_package_Manager = None

def usePkgManager(managers):
    global user_package_Manager
    for key, Value in managers.items():
        if setPackageManager(key):
            user_package_Manager = key
            break


with open('core/distroPKG.json', 'r') as PackageManager:
    pkg_Managers = json.load(PackageManager)


usePkgManager(pkg_Managers)
print(pkg_Managers[user_package_Manager]["install"])