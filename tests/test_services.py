"""Tests for the device_tracker platform."""

from unittest.mock import patch

import pytest
from homeassistant.const import ATTR_ENTITY_ID
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.weenect.const import DOMAIN
from custom_components.weenect.services import (
    SERVICE_ACTIVATE_SUPER_LIVE,
    SERVICE_REFRESH_LOCATION,
    SERVICE_RING,
    SERVICE_SET_UPDATE_INTERVAL,
    SERVICE_VIBRATE,
)
from tests.const import MOCK_CONFIG


@pytest.mark.usefixtures("get_trackers")
async def test_services(hass):
    """Test service calls."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)
    await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()

    with patch("aioweenect.AioWeenect.set_update_interval") as mock:
        await hass.services.async_call(
            DOMAIN,
            SERVICE_SET_UPDATE_INTERVAL,
            {ATTR_ENTITY_ID: "device_tracker.test"},
            blocking=True,
        )
        await hass.async_block_till_done()
        mock.assert_called_once()

    with patch("aioweenect.AioWeenect.activate_super_live") as mock:
        await hass.services.async_call(
            DOMAIN,
            SERVICE_ACTIVATE_SUPER_LIVE,
            {ATTR_ENTITY_ID: "device_tracker.test"},
            blocking=True,
        )
        await hass.async_block_till_done()
        mock.assert_called_once()

    with patch("aioweenect.AioWeenect.refresh_location") as mock:
        await hass.services.async_call(
            DOMAIN,
            SERVICE_REFRESH_LOCATION,
            {ATTR_ENTITY_ID: "device_tracker.test"},
            blocking=True,
        )
        await hass.async_block_till_done()
        mock.assert_called_once()

    with patch("aioweenect.AioWeenect.ring") as mock:
        await hass.services.async_call(
            DOMAIN, SERVICE_RING, {ATTR_ENTITY_ID: "device_tracker.test"}, blocking=True
        )
        await hass.async_block_till_done()
        mock.assert_called_once()

    with patch("aioweenect.AioWeenect.vibrate") as mock:
        await hass.services.async_call(
            DOMAIN,
            SERVICE_VIBRATE,
            {ATTR_ENTITY_ID: "device_tracker.test"},
            blocking=True,
        )
        await hass.async_block_till_done()
        mock.assert_called_once()
