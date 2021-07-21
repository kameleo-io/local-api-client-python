# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Os(Model):
    """Os.

    All required parameters must be populated in order to send to Azure.

    :param family: Required. Family of the OS. Possible values are 'windows',
     'macos', 'linux', 'android', 'ios'.
    :type family: str
    :param version: Required. Version of the OS. For example it helps you
     determine the exact version of the macOS.
    :type version: str
    :param platform: Required. Platform of the OS. Tells if it runs on 64 bit
     or 32 bit or some other processor platform.
    :type platform: str
    """

    _validation = {
        'family': {'required': True},
        'version': {'required': True},
        'platform': {'required': True},
    }

    _attribute_map = {
        'family': {'key': 'family', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'platform': {'key': 'platform', 'type': 'str'},
    }

    def __init__(self, *, family: str, version: str, platform: str, **kwargs) -> None:
        super(Os, self).__init__(**kwargs)
        self.family = family
        self.version = version
        self.platform = platform
