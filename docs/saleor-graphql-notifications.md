## Purpose

`saleor/graphql/notifications` (`saleor/graphql/notifications`) groups 9 source file(s) exposing 12 top-level declaration(s).

## Public surface

**`saleor/graphql/notifications/error_codes.py`**

- `ExternalNotificationErrorCodes` (class) — [saleor/graphql/notifications/error_codes.py:4]

**`saleor/graphql/notifications/mutations/external_notification_trigger.py`**

- `ExternalNotificationTriggerInput` (class) — [saleor/graphql/notifications/mutations/external_notification_trigger.py:22]
- `ExternalNotificationTrigger` (class) — [saleor/graphql/notifications/mutations/external_notification_trigger.py:45]
- `Arguments` (class) — [saleor/graphql/notifications/mutations/external_notification_trigger.py:46]
- `Meta` (class) — [saleor/graphql/notifications/mutations/external_notification_trigger.py:60]
- `perform_mutation` (function) — [saleor/graphql/notifications/mutations/external_notification_trigger.py:69]

**`saleor/graphql/notifications/schema.py`**

- `ExternalNotificationMutations` (class) — [saleor/graphql/notifications/schema.py:7]

**`saleor/graphql/notifications/tests/conftest.py`**

- `external_notification_trigger_query` (function) — [saleor/graphql/notifications/tests/conftest.py:5]

**`saleor/graphql/notifications/tests/test_external_notification_dispatch.py`**

- `test_notify_via_external_notification_trigger` (function) — [saleor/graphql/notifications/tests/test_external_notification_dispatch.py:9]

**`saleor/graphql/notifications/tests/test_external_notification_query.py`**

- `test_external_notification_trigger_query_with_invalid_data` (function) — [saleor/graphql/notifications/tests/test_external_notification_query.py:55]
- `test_notify_via_external_notification_trigger_for_plugin_manager` (function) — [saleor/graphql/notifications/tests/test_external_notification_query.py:78]
- `test_notify_via_external_notification_trigger_without_permission` (function) — [saleor/graphql/notifications/tests/test_external_notification_query.py:110]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/notifications/__init__.py` (1 lines)
- `saleor/graphql/notifications/error_codes.py` (8 lines)
- `saleor/graphql/notifications/mutations/__init__.py` (1 lines)
- `saleor/graphql/notifications/mutations/external_notification_trigger.py` (98 lines)
- `saleor/graphql/notifications/schema.py` (10 lines)
- `saleor/graphql/notifications/tests/__init__.py` (1 lines)
- `saleor/graphql/notifications/tests/conftest.py` (22 lines)
- `saleor/graphql/notifications/tests/test_external_notification_dispatch.py` (40 lines)
- `saleor/graphql/notifications/tests/test_external_notification_query.py` (131 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.models.User`
- `....core.exceptions.PermissionDenied`
- `....core.notify.UserNotifyEvent`
- `....graphql.tests.utils.assert_no_permission`
- `....plugins.tests.sample_plugins.PluginSample`
- `...core.ResolveInfo`
- `...core.fields.JSONString`
- `...core.mutations.BaseMutation`
- `...core.types.ExternalNotificationError`
- `...core.types.NonNullList`
- `...notifications.error_codes.ExternalNotificationErrorCodes`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `..core.descriptions.DEFAULT_DEPRECATION_REASON`
- `.mutations.external_notification_trigger.ExternalNotificationTrigger`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `cbce33e3f2aa` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
