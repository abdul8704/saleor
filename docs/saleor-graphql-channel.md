## Purpose

`saleor/graphql/channel` (`saleor/graphql/channel`) groups 7 source file(s) exposing 37 top-level declaration(s).

## Public surface

**`saleor/graphql/channel/enums.py`**

- `mark_as_paid_strategy_deprecation_reason` (function) — [saleor/graphql/channel/enums.py:22]

**`saleor/graphql/channel/filters.py`**

- `get_channel_slug_from_filter_data` (function) — [saleor/graphql/channel/filters.py:1]
- `get_currency_from_filter_data` (function) — [saleor/graphql/channel/filters.py:6]

**`saleor/graphql/channel/resolvers.py`**

- `resolve_channel` (function) — [saleor/graphql/channel/resolvers.py:9]
- `resolve_channels` (function) — [saleor/graphql/channel/resolvers.py:33]

**`saleor/graphql/channel/schema.py`**

- `ChannelQueries` (class) — [saleor/graphql/channel/schema.py:20]
- `resolve_channel` (function) — [saleor/graphql/channel/schema.py:45]
- `resolve_channels` (function) — [saleor/graphql/channel/schema.py:49]
- `ChannelMutations` (class) — [saleor/graphql/channel/schema.py:53]

**`saleor/graphql/channel/types.py`**

- `StockSettings` (class) — [saleor/graphql/channel/types.py:51]
- `Meta` (class) — [saleor/graphql/channel/types.py:60]
- `CheckoutSettings` (class) — [saleor/graphql/channel/types.py:65]
- `Meta` (class) — [saleor/graphql/channel/types.py:118]
- `OrderSettings` (class) — [saleor/graphql/channel/types.py:123]
- `Meta` (class) — [saleor/graphql/channel/types.py:202]
- `PaymentSettings` (class) — [saleor/graphql/channel/types.py:207]
- `Meta` (class) — [saleor/graphql/channel/types.py:238]
- `Channel` (class) — [saleor/graphql/channel/types.py:243]
- `Meta` (class) — [saleor/graphql/channel/types.py:366]
- `resolve_tax_configuration` (function) — [saleor/graphql/channel/types.py:372]
- `resolve_has_orders` (function) — [saleor/graphql/channel/types.py:376]
- `resolve_default_country` (function) — [saleor/graphql/channel/types.py:384]
- `resolve_warehouses` (function) — [saleor/graphql/channel/types.py:390]
- `resolve_countries` (function) — [saleor/graphql/channel/types.py:394]
- `get_countries` (function) — [saleor/graphql/channel/types.py:397]
- `resolve_available_shipping_methods_per_country` (function) — [saleor/graphql/channel/types.py:415]
- `filter_shipping_methods` (function) — [saleor/graphql/channel/types.py:477]
- `get_shipping_methods` (function) — [saleor/graphql/channel/types.py:486]
- `resolve_stock_settings` (function) — [saleor/graphql/channel/types.py:500]
- `resolve_order_settings` (function) — [saleor/graphql/channel/types.py:504]
- `resolve_checkout_settings` (function) — [saleor/graphql/channel/types.py:528]
- `resolve_payment_settings` (function) — [saleor/graphql/channel/types.py:539]

**`saleor/graphql/channel/utils.py`**

- `get_default_channel_slug_or_graphql_error` (function) — [saleor/graphql/channel/utils.py:14]
- `get_default_channel_or_graphql_error` (function) — [saleor/graphql/channel/utils.py:26]
- `validate_channel` (function) — [saleor/graphql/channel/utils.py:39]
- `clean_channel` (function) — [saleor/graphql/channel/utils.py:63]
- `delete_invalid_warehouse_to_shipping_zone_relations` (function) — [saleor/graphql/channel/utils.py:85]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/channel/__init__.py` (1 lines)
- `saleor/graphql/channel/enums.py` (41 lines)
- `saleor/graphql/channel/filters.py` (8 lines)
- `saleor/graphql/channel/resolvers.py` (36 lines)
- `saleor/graphql/channel/schema.py` (59 lines)
- `saleor/graphql/channel/types.py` (546 lines)
- `saleor/graphql/channel/utils.py` (160 lines)

## Interactions

- Imports from: `saleor/graphql`, `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...channel.AllocationStrategy`
- `...channel.MarkAsPaidStrategy`
- `...channel.TransactionFlowStrategy`
- `...channel.exceptions.ChannelNotDefined`
- `...channel.exceptions.NoDefaultChannel`
- `...channel.models`
- `...channel.models.Channel`
- `...channel.utils.get_default_channel`
- `...permission.auth_filters.AuthorizationFilters`
- `...permission.auth_filters.is_app`
- `...permission.auth_filters.is_staff_user`
- `...shipping.models.ShippingZone`
- `...shipping.utils.convert_to_shipping_method_data`
- `..account.enums.CountryCodeEnum`
- `..core.ResolveInfo`
- `..core.context.get_database_connection_name`
- `..core.descriptions.DEPRECATED_LEGACY_PAYMENTS`
- `..core.doc_category.DOC_CATEGORY_CHANNELS`
- `..core.enums.to_enum`
- `..core.fields.BaseField`
- `..core.fields.PermissionsField`
- `..core.scalars.DateTime`
- `..core.scalars.Day`
- `..core.scalars.Hour`
- `..core.scalars.Minute`
- `..core.types.BaseObjectType`
- `..core.types.CountryDisplay`
- `..core.types.ModelObjectType`
- `..core.types.NonNullList`
- `..core.utils.from_global_id_or_error`
- `..core.validators.validate_one_of_args_is_in_query`
- `..meta.types.ObjectWithMetadata`
- `..shipping.dataloaders.ShippingZonesByChannelIdLoader`
- `..tax.dataloaders.TaxConfigurationByChannelId`
- `..warehouse.dataloaders.WarehousesByChannelIdLoader`
- `..warehouse.types.Warehouse`
- `.dataloaders.by_order.ChannelWithHasOrdersByIdLoader`
- `.resolvers.resolve_channel`
- `.resolvers.resolve_channels`
- `.types.Channel`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c644951e88d9` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
