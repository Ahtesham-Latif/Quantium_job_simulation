#!/bin/bash

# 1. Navigate to the project directory (optional but safe)
# cd "$(dirname "$0")"

# 2. Activate the virtual environment
# Note: On Windows/Git Bash, the path is usually venv/Scripts/activate
source venv/Scripts/activate

# 3. Execute the test suite
pytest test_app.py

# 4. Capture the exit code of the pytest command
# $? stores the exit status of the last executed command
PYTEST_EXIT_CODE=$?

# 5. Return 0 if passed, 1 if failed
if [ $PYTEST_EXIT_CODE -eq 0 ]; then
    echo "Tests passed successfully! Exit code: 0"
    exit 0
else
    echo "Tests failed. Exit code: 1"
    exit 1
fi