# HS-Data-Migration
Demonstration of some of the code required to migrate client data from a PostgreSQL database into Hubspot, using SQL, Python, and Hubspot's API which is built using REST conventions.

*REPLACE ANY STRING WITH "HS_API_KEY" WITH YOUR API KEY.*

## Table of Contents

1. ["sql_queries" Folder](README.md#sql_queries-folder)
2. [Files with "1_"](README.md#files-with-1_)
3. [Files with "2_"](README.md#files-with-2_)
4. [Files with "3_"](README.md#files-with-3_)
5. [Files with "4_"](README.md#files-with-4_)
6. [format_api.py](README.md#format_api)
7. [unix_time.py](README.md#unix_time)
8. [Contact](README.md#contact)
9. [Acknowledgements](README.md#acknowledgements)

## "sql_queries" Folder
SQL code used to clean up example data.

## Files with "1_"
Creation of Hubspot properties. Properties are used to store data on HubSpot's standard CRM objects, custom objects, and products. A POST request is sent

## Files with "2_"
After properties are created for the corresponding objects, call the custom module "use_sql.py" to obtain cleaned data from the database to migrate over to Hubspot. A log folder will hold a .text file that will serve as error handling.

## Files with "3_"
A POST request to the "associations" endpoint will create assiociations between objects.

## Files with "4_"
Similar to files with "2_", these files will now use SQL calls to migrate over engagements: calls, emails, meetings, and notes.

## format_api
A module with helper functions to get objects and engagements API ready to make any POST requests.

## unix_time
Formats any "datetime" data into the appropriate Unix time (in milliseconds) as Hubspot records time this way.


## Contacts

Frank Ho - [@cuLyTech](https://twitter.com/culyTech)

Project Link: [https://github.com/frank-quoc/HS-Data-Migration](https://github.com/frank-quoc/HS-Data-Migration)

## Acknowledgements
- [Hubspot API documentation](https://developers.hubspot.com/docs/api/overview)
- [OBO Residency Program](https://theobogroup.com/careers/)
