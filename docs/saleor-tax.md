## Purpose

`saleor/tax` (`saleor/tax`) groups 4 source file(s) exposing 40 top-level declaration(s).

## Public surface

**`saleor/tax/__init__.py`**

- `TaxCalculationStrategy` (class) — [saleor/tax/__init__.py:1]
- `TaxableObjectDiscountType` (class) — [saleor/tax/__init__.py:8]

**`saleor/tax/error_codes.py`**

- `TaxExemptionManageErrorCode` (class) — [saleor/tax/error_codes.py:4]
- `TaxConfigurationUpdateErrorCode` (class) — [saleor/tax/error_codes.py:11]
- `TaxClassCreateErrorCode` (class) — [saleor/tax/error_codes.py:18]
- `TaxClassUpdateErrorCode` (class) — [saleor/tax/error_codes.py:24]
- `TaxClassDeleteErrorCode` (class) — [saleor/tax/error_codes.py:31]
- `TaxCountryConfigurationUpdateErrorCode` (class) — [saleor/tax/error_codes.py:37]
- `TaxCountryConfigurationDeleteErrorCode` (class) — [saleor/tax/error_codes.py:45]

**`saleor/tax/models.py`**

- `TaxClass` (class) — [saleor/tax/models.py:10]
- `Meta` (class) — [saleor/tax/models.py:13]
- `TaxClassCountryRate` (class) — [saleor/tax/models.py:20]
- `Meta` (class) — [saleor/tax/models.py:30]
- `TaxConfiguration` (class) — [saleor/tax/models.py:51]
- `Meta` (class) — [saleor/tax/models.py:68]
- `TaxConfigurationPerCountry` (class) — [saleor/tax/models.py:72]
- `Meta` (class) — [saleor/tax/models.py:85]

**`saleor/tax/utils.py`**

- `get_display_gross_prices` (function) — [saleor/tax/utils.py:24]
- `get_charge_taxes` (function) — [saleor/tax/utils.py:41]
- `get_tax_calculation_strategy` (function) — [saleor/tax/utils.py:58]
- `should_use_weighted_tax_for_shipping` (function) — [saleor/tax/utils.py:75]
- `get_tax_app_id` (function) — [saleor/tax/utils.py:92]
- `get_charge_taxes_for_order` (function) — [saleor/tax/utils.py:130]
- `get_tax_calculation_strategy_for_order` (function) — [saleor/tax/utils.py:138]
- `get_tax_app_identifier_for_order` (function) — [saleor/tax/utils.py:146]
- `get_tax_configuration_for_checkout` (function) — [saleor/tax/utils.py:154]
- `get_checkout_active_country` (function) — [saleor/tax/utils.py:173]
- `get_charge_taxes_for_checkout` (function) — [saleor/tax/utils.py:190]
- `get_tax_calculation_strategy_for_checkout` (function) — [saleor/tax/utils.py:201]
- `get_tax_app_identifier_for_checkout` (function) — [saleor/tax/utils.py:212]
- `should_use_weighted_tax_for_shipping_for_checkout` (function) — [saleor/tax/utils.py:223]
- `should_use_weighted_tax_for_shipping_for_order` (function) — [saleor/tax/utils.py:236]
- `get_shipping_tax_rate_for_checkout` (function) — [saleor/tax/utils.py:270]
- `get_shipping_tax_rate_for_order` (function) — [saleor/tax/utils.py:302]
- `normalize_tax_rate_for_db` (function) — [saleor/tax/utils.py:338]
- `denormalize_tax_rate_from_db` (function) — [saleor/tax/utils.py:345]
- `calculate_tax_rate` (function) — [saleor/tax/utils.py:350]
- `get_tax_rate_for_country` (function) — [saleor/tax/utils.py:362]
- `get_tax_class_kwargs_for_order_line` (function) — [saleor/tax/utils.py:381]
- `get_shipping_tax_class_kwargs_for_order` (function) — [saleor/tax/utils.py:393]

## How it works

The module's files, as provided to this run:

- `saleor/tax/__init__.py` (12 lines)
- `saleor/tax/models.py` (90 lines)
- `saleor/tax/error_codes.py` (48 lines)
- `saleor/tax/utils.py` (402 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`
- Imported by: `saleor/graphql/tax/tests/queries`, `saleor/tax/tests`, `saleor/tax/migrations`

Internal dependencies named in the source:

- `..TaxCalculationStrategy`
- `..channel.models.Channel`
- `..checkout.fetch.CheckoutInfo`
- `..checkout.fetch.CheckoutLineInfo`
- `..checkout.models.CheckoutLine`
- `..core.models.ModelWithMetadata`
- `..core.utils.country.get_active_country`
- `..order.models.Order`
- `..order.models.OrderLine`
- `..tax.models.TaxClass`
- `..tax.models.TaxClassCountryRate`
- `.models.TaxConfiguration`
- `.models.TaxConfigurationPerCountry`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `800b86d19945` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
