"""Support for weenect select entities."""
from __future__ import annotations

from typing import List

from homeassistant.components.select import SelectEntity, SelectEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from custom_components.weenect.services import async_set_update_interval

from .const import DOMAIN, TRACKER_ADDED
from .entity import WeenectEntity

SELECT_OPTIONS = ("0S", "30S", "1M", "2M", "3M", "5M", "10M")
DEFAULT_SELECT_OPTION = "10M"

SELECT_ENTITY_DESCRIPTIONS: tuple[SelectEntityDescription, ...] = (
    SelectEntityDescription(
        name="Update Rate",
        key="freq_mode",
        entity_category=EntityCategory.CONFIG,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the weenect selects."""

    coordinator = hass.data[DOMAIN][entry.entry_id]

    @callback
    def async_add_selects(
        added: List[int],
    ) -> None:
        """Add selects callback."""

        selects: list = []
        for tracker_id in added:
            for select_description in SELECT_ENTITY_DESCRIPTIONS:
                selects.append(
                    WeenectSelect(coordinator, tracker_id, select_description)
                )

        async_add_entities(selects, True)

    unsub_dispatcher = async_dispatcher_connect(
        hass,
        f"{entry.entry_id}_{TRACKER_ADDED}",
        async_add_selects,
    )
    entry.async_on_unload(unsub_dispatcher)
    if len(coordinator.data) > 0:
        async_add_selects(coordinator.data.keys())


class WeenectSelect(WeenectEntity, SelectEntity):
    """Representation of a weenect select."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        tracker_id: int,
        entity_description: SelectEntityDescription,
    ):
        super().__init__(coordinator, tracker_id, entity_description)
        self._attr_options = SELECT_OPTIONS

    @property
    def current_option(self) -> str:
        """Return the selected entity option to represent the entity state."""
        if self.id in self.coordinator.data:
            return str(self.coordinator.data[self.id][self.entity_description.key])
        return DEFAULT_SELECT_OPTION

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        await async_set_update_interval(self.hass, self.id, option)
