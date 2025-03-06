"""Constants for weenect tests."""

from typing import Any

from custom_components.weenect.const import CONF_PASSWORD, CONF_USERNAME

# Mock config data to be used across multiple tests
MOCK_CONFIG: dict[str, str] = {
    CONF_USERNAME: "test_username",
    CONF_PASSWORD: "test_password",
}

GET_RACKERS_RESPONSE: dict[str, Any] = {
    "items": [
        {
            "id": 100000,
            "name": "Test",
            "imei": 160389554842512,
            "sim": "8849390213023093728",
            "type": "pet2",
            "firmware": "pet3",
            "need_upgrade": False,
            "features": [
                "sos_button",
                "mode_gsensor",
                "mode_selection",
                "ringing",
                "vibrate",
                "activity_tracking",
                "super_tracking",
            ],
            "icon": None,
            "color": None,
            "creation_date": "2020-09-21T11:32:27.139332",
            "activation_date": "2020-09-21T11:32:27.136611",
            "first_connection_date": "2020-09-21T11:35:25.385947",
            "sos_phone": "+4917383836316",
            "sos_mode": "full-sos",
            "call_usage": 100,
            "call_notification": 0,
            "call_low_threshold": 420,
            "call_max_threshold": 600,
            "call_directly": False,
            "sos_appli_notification": True,
            "sos_mail_notification": False,
            "sos_sms_notification": False,
            "area_appli_notification": True,
            "area_mail_notification": True,
            "area_sms_notification": False,
            "report_appli_notification": True,
            "report_mail_notification": True,
            "report_sms_notification": False,
            "battery_appli_notification": True,
            "battery_mail_notification": True,
            "battery_sms_notification": False,
            "battery_threshold": 30,
            "battery_charged": 2,
            "button_appli_notification": True,
            "button_mail_notification": True,
            "button_sms_notification": False,
            "geofence_mode": "normal",
            "geofence_number": 0,
            "nb_geofence_out": 0,
            "spy_sos": False,
            "enable_ai": False,
            "enable_ai_spec": "",
            "force_subscription": False,
            "had_subscription": True,
            "expiration_date": "2022-09-21T11:34:12.704032",
            "remaining_days": 524,
            "valid_signal": False,
            "timezone": "Etc/UTC",
            "warranty_start": "2020-09-21T11:32:27.136611",
            "warranty_end": "2022-09-21T11:32:27.136611",
            "sales_data": {
                "vendor": "Amazon",
                "vendor_id": 32,
                "kind": "pet2",
                "warranty": "default",
            },
            "retailer_id": 32,
            "user": {
                "id": 100000,
                "site": "weenect",
                "mail": "test@googlemail.com",
                "valid": None,
                "is_admin": False,
                "is_security": False,
                "role_retailer_id": 0,
                "role_site": None,
                "need_subscription": True,
                "lastname": "Test",
                "firstname": "Test",
                "contact_mail": "",
                "address": "Eugen-Salomon-Straße 1",
                "postal_code": "55128",
                "city": "Mainz",
                "country": "DE",
                "phone": "+4917383836316",
                "creation_date": "2020-09-21T11:31:39.056246",
                "connection_date": "2021-04-15T08:31:47.625721",
                "last_connection_date": "2021-04-15T08:31:07.217021",
                "sms": 13,
                "language": "de",
                "optin": False,
                "promo_code": None,
                "activate_sponsoring": True,
                "sponsorship_gain_amount": 0,
                "sponsorship_benefit": 0,
                "disable_history": False,
                "short_code": None,
                "is_b2b": False,
                "product_review_link": "https://www.amazon.de/review/create-review/ref=cm_cr_pr_wr_but_top?ie=UTF8&nodeID=&asin=B08HG22PPD#",  # noqa: line-too-long
                "preferred_metric_system": "km",
                "white_label": None,
            },
            "buttons": [
                {
                    "id": 100000,
                    "number": 1,
                    "name": None,
                    "message": "",
                    "active": False,
                    "tracker_id": 100000,
                },
                {
                    "id": 100001,
                    "number": 2,
                    "name": None,
                    "message": "",
                    "active": False,
                    "tracker_id": 100000,
                },
                {
                    "id": 100002,
                    "number": 3,
                    "name": None,
                    "message": "",
                    "active": False,
                    "tracker_id": 100000,
                },
            ],
            "mail_contacts": [
                {
                    "id": 100003,
                    "number": 1,
                    "mail": "test@googlemail.com",
                    "tracker_id": 100000,
                }
            ],
            "sms_contacts": [
                {
                    "id": 100004,
                    "number": 1,
                    "phone": "+4917383836316",
                    "tracker_id": 100000,
                }
            ],
            "position": [
                {
                    "id": "6967da424787af4a9b5f8409",
                    "battery": 95,
                    "cellid": "26233-B7AD-E77B",
                    "mcc": 0,
                    "mnc": 0,
                    "lac": 0,
                    "cid": 0,
                    "date_server": "2021-04-15T08:29:28+00:00",
                    "date_tracker": "2021-04-15T05:53:24+00:00",
                    "direction": 312,
                    "geofence_name": None,
                    "gsm": 17,
                    "last_message": "2021-04-15T08:29:28+00:00",
                    "latitude": 47.024191,
                    "longitude": 6.2642536,
                    "pdop": 99.9,
                    "radius": 31,
                    "satellites": 0,
                    "speed": 4.8,
                    "type": "ALM-V",
                    "valid_signal": False,
                    "confidence": None,
                    "original_battery": 74,
                    "is_online": True,
                    "battery_text": "La batterie est bien charg\u00e9e.",
                    "battery_color": "green",
                    "signal_strength_percent": 43,
                    "gsm_text": "Le r\u00e9seau GSM est moyen, les performances du traceur peuvent \u00eatre affect\u00e9es.",
                    "gsm_color": "yellow",
                    "accuracy_text": "La pr\u00e9cision GPS est optimale !",
                    "accuracy_color": "green",
                    "wifi_zone_id": 0,
                    "is_in_deep_sleep": False,
                }
            ],
            "subscription": {
                "id": 100000,
                "site": "weenect",
                "max_tracker_nb": 1,
                "period": 24,
                "amount": 8990,
                "amount_gbp": 6483,
                "currency": "EUR",
                "status": "active",
                "option_status": True,
                "payment_mean": "hipay",
                "next_charge_at": "2022-09-21T11:34:12.704032",
                "created_at": "2020-09-21T11:33:29.468075",
                "updated_at": "2020-09-21T11:34:12.716050",
                "canceled_at": None,
                "cancel_reason": None,
                "cancel_explanation": None,
                "offer_id": 4,
                "trackers": [100000],
                "user_id": 100000,
                "is_under_commitment_period": False,
            },
            "last_change": None,
            "last_request": None,
            "freq_mode": "10M",
            "last_freq_mode": "10M",
            "sensor_mode": "normal",
            "has_activity_tracking": False,
            "last_sensor_mode": "normal",
            "activation_result": None,
        }
    ],
    "total": 1,
}
