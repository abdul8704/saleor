## Purpose

`saleor/graphql/shipping` (`saleor/graphql/shipping`) groups 8 source file(s) exposing 74 top-level declaration(s).

## Public surface

**`saleor/graphql/shipping/dataloaders.py`**

- `ShippingMethodByIdLoader` (class) — [saleor/graphql/shipping/dataloaders.py:16]
- `batch_load` (function) — [saleor/graphql/shipping/dataloaders.py:19]
- `ShippingZoneByIdLoader` (class) — [saleor/graphql/shipping/dataloaders.py:26]
- `batch_load` (function) — [saleor/graphql/shipping/dataloaders.py:29]
- `ShippingZonesByChannelIdLoader` (class) — [saleor/graphql/shipping/dataloaders.py:36]
- `batch_load` (function) — [saleor/graphql/shipping/dataloaders.py:39]
- `ShippingMethodsByShippingZoneIdLoader` (class) — [saleor/graphql/shipping/dataloaders.py:63]
- `batch_load` (function) — [saleor/graphql/shipping/dataloaders.py:66]
- `PostalCodeRulesByShippingMethodIdLoader` (class) — [saleor/graphql/shipping/dataloaders.py:81]
- `batch_load` (function) — [saleor/graphql/shipping/dataloaders.py:84]
- `ShippingMethodsByShippingZoneIdAndChannelSlugLoader` (class) — [saleor/graphql/shipping/dataloaders.py:100]
- `batch_load` (function) — [saleor/graphql/shipping/dataloaders.py:103]
- `ShippingMethodChannelListingByShippingMethodIdLoader` (class) — [saleor/graphql/shipping/dataloaders.py:127]
- `batch_load` (function) — [saleor/graphql/shipping/dataloaders.py:130]
- `ShippingMethodChannelListingByChannelSlugLoader` (class) — [saleor/graphql/shipping/dataloaders.py:147]
- `batch_load` (function) — [saleor/graphql/shipping/dataloaders.py:150]
- `ShippingMethodChannelListingByShippingMethodIdAndChannelSlugLoader` (class) — [saleor/graphql/shipping/dataloaders.py:168]
- `batch_load` (function) — [saleor/graphql/shipping/dataloaders.py:171]
- `ChannelsByShippingZoneIdLoader` (class) — [saleor/graphql/shipping/dataloaders.py:196]
- `batch_load` (function) — [saleor/graphql/shipping/dataloaders.py:199]
- `map_channels` (function) — [saleor/graphql/shipping/dataloaders.py:209]
- `ShippingZonesByCountryLoader` (class) — [saleor/graphql/shipping/dataloaders.py:229]
- `batch_load` (function) — [saleor/graphql/shipping/dataloaders.py:232]

**`saleor/graphql/shipping/filters.py`**

- `filter_channels` (function) — [saleor/graphql/shipping/filters.py:10]
- `filter_shipping_zones_search` (function) — [saleor/graphql/shipping/filters.py:17]
- `ShippingZoneFilter` (class) — [saleor/graphql/shipping/filters.py:21]
- `Meta` (class) — [saleor/graphql/shipping/filters.py:25]
- `ShippingZoneFilterInput` (class) — [saleor/graphql/shipping/filters.py:30]
- `Meta` (class) — [saleor/graphql/shipping/filters.py:31]

**`saleor/graphql/shipping/resolvers.py`**

- `resolve_shipping_zones` (function) — [saleor/graphql/shipping/resolvers.py:10]
- `resolve_price_range` (function) — [saleor/graphql/shipping/resolvers.py:22]
- `resolve_shipping_translation` (function) — [saleor/graphql/shipping/resolvers.py:32]

**`saleor/graphql/shipping/schema.py`**

- `ShippingQueries` (class) — [saleor/graphql/shipping/schema.py:32]
- `resolve_shipping_zone` (function) — [saleor/graphql/shipping/schema.py:59]
- `resolve_shipping_zones` (function) — [saleor/graphql/shipping/schema.py:71]
- `ShippingMutations` (class) — [saleor/graphql/shipping/schema.py:81]

**`saleor/graphql/shipping/types.py`**

- `ShippingMethodChannelListing` (class) — [saleor/graphql/shipping/types.py:53]
- `Meta` (class) — [saleor/graphql/shipping/types.py:70]
- `resolve_channel` (function) — [saleor/graphql/shipping/types.py:76]
- `resolve_minimum_order_price` (function) — [saleor/graphql/shipping/types.py:80]
- `ShippingMethodPostalCodeRule` (class) — [saleor/graphql/shipping/types.py:86]
- `Meta` (class) — [saleor/graphql/shipping/types.py:95]
- `ShippingMethodType` (class) — [saleor/graphql/shipping/types.py:101]
- `Meta` (class) — [saleor/graphql/shipping/types.py:163]
- `resolve_id` (function) — [saleor/graphql/shipping/types.py:173]
- `resolve_maximum_order_price` (function) — [saleor/graphql/shipping/types.py:177]
- `resolve_minimum_order_price` (function) — [saleor/graphql/shipping/types.py:194]
- `resolve_maximum_order_weight` (function) — [saleor/graphql/shipping/types.py:211]
- `resolve_postal_code_rules` (function) — [saleor/graphql/shipping/types.py:217]
- `resolve_minimum_order_weight` (function) — [saleor/graphql/shipping/types.py:221]
- `resolve_channel_listings` (function) — [saleor/graphql/shipping/types.py:227]
- `resolve_excluded_products` (function) — [saleor/graphql/shipping/types.py:233]
- `resolve_tax_class` (function) — [saleor/graphql/shipping/types.py:253]
- `ShippingZone` (class) — [saleor/graphql/shipping/types.py:261]
- `Meta` (class) — [saleor/graphql/shipping/types.py:294]
- `resolve_price_range` (function) — [saleor/graphql/shipping/types.py:306]
- `resolve_countries` (function) — [saleor/graphql/shipping/types.py:310]
- `resolve_shipping_methods` (function) — [saleor/graphql/shipping/types.py:317]
- `wrap_shipping_method_with_channel_context` (function) — [saleor/graphql/shipping/types.py:318]
- `resolve_warehouses` (function) — [saleor/graphql/shipping/types.py:340]
- `resolve_channels` (function) — [saleor/graphql/shipping/types.py:344]
- `ShippingMethod` (class) — [saleor/graphql/shipping/types.py:348]
- `Meta` (class) — [saleor/graphql/shipping/types.py:398]
- `resolve_id` (function) — [saleor/graphql/shipping/types.py:407]
- `resolve_maximum_order_weight` (function) — [saleor/graphql/shipping/types.py:411]
- `resolve_minimum_order_weight` (function) — [saleor/graphql/shipping/types.py:415]
- `ShippingZoneCountableConnection` (class) — [saleor/graphql/shipping/types.py:419]
- `Meta` (class) — [saleor/graphql/shipping/types.py:420]
- `ShippingMethodsPerCountry` (class) — [saleor/graphql/shipping/types.py:425]
- `Meta` (class) — [saleor/graphql/shipping/types.py:433]

**`saleor/graphql/shipping/utils.py`**

- `get_shipping_model_by_object_id` (function) — [saleor/graphql/shipping/utils.py:12]
- `get_shipping_model_by_object_id` (function) — [saleor/graphql/shipping/utils.py:18]
- `get_shipping_model_by_object_id` (function) — [saleor/graphql/shipping/utils.py:23]
- `get_instances_by_object_ids` (function) — [saleor/graphql/shipping/utils.py:48]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/shipping/__init__.py` (1 lines)
- `saleor/graphql/shipping/dataloaders.py` (246 lines)
- `saleor/graphql/shipping/enums.py` (17 lines)
- `saleor/graphql/shipping/filters.py` (33 lines)
- `saleor/graphql/shipping/resolvers.py` (37 lines)
- `saleor/graphql/shipping/schema.py` (97 lines)
- `saleor/graphql/shipping/types.py` (435 lines)
- `saleor/graphql/shipping/utils.py` (55 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...channel.models.Channel`
- `...core.weight.convert_weight_to_default_weight_unit`
- `...graphql.core.enums.to_enum`
- `...permission.auth_filters.AuthorizationFilters`
- `...permission.enums.ShippingPermissions`
- `...product.models`
- `...shipping.PostalCodeRuleInclusionType`
- `...shipping.ShippingMethodType`
- `...shipping.interface.ShippingMethodData`
- `...shipping.models`
- `...shipping.models.ShippingZone`
- `..account.enums.CountryCodeEnum`
- `..channel.dataloaders.by_self.ChannelByIdLoader`
- `..channel.types.Channel`
- `..core.ResolveInfo`
- `..core.connection.CountableConnection`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.context.ChannelContext`
- `..core.context.ChannelQsContext`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.descriptions.DEFAULT_DEPRECATION_REASON`
- `..core.descriptions.RICH_CONTENT`
- `..core.doc_category.DOC_CATEGORY_SHIPPING`
- `..core.fields.ConnectionField`
- `..core.fields.FilterConnectionField`
- `..core.fields.JSONString`
- `..core.fields.PermissionsField`
- `..core.filters.FilterInputObjectType`
- `..core.filters.GlobalIDMultipleChoiceFilter`
- `..core.tracing.traced_resolver`
- `..core.types.context.ChannelContextType`
- `..core.utils.from_global_id_or_error`
- `..meta.types.ObjectWithMetadata`
- `..product.types.ProductCountableConnection`
- `..shipping.resolvers.resolve_price_range`
- `..shipping.resolvers.resolve_shipping_translation`
- `..tax.dataloaders.TaxClassByIdLoader`
- `..tax.types.TaxClass`
- `..translations.fields.TranslationField`
- `..translations.mutations.ShippingPriceTranslate`
- `..translations.resolvers.resolve_translation`
- `..translations.types.ShippingMethodTranslation`
- `..utils.resolve_global_ids_to_primary_keys`
- `..warehouse.dataloaders.WarehousesByShippingZoneIdLoader`
- `..warehouse.types.Warehouse`
- `.bulk_mutations.ShippingPriceBulkDelete`
- `.bulk_mutations.ShippingZoneBulkDelete`
- `.enums.PostalCodeRuleInclusionTypeEnum`
- `.enums.ShippingMethodTypeEnum`
- `.filters.ShippingZoneFilterInput`
- `.mutations.delivery_options_calculate.DeliveryOptionsCalculate`
- `.resolvers.resolve_shipping_zones`
- `.types.ShippingMethod`
- `.types.ShippingMethodType`
- `.types.ShippingZone`
- `.types.ShippingZoneCountableConnection`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `aa995fce56a4` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
