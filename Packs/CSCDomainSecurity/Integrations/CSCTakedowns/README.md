This is an anti fraud external api for organizations.
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

### controldetectionflowbyeventidandaction

***
Control detection flow by event ID and action

#### Base Command

`controldetectionflowbyeventidandaction`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| action | Update the action with eventID. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### fetchthedetectiondataandconverttopdf

***
Fetch the detection data and convert to pdf

#### Base Command

`fetchthedetectiondataandconverttopdf`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| eventId | Event Id to download takedown report. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### fetchthephishkitdatawithticketid

***
Fetch the phishkit data with ticketId

#### Base Command

`fetchthephishkitdatawithticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket Id to fetch phishkit. | Required | 

#### Context Output

There is no context output for this command.
### fetchthescreenshotdatawithticketid

***
Fetch the screenshot data with ticketId

#### Base Command

`fetchthescreenshotdatawithticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket Id to fetch screenshot. | Required | 

#### Context Output

There is no context output for this command.
### fetchtheticketdataandconverttopdf

***
Fetch the ticket data and convert to pdf

#### Base Command

`fetchtheticketdataandconverttopdf`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket Id to fetch supporting documents for takedown. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### gethtmlsourcecodeforaticket

***
Get HTML Source Code for a Ticket

#### Base Command

`gethtmlsourcecodeforaticket`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket ID to fetch HTML source. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### getlistofands

***
Get list of Brands

#### Base Command

`getlistofands`

#### Input

There are no input arguments for this command.

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.brandId | Number |  | 
| content.brandName | String |  | 
| content.isActive | Boolean |  | 

### getlistoffraudtypes

***
Get list of fraud types

#### Base Command

`getlistoffraudtypes`

#### Input

There are no input arguments for this command.

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.fraudTypeId | Number |  | 
| content.fraudTypeName | String |  | 

### listofworklogsforticketid

***
List of work logs for ticket id

#### Base Command

`listofworklogsforticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket ID to fetch work log details. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### listtakedownevents

***
List Takedown Events

#### Base Command

`listtakedownevents`

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
| content.message | String |  | 
| content.status | String |  | 

### listtakedowneventswithfilters

***
List Takedown events with filters

#### Base Command

`listtakedowneventswithfilters`

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
| content.message | String |  | 
| content.status | String |  | 

### performanactiononasingletarget

***
Perform an action on a single target

#### Base Command

`performanactiononasingletarget`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| targetType | Type of the target (URL, PHONE, EMAIL). | Optional | 
| action | Ticket action. | Required | 
| fraudType | Type of the Fraud. | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### retrieveeventscreenshotwitheventid

***
Retrieve event screenshot with eventId

#### Base Command

`retrieveeventscreenshotwitheventid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| eventId | Event Id to fetch screenshot details. | Required | 

#### Context Output

There is no context output for this command.
### retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe

***
Retrieve filtered list of monitoring results within specified timeframe

#### Base Command

`retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| startDate | Filter by from date. Expected format: YYYY-MM-DD. | Required | 
| endDate | Filter by end date. Expected format: YYYY-MM-DD. | Required | 
| _andId | Filter by Brand Id. | Optional | 
| fraudType | Type of the Fraud. | Optional | 
| monitoringStatus | Monitoring Status. | Optional | 
| page | page size. | Optional | 
| limit | Limit between 100 and 500, default is 100. | Optional | 

#### Context Output

There is no context output for this command.
### retrievelistofdetectionswithinspecifiedtimeframe

***
Retrieve list of detections within specified timeframe

#### Base Command

`retrievelistofdetectionswithinspecifiedtimeframe`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| fromDate | Filter by from date. Expected format: YYYY-MM-DD. | Required | 
| toDate | Filter by to date. Expected format: YYYY-MM-DD. | Required | 
| scoreMin | Filter by score. | Optional | 
| ip | Filter by ip. | Optional | 
| isp | Filter by isp. | Optional | 
| registrar | Filter by registrar. | Optional | 
| monitoring | Filter by monitoring. | Optional | 
| page | page size. | Optional | 
| limit | Limit between 100 and 500, default is 100. | Optional | 

#### Context Output

There is no context output for this command.
### retrievelistofmonitoringresultswithinspecifiedtimeframe

***
Retrieve list of monitoring results within specified timeframe

#### Base Command

`retrievelistofmonitoringresultswithinspecifiedtimeframe`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| startDate | Filter by from date. Expected format: YYYY-MM-DD. | Required | 
| endDate | Filter by end date. Expected format: YYYY-MM-DD. | Required | 
| page | page size. | Optional | 
| limit | Limit between 100 and 500, default is 100. | Optional | 

#### Context Output

There is no context output for this command.
### retrievephishkitwitheventid

***
Retrieve phishkit with eventId

#### Base Command

`retrievephishkitwitheventid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| eventId | Event Id to fetch phishkit details. | Required | 

#### Context Output

There is no context output for this command.
### startorstopmonitoringforaspecificevent

***
Start or stop monitoring for a specific event

#### Base Command

`startorstopmonitoringforaspecificevent`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| action | Monitoring action to perform. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### updatetheactionwithticketid

***
Update the action with ticketId

#### Base Command

`updatetheactionwithticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| action | Ticket action. | Required | 

#### Context Output

There is no context output for this command.
