"""Constants for weenect."""
from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntityDescription,
)
from homeassistant.components.button import ButtonEntityDescription
from homeassistant.components.select import SelectEntityDescription
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import PERCENTAGE, SIGNAL_STRENGTH_DECIBELS, Platform
from homeassistant.helpers.entity import EntityCategory

# Base component constants
NAME = "Weenect"
DOMAIN = "weenect"
VERSION = "2.0.9"
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

BUTTON_ENTITY_DESCRIPTIONS: tuple[ButtonEntityDescription, ...] = (
    ButtonEntityDescription(
        key=SERVICE_ACTIVATE_SUPER_LIVE,
        name="Activate Super Live",
        icon="mdi:lightning-bolt",
        entity_category=EntityCategory.CONFIG,
    ),
    ButtonEntityDescription(
        key=SERVICE_REFRESH_LOCATION,
        name="Refresh Location",
        icon="mdi:refresh",
        entity_category=EntityCategory.CONFIG,
    ),
    ButtonEntityDescription(
        key=SERVICE_RING,
        name="Ring",
        icon="mdi:music-note",
        entity_category=EntityCategory.CONFIG,
    ),
    ButtonEntityDescription(
        key=SERVICE_VIBRATE,
        name="Vibrate",
        icon="mdi:vibrate",
        entity_category=EntityCategory.CONFIG,
    ),
)

SENSOR_ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        name="Last Update Rate",
        key="last_freq_mode",
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Sensor Mode",
        key="sensor_mode",
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Last Sensor Mode",
        key="last_sensor_mode",
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
)

LOCATION_SENSOR_ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        name="Battery",
        key="battery",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.BATTERY,
        native_unit_of_measurement=PERCENTAGE,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Cell Tower Id",
        key="cellid",
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="GSM Strength",
        key="gsm",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.SIGNAL_STRENGTH,
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Last Message Received",
        key="last_message",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TIMESTAMP,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="GPS Satellites",
        key="satellites",
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
)

BINARY_SENSOR_ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    BinarySensorEntityDescription(
        name="Valid Signal",
        key="valid_signal",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    BinarySensorEntityDescription(
        name="Is Online",
        key="is_online",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
)

SELECT_ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    SelectEntityDescription(
        name="Update Rate",
        key="freq_mode",
        entity_category=EntityCategory.CONFIG,
    ),
)

SELECT_OPTIONS = ("30S", "1M", "5M", "10M", "30M", "60M")
DEFAULT_SELECT_OPTION = "30M"

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
