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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kameleo.local_api_client.models.browser import Browser
from kameleo.local_api_client.models.device import Device
from kameleo.local_api_client.models.os import Os
from kameleo.local_api_client.models.webgl_meta import WebglMeta
from typing import Optional, Set
from typing_extensions import Self

class Fingerprint(BaseModel):
    """
    Provides a full view of a fingerprint, which encapsulates real-world browser fingerprint configurations used to  instantiate virtual browser profiles.
    """ # noqa: E501
    version: Optional[StrictStr] = Field(description="The version of the fingerprint. As time passes new fingerprint versions will be introduced. It is recommended to use the latest one.")
    id: Optional[StrictStr] = Field(description="The unique identifier of the fingerprint. You can use this as a reference to create a new profile from this fingerprint.")
    user_agent: Optional[StrictStr] = Field(description="The user agent of the browser fingerprint.", alias="userAgent")
    device: Optional[Device] = Field(description="Information about the device of the fingerprint.")
    os: Optional[Os] = Field(description="Information about the OS of the fingerprint.")
    browser: Optional[Browser] = Field(description="Information about the browser of the fingerprint.")
    webgl_meta: Optional[WebglMeta] = Field(description="The GPU details extracted from WebGL parameters.", alias="webglMeta")
    resolution: Optional[StrictStr] = Field(description="The screen size of the device in pixels.")
    fonts: Optional[List[StrictStr]] = Field(description="A list of font types included in the profile.")
    __properties: ClassVar[List[str]] = ["version", "id", "userAgent", "device", "os", "browser", "webglMeta", "resolution", "fonts"]

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
        """Create an instance of Fingerprint from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of os
        if self.os:
            _dict['os'] = self.os.to_dict()
        # override the default output from pydantic by calling `to_dict()` of browser
        if self.browser:
            _dict['browser'] = self.browser.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webgl_meta
        if self.webgl_meta:
            _dict['webglMeta'] = self.webgl_meta.to_dict()
        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if user_agent (nullable) is None
        # and model_fields_set contains the field
        if self.user_agent is None and "user_agent" in self.model_fields_set:
            _dict['userAgent'] = None

        # set to None if device (nullable) is None
        # and model_fields_set contains the field
        if self.device is None and "device" in self.model_fields_set:
            _dict['device'] = None

        # set to None if os (nullable) is None
        # and model_fields_set contains the field
        if self.os is None and "os" in self.model_fields_set:
            _dict['os'] = None

        # set to None if browser (nullable) is None
        # and model_fields_set contains the field
        if self.browser is None and "browser" in self.model_fields_set:
            _dict['browser'] = None

        # set to None if webgl_meta (nullable) is None
        # and model_fields_set contains the field
        if self.webgl_meta is None and "webgl_meta" in self.model_fields_set:
            _dict['webglMeta'] = None

        # set to None if resolution (nullable) is None
        # and model_fields_set contains the field
        if self.resolution is None and "resolution" in self.model_fields_set:
            _dict['resolution'] = None

        # set to None if fonts (nullable) is None
        # and model_fields_set contains the field
        if self.fonts is None and "fonts" in self.model_fields_set:
            _dict['fonts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Fingerprint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "version": obj.get("version"),
            "id": obj.get("id"),
            "userAgent": obj.get("userAgent"),
            "device": Device.from_dict(obj["device"]) if obj.get("device") is not None else None,
            "os": Os.from_dict(obj["os"]) if obj.get("os") is not None else None,
            "browser": Browser.from_dict(obj["browser"]) if obj.get("browser") is not None else None,
            "webglMeta": WebglMeta.from_dict(obj["webglMeta"]) if obj.get("webglMeta") is not None else None,
            "resolution": obj.get("resolution"),
            "fonts": obj.get("fonts")
        })
        return _obj


