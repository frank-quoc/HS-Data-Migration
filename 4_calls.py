import requests
import json
import os

from use_sql import get_rows
from format_api import make_engagement_api

# API and JSON information
url = "https://api.hubapi.com/engagements/v1/engagements"
querystring = {"hapikey":"HS_API_KEY"}
headers = {
    'Content-Type': "application/json",
    }

# SQL Query 
sql_query = '''SELECT * FROM frank.cleaned_calls;'''

# Path and file name to log migrations
cwd = os.getcwd()
file_name = "calls_log.txt"
complete_path = os.path.join(cwd + "/logs", file_name)

if __name__ == '__main__':
    # List for the indices of the errors
    id_errors = []
    # Get the data from PostGreSQL in the form of RealDict class
    calls_rows = get_rows(sql_query)
    # Add the correct Hubspot API formatting to POST a request
    calls = list(map(make_engagement_api, calls_rows))

    # Counts the number of line added
    count = 0
    for i in range(0, len(calls)):
        # Converts RealDict object to JSON string
        payload = json.dumps(calls[i])
        # POST request
        response = requests.post(url, data=payload, headers=headers, params=querystring)
        # See response code from Hubspot
        print(response)

        # Opens or creates a file to log
        with open(complete_path, 'a') as file:
            file.write('\n')
            # Writes current row number
            file.write(f"{i+1}")
            file.write('\n')
            # If the post request is not successful
            if response.status_code != 200:
                # Record the row number
                curr_id_err = f"{i+1}"
                file.write('\n')
                # Write the post response code and response
                file.write(f"{response} - {response.text}")
                file.write('\n')
                # Write the current row number with an error
                file.write("CURRENT ID ERROR: " + curr_id_err)
                file.write('\n')
                file.write('*' * 100)
                file.write('\n')
                # Put the current row number with an error in the list
                id_errors.append(curr_id_err)
            else:
                # Write the current row number successfully uploaded
                count += 1
                file.write('\n')
                file.write(f"{response} - {response.text}")
                file.write('\n')
                file.write('-' * 100)
                file.write('\n')
            file.close()
    with open(complete_path, 'a') as file:
        file.write('\n')
        # Summarizes the ids with errors
        file.write("SUMMARY - ID ERRORS: " + ", ".join(id_errors))
        file.write('\n')
        # Summarizes the number of engagements
        file.write(f"ADDED {count} ENGAGEMENTS")
    file.close()  