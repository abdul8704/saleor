## Purpose

`saleor/account/management` (`saleor/account/management`) groups 4 source file(s) exposing 6 top-level declaration(s).

## Public surface

**`saleor/account/management/commands/createsuperuser.py`**

- `NotRunningInTTYException` (class) — [saleor/account/management/commands/createsuperuser.py:21]
- `Command` (class) — [saleor/account/management/commands/createsuperuser.py:28]
- `add_arguments` (function) — [saleor/account/management/commands/createsuperuser.py:37]
- `execute` (function) — [saleor/account/management/commands/createsuperuser.py:85]
- `handle` (function) — [saleor/account/management/commands/createsuperuser.py:89]
- `get_input_data` (function) — [saleor/account/management/commands/createsuperuser.py:244]

## How it works

The module's files, as provided to this run:

- `saleor/account/management/__init__.py` (1 lines)
- `saleor/account/management/commands/__init__.py` (1 lines)
- `saleor/account/management/commands/changepassword.py` (3 lines)
- `saleor/account/management/commands/createsuperuser.py` (284 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/core/utils`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...models.User`
- `...tests.fixtures.user.dangerously_get_or_create_superuser`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `2d4119baf760` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
