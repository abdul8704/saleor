## Purpose

`saleor/graphql/discount/mutations/promotion` (`saleor/graphql/discount/mutations/promotion`) groups 9 source file(s) exposing 63 top-level declaration(s).

## Public surface

**`saleor/graphql/discount/mutations/promotion/promotion_bulk_delete.py`**

- `PromotionBulkDelete` (class) — [saleor/graphql/discount/mutations/promotion/promotion_bulk_delete.py:22]
- `Arguments` (class) — [saleor/graphql/discount/mutations/promotion/promotion_bulk_delete.py:23]
- `Meta` (class) — [saleor/graphql/discount/mutations/promotion/promotion_bulk_delete.py:33]
- `bulk_action` (function) — [saleor/graphql/discount/mutations/promotion/promotion_bulk_delete.py:49]
- `get_product_and_channel_map` (function) — [saleor/graphql/discount/mutations/promotion/promotion_bulk_delete.py:61]

**`saleor/graphql/discount/mutations/promotion/promotion_create.py`**

- `PromotionCreateError` (class) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:35]
- `PromotionRuleInput` (class) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:54]
- `Meta` (class) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:65]
- `PromotionInput` (class) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:69]
- `PromotionCreateInput` (class) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:77]
- `Meta` (class) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:89]
- `PromotionCreate` (class) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:93]
- `Arguments` (class) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:94]
- `Meta` (class) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:99]
- `clean_input` (function) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:118]
- `clean_rules` (function) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:143]
- `clean_channels` (function) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:189]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:210]
- `post_save_actions` (function) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:252]
- `has_started` (function) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:266]
- `save_promotion_events` (function) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:281]
- `send_promotion_started_webhook` (function) — [saleor/graphql/discount/mutations/promotion/promotion_create.py:298]

**`saleor/graphql/discount/mutations/promotion/promotion_delete.py`**

- `PromotionDeleteError` (class) — [saleor/graphql/discount/mutations/promotion/promotion_delete.py:21]
- `PromotionDelete` (class) — [saleor/graphql/discount/mutations/promotion/promotion_delete.py:25]
- `Arguments` (class) — [saleor/graphql/discount/mutations/promotion/promotion_delete.py:26]
- `Meta` (class) — [saleor/graphql/discount/mutations/promotion/promotion_delete.py:31]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/promotion/promotion_delete.py:46]

**`saleor/graphql/discount/mutations/promotion/promotion_rule_create.py`**

- `PromotionRuleCreateInput` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_create.py:28]
- `PromotionRuleCreateError` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_create.py:35]
- `PromotionRuleCreate` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_create.py:51]
- `Arguments` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_create.py:52]
- `Meta` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_create.py:57]
- `clean_input` (function) — [saleor/graphql/discount/mutations/promotion/promotion_rule_create.py:72]
- `post_save_action` (function) — [saleor/graphql/discount/mutations/promotion/promotion_rule_create.py:96]

**`saleor/graphql/discount/mutations/promotion/promotion_rule_delete.py`**

- `PromotionRuleDeleteError` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_delete.py:22]
- `PromotionRuleDelete` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_delete.py:26]
- `Arguments` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_delete.py:27]
- `Meta` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_delete.py:32]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/promotion/promotion_rule_delete.py:47]

**`saleor/graphql/discount/mutations/promotion/promotion_rule_update.py`**

- `PromotionRuleUpdateError` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_update.py:29]
- `PromotionRuleUpdateInput` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_update.py:44]
- `PromotionRuleUpdate` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_update.py:67]
- `Arguments` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_update.py:68]
- `Meta` (class) — [saleor/graphql/discount/mutations/promotion/promotion_rule_update.py:76]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/promotion/promotion_rule_update.py:91]
- `clean_input` (function) — [saleor/graphql/discount/mutations/promotion/promotion_rule_update.py:117]
- `post_save_actions` (function) — [saleor/graphql/discount/mutations/promotion/promotion_rule_update.py:160]

**`saleor/graphql/discount/mutations/promotion/promotion_update.py`**

- `PromotionUpdateError` (class) — [saleor/graphql/discount/mutations/promotion/promotion_update.py:31]
- `PromotionUpdateInput` (class) — [saleor/graphql/discount/mutations/promotion/promotion_update.py:35]
- `PromotionUpdate` (class) — [saleor/graphql/discount/mutations/promotion/promotion_update.py:39]
- `Arguments` (class) — [saleor/graphql/discount/mutations/promotion/promotion_update.py:40]
- `Meta` (class) — [saleor/graphql/discount/mutations/promotion/promotion_update.py:46]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/promotion/promotion_update.py:69]
- `clean_input` (function) — [saleor/graphql/discount/mutations/promotion/promotion_update.py:84]
- `post_save_actions` (function) — [saleor/graphql/discount/mutations/promotion/promotion_update.py:98]
- `get_toggle_type` (function) — [saleor/graphql/discount/mutations/promotion/promotion_update.py:114]
- `send_promotion_toggle_webhook` (function) — [saleor/graphql/discount/mutations/promotion/promotion_update.py:152]
- `save_events` (function) — [saleor/graphql/discount/mutations/promotion/promotion_update.py:172]

**`saleor/graphql/discount/mutations/promotion/validators.py`**

- `clean_promotion_rule` (function) — [saleor/graphql/discount/mutations/promotion/validators.py:15]
- `clean_predicate` (function) — [saleor/graphql/discount/mutations/promotion/validators.py:502]
- `clean_fixed_discount_value` (function) — [saleor/graphql/discount/mutations/promotion/validators.py:537]
- `clean_percentage_discount_value` (function) — [saleor/graphql/discount/mutations/promotion/validators.py:550]
- `get_from_input_or_instance` (function) — [saleor/graphql/discount/mutations/promotion/validators.py:561]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/discount/mutations/promotion/__init__.py` (1 lines)
- `saleor/graphql/discount/mutations/promotion/promotion_bulk_delete.py` (67 lines)
- `saleor/graphql/discount/mutations/promotion/promotion_create.py` (306 lines)
- `saleor/graphql/discount/mutations/promotion/promotion_delete.py` (62 lines)
- `saleor/graphql/discount/mutations/promotion/promotion_rule_create.py` (114 lines)
- `saleor/graphql/discount/mutations/promotion/promotion_rule_delete.py` (77 lines)
- `saleor/graphql/discount/mutations/promotion/promotion_rule_update.py` (183 lines)
- `saleor/graphql/discount/mutations/promotion/promotion_update.py` (183 lines)
- `saleor/graphql/discount/mutations/promotion/validators.py` (566 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....channel.models`
- `.....discount.PromotionType`
- `.....discount.RewardType`
- `.....discount.RewardValueType`
- `.....discount.events`
- `.....discount.models`
- `.....discount.models.PromotionRule`
- `.....discount.utils.promotion.get_current_products_for_rules`
- `.....discount.utils.promotion.mark_catalogue_promotion_rules_as_dirty`
- `.....graphql.core.mutations.ModelDeleteMutation`
- `.....permission.enums.DiscountPermissions`
- `.....plugins.manager.PluginsManager`
- `.....product.utils.product.mark_products_in_channels_as_dirty`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.utils.get_webhooks_for_event`
- `....app.dataloaders.get_app_promise`
- `....channel.types.Channel`
- `....core.ResolveInfo`
- `....core.descriptions.PREVIEW_FEATURE`
- `....core.doc_category.DOC_CATEGORY_DISCOUNTS`
- `....core.mutations.DeprecatedModelMutation`
- `....core.mutations.ModelBulkDeleteMutation`
- `....core.scalars.DateTime`
- `....core.scalars.JSON`
- `....core.types.BaseInputObjectType`
- `....core.types.DiscountError`
- `....core.types.Error`
- `....core.types.NonNullList`
- `....core.utils.WebhookEventInfo`
- `....core.validators.validate_end_is_after_start`
- `....core.validators.validate_price_precision`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `....utils.get_nodes`
- `....utils.validators.check_for_duplicates`
- `...enums.PromotionCreateErrorCode`
- `...enums.PromotionDeleteErrorCode`
- `...enums.PromotionRuleCreateErrorCode`
- `...enums.PromotionRuleDeleteErrorCode`
- `...enums.PromotionRuleUpdateErrorCode`
- `...enums.PromotionTypeEnum`
- `...enums.PromotionUpdateErrorCode`
- `...inputs.PromotionRuleBaseInput`
- `...types.Promotion`
- `...types.PromotionRule`
- `...utils.get_products_for_rule`
- `..utils.clear_promotion_old_sale_id`
- `..utils.promotion_rule_should_be_marked_with_dirty_variants`
- `.promotion_create.PromotionInput`
- `.promotion_create.PromotionRuleInput`
- `.validators.clean_promotion_rule`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `17b13789b6b7` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
