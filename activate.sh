#!/bin/bash
# Activate virtual environment and set up aliases
source .venv/Scripts/activate

# Create aliases to bypass Windows App Execution Aliases
alias python='C:/Users/pt971/code/db/.venv/Scripts/python.exe'
alias pip='C:/Users/pt971/code/db/.venv/Scripts/pip.exe'

# Export PATH with virtual environment first
export PATH="C:/Users/pt971/code/db/.venv/Scripts:$PATH"

echo "Virtual environment activated!"
echo "Python: $(which python 2>/dev/null || echo 'C:/Users/pt971/code/db/.venv/Scripts/python.exe')"