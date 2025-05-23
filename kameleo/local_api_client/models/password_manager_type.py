# coding: utf-8

"""
    kameleo-local-api

    You can use the following API endpoints to communicate with the local running Kameleo programmatically.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PasswordManagerType(str, Enum):
    """
    Defines whether the browser can save login credentials. Possible values are:  'enabled': Credential saving is allowed.  'disabled': Credential saving is blocked.
    """

    """
    allowed enum values
    """
    ENABLED = 'enabled'
    DISABLED = 'disabled'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PasswordManagerType from a JSON string"""
        return cls(json.loads(json_str))


