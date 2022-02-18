<img src="https://raw.githubusercontent.com/kameleo-io/local-api-client-python/HEAD/docs/kameleo-logo.png" width="150" align="right" />

# Kameleo Local API Client
With [Kameleo](https://kameleo.io), you can easily crate multiple virtual browser profiles to work with multiple accounts. It helps you hide your actual timezone, geolocation, language, IP address and creates natural browser fingerprints to prevent detection by anti-bot systems. Kameleo is compatible with [Selenium](https://www.selenium.dev/), [Playwright](https://playwright.dev/), and [Puppeteer](https://pptr.dev/) frameworks for automating web scraping tasks. This Python package provides convenient access to the [Local API](https://app.swaggerhub.com/apis/kameleo-team/kameleo-local-api/) REST interface of the Kameleo Client. See the [article](https://help.kameleo.io/hc/en-us/articles/4418166326417) in our knowledge base for Getting Started with Kameleo Automation.


# Features
- Stay completely undetected, so websites won’t be able to detect that you are using automation tools
- Start unlimited number of profiles with different natural browser fingerprints
- Use authenticated HTTP/SOCKS/SSH proxies in browsers
- Create isolated browsing environments simultaneously
- Use real browser profiles of Chrome, Firefox, Safari and Edge
- Edit, Import or Export browser cookies
- Modify WebRTC parameters
- Modify Geolocation settings
- Modify Timezone and Language settings
- Modify WebGL fingerprint
- Modify 2D Canvas fingerprint
- Modify Navigator properties
- Modify Screen resolution

> Note: _You need [Automation package](https://kameleo.io/pricing) of Kameleo to access the features described below._


# Quickstart Guide

## 1. Install package
```
pip install kameleo.local_api_client
```

## 2. Start the Kameleo.CLI on your computer
```
./Kameleo.CLI.exe email="your@email.com" password="Pa$$w0rd"
```

## 3. Start a browser with out-of-the-box fingerprinting protection 
```python
from kameleo.local_api_client.kameleo_local_api_client import KameleoLocalApiClient
from kameleo.local_api_client.builder_for_create_profile import BuilderForCreateProfile
from kameleo.local_api_client.models.problem_response_py3 import ProblemResponseException
import json

try:
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
    
    # At this point you can automate the browser with your favorite framework
except ProblemResponseException as e:
    raise Exception([str(e), json.dumps(e.error.error)])
```

# Automate Kameleo profiles with Selenium
Kameleo gives you the ability to control any supported browser using Selenium. It uses the WebDriver protocol, a W3C specification, and industry-standard to interact with a browser.

You need to install the official [Selenium package](https://pypi.org/project/selenium/).

```python
from selenium import webdriver
```

```python
# Connect to the running browser instance using WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("kameleo:profileId", profile.id)
driver = webdriver.Remote(
    command_executor=f'http://localhost:{kameleo_port}/webdriver',
    options=options
)

# Use any WebDriver command to drive the browser
# and enjoy full protection from bot detection products
driver.get('https://google.com')
```

The full example can be found [here](https://github.com/kameleo-io/local-api-examples/blob/master/python/connect_to_selenium/app.py).

# Automate Kameleo profiles with Puppeteer (Chromium-based)
Kameleo lets you control Chromium-based browsers (sorry Firefox fans) using the [Pyppeteer library](https://pypi.org/project/pyppeteer/). In this simple example you can see how to connect to the browser that Kameleo starts.

You need to import the [Pyppeteer library](https://pypi.org/project/pyppeteer/).

```python
import pyppeteer   
```

```python
# Connect to the browser with Puppeteer through CDP
browser_ws_endpoint = f'ws://localhost:{kameleo_port}/puppeteer/{profile.id}'
browser = await pyppeteer.launcher.connect(browserWSEndpoint=browser_ws_endpoint, defaultViewport=False)
page = await browser.newPage()

# Use any Playwright command to drive the browser
# and enjoy full protection from bot detection products
await page.goto('https://google.com')
```

The full example can be found [here](https://github.com/kameleo-io/local-api-examples/blob/master/python/connect_with_puppeteer_to_chrome/app.py).

# Automate Kameleo profiles with Playwright
Kameleo allows you to control the browser with the official [Playwright package](https://pypi.org/project/playwright/). It works little bit different with Chromium-based browsers and Firefox, so we provide an example for both. Here we showcase how you can connect to the browser that is already started by Kameleo.

You need to import the official [Playwright package](https://pypi.org/project/playwright/).
```python
import playwright
from playwright.sync_api import sync_playwright
```

## Chromium-based profiles with Playwright

```python
# Connect to the browser with Playwright through CDP
browser_ws_endpoint = f'ws://localhost:{kameleo_port}/playwright/{profile.id}'
with sync_playwright() as playwright:
    browser = playwright.chromium.connect_over_cdp(endpoint_url=browser_ws_endpoint)
    context = browser.contexts[0]
    page = context.new_page()

    # Use any Playwright command to drive the browser
    # and enjoy full protection from bot detection products
    page.goto('https://google.com')
```

The full example can be found [here](https://github.com/kameleo-io/local-api-examples/blob/master/python/connect_with_playwright_to_chrome/app.py).

## Firefox-based profiles with Playwright

```python
# Connect to the browser with Playwright
browser_ws_endpoint = f'ws://localhost:{kameleo_port}/playwright/{profile.id}'
with sync_playwright() as playwright:
    browser = playwright.firefox.launch(
        # The Playwright framework is not designed to connect to already running 
        # browsers. To overcome this limitation, a tool bundled with Kameleo, named 
        # pw-bridge.exe will bridge the communication gap between the running Firefox 
        # instance and this playwright script.
        executable_path='<PATH_TO_KAMELEO_FOLDER>>\\pw-bridge.exe',
        args=[f'-target {browser_ws_endpoint}'])
    
    # Kameleo will open the a new page in the default browser context.
    # NOTE: We DO NOT recommend using multiple browser contexts, as this might interfere 
    #       with Kameleo's browser fingerprint modification features.
    page = browser.new_page()

    # Use any Playwright command to drive the browser
    # and enjoy full protection from bot detection products
    page.goto('https://google.com')

    # Here we need to close the browser object as well, it is not enough just to stop the profile
    client.stop_profile(profile.id)
    browser.close()
```

The full example can be found [here](https://github.com/kameleo-io/local-api-examples/blob/master/python/connect_with_playwright_to_firefox/app.py).

# Example codes
[Several examples](https://github.com/kameleo-io/local-api-examples) have been prepared in a different repository to showcase the most interesting features. Feel free to create a pull request to add new example codes.

- Finding base profiles
- Creating profiles with custom options
- Updating profiles with new settings
- How to start a profile
- Using Selenium with Local API
- Using Playwright with Kameleo
- Using Puppeteer with Kameleo
- Adding an HTTP, SOCKS or SSH proxy to profile
- Saving/Loading a browsing session to/from a .kameleo file
- Modify and Delete browser cookies
- Start profile with extra WebDriver capabilities

> Note: _If you are interested in more information about Kameleo, or have encountered an issue with using it, please check out our [Help Center](https://help.kameleo.io/)._


# Endpoints
Available API endpoints with exhaustive descriptions and example values are documented on this [SwaggerHub](https://app.swaggerhub.com/apis/kameleo-team/kameleo-local-api/) page. This package has built-in [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) support in Visual Studio Code, no extra package installation needed.


# License
This project is released under MIT License. Please refer the LICENSE.txt for more details.
