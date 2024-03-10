"""Binary_sensor platform for weenect."""

from __future__ import annotations

from typing import List

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.core import callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN, TRACKER_ADDED
from .entity import WeenectEntity

BINARY_SENSOR_ENTITY_DESCRIPTIONS: tuple[BinarySensorEntityDescription, ...] = (
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


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the weenect binary_sensors."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]

    @callback
    def async_add_binary_sensors(
        added: List[int],
    ) -> None:
        """Add binary_sensors callback."""

        sensors: list = []
        for tracker_id in added:
            for binary_sensor_description in BINARY_SENSOR_ENTITY_DESCRIPTIONS:
                sensors.append(
                    WeenectBinarySensor(
                        coordinator, tracker_id, binary_sensor_description
                    )
                )

        async_add_entities(sensors, True)

    unsub_dispatcher = async_dispatcher_connect(
        hass,
        f"{config_entry.entry_id}_{TRACKER_ADDED}",
        async_add_binary_sensors,
    )
    config_entry.async_on_unload(unsub_dispatcher)
    if len(coordinator.data) > 0:
        async_add_binary_sensors(coordinator.data.keys())


class WeenectBinarySensor(WeenectEntity, BinarySensorEntity):
    """weenect binary_sensor."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        tracker_id: int,
        entity_description: BinarySensorEntityDescription,
    ):
        super().__init__(coordinator, tracker_id, entity_description)

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        if self.entity_description.key in ["valid_signal"]:
            return (
                super().available
                and bool(self.coordinator.data[self.id]["position"])
                and bool(self.coordinator.data[self.id]["position"][0]["is_online"])
            )
        return super().available and bool(self.coordinator.data[self.id]["position"])

    @property
    def is_on(self) -> bool | None:
        """Return True if the binary sensor is on."""
        if self.id in self.coordinator.data:
            if self.coordinator.data[self.id]["position"]:
                return bool(
                    self.coordinator.data[self.id]["position"][0][
                        self.entity_description.key
                    ]
                )
        return None
