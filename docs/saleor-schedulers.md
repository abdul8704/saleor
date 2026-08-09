## Purpose

`saleor/schedulers` (`saleor/schedulers`) groups 6 source file(s) exposing 22 top-level declaration(s).

## Public surface

**`saleor/schedulers/customschedule.py`**

- `CustomSchedule` (class) — [saleor/schedulers/customschedule.py:4]
- `remaining_estimate` (function) — [saleor/schedulers/customschedule.py:18]
- `is_due` (function) — [saleor/schedulers/customschedule.py:21]

**`saleor/schedulers/migrations/0001_initial.py`**

- `delete_django_celery_beat_data` (function) — [saleor/schedulers/migrations/0001_initial.py:8]
- `Migration` (class) — [saleor/schedulers/migrations/0001_initial.py:20]

**`saleor/schedulers/models.py`**

- `CustomSchedule` (class) — [saleor/schedulers/models.py:16]
- `schedule` (function) — [saleor/schedulers/models.py:44]
- `from_schedule` (function) — [saleor/schedulers/models.py:61]
- `PeriodicTaskQuerySet` (class) — [saleor/schedulers/models.py:74]
- `enabled` (function) — [saleor/schedulers/models.py:75]
- `CustomPeriodicTask` (class) — [saleor/schedulers/models.py:84]
- `validate_unique` (function) — [saleor/schedulers/models.py:103]
- `schedule` (function) — [saleor/schedulers/models.py:128]

**`saleor/schedulers/schedulers.py`**

- `setup_celery_logging` (function) — [saleor/schedulers/schedulers.py:20]
- `is_numeric_value` (function) — [saleor/schedulers/schedulers.py:28]
- `HeapEventType` (class) — [saleor/schedulers/schedulers.py:32]
- `CustomModelEntry` (class) — [saleor/schedulers/schedulers.py:38]
- `from_entry` (function) — [saleor/schedulers/schedulers.py:51]
- `BaseScheduler` (class) — [saleor/schedulers/schedulers.py:60]
- `tick` (function) — [saleor/schedulers/schedulers.py:65]
- `PersistentScheduler` (class) — [saleor/schedulers/schedulers.py:148]
- `DatabaseScheduler` (class) — [saleor/schedulers/schedulers.py:157]

## How it works

The module's files, as provided to this run:

- `saleor/schedulers/__init__.py` (1 lines)
- `saleor/schedulers/customschedule.py` (22 lines)
- `saleor/schedulers/migrations/__init__.py` (1 lines)
- `saleor/schedulers/migrations/0001_initial.py` (85 lines)
- `saleor/schedulers/models.py` (142 lines)
- `saleor/schedulers/schedulers.py` (169 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/core/db`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `..customschedule`
- `..models`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `2df66a473a57` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
