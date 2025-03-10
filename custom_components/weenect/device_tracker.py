"""Device tracker platform for weenect."""

from homeassistant.components.device_tracker import SourceType
from homeassistant.components.device_tracker.config_entry import TrackerEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.helpers import entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from custom_components.weenect.services import (
    SERVICE_SCHEMA,
    SERVICE_SET_UPDATE_INTERVAL_SCHEMA,
    UPDATE_INTERVAL,
    async_activate_super_live,
    async_refresh_location,
    async_ring,
    async_set_update_interval,
    async_vibrate,
)

from .const import (
    DOMAIN,
    SERVICE_ACTIVATE_SUPER_LIVE,
    SERVICE_REFRESH_LOCATION,
    SERVICE_RING,
    SERVICE_SET_UPDATE_INTERVAL,
    SERVICE_VIBRATE,
    TRACKER_ADDED,
)
from .entity import WeenectBaseEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the weenect device_trackers."""

    platform = entity_platform.async_get_current_platform()

    coordinator = hass.data[DOMAIN][entry.entry_id]

    @callback
    def async_add_device_trackers(
        added: list[str],
    ) -> None:
        """Add device_trackers callback."""

        trackers = [WeenectDeviceTracker(coordinator, tracker_id) for tracker_id in added]

        async_add_entities(trackers, True)

    unsub_dispatcher = async_dispatcher_connect(
        hass,
        f"{entry.entry_id}_{TRACKER_ADDED}",
        async_add_device_trackers,
    )
    entry.async_on_unload(unsub_dispatcher)
    if len(coordinator.data) > 0:
        async_add_device_trackers(coordinator.data.keys())

    async def async_call_service(service_call: ServiceCall) -> None:
        """Handle dispatched services."""
        assert platform is not None  # nosec
        entities = await platform.async_extract_from_service(service_call)

        tracker_ids = []
        for entity in entities:
            assert isinstance(entity, WeenectBaseEntity)  # nosec
            tracker_ids.append(entity.id)
        for tracker_id in set(tracker_ids):
            if service_call.service == SERVICE_SET_UPDATE_INTERVAL:
                await async_set_update_interval(hass, tracker_id, service_call.data[UPDATE_INTERVAL])
            if service_call.service == SERVICE_ACTIVATE_SUPER_LIVE:
                await async_activate_super_live(hass, tracker_id)
            if service_call.service == SERVICE_REFRESH_LOCATION:
                await async_refresh_location(hass, tracker_id)
            if service_call.service == SERVICE_RING:
                await async_ring(hass, tracker_id)
            if service_call.service == SERVICE_VIBRATE:
                await async_vibrate(hass, tracker_id)

    hass.services.async_register(
        DOMAIN,
        SERVICE_SET_UPDATE_INTERVAL,
        async_call_service,
        schema=SERVICE_SET_UPDATE_INTERVAL_SCHEMA,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_ACTIVATE_SUPER_LIVE,
        async_call_service,
        schema=SERVICE_SCHEMA,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_REFRESH_LOCATION,
        async_call_service,
        schema=SERVICE_SCHEMA,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_RING,
        async_call_service,
        schema=SERVICE_SCHEMA,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_VIBRATE,
        async_call_service,
        schema=SERVICE_SCHEMA,
    )


class WeenectDeviceTracker(WeenectBaseEntity, TrackerEntity):
    """weenect device tracker."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        tracker_id: str,
    ):
        super().__init__(coordinator, tracker_id)
        if self.coordinator.data[self.id]["type"].startswith("pet"):
            self._attr_icon = "mdi:paw"
        else:
            self._attr_icon = "mdi:tag"
        self._attr_unique_id = tracker_id
        self._attr_name = self.coordinator.data[self.id]["name"]

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return (
            super().available
            and bool(self.coordinator.data[self.id]["position"])
            and bool(self.coordinator.data[self.id]["position"][0]["is_online"])
        )

    @property
    def latitude(self):
        """Return latitude value of the device."""
        if self.id in self.coordinator.data:
            if self.coordinator.data[self.id]["position"]:
                return self.coordinator.data[self.id]["position"][0]["latitude"]

    @property
    def longitude(self):
        """Return longitude value of the device."""
        if self.id in self.coordinator.data:
            if self.coordinator.data[self.id]["position"]:
                return self.coordinator.data[self.id]["position"][0]["longitude"]

    @property
    def source_type(self) -> SourceType:
        """Return the source type, e.g. GPS or router, of the device."""
        return SourceType.GPS

    @property
    def location_accuracy(self):
        """Return the location accuracy of the device.

        Value in meters.
        """
        if self.id in self.coordinator.data:
            if self.coordinator.data[self.id]["position"]:
                return self.coordinator.data[self.id]["position"][0]["radius"]

    @property
    def extra_state_attributes(self):
        """Return device specific attributes."""
        res = self._attr_extra_state_attributes

        if self.id in self.coordinator.data:
            if self.coordinator.data[self.id]["position"]:
                res["speed"] = self.coordinator.data[self.id]["position"][0]["speed"]
                res["course"] = self.coordinator.data[self.id]["position"][0]["direction"]
                res["PDOP"] = self.coordinator.data[self.id]["position"][0]["pdop"]

        return res
