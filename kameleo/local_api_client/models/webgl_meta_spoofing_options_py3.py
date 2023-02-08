# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WebglMetaSpoofingOptions(Model):
    """When the WebGL Meta spoofing is used, these settings can override the
    values in the base profile.

    :param vendor: Unmasked vendor
    :type vendor: str
    :param renderer: Unmasked renderer
    :type renderer: str
    """

    _attribute_map = {
        'vendor': {'key': 'vendor', 'type': 'str'},
        'renderer': {'key': 'renderer', 'type': 'str'},
    }

    def __init__(self, *, vendor: str=None, renderer: str=None, **kwargs) -> None:
        super(WebglMetaSpoofingOptions, self).__init__(**kwargs)
        self.vendor = vendor
        self.renderer = renderer
