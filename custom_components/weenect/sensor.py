"""Sensor platform for weenect."""
from __future__ import annotations

from datetime import datetime
from typing import List

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PERCENTAGE, SIGNAL_STRENGTH_DECIBELS
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.util import dt

from .const import DOMAIN, TRACKER_ADDED
from .entity import WeenectEntity

SENSOR_ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        name="Last Update Rate",
        key="last_freq_mode",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Sensor Mode",
        key="sensor_mode",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Last Sensor Mode",
        key="last_sensor_mode",
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


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the weenect sensors."""

    coordinator = hass.data[DOMAIN][entry.entry_id]

    @callback
    def async_add_sensors(
        added: List[int],
    ) -> None:
        """Add sensors callback."""

        sensors: list = []
        for tracker_id in added:
            for sensor_description in SENSOR_ENTITY_DESCRIPTIONS:
                sensors.append(
                    WeenectSensor(coordinator, tracker_id, sensor_description)
                )
            for location_sensor_description in LOCATION_SENSOR_ENTITY_DESCRIPTIONS:
                sensors.append(
                    WeenectLocationSensor(
                        coordinator, tracker_id, location_sensor_description
                    )
                )

        async_add_entities(sensors, True)

    unsub_dispatcher = async_dispatcher_connect(
        hass,
        f"{entry.entry_id}_{TRACKER_ADDED}",
        async_add_sensors,
    )
    coordinator.unsub_dispatchers.append(unsub_dispatcher)
    if len(coordinator.data) > 0:
        async_add_sensors(coordinator.data.keys())


class WeenectSensor(WeenectEntity, SensorEntity):
    """weenect sensor for general information."""

    @property
    def native_value(self) -> StateType | datetime:
        """Return the state of the resources if it has been received yet."""
        if self.id in self.coordinator.data:
            return self.coordinator.data[self.id][self.entity_description.key]
        return None


class WeenectLocationSensor(WeenectSensor):
    """weenect sensor for location information."""

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return super().available and bool(self.coordinator.data[self.id]["position"])

    @property
    def native_value(self) -> StateType:
        """Return the state of the resources if it has been received yet."""
        if self.id in self.coordinator.data:
            if self.coordinator.data[self.id]["position"]:
                value = self.coordinator.data[self.id]["position"][0][
                    self.entity_description.key
                ]
                if self.device_class == str(SensorDeviceClass.TIMESTAMP):
                    return dt.parse_datetime(value)
                return value
        return None
