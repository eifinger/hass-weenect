"""Sensor platform for weenect."""
from __future__ import annotations

from datetime import datetime
from typing import List

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.util import dt

from .const import DOMAIN, LOCATION_SENSOR_TYPES, SENSOR_TYPES, TRACKER_ADDED
from .entity import WeenectEntity


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
            for sensor_type in SENSOR_TYPES:
                sensors.append(WeenectSensor(coordinator, tracker_id, sensor_type))
            for sensor_type in LOCATION_SENSOR_TYPES:
                sensors.append(
                    WeenectLocationSensor(coordinator, tracker_id, sensor_type)
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


class WeenectSensorBase(WeenectEntity, SensorEntity):
    """weenect Sensor Base."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        tracker_id: int,
        entity_description: SensorEntityDescription,
    ):
        super().__init__(coordinator, tracker_id)
        self.entity_description = entity_description
        self._attr_unique_id = f"{tracker_id}_{entity_description.name}"

    @property
    def name(self):
        """Return the name of this sensor."""
        if self.id in self.coordinator.data:
            return f"{self.coordinator.data[self.id]['name']} {self.entity_description.name}"
        return None


class WeenectSensor(WeenectSensorBase):
    """weenect sensor for general information."""

    @property
    def native_value(self) -> StateType | datetime:
        """Return the state of the resources if it has been received yet."""
        if self.id in self.coordinator.data:
            value = self.coordinator.data[self.id][self.entity_description.key]
            if self.device_class == SensorDeviceClass.TIMESTAMP:
                return dt.parse_datetime(value)
            return value
        return None


class WeenectLocationSensor(WeenectSensorBase):
    """weenect sensor for location information."""

    @property
    def native_value(self) -> StateType:
        """Return the state of the resources if it has been received yet."""
        if self.id in self.coordinator.data:
            return self.coordinator.data[self.id]["position"][0][
                self.entity_description.key
            ]
        return None
