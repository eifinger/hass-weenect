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
`device_tracker` | Adds your trackers as device_trackers so they appear on the map.
`sensor` | Adds sensors like signal and battery strength of your trackers.

![example][exampleimg]

## Services

### weeenct.set_update_interval

Set the tracker update interval.

Name | Description | Example
-- | -- | --
`tracker_id` | `The tracker id.` | `10000`
`update_interval` | `The update interval. Possible values are 30S 1M 5M 10M 30M 1H.` | `30M`

### weeenct.activate_super_live

Activate the super live mode.

Name | Description | Example
-- | -- | --
`tracker_id` | `The tracker id.` | `10000`

### weeenct.refresh_location

Request a location update.

Name | Description | Example
-- | -- | --
`tracker_id` | `The tracker id.` | `10000`

### weeenct.ring

Let the tracker ring.

Name | Description | Example
-- | -- | --
`tracker_id` | `The tracker id.` | `10000`

### weeenct.vibrate

Let the tracker vibrate.

Name | Description | Example
-- | -- | --
`tracker_id` | `The tracker id.` | `10000`

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
        data:
          tracker_id: !secret naya_tracker_id
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
        data:
          tracker_id: !secret naya_tracker_id
          update_interval: "60M"
````

<a href="https://www.buymeacoffee.com/eifinger" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/black_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a><br>

[buymecoffee]: https://www.buymeacoffee.com/eifinger
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/eifinger/hass-weenect?style=for-the-badge
[commits]: https://github.com/eifinger/hass-weenect/commits/master
[exampleimg]: https://github.com/eifinger/hass-weenect/blob/master/example.png?raw=true
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/t/custom-integration-weenect/300996
[license-shield]: https://img.shields.io/github/license/eifinger/hass-weenect.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Kevin%20Stillhammer%20%40eifinger-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/eifinger/hass-weenect.svg?style=for-the-badge
[releases]: https://github.com/eifinger/hass-weenect/releases
