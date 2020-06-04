#!/bin/bash
# Unit test code coverage for SonarQube to cover all modules.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=sftp_class test/unit/sftp_class/sftp_chg_dir.py
coverage run -a --source=sftp_class test/unit/sftp_class/sftp_close_conn.py
coverage run -a --source=sftp_class test/unit/sftp_class/sftp_get_pwd.py
coverage run -a --source=sftp_class test/unit/sftp_class/sftp_init.py
coverage run -a --source=sftp_class test/unit/sftp_class/sftp_open_conn.py
coverage run -a --source=sftp_class test/unit/sftp_class/sftp_put_file.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

