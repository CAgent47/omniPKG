#!/bin/bash
set -euo pipefail
INSTALL=$(python3 core/installPKG.py)
UPDATE=$(python3 core/updatePKG.py)
CREATE_JSON=$(python3 core/createJson.py)
# Created By CAgent_47
