This is a CSCTakedowns api for organizations.
This integration was integrated and tested with version xx of CSCTakedowns.

## Configure CSCTakedowns in Cortex


| **Parameter** | **Required** |
| --- | --- |
| Server URL | True |
| API Key | True |
| Trust any certificate (not secure) | False |
| Use system proxy settings | False |

## Commands

You can execute these commands from the CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.

### csctakedowns-fetchthephishkitdatawithticketid

***
Fetch the phishkit data with ticketId

#### Base Command

`csctakedowns-fetchthephishkitdatawithticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket Id to fetch phishkit. | Required | 

#### Context Output

There is no context output for this command.
### csctakedowns-fetchthescreenshotdatawithticketid

***
Fetch the screenshot data with ticketId

#### Base Command

`csctakedowns-fetchthescreenshotdatawithticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket Id to fetch screenshot. | Required | 

#### Context Output

There is no context output for this command.
### csctakedowns-fetchtheticketdataandconverttopdf

***
Fetch the ticket data and convert to pdf

#### Base Command

`csctakedowns-fetchtheticketdataandconverttopdf`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket Id to fetch supporting documents for takedown. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSCTakedowns.message | String |  | 
| CSCTakedowns.status | String |  | 

### csctakedowns-gethtmlsourcecodeforaticket

***
Get HTML Source Code for a Ticket

#### Base Command

`csctakedowns-gethtmlsourcecodeforaticket`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket ID to fetch HTML source. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSCTakedowns.message | String |  | 
| CSCTakedowns.status | String |  | 

### csctakedowns-listofworklogsforticketid

***
List of work logs for ticket id

#### Base Command

`csctakedowns-listofworklogsforticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket ID to fetch work log details. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSCTakedowns.message | String |  | 
| CSCTakedowns.status | String |  | 

### csctakedowns-listtakedownevents

***
List Takedown Events

#### Base Command

`csctakedowns-listtakedownevents`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| fromDate | Start date in YYYY-MM-DD format. | Required | 
| toDate | End date in YYYY--MM--DD format. | Required | 
| page | page size. | Optional | 
| limit | Limit between 100 and 500, default = 100. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSCTakedowns.message | String |  | 
| CSCTakedowns.status | String |  | 

### csctakedowns-listtakedowneventswithfilters

***
List Takedown events with filters

#### Base Command

`csctakedowns-listtakedowneventswithfilters`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| fromDate | Start date in YYYY-MM-DD format. | Required | 
| toDate | End date in YYYY--MM--DD format. | Required | 
| _andId | Filter by Brand Id. | Optional | 
| fraudType | Type of the Fraud. | Optional | 
| ticketStatus | Ticket Status. | Optional | 
| DetectionDate | Filter by Detection date. | Optional | 
| AuthorizationDate | Filter by Authorization date. | Optional | 
| CompletedDate | Filter by Closed date. | Optional | 
| page | page size. | Optional | 
| limit | Limit between 100 and 500, default = 100. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSCTakedowns.message | String |  | 
| CSCTakedowns.status | String |  | 

### csctakedowns-updatetheactionwithticketid

***
Update the action with ticketId

#### Base Command

`csctakedowns-updatetheactionwithticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| action | Ticket action. | Required | 

#### Context Output

There is no context output for this command.
