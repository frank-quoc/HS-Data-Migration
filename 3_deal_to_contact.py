import requests
import json
import os

from use_sql import get_rows, DictCursor
from format_api import make_assoc_api


# BATCH CREATE deal API CODE
url = "https://api.hubapi.com/crm/v3/associations/deal/contact/batch/create?hapikey=HS_API_KEY"
headers = {'Content-Type': "application/json"}

# SQL CODE
sql_query = '''SELECT * FROM frank.deals_contacts;'''

cwd = os.getcwd()
file_name = "deals_to_contacts_log.txt"
complete_path = os.path.join(cwd + "/logs", file_name)

if __name__ == '__main__':
    row_errors = []
    assoc_rows = get_rows(sql_query, cursor_factory=DictCursor)
    type = "deal_to_contact"

    count = 0
    for i in range(0, len(assoc_rows), 100):
        # List to send request
        hundred_associations = []
        # Add the appropriate format for each association
        for row in assoc_rows[i:i+100]:
            hundred_associations.append(make_assoc_api(row, type))

        payload = {"inputs": hundred_associations}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(response)
        with open(complete_path, 'a') as file:
            file.write('\n')
            # Writes current row number
            file.write(f"{i+1}")
            file.write('\n')
        if response.status_code != 201:
            file.write('\n')
            file.write(f"{response} - {response.text}")
            file.write('\n')
            file.write('*' * 100)
            file.write('\n')
            row_errors.append(f"{i+1} to {i+101}")
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
        # Summarizes the rows with errors
        file.write("SUMMARY - ID ERRORS: " + ", ".join(row_errors))
        file.write('\n')
        # Summarizes the number of OBJECTS added
        file.write(f"ADDED {count} ASSOCIATIONS")
    file.close()   