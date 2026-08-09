## Purpose

`saleor/tests` (`saleor/tests`) groups 13 source file(s) exposing 126 top-level declaration(s).

## Public surface

**`saleor/tests/dummy_password_hasher.py`**

- `DummyHasher` (class) — [saleor/tests/dummy_password_hasher.py:6]
- `encode` (function) — [saleor/tests/dummy_password_hasher.py:15]
- `verify` (function) — [saleor/tests/dummy_password_hasher.py:19]
- `safe_summary` (function) — [saleor/tests/dummy_password_hasher.py:24]
- `harden_runtime` (function) — [saleor/tests/dummy_password_hasher.py:28]

**`saleor/tests/fixtures.py`**

- `CaptureQueriesContext` (class) — [saleor/tests/fixtures.py:45]
- `captured_queries` (function) — [saleor/tests/fixtures.py:49]
- `is_query_ignored` (function) — [saleor/tests/fixtures.py:55]
- `initialize_test_telemetry` (function) — [saleor/tests/fixtures.py:100]
- `trace_context_propagation` (function) — [saleor/tests/fixtures.py:105]
- `get_test_spans` (function) — [saleor/tests/fixtures.py:112]
- `get_test_metrics_data` (function) — [saleor/tests/fixtures.py:121]
- `clear_telemetry_data` (function) — [saleor/tests/fixtures.py:130]
- `capture_queries` (function) — [saleor/tests/fixtures.py:144]
- `assert_num_queries` (function) — [saleor/tests/fixtures.py:158]
- `assert_max_num_queries` (function) — [saleor/tests/fixtures.py:163]
- `address` (function) — [saleor/tests/fixtures.py:168]
- `address_with_areas` (function) — [saleor/tests/fixtures.py:182]
- `address_other_country` (function) — [saleor/tests/fixtures.py:198]
- `address_usa` (function) — [saleor/tests/fixtures.py:211]
- `graphql_address_data` (function) — [saleor/tests/fixtures.py:225]
- `graphql_address_data_skipped_validation` (function) — [saleor/tests/fixtures.py:242]
- `image` (function) — [saleor/tests/fixtures.py:248]
- `icon_image` (function) — [saleor/tests/fixtures.py:256]
- `image_list` (function) — [saleor/tests/fixtures.py:264]
- `dummy_address_data` (function) — [saleor/tests/fixtures.py:279]
- `dummy_webhook_app_payment_data` (function) — [saleor/tests/fixtures.py:298]
- `promotion_events` (function) — [saleor/tests/fixtures.py:304]
- `permission_group_manage_discounts` (function) — [saleor/tests/fixtures.py:353]
- `permission_group_manage_orders` (function) — [saleor/tests/fixtures.py:364]
- `permission_group_manage_shipping` (function) — [saleor/tests/fixtures.py:375]
- `permission_group_manage_users` (function) — [saleor/tests/fixtures.py:386]
- `permission_group_manage_staff` (function) — [saleor/tests/fixtures.py:397]
- `permission_group_manage_apps` (function) — [saleor/tests/fixtures.py:408]
- `permission_group_handle_payments` (function) — [saleor/tests/fixtures.py:419]
- `permission_group_all_perms_all_channels` (function) — [saleor/tests/fixtures.py:430]
- `permission_group_no_perms_all_channels` (function) — [saleor/tests/fixtures.py:445]
- `permission_group_all_perms_channel_USD_only` (function) — [saleor/tests/fixtures.py:455]
- `permission_group_all_perms_without_any_channel` (function) — [saleor/tests/fixtures.py:472]
- `shop_permissions` (function) — [saleor/tests/fixtures.py:485]
- `voucher_translation_fr` (function) — [saleor/tests/fixtures.py:502]
- `product_translation_fr` (function) — [saleor/tests/fixtures.py:509]
- `variant_translation_fr` (function) — [saleor/tests/fixtures.py:519]
- `collection_translation_fr` (function) — [saleor/tests/fixtures.py:526]
- `category_translation_fr` (function) — [saleor/tests/fixtures.py:537]
- _…and 51 more in this file_

**`saleor/tests/migrations/0001_initial.py`**

- `Migration` (class) — [saleor/tests/migrations/0001_initial.py:6]

**`saleor/tests/models.py`**

- `Book` (class) — [saleor/tests/models.py:4]

**`saleor/tests/race_condition.py`**

- `RaceConditionTrigger` (class) — [saleor/tests/race_condition.py:5]
- `wrap` (function) — [saleor/tests/race_condition.py:28]
- `exec_with_callback` (function) — [saleor/tests/race_condition.py:38]
- `RunBefore` (class) — [saleor/tests/race_condition.py:42]
- `exec_with_callback` (function) — [saleor/tests/race_condition.py:43]
- `RunAfter` (class) — [saleor/tests/race_condition.py:48]
- `exec_with_callback` (function) — [saleor/tests/race_condition.py:49]

**`saleor/tests/runner.py`**

- `PytestTestRunner` (class) — [saleor/tests/runner.py:1]
- `run_tests` (function) — [saleor/tests/runner.py:9]

**`saleor/tests/settings.py`**

- `lazy_re_compile` (function) — [saleor/tests/settings.py:9]

**`saleor/tests/storages.py`**

- `PrivateFileSystemStorage` (class) — [saleor/tests/storages.py:5]
- `base_location` (function) — [saleor/tests/storages.py:7]

**`saleor/tests/test_cache_key_warning.py`**

- `test_ignore_cache_key_warning` (function) — [saleor/tests/test_cache_key_warning.py:6]

**`saleor/tests/test_db_connections.py`**

- `test_subqueries_no_allowed_across_different_databases` (function) — [saleor/tests/test_db_connections.py:7]

**`saleor/tests/utils.py`**

- `FakeDbReplicaConnection` (class) — [saleor/tests/utils.py:17]
- `cursor` (function) — [saleor/tests/utils.py:30]
- `chunked_cursor` (function) — [saleor/tests/utils.py:38]
- `prepare_test_db_connections` (function) — [saleor/tests/utils.py:52]
- `dummy_editorjs` (function) — [saleor/tests/utils.py:65]
- `dummy_editorjs` (function) — [saleor/tests/utils.py:67]
- `dummy_editorjs` (function) — [saleor/tests/utils.py:72]
- `round_down` (function) — [saleor/tests/utils.py:83]
- `round_up` (function) — [saleor/tests/utils.py:87]
- `get_metric_data` (function) — [saleor/tests/utils.py:91]
- `get_metric_and_data_point` (function) — [saleor/tests/utils.py:105]
- `get_metric_data_point` (function) — [saleor/tests/utils.py:121]
- `filter_spans_by_name` (function) — [saleor/tests/utils.py:129]
- `get_span_by_name` (function) — [saleor/tests/utils.py:135]

## How it works

The module's files, as provided to this run:

- `saleor/tests/utils.py` (142 lines)
- `saleor/tests/__init__.py` (4 lines)
- `saleor/tests/dummy_password_hasher.py` (29 lines)
- `saleor/tests/fixtures.py` (1708 lines)
- `saleor/tests/migrations/__init__.py` (1 lines)
- `saleor/tests/migrations/0001_initial.py` (27 lines)
- `saleor/tests/models.py` (5 lines)
- `saleor/tests/race_condition.py` (52 lines)
- `saleor/tests/runner.py` (30 lines)
- `saleor/tests/settings.py` (109 lines)
- `saleor/tests/storages.py` (8 lines)
- `saleor/tests/test_cache_key_warning.py` (16 lines)
- `saleor/tests/test_db_connections.py` (16 lines)

## Interactions

- Imports from: `saleor/core/utils`, `saleor/graphql/product/types`, `saleor/core`, `saleor/webhook`, `saleor/csv/utils`, `saleor/core/telemetry`
- Imported by: `(root)`

Internal dependencies named in the source:

- `..account.models.Address`
- `..account.models.Group`
- `..account.models.StaffNotificationRecipient`
- `..app.models.App`
- `..app.models.AppExtension`
- `..core.JobStatus`
- `..core.db.connection.allow_writer`
- `..core.editorjs.models.EditorJSDocumentModel`
- `..core.models.EventDelivery`
- `..core.models.EventDeliveryAttempt`
- `..core.models.EventPayload`
- `..core.payments.PaymentInterface`
- `..core.telemetry.Scope`
- `..core.telemetry.initialize_telemetry`
- `..core.telemetry.meter`
- `..core.telemetry.tracer`
- `..csv.events.ExportEvents`
- `..csv.models.ExportEvent`
- `..csv.models.ExportFile`
- `..discount.PromotionEvents`
- `..payment.interface.AddressData`
- `..permission.enums.get_permissions`
- `..settings.*  # noqa: F403`
- `..tax.TaxCalculationStrategy`
- `..webhook.event_types.WebhookEventAsyncType`
- `..webhook.transport.utils.to_payment_app_id`
- `.utils.dummy_editorjs`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `4d7c2e1d5020` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
