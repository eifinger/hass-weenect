# Changelog

<!--next-version-placeholder-->

## v5.1.1 (2024-05-14)

### Fix

* Unique_id is not a string ([#374](https://github.com/eifinger/hass-weenect/issues/374)) ([`43b8b5e`](https://github.com/eifinger/hass-weenect/commit/43b8b5ec1dda6f3296cfd704058a13a94bff22b8))

## v5.1.0 (2024-03-10)

### Feature

* Add extra attributes to device_tracker ([#371](https://github.com/eifinger/hass-weenect/issues/371)) ([`cac4af9`](https://github.com/eifinger/hass-weenect/commit/cac4af9241eab41a48a4bbf495df4eb913b808b7))

## v5.0.0 (2024-03-10)

### Fix

* Some sensors should be "unavailable" when the tracker is offline ([#372](https://github.com/eifinger/hass-weenect/issues/372)) ([`067bd3b`](https://github.com/eifinger/hass-weenect/commit/067bd3ba3a710c8c7d10033fb810d7b43a482682))

### Breaking

* some sensors should be "unavailable" when the tracker is offline ([#372](https://github.com/eifinger/hass-weenect/issues/372)) ([`067bd3b`](https://github.com/eifinger/hass-weenect/commit/067bd3ba3a710c8c7d10033fb810d7b43a482682))

## v4.1.0 (2024-03-06)

### Feature

* Release new sensors ([`59f3c55`](https://github.com/eifinger/hass-weenect/commit/59f3c5506a3a3d49e4a9868928de508de62e91d6))

## v4.0.0 (2024-03-06)

### Feature

* Update intervals ([#367](https://github.com/eifinger/hass-weenect/issues/367)) ([`ac1cf1a`](https://github.com/eifinger/hass-weenect/commit/ac1cf1a7a6f2fcff3ff6d9a722ba6cc9c9132d88))

### Breaking

* Update intervals ([#367](https://github.com/eifinger/hass-weenect/issues/367)) ([`ac1cf1a`](https://github.com/eifinger/hass-weenect/commit/ac1cf1a7a6f2fcff3ff6d9a722ba6cc9c9132d88))

### Documentation

* Add how to disable tracking to README.md ([#366](https://github.com/eifinger/hass-weenect/issues/366)) ([`d53802c`](https://github.com/eifinger/hass-weenect/commit/d53802ca13d5ffcd6642caec72d0d7fa6e458793))

## v3.3.1 (2024-02-28)

### Fix

* Replace deprecated SOURCE_TYPE_GPS with SourceType.GPS ([#365](https://github.com/eifinger/hass-weenect/issues/365)) ([`892c031`](https://github.com/eifinger/hass-weenect/commit/892c031c484a6c09d682284c198227470eb685e9))

## v3.3.0 (2024-02-27)

### Feature

* Allow disabling gps ([#363](https://github.com/eifinger/hass-weenect/issues/363)) ([`622c4f1`](https://github.com/eifinger/hass-weenect/commit/622c4f1de52014e39d2f2ef1e6b009a16cc6754f))

## v3.2.4 (2023-10-05)

### Fix

* Handle empty last_message_received ([#323](https://github.com/eifinger/hass-weenect/issues/323)) ([`f1b6bcf`](https://github.com/eifinger/hass-weenect/commit/f1b6bcf2635a6277b0e84b6f6552421c1b912a55))

## v3.2.3 (2023-10-05)

### Fix

* Log responses in debug mode ([#322](https://github.com/eifinger/hass-weenect/issues/322)) ([`64db8e7`](https://github.com/eifinger/hass-weenect/commit/64db8e7b5eb206b9edbb1f783ec2c4f60c657022))

## v3.2.2 (2023-08-27)

### Fix

* Check for None in parse_duration ([`f73d33e`](https://github.com/eifinger/hass-weenect/commit/f73d33ec8314737ac6d95204197741303ce10d3a))

## v3.2.1 (2023-08-23)

### Fix

* Allow multiple entries ([#306](https://github.com/eifinger/hass-weenect/issues/306)) ([`a1bbeb6`](https://github.com/eifinger/hass-weenect/commit/a1bbeb6303851744c072c005eb8dbf420d282544))

## v3.2.0 (2023-07-28)

### Feature

* Add service translations ([#294](https://github.com/eifinger/hass-weenect/issues/294)) ([`f427381`](https://github.com/eifinger/hass-weenect/commit/f4273819d82455efe52a94a232ec3ce9fa304891))

## v3.1.0 (2023-06-25)

### Feature

* Add debug log for exceptions ([#274](https://github.com/eifinger/hass-weenect/issues/274)) ([`ee41f76`](https://github.com/eifinger/hass-weenect/commit/ee41f7672ff5ba9dd9c7d23199c42e9f3b335539))

## v3.0.1 (2023-04-13)
### Fix
* Enable commit_version_number ([#224](https://github.com/eifinger/hass-weenect/issues/224)) ([`35b4f16`](https://github.com/eifinger/hass-weenect/commit/35b4f1638eb5291c356f24b9be5ecdaba9ccf0c6))

## v2.2.0 (2022-04-03)
### Feature
* Add German translation ([`55f7107`](https://github.com/eifinger/hass-weenect/commit/55f71079e117bb2617d2543ae1e5130421e71696))

### Fix
* Remove title from step_user ([`717bd23`](https://github.com/eifinger/hass-weenect/commit/717bd23b119fa0196ee5acc25b07e7c3ee015926))

## v2.1.2 (2022-02-18)
### Fix
* Use selector for update rate service ([`e983cc8`](https://github.com/eifinger/hass-weenect/commit/e983cc8fdf5d8593f2b5b16fef6d841fea0702aa))

### Documentation
* Update documentation ([`51fe1cf`](https://github.com/eifinger/hass-weenect/commit/51fe1cf8ed60b1f8df23159866cc4917b2e551f1))
* Use main branch in links ([`096f6b3`](https://github.com/eifinger/hass-weenect/commit/096f6b38214e4a250c05685302e5b069c855d325))

## v2.1.1 (2022-02-12)
### Fix
* Handle empty position responses ([`303b8d3`](https://github.com/eifinger/hass-weenect/commit/303b8d3ad7551e4322c4b932148f0c500f2d3720))

## v2.1.0 (2022-01-06)
### Feature
* Add button entities ([`caa9ad6`](https://github.com/eifinger/hass-weenect/commit/caa9ad6db710ac4a82bd464115ed7fc2c9a64350))
* Add select entity for update rate ([`3733d88`](https://github.com/eifinger/hass-weenect/commit/3733d88948b87de11974933d947bfe93aa8d8519))

## v2.0.9 (2022-01-06)
### Fix
* Generate correct unique_ids ([`f67ee48`](https://github.com/eifinger/hass-weenect/commit/f67ee48e581f1168a4ac3f1508ff214209160d06))

## v2.0.8 (2022-01-04)
### Fix
* Add support for HA 2022.2 ([`f0fb2d2`](https://github.com/eifinger/hass-weenect/commit/f0fb2d2c01606d93009d017b807e4aea48d0d138))

## v2.0.7 (2022-01-04)
### Fix
* Use old unique_id for device_tracker ([`054626c`](https://github.com/eifinger/hass-weenect/commit/054626cbab9a61d294bc8254e9c55cd5cb4d1598))

## v2.0.6 (2022-01-04)
### Fix
* Fix Sensor values ([`0e3d810`](https://github.com/eifinger/hass-weenect/commit/0e3d81066519eb4bc300c647144ad7d64e0adab1))

## v2.0.5 (2022-01-02)
### Fix
* Use aioweenect 1.1.1 ([`e69a6a5`](https://github.com/eifinger/hass-weenect/commit/e69a6a59f209fd5e5687fea34ea9e12203f5c42f))
