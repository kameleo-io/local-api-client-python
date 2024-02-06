# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.6, generator: @autorest/python@6.5.1)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AudioSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells the mode how the Audio will be spoofed. Possible values:
    'noise': Add some noise to the Audio generation
    'block': Completely block the Audio API
    'off': Turn off the spoofing, use the original settings.
    """

    OFF = "off"
    NOISE = "noise"
    BLOCK = "block"


class CanvasSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells the mode how the canvas will be spoofed. Possible values:
    'intelligent': Use some noise and in specific cases use the intelligent canvas spoofing. This
    will result non unique canvas fingerprints.
    'noise': Add some noise to the Canvas generation.
    'block': Completely block the 2D API.
    'off': Turn off the spoofing, use the original settings.
    """

    INTELLIGENT = "intelligent"
    NOISE = "noise"
    BLOCK = "block"
    OFF = "off"


class FontSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells the mode how the Fonts will be spoofed. Possible values:
    'enabled': Enable fonts spoofing. A list can be provided to override the fonts coming from the
    base profile.
    'disable': Disable fonts spoofing.
    """

    ENABLED = "enabled"
    DISABLED = "disabled"


class GeolocationSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells the mode how the Geolocation will be spoofed. Possible values:
    'automatic': Automatically set the values based on the IP address
    'manual': Manually set the longitude and latitude in the profile
    'block': Completely block the GeolocationAPI
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    BLOCK = "block"
    OFF = "off"


class HardwareConcurrencySpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells the mode how the HardwareConcurrency will be spoofed. Possible values:
    'automatic': Automatically set the values based on the Base Profile.
    'manual': Manually set the value in the profile. Valid values: 1, 2, 4, 8, 12, 16.
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    OFF = "off"


class PasswordManagerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells if the browser should support credential saving. Possible values are:
    'enabled': Credential saving is enabled.
    'disabled': Credential saving is disabled.
    """

    ENABLED = "enabled"
    DISABLED = "disabled"


class ProfileLifetimeState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the lifetime states of a profile, indicating which actions
    can be performed with the associated browser engine at each state. Possible values are:


    * Unknown: State of the profile is undefined.
    * Created: Profile is created; the associated browser engine is not started.
    * Starting: The associated browser engine is starting.
    * Running: The associated browser engine is currently running.
    * Terminating: The associated browser engine is in the process of terminating.
    * Terminated: The associated browser engine is not running but has been started at least once.
    """

    CREATED = "created"
    STARTING = "starting"
    RUNNING = "running"
    TERMINATING = "terminating"
    TERMINATED = "terminated"
    UNKNOWN = "unknown"


class ProfilePersistenceState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells if the profile is saved or not. Possible values:
    'unsaved': Profile is not saved
    'saved': Profile is saved and up-to-date.
    """

    UNSAVED = "unsaved"
    SAVED = "saved"


class ProxyConnectionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Proxy connection settings of the profiles. Possible values:
    'none': Direct connection without any proxy.
    'http': Use a HTTP proxy for upstream communication.
    'socks5': Use a SOCKS5 proxy for upstream communication.
    'ssh': Use an SSH connection for upstream communication. Basically a SOCKS5 proxy created at
    the given SSH host.
    """

    NONE = "none"
    HTTP = "http"
    SOCKS5 = "socks5"
    SSH = "ssh"


class ScreenSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells the mode how the screen will be spoofed. Possible values:
    'automatic': Automatically override the screen resolution based on the Base Profile.
    'manual': Manually override the screen resolution.
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    OFF = "off"


class TimezoneSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells the mode how the Timezone will be spoofed. Possble values:
    'automatic': Timezone is automatically set by the IP
    'manual': Timezone is manually overridden in the profile
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    OFF = "off"


class WebglMetaSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells the mode how the WebGL vendor and renderer will be spoofed. Possible values:
    'automatic': The vendor and renderer values comes from the base profile.
    'manual': Manually set the vendor and renderer values.
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    OFF = "off"


class WebglSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells the mode how the WebGL will be spoofed. Possible values:
    'noise': Add some noise to the WebGL generation
    'block': Completely block the 3D API
    'off': Turn off the spoofing, use the original settings.
    """

    NOISE = "noise"
    BLOCK = "block"
    OFF = "off"


class WebRtcSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells the mode how the WebRTC will be spoofed. Possible values:
    'automatic': Automatically set the webRTC public IP by the IP, and generates a random private
    IP like '2d2f78e7-1b1e-4345-a21b-07c904c98394.local'
    'manual': Manually override the webRTC public IP and private IP in the profile
    'block': Block the WebRTC functionality
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    BLOCK = "block"
    OFF = "off"
