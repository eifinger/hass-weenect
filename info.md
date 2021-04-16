# weenect

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
[![License][license-shield]](LICENSE.md)

![Project Maintenance][maintenance-shield]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Community Forum][forum-shield]][forum]

_Homeassistant Custom Component for [https://my.weenect.com/](https://my.weenect.com/)._

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show travel time between two places.

![example][exampleimg]

## Installation

### HACS

The easiest way to add this to your Homeassistant installation is using [HACS](https://custom-components.github.io/hacs/). And then follow the instructions under [Configuration](#configuration) below.

### Manual

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `weenect`.
4. Download _all_ the files from the `custom_components/weenect/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Blueprint"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/weenect/__init__.py
custom_components/weenect/binary_sensor.py
custom_components/weenect/config_flow.py
custom_components/weenect/const.py
custom_components/weenect/device_tracker.py
custom_components/weenect/entity.py
custom_components/weenect/manifest.json
custom_components/weenect/sensor.py
custom_components/weenect/services.py
custom_components/weenect/services.yaml
custom_components/weenect/translations/en.sjon
```


<a href="https://www.buymeacoffee.com/eifinger" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/black_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a><br>

[buymecoffee]: https://www.buymeacoffee.com/eifinger
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/eifinger/hass-weenect?style=for-the-badge
[commits]: https://github.com/eifinger/hass-weenect/commits/master
[exampleimg]: https://github.com/eifinger/hass-weenect/blob/master/example.png?raw=true
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/t/
[license-shield]: https://img.shields.io/github/license/eifinger/hass-weenect.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Kevin%20Eifinger%20%40eifinger-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/eifinger/hass-weenect.svg?style=for-the-badge
[releases]: https://github.com/eifinger/hass-weenect/releases
