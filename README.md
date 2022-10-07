# analog_devices_test
Python Script to Count number of lines in text files

# Steps to run the file

python linecount.py filepath <--optional file extension-->

# libraries used
<p>os
<p>sys

# Folder structure
  .
+-- _config.yml
+-- _drafts
|   +-- begin-with-the-crazy-ideas.textile
|   +-- on-simplicity-in-technology.markdown
+-- _includes
|   +-- footer.html
|   +-- header.html
+-- _layouts
|   +-- default.html
|   +-- post.html
+-- _posts
|   +-- 2007-10-29-why-every-programmer-should-play-nethack.textile
|   +-- 2009-04-26-barcamp-boston-4-roundup.textile
+-- _data
|   +-- members.yml
+-- _site
+-- index.html
  analog_devices_test
  <p>     |
  <p>     |-testcases
  <p>          | - inner 
  <p>          |     |-  texttext.txt
  <p>          | - newfile1.txt
  <p>          | - hello.py
  <p>     | - linecount.py
  <p>     | - test_linecount.py
        
testcases folder contains dummy files for running unit tests
test_lincount unit tests for the linecount.py

# Assumptions
  <p>Valid directory for fetching text files, non text files are not supported.
  <p>Files are not encrypted.
  
