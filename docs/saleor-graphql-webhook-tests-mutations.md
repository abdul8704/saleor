## Purpose

`saleor/graphql/webhook/tests/mutations` (`saleor/graphql/webhook/tests/mutations`) groups 7 source file(s) exposing 75 top-level declaration(s).

## Public surface

**`saleor/graphql/webhook/tests/mutations/test_delivery_retry.py`**

- `test_delivery_retry_mutation` (function) — [saleor/graphql/webhook/tests/mutations/test_delivery_retry.py:25]
- `test_webhook_delivery_retry_without_permission` (function) — [saleor/graphql/webhook/tests/mutations/test_delivery_retry.py:52]
- `test_webhook_delivery_retry_wrong_type` (function) — [saleor/graphql/webhook/tests/mutations/test_delivery_retry.py:62]
- `test_delivery_retry_mutation_wrong_id` (function) — [saleor/graphql/webhook/tests/mutations/test_delivery_retry.py:87]
- `test_delivery_retry_mutation_for_removed_app` (function) — [saleor/graphql/webhook/tests/mutations/test_delivery_retry.py:109]

**`saleor/graphql/webhook/tests/mutations/test_webhook_create.py`**

- `test_webhook_create_by_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:36]
- `test_webhook_create_with_identifier` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:75]
- `test_webhook_create_blank_identifier_stored_as_none` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:103]
- `test_webhook_create_duplicate_identifier_for_same_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:132]
- `test_webhook_create_too_long_identifier` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:172]
- `test_webhook_create_inactive_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:206]
- `test_webhook_create_without_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:226]
- `test_webhook_create_app_doesnt_exist` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:244]
- `test_webhook_create_by_staff` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:261]
- `test_webhook_create_by_staff_with_inactive_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:298]
- `test_webhook_create_by_staff_without_permission` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:319]
- `test_webhook_create_by_app_invalid_query` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:339]
- `test_webhook_create_by_staff_for_removed_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:371]
- `test_webhook_create_inherit_events_from_query` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:418]
- `test_webhook_create_invalid_custom_headers` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:466]
- `test_webhook_create_notify_user_with_another_event` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:494]
- `test_webhook_create_assigns_filterable_channel_slugs` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:546]
- `test_webhook_create_assigns_filterable_channel_slugs_above_max_limit` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_create.py:582]

**`saleor/graphql/webhook/tests/mutations/test_webhook_delete.py`**

- `test_webhook_delete_by_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_delete.py:27]
- `test_webhook_delete_by_staff` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_delete.py:36]
- `test_webhook_delete_by_app_and_webhook_assigned_to_other_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_delete.py:54]
- `test_webhook_delete_by_app_and_missing_webhook` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_delete.py:71]
- `test_webhook_delete_by_inactive_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_delete.py:83]
- `test_webhook_delete_deactivates_before_deletion` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_delete.py:95]
- `test_webhook_delete_raises_integrity_error` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_delete.py:113]
- `test_webhook_delete_when_app_doesnt_exist` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_delete.py:137]
- `test_webhook_delete_by_staff_for_removed_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_delete.py:147]

**`saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py`**

- `test_webhook_dry_run` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:27]
- `test_webhook_dry_run_missing_user_permission` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:51]
- `test_webhook_dry_run_staff_user_not_authorized` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:76]
- `test_webhook_dry_run_non_existing_id` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:97]
- `test_webhook_dry_run_invalid_query` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:122]
- `test_webhook_dry_run_object_id_does_not_match_event` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:148]
- `test_webhook_dry_run_event_type_not_supported` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:173]
- `test_webhook_dry_run_root_type` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:198]
- `test_webhook_dry_run_shop_type` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:239]
- `test_webhook_dry_run_root_type_for_transaction_item_metadata_updated` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:260]
- `test_webhook_dry_run_app_installed_for_removed_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:284]
- `test_webhook_dry_run_app_updated_for_removed_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:310]
- `test_webhook_dry_run_app_deleted_for_removed_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:336]
- `test_webhook_dry_run_app_status_changed_for_removed_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py:362]

**`saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py`**

- `webhook_subscribed_to_draft_delete` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:50]
- `test_webhook_trigger_success` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:64]
- `test_webhook_trigger_type_not_supported` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:114]
- `test_webhook_trigger_fail` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:164]
- `test_webhook_trigger_missing_user_permission` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:200]
- `test_webhook_trigger_staff_user_not_authorized` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:226]
- `test_webhook_trigger_missing_subscription_query` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:248]
- `test_webhook_trigger_invalid_subscription_query` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:277]
- `test_webhook_trigger_synchronous_event_not_supported` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:308]
- `test_webhook_trigger_object_id_does_not_match_event` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:338]
- `test_webhook_trigger_for_removed_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:364]
- `test_webhook_trigger_for_deferred_payload` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py:395]

**`saleor/graphql/webhook/tests/mutations/test_webhook_update.py`**

- `test_webhook_update_by_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:37]
- `test_webhook_update_identifier` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:72]
- `test_webhook_update_blank_identifier_clears_it` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:91]
- `test_webhook_update_duplicate_identifier_for_same_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:110]
- `test_webhook_update_by_other_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:136]
- `test_webhook_update_by_inactive_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:155]
- `test_webhook_update_app_cant_change_webhooks_ownership` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:170]
- `test_webhook_update_by_app_and_missing_webhook` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:191]
- `test_webhook_update_when_app_doesnt_exist` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:206]
- `test_webhook_update_by_staff` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:219]
- `test_webhook_update_by_staff_for_removed_app` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:260]
- `test_webhook_update_by_staff_without_permission` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:291]
- `test_webhook_update_inherit_events_from_query` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:313]
- `test_webhook_update_invalid_custom_headers` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:346]
- `test_webhook_update_notify_user_with_another_event` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:379]
- `test_webhook_update_filterable_channel_slugs` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:435]
- `test_webhook_create_assigns_filterable_channel_slugs_above_max_limit` (function) — [saleor/graphql/webhook/tests/mutations/test_webhook_update.py:472]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/webhook/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/webhook/tests/mutations/test_delivery_retry.py` (129 lines)
- `saleor/graphql/webhook/tests/mutations/test_webhook_create.py` (606 lines)
- `saleor/graphql/webhook/tests/mutations/test_webhook_delete.py` (167 lines)
- `saleor/graphql/webhook/tests/mutations/test_webhook_dry_run.py` (385 lines)
- `saleor/graphql/webhook/tests/mutations/test_webhook_trigger.py` (437 lines)
- `saleor/graphql/webhook/tests/mutations/test_webhook_update.py` (498 lines)

## Interactions

- Imports from: `saleor/graphql/webhook/mutations`, `saleor/webhook/transport/asynchronous`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....app.error_codes.AppErrorCode`
- `.....app.models.App`
- `.....core.EventDeliveryStatus`
- `.....graphql.shop.types.SHOP_ID`
- `.....graphql.tests.utils.assert_no_permission`
- `.....graphql.tests.utils.get_graphql_content`
- `.....webhook.error_codes.WebhookDryRunErrorCode`
- `.....webhook.error_codes.WebhookErrorCode`
- `.....webhook.error_codes.WebhookTriggerErrorCode`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.models.Webhook`
- `.....webhook.transport.asynchronous.transport.generate_deferred_payloads`
- `....core.enums.WebhookErrorCode`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...enums.WebhookEventTypeAsyncEnum`
- `...enums.WebhookEventTypeSyncEnum`
- `...subscription_types.WEBHOOK_TYPES_MAP`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `dd69a07ff911` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
