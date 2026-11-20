#!/bin/bash

if command -v jq &> /dev/null; then

    JSON_FILE="core/prereqisite.json"

    # root OR user
    if [ "$(id -u)" -eq 0 ]; then
        MODE="root"
    else
        MODE="sudo"
    fi

    for pm in $(jq -r 'keys[]' "$JSON_FILE"); do
        if ! command -v "$pm" >/dev/null 2>&1; then
            continue
        fi

        cmd=$(jq -r --arg pm "$pm" --arg mode "$MODE" '.[$pm][$mode].prereqisite' "$JSON_FILE")

        echo ">>> $pm detect shod. Ejra: $cmd"
        bash -c "$cmd"
        break
    done
else
    echo "[ ERROR ]: Please Install <jq> In your system and try again!"
    exit 1
fi