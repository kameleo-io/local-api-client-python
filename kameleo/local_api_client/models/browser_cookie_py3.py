# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BrowserCookie(Model):
    """Representation of a cookie.

    All required parameters must be populated in order to send to Azure.

    :param domain: Required. The domain attribute signifies the domain for
     which the cookie is valid and can be submitted with every request for this
     domain or its subdomains. If this attribute is not specified, then the
     hostname of the originating server is used as the default value.
    :type domain: str
    :param name: Required. The name for the Cookie.
    :type name: str
    :param path: Required. The path attribute indicates a URL path that must
     exist in the requested URL in order to send the Cookie header. The %x2F
     ("/") character is considered a directory separator, and subdirectories
     match as well.
    :type path: str
    :param value: Required. The value of the Cookie.
    :type value: str
    :param host_only: Required. Host Only cookie means that the cookie should
     be handled by the browser to the server only to the same host/server that
     firstly sent it to the browser.
    :type host_only: bool
    :param http_only: Required. When this attribute is set, client-side
     scripts are not allowed to access the cookie.
    :type http_only: bool
    :param secure: Required. A cookie with the Secure attribute is sent to the
     server only with an encrypted request over the HTTPS protocol, never with
     unsecured HTTP, and therefore can't easily be accessed by a
     man-in-the-middle attacker. Insecure sites (with http: in the URL) can't
     set cookies with the Secure attribute.
    :type secure: bool
    :param same_site: Required. The sameSite attribute lets servers require
     that a cookie shouldn't be sent with cross-origin requests (where Site is
     defined by the registrable domain), which provides some protection against
     cross-site request forgery attacks (CSRF).
     It takes three possible values: Strict, Lax, and None.With Strict, the
     cookie is sent only to the same site as the one that originated it; Lax is
     similar, with an exception for when the user navigates to a URL from an
     external site, such as by following a link; None has no restrictions on
     cross-site requests.
    :type same_site: str
    :param expiration_date: This unix timestamp formatted attribute is used to
     set persistent cookies. It signifies how long the browser should use the
     persistent cookie and when the cookie should be deleted.
     If this attribute is not specified, then the lifetime of the cookie is the
     same as that of browser session, i.e.it will be a non-persistent cookie.
    :type expiration_date: long
    :param session: Session cookies are deleted when the current session ends.
     The browser defines when the "current session" ends, and some browsers use
     session restoring when restarting, which can cause session cookies to last
     indefinitely long.
    :type session: bool
    :param store_id: The ID of the cookie store containing this cookie.
    :type store_id: str
    """

    _validation = {
        'domain': {'required': True},
        'name': {'required': True},
        'path': {'required': True},
        'value': {'required': True},
        'host_only': {'required': True},
        'http_only': {'required': True},
        'secure': {'required': True},
        'same_site': {'required': True},
    }

    _attribute_map = {
        'domain': {'key': 'domain', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'host_only': {'key': 'hostOnly', 'type': 'bool'},
        'http_only': {'key': 'httpOnly', 'type': 'bool'},
        'secure': {'key': 'secure', 'type': 'bool'},
        'same_site': {'key': 'sameSite', 'type': 'str'},
        'expiration_date': {'key': 'expirationDate', 'type': 'long'},
        'session': {'key': 'session', 'type': 'bool'},
        'store_id': {'key': 'storeId', 'type': 'str'},
    }

    def __init__(self, *, domain: str, name: str, path: str, value: str, host_only: bool, http_only: bool, secure: bool, same_site: str, expiration_date: int=None, session: bool=None, store_id: str=None, **kwargs) -> None:
        super(BrowserCookie, self).__init__(**kwargs)
        self.domain = domain
        self.name = name
        self.path = path
        self.value = value
        self.host_only = host_only
        self.http_only = http_only
        self.secure = secure
        self.same_site = same_site
        self.expiration_date = expiration_date
        self.session = session
        self.store_id = store_id
