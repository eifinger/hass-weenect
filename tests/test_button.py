"""Tests for the button platform."""

from unittest.mock import patch

import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.weenect.const import DOMAIN
from tests.const import MOCK_CONFIG


@pytest.mark.usefixtures("get_trackers")
async def test_button(hass):
    """Test that button works."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)
    await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()

    with patch("aioweenect.AioWeenect.activate_super_live") as mock:
        await hass.services.async_call(
            "button",
            "press",
            {"entity_id": "button.test_activate_super_live"},
            blocking=True,
        )
        await hass.async_block_till_done()
        mock.assert_called_once()

    with patch("aioweenect.AioWeenect.refresh_location") as mock:
        await hass.services.async_call(
            "button",
            "press",
            {"entity_id": "button.test_refresh_location"},
            blocking=True,
        )
        await hass.async_block_till_done()
        mock.assert_called_once()

    with patch("aioweenect.AioWeenect.ring") as mock:
        await hass.services.async_call("button", "press", {"entity_id": "button.test_ring"}, blocking=True)
        await hass.async_block_till_done()
        mock.assert_called_once()

    with patch("aioweenect.AioWeenect.vibrate") as mock:
        await hass.services.async_call("button", "press", {"entity_id": "button.test_vibrate"}, blocking=True)
        await hass.async_block_till_done()
        mock.assert_called_once()
