import shutil
import json

with open('core/distroPKG.json', 'r') as Dtect:
    Dist = json.load(Dtect)

for key, value in Dist.items():
    if shutil.which(key):
        UserDIST = key
        break

with open('core/packages.json', 'r') as Select:
    Selected_Dist = json.load(Select)

for key, pkg in Selected_Dist.items():
    if shutil.which(key):
        if key == UserDIST:
            packages_for_install = pkg
            break

for pkg in packages_for_install:
    print(pkg)