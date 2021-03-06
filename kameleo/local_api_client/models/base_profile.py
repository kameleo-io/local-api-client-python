# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BaseProfile(Model):
    """Representation of a base profile which is used to build profiles from.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. The version of the base profile. As time passes
     new base profile versions will be introduced. It is recommended to use the
     latest one.
    :type version: str
    :param id: Required. The unique identifier of the base profile. You can
     use this as a reference to create a new profile from this base profile.
    :type id: str
    :param device: Required.
    :type device: ~kameleo.local_api_client.models.Device
    :param os: Required.
    :type os: ~kameleo.local_api_client.models.Os
    :param browser: Required.
    :type browser: ~kameleo.local_api_client.models.Browser
    :param language: Required. Language of the base profile. Using ISO 639-1
     language codes.
    :type language: str
    :param resolution: Required. The screen size of the device in pixels
    :type resolution: str
    :param fonts: Required. A list of font types included in the profile
    :type fonts: list[str]
    :param plugins: Required. A list of plugins included in the profile
    :type plugins: list[str]
    """

    _validation = {
        'version': {'required': True},
        'id': {'required': True},
        'device': {'required': True},
        'os': {'required': True},
        'browser': {'required': True},
        'language': {'required': True},
        'resolution': {'required': True},
        'fonts': {'required': True},
        'plugins': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'device': {'key': 'device', 'type': 'Device'},
        'os': {'key': 'os', 'type': 'Os'},
        'browser': {'key': 'browser', 'type': 'Browser'},
        'language': {'key': 'language', 'type': 'str'},
        'resolution': {'key': 'resolution', 'type': 'str'},
        'fonts': {'key': 'fonts', 'type': '[str]'},
        'plugins': {'key': 'plugins', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(BaseProfile, self).__init__(**kwargs)
        self.version = kwargs.get('version', None)
        self.id = kwargs.get('id', None)
        self.device = kwargs.get('device', None)
        self.os = kwargs.get('os', None)
        self.browser = kwargs.get('browser', None)
        self.language = kwargs.get('language', None)
        self.resolution = kwargs.get('resolution', None)
        self.fonts = kwargs.get('fonts', None)
        self.plugins = kwargs.get('plugins', None)
