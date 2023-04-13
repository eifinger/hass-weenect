"""Global fixtures for integration_blueprint integration."""
from unittest.mock import AsyncMock, patch

import pytest

from tests.const import GET_RACKERS_RESPONSE

pytest_plugins = "pytest_homeassistant_custom_component"  # pylint: disable=invalid-name


@pytest.fixture(autouse=True)
def expected_lingering_timers() -> bool:
    """Temporary ability to bypass test failures.
    Parametrize to True to bypass the pytest failure.
    @pytest.mark.parametrize("expected_lingering_timers", [True])
    This should be removed when all lingering timers have been cleaned up.
    """
    return True

# This fixture enables loading custom integrations in all tests.
# Remove to enable selective use of this fixture
@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):  # noqa: F841
    """Enable custom integration loading."""
    yield


# This fixture, when used, will result in calls to get_trackers to return None. To have the call
# return a value, we would add the `return_value=<VALUE_TO_RETURN>` parameter to the patch call.
@pytest.fixture(name="bypass_get_trackers")
def bypass_get_trackers_fixture():
    """Skip calls to get data from weenect."""
    with patch("aioweenect.AioWeenect.get_trackers"):
        yield


# This fixture, when used, will result in calls to login to return None. To have the call
# return a value, we would add the `return_value=<VALUE_TO_RETURN>` parameter to the patch call.
@pytest.fixture(name="bypass_login")
def bypass_login_fixture():
    """Skip calls to login to weenect."""
    with patch("aioweenect.AioWeenect.login"):
        yield


# In this fixture, we are forcing calls to get_trackers to raise an Exception. This is useful
# for exception handling.
@pytest.fixture(name="error_on_get_trackers")
def error_get_trackers_fixture():
    """Simulate error when retrieving data from weenect."""
    with patch(
        "aioweenect.AioWeenect.get_trackers",
        side_effect=Exception,
    ):
        yield


# In this fixture, we are forcing calls to get_trackers to return a static result.
# This is useful to test the platforms.
@pytest.fixture(name="get_trackers")
def get_trackers_fixture():
    """Static result when retrieving data from weenect."""
    with patch(
        "aioweenect.AioWeenect.get_trackers",
        side_effect=AsyncMock(return_value=GET_RACKERS_RESPONSE),
    ):
        yield
