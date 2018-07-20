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


class UploadedFileInfo(object):
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
        'user_name': 'str',
        'filename': 'str',
        'format': 'str',
        'possible_ontology_iris': 'dict(str, PossibleOntologyInfo)'
    }

    attribute_map = {
        'user_name': 'userName',
        'filename': 'filename',
        'format': 'format',
        'possible_ontology_iris': 'possibleOntologyIris'
    }

    def __init__(self, user_name=None, filename=None, format=None, possible_ontology_iris=None):
        """
        UploadedFileInfo - a model defined in Swagger
        """

        self._user_name = None
        self._filename = None
        self._format = None
        self._possible_ontology_iris = None

        if user_name is not None:
          self.user_name = user_name
        if filename is not None:
          self.filename = filename
        if format is not None:
          self.format = format
        if possible_ontology_iris is not None:
          self.possible_ontology_iris = possible_ontology_iris

    @property
    def user_name(self):
        """
        Gets the user_name of this UploadedFileInfo.
        The user that requested the upload.

        :return: The user_name of this UploadedFileInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this UploadedFileInfo.
        The user that requested the upload.

        :param user_name: The user_name of this UploadedFileInfo.
        :type: str
        """

        self._user_name = user_name

    @property
    def filename(self):
        """
        Gets the filename of this UploadedFileInfo.
        The name associated with the file.

        :return: The filename of this UploadedFileInfo.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this UploadedFileInfo.
        The name associated with the file.

        :param filename: The filename of this UploadedFileInfo.
        :type: str
        """

        self._filename = filename

    @property
    def format(self):
        """
        Gets the format of this UploadedFileInfo.
        The format of the file.

        :return: The format of this UploadedFileInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this UploadedFileInfo.
        The format of the file.

        :param format: The format of this UploadedFileInfo.
        :type: str
        """

        self._format = format

    @property
    def possible_ontology_iris(self):
        """
        Gets the possible_ontology_iris of this UploadedFileInfo.
        The format of the file.

        :return: The possible_ontology_iris of this UploadedFileInfo.
        :rtype: dict(str, PossibleOntologyInfo)
        """
        return self._possible_ontology_iris

    @possible_ontology_iris.setter
    def possible_ontology_iris(self, possible_ontology_iris):
        """
        Sets the possible_ontology_iris of this UploadedFileInfo.
        The format of the file.

        :param possible_ontology_iris: The possible_ontology_iris of this UploadedFileInfo.
        :type: dict(str, PossibleOntologyInfo)
        """

        self._possible_ontology_iris = possible_ontology_iris

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
        if not isinstance(other, UploadedFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
