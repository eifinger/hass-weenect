"""Tests for the sensor platform."""

import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.weenect.const import ATTRIBUTION, DOMAIN
from tests.const import MOCK_CONFIG


@pytest.mark.usefixtures("get_trackers")
async def test_sensor(hass):
    """Test that sensor works."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()

    assert (
        hass.states.get("sensor.test_sensor_mode").attributes["attribution"]
        == ATTRIBUTION
    )
    assert hass.states.get("sensor.test_sensor_mode").attributes["id"] == 100000
    assert (
        hass.states.get("sensor.test_sensor_mode").attributes["sim"]
        == "8849390213023093728"
    )
    assert (
        hass.states.get("sensor.test_sensor_mode").attributes["imei"]
        == "160389554842512"
    )

    assert hass.states.get("sensor.test_last_update_rate").state == "10M"
    assert hass.states.get("sensor.test_sensor_mode").state == "normal"
    assert hass.states.get("sensor.test_last_sensor_mode").state == "normal"
    assert hass.states.get("sensor.test_battery").state == "95"
    assert hass.states.get("sensor.test_cell_tower_id").state == "26233-B7AD-E77B"
    assert hass.states.get("sensor.test_gsm_strength").state == "17"
    assert (
        hass.states.get("sensor.test_last_message_received").state
        == "2021-04-15T08:29:28+00:00"
    )
    assert hass.states.get("sensor.test_gps_satellites").state == "0"

    assert hass.states.get("sensor.test_sos_phone_number").state == "+4917383836316"
    assert hass.states.get("sensor.test_subscription_remaining_days").state == "524"
    assert (
        hass.states.get("sensor.test_subscription_expiration_date").state
        == "2022-09-21T11:34:12+00:00"
    )
    assert hass.states.get("sensor.test_phone_call_usage").state == "100"
    assert hass.states.get("sensor.test_phone_call_max").state == "600"
    assert hass.states.get("sensor.test_phone_call_available").state == "500"
    assert (
        hass.states.get("sensor.test_next_charge").state == "2022-09-21T11:34:12+00:00"
    )
    assert hass.states.get("sensor.test_sms_available").state == "13"


@pytest.mark.usefixtures("get_trackers")
async def test_device_class_does_not_return_string_for_its_state(hass, caplog):
    """Test that sensor works."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()

    assert (
        "is providing a string for its state, while the device class is"
        not in caplog.text
    )


@pytest.mark.usefixtures("get_trackers_last_message_none")
async def test_sensor_with_last_message_none(hass):
    """Test that the special timestamp sensor works for a None value ."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()

    assert hass.states.get("sensor.test_last_message_received").state == "unknown"


@pytest.mark.usefixtures("get_trackers_phone_call_available_minuend_missing")
async def test_sensor_with_call_available_minuend_missing(hass):
    """Test that the subtraction sensor works when minuend is not available ."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()

    assert hass.states.get("sensor.test_phone_call_available") == None


@pytest.mark.usefixtures("get_trackers_phone_call_available_subtrahend_missing")
async def test_sensor_with_call_available_subtrahend_missing(hass):
    """Test that the subtraction sensor works when subtrahend is not available ."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(config_entry.entry_id)

    await hass.async_block_till_done()

    assert hass.states.get("sensor.test_phone_call_available") == None
