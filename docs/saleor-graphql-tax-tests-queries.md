## Purpose

`saleor/graphql/tax/tests/queries` (`saleor/graphql/tax/tests/queries`) groups 7 source file(s) exposing 24 top-level declaration(s).

## Public surface

**`saleor/graphql/tax/tests/queries/test_tax_class.py`**

- `test_tax_class_query_no_permissions` (function) — [saleor/graphql/tax/tests/queries/test_tax_class.py:30]
- `test_tax_class_query_staff_user` (function) — [saleor/graphql/tax/tests/queries/test_tax_class.py:43]
- `test_tax_class_query_app` (function) — [saleor/graphql/tax/tests/queries/test_tax_class.py:58]
- `test_tax_class_private_metadata_requires_manage_taxes_app` (function) — [saleor/graphql/tax/tests/queries/test_tax_class.py:86]
- `test_tax_class_private_metadata_requires_manage_taxes_staff_user` (function) — [saleor/graphql/tax/tests/queries/test_tax_class.py:108]

**`saleor/graphql/tax/tests/queries/test_tax_classes.py`**

- `test_tax_classes_query_no_permissions` (function) — [saleor/graphql/tax/tests/queries/test_tax_classes.py:25]
- `test_tax_classes_query_staff_user` (function) — [saleor/graphql/tax/tests/queries/test_tax_classes.py:33]
- `test_tax_classes_query_app` (function) — [saleor/graphql/tax/tests/queries/test_tax_classes.py:48]
- `test_tax_classes_filter_by_ids` (function) — [saleor/graphql/tax/tests/queries/test_tax_classes.py:63]
- `test_tax_classes_filter_by_countries` (function) — [saleor/graphql/tax/tests/queries/test_tax_classes.py:79]

**`saleor/graphql/tax/tests/queries/test_tax_configuration.py`**

- `test_tax_configuration_query_no_permissions` (function) — [saleor/graphql/tax/tests/queries/test_tax_configuration.py:48]
- `test_tax_configuration_query_staff_user` (function) — [saleor/graphql/tax/tests/queries/test_tax_configuration.py:62]
- `test_tax_configuration_query_app` (function) — [saleor/graphql/tax/tests/queries/test_tax_configuration.py:79]
- `test_tax_class_private_metadata_requires_manage_taxes_app` (function) — [saleor/graphql/tax/tests/queries/test_tax_configuration.py:109]

**`saleor/graphql/tax/tests/queries/test_tax_configurations.py`**

- `test_tax_configurations_query_no_permissions` (function) — [saleor/graphql/tax/tests/queries/test_tax_configurations.py:24]
- `test_tax_configurations_query_staff_user` (function) — [saleor/graphql/tax/tests/queries/test_tax_configurations.py:32]
- `test_tax_configurations_query_app` (function) — [saleor/graphql/tax/tests/queries/test_tax_configurations.py:47]
- `test_tax_configurations_filter` (function) — [saleor/graphql/tax/tests/queries/test_tax_configurations.py:62]

**`saleor/graphql/tax/tests/queries/test_tax_country_configuration.py`**

- `test_tax_country_configuration_query_no_permissions` (function) — [saleor/graphql/tax/tests/queries/test_tax_country_configuration.py:44]
- `test_tax_country_configuration_query_staff_user` (function) — [saleor/graphql/tax/tests/queries/test_tax_country_configuration.py:57]
- `test_tax_country_configuration_query_app` (function) — [saleor/graphql/tax/tests/queries/test_tax_country_configuration.py:72]

**`saleor/graphql/tax/tests/queries/test_tax_country_configurations.py`**

- `test_tax_country_configurations_query_no_permissions` (function) — [saleor/graphql/tax/tests/queries/test_tax_country_configurations.py:23]
- `test_tax_country_configurations_query_staff_user` (function) — [saleor/graphql/tax/tests/queries/test_tax_country_configurations.py:31]
- `test_tax_country_configurations_query_app` (function) — [saleor/graphql/tax/tests/queries/test_tax_country_configurations.py:40]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/tax/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/tax/tests/queries/test_tax_class.py` (127 lines)
- `saleor/graphql/tax/tests/queries/test_tax_classes.py` (89 lines)
- `saleor/graphql/tax/tests/queries/test_tax_configuration.py` (131 lines)
- `saleor/graphql/tax/tests/queries/test_tax_configurations.py` (76 lines)
- `saleor/graphql/tax/tests/queries/test_tax_country_configuration.py` (84 lines)
- `saleor/graphql/tax/tests/queries/test_tax_country_configurations.py` (46 lines)

## Interactions

- Imports from: `saleor/tax`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....tax.models.TaxClass`
- `.....tax.models.TaxConfiguration`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `..fragments.TAX_CLASS_FRAGMENT`
- `..fragments.TAX_CONFIGURATION_FRAGMENT`
- `..fragments.TAX_COUNTRY_CONFIGURATION_FRAGMENT`
- `saleor.tax.models.TaxClassCountryRate`
- `saleor.tax.models.TaxConfiguration`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `03d53b973f84` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
