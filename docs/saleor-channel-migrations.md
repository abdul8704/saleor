## Purpose

`saleor/channel/migrations` (`saleor/channel/migrations`) groups 33 source file(s) exposing 43 top-level declaration(s).

## Public surface

**`saleor/channel/migrations/0001_initial.py`**

- `assign_permissions` (function) — [saleor/channel/migrations/0001_initial.py:11]
- `on_migrations_complete` (function) — [saleor/channel/migrations/0001_initial.py:12]
- `get_default_currency` (function) — [saleor/channel/migrations/0001_initial.py:36]
- `create_default_channel` (function) — [saleor/channel/migrations/0001_initial.py:55]
- `Migration` (class) — [saleor/channel/migrations/0001_initial.py:77]

**`saleor/channel/migrations/0002_channel_default_country.py`**

- `Migration` (class) — [saleor/channel/migrations/0002_channel_default_country.py:7]

**`saleor/channel/migrations/0003_alter_channel_default_country.py`**

- `set_default_country_for_channels` (function) — [saleor/channel/migrations/0003_alter_channel_default_country.py:8]
- `Migration` (class) — [saleor/channel/migrations/0003_alter_channel_default_country.py:27]

**`saleor/channel/migrations/0004_create_default_channel.py`**

- `create_default_channel` (function) — [saleor/channel/migrations/0004_create_default_channel.py:5]
- `Migration` (class) — [saleor/channel/migrations/0004_create_default_channel.py:17]

**`saleor/channel/migrations/0005_channel_allocation_strategy.py`**

- `Migration` (class) — [saleor/channel/migrations/0005_channel_allocation_strategy.py:6]

**`saleor/channel/migrations/0006_order_settings_fields.py`**

- `Migration` (class) — [saleor/channel/migrations/0006_order_settings_fields.py:6]

**`saleor/channel/migrations/0007_order_settings_per_channel.py`**

- `set_order_settings` (function) — [saleor/channel/migrations/0007_order_settings_per_channel.py:4]
- `Migration` (class) — [saleor/channel/migrations/0007_order_settings_per_channel.py:25]

**`saleor/channel/migrations/0008_update_null_order_settings.py`**

- `set_order_settings` (function) — [saleor/channel/migrations/0008_update_null_order_settings.py:11]
- `Migration` (class) — [saleor/channel/migrations/0008_update_null_order_settings.py:35]

**`saleor/channel/migrations/0009_channel_order_mark_as_paid_strategy.py`**

- `Migration` (class) — [saleor/channel/migrations/0009_channel_order_mark_as_paid_strategy.py:6]

**`saleor/channel/migrations/0010_channel_default_transaction_flow_strategy.py`**

- `Migration` (class) — [saleor/channel/migrations/0010_channel_default_transaction_flow_strategy.py:6]

**`saleor/channel/migrations/0011_channel_expire_orders_after.py`**

- `Migration` (class) — [saleor/channel/migrations/0011_channel_expire_orders_after.py:4]

**`saleor/channel/migrations/0012_channel_delete_expired_orders_after.py`**

- `Migration` (class) — [saleor/channel/migrations/0012_channel_delete_expired_orders_after.py:8]

**`saleor/channel/migrations/0013_auto_20230630_1039.py`**

- `Migration` (class) — [saleor/channel/migrations/0013_auto_20230630_1039.py:8]

**`saleor/channel/migrations/0014_channel_allow_to_create_order_without_payment.py`**

- `Migration` (class) — [saleor/channel/migrations/0014_channel_allow_to_create_order_without_payment.py:4]

**`saleor/channel/migrations/0015_channel_use_legacy_error_flow_for_checkout.py`**

- `Migration` (class) — [saleor/channel/migrations/0015_channel_use_legacy_error_flow_for_checkout.py:6]

**`saleor/channel/migrations/0016_auto_20230816_1209.py`**

- `Migration` (class) — [saleor/channel/migrations/0016_auto_20230816_1209.py:8]

**`saleor/channel/migrations/0017_channel_include_draft_order_in_voucher_usage.py`**

- `Migration` (class) — [saleor/channel/migrations/0017_channel_include_draft_order_in_voucher_usage.py:6]

**`saleor/channel/migrations/0018_channel_automatically_complete_paid_checkouts.py`**

- `Migration` (class) — [saleor/channel/migrations/0018_channel_automatically_complete_paid_checkouts.py:6]

**`saleor/channel/migrations/0019_auto_20250625_1048.py`**

- `Migration` (class) — [saleor/channel/migrations/0019_auto_20250625_1048.py:8]

**`saleor/channel/migrations/0019_channel_draft_order_line_price_freeze_period.py`**

- `Migration` (class) — [saleor/channel/migrations/0019_channel_draft_order_line_price_freeze_period.py:6]

**`saleor/channel/migrations/0020_alter_channel_metadata_and_more.py`**

- `Migration` (class) — [saleor/channel/migrations/0020_alter_channel_metadata_and_more.py:8]

**`saleor/channel/migrations/0020_channel_use_legacy_line_voucher_propagation_for_order.py`**

- `Migration` (class) — [saleor/channel/migrations/0020_channel_use_legacy_line_voucher_propagation_for_order.py:6]

**`saleor/channel/migrations/0020_migrate_checkout_ttl_release_funds.py`**

- `queryset_in_batches` (function) — [saleor/channel/migrations/0020_migrate_checkout_ttl_release_funds.py:10]
- `migrate_env_variable_setting_to_channels` (function) — [saleor/channel/migrations/0020_migrate_checkout_ttl_release_funds.py:29]
- `Migration` (class) — [saleor/channel/migrations/0020_migrate_checkout_ttl_release_funds.py:51]

**`saleor/channel/migrations/0021_merge_20250423_1021.py`**

- `Migration` (class) — [saleor/channel/migrations/0021_merge_20250423_1021.py:6]

**`saleor/channel/migrations/0021_rename_use_legacy_line_voucher_propagation_for_order_channel_use_legacy_line_discount_propagation_fo.py`**

- `Migration` (class) — [saleor/channel/migrations/0021_rename_use_legacy_line_voucher_propagation_for_order_channel_use_legacy_line_discount_propagation_fo.py:6]

**`saleor/channel/migrations/0022_merge_20250527_1210.py`**

- `Migration` (class) — [saleor/channel/migrations/0022_merge_20250527_1210.py:6]

**`saleor/channel/migrations/0022_merge_20250708_1220.py`**

- `Migration` (class) — [saleor/channel/migrations/0022_merge_20250708_1220.py:6]

**`saleor/channel/migrations/0023_merge_20250709_1453.py`**

- `Migration` (class) — [saleor/channel/migrations/0023_merge_20250709_1453.py:6]

**`saleor/channel/migrations/0024_channel_automatic_completion_delay.py`**

- `Migration` (class) — [saleor/channel/migrations/0024_channel_automatic_completion_delay.py:6]

**`saleor/channel/migrations/0025_set_automatic_completion_delay.py`**

- `set_automatic_completion_delay` (function) — [saleor/channel/migrations/0025_set_automatic_completion_delay.py:6]
- `Migration` (class) — [saleor/channel/migrations/0025_set_automatic_completion_delay.py:13]

**`saleor/channel/migrations/0026_channel_automatic_completion_cut_off_date.py`**

- `Migration` (class) — [saleor/channel/migrations/0026_channel_automatic_completion_cut_off_date.py:6]

**`saleor/channel/migrations/0027_channel_allow_legacy_gift_card_use.py`**

- `Migration` (class) — [saleor/channel/migrations/0027_channel_allow_legacy_gift_card_use.py:6]

## How it works

The module's files, as provided to this run:

- `saleor/channel/migrations/__init__.py` (1 lines)
- `saleor/channel/migrations/0001_initial.py` (116 lines)
- `saleor/channel/migrations/0002_channel_default_country.py` (18 lines)
- `saleor/channel/migrations/0003_alter_channel_default_country.py` (42 lines)
- `saleor/channel/migrations/0004_create_default_channel.py` (23 lines)
- `saleor/channel/migrations/0005_channel_allocation_strategy.py` (37 lines)
- `saleor/channel/migrations/0006_order_settings_fields.py` (22 lines)
- `saleor/channel/migrations/0007_order_settings_per_channel.py` (33 lines)
- `saleor/channel/migrations/0008_update_null_order_settings.py` (42 lines)
- `saleor/channel/migrations/0009_channel_order_mark_as_paid_strategy.py` (32 lines)
- `saleor/channel/migrations/0010_channel_default_transaction_flow_strategy.py` (29 lines)
- `saleor/channel/migrations/0011_channel_expire_orders_after.py` (15 lines)
- `saleor/channel/migrations/0012_channel_delete_expired_orders_after.py` (27 lines)
- `saleor/channel/migrations/0013_auto_20230630_1039.py` (34 lines)
- `saleor/channel/migrations/0014_channel_allow_to_create_order_without_payment.py` (23 lines)
- `saleor/channel/migrations/0015_channel_use_legacy_error_flow_for_checkout.py` (25 lines)
- `saleor/channel/migrations/0016_auto_20230816_1209.py` (28 lines)
- `saleor/channel/migrations/0017_channel_include_draft_order_in_voucher_usage.py` (25 lines)
- `saleor/channel/migrations/0018_channel_automatically_complete_paid_checkouts.py` (25 lines)
- `saleor/channel/migrations/0019_auto_20250625_1048.py` (41 lines)
- `saleor/channel/migrations/0019_channel_draft_order_line_price_freeze_period.py` (25 lines)
- `saleor/channel/migrations/0020_alter_channel_metadata_and_more.py` (34 lines)
- `saleor/channel/migrations/0020_channel_use_legacy_line_voucher_propagation_for_order.py` (25 lines)
- `saleor/channel/migrations/0020_migrate_checkout_ttl_release_funds.py` (61 lines)
- `saleor/channel/migrations/0021_merge_20250423_1021.py` (12 lines)
- `saleor/channel/migrations/0021_rename_use_legacy_line_voucher_propagation_for_order_channel_use_legacy_line_discount_propagation_fo.py` (17 lines)
- `saleor/channel/migrations/0022_merge_20250527_1210.py` (15 lines)
- `saleor/channel/migrations/0022_merge_20250708_1220.py` (15 lines)
- `saleor/channel/migrations/0023_merge_20250709_1453.py` (12 lines)
- `saleor/channel/migrations/0024_channel_automatic_completion_delay.py` (17 lines)
- `saleor/channel/migrations/0025_set_automatic_completion_delay.py` (23 lines)
- `saleor/channel/migrations/0026_channel_automatic_completion_cut_off_date.py` (17 lines)
- `saleor/channel/migrations/0027_channel_allow_legacy_gift_card_use.py` (17 lines)

## Interactions

- Imports from: `saleor/core/utils`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `saleor.core.utils.json_serializer`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7f5a5a62719d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
