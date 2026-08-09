## Purpose

`saleor/graphql/tax` (`saleor/graphql/tax`) groups 7 source file(s) exposing 64 top-level declaration(s).

## Public surface

**`saleor/graphql/tax/dataloaders.py`**

- `TaxConfigurationPerCountryByTaxConfigurationIDLoader` (class) — [saleor/graphql/tax/dataloaders.py:22]
- `batch_load` (function) — [saleor/graphql/tax/dataloaders.py:25]
- `TaxConfigurationByChannelId` (class) — [saleor/graphql/tax/dataloaders.py:37]
- `batch_load` (function) — [saleor/graphql/tax/dataloaders.py:40]
- `TaxClassCountryRateByTaxClassIDLoader` (class) — [saleor/graphql/tax/dataloaders.py:47]
- `batch_load` (function) — [saleor/graphql/tax/dataloaders.py:50]
- `TaxClassDefaultRateByCountryLoader` (class) — [saleor/graphql/tax/dataloaders.py:62]
- `batch_load` (function) — [saleor/graphql/tax/dataloaders.py:65]
- `TaxClassByIdLoader` (class) — [saleor/graphql/tax/dataloaders.py:73]
- `batch_load` (function) — [saleor/graphql/tax/dataloaders.py:76]
- `TaxClassIdByProductIdLoader` (class) — [saleor/graphql/tax/dataloaders.py:83]
- `batch_load` (function) — [saleor/graphql/tax/dataloaders.py:86]
- `load_tax_classes` (function) — [saleor/graphql/tax/dataloaders.py:90]
- `TaxClassByVariantIdLoader` (class) — [saleor/graphql/tax/dataloaders.py:107]
- `batch_load` (function) — [saleor/graphql/tax/dataloaders.py:110]
- `load_tax_classes` (function) — [saleor/graphql/tax/dataloaders.py:114]
- `ProductChargeTaxesByTaxClassIdLoader` (class) — [saleor/graphql/tax/dataloaders.py:138]
- `batch_load` (function) — [saleor/graphql/tax/dataloaders.py:146]

**`saleor/graphql/tax/enums.py`**

- `description` (function) — [saleor/graphql/tax/enums.py:15]

**`saleor/graphql/tax/filters.py`**

- `filter_tax_classes_by_country` (function) — [saleor/graphql/tax/filters.py:16]
- `TaxConfigurationFilter` (class) — [saleor/graphql/tax/filters.py:25]
- `Meta` (class) — [saleor/graphql/tax/filters.py:28]
- `TaxConfigurationFilterInput` (class) — [saleor/graphql/tax/filters.py:33]
- `Meta` (class) — [saleor/graphql/tax/filters.py:34]
- `TaxClassFilter` (class) — [saleor/graphql/tax/filters.py:39]
- `Meta` (class) — [saleor/graphql/tax/filters.py:45]
- `TaxClassFilterInput` (class) — [saleor/graphql/tax/filters.py:50]
- `Meta` (class) — [saleor/graphql/tax/filters.py:51]

**`saleor/graphql/tax/schema.py`**

- `TaxQueries` (class) — [saleor/graphql/tax/schema.py:36]
- `resolve_tax_configuration` (function) — [saleor/graphql/tax/schema.py:112]
- `resolve_tax_configurations` (function) — [saleor/graphql/tax/schema.py:123]
- `resolve_tax_class` (function) — [saleor/graphql/tax/schema.py:134]
- `resolve_tax_classes` (function) — [saleor/graphql/tax/schema.py:143]
- `resolve_tax_country_configuration` (function) — [saleor/graphql/tax/schema.py:152]
- `resolve_tax_country_configurations` (function) — [saleor/graphql/tax/schema.py:162]
- `TaxMutations` (class) — [saleor/graphql/tax/schema.py:177]

**`saleor/graphql/tax/sorters.py`**

- `TaxClassSortField` (class) — [saleor/graphql/tax/sorters.py:5]
- `Meta` (class) — [saleor/graphql/tax/sorters.py:8]
- `description` (function) — [saleor/graphql/tax/sorters.py:12]
- `TaxClassSortingInput` (class) — [saleor/graphql/tax/sorters.py:19]
- `Meta` (class) — [saleor/graphql/tax/sorters.py:20]

**`saleor/graphql/tax/types.py`**

- `TaxConfiguration` (class) — [saleor/graphql/tax/types.py:19]
- `Meta` (class) — [saleor/graphql/tax/types.py:70]
- `resolve_channel` (function) — [saleor/graphql/tax/types.py:76]
- `resolve_countries` (function) — [saleor/graphql/tax/types.py:80]
- `resolve_use_weighted_tax_for_shipping` (function) — [saleor/graphql/tax/types.py:86]
- `TaxConfigurationCountableConnection` (class) — [saleor/graphql/tax/types.py:92]
- `Meta` (class) — [saleor/graphql/tax/types.py:93]
- `TaxConfigurationPerCountry` (class) — [saleor/graphql/tax/types.py:98]
- `Meta` (class) — [saleor/graphql/tax/types.py:138]
- `resolve_country` (function) — [saleor/graphql/tax/types.py:144]
- `resolve_use_weighted_tax_for_shipping` (function) — [saleor/graphql/tax/types.py:148]
- `TaxClass` (class) — [saleor/graphql/tax/types.py:154]
- `Meta` (class) — [saleor/graphql/tax/types.py:162]
- `resolve_countries` (function) — [saleor/graphql/tax/types.py:172]
- `TaxClassCountableConnection` (class) — [saleor/graphql/tax/types.py:176]
- `Meta` (class) — [saleor/graphql/tax/types.py:177]
- `TaxClassCountryRate` (class) — [saleor/graphql/tax/types.py:182]
- `Meta` (class) — [saleor/graphql/tax/types.py:193]
- `resolve_country` (function) — [saleor/graphql/tax/types.py:202]
- `resolve_tax_class` (function) — [saleor/graphql/tax/types.py:206]
- `TaxCountryConfiguration` (class) — [saleor/graphql/tax/types.py:214]
- `Meta` (class) — [saleor/graphql/tax/types.py:224]
- `resolve_country` (function) — [saleor/graphql/tax/types.py:229]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/tax/__init__.py` (1 lines)
- `saleor/graphql/tax/dataloaders.py` (163 lines)
- `saleor/graphql/tax/enums.py` (35 lines)
- `saleor/graphql/tax/filters.py` (53 lines)
- `saleor/graphql/tax/schema.py` (184 lines)
- `saleor/graphql/tax/sorters.py` (23 lines)
- `saleor/graphql/tax/types.py` (230 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...permission.auth_filters.AuthorizationFilters`
- `...tax.models`
- `..account.enums.CountryCodeEnum`
- `..channel.dataloaders.by_self.ChannelByIdLoader`
- `..channel.types.Channel`
- `..core.ResolveInfo`
- `..core.connection.CountableConnection`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.doc_category.DOC_CATEGORY_TAXES`
- `..core.enums.to_enum`
- `..core.fields.FilterConnectionField`
- `..core.fields.PermissionsField`
- `..core.types.BaseEnum`
- `..core.types.BaseObjectType`
- `..core.types.CountryDisplay`
- `..core.types.ModelObjectType`
- `..core.types.NonNullList`
- `..core.types.SortInputObjectType`
- `..core.utils.from_global_id_or_error`
- `..meta.types.ObjectWithMetadata`
- `..utils.filters.filter_by_id`
- `.enums.TaxCalculationStrategy`
- `.filters.TaxClassFilterInput`
- `.filters.TaxConfigurationFilterInput`
- `.sorters.TaxClassSortingInput`
- `.types.TaxClass`
- `.types.TaxConfiguration`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `d8d2d375a30e` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
