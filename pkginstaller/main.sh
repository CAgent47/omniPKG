#!/bin/bash
set -euo pipefail
python3 core/createJson.py
# eval $(python3 core/updatePKG.py)
eval $(python3 core/installPKG.py) cowsay
# Created By CAgent_47