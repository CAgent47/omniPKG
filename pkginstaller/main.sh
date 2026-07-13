#!/bin/bash
set -euo pipefail
python3 core/createJson.py

eval $(python3 )

if ! command -v jq &> /dev/null; then 
    eval $(python3 core/installPKG.py) jq
fi



# Created By CAgent_47