## Purpose

`saleor/graphql/meta` (`saleor/graphql/meta`) groups 7 source file(s) exposing 55 top-level declaration(s).

## Public surface

**`saleor/graphql/meta/extra_methods.py`**

- `extra_checkout_actions` (function) — [saleor/graphql/meta/extra_methods.py:9]
- `extra_channel_actions` (function) — [saleor/graphql/meta/extra_methods.py:25]
- `extra_collection_actions` (function) — [saleor/graphql/meta/extra_methods.py:30]
- `extra_fulfillment_actions` (function) — [saleor/graphql/meta/extra_methods.py:35]
- `extra_gift_card_actions` (function) — [saleor/graphql/meta/extra_methods.py:40]
- `extra_order_actions` (function) — [saleor/graphql/meta/extra_methods.py:45]
- `extra_product_actions` (function) — [saleor/graphql/meta/extra_methods.py:54]
- `extra_variant_actions` (function) — [saleor/graphql/meta/extra_methods.py:63]
- `extra_shipping_zone_actions` (function) — [saleor/graphql/meta/extra_methods.py:72]
- `extra_transaction_item_actions` (function) — [saleor/graphql/meta/extra_methods.py:77]
- `extra_user_actions` (function) — [saleor/graphql/meta/extra_methods.py:82]
- `extra_warehouse_actions` (function) — [saleor/graphql/meta/extra_methods.py:91]
- `extra_voucher_actions` (function) — [saleor/graphql/meta/extra_methods.py:96]
- `extra_shop_actions` (function) — [saleor/graphql/meta/extra_methods.py:101]

**`saleor/graphql/meta/inputs.py`**

- `MetadataInputDescription` (class) — [saleor/graphql/meta/inputs.py:4]
- `MetadataInput` (class) — [saleor/graphql/meta/inputs.py:20]

**`saleor/graphql/meta/permissions.py`**

- `no_permissions` (function) — [saleor/graphql/meta/permissions.py:40]
- `public_user_permissions` (function) — [saleor/graphql/meta/permissions.py:44]
- `private_user_permissions` (function) — [saleor/graphql/meta/permissions.py:74]
- `public_address_permissions` (function) — [saleor/graphql/meta/permissions.py:90]
- `private_address_permissions` (function) — [saleor/graphql/meta/permissions.py:141]
- `product_permissions` (function) — [saleor/graphql/meta/permissions.py:176]
- `product_type_permissions` (function) — [saleor/graphql/meta/permissions.py:182]
- `order_permissions` (function) — [saleor/graphql/meta/permissions.py:188]
- `invoice_permissions` (function) — [saleor/graphql/meta/permissions.py:192]
- `menu_permissions` (function) — [saleor/graphql/meta/permissions.py:198]
- `app_permissions` (function) — [saleor/graphql/meta/permissions.py:202]
- `private_app_permssions` (function) — [saleor/graphql/meta/permissions.py:215]
- `channel_permissions` (function) — [saleor/graphql/meta/permissions.py:224]
- `checkout_permissions` (function) — [saleor/graphql/meta/permissions.py:230]
- `page_permissions` (function) — [saleor/graphql/meta/permissions.py:236]
- `page_type_permissions` (function) — [saleor/graphql/meta/permissions.py:240]
- `attribute_permissions` (function) — [saleor/graphql/meta/permissions.py:246]
- `shipping_permissions` (function) — [saleor/graphql/meta/permissions.py:256]
- `discount_permissions` (function) — [saleor/graphql/meta/permissions.py:262]
- `public_payment_permissions` (function) — [saleor/graphql/meta/permissions.py:268]
- `private_payment_permissions` (function) — [saleor/graphql/meta/permissions.py:281]
- `gift_card_permissions` (function) — [saleor/graphql/meta/permissions.py:290]
- `tax_permissions` (function) — [saleor/graphql/meta/permissions.py:296]
- `site_permissions` (function) — [saleor/graphql/meta/permissions.py:303]

**`saleor/graphql/meta/resolvers.py`**

- `resolve_object_with_metadata_type` (function) — [saleor/graphql/meta/resolvers.py:30]
- `resolve_metadata` (function) — [saleor/graphql/meta/resolvers.py:110]
- `check_private_metadata_privilege` (function) — [saleor/graphql/meta/resolvers.py:117]
- `resolve_private_metadata` (function) — [saleor/graphql/meta/resolvers.py:141]

**`saleor/graphql/meta/schema.py`**

- `MetaMutations` (class) — [saleor/graphql/meta/schema.py:11]

**`saleor/graphql/meta/types.py`**

- `MetadataItem` (class) — [saleor/graphql/meta/types.py:16]
- `Metadata` (class) — [saleor/graphql/meta/types.py:21]
- `ObjectWithMetadata` (class) — [saleor/graphql/meta/types.py:49]
- `resolve_metadata` (function) — [saleor/graphql/meta/types.py:96]
- `resolve_metafield` (function) — [saleor/graphql/meta/types.py:103]
- `resolve_metafields` (function) — [saleor/graphql/meta/types.py:113]
- `resolve_private_metadata` (function) — [saleor/graphql/meta/types.py:118]
- `resolve_private_metafield` (function) — [saleor/graphql/meta/types.py:125]
- `resolve_private_metafields` (function) — [saleor/graphql/meta/types.py:136]
- `resolve_type` (function) — [saleor/graphql/meta/types.py:147]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/meta/__init__.py` (1 lines)
- `saleor/graphql/meta/extra_methods.py` (121 lines)
- `saleor/graphql/meta/inputs.py` (22 lines)
- `saleor/graphql/meta/permissions.py` (383 lines)
- `saleor/graphql/meta/resolvers.py` (143 lines)
- `saleor/graphql/meta/schema.py` (15 lines)
- `saleor/graphql/meta/types.py` (154 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/plugins/openid_connect`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...account.error_codes.AccountErrorCode`
- `...account.models`
- `...app.models`
- `...attribute.AttributeType`
- `...attribute.models`
- `...channel.models`
- `...checkout.actions.call_checkout_events`
- `...checkout.models`
- `...core.exceptions.PermissionDenied`
- `...core.jwt.JWT_THIRDPARTY_ACCESS_TYPE`
- `...core.models.ModelWithMetadata`
- `...discount.models`
- `...giftcard.models`
- `...invoice.models`
- `...menu.models`
- `...order.actions.call_order_event`
- `...order.models`
- `...page.models`
- `...payment.models`
- `...payment.utils.payment_owned_by_user`
- `...permission.utils.one_of_permissions_or_auth_filter_required`
- `...product.models`
- `...shipping.interface.ShippingMethodData`
- `...shipping.models`
- `...site.models`
- `...tax.models`
- `...warehouse.models`
- `...webhook.event_types.WebhookEventAsyncType`
- `..account.types`
- `..app.dataloaders.get_app_promise`
- `..app.types`
- `..attribute.types`
- `..channel.types`
- `..checkout.types`
- `..core.ResolveInfo`
- `..core.context.BaseContext`
- `..core.context.get_database_connection_name`
- `..core.types.NonNullList`
- `..core.utils.from_global_id_or_error`
- `..discount.types`
- `..giftcard.types`
- `..invoice.types`
- `..menu.types`
- `..order.types`
- `..page.types`
- `..payment.types`
- `..plugins.dataloaders.get_plugin_manager_promise`
- `..product.types`
- `..shipping.types`
- `..shop.types`
- `..site.dataloaders.get_site_promise`
- `..tax.types`
- `..utils.get_user_or_app_from_context`
- `..warehouse.types`
- `.permissions.PRIVATE_META_PERMISSION_MAP`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `35136ddc07ad` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
