To set up (from basic WSL)

Virtual environment:

sudo apt-get update
sudo apt-get install python3-venv
python3 -m venv .venv
source .venv/bin/activate

Install package:

pip install -e .
pip install pytest

(pytest isn't working - loading wrong python)

Black

sudo apt install black
