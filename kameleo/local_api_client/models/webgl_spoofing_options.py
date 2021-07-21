# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WebglSpoofingOptions(Model):
    """When the WebGL spoofing is set to noise these extra settings can be used to
    ovveride the values in the base profile.

    :param vendor: Unmasked vendor
    :type vendor: str
    :param renderer: Unmasked renderer
    :type renderer: str
    """

    _attribute_map = {
        'vendor': {'key': 'vendor', 'type': 'str'},
        'renderer': {'key': 'renderer', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WebglSpoofingOptions, self).__init__(**kwargs)
        self.vendor = kwargs.get('vendor', None)
        self.renderer = kwargs.get('renderer', None)
