from .models.create_profile_request_py3 import CreateProfileRequest
from .models.webgl_spoofing_type_webgl_spoofing_options_multi_level_choice_py3 import WebglSpoofingTypeWebglSpoofingOptionsMultiLevelChoice
from .models.timezone_spoofing_type_timezone_multi_level_choice_py3 import TimezoneSpoofingTypeTimezoneMultiLevelChoice
from .models.geolocation_spoofing_type_geolocation_spoofing_options_multi_level_choice_py3 import GeolocationSpoofingTypeGeolocationSpoofingOptionsMultiLevelChoice
from .models.proxy_connection_type_server_multi_level_choice_py3 import ProxyConnectionTypeServerMultiLevelChoice
from .models.web_rtc_spoofing_type_web_rtc_spoofing_options_multi_level_choice_py3 import WebRtcSpoofingTypeWebRtcSpoofingOptionsMultiLevelChoice
from .models.font_spoofing_type_font_ilist_multi_level_choice_py3 import FontSpoofingTypeFontIListMultiLevelChoice
from .models.plugin_spoofing_type_plugin_ilist_multi_level_choice_py3 import PluginSpoofingTypePluginIListMultiLevelChoice
from .models.screen_spoofing_type_screen_size_multi_level_choice_py3 import ScreenSpoofingTypeScreenSizeMultiLevelChoice


class BuilderForCreateProfile:
    def __init__(self, base_profile_id):
        self.profile_request = self.reset(base_profile_id)

    @staticmethod
    def for_base_profile(base_profile_id):
        if not base_profile_id:
            raise ValueError("base_profile_id must be set")
        return BuilderForCreateProfile(base_profile_id)

    def build(self):
        result = self.profile_request
        self.profile_request = self.reset(result.base_profile_id)
        return result

    def set_canvas(self, value):
        """Tells the mode how the canvas will be spoofed. Possible values:
            'noise': Add some noise to the Canvas generation.
            'block': Completely block the 2D API.
            'off': Turn off the spoofing, use the original settings.
        :param string value: Canvas spoofing type. Possible values: 'noise', 'block', 'off'
        """
        self.profile_request.canvas = value
        return self
    
    def set_webgl(self, value, options):
        """Set the Webgl spoofing. Possible values:
            'noise': Add some noise to the WebGL generation
            'block': Completely block the 3D API
            'off': Turn off the spoofing, use the original settings
        :param string value: WebGL spoofing type. Possible values: 'noise', 'block', 'off'
        :param options: Provide unmasked_vendor and unmasked_renderer
        :type options: ~kameleo.local_api_client.models.WebglSpoofingOptions
        """
        self.profile_request.webgl.value = value
        self.profile_request.webgl.extra = options
        return self

    def set_audio(self, value):
        """Tells the mode how the audio will be spoofed. Possible values:
            'noise': Add some noise to the Audio generation.
            'block': Completely block the Audio API.
            'off': Turn off the audio spoofing, use the original settings.
        :param string value: Audio spoofing type. Possible values: 'noise', 'block', 'off'
        """
        self.profile_request.audio = value
        return self

    def set_timezone(self, value, options):
        """Tells the mode how the Timezone will be spoofed. Possble values:
            'automatic': Timezone is automatically set by the IP
            'manual': Timezone is manually overridden in the profile
            'off': Turn off the spoofing, use the original settings
        :param string value: Timezone spoofing type. Possible values: 'automatic', 'manual', 'off'
        :param str options: When the Timezone spoofing is set to manual the timezone in Iana format is required. For example: America/Grenada
        """
        self.profile_request.timezone.value = value
        self.profile_request.timezone.extra = options
        return self

    def set_geolocation(self, value, options):
        """Tells the mode how the Geolocation will be spoofed. Possible values:
            'automatic': Automatically set the values based on the IP address
            'manual': Manually set the longitude and latitude in the profile
            'block': Completely block the GeolocationAPI
            'off': Turn off the spoofing, use the original settings
        :param string value: Geolocation spoofing type. Possible values: 'automatic', 'manual', 'block', 'off'
        :param options: When the Geolocation spoofing is set to manual the Geolocation coordinates must be provided
        :type options: ~kameleo.local_api_client.models.GeolocationSpoofingOptions
        """
        self.profile_request.geolocation.value = value
        self.profile_request.geolocation.extra = options
        return self

    def set_proxy(self, value, options):
        """Proxy connection settings of the profiles. Possible values:
            'none': Direct connection without any proxy.</para>
            'http': Use a HTTP(S) proxy for upstream communication.</para>
            'socks5': Use a SOCKS5 proxy for upstream communication.</para>
            'ssh': Use an SSH connection for upstream communication. Basically a SOCKS5 proxy created at the given SSH host.</para>
        :param string value: Proxy connection type. Possible values: 'none', 'http', 'socks5', 'ssh'
        :param options: When the Proxy connection is set, a Proxy Server must be provided
        :type options: ~kameleo.local_api_client.models.Server
        """
        self.profile_request.proxy.value = value
        self.profile_request.proxy.extra = options
        return self

    def set_web_rtc(self, value, options):
        """Tells the mode how the WebRTC will be spoofed. Possible values:
            'automatic': Automatically set the webRTC public IP by the IP, and generates a random private IP like '2d2f78e7-1b1e-4345-a21b-07c904c98394.local'
            'manual': Manually override the webRTC public IP and private IP in the profile
            'block': Block the WebRTC functionality
            'off': Turn off the spoofing, use the original settings
        :param string value: WebRTC spoofing type. Possible values: 'automatic', 'manual', 'block', 'off'
        :param options: When the WebRTC spoofing is set to manual, the private_ip and public_ip must be provided
        :type options: ~kameleo.local_api_client.models.WebRtcSpoofingOptions
        """
        self.profile_request.web_rtc.value = value
        self.profile_request.web_rtc.extra = options
        return self

    def set_fonts(self, value, options):
        """Tells the mode how the Fonts will be spoofed. Possible values:
            'enabled': Enable fonts spoofing. A list can be provided to override the fonts coming from the base profile.
            'disable': Disable fonts spoofing.
        :param string value: Fonts spoofing type. Possible values: 'enabled', 'disabled'
        :param options: When the Font spoofing is set to enabled, a list can be provided to overrider the fonts coming from the base profile.
        :type options: list[str]
        """
        self.profile_request.fonts.value = value
        self.profile_request.fonts.extra = options
        return self

    def set_plugins(self, value, options):
        """Tells the mode how the Plugins will be spoofed. Possible values:
            'enabled': Enable plugins spoofing. A list can be provided to EXCLUDE plugins from the plugins of the base profile.
            'disable': Disable plugins spoofing.
        :param string value: Plugins spoofing type. Possible values: 'enabled', 'disabled'
        :param options: When the Plugins spoofing is set to enabled, a list can be provided to EXCLUDE plugins from the plugins of the base profile.
        :type options: list[str]
        """
        self.profile_request.plugins.value = value
        self.profile_request.plugins.extra = options
        return self

    def set_start_page(self, value):
        """This website will be opened in the browser when the profile launches.
        :param string value: The url of the start page
        """
        self.profile_request.start_page = value
        return self

    def set_password_manager(self, value):
        """Enable or disable the password manager function in the browser. Possible values:
            'enabled': Enable password manager so browser will ask to save and load passwords on logins.
            'disable': Disable password manager.
        :param string value: Password Manager possible values: 'enabled', 'disabled'
        """
        self.profile_request.password_manager = value
        return self

    def set_screen(self, value, options):
        """Tells the mode how the screen will be spoofed. Possible values:
            'automatic': Automatically override the screen resolution based on the Base Profile.
            'manual': Manually override the screen resolution.
            'off': Turn off the spoofing, use the original settings.
        :param string value: Screen spoofing type. Possible values: 'automatic', 'manual', 'off'
        :param string options: When the Screen spoofing is set to manual, the required screen size must be provided. For example: 1080x1920
        """
        self.profile_request.screen.value = value
        self.profile_request.screen.extra = options
        return self

    def set_extensions(self, absolute_paths):
        """A list of absolute paths from where the profile should load extensions or addons when starting the browser. For chrome and edge use CRX3 format extensions. For firefox use signed xpi format addons.
        :param absolute_paths: A list of abolute paths from where the profile should load extensions or addons when starting the browser.
        :type absolute_paths: list[str]
        """
        self.profile_request.extensions = absolute_paths
        return self
    
    def set_notes(self, notes):
        """A free text including any notes written by the user.
        """
        self.profile_request.notes = notes
        return self

    def set_launcher(self, browser_launcher):
        """The mode how the profile should be launched. It determines which browser to launch. This cannot be modified after creation. Possible values are:
            'automatic': Automatically choose launcher based on DeviceType and BrowserProduct property.
            'chrome': Forcefully start the profile in Chrome.
            'chromium': Forcefully start the profile in Chromium.
            'firefox': Forcefully start the profile in Firefox.
            'edge': Forcefully start the profile in Edge.
            'external': Only start the external spoofing engine and connect any browser manually. This is also used for Mobile Device spoofing.
        :param string browser_launcher: Browser Launcher. Possible values: 'automatic', 'chrome', 'chromium', 'firefox', 'edge', 'external'
        """
        self.profile_request.launcher = browser_launcher
        return self

    def set_recommended_defaults(self):
        """This sets all the profile options to the defaults recommended by Kameleo Team. Please consider providing Proxy settings to your profile.
        """
        self.profile_request.canvas = "noise"
        self.profile_request.webgl.value = "noise"
        self.profile_request.audio = "noise"
        self.profile_request.timezone.value = "automatic"
        self.profile_request.geolocation.value = "automatic"
        self.profile_request.web_rtc.value = "automatic"
        self.profile_request.fonts.value = "enabled"
        self.profile_request.plugins.value = "enabled"
        self.profile_request.screen.value = "automatic"
        self.profile_request.launcher = "automatic"

        return self;
    
    def reset(self, base_profile_id):
        return CreateProfileRequest(
            base_profile_id=base_profile_id,
            canvas="off",
            webgl=WebglSpoofingTypeWebglSpoofingOptionsMultiLevelChoice(value="off", extra=None),
            audio="off",
            timezone=TimezoneSpoofingTypeTimezoneMultiLevelChoice(value="off", extra=None),
            geolocation=GeolocationSpoofingTypeGeolocationSpoofingOptionsMultiLevelChoice(value="off", extra=None),
            proxy=ProxyConnectionTypeServerMultiLevelChoice(value="none", extra=None),
            web_rtc=WebRtcSpoofingTypeWebRtcSpoofingOptionsMultiLevelChoice(value="off", extra=None),
            fonts=FontSpoofingTypeFontIListMultiLevelChoice(value="disabled", extra=None),
            plugins=PluginSpoofingTypePluginIListMultiLevelChoice(value="disabled", extra=None),
            screen=ScreenSpoofingTypeScreenSizeMultiLevelChoice(value="off", extra=None),
            password_manager="disabled")
