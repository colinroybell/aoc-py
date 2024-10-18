To set up (from basic WSL)

Virtual environment:

sudo apt-get update
sudo apt-get install python3-venv
python3 -m venv .venv
source .venv/bin/activate

Install package:

pip install -e .
pip install pytest
pip install pytest-xdist
pip install pytest-timeout --timeout=300 (seconds)
# and need smypy and others

pytest -n 10 runs in parallel
pytest --durations 10 for speed.

Black

sudo apt install black


# Notes

pytest xfail is usual semantic for a test that is expected to fail, so think I'm fine at the minute for regressions. Having a pass for bringup tests is 