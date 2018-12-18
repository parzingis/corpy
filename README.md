# swagger-client
The main ORR documentation is located at: https://mmisw.org/orrdoc/  __Please note__: - The ORR API is approaching a stable version but is still work in progress.   Please [let us know](https://github.com/mmisw/mmiorr-docs/issues) if you have any   questions or suggestions.  - Besides the documentation itself, this page lets you directly exercise and test the API.   Click on any operation header below to learn more details about it, and see a \"Try it out\" button.  - You can click on the \"Authorize\" button at the top right of this page   (or the `!` icon under the particular operation)   to retrieve an authentication token corresponding to your ORR instance credentials (username and password).   Once authorized, the authentication token will be automatically included in the corresponding request.   You will be able to not only perform the basic `GET` operations,   but also see expanded responses according to your access privileges   as well as perform other operations.  - The \"Try it out\" button will also show the corresponding API call that you can submit   from the command line using [`curl`](https://curl.haxx.se/).  - This API includes administrative operations related with the triple store.   The SPARQL endpoint itself   (located at `http://cor.esipfed.org/sparql` for the MMI ORR instance)   is not described here.   (General SPARQL information can be found [here](https://en.wikipedia.org/wiki/SPARQL),   and regarding the current service used by the ORR to support the SPARQL interface   [here](http://franz.com/agraph/support/documentation/current/http-protocol.html).)  - Actual requests from this page are against the specific endpoint at   `http://cor.esipfed.org/ont`. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/ESIPFed/corpy.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ESIPFed/corpy.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'
# create an instance of the API class
api_instance = swagger_client.OntologyApi()
body = swagger_client.PostOnt() # PostOnt | Object with information for the ontology to be registered.  To provide the contents of the ontology you have two options:  - Specify a previously uploaded file (via `POST /ont/upload`) by   providing the corresponding reported filename (in the `uploadedFilename`   field) and format (`uploadedFormat`). There's no need to upload the file   itself again. - Embbed the complete contents in the `contents` field, and provide the associated   format in `format`.  See the `PostOnt` object description for more details. 

try:
    # Registers a brand new ontology
    api_instance.add_ont(body)
except ApiException as e:
    print("Exception when calling OntologyApi->add_ont: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://cor.esipfed.org/ont/api/v0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OntologyApi* | [**add_ont**](docs/OntologyApi.md#add_ont) | **POST** /ont | Registers a brand new ontology
*OntologyApi* | [**add_term**](docs/OntologyApi.md#add_term) | **POST** /ont/term | Adds a term to an existing ORR vocabulary
*OntologyApi* | [**delete_ont**](docs/OntologyApi.md#delete_ont) | **DELETE** /ont | Deletes a particular version or a whole ontology entry
*OntologyApi* | [**ont_get**](docs/OntologyApi.md#ont_get) | **GET** /ont | Gets information about registered ontologies or terms
*OntologyApi* | [**update_ont**](docs/OntologyApi.md#update_ont) | **PUT** /ont | Updates a given ontology version or adds a new version
*OntologyApi* | [**upload_ont**](docs/OntologyApi.md#upload_ont) | **POST** /ont/upload | Uploads an ontology file for subsequent registration
*OrganizationApi* | [**add_org**](docs/OrganizationApi.md#add_org) | **POST** /org | Registers an organization
*OrganizationApi* | [**delete_org**](docs/OrganizationApi.md#delete_org) | **DELETE** /org/{orgName} | Unregisters an organization
*OrganizationApi* | [**org_get**](docs/OrganizationApi.md#org_get) | **GET** /org | Gets information about registered organizations
*OrganizationApi* | [**org_org_name_get**](docs/OrganizationApi.md#org_org_name_get) | **GET** /org/{orgName} | Gets basic information of a particular organization
*OrganizationApi* | [**update_org**](docs/OrganizationApi.md#update_org) | **PUT** /org/{orgName} | Updates information about a registered organization
*TermApi* | [**add_term**](docs/TermApi.md#add_term) | **POST** /ont/term | Adds a term to an existing ORR vocabulary
*TermApi* | [**term_get**](docs/TermApi.md#term_get) | **GET** /term | Simplified semantic search queries against the triple store
*TriplestoreApi* | [**get_triplestore_size**](docs/TriplestoreApi.md#get_triplestore_size) | **GET** /ts | Gets the size of the store or the size of a particular named graph
*TriplestoreApi* | [**load_ont_in_triplestore**](docs/TriplestoreApi.md#load_ont_in_triplestore) | **POST** /ts | Loads an ontology in the triplestore
*TriplestoreApi* | [**reload_onts_in_triplestore**](docs/TriplestoreApi.md#reload_onts_in_triplestore) | **PUT** /ts | Reloads an ontology or all ontologies in the triplestore
*TriplestoreApi* | [**unload_onts_in_triplestore**](docs/TriplestoreApi.md#unload_onts_in_triplestore) | **DELETE** /ts | Unloads an ontology or all ontologies from the triplestore
*UserApi* | [**add_user**](docs/UserApi.md#add_user) | **POST** /user | Registers a user
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /user/{userName} | Unregisters a user
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /user/{userName} | Updates information about a registered user
*UserApi* | [**user_get**](docs/UserApi.md#user_get) | **GET** /user | Gets information about registered users
*UserApi* | [**user_user_name_get**](docs/UserApi.md#user_user_name_get) | **GET** /user/{userName} | Gets basic information of a particular user


## Documentation For Models

 - [Ont](docs/Ont.md)
 - [Org](docs/Org.md)
 - [OrgNew](docs/OrgNew.md)
 - [OrgUpdated](docs/OrgUpdated.md)
 - [PossibleOntologyInfo](docs/PossibleOntologyInfo.md)
 - [PostOnt](docs/PostOnt.md)
 - [PostOrg](docs/PostOrg.md)
 - [PostTerm](docs/PostTerm.md)
 - [PostUser](docs/PostUser.md)
 - [PutOnt](docs/PutOnt.md)
 - [PutOrg](docs/PutOrg.md)
 - [PutUser](docs/PutUser.md)
 - [UploadedFileInfo](docs/UploadedFileInfo.md)
 - [User](docs/User.md)

<img src="https://ci.appveyor.com/api/projects/status/32r7s2skrgm9ubva?svg=true" alt="Project Badge" width="300">

<img src="https://ci.appveyor.com/api/projects/status/32r7s2skrgm9ubva?svg=true&passingText=master%20-%20OK" alt="Project Badge">
## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author



