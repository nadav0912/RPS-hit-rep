#!/bin/bash
set -e  # Exit on error

echo "---------------------------------------------------------"
echo "1. Check if Python 3.12 is accessible via python3.12"
echo "---------------------------------------------------------"
if ! command -v python3.12 &> /dev/null; then
    echo
    echo "Python 3.12 not found."
    echo "Please install Python 3.12 manually (e.g., using pyenv or apt)."
    echo "Automatic download/install is not supported in this script."
    exit 1
fi

echo
echo "Python 3.12 found."
echo "Creating virtual environment..."
python3.12 -m venv venv

echo "---------------------------------------------------------"
echo "2. Activate the virtual environment"
echo "---------------------------------------------------------"
# Activate venv for this script only
source venv/bin/activate

echo "---------------------------------------------------------"
echo "3. Upgrade pip and install requirements"
echo "---------------------------------------------------------"
python -m pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install -r requirements.txt

echo
echo "====================================================="
echo "Done! The virtual environment 'venv' is now ready."
echo "Installed packages from requirements.txt"
echo "====================================================="
echo
echo "READ THIS! :)"
echo "1. To activate the virtual environment in your shell:"
echo "   source venv/bin/activate"
echo
echo "2. In VSCode, select the interpreter:"
echo "   - Ctrl + Shift + P"
echo "   - Type 'Python: Select Interpreter'"
echo "   - Choose the one inside ./venv"
echo
echo "3. Check for any errors above. If you see any,"
echo "   notify Yuri so he can help! Don't keep it to yourself :)"
echo