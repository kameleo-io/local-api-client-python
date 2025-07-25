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
from kameleo.local_api_client.models.browser import Browser
from kameleo.local_api_client.models.device import Device
from kameleo.local_api_client.models.os import Os
from kameleo.local_api_client.models.profile_storage_location import ProfileStorageLocation
from kameleo.local_api_client.models.proxy_choice import ProxyChoice
from kameleo.local_api_client.models.status_response import StatusResponse
from typing import Optional, Set
from typing_extensions import Self

class ProfilePreview(BaseModel):
    """
    A preview about the profile with some of its properties.
    """ # noqa: E501
    id: StrictStr = Field(description="A unique identifier of the profile")
    name: Optional[StrictStr] = Field(description="The name of the profile")
    tags: Optional[List[StrictStr]] = Field(description="Profile tags")
    proxy: Optional[ProxyChoice] = Field(description="Proxy connection settings of the profiles. Values can be 'none', 'http', 'socks5', 'ssh'. When it is not set to none, a server is provided.")
    created_at: datetime = Field(description="Date when the profile was created.", alias="createdAt")
    device: Optional[Device] = Field(description="Device information about the profile. This is derived from the fingerprint.")
    os: Optional[Os] = Field(description="Information about the OS of the profile. This is derived from the fingerprint.")
    browser: Optional[Browser] = Field(description="Information about the browser of the profile. This is derived from the fingerprint.")
    language: Optional[StrictStr] = Field(description="Language of the profile as ISO 639-1 language and optionally ISO 3166-1 region code.")
    status: Optional[StatusResponse] = Field(description="Status information about the profile.")
    storage: Optional[ProfileStorageLocation] = Field(default=None, description="Profile storage property which determines where the profile is stored. The default value is 'local'. When the value is changed the profile  will be migrated.")
    folder_id: Optional[StrictStr] = Field(default=None, description="A unique identifier of the containing folder, or empty (00000000-0000-0000-0000-000000000000) if not in a folder.  This will always be empty for locally stored profiles, as only cloud profiles can be added to folders.", alias="folderId")
    __properties: ClassVar[List[str]] = ["id", "name", "tags", "proxy", "createdAt", "device", "os", "browser", "language", "status", "storage", "folderId"]

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
        """Create an instance of ProfilePreview from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of proxy
        if self.proxy:
            _dict['proxy'] = self.proxy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of os
        if self.os:
            _dict['os'] = self.os.to_dict()
        # override the default output from pydantic by calling `to_dict()` of browser
        if self.browser:
            _dict['browser'] = self.browser.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if proxy (nullable) is None
        # and model_fields_set contains the field
        if self.proxy is None and "proxy" in self.model_fields_set:
            _dict['proxy'] = None

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

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.folder_id is None and "folder_id" in self.model_fields_set:
            _dict['folderId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfilePreview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "tags": obj.get("tags"),
            "proxy": ProxyChoice.from_dict(obj["proxy"]) if obj.get("proxy") is not None else None,
            "createdAt": obj.get("createdAt"),
            "device": Device.from_dict(obj["device"]) if obj.get("device") is not None else None,
            "os": Os.from_dict(obj["os"]) if obj.get("os") is not None else None,
            "browser": Browser.from_dict(obj["browser"]) if obj.get("browser") is not None else None,
            "language": obj.get("language"),
            "status": StatusResponse.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "storage": obj.get("storage"),
            "folderId": obj.get("folderId")
        })
        return _obj


