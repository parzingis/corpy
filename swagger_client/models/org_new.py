# coding: utf-8

"""
    ORR API Documentation

    The main ORR documentation is located at: https://mmisw.org/orrdoc/  __Please note__: - The ORR API is approaching a stable version but is still work in progress.   Please [let us know](https://github.com/mmisw/mmiorr-docs/issues) if you have any   questions or suggestions.  - Besides the documentation itself, this page lets you directly exercise and test the API.   Click on any operation header below to learn more details about it, and see a \"Try it out\" button.  - You can click on the \"Authorize\" button at the top right of this page   (or the `!` icon under the particular operation)   to retrieve an authentication token corresponding to your ORR instance credentials (username and password).   Once authorized, the authentication token will be automatically included in the corresponding request.   You will be able to not only perform the basic `GET` operations,   but also see expanded responses according to your access privileges   as well as perform other operations.  - The \"Try it out\" button will also show the corresponding API call that you can submit   from the command line using [`curl`](https://curl.haxx.se/).  - This API includes administrative operations related with the triple store.   The SPARQL endpoint itself   (located at `https://mmisw.org/sparql` for the MMI ORR instance)   is not described here.   (General SPARQL information can be found [here](https://en.wikipedia.org/wiki/SPARQL),   and regarding the current service used by the ORR to support the SPARQL interface   [here](http://franz.com/agraph/support/documentation/current/http-protocol.html).)  - Actual requests from this page are against the specific endpoint at   `https://mmisw.org/ont`. 

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OrgNew(object):
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
        'org_name': 'str',
        'name': 'str',
        'url': 'str',
        'members': 'list[str]',
        'registered_by': 'str'
    }

    attribute_map = {
        'org_name': 'orgName',
        'name': 'name',
        'url': 'url',
        'members': 'members',
        'registered_by': 'registeredBy'
    }

    def __init__(self, org_name=None, name=None, url=None, members=None, registered_by=None):
        """
        OrgNew - a model defined in Swagger
        """

        self._org_name = None
        self._name = None
        self._url = None
        self._members = None
        self._registered_by = None

        if org_name is not None:
          self.org_name = org_name
        if name is not None:
          self.name = name
        if url is not None:
          self.url = url
        if members is not None:
          self.members = members
        if registered_by is not None:
          self.registered_by = registered_by

    @property
    def org_name(self):
        """
        Gets the org_name of this OrgNew.

        :return: The org_name of this OrgNew.
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """
        Sets the org_name of this OrgNew.

        :param org_name: The org_name of this OrgNew.
        :type: str
        """

        self._org_name = org_name

    @property
    def name(self):
        """
        Gets the name of this OrgNew.

        :return: The name of this OrgNew.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrgNew.

        :param name: The name of this OrgNew.
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """
        Gets the url of this OrgNew.

        :return: The url of this OrgNew.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this OrgNew.

        :param url: The url of this OrgNew.
        :type: str
        """

        self._url = url

    @property
    def members(self):
        """
        Gets the members of this OrgNew.

        :return: The members of this OrgNew.
        :rtype: list[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this OrgNew.

        :param members: The members of this OrgNew.
        :type: list[str]
        """

        self._members = members

    @property
    def registered_by(self):
        """
        Gets the registered_by of this OrgNew.

        :return: The registered_by of this OrgNew.
        :rtype: str
        """
        return self._registered_by

    @registered_by.setter
    def registered_by(self, registered_by):
        """
        Sets the registered_by of this OrgNew.

        :param registered_by: The registered_by of this OrgNew.
        :type: str
        """

        self._registered_by = registered_by

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
        if not isinstance(other, OrgNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
