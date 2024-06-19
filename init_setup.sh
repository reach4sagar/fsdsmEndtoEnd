echo [$(date)]: "START"

echo [$(date)]: "Creating new pythong environment with 3.8 version"

conda create --prefix  ./env python=3.8 -y

echo [$(date)]: "Activating enviornment"

source activate ./env

echo [$(date)]: "Installing requirements.txt"

pip install -r requirements.txt

echo [$(date)]: "END"