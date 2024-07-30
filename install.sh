#!/bin/bash




install_python() {
    echo "Installing Python..."
    pkg update -y || { echo "Failed to update packages. Exiting."; exit 1; }
    pkg install python -y || { echo "Failed to install Python. Exiting."; exit 1; }
    pkg install python-pip -y || { echo "Failed to install Python. Exiting."; exit 1; }
}

install_git() {
    echo "Installing Git..."
    pkg install git -y || { echo "Failed to install Git. Exiting."; exit 1; }
    pkg install python git -y || { echo "Failed to install Git Python. Exiting."; exit 1; }
}

install_wget() {
    echo "Installing wget..."
    pkg install wget -y || { echo "Failed to install wget. Exiting."; exit 1; }
}

install_curl() {
    echo "Installing curl..."
    pkg install curl -y || { echo "Failed to install curl. Exiting."; exit 1; }
}



if ! command -v python || ! command -v pip; then
    install_python
fi

if ! command -v git; then
    install_git
fi

if ! command -v wget; then
    install_wget
fi

if ! command -v curl; then
    install_curl
fi
if [ -f Cfscanner-pre.py ]; then
    first_line=$(head -n 1 Cfscanner-pre.py)
    if [ "$first_line" != "V=1" ]; then
        rm Cfscanner-pre.py
        echo "Updating Cfscanner-pre.py..."
        curl -fsSL -o Cfscanner-pre.py https://raw.githubusercontent.com/arshiacomplus/WarpScanner/main/Cfscanner-pre.py || { echo \"Failed to download Cfscanner-pre.py. Exiting.\"; exit 1; }
        
        python Cfscanner-pre.py
        exit 0
    else
        python Cfscanner-pre.py
        exit 0
    fi
fi

echo "install Cfscanner-pre.py"
curl -fsSL -o Cfscanner-pre.py https://raw.githubusercontent.com/arshiacomplus/WarpScanner/main/Cfscanner-pre.py || { echo \"Failed to download Cfscanner-pre.py. Exiting.\"; exit 1; }
python Cfscanner-pre.py
