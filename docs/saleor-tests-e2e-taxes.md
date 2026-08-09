## Purpose

`saleor/tests/e2e/taxes` (`saleor/tests/e2e/taxes`) groups 7 source file(s) exposing 5 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/taxes/utils/query_tax_configurations.py`**

- `get_tax_configurations` (function) — [saleor/tests/e2e/taxes/utils/query_tax_configurations.py:25]

**`saleor/tests/e2e/taxes/utils/tax_class_create.py`**

- `create_tax_class` (function) — [saleor/tests/e2e/taxes/utils/tax_class_create.py:29]

**`saleor/tests/e2e/taxes/utils/tax_class_update.py`**

- `update_tax_class` (function) — [saleor/tests/e2e/taxes/utils/tax_class_update.py:25]

**`saleor/tests/e2e/taxes/utils/tax_configuration_update.py`**

- `update_tax_configuration` (function) — [saleor/tests/e2e/taxes/utils/tax_configuration_update.py:36]

**`saleor/tests/e2e/taxes/utils/tax_country_configuration_update.py`**

- `update_country_tax_rates` (function) — [saleor/tests/e2e/taxes/utils/tax_country_configuration_update.py:36]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/taxes/__init__.py` (1 lines)
- `saleor/tests/e2e/taxes/utils/__init__.py` (13 lines)
- `saleor/tests/e2e/taxes/utils/query_tax_configurations.py` (34 lines)
- `saleor/tests/e2e/taxes/utils/tax_class_create.py` (44 lines)
- `saleor/tests/e2e/taxes/utils/tax_class_update.py` (40 lines)
- `saleor/tests/e2e/taxes/utils/tax_configuration_update.py` (74 lines)
- `saleor/tests/e2e/taxes/utils/tax_country_configuration_update.py` (57 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...utils.get_graphql_content`
- `.query_tax_configurations.get_tax_configurations`
- `.tax_class_create.create_tax_class`
- `.tax_class_update.update_tax_class`
- `.tax_configuration_update.update_tax_configuration`
- `.tax_country_configuration_update.update_country_tax_rates`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `96e84f56fcc3` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
