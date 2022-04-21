import requests
import json

url = "https://api.hubapi.com/crm/v3/properties/deals/batch/create?hapikey=HS_API_KEY"

#Same payload we used for the postman request
payload={
  "inputs": [
    {
      "groupName": "dealinformation",
      "hidden": "false",
      "displayOrder": 2,
      "options": [
        {
          "label": "building",
          "description": "Choice number one",
          "value": "building",
          "displayOrder": 1,
          "hidden": "false"
        },
        {
          "label": "yellow",
          "description": "Choice number two",
          "value": "yellow",
          "displayOrder": 2,
          "hidden": "false"
        },
        {
          "label": "hello",
          "value": "hello",
          "displayOrder": 3
        },
        {
          "label": "red",
          "value": "red",
          "displayOrder": 4
        },
        {
          "label": "bird",
          "value": "bird",
          "displayOrder": 5
        },
        {
          "label": "orange",
          "value": "orange",
          "displayOrder": 6
        }
      ],
      "label": "multi_picklist_3",
      "hasUniqueValue": "false",
      "type": "enumeration",
      "fieldType": "checkbox",
      "formField": "true",
      "name": "multi_picklist_3"
    },
    {
      "name": "sentence",
      "label": "sentence",
      "type": "string",
      "fieldType": "text",
      "groupName": "dealinformation"
    },
    {
      "name": "external_id",
      "label": "external_id",
      "type": "number",
      "fieldType": "number",
      "groupName": "dealinformation"
    },
    {
      "name": "website",
      "label": "website",
      "type": "string",
      "fieldType": "text",
      "groupName": "dealinformation"
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