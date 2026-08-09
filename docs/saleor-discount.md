## Purpose

`saleor/discount` (`saleor/discount`) groups 6 source file(s) exposing 98 top-level declaration(s).

## Public surface

**`saleor/discount/__init__.py`**

- `DiscountValueType` (class) — [saleor/discount/__init__.py:8]
- `DiscountType` (class) — [saleor/discount/__init__.py:18]
- `VoucherType` (class) — [saleor/discount/__init__.py:34]
- `PromotionType` (class) — [saleor/discount/__init__.py:46]
- `RewardValueType` (class) — [saleor/discount/__init__.py:56]
- `RewardType` (class) — [saleor/discount/__init__.py:66]
- `PromotionEvents` (class) — [saleor/discount/__init__.py:76]
- `PromotionRuleInfo` (class) — [saleor/discount/__init__.py:98]

**`saleor/discount/error_codes.py`**

- `DiscountErrorCode` (class) — [saleor/discount/error_codes.py:4]
- `PromotionCreateErrorCode` (class) — [saleor/discount/error_codes.py:16]
- `PromotionUpdateErrorCode` (class) — [saleor/discount/error_codes.py:29]
- `PromotionDeleteErrorCode` (class) — [saleor/discount/error_codes.py:36]
- `PromotionRuleCreateErrorCode` (class) — [saleor/discount/error_codes.py:41]
- `PromotionRuleUpdateErrorCode` (class) — [saleor/discount/error_codes.py:54]
- `PromotionRuleDeleteErrorCode` (class) — [saleor/discount/error_codes.py:67]
- `VoucherCodeBulkDeleteErrorCode` (class) — [saleor/discount/error_codes.py:72]

**`saleor/discount/events.py`**

- `promotion_created_event` (function) — [saleor/discount/events.py:20]
- `promotion_updated_event` (function) — [saleor/discount/events.py:26]
- `promotion_started_event` (function) — [saleor/discount/events.py:32]
- `promotion_ended_event` (function) — [saleor/discount/events.py:38]
- `rule_created_event` (function) — [saleor/discount/events.py:66]
- `rule_updated_event` (function) — [saleor/discount/events.py:79]
- `rule_deleted_event` (function) — [saleor/discount/events.py:92]

**`saleor/discount/interface.py`**

- `DiscountInfo` (class) — [saleor/discount/interface.py:22]
- `VoucherInfo` (class) — [saleor/discount/interface.py:42]
- `fetch_voucher_info` (function) — [saleor/discount/interface.py:53]
- `VariantPromotionRuleInfo` (class) — [saleor/discount/interface.py:71]
- `fetch_variant_rules_info` (function) — [saleor/discount/interface.py:79]
- `get_rule_translations` (function) — [saleor/discount/interface.py:115]

**`saleor/discount/models.py`**

- `NotApplicable` (class) — [saleor/discount/models.py:37]
- `VoucherQueryset` (class) — [saleor/discount/models.py:52]
- `active` (function) — [saleor/discount/models.py:53]
- `active_in_channel` (function) — [saleor/discount/models.py:70]
- `expired` (function) — [saleor/discount/models.py:82]
- `Voucher` (class) — [saleor/discount/models.py:99]
- `Meta` (class) — [saleor/discount/models.py:131]
- `code` (function) — [saleor/discount/models.py:135]
- `promo_codes` (function) — [saleor/discount/models.py:141]
- `get_discount` (function) — [saleor/discount/models.py:144]
- `get_discount_amount_for` (function) — [saleor/discount/models.py:171]
- `validate_min_spent` (function) — [saleor/discount/models.py:178]
- `validate_min_checkout_items_quantity` (function) — [saleor/discount/models.py:188]
- `validate_once_per_customer` (function) — [saleor/discount/models.py:200]
- `validate_only_for_staff` (function) — [saleor/discount/models.py:210]
- `VoucherCode` (class) — [saleor/discount/models.py:219]
- `Meta` (class) — [saleor/discount/models.py:229]
- `VoucherChannelListing` (class) — [saleor/discount/models.py:234]
- `Meta` (class) — [saleor/discount/models.py:265]
- `VoucherCustomer` (class) — [saleor/discount/models.py:270]
- `Meta` (class) — [saleor/discount/models.py:279]
- `VoucherTranslation` (class) — [saleor/discount/models.py:287]
- `Meta` (class) — [saleor/discount/models.py:293]
- `get_translated_object_id` (function) — [saleor/discount/models.py:297]
- `get_translated_keys` (function) — [saleor/discount/models.py:300]
- `PromotionQueryset` (class) — [saleor/discount/models.py:304]
- `active` (function) — [saleor/discount/models.py:305]
- `expired` (function) — [saleor/discount/models.py:312]
- `Promotion` (class) — [saleor/discount/models.py:321]
- `Meta` (class) — [saleor/discount/models.py:338]
- `is_active` (function) — [saleor/discount/models.py:351]
- `assign_old_sale_id` (function) — [saleor/discount/models.py:356]
- `PromotionTranslation` (class) — [saleor/discount/models.py:364]
- `Meta` (class) — [saleor/discount/models.py:371]
- `get_translated_object_id` (function) — [saleor/discount/models.py:374]
- `get_translated_keys` (function) — [saleor/discount/models.py:377]
- `PromotionRule` (class) — [saleor/discount/models.py:381]
- `Meta` (class) — [saleor/discount/models.py:416]
- `get_discount` (function) — [saleor/discount/models.py:419]
- `get_old_channel_listing_ids` (function) — [saleor/discount/models.py:432]
- _…and 17 more in this file_

**`saleor/discount/tasks.py`**

- `handle_promotion_toggle` (function) — [saleor/discount/tasks.py:51]
- `get_starting_promotions` (function) — [saleor/discount/tasks.py:136]
- `get_ending_promotions` (function) — [saleor/discount/tasks.py:156]
- `fetch_promotion_variants_and_product_ids` (function) — [saleor/discount/tasks.py:176]
- `clear_promotion_rule_variants_task` (function) — [saleor/discount/tasks.py:197]
- `release_voucher_code_usage_of_draft_orders` (function) — [saleor/discount/tasks.py:221]
- `decrease_voucher_code_usage_of_draft_orders` (function) — [saleor/discount/tasks.py:252]
- `decrease_voucher_codes_usage_task` (function) — [saleor/discount/tasks.py:270]
- `disconnect_voucher_codes_from_draft_orders` (function) — [saleor/discount/tasks.py:293]
- `disconnect_voucher_codes_from_draft_orders_task` (function) — [saleor/discount/tasks.py:306]
- `update_discounted_prices_task` (function) — [saleor/discount/tasks.py:331]
- `set_promotion_rule_variants_task` (function) — [saleor/discount/tasks.py:368]

## How it works

The module's files, as provided to this run:

- `saleor/discount/__init__.py` (100 lines)
- `saleor/discount/error_codes.py` (75 lines)
- `saleor/discount/events.py` (102 lines)
- `saleor/discount/interface.py` (134 lines)
- `saleor/discount/models.py` (651 lines)
- `saleor/discount/tasks.py` (393 lines)

## Interactions

- Imports from: `saleor/plugins/openid_connect`, `saleor/core`, `saleor/graphql/product/types`
- Imported by: `saleor/discount/utils`, `saleor/discount/tests`

Internal dependencies named in the source:

- `..DiscountType`
- `..DiscountValueType`
- `..PromotionEvents`
- `..account.models.User`
- `..app.models.App`
- `..celeryconf.app`
- `..channel.models.Channel`
- `..core.db.connection.allow_writer`
- `..core.db.fields.MoneyField`
- `..core.db.fields.SanitizedJSONField`
- `..core.editorjs.clean_editorjs`
- `..core.models.ModelWithMetadata`
- `..core.utils.json_serializer.CustomJsonEncoder`
- `..core.utils.translations.Translation`
- `..graphql.discount.utils.get_variants_for_catalogue_predicate`
- `..order.OrderStatus`
- `..order.models.Order`
- `..order.models.OrderLine`
- `..permission.enums.DiscountPermissions`
- `..plugins.manager.get_plugins_manager`
- `..product.utils.product.mark_products_in_channels_as_dirty_based_on_rules`
- `..product.utils.variant_prices.update_discounted_prices_for_promotion`
- `..product.utils.variants.fetch_variants_for_promotion_rules`
- `..webhook.event_types.WebhookEventAsyncType`
- `..webhook.utils.get_webhooks_for_event`
- `.models.Promotion`
- `.models.PromotionEvent`
- `.models.PromotionRule`
- `.models.Voucher`
- `.utils.promotion.mark_catalogue_promotion_rules_as_dirty`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7a88d58ffb6e` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
