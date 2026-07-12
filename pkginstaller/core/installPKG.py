import shutil
import json

def setPackageManager(manager):
    if shutil.which(manager):
        return manager

pkg_Managers = None

user_package_Manager = None

def usePkgManager(managers):
    global user_package_Manager
    for pm in managers:
        if setPackageManager(pm):
            user_package_Manager = pm
            break

usePkgManager(pkg_Managers)
system_Package_Manager = user_package_Manager
print(system_Package_Manager)