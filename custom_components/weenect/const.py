"""Constants for weenect."""
from __future__ import annotations

from homeassistant.const import Platform

# Base component constants
NAME = "Weenect"
DOMAIN = "weenect"
VERSION = "3.1.0"
ATTRIBUTION = "Data provided by https://my.weenect.com/"
ISSUE_URL = "https://github.com/eifinger/hass-weenect/issues"

PLATFORMS = [
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    Platform.DEVICE_TRACKER,
    Platform.SELECT,
    Platform.SENSOR,
]

UPDATE_INTERVAL = "update_interval"

SERVICE_ACTIVATE_SUPER_LIVE = "activate_super_live"
SERVICE_REFRESH_LOCATION = "refresh_location"
SERVICE_RING = "ring"
SERVICE_VIBRATE = "vibrate"
SERVICE_SET_UPDATE_INTERVAL = "set_update_interval"

# Configuration and options
CONF_USERNAME = "username"
CONF_PASSWORD = "password"  # nosec
CONF_UPDATE_RATE = "update_rate"

# Dispatcher identifiers
TRACKER_ADDED = "tracker_added"


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
