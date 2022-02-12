"""weenect class"""
# pyright: reportGeneralTypeIssues=false
from __future__ import annotations

from homeassistant.helpers.entity import DeviceInfo, EntityDescription
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import ATTRIBUTION, DOMAIN, NAME


class WeenectBaseEntity(CoordinatorEntity):
    """Abstract base entity for weenect."""

    def __init__(self, coordinator: DataUpdateCoordinator, tracker_id: int):
        super().__init__(coordinator)
        self.id = tracker_id
        self._attr_attribution = ATTRIBUTION
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self.id)},
            name=str(self.coordinator.data[self.id]["name"]),
            model=str(self.coordinator.data[self.id]["type"]),
            manufacturer=NAME,
            sw_version=str(self.coordinator.data[self.id]["firmware"]),
        )
        self._attr_extra_state_attributes = {
            "id": self.id,
            "sim": str(self.coordinator.data[self.id]["sim"]),
            "imei": str(self.coordinator.data[self.id]["imei"]),
        }


class WeenectEntity(WeenectBaseEntity):
    """Entity for weenect."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        tracker_id: int,
        entity_description: EntityDescription,
    ) -> None:
        super().__init__(coordinator, tracker_id)
        self.entity_description = entity_description
        self._attr_name = (
            f"{self.coordinator.data[self.id]['name']} {self.entity_description.name}"
        )
        self._attr_unique_id = f"{self.id}_{self.entity_description.key}"
