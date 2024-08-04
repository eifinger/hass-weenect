"""weenect services."""

import logging

import voluptuous as vol
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN, UPDATE_INTERVAL

DOMAIN_SERVICES = f"{DOMAIN}_services"

SERVICE_SET_UPDATE_INTERVAL_SCHEMA = cv.make_entity_service_schema(
    {
        vol.Optional(UPDATE_INTERVAL, default="10M"): cv.string,
    }
)

SERVICE_SCHEMA = cv.make_entity_service_schema({})

_LOGGER: logging.Logger = logging.getLogger(__package__)


def _is_valid_tracker_id(hass, tracker_id, config_entry) -> bool:
    """Determine whether the config_entry is valid this tracker_id."""
    if tracker_id in hass.data[DOMAIN][config_entry].data:
        return True
    _LOGGER.warning(
        "Could not find a registered integration for tracker with id: %s",
        tracker_id,
    )
    return False


async def async_set_update_interval(hass: HomeAssistant, tracker_id: str, update_interval: str):
    """Set the update interval for this tracker id."""

    for config_entry in hass.data[DOMAIN]:
        if _is_valid_tracker_id(hass, tracker_id, config_entry):
            await hass.data[DOMAIN][config_entry].client.set_update_interval(tracker_id, update_interval)


async def async_activate_super_live(hass: HomeAssistant, tracker_id: str):
    """Activate the super live mode for this tracker id."""

    for config_entry in hass.data[DOMAIN]:
        if _is_valid_tracker_id(hass, tracker_id, config_entry):
            await hass.data[DOMAIN][config_entry].client.activate_super_live(tracker_id)


async def async_refresh_location(hass: HomeAssistant, tracker_id: str):
    """Request a position refresh for this tracker id."""

    for config_entry in hass.data[DOMAIN]:
        if _is_valid_tracker_id(hass, tracker_id, config_entry):
            await hass.data[DOMAIN][config_entry].client.refresh_location(tracker_id)


async def async_ring(hass: HomeAssistant, tracker_id: str):
    """Send a ring command for this tracker id."""

    for config_entry in hass.data[DOMAIN]:
        if _is_valid_tracker_id(hass, tracker_id, config_entry):
            await hass.data[DOMAIN][config_entry].client.ring(tracker_id)


async def async_vibrate(hass: HomeAssistant, tracker_id: str):
    """Send a vibrate command for this tracker id."""

    for config_entry in hass.data[DOMAIN]:
        if _is_valid_tracker_id(hass, tracker_id, config_entry):
            await hass.data[DOMAIN][config_entry].client.vibrate(tracker_id)
