import requests
import json
import os

from use_sql import get_rows, create_table, add_to_db
from format_api import make_api_ready

# API BATCH contacts and JSON information
url = "https://api.hubapi.com/crm/v3/objects/contacts/batch/create?hapikey=HS_API_KEY"
headers = {'Content-Type': "application/json"}

# SQL CODE
sql_query = '''SELECT * FROM frank.cleaned_contacts;'''

# Path and file name to log migrations
cwd = os.getcwd()
file_name = "contact_log.txt"
complete_path = os.path.join(cwd + "/logs", file_name)

if __name__ == '__main__':
    # List of the rows of the errors (in 10s)
    row_errors = []
    # Get the data from PostGreSQL in the form of RealDict class
    contact_rows = get_rows(sql_query)
    # Add the correct Hubspot API formatting to POST a request
    contacts = list(map(make_api_ready, contact_rows))
    # Prepare table to added hubspot primary key and original primary key
    table_name = "migrated_contacts"
    create_table(table_name)

    # Counts the number of line added
    count = 0
    for i in range(0, len(contacts), 100):
        # List of tuples of (hubspot_id, database_id)
        ids = []
        ten_contacts = contacts[i:i+100]
        payload = {"inputs": ten_contacts}
        # POST request and JSON string
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        # See response code from Hubspot
        print(response)

        # Opens or creates a file to log
        with open(complete_path, 'a') as file:
            file.write('\n')
            # Writes current row number
            file.write(f"{i+1}")
            file.write('\n')
            # If the post request is not successful
            if response.status_code != 201:
                # Record the row number
                curr_row_err = f"{i+1} to {i+11}"
                file.write('\n')
                # Write the post response code and response
                file.write(f"{response} - {response.text}")
                file.write('\n')
                # Write the current row number with an error
                file.write("CURRENT ID ERROR: " + curr_row_err)
                file.write('\n')
                file.write('*' * 100)
                file.write('\n')
                # Put the current row number with an error in the list
                row_errors.append(curr_row_err)
            else:
                # Add hubspot id and database id to the table
                results = json.loads(response.text)
                for result in results['results']:
                    ids.append((result['id'], result['properties']['external_id']))
                add_to_db(ids, table_name)

    with open(complete_path, 'a') as file:
        file.write('\n')
        # Summarizes the rows with errors
        file.write("SUMMARY - ID ERRORS: " + ", ".join(row_errors))
        file.write('\n')
        # Summarizes the number of OBJECTS added
        file.write(f"ADDED {count} OBJECTS")
    file.close()          