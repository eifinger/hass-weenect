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
`binary_sensor` | Adds sensors to show the connection status of your trackers.
`button` | Shortcuts to service. Activate Super Live Mode, Ring, Vibrate and Request a Location Update.
`device_tracker` | Adds your trackers as device_trackers so they appear on the map.
`select` | Select the update interval.
`sensor` | Adds sensors like signal and battery strength of your trackers.

![example][exampleimg]
![configuration][configurationimg]

## Services

### weenect.set_update_interval

Set the tracker update interval. Disable tracking by setting interval to 0S.

Name | Description | Example
-- | -- | --
`update_interval` | `The update interval. Possible values are 0S, 30S, 1M, 2M, 3M, 5M, 10M, 30M, 60M. Please note, that 30M and 60M are not officially supported in the Weenect app.` | `10M`

### weenect.activate_super_live

Activate the super live mode.

### weenect.refresh_location

Request a location update.

### weenect.ring

Let the tracker ring.

### weenect.vibrate

Let the tracker vibrate.

## Installation

### HACS

The easiest way to add this to your Homeassistant installation is using [HACS](https://hacs.xyz/).

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
custom_components/weenect/button.py
custom_components/weenect/binary_sensor.py
custom_components/weenect/config_flow.py
custom_components/weenect/const.py
custom_components/weenect/device_tracker.py
custom_components/weenect/entity.py
custom_components/weenect/manifest.json
custom_components/weenect/select.py
custom_components/weenect/sensor.py
custom_components/weenect/services.py
custom_components/weenect/services.yaml
custom_components/weenect/translations/en.json
```

## Automations

I have configured the following two automations to save battery on the tracker without having it to turn on/off by hand:

```yaml
---
automation:
  - id: 743b7e7d-ffa8-4fa3-9c1c-62d9ada9ced8
    alias: "Setze Nayas Tracker Updaterate auf 1M wenn wir unterwegs sind"
    description: "Set Nayas tracker update rate to 1m when we are not at home"
    mode: single
    initial_state: true
    trigger:
      - platform: state
        entity_id: input_boolean.is_home
        from: "on"
        to: "off"
    action:
      - service: weenect.set_update_interval
        target:
            entity_id: device_tracker.naya
        data:
          update_interval: "1M"
  - id: 652b4b69-c951-4861-8b7d-3cbb15fc8b79
    alias: "Setze Nayas Tracker Updaterate auf 60M wenn wir zu Hause sind"
    description: "Set Nayas tracker update rate to 60m when we are at home"
    mode: single
    initial_state: true
    trigger:
      - platform: state
        entity_id: input_boolean.is_home
        from: "off"
        to: "on"
    action:
      - service: weenect.set_update_interval
        target:
          entity_id: device_tracker.naya
        data:
          update_interval: "60M"
````


<a href="https://www.buymeacoffee.com/eifinger" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/black_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a><br>

[buymecoffee]: https://www.buymeacoffee.com/eifinger
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/eifinger/hass-weenect?style=for-the-badge
[commits]: https://github.com/eifinger/hass-weenect/commits/main
[exampleimg]: https://github.com/eifinger/hass-weenect/blob/main/example.png?raw=true
[configurationimg]: https://github.com/eifinger/hass-weenect/blob/main/configuration.png?raw=true
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/t/custom-integration-weenect/300996
[license-shield]: https://img.shields.io/github/license/eifinger/hass-weenect.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Kevin%20Stillhammer%20%40eifinger-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/eifinger/hass-weenect.svg?style=for-the-badge
[releases]: https://github.com/eifinger/hass-weenect/releases
