## Purpose

`saleor/core/utils` (`saleor/core/utils`) groups 17 source file(s) exposing 127 top-level declaration(s).

## Public surface

**`saleor/core/utils/__init__.py`**

- `get_domain` (function) — [saleor/core/utils/__init__.py:24]
- `get_public_url` (function) — [saleor/core/utils/__init__.py:32]
- `is_ssl_enabled` (function) — [saleor/core/utils/__init__.py:40]
- `build_absolute_uri` (function) — [saleor/core/utils/__init__.py:46]
- `get_client_ip` (function) — [saleor/core/utils/__init__.py:57]
- `is_valid_ipv4` (function) — [saleor/core/utils/__init__.py:74]
- `is_valid_ipv6` (function) — [saleor/core/utils/__init__.py:83]
- `generate_unique_slug` (function) — [saleor/core/utils/__init__.py:92]
- `prepare_unique_slug` (function) — [saleor/core/utils/__init__.py:139]
- `prepare_unique_attribute_value_slug` (function) — [saleor/core/utils/__init__.py:151]
- `create_file_from_response` (function) — [saleor/core/utils/__init__.py:158]

**`saleor/core/utils/anonymization.py`**

- `generate_fake_address` (function) — [saleor/core/utils/anonymization.py:24]
- `generate_fake_user` (function) — [saleor/core/utils/anonymization.py:35]
- `generate_fake_metadata` (function) — [saleor/core/utils/anonymization.py:46]
- `anonymize_order` (function) — [saleor/core/utils/anonymization.py:51]
- `anonymize_checkout` (function) — [saleor/core/utils/anonymization.py:70]

**`saleor/core/utils/batches.py`**

- `queryset_in_batches` (function) — [saleor/core/utils/batches.py:4]

**`saleor/core/utils/cache.py`**

- `CacheDict` (class) — [saleor/core/utils/cache.py:4]

**`saleor/core/utils/country.py`**

- `get_active_country` (function) — [saleor/core/utils/country.py:10]

**`saleor/core/utils/date_time.py`**

- `convert_to_utc_date_time` (function) — [saleor/core/utils/date_time.py:4]

**`saleor/core/utils/events.py`**

- `get_is_deferred_payload` (function) — [saleor/core/utils/events.py:6]
- `call_event` (function) — [saleor/core/utils/events.py:19]

**`saleor/core/utils/json_serializer.py`**

- `Serializer` (class) — [saleor/core/utils/json_serializer.py:9]
- `CustomJsonEncoder` (class) — [saleor/core/utils/json_serializer.py:15]
- `default` (function) — [saleor/core/utils/json_serializer.py:16]

**`saleor/core/utils/lazyobjects.py`**

- `lazy_no_retry` (function) — [saleor/core/utils/lazyobjects.py:8]
- `unwrap_lazy` (function) — [saleor/core/utils/lazyobjects.py:36]

**`saleor/core/utils/metadata_manager.py`**

- `MetadataType` (class) — [saleor/core/utils/metadata_manager.py:9]
- `MetadataEmptyKeyError` (class) — [saleor/core/utils/metadata_manager.py:14]
- `MetadataItem` (class) — [saleor/core/utils/metadata_manager.py:19]
- `MetadataItemCollection` (class) — [saleor/core/utils/metadata_manager.py:32]
- `store_on_instance` (function) — [saleor/core/utils/metadata_manager.py:36]
- `create_from_graphql_input` (function) — [saleor/core/utils/metadata_manager.py:59]
- `metadata_is_valid` (function) — [saleor/core/utils/metadata_manager.py:79]

**`saleor/core/utils/promo_code.py`**

- `InvalidPromoCode` (class) — [saleor/core/utils/promo_code.py:10]
- `generate_promo_code` (function) — [saleor/core/utils/promo_code.py:21]
- `generate_random_code` (function) — [saleor/core/utils/promo_code.py:29]
- `is_available_promo_code` (function) — [saleor/core/utils/promo_code.py:35]
- `promo_code_is_voucher` (function) — [saleor/core/utils/promo_code.py:39]
- `promo_code_is_gift_card` (function) — [saleor/core/utils/promo_code.py:43]

**`saleor/core/utils/random_data.py`**

- `get_sample_data` (function) — [saleor/core/utils/random_data.py:182]
- `get_weight` (function) — [saleor/core/utils/random_data.py:196]
- `create_product_types` (function) — [saleor/core/utils/random_data.py:203]
- `create_categories` (function) — [saleor/core/utils/random_data.py:211]
- `create_collection_channel_listings` (function) — [saleor/core/utils/random_data.py:226]
- `create_collections` (function) — [saleor/core/utils/random_data.py:238]
- `assign_products_to_collections` (function) — [saleor/core/utils/random_data.py:250]
- `create_attributes` (function) — [saleor/core/utils/random_data.py:259]
- `create_attributes_values` (function) — [saleor/core/utils/random_data.py:266]
- `assign_reference_page_types_to_attributes` (function) — [saleor/core/utils/random_data.py:274]
- `create_products` (function) — [saleor/core/utils/random_data.py:281]
- `create_product_channel_listings` (function) — [saleor/core/utils/random_data.py:303]
- `create_stocks` (function) — [saleor/core/utils/random_data.py:315]
- `create_product_variants` (function) — [saleor/core/utils/random_data.py:325]
- `create_product_variant_channel_listings` (function) — [saleor/core/utils/random_data.py:350]
- `assign_attributes_to_product_types` (function) — [saleor/core/utils/random_data.py:363]
- `assign_attributes_to_page_types` (function) — [saleor/core/utils/random_data.py:375]
- `assign_attribute_values_to_products` (function) — [saleor/core/utils/random_data.py:387]
- `assign_attributes_to_variants` (function) — [saleor/core/utils/random_data.py:396]
- `assign_attribute_values_to_variants` (function) — [saleor/core/utils/random_data.py:405]
- `set_field_as_money` (function) — [saleor/core/utils/random_data.py:414]
- `create_products_by_schema` (function) — [saleor/core/utils/random_data.py:420]
- `SaleorProvider` (class) — [saleor/core/utils/random_data.py:479]
- `money` (function) — [saleor/core/utils/random_data.py:480]
- `weight` (function) — [saleor/core/utils/random_data.py:483]
- `get_email` (function) — [saleor/core/utils/random_data.py:490]
- `create_product_image` (function) — [saleor/core/utils/random_data.py:498]
- `create_address` (function) — [saleor/core/utils/random_data.py:508]
- `create_fake_user` (function) — [saleor/core/utils/random_data.py:530]
- `create_fake_payment` (function) — [saleor/core/utils/random_data.py:576]
- `create_transaction_with_events` (function) — [saleor/core/utils/random_data.py:645]
- `create_order_lines` (function) — [saleor/core/utils/random_data.py:763]
- `create_order_lines_with_preorder` (function) — [saleor/core/utils/random_data.py:820]
- `create_fulfillments` (function) — [saleor/core/utils/random_data.py:918]
- `create_fake_order` (function) — [saleor/core/utils/random_data.py:938]
- `create_fake_catalogue_promotion` (function) — [saleor/core/utils/random_data.py:1033]
- `create_fake_order_promotion` (function) — [saleor/core/utils/random_data.py:1078]
- `create_users` (function) — [saleor/core/utils/random_data.py:1117]
- `create_permission_groups` (function) — [saleor/core/utils/random_data.py:1123]
- `create_staffs` (function) — [saleor/core/utils/random_data.py:1144]
- _…and 25 more in this file_

**`saleor/core/utils/text.py`**

- `strip_accents` (function) — [saleor/core/utils/text.py:4]
- `safe_truncate` (function) — [saleor/core/utils/text.py:10]

**`saleor/core/utils/translations.py`**

- `TranslationWrapper` (class) — [saleor/core/utils/translations.py:7]
- `Translation` (class) — [saleor/core/utils/translations.py:30]
- `Meta` (class) — [saleor/core/utils/translations.py:33]
- `get_translated_object_id` (function) — [saleor/core/utils/translations.py:36]
- `get_translated_keys` (function) — [saleor/core/utils/translations.py:41]
- `get_translation_context` (function) — [saleor/core/utils/translations.py:46]
- `get_translation` (function) — [saleor/core/utils/translations.py:50]

**`saleor/core/utils/update_mutation_manager.py`**

- `InstanceTracker` (class) — [saleor/core/utils/update_mutation_manager.py:9]
- `get_field_values` (function) — [saleor/core/utils/update_mutation_manager.py:38]
- `get_modified_fields` (function) — [saleor/core/utils/update_mutation_manager.py:45]
- `get_foreign_modified_fields` (function) — [saleor/core/utils/update_mutation_manager.py:63]

**`saleor/core/utils/url.py`**

- `validate_storefront_url` (function) — [saleor/core/utils/url.py:11]
- `prepare_url` (function) — [saleor/core/utils/url.py:34]
- `get_default_storage_root_url` (function) — [saleor/core/utils/url.py:44]
- `sanitize_url_for_logging` (function) — [saleor/core/utils/url.py:54]

**`saleor/core/utils/validators.py`**

- `get_oembed_data` (function) — [saleor/core/utils/validators.py:17]
- `is_date_in_future` (function) — [saleor/core/utils/validators.py:30]
- `get_mime_type` (function) — [saleor/core/utils/validators.py:35]
- `is_image_mimetype` (function) — [saleor/core/utils/validators.py:41]
- `is_valid_image_content_type` (function) — [saleor/core/utils/validators.py:48]

## How it works

The module's files, as provided to this run:

- `saleor/core/utils/json_serializer.py` (22 lines)
- `saleor/core/utils/text.py` (25 lines)
- `saleor/core/utils/cache.py` (20 lines)
- `saleor/core/utils/__init__.py` (171 lines)
- `saleor/core/utils/translations.py` (53 lines)
- `saleor/core/utils/anonymization.py` (87 lines)
- `saleor/core/utils/batches.py` (17 lines)
- `saleor/core/utils/country.py` (36 lines)
- `saleor/core/utils/date_time.py` (10 lines)
- `saleor/core/utils/events.py` (28 lines)
- `saleor/core/utils/lazyobjects.py` (40 lines)
- `saleor/core/utils/metadata_manager.py` (85 lines)
- `saleor/core/utils/promo_code.py` (44 lines)
- `saleor/core/utils/random_data.py` (1905 lines)
- `saleor/core/utils/update_mutation_manager.py` (70 lines)
- `saleor/core/utils/url.py` (63 lines)
- `saleor/core/utils/validators.py` (52 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`, `saleor/webhook`, `saleor/plugins/openid_connect`
- Imported by: `saleor/product/migrations`, `saleor/order/migrations`, `saleor/account/migrations`, `saleor/discount/migrations`, `saleor/checkout/migrations`, `saleor/graphql/product/tests/mutations`, `saleor/shipping/migrations`, `saleor/app/migrations`, `saleor/graphql/attribute/mutations`, `saleor/graphql/attribute/tests/mutations`, `saleor/invoice/migrations`, `saleor/menu/migrations`, `saleor/page/migrations`, `saleor/payment/migrations`, `saleor/plugins/migrations`, `saleor/site/migrations`, `saleor/warehouse/migrations`, `saleor/attribute/migrations`, `saleor/channel/migrations`, `saleor/csv/migrations`, `saleor/giftcard/migrations`, `saleor/graphql/channel/mutations`, `saleor/graphql/channel/tests/mutations`, `saleor/graphql/page/tests/mutations`, `saleor/graphql`, `saleor/plugins/openid_connect`, `saleor/tax/migrations`, `saleor/tests`, `saleor/webhook/transport`, `saleor/account/management`, `saleor/account`, `saleor/app`, `saleor/core/tests`, `saleor/graphql/app/dataloaders`, `saleor/graphql/attribute/tests`, `saleor/graphql/attribute/utils`, `saleor/graphql/page/tests/deprecated`, `saleor/graphql/product/bulk_mutations`, `saleor/plugins/avatax`, `saleor`, `saleor/webhook`, `saleor/webhook/migrations`, `saleor/webhook/observability/tests`, `saleor/webhook/observability`, `saleor/webhook/transport/synchronous`

Internal dependencies named in the source:

- `...account.models.Address`
- `...account.models.Group`
- `...account.models.User`
- `...account.tests.fixtures.user.dangerously_create_test_user`
- `...account.utils.store_user_address`
- `...app.models.App`
- `...attribute.models.Attribute`
- `...channel.models.Channel`
- `...checkout.AddressType`
- `...checkout.fetch.fetch_checkout_info`
- `...checkout.models.Checkout`
- `...checkout.tests.utils.add_variant_to_checkout`
- `...checkout.utils.get_or_create_checkout_metadata`
- `...core.weight.zero_weight`
- `...discount.DiscountValueType`
- `...discount.RewardValueType`
- `...discount.VoucherType`
- `...discount.models.VoucherCode`
- `...giftcard.error_codes.GiftCardErrorCode`
- `...giftcard.events`
- `...giftcard.models.GiftCard`
- `...giftcard.models.GiftCardTag`
- `...graphql.account.types.AddressInput`
- `...graphql.meta.inputs.MetadataInput`
- `...menu.models.Menu`
- `...menu.models.MenuItem`
- `...order.OrderStatus`
- `...order.models.Fulfillment`
- `...order.models.Order`
- `...order.models.OrderLine`
- `...order.search.prepare_order_search_vector_value`
- `...order.utils.update_order_status`
- `...page.models.Page`
- `...page.models.PageType`
- `...payment.TransactionAction`
- `...payment.TransactionEventType`
- `...payment.models.TransactionEvent`
- `...payment.models.TransactionItem`
- `...permission.models.Permission`
- `...plugins.manager.get_plugins_manager`
- `...product.ProductMediaTypes`
- `...product.search.update_products_search_vector`
- `...site.models.SiteSettings`
- `...tax.models.TaxClass`
- `...tax.models.TaxConfiguration`
- `...tax.utils.get_tax_class_kwargs_for_order_line`
- `...thumbnail.MIME_TYPE_TO_PIL_IDENTIFIER`
- `...warehouse.WarehouseClickAndCollectOption`
- `...warehouse.management.increase_stock`
- `...warehouse.models.PreorderAllocation`
- `...warehouse.models.Stock`
- `...warehouse.models.Warehouse`
- `...webhook.event_types.WebhookEventAsyncType`
- `..build_absolute_uri`
- `..exceptions.UnsupportedMediaProviderException`
- `..models.ModelWithMetadata`
- `..postgres.FlatConcatSearchVector`
- `.random_data.create_address`
- `.random_data.create_fake_user`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8048f5c95422` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
