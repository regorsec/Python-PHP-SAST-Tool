import os

# Define the directory to search in
directory = '.'

# Define the list of functions to look for
functions = ['system', 'exec', 'eval']

# Define the list of error handling variables
inivars = ['expose_php', 'error_reporting', 'display_errors', 'display_startup_errors', 'error_log', 'upload_tmp_dir', 'upload_max_filesize', 'disable_functions']

# Print Header for 1st Section - Dangerous Function Calls
print("#\n # DANGEROUS FUNCTIONS FOUND: \n #")

# Recursively search for PHP files in the directory
for root, dirs, files in os.walk(directory):

    for file in files:

        # Check for dangerous functions in all .php files and return the file if found
        if file.endswith('.php'):

            # Check if any of the functions exist in the PHP file
            with open(os.path.join(root, file), 'r', encoding='ISO-8859-1') as f:
                contents = f.read()
                for function in functions:
                    if function in contents:
                        print(f'{function} found in {os.path.join(root, file)}')
            

# Print Header for Second Section - PHP.INI Findings
print("#\n # REVIEW THE PHP.INI FINDINGS BELOW: \n #")

# Recursively search for PHP files in the directory
for root, dirs, files in os.walk(directory):
    for file in files:       
        
        if file is 'php.ini':
            # Check if any of the functions exist in the PHP file
            with open(os.path.join(root, file), 'r', encoding='ISO-8859-1') as f:
                contents = f.read()
                for evar in inivars:
                    if evar in contents:
                        print(f'{evar} found in {os.path.join(root, file)}')
