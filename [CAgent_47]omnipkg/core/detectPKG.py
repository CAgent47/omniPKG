import shutil
import omnimadule

Dist = omnimadule.loadJson('core/distroPKG.json')

UserDIST = omnimadule.loopInDICT(Dist)

Selected_Dist = omnimadule.loadJson('core/packages.json')

for key, pkg in Selected_Dist.items():
    if shutil.which(key):
        if key == UserDIST:
            packages_for_install = pkg
            break

for pkg in packages_for_install:
    print(pkg)