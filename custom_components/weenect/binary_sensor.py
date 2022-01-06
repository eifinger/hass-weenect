"""Binary_sensor platform for weenect."""
import logging
from typing import List

from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.core import callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import BINARY_SENSOR_ENTITY_DESCRIPTIONS, DOMAIN, TRACKER_ADDED
from .entity import WeenectEntity

_LOGGER = logging.getLogger(__name__)


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
    coordinator.unsub_dispatchers.append(unsub_dispatcher)
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
        super().__init__(coordinator, tracker_id)
        self.entity_description = entity_description

    @property
    def name(self):
        """Return the name of this tracker."""
        if self.id in self.coordinator.data:
            return f"{self.coordinator.data[self.id]['name']} {self.entity_description.name}"

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.id}_{self.entity_description.key}"

    @property
    def is_on(self):
        """Return True if the binary sensor is on."""
        if self.id in self.coordinator.data:
            return self.coordinator.data[self.id]["position"][0][
                self.entity_description.key
            ]
