## Purpose

`saleor/graphql/product/types` (`saleor/graphql/product/types`) groups 5 source file(s) exposing 170 top-level declaration(s).

## Public surface

**`saleor/graphql/product/types/categories.py`**

- `Category` (class) — [saleor/graphql/product/types/categories.py:44]
- `Meta` (class) — [saleor/graphql/product/types/categories.py:92]
- `resolve_ancestors` (function) — [saleor/graphql/product/types/categories.py:102]
- `resolve_description_json` (function) — [saleor/graphql/product/types/categories.py:112]
- `resolve_background_image` (function) — [saleor/graphql/product/types/categories.py:117]
- `resolve_children` (function) — [saleor/graphql/product/types/categories.py:146]
- `slice_children_categories` (function) — [saleor/graphql/product/types/categories.py:147]
- `resolve_parent` (function) — [saleor/graphql/product/types/categories.py:159]
- `resolve_url` (function) — [saleor/graphql/product/types/categories.py:165]
- `resolve_products` (function) — [saleor/graphql/product/types/categories.py:169]
- `CategoryCountableConnection` (class) — [saleor/graphql/product/types/categories.py:231]
- `Meta` (class) — [saleor/graphql/product/types/categories.py:232]

**`saleor/graphql/product/types/channels.py`**

- `Margin` (class) — [saleor/graphql/product/types/channels.py:39]
- `Meta` (class) — [saleor/graphql/product/types/channels.py:43]
- `ProductChannelListing` (class) — [saleor/graphql/product/types/channels.py:48]
- `Meta` (class) — [saleor/graphql/product/types/channels.py:113]
- `resolve_publication_date` (function) — [saleor/graphql/product/types/channels.py:119]
- `resolve_available_for_purchase` (function) — [saleor/graphql/product/types/channels.py:123]
- `resolve_channel` (function) — [saleor/graphql/product/types/channels.py:127]
- `resolve_purchase_cost` (function) — [saleor/graphql/product/types/channels.py:132]
- `calculate_margin_with_channel_listings` (function) — [saleor/graphql/product/types/channels.py:133]
- `resolve_margin` (function) — [saleor/graphql/product/types/channels.py:159]
- `calculate_margin_with_channel_listings` (function) — [saleor/graphql/product/types/channels.py:160]
- `resolve_is_available_for_purchase` (function) — [saleor/graphql/product/types/channels.py:185]
- `resolve_pricing` (function) — [saleor/graphql/product/types/channels.py:189]
- `load_tax_configuration` (function) — [saleor/graphql/product/types/channels.py:195]
- `load_tax_country_exceptions` (function) — [saleor/graphql/product/types/channels.py:199]
- `load_variant_channel_listings` (function) — [saleor/graphql/product/types/channels.py:200]
- `load_default_tax_rate` (function) — [saleor/graphql/product/types/channels.py:203]
- `calculate_pricing_info` (function) — [saleor/graphql/product/types/channels.py:216]
- `PreorderThreshold` (class) — [saleor/graphql/product/types/channels.py:292]
- `Meta` (class) — [saleor/graphql/product/types/channels.py:302]
- `ProductVariantChannelListing` (class) — [saleor/graphql/product/types/channels.py:307]
- `Meta` (class) — [saleor/graphql/product/types/channels.py:337]
- `resolve_channel` (function) — [saleor/graphql/product/types/channels.py:343]
- `resolve_margin` (function) — [saleor/graphql/product/types/channels.py:347]
- `resolve_preorder_threshold` (function) — [saleor/graphql/product/types/channels.py:351]
- `CollectionChannelListing` (class) — [saleor/graphql/product/types/channels.py:360]
- `Meta` (class) — [saleor/graphql/product/types/channels.py:378]
- `resolve_publication_date` (function) — [saleor/graphql/product/types/channels.py:384]
- `resolve_channel` (function) — [saleor/graphql/product/types/channels.py:388]

**`saleor/graphql/product/types/collections.py`**

- `Collection` (class) — [saleor/graphql/product/types/collections.py:52]
- `Meta` (class) — [saleor/graphql/product/types/collections.py:98]
- `resolve_channel` (function) — [saleor/graphql/product/types/collections.py:105]
- `resolve_background_image` (function) — [saleor/graphql/product/types/collections.py:109]
- `resolve_products` (function) — [saleor/graphql/product/types/collections.py:139]
- `resolve_channel_listings` (function) — [saleor/graphql/product/types/collections.py:177]
- `resolve_description_json` (function) — [saleor/graphql/product/types/collections.py:183]
- `CollectionCountableConnection` (class) — [saleor/graphql/product/types/collections.py:210]
- `Meta` (class) — [saleor/graphql/product/types/collections.py:211]

**`saleor/graphql/product/types/products.py`**

- `BasePricingInfo` (class) — [saleor/graphql/product/types/products.py:195]
- `Meta` (class) — [saleor/graphql/product/types/products.py:215]
- `VariantPricingInfo` (class) — [saleor/graphql/product/types/products.py:220]
- `Meta` (class) — [saleor/graphql/product/types/products.py:241]
- `ProductPricingInfo` (class) — [saleor/graphql/product/types/products.py:246]
- `Meta` (class) — [saleor/graphql/product/types/products.py:273]
- `PreorderData` (class) — [saleor/graphql/product/types/products.py:278]
- `Meta` (class) — [saleor/graphql/product/types/products.py:293]
- `resolve_global_threshold` (function) — [saleor/graphql/product/types/products.py:298]
- `resolve_global_sold_units` (function) — [saleor/graphql/product/types/products.py:302]
- `ProductVariant` (class) — [saleor/graphql/product/types/products.py:307]
- `Meta` (class) — [saleor/graphql/product/types/products.py:471]
- `resolve_created` (function) — [saleor/graphql/product/types/products.py:480]
- `resolve_channel` (function) — [saleor/graphql/product/types/products.py:484]
- `resolve_stocks` (function) — [saleor/graphql/product/types/products.py:489]
- `resolve_quantity_available` (function) — [saleor/graphql/product/types/products.py:515]
- `calculate_available_per_channel` (function) — [saleor/graphql/product/types/products.py:537]
- `calculate_available_channel_quantity_with_reservations` (function) — [saleor/graphql/product/types/products.py:549]
- `calculate_available_global` (function) — [saleor/graphql/product/types/products.py:576]
- `calculate_available_global_quantity_with_reservations` (function) — [saleor/graphql/product/types/products.py:596]
- `resolve_assigned_attribute` (function) — [saleor/graphql/product/types/products.py:640]
- `resolve_attributes` (function) — [saleor/graphql/product/types/products.py:646]
- `resolve_assigned_attributes` (function) — [saleor/graphql/product/types/products.py:663]
- `resolve_channel_listings` (function) — [saleor/graphql/product/types/products.py:674]
- `resolve_pricing` (function) — [saleor/graphql/product/types/products.py:678]
- `load_tax_configuration` (function) — [saleor/graphql/product/types/products.py:698]
- `load_tax_country_exceptions` (function) — [saleor/graphql/product/types/products.py:710]
- `load_default_tax_rate` (function) — [saleor/graphql/product/types/products.py:711]
- `calculate_pricing_info` (function) — [saleor/graphql/product/types/products.py:712]
- `resolve_product` (function) — [saleor/graphql/product/types/products.py:785]
- `resolve_quantity_ordered` (function) — [saleor/graphql/product/types/products.py:792]
- `resolve_revenue` (function) — [saleor/graphql/product/types/products.py:799]
- `calculate_revenue_with_channel` (function) — [saleor/graphql/product/types/products.py:804]
- `calculate_revenue_with_order_lines` (function) — [saleor/graphql/product/types/products.py:808]
- `calculate_revenue_with_orders` (function) — [saleor/graphql/product/types/products.py:809]
- `resolve_media` (function) — [saleor/graphql/product/types/products.py:839]
- `resolve_images` (function) — [saleor/graphql/product/types/products.py:843]
- `resolve_weight` (function) — [saleor/graphql/product/types/products.py:847]
- `resolve_preorder` (function) — [saleor/graphql/product/types/products.py:852]
- `calculate_global_sold_units` (function) — [saleor/graphql/product/types/products.py:859]
- _…and 80 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/types/collections.py` (214 lines)
- `saleor/graphql/product/types/__init__.py` (25 lines)
- `saleor/graphql/product/types/categories.py` (234 lines)
- `saleor/graphql/product/types/channels.py` (389 lines)
- `saleor/graphql/product/types/products.py` (2131 lines)

## Interactions

- Imports from: `saleor/graphql`, `saleor/plugins/openid_connect`
- Imported by: `saleor/order`, `saleor/warehouse`, `saleor/checkout`, `saleor/core`, `saleor/graphql/checkout/dataloaders`, `saleor/graphql/product/bulk_mutations`, `saleor/webhook`, `saleor/payment`, `saleor/discount/utils`, `saleor/graphql/app/dataloaders`, `saleor/graphql/attribute/dataloaders`, `saleor/graphql/order`, `saleor/plugins`, `saleor/product`, `saleor/product/utils`, `saleor/core/telemetry`, `saleor/core/utils`, `saleor/graphql/core`, `saleor/graphql`, `saleor/graphql/order/mutations`, `saleor/app`, `saleor/giftcard`, `saleor/graphql/attribute/mutations`, `saleor/graphql/attribute/utils`, `saleor/graphql/channel/mutations`, `saleor/graphql/discount/mutations/promotion`, `saleor/graphql/discount/mutations/sale`, `saleor/graphql/order/bulk_mutations`, `saleor/graphql/page/mutations`, `saleor/graphql/product/dataloaders`, `saleor/graphql/warehouse`, `saleor/product/migrations`, `saleor/warehouse/webhooks`, `saleor/account`, `saleor/attribute/migrations`, `saleor/csv/utils`, `saleor/graphql/account/bulk_mutations`, `saleor/graphql/account`, `saleor/graphql/account/mutations/permission_group`, `saleor/graphql/attribute/tests`, `saleor/graphql/channel`, `saleor/graphql/checkout/mutations`, `saleor/graphql/discount`, `saleor/graphql/plugins`, `saleor/graphql/product/mutations`, `saleor/graphql/product`, `saleor/graphql/shipping`, `saleor/graphql/shipping/mutations`, `saleor/graphql/tax`, `saleor/graphql/utils`, `saleor/graphql/webhook`, `saleor/permission`, `saleor/plugins/admin_email`, `saleor/plugins/avatax`, `saleor/plugins/user_email`, `saleor/plugins/webhook`, `saleor/shipping`, `saleor/tax/calculations`, `saleor/tax`, `saleor/webhook/observability`, `saleor/webhook/transport/asynchronous`, `saleor/account/migrations`, `saleor/account/migrations/tasks`, `saleor/attribute`, `saleor/core/db`, `saleor/core/utils/tests`, `saleor/csv/tests`, `saleor/discount`, `saleor/graphql/account/mutations`, `saleor/graphql/account/mutations/staff`, `saleor/graphql/account/tests/mutations/staff`, `saleor/graphql/channel/dataloaders`, `saleor/graphql/channel/tests/mutations`, `saleor/graphql/core/federation`, `saleor/graphql/core/utils`, `saleor/graphql/core/validators`, `saleor/graphql/csv`, `saleor/graphql/csv/mutations`, `saleor/graphql/discount/mutations`, `saleor/graphql/discount/mutations/voucher`, `saleor/graphql/discount/tests`, `saleor/graphql/giftcard/bulk_mutations`, `saleor/graphql/giftcard`, `saleor/graphql/giftcard/mutations`, `saleor/graphql/invoice`, `saleor/graphql/menu`, `saleor/graphql/meta`, `saleor/graphql/page`, `saleor/graphql/payment`, `saleor/graphql/product/filters`, `saleor/graphql/shop/tests/queries`, `saleor/graphql/translations`, `saleor/graphql/translations/mutations`, `saleor/graphql/warehouse/mutations`, `saleor/order/migrations`, `saleor/order/webhooks`, `saleor/page`, `saleor/payment/tests/fixtures`, `saleor/plugins/migrations`, `saleor/plugins/sendgrid`, `saleor/plugins/tests`, `saleor/product/tests`, `saleor/site`, `saleor/tax/migrations`, `saleor/tests`, `saleor/thumbnail`, `saleor/webhook/transport`

Internal dependencies named in the source:

- `....attribute.models`
- `....channel.models.Channel`
- `....core.db.connection.allow_writer_in_context`
- `....core.search.prefix_search`
- `....core.utils.build_absolute_uri`
- `....core.utils.country.get_active_country`
- `....core.weight.convert_weight_to_default_weight_unit`
- `....graphql.core.types.Money`
- `....graphql.core.types.MoneyRange`
- `....permission.auth_filters.AuthorizationFilters`
- `....permission.enums.OrderPermissions`
- `....permission.enums.ProductPermissions`
- `....permission.utils.has_one_of_permissions`
- `....product.ProductMediaTypes`
- `....product.models`
- `....product.models.ALL_PRODUCTS_PERMISSIONS`
- `....product.utils.availability.get_product_availability`
- `....product.utils.calculate_revenue_for_variant`
- `....product.utils.variants.get_variant_selection_attributes`
- `....warehouse.reservations.is_reservation_enabled`
- `...account.enums.CountryCodeEnum`
- `...account.types`
- `...attribute.resolvers.resolve_attributes`
- `...channel.dataloaders.by_self.ChannelByIdLoader`
- `...channel.dataloaders.by_self.ChannelBySlugLoader`
- `...channel.types.Channel`
- `...channel.utils.get_default_channel_slug_or_graphql_error`
- `...core.ResolveInfo`
- `...core.const.DEFAULT_NESTED_LIST_LIMIT`
- `...core.context.ChannelQsContext`
- `...core.context.get_database_connection_name`
- `...core.descriptions.DEPRECATED_IN_3X_INPUT`
- `...core.descriptions.RICH_CONTENT`
- `...core.doc_category.DOC_CATEGORY_PRODUCTS`
- `...core.enums.ReportingPeriod`
- `...core.federation.federated_entity`
- `...core.federation.resolve_federation_references`
- `...core.fields.ConnectionField`
- `...core.fields.FilterConnectionField`
- `...core.fields.JSONString`
- `...core.fields.PermissionsField`
- `...core.scalars.Date`
- `...core.scalars.DateTime`
- `...core.scalars.PositiveInt`
- `...core.tracing.traced_resolver`
- `...core.types.BaseObjectType`
- `...core.types.Image`
- `...core.types.ModelObjectType`
- `...core.types.NonNullList`
- `...core.types.ThumbnailField`
- `...core.types.context.ChannelContextType`
- `...core.utils.from_global_id_or_error`
- `...core.utils.validate_and_apply_search_rank_sorting`
- `...meta.types.ObjectWithMetadata`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...site.dataloaders.load_site_callback`
- `...tax.types.TaxClass`
- `...translations.fields.TranslationField`
- `...translations.types.CategoryTranslation`
- `...translations.types.CollectionTranslation`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `0e3996958c7c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
