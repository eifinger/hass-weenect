"""weenect class"""
# pyright: reportGeneralTypeIssues=false
from __future__ import annotations

from typing import Dict, Optional

from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import ATTRIBUTION, DOMAIN, NAME


class WeenectEntity(CoordinatorEntity):
    """Base entity for weenect."""

    def __init__(self, coordinator: DataUpdateCoordinator, tracker_id: int) -> None:
        super().__init__(coordinator)
        self.id = tracker_id
        self._attr_attribution = ATTRIBUTION

    @property
    def device_name(self) -> Optional[str]:
        """Return the name of this tracker."""
        if self.id in self.coordinator.data:
            return str(self.coordinator.data[self.id]["name"])
        return None

    @property
    def imei(self) -> Optional[str]:
        """Return the imei of this tracker."""
        if self.id in self.coordinator.data:
            return str(self.coordinator.data[self.id]["imei"])
        return None

    @property
    def sim(self) -> Optional[str]:
        """Return the sim of this tracker."""
        if self.id in self.coordinator.data:
            return str(self.coordinator.data[self.id]["sim"])
        return None

    @property
    def tracker_type(self) -> Optional[str]:
        """Return the type of this tracker."""
        if self.id in self.coordinator.data:
            return str(self.coordinator.data[self.id]["type"])
        return None

    @property
    def firmware(self) -> Optional[str]:
        """Return the firmware of this tracker."""
        if self.id in self.coordinator.data:
            return str(self.coordinator.data[self.id]["firmware"])
        return None

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self.id)},
            name=self.device_name,
            model=self.tracker_type,
            manufacturer=NAME,
            sw_version=self.firmware,
        )

    @property
    def extra_state_attributes(self) -> Dict[str, Optional[str] | Optional[int]]:
        """Return the state attributes."""
        return {
            "id": self.id,
            "sim": self.sim,
            "imei": self.imei,
        }
