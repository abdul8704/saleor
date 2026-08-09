## Purpose

`saleor/app/migrations` (`saleor/app/migrations`) groups 46 source file(s) exposing 65 top-level declaration(s).

## Public surface

**`saleor/app/migrations/0001_initial.py`**

- `update_contentypes` (function) — [saleor/app/migrations/0001_initial.py:11]
- `update_contentypes_reverse` (function) — [saleor/app/migrations/0001_initial.py:29]
- `convert_service_account_permissions_to_app_permissions` (function) — [saleor/app/migrations/0001_initial.py:41]
- `Migration` (class) — [saleor/app/migrations/0001_initial.py:52]

**`saleor/app/migrations/0002_auto_20200702_0945.py`**

- `Migration` (class) — [saleor/app/migrations/0002_auto_20200702_0945.py:6]

**`saleor/app/migrations/0003_auto_20200810_1415.py`**

- `Migration` (class) — [saleor/app/migrations/0003_auto_20200810_1415.py:8]

**`saleor/app/migrations/0004_auto_20210308_1135.py`**

- `Migration` (class) — [saleor/app/migrations/0004_auto_20210308_1135.py:7]

**`saleor/app/migrations/0005_appextension.py`**

- `Migration` (class) — [saleor/app/migrations/0005_appextension.py:7]

**`saleor/app/migrations/0006_convert_extension_enums_into_one.py`**

- `migrate_enum_values_to_single_enum` (function) — [saleor/app/migrations/0006_convert_extension_enums_into_one.py:6]
- `Migration` (class) — [saleor/app/migrations/0006_convert_extension_enums_into_one.py:21]

**`saleor/app/migrations/0007_auto_20220127_0942.py`**

- `Migration` (class) — [saleor/app/migrations/0007_auto_20220127_0942.py:6]

**`saleor/app/migrations/0008_appextension_target.py`**

- `Migration` (class) — [saleor/app/migrations/0008_appextension_target.py:6]

**`saleor/app/migrations/0009_apptoken_token_last_4.py`**

- `Migration` (class) — [saleor/app/migrations/0009_apptoken_token_last_4.py:6]

**`saleor/app/migrations/0010_update_app_tokens.py`**

- `update_app_tokens` (function) — [saleor/app/migrations/0010_update_app_tokens.py:9]
- `queryset_in_batches` (function) — [saleor/app/migrations/0010_update_app_tokens.py:21]
- `Migration` (class) — [saleor/app/migrations/0010_update_app_tokens.py:40]

**`saleor/app/migrations/0011_alter_apptoken_token_last_4.py`**

- `Migration` (class) — [saleor/app/migrations/0011_alter_apptoken_token_last_4.py:6]

**`saleor/app/migrations/0012_rename_created_app_created_at.py`**

- `Migration` (class) — [saleor/app/migrations/0012_rename_created_app_created_at.py:6]

**`saleor/app/migrations/0013_alter_appextension_mount.py`**

- `Migration` (class) — [saleor/app/migrations/0013_alter_appextension_mount.py:6]

**`saleor/app/migrations/0014_alter_app_options.py`**

- `assign_permissions` (function) — [saleor/app/migrations/0014_alter_app_options.py:7]
- `on_migrations_complete` (function) — [saleor/app/migrations/0014_alter_app_options.py:8]
- `Migration` (class) — [saleor/app/migrations/0014_alter_app_options.py:35]

**`saleor/app/migrations/0015_app_manifest_url.py`**

- `Migration` (class) — [saleor/app/migrations/0015_app_manifest_url.py:6]

**`saleor/app/migrations/0016_alter_appextension_mount.py`**

- `Migration` (class) — [saleor/app/migrations/0016_alter_appextension_mount.py:6]

**`saleor/app/migrations/0017_app_audience.py`**

- `Migration` (class) — [saleor/app/migrations/0017_app_audience.py:6]

**`saleor/app/migrations/0018_auto_20221122_1148.py`**

- `Migration` (class) — [saleor/app/migrations/0018_auto_20221122_1148.py:49]

**`saleor/app/migrations/0019_fix_constraint_names_in_app_app_permisons.py`**

- `Migration` (class) — [saleor/app/migrations/0019_fix_constraint_names_in_app_app_permisons.py:26]

**`saleor/app/migrations/0020_app_is_installed.py`**

- `Migration` (class) — [saleor/app/migrations/0020_app_is_installed.py:6]

**`saleor/app/migrations/0021_app_author.py`**

- `Migration` (class) — [saleor/app/migrations/0021_app_author.py:6]

**`saleor/app/migrations/0022_auto_20230410_0859.py`**

- `Migration` (class) — [saleor/app/migrations/0022_auto_20230410_0859.py:6]

**`saleor/app/migrations/0023_populate_app_and_app_installation_uuid.py`**

- `queryset_in_batches` (function) — [saleor/app/migrations/0023_populate_app_and_app_installation_uuid.py:9]
- `batch_ids` (function) — [saleor/app/migrations/0023_populate_app_and_app_installation_uuid.py:10]
- `update_uuid_field` (function) — [saleor/app/migrations/0023_populate_app_and_app_installation_uuid.py:19]
- `update_apps_uuid_field_migration` (function) — [saleor/app/migrations/0023_populate_app_and_app_installation_uuid.py:26]
- `Migration` (class) — [saleor/app/migrations/0023_populate_app_and_app_installation_uuid.py:33]

**`saleor/app/migrations/0024_auto_20230412_1343.py`**

- `Migration` (class) — [saleor/app/migrations/0024_auto_20230412_1343.py:8]

**`saleor/app/migrations/0025_auto_20230420_1544.py`**

- `Migration` (class) — [saleor/app/migrations/0025_auto_20230420_1544.py:6]

**`saleor/app/migrations/0026_app_removed_at.py`**

- `Migration` (class) — [saleor/app/migrations/0026_app_removed_at.py:6]

**`saleor/app/migrations/0027_set_identifier_when_missing.py`**

- `set_local_app_identifier_in_transaction_item` (function) — [saleor/app/migrations/0027_set_identifier_when_missing.py:8]
- `set_local_app_identifier_in_transaction_event` (function) — [saleor/app/migrations/0027_set_identifier_when_missing.py:24]
- `set_identifier_for_local_apps` (function) — [saleor/app/migrations/0027_set_identifier_when_missing.py:41]
- `Migration` (class) — [saleor/app/migrations/0027_set_identifier_when_missing.py:55]

**`saleor/app/migrations/0028_set_identifier.py`**

- `set_local_app_identifier_in_transaction_item` (function) — [saleor/app/migrations/0028_set_identifier.py:14]
- `set_local_app_identifier_in_transaction_event` (function) — [saleor/app/migrations/0028_set_identifier.py:33]
- `set_identifier_for_local_apps` (function) — [saleor/app/migrations/0028_set_identifier.py:52]
- `Migration` (class) — [saleor/app/migrations/0028_set_identifier.py:69]

**`saleor/app/migrations/0029_alter_app_identifier.py`**

- `Migration` (class) — [saleor/app/migrations/0029_alter_app_identifier.py:4]

**`saleor/app/migrations/0030_alter_app_metadata_alter_app_private_metadata.py`**

- `Migration` (class) — [saleor/app/migrations/0030_alter_app_metadata_alter_app_private_metadata.py:8]

**`saleor/app/migrations/0031_alter_appextension_mount_alter_appextension_target.py`**

- `Migration` (class) — [saleor/app/migrations/0031_alter_appextension_mount_alter_appextension_target.py:6]

**`saleor/app/migrations/0032_appextension_http_target_method_and_more.py`**

- `Migration` (class) — [saleor/app/migrations/0032_appextension_http_target_method_and_more.py:6]

**`saleor/app/migrations/0033_appextension_settings.py`**

- `Migration` (class) — [saleor/app/migrations/0033_appextension_settings.py:6]

**`saleor/app/migrations/0034_alter_appextension_mount.py`**

- `Migration` (class) — [saleor/app/migrations/0034_alter_appextension_mount.py:6]

**`saleor/app/migrations/0035_app_extensions_mount_target_settings_reshape.py`**

- `fill_app_extension_settings_migration` (function) — [saleor/app/migrations/0035_app_extensions_mount_target_settings_reshape.py:10]
- `on_migrations_complete` (function) — [saleor/app/migrations/0035_app_extensions_mount_target_settings_reshape.py:11]
- `Migration` (class) — [saleor/app/migrations/0035_app_extensions_mount_target_settings_reshape.py:18]

**`saleor/app/migrations/0035_appproblem.py`**

- `Migration` (class) — [saleor/app/migrations/0035_appproblem.py:7]

**`saleor/app/migrations/0036_app_extensions_loosen_target.py`**

- `Migration` (class) — [saleor/app/migrations/0036_app_extensions_loosen_target.py:6]

**`saleor/app/migrations/0037_app_extensions_loosen_mount.py`**

- `Migration` (class) — [saleor/app/migrations/0037_app_extensions_loosen_mount.py:6]

**`saleor/app/migrations/0038_merge_20260213_1154.py`**

- `Migration` (class) — [saleor/app/migrations/0038_merge_20260213_1154.py:6]

**`saleor/app/migrations/0039_appextension_identifier_and_more.py`**

- `Migration` (class) — [saleor/app/migrations/0039_appextension_identifier_and_more.py:6]

**`saleor/app/migrations/0039_remove_manage_apps_permission.py`**

- `remove_manage_apps_permission` (function) — [saleor/app/migrations/0039_remove_manage_apps_permission.py:4]
- `Migration` (class) — [saleor/app/migrations/0039_remove_manage_apps_permission.py:19]

**`saleor/app/migrations/0040_appextension_identifier_unique_constraint.py`**

- `Migration` (class) — [saleor/app/migrations/0040_appextension_identifier_unique_constraint.py:4]

**`saleor/app/migrations/0041_merge_20260714_1040.py`**

- `Migration` (class) — [saleor/app/migrations/0041_merge_20260714_1040.py:6]

**`saleor/app/migrations/tasks/saleor3_23.py`**

- `fill_app_extension_settings_task` (function) — [saleor/app/migrations/tasks/saleor3_23.py:13]

## How it works

The module's files, as provided to this run:

- `saleor/app/migrations/__init__.py` (1 lines)
- `saleor/app/migrations/0001_initial.py` (162 lines)
- `saleor/app/migrations/0002_auto_20200702_0945.py` (110 lines)
- `saleor/app/migrations/0003_auto_20200810_1415.py` (34 lines)
- `saleor/app/migrations/0004_auto_20210308_1135.py` (27 lines)
- `saleor/app/migrations/0005_appextension.py` (67 lines)
- `saleor/app/migrations/0006_convert_extension_enums_into_one.py` (48 lines)
- `saleor/app/migrations/0007_auto_20220127_0942.py` (42 lines)
- `saleor/app/migrations/0008_appextension_target.py` (21 lines)
- `saleor/app/migrations/0009_apptoken_token_last_4.py` (22 lines)
- `saleor/app/migrations/0010_update_app_tokens.py` (47 lines)
- `saleor/app/migrations/0011_alter_apptoken_token_last_4.py` (17 lines)
- `saleor/app/migrations/0012_rename_created_app_created_at.py` (17 lines)
- `saleor/app/migrations/0013_alter_appextension_mount.py` (33 lines)
- `saleor/app/migrations/0014_alter_app_options.py` (52 lines)
- `saleor/app/migrations/0015_app_manifest_url.py` (17 lines)
- `saleor/app/migrations/0016_alter_appextension_mount.py` (39 lines)
- `saleor/app/migrations/0017_app_audience.py` (17 lines)
- `saleor/app/migrations/0018_auto_20221122_1148.py` (101 lines)
- `saleor/app/migrations/0019_fix_constraint_names_in_app_app_permisons.py` (33 lines)
- `saleor/app/migrations/0020_app_is_installed.py` (21 lines)
- `saleor/app/migrations/0021_app_author.py` (17 lines)
- `saleor/app/migrations/0022_auto_20230410_0859.py` (22 lines)
- `saleor/app/migrations/0023_populate_app_and_app_installation_uuid.py` (42 lines)
- `saleor/app/migrations/0024_auto_20230412_1343.py` (24 lines)
- `saleor/app/migrations/0025_auto_20230420_1544.py` (24 lines)
- `saleor/app/migrations/0026_app_removed_at.py` (17 lines)
- `saleor/app/migrations/0027_set_identifier_when_missing.py` (69 lines)
- `saleor/app/migrations/0028_set_identifier.py` (82 lines)
- `saleor/app/migrations/0029_alter_app_identifier.py` (15 lines)
- `saleor/app/migrations/0030_alter_app_metadata_alter_app_private_metadata.py` (34 lines)
- `saleor/app/migrations/0031_alter_appextension_mount_alter_appextension_target.py` (109 lines)
- `saleor/app/migrations/0032_appextension_http_target_method_and_more.py` (124 lines)
- `saleor/app/migrations/0033_appextension_settings.py` (17 lines)
- `saleor/app/migrations/0034_alter_appextension_mount.py` (104 lines)
- `saleor/app/migrations/0035_app_extensions_mount_target_settings_reshape.py` (27 lines)
- `saleor/app/migrations/0035_appproblem.py` (60 lines)
- `saleor/app/migrations/0036_app_extensions_loosen_target.py` (17 lines)
- `saleor/app/migrations/0037_app_extensions_loosen_mount.py` (17 lines)
- `saleor/app/migrations/0038_merge_20260213_1154.py` (12 lines)
- `saleor/app/migrations/0039_appextension_identifier_and_more.py` (24 lines)
- `saleor/app/migrations/0039_remove_manage_apps_permission.py` (26 lines)
- `saleor/app/migrations/0040_appextension_identifier_unique_constraint.py` (49 lines)
- `saleor/app/migrations/0041_merge_20260714_1040.py` (12 lines)
- `saleor/app/migrations/tasks/__init__.py` (1 lines)
- `saleor/app/migrations/tasks/saleor3_23.py` (42 lines)

## Interactions

- Imports from: `saleor/core/utils`, `saleor/core`, `saleor/graphql/core/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....celeryconf.app`
- `....core.db.connection.allow_writer`
- `...models.AppExtension`
- `.tasks.saleor3_23.fill_app_extension_settings_task`
- `saleor.core.utils.json_serializer`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `56d3e1bcdb32` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
