#!/bin/bash -eu

mkdir -p "$1/$2"
case "$2" in
    python)
        cp template.py "$1/$2/AoC_${1}a.py"
        ;;
    *)
        echo "eh?"
        ;;
esac
