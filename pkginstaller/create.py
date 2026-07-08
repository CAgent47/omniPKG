import os
import json

pkg_List = {
    "project": "Linux Package installer (Debian Based Distro)",
    "author": "CAgent_47",
	"GitHub": "https://github.com/CAgent47",
	"LinkedIn": "https://www.linkedin.com/in/mohammad-shaygan-2a96a8387",
	"X": "https://x.com/CAgent_47",


    "Packages": [
        "python3-full",
        "curl",
        "git",
        "ssh",
        "dos2unix",
        "ipython3",
        "libnotify-bin",
	    "unrar",
		"wget",
		"python3-pip",
		"lolcat",
		"fortune",
		"cowsay",
        "btop"
    ]
}

pkg_configuration = "config.json"
def createJsonFile(file, list):
    with open(file, "w") as savePackages:
        json.dump(list, savePackages, indent=4)
    print(" ")
    print("[ Python Message ]: The json file did not exist and was created. Edit the config.json file to edit the installable packages.")
    print(" ")

if not os.path.exists(pkg_configuration):
    createJsonFile(pkg_configuration, pkg_List)
else:
    print("exists")