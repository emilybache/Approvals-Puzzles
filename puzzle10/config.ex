# Full path to the System Under Test (or Java Main Class name)
executable:${TEXTTEST_HOME}/puzzle10/example.py

# Naming scheme to use for files for stdin,stdout and stderr
filename_convention_scheme:standard

# Expanded name to use for application
full_name:example

[run_dependent_text]
stdout:^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}{REPLACE timestamp}
stdout:(process_id)=\d+{REPLACE \1=1234}
