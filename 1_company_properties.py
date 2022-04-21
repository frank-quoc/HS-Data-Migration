import requests
import json

url = "https://api.hubapi.com/crm/v3/properties/companies/batch/create?hapikey=HS_API_KEY"

#Payload to add company properties
payload={
  "inputs": [
    {
      "groupName": "companyinformation",
      "hidden": False,
      "displayOrder": 1,
      "options": [],
      "label": "text",
      "hasUniqueValue": False,
      "type": "string",
      "fieldType": "text",
      "formField": True,
      "name": "text"
    },
    {
      "name": "external_id",
      "label": "external_id",
      "type": "number",
      "fieldType": "number",
      "groupName": "companyinformation"
    },
    {
      "name": "boolean",
      "label": "boolean",
      "type": "enumeration",
      "fieldType": "booleancheckbox",
      "groupName": "companyinformation",
      "options": [
        {
          "label": "true",
          "value": "true"
        },
        {
          "label": "false",
          "value": "false"
        }
      ]
    }
  ]
}

#Set the Content-Type to Application/json
headers = {'Content-Type': 'application/json'}

#Json dumps changes the json to a string
response = requests.post(url, headers=headers, data=json.dumps(payload))

#See the response code from Hubspot
print(response)

#See the response from Hubspot
print(response.text)