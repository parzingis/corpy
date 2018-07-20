# coding: utf-8

"""
    ORR API Documentation

    The main ORR documentation is located at: https://mmisw.org/orrdoc/  __Please note__: - The ORR API is approaching a stable version but is still work in progress.   Please [let us know](https://github.com/mmisw/mmiorr-docs/issues) if you have any   questions or suggestions.  - Besides the documentation itself, this page lets you directly exercise and test the API.   Click on any operation header below to learn more details about it, and see a \"Try it out\" button.  - You can click on the \"Authorize\" button at the top right of this page   (or the `!` icon under the particular operation)   to retrieve an authentication token corresponding to your ORR instance credentials (username and password).   Once authorized, the authentication token will be automatically included in the corresponding request.   You will be able to not only perform the basic `GET` operations,   but also see expanded responses according to your access privileges   as well as perform other operations.  - The \"Try it out\" button will also show the corresponding API call that you can submit   from the command line using [`curl`](https://curl.haxx.se/).  - This API includes administrative operations related with the triple store.   The SPARQL endpoint itself   (located at `http://cor.esipfed.org/sparql` for the MMI ORR instance)   is not described here.   (General SPARQL information can be found [here](https://en.wikipedia.org/wiki/SPARQL),   and regarding the current service used by the ORR to support the SPARQL interface   [here](http://franz.com/agraph/support/documentation/current/http-protocol.html).)  - Actual requests from this page are against the specific endpoint at   `http://cor.esipfed.org/ont`. 

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PostOnt(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'iri': 'str',
        'original_iri': 'str',
        'name': 'str',
        'org_name': 'str',
        'visibility': 'str',
        'status': 'str',
        'user_name': 'str',
        'uploaded_filename': 'str',
        'uploaded_format': 'str',
        'contents': 'str',
        'format': 'str'
    }

    attribute_map = {
        'iri': 'iri',
        'original_iri': 'originalIri',
        'name': 'name',
        'org_name': 'orgName',
        'visibility': 'visibility',
        'status': 'status',
        'user_name': 'userName',
        'uploaded_filename': 'uploadedFilename',
        'uploaded_format': 'uploadedFormat',
        'contents': 'contents',
        'format': 'format'
    }

    def __init__(self, iri=None, original_iri=None, name=None, org_name=None, visibility=None, status=None, user_name=None, uploaded_filename=None, uploaded_format=None, contents=None, format=None):
        """
        PostOnt - a model defined in Swagger
        """

        self._iri = None
        self._original_iri = None
        self._name = None
        self._org_name = None
        self._visibility = None
        self._status = None
        self._user_name = None
        self._uploaded_filename = None
        self._uploaded_format = None
        self._contents = None
        self._format = None

        if iri is not None:
          self.iri = iri
        if original_iri is not None:
          self.original_iri = original_iri
        if name is not None:
          self.name = name
        if org_name is not None:
          self.org_name = org_name
        if visibility is not None:
          self.visibility = visibility
        if status is not None:
          self.status = status
        if user_name is not None:
          self.user_name = user_name
        if uploaded_filename is not None:
          self.uploaded_filename = uploaded_filename
        if uploaded_format is not None:
          self.uploaded_format = uploaded_format
        if contents is not None:
          self.contents = contents
        if format is not None:
          self.format = format

    @property
    def iri(self):
        """
        Gets the iri of this PostOnt.
        The IRI of the ontology. 

        :return: The iri of this PostOnt.
        :rtype: str
        """
        return self._iri

    @iri.setter
    def iri(self, iri):
        """
        Sets the iri of this PostOnt.
        The IRI of the ontology. 

        :param iri: The iri of this PostOnt.
        :type: str
        """

        self._iri = iri

    @property
    def original_iri(self):
        """
        Gets the original_iri of this PostOnt.
        In case of a fully-hosted registration, enter this field to indicate the original IRI in the provided contents to be used for the \"migration\" of corresponding entities to the new IRI. 

        :return: The original_iri of this PostOnt.
        :rtype: str
        """
        return self._original_iri

    @original_iri.setter
    def original_iri(self, original_iri):
        """
        Sets the original_iri of this PostOnt.
        In case of a fully-hosted registration, enter this field to indicate the original IRI in the provided contents to be used for the \"migration\" of corresponding entities to the new IRI. 

        :param original_iri: The original_iri of this PostOnt.
        :type: str
        """

        self._original_iri = original_iri

    @property
    def name(self):
        """
        Gets the name of this PostOnt.
        The name for the ontology. If omitted, the ORR will try to get this information from standard metadata in the submitted ontology contents. 

        :return: The name of this PostOnt.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PostOnt.
        The name for the ontology. If omitted, the ORR will try to get this information from standard metadata in the submitted ontology contents. 

        :param name: The name of this PostOnt.
        :type: str
        """

        self._name = name

    @property
    def org_name(self):
        """
        Gets the org_name of this PostOnt.
        ID of the organization that will own the ontology registration. If omitted, the owner will be the submitting user. 

        :return: The org_name of this PostOnt.
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """
        Sets the org_name of this PostOnt.
        ID of the organization that will own the ontology registration. If omitted, the owner will be the submitting user. 

        :param org_name: The org_name of this PostOnt.
        :type: str
        """

        self._org_name = org_name

    @property
    def visibility(self):
        """
        Gets the visibility of this PostOnt.
        One of: `owner` or `public`. The default visibility is `owner`. 

        :return: The visibility of this PostOnt.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """
        Sets the visibility of this PostOnt.
        One of: `owner` or `public`. The default visibility is `owner`. 

        :param visibility: The visibility of this PostOnt.
        :type: str
        """

        self._visibility = visibility

    @property
    def status(self):
        """
        Gets the status of this PostOnt.
        One of: `draft`, `unstable`, `testing`, `stable`,  `deprecated`, `archaic`. There's no default value. 

        :return: The status of this PostOnt.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PostOnt.
        One of: `draft`, `unstable`, `testing`, `stable`,  `deprecated`, `archaic`. There's no default value. 

        :param status: The status of this PostOnt.
        :type: str
        """

        self._status = status

    @property
    def user_name(self):
        """
        Gets the user_name of this PostOnt.
        Registered user making the request. 

        :return: The user_name of this PostOnt.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this PostOnt.
        Registered user making the request. 

        :param user_name: The user_name of this PostOnt.
        :type: str
        """

        self._user_name = user_name

    @property
    def uploaded_filename(self):
        """
        Gets the uploaded_filename of this PostOnt.
        Name of file previously uploaded via prior `POST /ont/upload` request. 

        :return: The uploaded_filename of this PostOnt.
        :rtype: str
        """
        return self._uploaded_filename

    @uploaded_filename.setter
    def uploaded_filename(self, uploaded_filename):
        """
        Sets the uploaded_filename of this PostOnt.
        Name of file previously uploaded via prior `POST /ont/upload` request. 

        :param uploaded_filename: The uploaded_filename of this PostOnt.
        :type: str
        """

        self._uploaded_filename = uploaded_filename

    @property
    def uploaded_format(self):
        """
        Gets the uploaded_format of this PostOnt.
        Format of the file previously uploaded via prior `POST /ont/upload` request. 

        :return: The uploaded_format of this PostOnt.
        :rtype: str
        """
        return self._uploaded_format

    @uploaded_format.setter
    def uploaded_format(self, uploaded_format):
        """
        Sets the uploaded_format of this PostOnt.
        Format of the file previously uploaded via prior `POST /ont/upload` request. 

        :param uploaded_format: The uploaded_format of this PostOnt.
        :type: str
        """

        self._uploaded_format = uploaded_format

    @property
    def contents(self):
        """
        Gets the contents of this PostOnt.
        Direct contents of the ontology. 

        :return: The contents of this PostOnt.
        :rtype: str
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """
        Sets the contents of this PostOnt.
        Direct contents of the ontology. 

        :param contents: The contents of this PostOnt.
        :type: str
        """

        self._contents = contents

    @property
    def format(self):
        """
        Gets the format of this PostOnt.
        Format of the `contents`. 

        :return: The format of this PostOnt.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this PostOnt.
        Format of the `contents`. 

        :param format: The format of this PostOnt.
        :type: str
        """

        self._format = format

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PostOnt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
