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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from kameleo.local_api_client.models.share_access_request import ShareAccessRequest
from typing import Optional, Set
from typing_extensions import Self

class ShareGroupRequest(BaseModel):
    """
    ShareGroupRequest
    """ # noqa: E501
    share_accesses: List[ShareAccessRequest] = Field(description="List of share accesses to the folder.", alias="shareAccesses")
    __properties: ClassVar[List[str]] = ["shareAccesses"]

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
        """Create an instance of ShareGroupRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in share_accesses (list)
        _items = []
        if self.share_accesses:
            for _item_share_accesses in self.share_accesses:
                if _item_share_accesses:
                    _items.append(_item_share_accesses.to_dict())
            _dict['shareAccesses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShareGroupRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shareAccesses": [ShareAccessRequest.from_dict(_item) for _item in obj["shareAccesses"]] if obj.get("shareAccesses") is not None else None
        })
        return _obj


