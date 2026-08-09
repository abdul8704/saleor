## Purpose

`saleor/plugins/migrations` (`saleor/plugins/migrations`) groups 12 source file(s) exposing 21 top-level declaration(s).

## Public surface

**`saleor/plugins/migrations/0001_initial.py`**

- `Migration` (class) — [saleor/plugins/migrations/0001_initial.py:9]

**`saleor/plugins/migrations/0002_auto_20200417_0335.py`**

- `get_plugin` (function) — [saleor/plugins/migrations/0002_auto_20200417_0335.py:8]
- `update_identifier_field` (function) — [saleor/plugins/migrations/0002_auto_20200417_0335.py:15]
- `Migration` (class) — [saleor/plugins/migrations/0002_auto_20200417_0335.py:30]

**`saleor/plugins/migrations/0003_auto_20200429_0142.py`**

- `get_plugin` (function) — [saleor/plugins/migrations/0003_auto_20200429_0142.py:9]
- `fill_plugins_name` (function) — [saleor/plugins/migrations/0003_auto_20200429_0142.py:16]
- `Migration` (class) — [saleor/plugins/migrations/0003_auto_20200429_0142.py:31]

**`saleor/plugins/migrations/0004_drop_support_for_env_vatlayer_access_key.py`**

- `deactivate_vatlayer` (function) — [saleor/plugins/migrations/0004_drop_support_for_env_vatlayer_access_key.py:4]
- `Migration` (class) — [saleor/plugins/migrations/0004_drop_support_for_env_vatlayer_access_key.py:16]

**`saleor/plugins/migrations/0005_auto_20200810_1415.py`**

- `Migration` (class) — [saleor/plugins/migrations/0005_auto_20200810_1415.py:8]

**`saleor/plugins/migrations/0006_auto_20200909_1253.py`**

- `Migration` (class) — [saleor/plugins/migrations/0006_auto_20200909_1253.py:6]

**`saleor/plugins/migrations/0007_add_user_emails_configuration.py`**

- `populate_email_config_in_user_email_plugin` (function) — [saleor/plugins/migrations/0007_add_user_emails_configuration.py:9]
- `Migration` (class) — [saleor/plugins/migrations/0007_add_user_emails_configuration.py:52]

**`saleor/plugins/migrations/0008_pluginconfiguration_channel.py`**

- `move_company_address_to_avatax_configuration` (function) — [saleor/plugins/migrations/0008_pluginconfiguration_channel.py:12]
- `populate_plugin_configurations_for_channels` (function) — [saleor/plugins/migrations/0008_pluginconfiguration_channel.py:50]
- `Migration` (class) — [saleor/plugins/migrations/0008_pluginconfiguration_channel.py:68]

**`saleor/plugins/migrations/0009_emailtemplate.py`**

- `Migration` (class) — [saleor/plugins/migrations/0009_emailtemplate.py:7]

**`saleor/plugins/migrations/0010_auto_20220104_1239.py`**

- `move_email_templates_to_separate_model` (function) — [saleor/plugins/migrations/0010_auto_20220104_1239.py:38]
- `revert_changes` (function) — [saleor/plugins/migrations/0010_auto_20220104_1239.py:73]
- `Migration` (class) — [saleor/plugins/migrations/0010_auto_20220104_1239.py:90]

**`saleor/plugins/migrations/0011_alter_pluginconfiguration_configuration.py`**

- `Migration` (class) — [saleor/plugins/migrations/0011_alter_pluginconfiguration_configuration.py:8]

## How it works

The module's files, as provided to this run:

- `saleor/plugins/migrations/__init__.py` (1 lines)
- `saleor/plugins/migrations/0001_initial.py` (42 lines)
- `saleor/plugins/migrations/0002_auto_20200417_0335.py` (53 lines)
- `saleor/plugins/migrations/0003_auto_20200429_0142.py` (44 lines)
- `saleor/plugins/migrations/0004_drop_support_for_env_vatlayer_access_key.py` (23 lines)
- `saleor/plugins/migrations/0005_auto_20200810_1415.py` (24 lines)
- `saleor/plugins/migrations/0006_auto_20200909_1253.py` (17 lines)
- `saleor/plugins/migrations/0007_add_user_emails_configuration.py` (59 lines)
- `saleor/plugins/migrations/0008_pluginconfiguration_channel.py` (96 lines)
- `saleor/plugins/migrations/0009_emailtemplate.py` (37 lines)
- `saleor/plugins/migrations/0010_auto_20220104_1239.py` (100 lines)
- `saleor/plugins/migrations/0011_alter_pluginconfiguration_configuration.py` (23 lines)

## Interactions

- Imports from: `saleor/core/utils`, `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `saleor.core.utils.json_serializer`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8da3c394db1f` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
