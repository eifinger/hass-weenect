"""Tests for the sensor platform."""

import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.weenect.const import DOMAIN
from tests.const import MOCK_CONFIG


@pytest.mark.usefixtures("get_trackers")
async def test_select(hass):
    """Test that select works."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()

    assert hass.states.get("select.test_update_rate").state == "10M"
