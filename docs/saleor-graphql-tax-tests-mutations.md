## Purpose

`saleor/graphql/tax/tests/mutations` (`saleor/graphql/tax/tests/mutations`) groups 8 source file(s) exposing 58 top-level declaration(s).

## Public surface

**`saleor/graphql/tax/tests/mutations/test_tax_class_create.py`**

- `test_no_permission_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_create.py:35]
- `test_no_permission_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_create.py:39]
- `test_create_as_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_create.py:72]
- `test_create_as_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_create.py:76]

**`saleor/graphql/tax/tests/mutations/test_tax_class_delete.py`**

- `test_no_permission_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_delete.py:38]
- `test_no_permission_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_delete.py:42]
- `test_delete_as_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_delete.py:64]
- `test_delete_as_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_delete.py:68]

**`saleor/graphql/tax/tests/mutations/test_tax_class_update.py`**

- `test_no_permission_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_update.py:41]
- `test_no_permission_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_update.py:45]
- `test_create_as_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_update.py:90]
- `test_create_as_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_update.py:94]
- `test_raise_duplicated_item_error` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_update.py:98]
- `test_remove_all_country_rates` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_update.py:124]
- `test_remove_individual_country_rates` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_update.py:146]
- `test_remove_individual_country_rates_non_existing_rate` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_update.py:183]
- `test_tax_class_update_zero_rate` (function) — [saleor/graphql/tax/tests/mutations/test_tax_class_update.py:220]

**`saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py`**

- `test_no_permission_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:50]
- `test_no_permission_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:54]
- `example_tax_configuration` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:59]
- `test_update_as_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:122]
- `test_update_as_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:130]
- `test_raise_duplicate_input_item` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:138]
- `test_create_and_update_country_configurations` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:167]
- `test_create_and_update_country_configurations_no_tax_calculation_strategy` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:222]
- `test_remove_country_configurations` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:278]
- `test_tax_configuration_update_tax_app_id` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:300]
- `test_tax_configuration_update_tax_app_id_with_no_tax_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:339]
- `test_tax_configuration_update_tax_app_id_with_non_existent_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:374]
- `test_tax_configuration_update_tax_app_id_with_plugin` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:400]
- `test_tax_configuration_update_use_weighted_tax_for_shipping` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:426]
- `test_tax_configuration_update_turn_off_use_weighted_tax_for_shipping` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:459]
- `test_tax_configuration_update_use_weighted_tax_for_shipping_with_tax_app_included_in_input` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:495]
- `test_tax_configuration_update_use_weighted_tax_for_shipping_with_tax_app_already_set` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:525]
- `test_tax_configuration_per_country_update_use_weighted_tax_for_shipping` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:559]
- `test_tax_configuration_per_country_update_turn_off_weighted_tax_for_shipping` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:603]
- `test_tax_configuration_per_country_update_use_weighted_tax_for_shipping_with_tax_app_included_in_input` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:656]
- `test_tax_configuration_per_country_update_use_weighted_tax_for_shipping_with_tax_app_already_set` (function) — [saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py:695]

**`saleor/graphql/tax/tests/mutations/test_tax_country_configuration_delete.py`**

- `test_no_permission_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_delete.py:37]
- `test_no_permission_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_delete.py:41]
- `test_delete_tax_rates_for_country_by_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_delete.py:65]
- `test_delete_tax_rates_for_country_by_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_delete.py:71]

**`saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py`**

- `test_no_permission_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py:50]
- `test_no_permission_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py:54]
- `test_update_rates_as_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py:93]
- `test_update_rates_as_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py:97]
- `test_create_country_rate_ignore_input_item_when_rate_is_none` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py:101]
- `test_delete_country_rate` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py:139]
- `test_tax_class_id_not_found` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py:163]
- `test_update_default_country_rate` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py:191]
- `test_delete_default_country_rate` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py:216]
- `test_update_default_country_rate_throws_error_with_multiple_rates` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py:236]
- `test_validate_negative_rates` (function) — [saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py:256]

**`saleor/graphql/tax/tests/mutations/test_tax_exemption_manage.py`**

- `test_tax_exemption_manage_for_checkout_as_staff` (function) — [saleor/graphql/tax/tests/mutations/test_tax_exemption_manage.py:33]
- `test_tax_exemption_manage_for_checkout_as_app` (function) — [saleor/graphql/tax/tests/mutations/test_tax_exemption_manage.py:55]
- `test_tax_exemption_manage_for_order` (function) — [saleor/graphql/tax/tests/mutations/test_tax_exemption_manage.py:76]
- `test_tax_exemption_manage_return_error_when_invalid_object_id` (function) — [saleor/graphql/tax/tests/mutations/test_tax_exemption_manage.py:98]
- `test_tax_exemption_manage_return_error_when_invalid_order_status` (function) — [saleor/graphql/tax/tests/mutations/test_tax_exemption_manage.py:118]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/tax/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/tax/tests/mutations/test_tax_class_create.py` (77 lines)
- `saleor/graphql/tax/tests/mutations/test_tax_class_delete.py` (69 lines)
- `saleor/graphql/tax/tests/mutations/test_tax_class_update.py` (249 lines)
- `saleor/graphql/tax/tests/mutations/test_tax_configuration_update.py` (736 lines)
- `saleor/graphql/tax/tests/mutations/test_tax_country_configuration_delete.py` (72 lines)
- `saleor/graphql/tax/tests/mutations/test_tax_country_configuration_update.py` (284 lines)
- `saleor/graphql/tax/tests/mutations/test_tax_exemption_manage.py` (140 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....core.tests.test_taxes.app_factory`
- `.....core.tests.test_taxes.tax_app_factory  # noqa: F401`
- `.....order.OrderStatus`
- `.....plugins.PLUGIN_IDENTIFIER_PREFIX`
- `.....plugins.tests.sample_plugins.PluginSample`
- `.....tax.error_codes.TaxClassUpdateErrorCode`
- `.....tax.error_codes.TaxConfigurationUpdateErrorCode`
- `.....tax.error_codes.TaxCountryConfigurationUpdateErrorCode`
- `.....tax.error_codes.TaxExemptionManageErrorCode`
- `.....tax.models.TaxClass`
- `.....tax.models.TaxClassCountryRate`
- `.....tax.models.TaxConfiguration`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...enums.TaxCalculationStrategy`
- `..fragments.TAX_CLASS_FRAGMENT`
- `..fragments.TAX_CONFIGURATION_FRAGMENT`
- `..fragments.TAX_COUNTRY_CONFIGURATION_FRAGMENT`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `9ac877dbeaad` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
