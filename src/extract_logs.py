#!/usr/bin/env python
# coding: utf-8

# In[3]:


def extract_logs(log_file, target_date):
    # Ensure the output directory exists
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Output file path
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    # Open the log file for reading
    try:
        with open(log_file, 'r') as infile, open(output_file, 'w') as outfile:
            found = False
            for line in infile:
                # Check if the line starts with the target date
                if line.startswith(target_date):
                    outfile.write(line)
                    found = True

            if found:
                print(f"Logs for {target_date} saved to {output_file}")
            else:
                print(f"No logs found for the date {target_date}.")
    except FileNotFoundError:
        print(f"Error: The log file '{log_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# In[4]:


import os


# In[5]:


# Specify the log file and target date
log_filename = "logs_2024.log"  # Path to the log file
target_date = "2024-12-01"  # Target date in YYYY-MM-DD format

# Call the function to extract logs for the specified date
extract_logs(log_filename, target_date)


# In[9]:


import os
from IPython.display import FileLink

# Function to extract logs based on a specific date
def extract_logs(log_file, target_date):
    # Ensure the output directory exists
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Output file path
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    # Open the log file for reading and write the logs for the target date
    try:
        with open(log_file, 'r') as infile, open(output_file, 'w') as outfile:
            found = False
            for line in infile:
                # Check if the line starts with the target date
                if line.startswith(target_date):
                    outfile.write(line)
                    found = True

            if found:
                print(f"Logs for {target_date} saved to {output_file}")
            else:
                print(f"No logs found for the date {target_date}.")
    except FileNotFoundError:
        print(f"Error: The log file '{log_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage - specify the log file and target date
log_filename = "logs_2024.log"  # Replace with your log file's name
target_date = "2024-12-01"  # Replace with the target date in YYYY-MM-DD format
extract_logs(log_filename, target_date)

# Now, let's check if the output file was created and generate the download link

output_dir = "output"
output_file = os.path.join(output_dir, f"output_{target_date}.txt")

# Check if the output file exists
if os.path.exists(output_file):
    print(f"Logs saved to {output_file}. You can open this file to view the results.")
    
    # Create a download link for the output file
    download_link = FileLink(output_file)
    download_link  # Display the download link for Jupyter
else:
    print(f"Output file '{output_file}' not found.")


# In[10]:


from IPython.display import FileLink

# Assuming the file was successfully created
output_dir = "output"
target_date = "2024-12-01"  # Replace with your target date if needed
output_file = os.path.join(output_dir, f"output_{target_date}.txt")

# Check if the file exists before creating a link
if os.path.exists(output_file):
    print(f"Logs have been saved to {output_file}. Click the link below to download:")
    # Create a download link for the output file
    download_link = FileLink(output_file)
    display(download_link)  # This will display the clickable link in the notebook
else:
    print(f"Output file '{output_file}' not found.")


# In[ ]:
