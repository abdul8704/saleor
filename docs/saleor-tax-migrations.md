## Purpose

`saleor/tax/migrations` (`saleor/tax/migrations`) groups 14 source file(s) exposing 24 top-level declaration(s).

## Public surface

**`saleor/tax/migrations/0001_initial.py`**

- `Migration` (class) — [saleor/tax/migrations/0001_initial.py:11]

**`saleor/tax/migrations/0002_add_default_tax_configs.py`**

- `add_tax_configuration_for_channels` (function) — [saleor/tax/migrations/0002_add_default_tax_configs.py:14]
- `populate_tax_calculation_strategy` (function) — [saleor/tax/migrations/0002_add_default_tax_configs.py:43]
- `Migration` (class) — [saleor/tax/migrations/0002_add_default_tax_configs.py:108]

**`saleor/tax/migrations/0003_add_manage_taxes_permission.py`**

- `assign_permissions` (function) — [saleor/tax/migrations/0003_add_manage_taxes_permission.py:8]
- `on_migrations_complete` (function) — [saleor/tax/migrations/0003_add_manage_taxes_permission.py:9]
- `Migration` (class) — [saleor/tax/migrations/0003_add_manage_taxes_permission.py:39]

**`saleor/tax/migrations/0004_migrate_tax_classes.py`**

- `queryset_in_batches` (function) — [saleor/tax/migrations/0004_migrate_tax_classes.py:23]
- `migrate_product_tax_codes` (function) — [saleor/tax/migrations/0004_migrate_tax_classes.py:59]
- `migrate_products_with_disabled_taxes` (function) — [saleor/tax/migrations/0004_migrate_tax_classes.py:114]
- `Migration` (class) — [saleor/tax/migrations/0004_migrate_tax_classes.py:147]

**`saleor/tax/migrations/0005_migrate_vatlayer.py`**

- `create_tax_configurations` (function) — [saleor/tax/migrations/0005_migrate_vatlayer.py:23]
- `create_tax_rates` (function) — [saleor/tax/migrations/0005_migrate_vatlayer.py:62]
- `migrate_vatlayer` (function) — [saleor/tax/migrations/0005_migrate_vatlayer.py:109]
- `Migration` (class) — [saleor/tax/migrations/0005_migrate_vatlayer.py:122]

**`saleor/tax/migrations/0006_alter_taxconfiguration_tax_calculation_strategy.py`**

- `Migration` (class) — [saleor/tax/migrations/0006_alter_taxconfiguration_tax_calculation_strategy.py:6]

**`saleor/tax/migrations/0007_auto_20230217_0837.py`**

- `set_flat_rates_as_default_strategy` (function) — [saleor/tax/migrations/0007_auto_20230217_0837.py:8]
- `Migration` (class) — [saleor/tax/migrations/0007_auto_20230217_0837.py:15]

**`saleor/tax/migrations/0008_auto_20240122_1353.py`**

- `Migration` (class) — [saleor/tax/migrations/0008_auto_20240122_1353.py:6]

**`saleor/tax/migrations/0009_alter_taxclass_metadata_and_more.py`**

- `Migration` (class) — [saleor/tax/migrations/0009_alter_taxclass_metadata_and_more.py:8]

**`saleor/tax/migrations/0009_alter_taxclasscountryrate_rate.py`**

- `Migration` (class) — [saleor/tax/migrations/0009_alter_taxclasscountryrate_rate.py:6]

**`saleor/tax/migrations/0010_merge_20250527_1210.py`**

- `Migration` (class) — [saleor/tax/migrations/0010_merge_20250527_1210.py:6]

**`saleor/tax/migrations/0010_taxconfiguration_use_weighted_tax_for_shipping_and_more.py`**

- `Migration` (class) — [saleor/tax/migrations/0010_taxconfiguration_use_weighted_tax_for_shipping_and_more.py:6]

**`saleor/tax/migrations/0011_merge_20250530_0929.py`**

- `Migration` (class) — [saleor/tax/migrations/0011_merge_20250530_0929.py:6]

## How it works

The module's files, as provided to this run:

- `saleor/tax/migrations/__init__.py` (1 lines)
- `saleor/tax/migrations/0001_initial.py` (196 lines)
- `saleor/tax/migrations/0002_add_default_tax_configs.py` (127 lines)
- `saleor/tax/migrations/0003_add_manage_taxes_permission.py` (46 lines)
- `saleor/tax/migrations/0004_migrate_tax_classes.py` (158 lines)
- `saleor/tax/migrations/0005_migrate_vatlayer.py` (127 lines)
- `saleor/tax/migrations/0006_alter_taxconfiguration_tax_calculation_strategy.py` (23 lines)
- `saleor/tax/migrations/0007_auto_20230217_0837.py` (24 lines)
- `saleor/tax/migrations/0008_auto_20240122_1353.py` (22 lines)
- `saleor/tax/migrations/0009_alter_taxclass_metadata_and_more.py` (54 lines)
- `saleor/tax/migrations/0009_alter_taxclasscountryrate_rate.py` (17 lines)
- `saleor/tax/migrations/0010_merge_20250527_1210.py` (12 lines)
- `saleor/tax/migrations/0010_taxconfiguration_use_weighted_tax_for_shipping_and_more.py` (38 lines)
- `saleor/tax/migrations/0011_merge_20250530_0929.py` (12 lines)

## Interactions

- Imports from: `saleor/core/utils`, `saleor/tax`, `saleor/core/db`, `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...TaxCalculationStrategy`
- `saleor.core.utils.json_serializer`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c857d9717515` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
