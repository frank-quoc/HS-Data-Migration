import requests
import json

url = "https://api.hubapi.com/crm/v3/properties/contacts/batch/create?hapikey=HS_API_KEY"

#Same payload we used for the postman request
payload={
  "inputs": [
    {
      "name": "prefix",
      "label": "prefix",
      "type": "enumeration",
      "fieldType": "radio",
      "groupName": "contactinformation",
      "options": [
        {
          "label": "Mr.",
          "value": "Mr.",
          "displayOrder": 1
        },
        {
          "label": "Mrs.",
          "value": "Mrs.",
          "displayOrder": 2
        },
        {
          "label": "Ms.",
          "value": "Ms.",
          "displayOrder": 3
        },
        {
          "label": "Dr.",
          "value": "Dr.",
          "displayOrder": 4
        }
      ],
      "displayOrder": 0
    },
    {
      "name": "external_id",
      "label": "external_id",
      "type": "number",
      "fieldType": "number",
      "groupName": "contactinformation"
    },
    {
      "name": "picklist",
      "label": "picklist",
      "type": "enumeration",
      "fieldType": "select",
      "groupName": "contactinformation",
      "options": [
        {
          "label": "red",
          "value": "red",
          "displayOrder": 1
        },
        {
          "label": "orange",
          "value": "orange",
          "displayOrder": 2
        },
        {
          "label": "yellow",
          "value": "yellow",
          "displayOrder": 3
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