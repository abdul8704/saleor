## Purpose

`saleor/graphql/tax/mutations` (`saleor/graphql/tax/mutations`) groups 8 source file(s) exposing 70 top-level declaration(s).

## Public surface

**`saleor/graphql/tax/mutations/tax_class_create.py`**

- `TaxClassCreateError` (class) — [saleor/graphql/tax/mutations/tax_class_create.py:19]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_class_create.py:27]
- `CountryRateInput` (class) — [saleor/graphql/tax/mutations/tax_class_create.py:31]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_class_create.py:43]
- `TaxClassCreateInput` (class) — [saleor/graphql/tax/mutations/tax_class_create.py:47]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_class_create.py:54]
- `TaxClassCreate` (class) — [saleor/graphql/tax/mutations/tax_class_create.py:58]
- `Arguments` (class) — [saleor/graphql/tax/mutations/tax_class_create.py:59]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_class_create.py:64]
- `create_country_rates` (function) — [saleor/graphql/tax/mutations/tax_class_create.py:72]
- `save` (function) — [saleor/graphql/tax/mutations/tax_class_create.py:82]

**`saleor/graphql/tax/mutations/tax_class_delete.py`**

- `TaxClassDeleteError` (class) — [saleor/graphql/tax/mutations/tax_class_delete.py:18]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_class_delete.py:21]
- `TaxClassDelete` (class) — [saleor/graphql/tax/mutations/tax_class_delete.py:25]
- `Arguments` (class) — [saleor/graphql/tax/mutations/tax_class_delete.py:26]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_class_delete.py:29]

**`saleor/graphql/tax/mutations/tax_class_update.py`**

- `CountryRateUpdateInput` (class) — [saleor/graphql/tax/mutations/tax_class_update.py:22]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_class_update.py:34]
- `TaxClassUpdateError` (class) — [saleor/graphql/tax/mutations/tax_class_update.py:38]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_class_update.py:46]
- `TaxClassUpdateInput` (class) — [saleor/graphql/tax/mutations/tax_class_update.py:50]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_class_update.py:66]
- `TaxClassUpdate` (class) — [saleor/graphql/tax/mutations/tax_class_update.py:70]
- `Arguments` (class) — [saleor/graphql/tax/mutations/tax_class_update.py:71]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_class_update.py:77]
- `clean_input` (function) — [saleor/graphql/tax/mutations/tax_class_update.py:85]
- `update_country_rates` (function) — [saleor/graphql/tax/mutations/tax_class_update.py:104]
- `remove_country_rates` (function) — [saleor/graphql/tax/mutations/tax_class_update.py:141]
- `save` (function) — [saleor/graphql/tax/mutations/tax_class_update.py:145]

**`saleor/graphql/tax/mutations/tax_configuration_update.py`**

- `TaxConfigurationPerCountryInput` (class) — [saleor/graphql/tax/mutations/tax_configuration_update.py:26]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_configuration_update.py:65]
- `TaxConfigurationUpdateInput` (class) — [saleor/graphql/tax/mutations/tax_configuration_update.py:69]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_configuration_update.py:120]
- `TaxConfigurationUpdateError` (class) — [saleor/graphql/tax/mutations/tax_configuration_update.py:124]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_configuration_update.py:132]
- `TaxConfigurationUpdate` (class) — [saleor/graphql/tax/mutations/tax_configuration_update.py:136]
- `Arguments` (class) — [saleor/graphql/tax/mutations/tax_configuration_update.py:137]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_configuration_update.py:144]
- `clean_input` (function) — [saleor/graphql/tax/mutations/tax_configuration_update.py:152]
- `clean_use_weighted_tax_for_shipping` (function) — [saleor/graphql/tax/mutations/tax_configuration_update.py:195]
- `clean_tax_app_id` (function) — [saleor/graphql/tax/mutations/tax_configuration_update.py:248]
- `update_countries_configuration` (function) — [saleor/graphql/tax/mutations/tax_configuration_update.py:307]
- `remove_countries_configuration` (function) — [saleor/graphql/tax/mutations/tax_configuration_update.py:361]
- `save` (function) — [saleor/graphql/tax/mutations/tax_configuration_update.py:367]

**`saleor/graphql/tax/mutations/tax_country_configuration_delete.py`**

- `TaxCountryConfigurationDeleteError` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_delete.py:21]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_delete.py:26]
- `TaxCountryConfigurationDelete` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_delete.py:30]
- `Arguments` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_delete.py:36]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_delete.py:41]
- `perform_mutation` (function) — [saleor/graphql/tax/mutations/tax_country_configuration_delete.py:48]

**`saleor/graphql/tax/mutations/tax_country_configuration_update.py`**

- `TaxCountryConfigurationUpdateError` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_update.py:25]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_update.py:35]
- `TaxClassRateInput` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_update.py:39]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_update.py:45]
- `TaxCountryConfigurationUpdate` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_update.py:49]
- `Arguments` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_update.py:55]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_country_configuration_update.py:70]
- `clean_input` (function) — [saleor/graphql/tax/mutations/tax_country_configuration_update.py:162]
- `update_default_rate` (function) — [saleor/graphql/tax/mutations/tax_country_configuration_update.py:169]
- `update_and_create_country_rates` (function) — [saleor/graphql/tax/mutations/tax_country_configuration_update.py:189]
- `perform_mutation` (function) — [saleor/graphql/tax/mutations/tax_country_configuration_update.py:227]

**`saleor/graphql/tax/mutations/tax_exemption_manage.py`**

- `TaxExemptionManageError` (class) — [saleor/graphql/tax/mutations/tax_exemption_manage.py:27]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_exemption_manage.py:30]
- `TaxExemptionManage` (class) — [saleor/graphql/tax/mutations/tax_exemption_manage.py:34]
- `Arguments` (class) — [saleor/graphql/tax/mutations/tax_exemption_manage.py:37]
- `Meta` (class) — [saleor/graphql/tax/mutations/tax_exemption_manage.py:45]
- `validate_input` (function) — [saleor/graphql/tax/mutations/tax_exemption_manage.py:57]
- `validate_order_status` (function) — [saleor/graphql/tax/mutations/tax_exemption_manage.py:65]
- `get_object` (function) — [saleor/graphql/tax/mutations/tax_exemption_manage.py:75]
- `perform_mutation` (function) — [saleor/graphql/tax/mutations/tax_exemption_manage.py:93]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/tax/mutations/__init__.py` (17 lines)
- `saleor/graphql/tax/mutations/tax_class_create.py` (85 lines)
- `saleor/graphql/tax/mutations/tax_class_delete.py` (38 lines)
- `saleor/graphql/tax/mutations/tax_class_update.py` (150 lines)
- `saleor/graphql/tax/mutations/tax_configuration_update.py` (376 lines)
- `saleor/graphql/tax/mutations/tax_country_configuration_delete.py` (55 lines)
- `saleor/graphql/tax/mutations/tax_country_configuration_update.py` (242 lines)
- `saleor/graphql/tax/mutations/tax_exemption_manage.py` (116 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....app.utils.get_active_tax_apps`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....checkout.models.Checkout`
- `....checkout.utils.invalidate_checkout`
- `....graphql.core.mutations.BaseMutation`
- `....order.ORDER_EDITABLE_STATUS`
- `....order.models.Order`
- `....permission.enums.CheckoutPermissions`
- `....plugins.PLUGIN_IDENTIFIER_PREFIX`
- `....tax.error_codes`
- `....tax.models`
- `...account.enums.CountryCodeEnum`
- `...core.ResolveInfo`
- `...core.context.SyncWebhookControlContext`
- `...core.doc_category.DOC_CATEGORY_TAXES`
- `...core.mutations.BaseMutation`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.types.BaseInputObjectType`
- `...core.types.Error`
- `...core.types.NonNullList`
- `...core.types.taxes.TaxSourceObject`
- `...core.utils.from_global_id_or_error`
- `...core.utils.get_duplicates_items`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `..enums.TaxCalculationStrategy`
- `..types.TaxClass`
- `..types.TaxConfiguration`
- `..types.TaxCountryConfiguration`
- `.tax_class_create.TaxClassCreate`
- `.tax_class_delete.TaxClassDelete`
- `.tax_class_update.TaxClassUpdate`
- `.tax_configuration_update.TaxConfigurationUpdate`
- `.tax_country_configuration_delete.TaxCountryConfigurationDelete`
- `.tax_country_configuration_update.TaxCountryConfigurationUpdate`
- `.tax_exemption_manage.TaxExemptionManage`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `3d05eb5159f0` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
