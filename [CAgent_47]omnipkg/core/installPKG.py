import shutil
import json

with open('core/distroPKG.json', 'r') as installDetect:
    detectSyntax = json.load(installDetect)

for key, syntax in detectSyntax.items():
    if shutil.which(key):
        SyntaxInstallDetect = key
        break

print(detectSyntax[SyntaxInstallDetect]["install"])