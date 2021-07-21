# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UserInfoResponse(Model):
    """UserInfoResponse.

    All required parameters must be populated in order to send to Azure.

    :param user_id: Required. The guid of the user.
    :type user_id: str
    :param email: Required. The email address of the authenticated user.
    :type email: str
    :param subscription_end: Required. The end date of the authenticated
     user's current subscription.
    :type subscription_end: datetime
    :param capabilities: Required. The capabilities that the authenticated
     user owns thanks to his current subscription.
    :type capabilities: list[str]
    :param last_app_login: The last date when the user authenticated by the
     app.
    :type last_app_login: datetime
    """

    _validation = {
        'user_id': {'required': True},
        'email': {'required': True},
        'subscription_end': {'required': True},
        'capabilities': {'required': True},
    }

    _attribute_map = {
        'user_id': {'key': 'userId', 'type': 'str'},
        'email': {'key': 'email', 'type': 'str'},
        'subscription_end': {'key': 'subscriptionEnd', 'type': 'iso-8601'},
        'capabilities': {'key': 'capabilities', 'type': '[str]'},
        'last_app_login': {'key': 'lastAppLogin', 'type': 'iso-8601'},
    }

    def __init__(self, *, user_id: str, email: str, subscription_end, capabilities, last_app_login=None, **kwargs) -> None:
        super(UserInfoResponse, self).__init__(**kwargs)
        self.user_id = user_id
        self.email = email
        self.subscription_end = subscription_end
        self.capabilities = capabilities
        self.last_app_login = last_app_login
