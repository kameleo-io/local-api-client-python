# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WebRtcSpoofingOptions(Model):
    """When the WebRTC spoofing is set to manual these extra settings will be used
    as well.

    All required parameters must be populated in order to send to Azure.

    :param private_ip: Required. The WebRTC local IP address of the machine.
     It can be an obfuscated value as well.
    :type private_ip: str
    :param public_ip: Required. The WebRTC public IP address of the machine.
    :type public_ip: str
    """

    _validation = {
        'private_ip': {'required': True},
        'public_ip': {'required': True},
    }

    _attribute_map = {
        'private_ip': {'key': 'privateIp', 'type': 'str'},
        'public_ip': {'key': 'publicIp', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WebRtcSpoofingOptions, self).__init__(**kwargs)
        self.private_ip = kwargs.get('private_ip', None)
        self.public_ip = kwargs.get('public_ip', None)
