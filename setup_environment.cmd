@echo off
setlocal
clear

echo ---------------------------------------------------------
echo 1. Check if Python 3.12 is already accessible via py -3.12
echo ---------------------------------------------------------
echo Checking for Python 3.12...
py -3.12 --version >nul 2>nul

IF ERRORLEVEL 1 (
    echo.
    echo Python 3.12 not found via the "py -3.12" launcher.
    echo Attempting to download and install Python 3.12...
    echo (This requires internet access and typically admin rights)
    echo.

    echo -----------------------------------------------------
    echo 2. Download & install Python 3.12 (example using PowerShell)
    echo    Adjust the installer URL and parameters as needed
    echo -----------------------------------------------------
    powershell -Command "Start-BitsTransfer -Source 'https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe' -Destination 'python-3.12.0-amd64.exe'"
    if NOT EXIST python-3.12.0-amd64.exe (
        echo Failed to download Python 3.12 installer. Exiting...
        exit /b 1
    )

    REM /quiet for silent install
    REM /passive for minimal UI
    start /wait python-3.12.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    REM Check again after installation
    py -3.12 --version >nul 2>nul
    IF ERRORLEVEL 1 (
        echo Python 3.12 installation failed or was not found on PATH.
        echo Please install Python 3.12 manually and rerun this script.
        exit /b 1
    )
)

echo.
echo Python 3.12 found or successfully installed.
echo Creating virtual environment...
py -3.12 -m venv venv

echo ---------------------------------------------------------
echo 3. Activate the virtual environment
echo ---------------------------------------------------------
call venv\Scripts\activate.bat

echo ---------------------------------------------------------
echo 4. Install the requirements
echo ---------------------------------------------------------
python.exe -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo =====================================================
echo Done! The virtual environment "venv" is now active.
echo Installed packages from requirements.txt
echo =====================================================
echo.
echo READ THIS! :)
echo 1. YOU, the user must run the following command:
echo    venv\Scripts\activate
echo    It will activate the venv for you to start working.
echo.
echo 2. Go over the terminal and make sure there aren't any errors, if there are any
echo    notify Yuri so he can resolve those issues! Don't keep it to yourself.
echo.