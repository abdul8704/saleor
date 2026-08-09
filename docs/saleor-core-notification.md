## Purpose

`saleor/core/notification` (`saleor/core/notification`) groups 4 source file(s) exposing 8 top-level declaration(s).

## Public surface

**`saleor/core/notification/mutation_handler.py`**

- `get_external_notification_payload` (function) — [saleor/core/notification/mutation_handler.py:1]
- `send_notification` (function) — [saleor/core/notification/mutation_handler.py:8]
- `trigger_notifications` (function) — [saleor/core/notification/mutation_handler.py:24]

**`saleor/core/notification/utils.py`**

- `get_site_context` (function) — [saleor/core/notification/utils.py:9]

**`saleor/core/notification/validation.py`**

- `validate_ids_and_get_model_type_and_pks` (function) — [saleor/core/notification/validation.py:26]
- `validate_and_get_external_event_type` (function) — [saleor/core/notification/validation.py:40]
- `validate_and_get_channel` (function) — [saleor/core/notification/validation.py:53]
- `validate_and_get_payload_params` (function) — [saleor/core/notification/validation.py:66]

## How it works

The module's files, as provided to this run:

- `saleor/core/notification/__init__.py` (1 lines)
- `saleor/core/notification/mutation_handler.py` (35 lines)
- `saleor/core/notification/utils.py` (16 lines)
- `saleor/core/notification/validation.py` (79 lines)

## Interactions

- Imports from: `saleor/webhook`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...account.models.User`
- `...account.notifications.get_user_custom_payload`
- `...graphql.channel.utils.validate_channel`
- `...graphql.core.enums.ExternalNotificationTriggerErrorCode`
- `...graphql.utils.resolve_global_ids_to_primary_keys`
- `...order.models.Order`
- `...order.notifications.get_custom_order_payload`
- `...permission.enums.AccountPermissions`
- `...permission.enums.OrderPermissions`
- `..utils.build_absolute_uri`
- `..utils.get_domain`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `dad30d8309ac` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
