API Documentation
This integration was integrated and tested with version xx of DomainManager API.

## Configure DomainManager API in Cortex


| **Parameter** | **Description** | **Required** |
| --- | --- | --- |
| Server URL (e.g. https://apis.cscglobal.com/dbs/api/v2) |  | True |
| Token | The token to use for connection. | True |
| API Key | The API Key to use for connection. | True |
| Trust any certificate (not secure) |  | False |
| Use system proxy settings |  | False |

## Commands

You can execute these commands from the CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.

### csc-dbs-api-activateurlforwardingnode

***
Activate URL forwarding node

#### Base Command

`csc-dbs-api-activateurlforwardingnode`

#### Input

There are no input arguments for this command.

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.UrlForwardingActivateResult.link | String |  | 
| CSC-DBS-API.UrlForwardingActivateResult.status | String |  | 

### csc-dbs-api-addonedsrecordtoadomain

***
Add one DS record to a domain

#### Base Command

`csc-dbs-api-addonedsrecordtoadomain`

#### Input

There are no input arguments for this command.

#### Context Output

There is no context output for this command.
### csc-dbs-api-addurlforwardingnode

***
Add URL forwarding node

#### Base Command

`csc-dbs-api-addurlforwardingnode`

#### Input

There are no input arguments for this command.

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.UrlForwardingResult.result.price | Unknown | price of service | 
| CSC-DBS-API.UrlForwardingResult.result.service | String |  | 

### csc-dbs-api-cancelazoneeditwithafailedstatus

***
Cancel a zone edit with a 'FAILED' status

#### Base Command

`csc-dbs-api-cancelazoneeditwithafailedstatus`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| editID | Zone Edit ID. | Required | 

#### Context Output

There is no context output for this command.
### csc-dbs-api-checkregistrationavailabilityforoneormoredomainnames

***
Check registration availability for one or more domain names

#### Base Command

`csc-dbs-api-checkregistrationavailabilityforoneormoredomainnames`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| qualifiedDomainNames | Provide a maximum of 50 fully qualified domain names delimited by a comma (,). | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.RegistrationAvailabilityResult.results.qualifiedDomainName | String |  | 
| CSC-DBS-API.RegistrationAvailabilityResult.results.result.code | String | Availability result | 
| CSC-DBS-API.RegistrationAvailabilityResult.results.result.message | String |  | 
| CSC-DBS-API.RegistrationAvailabilityResult.results.basePrice.price | Unknown |  | 
| CSC-DBS-API.RegistrationAvailabilityResult.results.basePrice.currency | String |  | 

### csc-dbs-api-deletealldsrecordsforthegivendomainname

***
Delete all DS records for the given domain name

#### Base Command

`csc-dbs-api-deletealldsrecordsforthegivendomainname`

#### Input

There are no input arguments for this command.

#### Context Output

There is no context output for this command.
### csc-dbs-api-deleteasingledsrecordforadomain

***
Delete a single DS record for a domain

#### Base Command

`csc-dbs-api-deleteasingledsrecordforadomain`

#### Input

There are no input arguments for this command.

#### Context Output

There is no context output for this command.
### csc-dbs-api-deleteurlforwardingbyqualifieddomainname

***
Delete URL forwarding by qualified domain name

#### Base Command

`csc-dbs-api-deleteurlforwardingbyqualifieddomainname`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| qualifiedDomainName | Qualified domain name. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.UrlForwardingDeleteAllResult.qualifiedDomainName | String |  | 
| CSC-DBS-API.UrlForwardingDeleteAllResult.message | String |  | 

### csc-dbs-api-deleteurlforwardingbyqualifieddomainnameandnodename

***
Delete URL forwarding by qualified domain name and node name

#### Base Command

`csc-dbs-api-deleteurlforwardingbyqualifieddomainnameandnodename`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| qualifiedDomainName | Qualified domain name. | Required | 
| nodeName | Node name to be deleted. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.UrlForwardingDeleteResult.qualifiedDomainName | String |  | 
| CSC-DBS-API.UrlForwardingDeleteResult.message | String |  | 
| CSC-DBS-API.UrlForwardingDeleteResult.nodeRemoved | String |  | 

### csc-dbs-api-getalldsrecordsforaqualifieddomainname

***
Get all DS records for a qualified domain name

#### Base Command

`csc-dbs-api-getalldsrecordsforaqualifieddomainname`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| qualifiedDomainName | Qualified domain name. | Required | 

#### Context Output

There is no context output for this command.
### csc-dbs-api-getasinglezoneeditbyitsuuid

***
Get a single zone edit by its UUID

#### Base Command

`csc-dbs-api-getasinglezoneeditbyitsuuid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| editID | A zone edit's UUID. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.ZoneEdit.zoneName | String |  | 
| CSC-DBS-API.ZoneEdit.id | String |  | 
| CSC-DBS-API.ZoneEdit.zoneId | String |  | 
| CSC-DBS-API.ZoneEdit.modifiedDate | String |  | 
| CSC-DBS-API.ZoneEdit.requestedBy | String |  | 
| CSC-DBS-API.ZoneEdit.source | String |  | 

### csc-dbs-api-getbusinessunitdata

***
Get business unit data

#### Base Command

`csc-dbs-api-getbusinessunitdata`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| filter_ | Filters can be applied to your request to limit the type of data you receive.  ### Selectors  Selectors can be used to filter by specific properties on the business unit.  - accountName  - accountNumber  - businessUnitName  - usage  ---   ### Search Operators    \| Operator \| Name                     \| \|----------\|--------------------------\| \| ==       \| Equals                   \| \| =gt=     \| Greater Than             \| \| =ge=     \| Greater Than or Equal to \| \| =lt=     \| Less Than                \| \| =le=     \| Less Than or Equal to    \| \| =in=     \| In a list                \| \| =like=   \| Like query               \|   ---  ### Joiners  Joiners can be used to create compound filters.  \| Joiner \| Name \| \|--------\|------\| \| ;      \| And  \| \| ,      \| Or   \|   ---    ### Special Considerations  1. Surround values in double quotes. If the value is a single alphanumeric term, the quotes can be omitted.  2. If a value contains a double quote (") or a backslash (\\), it must be escaped with a backslash.  3. Ampersand and non-ascii characters must be URL encoded.   ---    ### Examples   details   summary Click to view - All examples exclude the required preceding "filter=" /summary  blockquote    details  summary Find all business units with a businessUnitName of TEST BU /summary  blockquote   ``` businessUnitName=="TEST BU" ```   /blockquote   /details    details  summary Find all business units with a businessUnitName like TEST /summary  blockquote   ``` businessUnitName=like="TEST " ```   /blockquote   /details     details  summary Find all business units with a usage of DOMAIN and an accountNumber of 123456 /summary  blockquote   ``` usage=="DOMAIN";accountNumber=="123456" ```   /blockquote   /details     details  summary Find all business units with a usage of DOMAIN or RELATED_SERVICES /summary  blockquote   ``` usage=in=("DOMAIN","RELATED_SERVICES") ```   /blockquote   /details     /blockquote   /details   --- . | Optional | 
|  |  | Optional | 
|  |  | Optional | 
|  |  | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.PagedBusinessUnitResponse.businessUnits.businessUnitName | String |  | 

### csc-dbs-api-getbusinessunitdatabybusinessunitname

***
Get business unit data by business unit name

#### Base Command

`csc-dbs-api-getbusinessunitdatabybusinessunitname`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| businessUnitName | Business unit name. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.BusinessUnit.businessUnitName | String |  | 

### csc-dbs-api-getcertificatebyuuid

***
Get certificate by UUID

#### Base Command

`csc-dbs-api-getcertificatebyuuid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| uuid | The UUID of the order. Returned as 'uuid' in the response. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.TlsOrderResponse.uuid | String |  | 
| CSC-DBS-API.TlsOrderResponse.commonName | String |  | 
| CSC-DBS-API.TlsOrderResponse.status | String |  | 
| CSC-DBS-API.TlsOrderResponse.effectiveDate | String |  | 
| CSC-DBS-API.TlsOrderResponse.isRenewed | Boolean |  | 
| CSC-DBS-API.TlsOrderResponse.expirationDate | String |  | 
| CSC-DBS-API.TlsOrderResponse.businessUnit | String |  | 
| CSC-DBS-API.TlsOrderResponse.orderedBy | String |  | 
| CSC-DBS-API.TlsOrderResponse.orderDate | String |  | 
| CSC-DBS-API.TlsOrderResponse.serverSoftware | String |  | 
| CSC-DBS-API.TlsOrderResponse.certificate | String |  | 
| CSC-DBS-API.TlsOrderResponse.customFields.name | String | Name of the custom field as defined in Domain Manager | 
| CSC-DBS-API.TlsOrderResponse.customFields.value | String |  | 

### csc-dbs-api-getcustomfieldsforthisaccount

***
Get custom fields for this account

#### Base Command

`csc-dbs-api-getcustomfieldsforthisaccount`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
|  |  | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.AccountCustomFields.customFields.label | String | Name of the custom field as defined in the account | 
| CSC-DBS-API.AccountCustomFields.customFields.mandatory | Boolean | Is this a required field to include with orders? | 
| CSC-DBS-API.AccountCustomFields.customFields.includedOnInvoice | Boolean | Is a required field to be included on invoicing? | 

### csc-dbs-api-getdomainconfigurationinformationforowneddomainswithoptionalfiltering

***
Get domain configuration information for owned domains with optional filtering

#### Base Command

`csc-dbs-api-getdomainconfigurationinformationforowneddomainswithoptionalfiltering`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| filter_ | Filters can be applied to your request to limit the type of data you receive.  ### Selectors  Selectors can be used to filter by specific properties on the domain.  - domain  - domainLabel  - domainStatusCode  - dnsHostingType  - extension  - tld  - country  - adminEmail  - adminName  - adminOrg  - regEmail  - regName  - regOrg  - techEmail  - techName  - techOrg  - accountNumber  - accountName  - businessUnit  - dnsTraffic12moAve  - hasCscUrlf  - hasDkim  - hasDnssecDs  - hasSpf  - hasWww  - isGtld  - isLive  - isLiveType  - isMultilockEligible  - isVital  - multiLocked  - numLiveMx  - numRootA  - numRootTxt  - numSslNetcraft  - numWwwA  - numWwwCname  - registryExpiryDate  - rootHttpCode  - rootHttpUrl  - rootIsUrlf  - serverDeleteProhibited  - serverTransferProhibited  - serverUpdateProhibited  - urlfTraffic12moAve  - valueRootA  - valueRootMx  - valueRootTxt  - valueWwwA  - valueWwwCname  - wwwHttpCode  - wwwHttpUrl  - wwwIsUrlf  ### Search Operators  \| Operator \| Name                     \| \|----------\|--------------------------\| \| ==       \| Equals                   \| \| =gt=     \| Greater Than             \| \| =ge=     \| Greater Than or Equal to \| \| =lt=     \| Less Than                \| \| =le=     \| Less Than or Equal to    \| \| =in=     \| In a list                \| \| =like=   \| Like query               \|   ---  ### Joiners  Joiners can be used to create compound filters.  \| Joiner \| Name \| \|--------\|------\| \| ;      \| And  \| \| ,      \| Or   \|   ---    ### Special Considerations  1. Surround values in double quotes. If the value is a single alphanumeric term, the quotes can be omitted.  2. If a value contains a double quote (") or a backslash (\), it must be escaped with a backslash.  3. Ampersand and non-ascii characters must be URL encoded.  ---    ### Examples   details   summary Click to view - All examples exclude the required preceding "filter=" /summary  blockquote    details  summary Find configuration for the domain example.com /summary  blockquote   ``` domain=="example.com" ```   /blockquote   /details    details  summary Find all domains with a domainLabel like example /summary  blockquote   ``` domainLabel=like="example " ```   /blockquote   /details     details  summary Find all domains with a registryExpiryDate greater than Jan 05 2020 /summary  blockquote   ``` registryExpiryDate=gt="2020-01-05" ```   /blockquote   /details    details  summary Find all domains with an accountNumber of 1234567 or 0987654 /summary  blockquote   ``` accountNumber=in=(1234567, 0987654) ```   /blockquote   /details     details  summary Find all domains with a valueRootA of 165.160.13.20 or 165.160.15.25 and an extension of 'com' /summary  blockquote   ``` valueRootA=in=("165.160.13.20", "165.160.15.25");extension=="com" ```   /blockquote   /details     details  summary Find all domains where isVital is true and either multiLocked is false or isMultilockEligible is false /summary  blockquote   ``` isVital==true;multiLocked==false,isMultilockEligible=... | Optional | 
|  |  | Optional | 
|  |  | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.ConfigurationCallSuccess.meta.numResults | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.meta.pages | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.domain | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.domainLabel | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.domainStatusCode | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.dnsHostingType | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.extension | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.tld | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.country | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.adminEmail | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.adminName | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.adminOrg | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.regEmail | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.regName | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.regOrg | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.techEmail | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.techName | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.techOrg | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.accounts.accountNumber | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.accounts.accountName | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.businessUnit | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.dnsData.dnsName | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.dnsTraffic12moAve | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.hasCscUrlf | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.hasDkim | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.hasDmarc | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.hasDnssecDs | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.hasSpf | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.hasWww | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.isGtld | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.isLive | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.isLiveType | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.isMultilockEligible | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.isVital | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.multiLocked | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.numLiveMx | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.numRootA | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.numRootTxt | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.numSslNetcraft | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.numWwwA | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.numWwwCname | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.registryExpiryDate | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.rootHttpCode | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.rootHttpUrl | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.rootIsUrlf | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.serverDeleteProhibited | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.serverTransferProhibited | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.serverUpdateProhibited | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.urlfTraffic12moAve | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.wwwHttpeCode | Unknown |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.wwwHttpUrl | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.configurations.wwwIsUrlf | Boolean |  | 
| CSC-DBS-API.ConfigurationCallSuccess.links.self | String |  | 
| CSC-DBS-API.ConfigurationCallSuccess.links.next | String |  | 

### csc-dbs-api-getdomaindatabyqualifieddomainname

***
Get domain data by qualified domain name

#### Base Command

`csc-dbs-api-getdomaindatabyqualifieddomainname`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| qualifiedDomainName | Qualified domain name. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.Domain.qualifiedDomainName | String |  | 
| CSC-DBS-API.Domain.domain | String |  | 
| CSC-DBS-API.Domain.idn | String |  | 
| CSC-DBS-API.Domain.extension | String |  | 
| CSC-DBS-API.Domain.newGtld | Boolean |  | 
| CSC-DBS-API.Domain.managedStatus | String |  | 
| CSC-DBS-API.Domain.registrationDate | String |  | 
| CSC-DBS-API.Domain.registryExpiryDate | String |  | 
| CSC-DBS-API.Domain.paidThroughDate | String |  | 
| CSC-DBS-API.Domain.countryCode | String |  | 
| CSC-DBS-API.Domain.serverDeleteProhibited | Boolean |  | 
| CSC-DBS-API.Domain.serverTransferProhibited | Boolean |  | 
| CSC-DBS-API.Domain.serverUpdateProhibited | Boolean |  | 
| CSC-DBS-API.Domain.whoisPrivacy | Boolean |  | 
| CSC-DBS-API.Domain.localAgent | Boolean |  | 
| CSC-DBS-API.Domain.dnssecActivated | String |  | 
| CSC-DBS-API.Domain.criticalDomain | Boolean |  | 
| CSC-DBS-API.Domain.businessUnit | String |  | 
| CSC-DBS-API.Domain.brandName | String |  | 
| CSC-DBS-API.Domain.idnReferenceName | String |  | 
| CSC-DBS-API.Domain.customFields.name | String | Name of the custom field as defined in Domain Manager | 
| CSC-DBS-API.Domain.customFields.value | String |  | 
| CSC-DBS-API.Domain.whoisContacts.contactType | String |  | 
| CSC-DBS-API.Domain.whoisContacts.firstName | String |  | 
| CSC-DBS-API.Domain.whoisContacts.lastName | String |  | 
| CSC-DBS-API.Domain.whoisContacts.organization | String |  | 
| CSC-DBS-API.Domain.whoisContacts.street1 | String |  | 
| CSC-DBS-API.Domain.whoisContacts.street2 | String |  | 
| CSC-DBS-API.Domain.whoisContacts.city | String |  | 
| CSC-DBS-API.Domain.whoisContacts.stateProvince | String |  | 
| CSC-DBS-API.Domain.whoisContacts.country | String |  | 
| CSC-DBS-API.Domain.whoisContacts.postalCode | String |  | 
| CSC-DBS-API.Domain.whoisContacts.email | String |  | 
| CSC-DBS-API.Domain.whoisContacts.phone | String |  | 
| CSC-DBS-API.Domain.whoisContacts.phoneExtn | String |  | 
| CSC-DBS-API.Domain.whoisContacts.fax | String |  | 
| CSC-DBS-API.Domain.lastModifiedDate | String |  | 
| CSC-DBS-API.Domain.lastModifiedReason | String |  | 
| CSC-DBS-API.Domain.lastModifiedDescription | String |  | 

### csc-dbs-api-getdomainportfoliodata

***
Get domain portfolio data

#### Base Command

`csc-dbs-api-getdomainportfoliodata`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| filter_ | Filters can be applied to your request to limit the type of data you receive.  ### Selectors  Selectors can be used to filter by specific properties on the domain.  - accountName  - accountNumber  -  andName  - businessUnit  - city  - country  - countryCode  - criticalDomain  - dnssecActivated  - dnsType  - domain  - email  - extension  - fax  - firstName  - idnReferenceName  - lastModifiedDate  - lastModifiedDescription  - lastModifiedReason  - lastName  - localAgent  - managedStatus  - nameServers  - newGtld  - organization  - paidThroughDate  - phone  - phoneExtn  - postalCode  - qualifiedDomainName  - redirectType  - registrationDate  - registryExpiryDate  - serverDeleteProhibited  - serverTransferProhibited  - serverUpdateProhibited  - stateProvince  - street1  - street2  - urlForwarding  - whoisPrivacy  ---   ### Search Operators    \| Operator \| Name                     \| \|----------\|--------------------------\| \| ==       \| Equals                   \| \| =gt=     \| Greater Than             \| \| =ge=     \| Greater Than or Equal to \| \| =lt=     \| Less Than                \| \| =le=     \| Less Than or Equal to    \| \| =in=     \| In a list                \| \| =like=   \| Like query               \|   ---  ### Joiners  Joiners can be used to create compound filters.  \| Joiner \| Name \| \|--------\|------\| \| ;      \| And  \| \| ,      \| Or   \|   ---    ### Special Considerations  1. Surround values in double quotes. If the value is a single alphanumeric term, the quotes can be omitted.  2. If a value contains a double quote (") or a backslash (\\), it must be escaped with a backslash.  3. Ampersand and non-ascii characters must be URL encoded.   ---    ### Examples   details   summary Click to view - All examples exclude the required preceding "filter=" /summary  blockquote    details  summary Find all domains with a qualifiedDomainName of example.com /summary  blockquote   ``` qualifiedDomainName=="example.com" ```   /blockquote   /details    details  summary Find all domains with a qualifiedDomainName like example /summary  blockquote   ``` qualifiedDomainName=like="example\ " ```   /blockquote   /details     details  summary Find all domains with a registrationDate greater than Jan 05 2010 /summary  blockquote   ``` registrationDate=gt="05-JAN-2010" ```   /blockquote   /details    details  summary Find all domains with a nameserver of dns1.mydns.com and an extension of 'com' /summary  blockquote   ``` nameservers=="dns1.mydns.com";extension=="com" ```   /blockquote   /details     details  summary Find all domains with a nameserver of dns1.mydns.com or dns2.mydns.com /summary  blockquote   ``` nameservers=in=("dns1.mydns.com","dns2.mydns.com") ```   /blockquote   /details     details  summary Find all domains with a WHOIS contact first name of Tom OR a last name of Smith /summary  blockquote   ``` firstName=="Tom",lastName=="Smith"&amp;sort=qualifiedDomainName,asc ```   /blockquote   /details     details  summary Find all domains by business unit name Foo &amp; Bar... | Optional | 
|  |  | Optional | 
|  |  | Optional | 
|  |  | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.PagedDomainResponse.domains.qualifiedDomainName | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.domain | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.idn | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.extension | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.newGtld | Boolean |  | 
| CSC-DBS-API.PagedDomainResponse.domains.managedStatus | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.registrationDate | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.registryExpiryDate | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.paidThroughDate | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.countryCode | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.serverDeleteProhibited | Boolean |  | 
| CSC-DBS-API.PagedDomainResponse.domains.serverTransferProhibited | Boolean |  | 
| CSC-DBS-API.PagedDomainResponse.domains.serverUpdateProhibited | Boolean |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisPrivacy | Boolean |  | 
| CSC-DBS-API.PagedDomainResponse.domains.localAgent | Boolean |  | 
| CSC-DBS-API.PagedDomainResponse.domains.dnssecActivated | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.criticalDomain | Boolean |  | 
| CSC-DBS-API.PagedDomainResponse.domains.businessUnit | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.brandName | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.idnReferenceName | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.customFields.name | String | Name of the custom field as defined in Domain Manager | 
| CSC-DBS-API.PagedDomainResponse.domains.customFields.value | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.contactType | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.firstName | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.lastName | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.organization | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.street1 | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.street2 | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.city | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.stateProvince | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.country | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.postalCode | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.email | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.phone | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.phoneExtn | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.whoisContacts.fax | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.lastModifiedDate | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.lastModifiedReason | String |  | 
| CSC-DBS-API.PagedDomainResponse.domains.lastModifiedDescription | String |  | 

### csc-dbs-api-getoneormorecertificates

***
Get one or more certificates

#### Base Command

`csc-dbs-api-getoneormorecertificates`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| filter_ | Filters can be applied to your request to limit the type of data that you receive. When filter is not given the API will fetch certificates with status (ACTIVE, PENDING, IMPORTED) for the accessible business units.  ### Selectors  Selectors can be used to filter by specific properties on the security event.  - certificateTypeId  - name  - expirationDate  - effectiveDate  - status  - uuid  ---  ### ExpirationDate, EffectiveDate  The 'expirationDate' and the 'effectiveDate' selectors must have the following format: yyyy/MM/dd  ---  ### Search Operators  \| Operator \| Name                     \| \|----------\|--------------------------\| \| ==       \| Equals                   \| \| =gt=     \| Greater Than             \| \| =ge=     \| Greater Than or Equal to \| \| =lt=     \| Less Than                \| \| =le=     \| Less Than or Equal to    \| \| =in=     \| In a list                \| \| =like=   \| Like Query               \|  ---  ### Joiners  Joiners can be used to create compound filters.  \| Joiner \| Name \| \|--------\|------\| \| ;      \| And  \| \| ,      \| Or   \|  ---  ### Special Considerations  1. Surround values in double quotes. If the value is a single alphanumeric term, the quotes can be omitted.  2. If a value contains a double quote (") or a backslash (\\), it must be escaped with a backslash.  3. Ampersand and non-ascii characters must be URL encoded.  ---  ### Examples   details   summary Click to view - All examples exclude the required preceding "filter=" /summary  blockquote    details  summary Find all cetificates with status ACTIVE /summary  blockquote   ``` status==ACTIVE ```   /blockquote   /details    details  summary Find all certificates between two dates /summary  blockquote   ``` expirationDate=le=2019/09/25;expirationDate=ge=2019/07/04 ```   /blockquote   /details    details  summary Find all certificate orders that have expiry date after August 25, 2019 /summary  blockquote   ``` expirationDate=gt=2019/08/25;status==ACTIVE ```   /blockquote   /details    /blockquote   /details   --- . | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.MultiTlsRetrieveResponse.meta.numResults | Number |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.uuid | String |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.commonName | String |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.status | String |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.effectiveDate | String |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.isRenewed | Boolean |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.expirationDate | String |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.businessUnit | String |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.orderedBy | String |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.orderDate | String |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.serverSoftware | String |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.certificate | String |  | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.customFields.name | String | Name of the custom field as defined in Domain Manager | 
| CSC-DBS-API.MultiTlsRetrieveResponse.results.customFields.value | String |  | 

### csc-dbs-api-getoneormoreorders

***
Get one or more orders

#### Base Command

`csc-dbs-api-getoneormoreorders`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| filter_ |  Filters can be applied to your request to limit the type of data that you receive.  ### Selectors  Selectors can be used to filter by specific properties on the order.  - orderType  - qualifiedDomainName  - raisedDate  - uuid  ---  ### Raised Date  The 'raised date' selector must have the following format: yyyy/MM/dd  ---  ### Search Operators  \| Operator \| Name                     \| \|----------\|--------------------------\| \| ==       \| Equals                   \| \| =gt=     \| Greater Than             \| \| =ge=     \| Greater Than or Equal to \| \| =lt=     \| Less Than                \| \| =le=     \| Less Than or Equal to    \| \| =in=     \| In a list                \| \| =like=   \| Like Query               \|  ---  ### Joiners  Joiners can be used to create compound filters.  \| Joiner \| Name \| \|--------\|------\| \| ;      \| And  \| \| ,      \| Or   \|  ---  ### Special Considerations  1. Surround values in double quotes. If the value is a single alphanumeric term, the quotes can be omitted.  2. If a value contains a double quote (") or a backslash (\\), it must be escaped with a backslash.  3. Ampersand and non-ascii characters must be URL encoded.  ---  ### Examples   details   summary Click to view - All examples exclude the required preceding "filter=" /summary  blockquote    details  summary Find all orders of type MULTILOCK /summary  blockquote   ``` orderType==MULTILOCK ```   /blockquote   /details    details  summary Find all orders between two dates /summary  blockquote   ``` raisedDate=le=2019/09/25;raisedDate=ge=2019/07/04 ```   /blockquote   /details    details  summary Find all REGISTRATION orders that were raised after August 25, 2019 /summary  blockquote   ``` raisedDate=gt=2019/08/25;orderType==REGISTRATION ```   /blockquote   /details     /blockquote   /details   --- . | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.MultiOrderResponse.meta.numResults | Number |  | 
| CSC-DBS-API.MultiOrderResponse.ordersList.qualifiedDomainName | String |  | 
| CSC-DBS-API.MultiOrderResponse.ordersList.accountName | String |  | 
| CSC-DBS-API.MultiOrderResponse.ordersList.accountNumber | String |  | 
| CSC-DBS-API.MultiOrderResponse.ordersList.raisedBy | String |  | 
| CSC-DBS-API.MultiOrderResponse.ordersList.raisedDate | String |  | 
| CSC-DBS-API.MultiOrderResponse.ordersList.uuid | String |  | 

### csc-dbs-api-getoneormoresecurityevents

***
Get one or more security events

#### Base Command

`csc-dbs-api-getoneormoresecurityevents`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| filter_ |  Filters can be applied to your request to limit the type of data you receive.  ### Selectors  Selectors can be used to filter by specific properties on the security event.  - eventDate  - eventType  - id  ---  ### Event Date  If the 'event date' selector is provided it must be an ISO-standard timestamp. (ex. 2019-11-17T22:35:32). The timezone needs to be UTC for accurate results.  ---  ### Search Operators    \| Operator \| Name                     \| \|----------\|--------------------------\| \| ==       \| Equals                   \| \| =gt=     \| Greater Than             \| \| =ge=     \| Greater Than or Equal to \| \| =lt=     \| Less Than                \| \| =le=     \| Less Than or Equal to    \| \| =in=     \| In a list                \|   ---   ### Joiners  Joiners can be used to create compound filters.  \| Joiner \| Name \| \|--------\|------\| \| ;      \| And  \| \| ,      \| Or   \|   ---   ### Special Considerations  1. Surround values in double quotes. If the value is a single alphanumeric term, the quotes can be omitted.  2. If a value contains a double quote (") or a backslash (\\), it must be escaped with a backslash.  3. Ampersand and non-ascii characters must be URL encoded.   ---  ### Examples   details   summary Click to view - All examples exclude the required preceding "filter=" /summary  blockquote    details  summary Find all events of type DNS_CHANGE_REQUESTED /summary  blockquote   ``` eventType==DNS_CHANGE_REQUESTED ```   /blockquote   /details    details  summary Find all events between two timestamps /summary  blockquote   ``` eventdate=le=2019-09-25T00:00:00;eventDate=ge=2019-07-04T00:00:00 ```   /blockquote   /details     details  summary Find all LOGIN events that occurred after August 25, 2019 /summary  blockquote   ``` eventdate=gt=2019-08-25T00:00:00;eventType==LOGIN ```   /blockquote   /details     /blockquote   /details   --- . | Optional | 
|  |  | Optional | 
|  |  | Optional | 
|  |  | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.PagedEventResponse.events.id | String |  | 

### csc-dbs-api-getoneormorezoneedits

***
Get one or more zone edits

#### Base Command

`csc-dbs-api-getoneormorezoneedits`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| filter_ | Filters can be applied to your request to limit the type of data you receive.  ### Selectors  Selectors can be used to filter by specific properties on the zone or zone edit.  - zoneName  - modifiedDate  - status  ---   ### Search Operators    \| Operator \| Name                     \| \|----------\|--------------------------\| \| ==       \| Equals                   \| \| =gt=     \| Greater Than             \| \| =ge=     \| Greater Than or Equal to \| \| =lt=     \| Less Than                \| \| =le=     \| Less Than or Equal to    \| \| =in=     \| In a list                \| \| =like=   \| Like query               \|   ---  ### Joiners  Joiners can be used to create compound filters.  \| Joiner \| Name \| \|--------\|------\| \| ;      \| And  \| \| ,      \| Or   \|   ---    ### Special Considerations  1. Surround values in double quotes. If the value is a single alphanumeric term, the quotes can be omitted.  2. If a value contains a double quote (") or a backslash (\\), it must be escaped with a backslash.  3. Ampersand and non-ascii characters must be URL encoded.   ---    ### Examples   details   summary Click to view - All examples exclude the required preceding "filter=" /summary  blockquote    details  summary Find all zone edits for the zone of example.com /summary  blockquote   ``` zoneName=="example.com" ```   /blockquote   /details    details  summary Find all zone edits for a zone with a name like example /summary  blockquote   ``` zoneName=like="\ example\ " ```   /blockquote   /details     details  summary Find all zone edits with a modified date of March 31st, 2020 /summary  blockquote   ``` modifiedDate==31-Mar-2020 ```   /blockquote   /details    details  summary Find all zone edits with a modified date before March 31st, 2020 and with a status of 'CANCELED' /summary  blockquote   ``` modifiedDate=lt=31-Mar-2020;status==canceled ```   /blockquote   /details     /blockquote   /details   --- . | Optional | 
|  |  | Optional | 
|  |  | Optional | 
|  |  | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.PagedZoneEditResponse.zoneEdits.zoneName | String |  | 
| CSC-DBS-API.PagedZoneEditResponse.zoneEdits.id | String |  | 
| CSC-DBS-API.PagedZoneEditResponse.zoneEdits.zoneId | String |  | 
| CSC-DBS-API.PagedZoneEditResponse.zoneEdits.modifiedDate | String |  | 
| CSC-DBS-API.PagedZoneEditResponse.zoneEdits.requestedBy | String |  | 
| CSC-DBS-API.PagedZoneEditResponse.zoneEdits.source | String |  | 

### csc-dbs-api-getordersbytheiruuid

***
Get orders by their UUID

#### Base Command

`csc-dbs-api-getordersbytheiruuid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| orderUUID | The UUID of the order. Returned as 'uuid' in the response. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.Order.qualifiedDomainName | String |  | 
| CSC-DBS-API.Order.accountName | String |  | 
| CSC-DBS-API.Order.accountNumber | String |  | 
| CSC-DBS-API.Order.raisedBy | String |  | 
| CSC-DBS-API.Order.raisedDate | String |  | 
| CSC-DBS-API.Order.uuid | String |  | 

### csc-dbs-api-getsecurityeventsbyid

***
Get security events by ID

#### Base Command

`csc-dbs-api-getsecurityeventsbyid`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| eventID | Event ID. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.SecurityEvent.id | String |  | 

### csc-dbs-api-getthecurrentstatusofazoneedit

***
Get the current status of a zone edit

#### Base Command

`csc-dbs-api-getthecurrentstatusofazoneedit`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| editID | Zone Edit ID. | Required | 

#### Context Output

There is no context output for this command.
### csc-dbs-api-geturlforwardingdatabyqualifieddomainname

***
Get URL forwarding data by qualified domain name

#### Base Command

`csc-dbs-api-geturlforwardingdatabyqualifieddomainname`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| qualifiedDomainName | Qualified domain name. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.UrlForwardingRecords.urlForwardingRecords.node | String |  | 
| CSC-DBS-API.UrlForwardingRecords.urlForwardingRecords.domainName | String |  | 
| CSC-DBS-API.UrlForwardingRecords.urlForwardingRecords.sourceUrl | String | The node with the domain name. | 
| CSC-DBS-API.UrlForwardingRecords.urlForwardingRecords.targetUrl | String |  | 
| CSC-DBS-API.UrlForwardingRecords.urlForwardingRecords.redirectType | String | The HTTP redirection status code \(3  \) | 

### csc-dbs-api-getwhoiscontactprofiledata

***
Get Whois contact profile data

#### Base Command

`csc-dbs-api-getwhoiscontactprofiledata`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| filter_ | Filters can be applied to your request to limit the type of data you receive. #### Selectors Selectors can be used to filter by specific properties on the whois contact profile. - profileName - firstName - lastName - organization - street1 - street2 - city - stateProvince - country - postalCode - email - phone - phoneExtn - fax - contactTypes ---  #### Search Operators ==  =gt= (greater than)  =ge= (greater than or equal)  =lt= (less than)  =le= (less than or equal)  =in=  =like=   #### Joiners   Joiners can be used to create compound filters.     ;   (and)     ,   (or) #### Special Considerations 1. Surround values in double quotes. If the value is a single alphanumeric term, the quotes can be omitted. 2. If a value contains a double quote (") or a backslash (\\), it must be escaped with a backslash. 3. Ampersand and non-ascii characters must be URL encoded.  ---   ### Examples  details  summary Click to view - All examples exclude the required preceding "filter=" /summary  blockquote   details  summary Find all profiles with a last name of Jones /summary   blockquote  ``` lastName=="Jones" ```  /blockquote   /details    details  summary Find all profiles with a last name like Jo /summary   blockquote  ``` lastName=like="Jo " ```  /blockquote   /details    details  summary Find all profiles with a last name of Jones and a contact type of REGISTRANT /summary   blockquote  ``` lastName=="Jones";contactTypes=="REGISTRANT" ```  /blockquote   /details    details  summary Find all profiles with a contact type of TECHNICAL or ADMINISTRATIVE /summary   blockquote  ``` contactTypes=in=(ADMINISTRATIVE, TECHNICAL) ```  /blockquote   /details    details  summary Find all profiles with a first name of Chuck OR a last name of Smith, in ascending order by profile name /summary   blockquote  ``` firstName=="Chuck",lastName=="Smith"&amp;sort=profileName,asc ```  /blockquote   /details    details  summary Find all profiles by profile name Foo &amp; Bar (encoded) /summary  blockquote  ``` profileName=="Foo%20%26%20Bar" ```  /blockquote   /details    /blockquote   /details   --- . | Optional | 
|  |  | Optional | 
|  |  | Optional | 
|  |  | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.profileName | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.firstName | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.lastName | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.organization | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.street1 | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.street2 | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.city | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.stateProvince | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.country | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.postalCode | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.email | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.phone | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.phoneExtn | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.whoisContactProfiles.fax | String |  | 
| CSC-DBS-API.WhoisContactProfilePagedResource.links.self | String |  | 

### csc-dbs-api-getzonedatabyqualifiedzonename

***
Get zone data by qualified zone name

#### Base Command

`csc-dbs-api-getzonedatabyqualifiedzonename`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| zoneName | Zone name. | Required | 
| filter_ | Filters can be applied to your request to limit the zone records returned.  ### Selectors  Selectors can be used to filter by specific properties on the zone resource records.  - flag  - key  - port  - priority  - recordType  - tag  - ttl  - value  - weight  ---   ### Search Operators    \| Operator \| Name                     \| \|----------\|--------------------------\| \| ==       \| Equals                   \| \| =gt=     \| Greater Than             \| \| =ge=     \| Greater Than or Equal to \| \| =lt=     \| Less Than                \| \| =le=     \| Less Than or Equal to    \| \| =in=     \| In a list                \| \| =like=   \| Like query               \|   ---  ### Joiners  Joiners can be used to create compound filters.  \| Joiner \| Name \| \|--------\|------\| \| ;      \| And  \| \| ,      \| Or   \|   ---    ### Special Considerations  1. Surround values in double quotes. If the value is a single alphanumeric term, the quotes can be omitted.  2. If a value contains a double quote (") or a backslash (\\), it must be escaped with a backslash.  3. Ampersand and non-ascii characters must be URL encoded.   ---    ### Examples   details   summary Click to view - All examples exclude the required preceding "filter=" /summary  blockquote    details  summary Find all resource records with a recordType of A /summary  blockquote   ``` recordType=="A" ```   /blockquote   /details    details  summary Find all resource records with a key of "@" and a value like "165.160. " /summary  blockquote   ``` key="@";value=like="165.160. " ```   /blockquote   /details    details  summary Find all resource records with an 'A' record with a value of 1.2.3.4 /summary  blockquote   ``` (recordType=="a";value=="1.2.3.4") ```   /blockquote   /details     details  summary Find all resource records that have a '10' or '20' priority /summary  blockquote   ``` priority=in=("10","20") ```   /blockquote   /details     details  summary Find all resource records with an 'A' record with a key of 'www' OR a 'CNAME' record with a value of 'www' /summary  blockquote   ``` (recordType=="a";key=="www"),(recordType=="cname";value=="www") ```   /blockquote   /details     /blockquote   /details   --- . | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.Zone.zoneName | String |  | 
| CSC-DBS-API.Zone.hostingType | String |  | 
| CSC-DBS-API.Zone.a.id | String |  | 
| CSC-DBS-API.Zone.a.value | String |  | 
| CSC-DBS-API.Zone.a.key | String |  | 
| CSC-DBS-API.Zone.a.ttl | Number |  | 
| CSC-DBS-API.Zone.a.status | String |  | 
| CSC-DBS-API.Zone.cname.id | String |  | 
| CSC-DBS-API.Zone.cname.value | String |  | 
| CSC-DBS-API.Zone.cname.key | String |  | 
| CSC-DBS-API.Zone.cname.ttl | Number |  | 
| CSC-DBS-API.Zone.cname.status | String |  | 
| CSC-DBS-API.Zone.aaaa.id | String |  | 
| CSC-DBS-API.Zone.aaaa.value | String |  | 
| CSC-DBS-API.Zone.aaaa.key | String |  | 
| CSC-DBS-API.Zone.aaaa.ttl | Number |  | 
| CSC-DBS-API.Zone.aaaa.status | String |  | 
| CSC-DBS-API.Zone.txt.id | String |  | 
| CSC-DBS-API.Zone.txt.value | String |  | 
| CSC-DBS-API.Zone.txt.key | String |  | 
| CSC-DBS-API.Zone.txt.ttl | Number |  | 
| CSC-DBS-API.Zone.txt.status | String |  | 
| CSC-DBS-API.Zone.mx.id | String |  | 
| CSC-DBS-API.Zone.mx.value | String |  | 
| CSC-DBS-API.Zone.mx.key | String |  | 
| CSC-DBS-API.Zone.mx.ttl | Number |  | 
| CSC-DBS-API.Zone.mx.priority | Number |  | 
| CSC-DBS-API.Zone.mx.status | String |  | 
| CSC-DBS-API.Zone.ns.id | String |  | 
| CSC-DBS-API.Zone.ns.value | String |  | 
| CSC-DBS-API.Zone.ns.key | String |  | 
| CSC-DBS-API.Zone.ns.priority | Number |  | 
| CSC-DBS-API.Zone.ns.ttl | Number |  | 
| CSC-DBS-API.Zone.ns.status | String |  | 
| CSC-DBS-API.Zone.srv.id | String |  | 
| CSC-DBS-API.Zone.srv.value | String |  | 
| CSC-DBS-API.Zone.srv.key | String |  | 
| CSC-DBS-API.Zone.srv.priority | Number |  | 
| CSC-DBS-API.Zone.srv.weight | Number |  | 
| CSC-DBS-API.Zone.srv.ttl | Number |  | 
| CSC-DBS-API.Zone.srv.status | String |  | 
| CSC-DBS-API.Zone.caa.id | String |  | 
| CSC-DBS-API.Zone.caa.value | String |  | 
| CSC-DBS-API.Zone.caa.key | String |  | 
| CSC-DBS-API.Zone.caa.ttl | Number |  | 
| CSC-DBS-API.Zone.caa.status | String |  | 
| CSC-DBS-API.Zone.caa.tag | String |  | 
| CSC-DBS-API.Zone.caa.flag | Number |  | 
| CSC-DBS-API.Zone.soa.serial | Number |  | 
| CSC-DBS-API.Zone.soa.refresh | Number |  | 
| CSC-DBS-API.Zone.soa.retry | Number |  | 
| CSC-DBS-API.Zone.soa.expire | Number |  | 
| CSC-DBS-API.Zone.soa.ttlMin | Number |  | 
| CSC-DBS-API.Zone.soa.ttlNeg | Number |  | 
| CSC-DBS-API.Zone.soa.ttlZone | Number |  | 
| CSC-DBS-API.Zone.soa.techEmail | String |  | 
| CSC-DBS-API.Zone.soa.masterHost | String |  | 

### csc-dbs-api-getzoneportfoliodata

***
Get zone portfolio data

#### Base Command

`csc-dbs-api-getzoneportfoliodata`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| filter_ | Filters can be applied to your request to limit the type of data you receive.  ### Selectors  Selectors can be used to filter by specific properties on the zone or zone resource records.  - expire  - flag  - fullDomainName  - id  - key  - masterHost  - port  - priority  - recordType  - refresh  - retry  - serial  - tag  - techEmail  - ttl  - ttlMin  - ttlNeg  - ttlZone  - value  - weight  - zoneId  - zoneName  ---   ### Search Operators    \| Operator \| Name                     \| \|----------\|--------------------------\| \| ==       \| Equals                   \| \| =gt=     \| Greater Than             \| \| =ge=     \| Greater Than or Equal to \| \| =lt=     \| Less Than                \| \| =le=     \| Less Than or Equal to    \| \| =in=     \| In a list                \| \| =like=   \| Like query               \|   ---  ### Joiners  Joiners can be used to create compound filters.  \| Joiner \| Name \| \|--------\|------\| \| ;      \| And  \| \| ,      \| Or   \|   ---    ### Special Considerations  1. Surround values in double quotes. If the value is a single alphanumeric term, the quotes can be omitted.  2. If a value contains a double quote (") or a backslash (\\), it must be escaped with a backslash.  3. Ampersand and non-ascii characters must be URL encoded.   ---    ### Examples   details   summary Click to view - All examples exclude the required preceding "filter=" /summary  blockquote    details  summary Find all zones with a zoneName of example.com /summary  blockquote   ``` zoneName=="example.com" ```   /blockquote   /details    details  summary Find all zones with a zoneName like example /summary  blockquote   ``` zoneName=like="\ example\ " ```   /blockquote   /details     details  summary Find all zones with a ttlNeg less than 15000 /summary  blockquote   ``` ttlNeg=lt="15000" ```   /blockquote   /details    details  summary Find all zones with an 'A' record with a value of 1.2.3.4 /summary  blockquote   ``` (recordType=="a";value=="1.2.3.4") ```   /blockquote   /details     details  summary Find all zones that have a resource record with a '10' or '20' priority /summary  blockquote   ``` priority=in=("10","20") ```   /blockquote   /details     details  summary Find all zones with an 'A' record with a key of 'www' OR a 'CNAME' record with a value of 'www' /summary  blockquote   ``` (recordType=="a";key=="www"),(recordType=="cname";value=="www") ```   /blockquote   /details     /blockquote   /details   --- . | Optional | 
|  |  | Optional | 
|  |  | Optional | 
|  |  | Optional | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.PagedZoneResponse.zones.zoneName | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.hostingType | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.a.id | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.a.value | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.a.key | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.a.ttl | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.a.status | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.cname.id | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.cname.value | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.cname.key | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.cname.ttl | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.cname.status | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.aaaa.id | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.aaaa.value | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.aaaa.key | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.aaaa.ttl | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.aaaa.status | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.txt.id | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.txt.value | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.txt.key | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.txt.ttl | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.txt.status | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.mx.id | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.mx.value | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.mx.key | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.mx.ttl | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.mx.priority | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.mx.status | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.ns.id | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.ns.value | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.ns.key | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.ns.priority | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.ns.ttl | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.ns.status | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.srv.id | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.srv.value | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.srv.key | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.srv.priority | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.srv.weight | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.srv.ttl | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.srv.status | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.caa.id | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.caa.value | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.caa.key | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.caa.ttl | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.caa.status | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.caa.tag | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.caa.flag | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.soa.serial | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.soa.refresh | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.soa.retry | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.soa.expire | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.soa.ttlMin | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.soa.ttlNeg | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.soa.ttlZone | Number |  | 
| CSC-DBS-API.PagedZoneResponse.zones.soa.techEmail | String |  | 
| CSC-DBS-API.PagedZoneResponse.zones.soa.masterHost | String |  | 
| CSC-DBS-API.PagedZoneResponse.notManaged.code | String |  | 
| CSC-DBS-API.PagedZoneResponse.notManaged.message | String |  | 

### csc-dbs-api-modifythebusinessunitassociatedwithadomain

***
Modify the business unit associated with a domain

#### Base Command

`csc-dbs-api-modifythebusinessunitassociatedwithadomain`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| businessUnitName | New business unit name to associate with the domain. | Required | 
| qualifiedDomainName | Fully qualified domain name. | Required | 

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.businessUnitModResult.qualifiedDomainName | String |  | 
| CSC-DBS-API.businessUnitModResult.status.code | String |  | 
| CSC-DBS-API.businessUnitModResult.status.message | String |  | 
| CSC-DBS-API.businessUnitModResult.status.additionalInformation | String |  | 

### csc-dbs-api-modifythecustomfieldsassociatedwithadomain

***
Modify the custom fields associated with a domain

#### Base Command

`csc-dbs-api-modifythecustomfieldsassociatedwithadomain`

#### Input

There are no input arguments for this command.

#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| CSC-DBS-API.customFieldModResult.qualifiedDomainName | String |  | 
| CSC-DBS-API.customFieldModResult.status.code | String |  | 
| CSC-DBS-API.customFieldModResult.status.message | String |  | 
| CSC-DBS-API.customFieldModResult.status.additionalInformation | String |  | 

### csc-dbs-api-placeadomainregistrationorder

***
Place a domain registration order

#### Base Command

`csc-dbs-api-placeadomainregistrationorder`

#### Input

There are no input arguments for this command.

#### Context Output

There is no context output for this command.
### csc-dbs-api-placeansmodificationorder

***
Place a NS modification order

#### Base Command

`csc-dbs-api-placeansmodificationorder`

#### Input

There are no input arguments for this command.

#### Context Output

There is no context output for this command.
### csc-dbs-api-placeatlsregistrationorder

***
Place a TLS registration order

#### Base Command

`csc-dbs-api-placeatlsregistrationorder`

#### Input

There are no input arguments for this command.

#### Context Output

There is no context output for this command.
### csc-dbs-api-placeatlsreissueorder

***
Place a TLS reissue order

#### Base Command

`csc-dbs-api-placeatlsreissueorder`

#### Input

There are no input arguments for this command.

#### Context Output

There is no context output for this command.
### csc-dbs-api-placeatlsrenewalorder

***
Place a TLS renewal order

#### Base Command

`csc-dbs-api-placeatlsrenewalorder`

#### Input

There are no input arguments for this command.

#### Context Output

There is no context output for this command.
### csc-dbs-api-placeawhoiscontactmodificationorder

***
Place a Whois contact modification order

#### Base Command

`csc-dbs-api-placeawhoiscontactmodificationorder`

#### Input

There are no input arguments for this command.

#### Context Output

There is no context output for this command.
### csc-dbs-api-refreshexpiredtoken

***
Refresh expired token

#### Base Command

`csc-dbs-api-refreshexpiredtoken`

#### Input

There are no input arguments for this command.

#### Context Output

There is no context output for this command.
### csc-dbs-api-submitandpublishoneormorezoneedits

***
Submit and publish one or more zone edits

#### Base Command

`csc-dbs-api-submitandpublishoneormorezoneedits`

#### Input

There are no input arguments for this command.

#### Context Output

There is no context output for this command.
