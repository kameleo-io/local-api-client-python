# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GeolocationSpoofingTypeGeolocationSpoofingOptionsMultiLevelChoice(Model):
    """GeolocationSpoofingTypeGeolocationSpoofingOptionsMultiLevelChoice.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. Possible values include: 'automatic', 'manual',
     'block', 'off'
    :type value: str or ~kameleo.local_api_client.models.enum
    :param extra:
    :type extra: ~kameleo.local_api_client.models.GeolocationSpoofingOptions
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'extra': {'key': 'extra', 'type': 'GeolocationSpoofingOptions'},
    }

    def __init__(self, **kwargs):
        super(GeolocationSpoofingTypeGeolocationSpoofingOptionsMultiLevelChoice, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.extra = kwargs.get('extra', None)
