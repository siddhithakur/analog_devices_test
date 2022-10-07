# analog_devices_test
Python Script to Count number of lines in text files

# Steps to run the file

python linecount.py filepath <--optional file extension-->

# libraries used
<p>os
<p>sys

# Folder structure
  .
├── ...
├── test                    # Test files (alternatively `spec` or `tests`)
│   ├── benchmarks          # Load and stress tests
│   ├── integration         # End-to-end, integration tests (alternatively `e2e`)
│   └── unit                # Unit tests
└── ...
  analog_devices_test
  <p>      |
  <p>     |-testcases
  <p>           | - inner 
  <p>          |     |-  texttext.txt
  <p>           | - newfile1.txt
  <p>           | - hello.py
  <p>      | - linecount.py
  <p>       | - test_linecount.py
        
testcases folder contains dummy files for running unit tests
test_lincount unit tests for the linecount.py

# Assumptions
  <p>Valid directory for fetching text files, non text files are not supported.
  <p>Files are not encrypted.
  
