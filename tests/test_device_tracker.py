"""Tests for the device_tracker platform."""

import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.weenect.const import ATTRIBUTION, DOMAIN
from tests.const import MOCK_CONFIG


@pytest.mark.usefixtures("get_trackers")
async def test_device_tracker(hass):
    """Test that device_tracker works."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()

    assert (
        hass.states.get("device_tracker.test").attributes["attribution"] == ATTRIBUTION
    )
    assert hass.states.get("device_tracker.test").attributes["id"] == 100000
    assert (
        hass.states.get("device_tracker.test").attributes["sim"]
        == "8849390213023093728"
    )
    assert (
        hass.states.get("device_tracker.test").attributes["imei"] == "160389554842512"
    )

    assert hass.states.get("device_tracker.test").state == "not_home"
    assert hass.states.get("device_tracker.test").attributes["source_type"] == "gps"
    assert hass.states.get("device_tracker.test").attributes["latitude"] == 47.024191
    assert hass.states.get("device_tracker.test").attributes["gps_accuracy"] == 31
    assert hass.states.get("device_tracker.test").attributes["icon"] == "mdi:paw"


@pytest.mark.usefixtures("get_trackers_not_a_pet_tracker")
async def test_device_tracker_not_a_pet_tracker(hass):
    """Test that device_tracker icon changes when it's not a pet tracker ."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()

    assert hass.states.get("device_tracker.test").attributes["icon"] == "mdi:tag"


@pytest.mark.usefixtures("get_trackers_when_offline")
async def test_device_tracker_unavailable_when_offline(hass):
    """Test that device_tracker is unavailable when offline."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()

    assert hass.states.get("device_tracker.test").state == "unavailable"
