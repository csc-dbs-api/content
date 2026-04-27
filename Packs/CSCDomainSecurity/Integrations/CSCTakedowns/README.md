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

### CSCTakedowns-controldetectionflowbyeventidandaction

***
Control detection flow by event ID and action

#### Base Command

`CSCTakedowns-controldetectionflowbyeventidandaction`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| action | Update the action with eventID. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### CSCTakedowns-fetchthedetectiondataandconverttopdf

***
Fetch the detection data and convert to pdf

#### Base Command

`CSCTakedowns-fetchthedetectiondataandconverttopdf`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| eventId | Event Id to download takedown report. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### CSCTakedowns-fetchthephishkitdatawithticketid

***
Fetch the phishkit data with ticketId

#### Base Command

`CSCTakedowns-fetchthephishkitdatawithticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket Id to fetch phishkit. | Required | 

#### Context Output

There is no context output for this command.
### CSCTakedowns-fetchthescreenshotdatawithticketid

***
Fetch the screenshot data with ticketId

#### Base Command

`CSCTakedowns-fetchthescreenshotdatawithticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket Id to fetch screenshot. | Required | 

#### Context Output

There is no context output for this command.
### CSCTakedowns-fetchtheticketdataandconverttopdf

***
Fetch the ticket data and convert to pdf

#### Base Command

`CSCTakedowns-fetchtheticketdataandconverttopdf`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket Id to fetch supporting documents for takedown. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### CSCTakedowns-gethtmlsourcecodeforaticket

***
Get HTML Source Code for a Ticket

#### Base Command

`CSCTakedowns-gethtmlsourcecodeforaticket`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket ID to fetch HTML source. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### CSCTakedowns-getlistofands

***
Get list of Brands

#### Base Command

`CSCTakedowns-getlistofands`

#### Input

There are no input arguments for this command.

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.brandId | Number |  | 
| content.brandName | String |  | 
| content.isActive | Boolean |  | 

### CSCTakedowns-getlistoffraudtypes

***
Get list of fraud types

#### Base Command

`CSCTakedowns-getlistoffraudtypes`

#### Input

There are no input arguments for this command.

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.fraudTypeId | Number |  | 
| content.fraudTypeName | String |  | 

### CSCTakedowns-listofworklogsforticketid

***
List of work logs for ticket id

#### Base Command

`CSCTakedowns-listofworklogsforticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ticketId | Ticket ID to fetch work log details. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### CSCTakedowns-listtakedownevents

***
List Takedown Events

#### Base Command

`CSCTakedowns-listtakedownevents`

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

### CSCTakedowns-listtakedowneventswithfilters

***
List Takedown events with filters

#### Base Command

`CSCTakedowns-listtakedowneventswithfilters`

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

### CSCTakedowns-performanactiononasingletarget

***
Perform an action on a single target

#### Base Command

`CSCTakedowns-performanactiononasingletarget`

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

### CSCTakedowns-retrieveeventscreenshotwitheventid

***
Retrieve event screenshot with eventId

#### Base Command

`CSCTakedowns-retrieveeventscreenshotwitheventid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| eventId | Event Id to fetch screenshot details. | Required | 

#### Context Output

There is no context output for this command.
### CSCTakedowns-retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe

***
Retrieve filtered list of monitoring results within specified timeframe

#### Base Command

`CSCTakedowns-retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe`

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
### CSCTakedowns-retrievelistofdetectionswithinspecifiedtimeframe

***
Retrieve list of detections within specified timeframe

#### Base Command

`CSCTakedowns-retrievelistofdetectionswithinspecifiedtimeframe`

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
### CSCTakedowns-retrievelistofmonitoringresultswithinspecifiedtimeframe

***
Retrieve list of monitoring results within specified timeframe

#### Base Command

`CSCTakedowns-retrievelistofmonitoringresultswithinspecifiedtimeframe`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| startDate | Filter by from date. Expected format: YYYY-MM-DD. | Required | 
| endDate | Filter by end date. Expected format: YYYY-MM-DD. | Required | 
| page | page size. | Optional | 
| limit | Limit between 100 and 500, default is 100. | Optional | 

#### Context Output

There is no context output for this command.
### CSCTakedowns-retrievephishkitwitheventid

***
Retrieve phishkit with eventId

#### Base Command

`CSCTakedowns-retrievephishkitwitheventid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| eventId | Event Id to fetch phishkit details. | Required | 

#### Context Output

There is no context output for this command.
### CSCTakedowns-startorstopmonitoringforaspecificevent

***
Start or stop monitoring for a specific event

#### Base Command

`CSCTakedowns-startorstopmonitoringforaspecificevent`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| action | Monitoring action to perform. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| content.message | String |  | 
| content.status | String |  | 

### CSCTakedowns-updatetheactionwithticketid

***
Update the action with ticketId

#### Base Command

`CSCTakedowns-updatetheactionwithticketid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| action | Ticket action. | Required | 

#### Context Output

There is no context output for this command.
