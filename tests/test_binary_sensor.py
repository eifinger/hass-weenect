"""Tests for the binary_sensor platform."""

import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.weenect.const import ATTRIBUTION, DOMAIN
from tests.const import MOCK_CONFIG


@pytest.mark.usefixtures("get_trackers")
async def test_binary_sensor(hass):
    """Test that binary_sensor works."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()

    assert (
        hass.states.get("binary_sensor.test_valid_signal").attributes["attribution"]
        == ATTRIBUTION
    )
    assert hass.states.get("binary_sensor.test_valid_signal").attributes["id"] == 100000
    assert (
        hass.states.get("binary_sensor.test_valid_signal").attributes["sim"]
        == "8849390213023093728"
    )
    assert (
        hass.states.get("binary_sensor.test_valid_signal").attributes["imei"]
        == "160389554842512"
    )

    assert hass.states.get("binary_sensor.test_valid_signal").state == "off"
    assert hass.states.get("binary_sensor.test_is_online").state == "on"


@pytest.mark.usefixtures("get_trackers_when_offline")
async def test_binary_sensor_unavailable_when_offline(hass):
    """Test that valid_signal is unavailable when offline."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()

    assert hass.states.get("binary_sensor.test_valid_signal").state == "unavailable"
