"""Sensor platform for weenect."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import List

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PERCENTAGE, SIGNAL_STRENGTH_DECIBELS, UnitOfTime
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.util import dt

from .const import DOMAIN, TRACKER_ADDED
from .entity import WeenectEntity

SENSOR_ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        name="Last Update Rate",
        key="last_freq_mode",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Sensor Mode",
        key="sensor_mode",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Last Sensor Mode",
        key="last_sensor_mode",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="SOS Phone Number",
        key="sos_phone",
        icon="mdi:phone-alert",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Subscription Remaining Days",
        key="remaining_days",
        icon="mdi:currency-usd-off",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Subscription Expiration Date",
        key="expiration_date",
        icon="mdi:currency-usd-off",
        device_class=SensorDeviceClass.TIMESTAMP,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Phone Call Usage",
        key="call_usage",
        icon="mdi:phone",
        entity_category=EntityCategory.DIAGNOSTIC,
        native_unit_of_measurement=UnitOfTime.SECONDS,
    ),
    SensorEntityDescription(
        name="Phone Call Max",
        key="call_max_threshold",
        icon="mdi:phone",
        entity_category=EntityCategory.DIAGNOSTIC,
        native_unit_of_measurement=UnitOfTime.SECONDS,
    ),
    SensorEntityDescription(
        name="Phone Call Available",
        key="call_available",
        icon="mdi:phone",
        entity_category=EntityCategory.DIAGNOSTIC,
        native_unit_of_measurement=UnitOfTime.SECONDS,
    ),
)

LOCATION_SENSOR_ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        name="Battery",
        key="battery",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.BATTERY,
        native_unit_of_measurement=PERCENTAGE,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Cell Tower Id",
        key="cellid",
        icon="mdi:radio-tower",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="GSM Strength",
        key="gsm",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.SIGNAL_STRENGTH,
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="Last Message Received",
        key="last_message",
        device_class=SensorDeviceClass.TIMESTAMP,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        name="GPS Satellites",
        key="satellites",
        icon="mdi:crosshairs-gps",
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
)

SUBSCRIPTION_SENSOR_ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        name="Next Charge",
        key="next_charge_at",
        icon="mdi:currency-usd",
        device_class=SensorDeviceClass.TIMESTAMP,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
)

USER_SENSOR_ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        name="SMS Available",
        key="sms",
        icon="mdi:message-processing",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the weenect sensors."""

    coordinator = hass.data[DOMAIN][entry.entry_id]

    @callback
    def async_add_sensors(
        added: List[int],
    ) -> None:
        """Add sensors callback."""

        sensors: list = []
        for tracker_id in added:
            for sensor_description in SENSOR_ENTITY_DESCRIPTIONS:
                sensors.append(
                    WeenectSensor(coordinator, tracker_id, sensor_description)
                )
            for location_sensor_description in LOCATION_SENSOR_ENTITY_DESCRIPTIONS:
                sensors.append(
                    WeenectLocationSensor(
                        coordinator, tracker_id, location_sensor_description
                    )
                )
            for (
                subscription_sensor_description
            ) in SUBSCRIPTION_SENSOR_ENTITY_DESCRIPTIONS:
                sensors.append(
                    WeenectSubscriptionSensor(
                        coordinator, tracker_id, subscription_sensor_description
                    )
                )
            for user_sensor_description in USER_SENSOR_ENTITY_DESCRIPTIONS:
                sensors.append(
                    WeenectUserSensor(coordinator, tracker_id, user_sensor_description)
                )

        async_add_entities(sensors, True)

    unsub_dispatcher = async_dispatcher_connect(
        hass,
        f"{entry.entry_id}_{TRACKER_ADDED}",
        async_add_sensors,
    )
    entry.async_on_unload(unsub_dispatcher)
    if len(coordinator.data) > 0:
        async_add_sensors(coordinator.data.keys())


class WeenectSensor(WeenectEntity, SensorEntity):
    """weenect sensor for general information."""

    def _get_call_available(self) -> int | None:
        """Return remaining call time."""
        if (
            "call_usage" in self.coordinator.data[self.id]
            and "call_max_threshold" in self.coordinator.data[self.id]
        ):
            return int(
                self.coordinator.data[self.id]["call_max_threshold"]
                - self.coordinator.data[self.id]["call_usage"]
            )
        else:
            return None

    @property
    def native_value(self) -> StateType | datetime:
        """Return the state of the resources if it has been received yet."""
        if self.id in self.coordinator.data:
            if self.entity_description.key == "call_available":
                return self._get_call_available()
            value = self.coordinator.data[self.id][self.entity_description.key]
            if self.device_class == str(SensorDeviceClass.TIMESTAMP):
                if value:
                    value = dt.parse_datetime(value)
                    if value and value.tzinfo is None:
                        value = value.replace(tzinfo=timezone.utc)
                    return value
            return value
        return None


class WeenectLocationSensor(WeenectSensor):
    """weenect sensor for location information."""

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        if self.entity_description.key in ["battery", "cellid", "gsm", "satellites"]:
            return super().available and bool(self.coordinator.data[self.id]["position"]) and bool(self.coordinator.data[self.id]["position"][0]["is_online"])
        return super().available and bool(self.coordinator.data[self.id]["position"])

    @property
    def native_value(self) -> StateType:
        """Return the state of the resources if it has been received yet."""
        if self.id in self.coordinator.data:
            if self.coordinator.data[self.id]["position"]:
                value = self.coordinator.data[self.id]["position"][0][
                    self.entity_description.key
                ]
                if self.device_class == str(SensorDeviceClass.TIMESTAMP):
                    if value:
                        value = dt.parse_datetime(value)
                        if value and value.tzinfo is None:
                            value = value.replace(tzinfo=timezone.utc)
                return value
        return None


class WeenectSubscriptionSensor(WeenectSensor):
    """weenect sensor for subscription information."""

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return super().available and bool(
            self.coordinator.data[self.id]["subscription"]
        )

    @property
    def native_value(self) -> StateType:
        """Return the state of the resources if it has been received yet."""
        if self.id in self.coordinator.data:
            if self.coordinator.data[self.id]["subscription"]:
                value = self.coordinator.data[self.id]["subscription"][
                    self.entity_description.key
                ]
                if self.device_class == str(SensorDeviceClass.TIMESTAMP):
                    if value:
                        value = dt.parse_datetime(value)
                        if value and value.tzinfo is None:
                            value = value.replace(tzinfo=timezone.utc)
                return value
        return None


class WeenectUserSensor(WeenectSensor):
    """weenect sensor for user information."""

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return super().available and bool(self.coordinator.data[self.id]["user"])

    @property
    def native_value(self) -> StateType:
        """Return the state of the resources if it has been received yet."""
        if self.id in self.coordinator.data:
            if self.coordinator.data[self.id]["user"]:
                value = self.coordinator.data[self.id]["user"][
                    self.entity_description.key
                ]
                return value
        return None
