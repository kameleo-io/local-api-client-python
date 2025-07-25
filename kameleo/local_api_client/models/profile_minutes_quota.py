# coding: utf-8

"""
    kameleo-local-api

    You can use the following API endpoints to communicate with the local running Kameleo programmatically.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProfileMinutesQuota(BaseModel):
    """
    ProfileMinutesQuota
    """ # noqa: E501
    current_usage: Optional[StrictStr] = Field(default=None, alias="currentUsage")
    maximum_limit: Optional[StrictStr] = Field(default=None, alias="maximumLimit")
    next_reset_at: Optional[datetime] = Field(default=None, alias="nextResetAt")
    __properties: ClassVar[List[str]] = ["currentUsage", "maximumLimit", "nextResetAt"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ProfileMinutesQuota from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if maximum_limit (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_limit is None and "maximum_limit" in self.model_fields_set:
            _dict['maximumLimit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfileMinutesQuota from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currentUsage": obj.get("currentUsage"),
            "maximumLimit": obj.get("maximumLimit"),
            "nextResetAt": obj.get("nextResetAt")
        })
        return _obj


