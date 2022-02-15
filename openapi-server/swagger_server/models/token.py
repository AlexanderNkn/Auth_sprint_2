# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Token(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, access_token: str=None, refresh_token: str=None):  # noqa: E501
        """Token - a model defined in Swagger

        :param access_token: The access_token of this Token.  # noqa: E501
        :type access_token: str
        :param refresh_token: The refresh_token of this Token.  # noqa: E501
        :type refresh_token: str
        """
        self.swagger_types = {
            'access_token': str,
            'refresh_token': str
        }

        self.attribute_map = {
            'access_token': 'access_token',
            'refresh_token': 'refresh_token'
        }
        self._access_token = access_token
        self._refresh_token = refresh_token

    @classmethod
    def from_dict(cls, dikt) -> 'Token':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Token of this Token.  # noqa: E501
        :rtype: Token
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_token(self) -> str:
        """Gets the access_token of this Token.


        :return: The access_token of this Token.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token: str):
        """Sets the access_token of this Token.


        :param access_token: The access_token of this Token.
        :type access_token: str
        """

        self._access_token = access_token

    @property
    def refresh_token(self) -> str:
        """Gets the refresh_token of this Token.


        :return: The refresh_token of this Token.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token: str):
        """Sets the refresh_token of this Token.


        :param refresh_token: The refresh_token of this Token.
        :type refresh_token: str
        """

        self._refresh_token = refresh_token
