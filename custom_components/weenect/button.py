"""Support for weenect button entities."""
from __future__ import annotations

from typing import List

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import (
    BUTTON_ENTITY_DESCRIPTIONS,
    DOMAIN,
    SERVICE_ACTIVATE_SUPER_LIVE,
    SERVICE_REFRESH_LOCATION,
    SERVICE_RING,
    SERVICE_VIBRATE,
    TRACKER_ADDED,
)
from .entity import WeenectEntity
from .services import (
    async_activate_super_live,
    async_refresh_location,
    async_ring,
    async_vibrate,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the weenect buttons."""

    coordinator = hass.data[DOMAIN][entry.entry_id]

    @callback
    def async_add_buttons(
        added: List[int],
    ) -> None:
        """Add buttons callback."""

        selects: list = []
        for tracker_id in added:
            for button_description in BUTTON_ENTITY_DESCRIPTIONS:
                selects.append(
                    WeenectButton(coordinator, tracker_id, button_description)
                )

        async_add_entities(selects, True)

    unsub_dispatcher = async_dispatcher_connect(
        hass,
        f"{entry.entry_id}_{TRACKER_ADDED}",
        async_add_buttons,
    )
    coordinator.unsub_dispatchers.append(unsub_dispatcher)
    if len(coordinator.data) > 0:
        async_add_buttons(coordinator.data.keys())


class WeenectButton(WeenectEntity, ButtonEntity):
    """Representation of a weenect button."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        tracker_id: int,
        entity_description: ButtonEntityDescription,
    ):
        super().__init__(coordinator, tracker_id)
        self.entity_description = entity_description
        self._attr_unique_id = f"{tracker_id}_{entity_description.key}"

    @property
    def name(self):
        """Return the name of this sensor."""
        if self.id in self.coordinator.data:
            return f"{self.coordinator.data[self.id]['name']} {self.entity_description.name}"
        return None

    async def async_press(self) -> None:
        """Handle the button press."""
        if self.entity_description.key == SERVICE_ACTIVATE_SUPER_LIVE:
            await async_activate_super_live(self.hass, self.id)
        if self.entity_description.key == SERVICE_REFRESH_LOCATION:
            await async_refresh_location(self.hass, self.id)
        if self.entity_description.key == SERVICE_RING:
            await async_ring(self.hass, self.id)
        if self.entity_description.key == SERVICE_VIBRATE:
            await async_vibrate(self.hass, self.id)
