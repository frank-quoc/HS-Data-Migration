from unix_time import return_unix_time

def make_api_ready(rows):
    """
    The make_api_ready function takes the SQL rows for OBJECTS and returns the format to be ready for the Hubspot API
    :param rows: the row of the SQL to be added
    :return: a dictionary with 'properties' as the key
    """
    return {"properties": dict(rows)}

def make_assoc_api(row, type):
    """ 
    The make_assoc_api function takes a table with the hubspot id in the 0th index and database id in the 1st index along with the type to return the format ready for the Hubspot id 
    for ASSOCIATIONS
    :param row: the row of the SQL to be added
    :param type: the type of association to create
    :return: a dictionary with the appropriate API format for Hubspot
    """
    return {
        "from": {
        "id": row[0]
    },
        "to": {
        "id": row[1]
    },
        "type": type
    }

def make_engagement_api(row):
    """
    The make_engagement_api takes the cleaned up rows for ENGAGEMENTS and makes it Hubspot api ready.
    :param row: the values of the rows to be added to the API
    :return API JSON for engagements
    """
    # The part of the engagement API that is common across all engagements
    engagement_api =  {
        "engagement": {
            "active": row["active"],
            "ownerId": row.get("ownerId", ""),
            "type": row["type"],
            "timestamp": return_unix_time(row["timestamp"])
        },
        "associations": {
            "contactIds": [row.get("contactids", "")],
            "companyIds": [row.get("companyids", "")],
            "dealIds": [row.get("dealsids", "")],
            "ownerIds": [row.get("ownerids", "")]
        },
        "attachments": [
            {
                "id": row.get("file_id", "")
            }
        ]
    }
    # metatdata for CALL
    if row["type"] == "CALL":
        engagement_api["metadata"] = {
            "toNumber": row.get("toNumber", ""),
            "fromNumber": row.get("fromNumber", ""),
            "status": row.get("status", ""),
            "durationMilliseconds": row.get("durationMilliseconds", ""),
            "recordingUrl": row.get("recordingUrl", ""),
            "body":  row.get("body", "")
        }
    # metadata for EMAIL
    elif row["type"] == "EMAIL":
        engagement_api["metadata"] = {
            "from": {
                "email": row.get("from_email", ""),
                "firstName": row.get("firstName", ""),
                "lastName": row.get("lastName", "")
            },
            "to": [
                {
                    "email": row.get("to_email", "")
                }
            ],
            "cc": [ {
                    "email": row.get("cc", "")
                }], 
            "bcc": [ {
                    "email": row.get("bcc", "")
                }],
            "subject": row.get("subject", ""),
            "html": row.get("html", ""),
            "text": row.get("text", "")
        }
    # metadata for NOTES
    elif row["type"] == "NOTE":
        engagement_api["metadata"] = {
            "toNumber": row.get("toNumber", ""), 
            "fromNumber": row.get("fromNumber", ""),
            "status": row.get("status", ""),
            "durationMilliseconds": row.get("durationMillisecond", ""),
            "title" : row.get("title", ""),  
            "recordingUrl": row.get("recordingUrl", ""),
            "source" : row.get("ource", ""),
            "appId" : row.get("appId", ""), 
        }
    # metadata for MEETING
    elif row["type"] == "MEETING":
        engagement_api["metadata"] = {
            "body": row.get("body", ""),
            "startTime": row.get("startTime", ""),
            "endTime": row.get("endTime", ""),
            "title": row.get("title", ""),
            "internalMeetingNotes" : row.get("internalMeetingNotes", "")
        }
  
    return engagement_api