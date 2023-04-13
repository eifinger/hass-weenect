"""
Custom integration to integrate weenect with Home Assistant.

For more details about this integration, please refer to
https://github.com/eifinger/hass-weenect
"""
# pyright: reportGeneralTypeIssues=false
import logging
import re
from datetime import timedelta
from typing import Any, Dict, Optional

from aioweenect import AioWeenect
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_send
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    CONF_PASSWORD,
    CONF_USERNAME,
    DOMAIN,
    PLATFORMS,
    STARTUP_MESSAGE,
    TRACKER_ADDED,
)

_LOGGER: logging.Logger = logging.getLogger(__package__)

DEFAULT_UPDATE_RATE = 30


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up this integration using UI."""
    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})
        _LOGGER.info(STARTUP_MESSAGE)

    username = entry.data.get(CONF_USERNAME)
    password = entry.data.get(CONF_PASSWORD)

    session = async_get_clientsession(hass)
    client = AioWeenect(username=username, password=password, session=session)

    coordinator = WeenectDataUpdateCoordinator(hass, config_entry=entry, client=client)
    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(async_reload_entry))
    return True


class WeenectDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    def __init__(
        self, hass: HomeAssistant, config_entry: ConfigEntry, client: AioWeenect
    ) -> None:
        """Initialize."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_UPDATE_RATE),
        )
        self.client = client
        self.config_entry = config_entry
        self.data: Dict[str, Any] = {}

    async def _async_update_data(self) -> Dict[int, Any]:
        """Update data via library."""
        try:
            data = await self.client.get_trackers()
            data = self.transform_data(data)
            self._detect_added_and_removed_trackers(data)
            self._adjust_update_rate(data)
            return data  # type: ignore
        except Exception as exception:
            raise UpdateFailed(exception) from exception

    def _detect_added_and_removed_trackers(self, data: Dict[int, Any]) -> None:
        """Detect if trackers were added or removed."""
        added = set(data.keys()) - set(self.data.keys())  # type: ignore
        async_dispatcher_send(
            self.hass, f"{self.config_entry.entry_id}_{TRACKER_ADDED}", added
        )

    def _adjust_update_rate(self, data: Dict[int, Any]) -> None:
        """Set the update rate to the shortest update rate of all trackers."""
        update_rate = timedelta(seconds=DEFAULT_UPDATE_RATE)
        for tracker in data.values():
            tracker_rate = self.parse_duration(tracker["last_freq_mode"])
            if tracker_rate and tracker_rate < update_rate:
                update_rate = tracker_rate
        self.update_interval = update_rate
        _LOGGER.debug("Setting update_interval to %s", update_rate)

    @staticmethod
    def transform_data(data: Any) -> Dict[int, Any]:
        """Extract trackers from list and put them in a dict by tracker id."""
        result = {}
        for tracker in data["items"]:
            result[tracker["id"]] = tracker
        return result

    @staticmethod
    def parse_duration(duration: str) -> Optional[timedelta]:
        """Parse a timedelta from a weenect duration."""
        pattern = re.compile(r"\d\d[S,M,H]")

        if pattern.match(duration) is not None:
            if duration.endswith("S"):
                return timedelta(seconds=float(duration[:-1]))
            if duration.endswith("M"):
                return timedelta(minutes=float(duration[:-1]))
            if duration.endswith("H"):
                return timedelta(hours=float(duration[:-1]))
        return None


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle removal of an entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)
