# Full path to the System Under Test (or Java Main Class name)
executable:${TEXTTEST_HOME}/puzzle9/log_dump.py
interpreter:python

# Naming scheme to use for files for stdin,stdout and stderr
filename_convention_scheme:standard

# Expanded name to use for application
full_name:Log Dump

copy_test_path:logs

[collate_file]
dump:logs.tar.gz
[end]

[collate_script]
dump:python ${TEXTTEST_HOME}/puzzle9/read_dump.py
[end]

[run_dependent_text]
dump:{INTERNAL writedir}
dump:43\d{REPLACE 436}
