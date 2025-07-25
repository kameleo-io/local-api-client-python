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
from kameleo.local_api_client.models.audio_spoofing_type import AudioSpoofingType
from kameleo.local_api_client.models.canvas_spoofing_type import CanvasSpoofingType
from kameleo.local_api_client.models.device_memory_choice import DeviceMemoryChoice
from kameleo.local_api_client.models.fingerprint import Fingerprint
from kameleo.local_api_client.models.font_spoofing_type import FontSpoofingType
from kameleo.local_api_client.models.geolocation_choice import GeolocationChoice
from kameleo.local_api_client.models.hardware_concurrency_choice import HardwareConcurrencyChoice
from kameleo.local_api_client.models.password_manager_type import PasswordManagerType
from kameleo.local_api_client.models.profile_storage_location import ProfileStorageLocation
from kameleo.local_api_client.models.proxy_choice import ProxyChoice
from kameleo.local_api_client.models.screen_choice import ScreenChoice
from kameleo.local_api_client.models.status_response import StatusResponse
from kameleo.local_api_client.models.timezone_choice import TimezoneChoice
from kameleo.local_api_client.models.web_rtc_choice import WebRtcChoice
from kameleo.local_api_client.models.webgl_meta_choice import WebglMetaChoice
from kameleo.local_api_client.models.webgl_spoofing_type import WebglSpoofingType
from typing import Optional, Set
from typing_extensions import Self

class ProfileResponse(BaseModel):
    """
    ProfileResponse
    """ # noqa: E501
    id: StrictStr = Field(description="A unique identifier of the profile")
    name: Optional[StrictStr] = Field(description="Profile name property. The value obtained by file name for existing profiles. For new profiles the value is generated by a random name  generator.")
    tags: Optional[List[StrictStr]] = Field(description="Profile tags")
    created_at: datetime = Field(description="Date when the profile was created.", alias="createdAt")
    fingerprint: Optional[Fingerprint] = Field(description="Provides a full view of a fingerprint, which encapsulates real-world browser fingerprint configurations used to  instantiate virtual browser profiles.")
    canvas: CanvasSpoofingType = Field(description="Specifies how the canvas will be spoofed. Possible values:  'intelligent': Use intelligent canvas spoofing. This will result non-unique canvas fingerprints.  'noise': Add some noise to canvas generation.  'block': Completely block the 2D API.  'off': Turn off the spoofing, use the original settings.")
    webgl: WebglSpoofingType = Field(description="Specifies how the WebGL will be spoofed. Possible values:  'noise': Add some noise to the WebGL generation  'block': Completely block the 3D API  'off': Turn off the spoofing, use the original settings")
    webgl_meta: Optional[WebglMetaChoice] = Field(description="Sets how the WebGL Vendor and Renderer will be spoofed. Possible values:  'automatic': The vendor and renderer values comes from the fingerprint.  'manual': Manually set the vendor and renderer values.  'off': Turn off the spoofing, use the original settings", alias="webglMeta")
    audio: AudioSpoofingType = Field(description="Specifies how the audio will be spoofed. Possible values:  'noise': Add some noise to the Audio generation  'block': Completely block the Audio API  'off': Turn off the spoofing, use the original settings")
    timezone: Optional[TimezoneChoice] = Field(description="Sets how the Timezone will be spoofed. Values can be 'automatic', 'manual', 'off'.")
    geolocation: Optional[GeolocationChoice] = Field(description="Sets how the Geolocation will be spoofed. Values can be 'automatic', 'manual', 'block', 'off'.")
    proxy: Optional[ProxyChoice] = Field(description="Proxy connection settings of the profiles. Values can be 'none', 'http', 'socks5', 'ssh'. When it is not set to none, a server is provided.")
    web_rtc: Optional[WebRtcChoice] = Field(description="Sets how the WebRTC will be spoofed. Values can be 'automatic', 'manual', 'block', 'off'.", alias="webRtc")
    fonts: FontSpoofingType = Field(description="Specifies how the fonts will be spoofed. Possible values:  'automatic': Spoof fonts based on the browser fingerpint.  'off': Don't spoof fonts, use the real fonts of your machine.")
    screen: Optional[ScreenChoice] = Field(description="Sets how the Screen will be spoofed. Values can be 'automatic', 'manual', 'off'. When value is set to manual, a ScreenSize must be provided")
    hardware_concurrency: Optional[HardwareConcurrencyChoice] = Field(description="Sets how the Hardware Concurrency will be spoofed. Values can be 'automatic', 'manual', 'off'. When value is set to manual, a  HardwareConcurrencyType must be provided (valid values:1, 2, 4, 8, 12, 16)", alias="hardwareConcurrency")
    device_memory: Optional[DeviceMemoryChoice] = Field(description="Sets the level of device memory spoofing. Values can be 'automatic', 'manual', 'off'.  When value is set to manual, a specific amount of device memory must be provided (valid values: 0.25, 0.5, 1, 2, 4, 8)", alias="deviceMemory")
    language: Optional[StrictStr] = Field(description="Language of the profile as ISO 639-1 language and optionally ISO 3166-1 region code.")
    start_page: Optional[StrictStr] = Field(description="This website will be opened in the browser when the profile launches.", alias="startPage")
    password_manager: PasswordManagerType = Field(description="Defines whether the browser can save login credentials. Possible values are:  'enabled': Credential saving is allowed.  'disabled': Credential saving is blocked.", alias="passwordManager")
    extensions: Optional[List[StrictStr]] = Field(description="A list of extensions or addons that will be loaded to the profile when the profile is started. For chrome and edge use CRX3 format  extensions. For firefox use signed xpi format addons.")
    notes: Optional[StrictStr] = Field(description="A free text including any notes written by the user.")
    status: Optional[StatusResponse] = Field(description="Status information about the profile.")
    storage: Optional[ProfileStorageLocation] = Field(default=None, description="Profile storage property which determines where the profile is stored. The default value is 'local'. When the value is changed the profile  will be migrated.")
    folder_id: Optional[StrictStr] = Field(default=None, description="A unique identifier of the containing folder or empty (00000000-0000-0000-0000-000000000000) if it is not in folder.", alias="folderId")
    __properties: ClassVar[List[str]] = ["id", "name", "tags", "createdAt", "fingerprint", "canvas", "webgl", "webglMeta", "audio", "timezone", "geolocation", "proxy", "webRtc", "fonts", "screen", "hardwareConcurrency", "deviceMemory", "language", "startPage", "passwordManager", "extensions", "notes", "status", "storage", "folderId"]

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
        """Create an instance of ProfileResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fingerprint
        if self.fingerprint:
            _dict['fingerprint'] = self.fingerprint.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webgl_meta
        if self.webgl_meta:
            _dict['webglMeta'] = self.webgl_meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timezone
        if self.timezone:
            _dict['timezone'] = self.timezone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geolocation
        if self.geolocation:
            _dict['geolocation'] = self.geolocation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of proxy
        if self.proxy:
            _dict['proxy'] = self.proxy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of web_rtc
        if self.web_rtc:
            _dict['webRtc'] = self.web_rtc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of screen
        if self.screen:
            _dict['screen'] = self.screen.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hardware_concurrency
        if self.hardware_concurrency:
            _dict['hardwareConcurrency'] = self.hardware_concurrency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device_memory
        if self.device_memory:
            _dict['deviceMemory'] = self.device_memory.to_dict()
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

        # set to None if fingerprint (nullable) is None
        # and model_fields_set contains the field
        if self.fingerprint is None and "fingerprint" in self.model_fields_set:
            _dict['fingerprint'] = None

        # set to None if webgl_meta (nullable) is None
        # and model_fields_set contains the field
        if self.webgl_meta is None and "webgl_meta" in self.model_fields_set:
            _dict['webglMeta'] = None

        # set to None if timezone (nullable) is None
        # and model_fields_set contains the field
        if self.timezone is None and "timezone" in self.model_fields_set:
            _dict['timezone'] = None

        # set to None if geolocation (nullable) is None
        # and model_fields_set contains the field
        if self.geolocation is None and "geolocation" in self.model_fields_set:
            _dict['geolocation'] = None

        # set to None if proxy (nullable) is None
        # and model_fields_set contains the field
        if self.proxy is None and "proxy" in self.model_fields_set:
            _dict['proxy'] = None

        # set to None if web_rtc (nullable) is None
        # and model_fields_set contains the field
        if self.web_rtc is None and "web_rtc" in self.model_fields_set:
            _dict['webRtc'] = None

        # set to None if screen (nullable) is None
        # and model_fields_set contains the field
        if self.screen is None and "screen" in self.model_fields_set:
            _dict['screen'] = None

        # set to None if hardware_concurrency (nullable) is None
        # and model_fields_set contains the field
        if self.hardware_concurrency is None and "hardware_concurrency" in self.model_fields_set:
            _dict['hardwareConcurrency'] = None

        # set to None if device_memory (nullable) is None
        # and model_fields_set contains the field
        if self.device_memory is None and "device_memory" in self.model_fields_set:
            _dict['deviceMemory'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if start_page (nullable) is None
        # and model_fields_set contains the field
        if self.start_page is None and "start_page" in self.model_fields_set:
            _dict['startPage'] = None

        # set to None if extensions (nullable) is None
        # and model_fields_set contains the field
        if self.extensions is None and "extensions" in self.model_fields_set:
            _dict['extensions'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

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
        """Create an instance of ProfileResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "tags": obj.get("tags"),
            "createdAt": obj.get("createdAt"),
            "fingerprint": Fingerprint.from_dict(obj["fingerprint"]) if obj.get("fingerprint") is not None else None,
            "canvas": obj.get("canvas"),
            "webgl": obj.get("webgl"),
            "webglMeta": WebglMetaChoice.from_dict(obj["webglMeta"]) if obj.get("webglMeta") is not None else None,
            "audio": obj.get("audio"),
            "timezone": TimezoneChoice.from_dict(obj["timezone"]) if obj.get("timezone") is not None else None,
            "geolocation": GeolocationChoice.from_dict(obj["geolocation"]) if obj.get("geolocation") is not None else None,
            "proxy": ProxyChoice.from_dict(obj["proxy"]) if obj.get("proxy") is not None else None,
            "webRtc": WebRtcChoice.from_dict(obj["webRtc"]) if obj.get("webRtc") is not None else None,
            "fonts": obj.get("fonts"),
            "screen": ScreenChoice.from_dict(obj["screen"]) if obj.get("screen") is not None else None,
            "hardwareConcurrency": HardwareConcurrencyChoice.from_dict(obj["hardwareConcurrency"]) if obj.get("hardwareConcurrency") is not None else None,
            "deviceMemory": DeviceMemoryChoice.from_dict(obj["deviceMemory"]) if obj.get("deviceMemory") is not None else None,
            "language": obj.get("language"),
            "startPage": obj.get("startPage"),
            "passwordManager": obj.get("passwordManager"),
            "extensions": obj.get("extensions"),
            "notes": obj.get("notes"),
            "status": StatusResponse.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "storage": obj.get("storage"),
            "folderId": obj.get("folderId")
        })
        return _obj


