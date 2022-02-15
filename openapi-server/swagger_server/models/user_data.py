# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, birth_date: str=None, city: str=None, email: str=None, first_name: str=None, last_name: str=None, phone: str=None):  # noqa: E501
        """UserData - a model defined in Swagger

        :param birth_date: The birth_date of this UserData.  # noqa: E501
        :type birth_date: str
        :param city: The city of this UserData.  # noqa: E501
        :type city: str
        :param email: The email of this UserData.  # noqa: E501
        :type email: str
        :param first_name: The first_name of this UserData.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this UserData.  # noqa: E501
        :type last_name: str
        :param phone: The phone of this UserData.  # noqa: E501
        :type phone: str
        """
        self.swagger_types = {
            'birth_date': str,
            'city': str,
            'email': str,
            'first_name': str,
            'last_name': str,
            'phone': str
        }

        self.attribute_map = {
            'birth_date': 'birth_date',
            'city': 'city',
            'email': 'email',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'phone': 'phone'
        }
        self._birth_date = birth_date
        self._city = city
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone

    @classmethod
    def from_dict(cls, dikt) -> 'UserData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserData of this UserData.  # noqa: E501
        :rtype: UserData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def birth_date(self) -> str:
        """Gets the birth_date of this UserData.


        :return: The birth_date of this UserData.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date: str):
        """Sets the birth_date of this UserData.


        :param birth_date: The birth_date of this UserData.
        :type birth_date: str
        """

        self._birth_date = birth_date

    @property
    def city(self) -> str:
        """Gets the city of this UserData.


        :return: The city of this UserData.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city of this UserData.


        :param city: The city of this UserData.
        :type city: str
        """

        self._city = city

    @property
    def email(self) -> str:
        """Gets the email of this UserData.


        :return: The email of this UserData.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UserData.


        :param email: The email of this UserData.
        :type email: str
        """

        self._email = email

    @property
    def first_name(self) -> str:
        """Gets the first_name of this UserData.


        :return: The first_name of this UserData.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this UserData.


        :param first_name: The first_name of this UserData.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this UserData.


        :return: The last_name of this UserData.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this UserData.


        :param last_name: The last_name of this UserData.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def phone(self) -> str:
        """Gets the phone of this UserData.


        :return: The phone of this UserData.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this UserData.


        :param phone: The phone of this UserData.
        :type phone: str
        """

        self._phone = phone
