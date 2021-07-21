# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LoadProfileRequest(Model):
    """Tells where the profile should be loaded from.

    All required parameters must be populated in order to send to Azure.

    :param path: Required. The path where the profile should be loaded from
    :type path: str
    """

    _validation = {
        'path': {'required': True},
    }

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LoadProfileRequest, self).__init__(**kwargs)
        self.path = kwargs.get('path', None)
