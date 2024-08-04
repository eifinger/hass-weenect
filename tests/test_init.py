"""Test weenect setup process."""

import pytest
from homeassistant.exceptions import ConfigEntryNotReady
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.weenect import (
    WeenectDataUpdateCoordinator,
    async_setup_entry,
    async_unload_entry,
)
from custom_components.weenect.const import DOMAIN

from .const import MOCK_CONFIG


# We can pass fixtures as defined in conftest.py to tell pytest to use the fixture
# for a given test. We can also leverage fixtures and mocks that are available in
# Home Assistant using the pytest_homeassistant_custom_component plugin.
# Assertions allow you to verify that the return value of whatever is on the left
# side of the assertion matches with the right side.
@pytest.mark.usefixtures("bypass_get_trackers")
async def test_setup_unload_and_reload_entry(hass):
    """Test entry setup and unload."""
    # Create a mock entry so we don't have to go through config flow
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)
    await hass.async_block_till_done()

    await hass.config_entries.async_setup(config_entry.entry_id)

    assert DOMAIN in hass.data and config_entry.entry_id in hass.data[DOMAIN]
    assert isinstance(hass.data[DOMAIN][config_entry.entry_id], WeenectDataUpdateCoordinator)

    # Unload the entry and verify that the data has been removed
    assert await async_unload_entry(hass, config_entry)
    assert config_entry.entry_id not in hass.data[DOMAIN]


@pytest.mark.usefixtures("error_on_get_trackers")
async def test_setup_entry_exception(hass, caplog):
    """Test ConfigEntryNotReady when API raises an exception during entry setup."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")

    # In this case we are testing the condition where async_setup_entry raises
    # ConfigEntryNotReady using the `error_on_get_trackers` fixture which simulates
    # an error.
    with pytest.raises(ConfigEntryNotReady):
        assert await async_setup_entry(hass, config_entry)
    assert "Dummy Exception Message" in caplog.text


@pytest.mark.usefixtures("get_trackers_last_freq_mode_none")
async def test_setup_entry_last_freq_mode_none(hass, caplog):
    """Test ConfigEntryNotReady when last_freq_mode is None."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()
    assert "TypeError: expected string or bytes-like object" not in caplog.text
