"""Constants for weenect."""
from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntityDescription,
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import PERCENTAGE, SIGNAL_STRENGTH_DECIBELS

# Base component constants
NAME = "Weenect"
DOMAIN = "weenect"
VERSION = "2.0.8"
ATTRIBUTION = "Data provided by https://my.weenect.com/"
ISSUE_URL = "https://github.com/eifinger/hass-weenect/issues"

# Platforms
PLATFORMS = ["binary_sensor", "device_tracker", "sensor"]

# Sensors
SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        name="Update Rate",
        key="freq_mode",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        name="Last Update Rate",
        key="last_freq_mode",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        name="Sensor Mode",
        key="sensor_mode",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        name="Last Sensor Mode",
        key="last_sensor_mode",
        state_class=SensorStateClass.MEASUREMENT,
    ),
)
LOCATION_SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        name="Battery",
        key="battery",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.BATTERY,
        native_unit_of_measurement=PERCENTAGE,
    ),
    SensorEntityDescription(
        name="Cell Tower Id",
        key="cellid",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        name="GSM Strength",
        key="gsm",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.SIGNAL_STRENGTH,
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS,
    ),
    SensorEntityDescription(
        name="Last Message Received",
        key="last_message",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        name="GPS Satellites",
        key="satellites",
        state_class=SensorStateClass.MEASUREMENT,
    ),
)

BINARY_SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    BinarySensorEntityDescription(
        name="Valid Signal",
        key="valid_signal",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
    ),
    BinarySensorEntityDescription(
        name="Is Online",
        key="is_online",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
    ),
)

# Configuration and options
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"  # nosec
CONF_UPDATE_RATE = "update_rate"
DEFAULT_UPDATE_RATE = 30

# Defaults
DEFAULT_NAME = DOMAIN

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
