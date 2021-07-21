<img src="https://raw.githubusercontent.com/kameleo-io/local-api-client-python/HEAD/docs/kameleo-logo.png" width="150" align="right" />

# Kameleo Local API Client
[Kameleo](https://kameleo.io) is a complete and integrated solution for browser fingerprinting protection, and also for easy browser automation using W3C WebDriver. This Python package provides convenient access to the [Local API](https://app.swaggerhub.com/apis/kameleo-team/kameleo-local-api/2.3) REST interface of the Kameleo Client.


# Features
- Protection from Selenium/WebDriver detection
- Start unlimited number of profiles with different browser fingerprints
- Use authenticated HTTP/SOCKS/SSH proxies in browsers
- Create isolated browsing environments simultaneously
- Use real browser profiles of Chrome, Firefox, Safari and Edge
- Edit, Import or Export browser cookies
- Modify WebRTC parameters
- Modify Geolocation settings
- Modify WebGL fingerprint
- Modify 2D Canvas fingerprint
- Modify Navigator properties
- Modify Screen resolution


# Quickstart Guide

## 1. Install package
```
pip install kameleo.local_api_client
```

## 2. Start the Kameleo.CLI on your computer
```
./Kameleo.CLI.exe email="your@email.com" password="Pa$$w0rd"
```
> Note: _You need [Automation package](https://kameleo.io/pricing) of Kameleo to access the features described below._

## 3. Start a browser with out-of-the-box fingerprinting protection 
```python
from kameleo.local_api_client.kameleo_local_api_client import KameleoLocalApiClient
from kameleo.local_api_client.builder_for_create_profile import BuilderForCreateProfile

client = KameleoLocalApiClient()
base_profiles = client.search_base_profiles(
    device_type='desktop',
    browser_product='chrome'
)

# Create a new profile with recommended settings
# for browser fingerprinting protection
create_profile_request = BuilderForCreateProfile \
    .for_base_profile(base_profiles[0].id) \
    .set_recommended_defaults() \
    .build()
profile = client.create_profile(body=create_profile_request)

# Start the browser
client.start_profile(profile.id)
```

# Automate browsers with W3C WebDriver
Kameleo uses a WebDriver compatible server to control the browser. WebDriver is a W3C specification and industry standard which provides a platform and HTTP protocol to interact with a browser.

```python
from kameleo.local_api_client.kameleo_local_api_client import KameleoLocalApiClient
from kameleo.local_api_client.builder_for_create_profile import BuilderForCreateProfile
from selenium import webdriver

kameleoBaseUrl = 'http://localhost:5050'
client = KameleoLocalApiClient(kameleoBaseUrl)

# Search Chrome Base Profiles
base_profiles = client.search_base_profiles(
    device_type='desktop',
    browser_product='chrome'
)

# Create a new profile with recommended settings
# for browser fingerprinting protection
create_profile_request = BuilderForCreateProfile \
    .for_base_profile(base_profiles[0].id) \
    .set_recommended_defaults() \
    .build()
profile = client.create_profile(body=create_profile_request)

# Start the browser
client.start_profile(profile.id)

# Connect to the running browser instance using WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("kameleo:profileId", profile.id)
driver = webdriver.Remote(
    command_executor=f'{kameleoBaseUrl}/webdriver',
    options=options
)

# Use any WebDriver command to drive the browser
# and enjoy full protection from Selenium detection methods
driver.get('https://google.com')
driver.find_element('css selector', 'div[aria-modal="true"][tabindex="0"] button:not([aria-label]):last-child').click()
driver.find_element('name', 'q').send_keys('Kameleo\n')
print(driver.title)

# Stop the browser by stopping the Kameleo profile
client.stop_profile(profile.id)
```

# Example codes
Several [examples](https://github.com/kameleo-io/local-api-examples) have been prepared in a different repository to showcase the most interesting features. Feel free to create a pull request to add new example codes.

- Finding base profiles
- Creating profiles with custom options
- Updating profiles with new settings
- How to start a profile
- Using WebDriver with Local API
- Adding an HTTP, SOCKS or SSH proxy to profile
- Saving/Loading a browsing session to/from a .kameleo file
- Modify and Delete browser cookies
- Hooking up Kameleo with an external browser (Puppeteer)
- Start profile with extra WebDriver capabilities


# Endpoints
Available API endpoints with exhaustive descriptions and example values are documented on this [SwaggerHub](https://app.swaggerhub.com/apis/kameleo-team/kameleo-local-api/2.0) page. This package has built-in [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) support in Visual Studio Code, no extra package installation needed.


# License
This project is released under MIT License. Please refer the LICENSE.txt for more details.
