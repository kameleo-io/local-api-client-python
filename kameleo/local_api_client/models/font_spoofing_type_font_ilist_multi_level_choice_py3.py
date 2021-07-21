# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FontSpoofingTypeFontIListMultiLevelChoice(Model):
    """FontSpoofingTypeFontIListMultiLevelChoice.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. Possible values include: 'enabled', 'disabled'
    :type value: str or ~kameleo.local_api_client.models.enum
    :param extra:
    :type extra: list[str]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'extra': {'key': 'extra', 'type': '[str]'},
    }

    def __init__(self, *, value, extra=None, **kwargs) -> None:
        super(FontSpoofingTypeFontIListMultiLevelChoice, self).__init__(**kwargs)
        self.value = value
        self.extra = extra
