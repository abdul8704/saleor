## Purpose

`saleor/graphql/giftcard/bulk_mutations` (`saleor/graphql/giftcard/bulk_mutations`) groups 5 source file(s) exposing 25 top-level declaration(s).

## Public surface

**`saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_activate.py`**

- `GiftCardBulkActivate` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_activate.py:20]
- `Arguments` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_activate.py:21]
- `Meta` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_activate.py:26]
- `clean_instance` (function) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_activate.py:40]
- `bulk_action` (function) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_activate.py:49]

**`saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py`**

- `GiftCardBulkCreateInput` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:28]
- `Meta` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:42]
- `GiftCardBulkCreate` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:46]
- `Arguments` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:59]
- `Meta` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:64]
- `perform_mutation` (function) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:83]
- `clean_count_value` (function) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:101]
- `clean_expiry_date` (function) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:113]
- `clean_balance` (function) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:126]
- `create_instances` (function) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:149]
- `assign_gift_card_tags` (function) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:163]
- `call_gift_card_created_on_plugins` (function) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py:176]

**`saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_deactivate.py`**

- `GiftCardBulkDeactivate` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_deactivate.py:17]
- `Arguments` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_deactivate.py:18]
- `Meta` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_deactivate.py:25]
- `bulk_action` (function) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_deactivate.py:40]

**`saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_delete.py`**

- `GiftCardBulkDelete` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_delete.py:16]
- `Arguments` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_delete.py:17]
- `Meta` (class) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_delete.py:27]
- `bulk_action` (function) — [saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_delete.py:42]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_activate.py` (62 lines)
- `saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_deactivate.py` (53 lines)
- `saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_delete.py` (48 lines)
- `saleor/graphql/giftcard/bulk_mutations/__init__.py` (11 lines)
- `saleor/graphql/giftcard/bulk_mutations/gift_card_bulk_create.py` (179 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: `saleor/graphql/giftcard/tests/bulk_mutations`

Internal dependencies named in the source:

- `....core.tracing.traced_atomic_transaction`
- `....core.utils.promo_code.generate_promo_code`
- `....core.utils.validators.is_date_in_future`
- `....giftcard.error_codes.GiftCardErrorCode`
- `....giftcard.events`
- `....giftcard.models`
- `....giftcard.utils.is_gift_card_expired`
- `....permission.enums.GiftcardPermissions`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.utils.get_webhooks_for_event`
- `...app.dataloaders.get_app_promise`
- `...core.ResolveInfo`
- `...core.doc_category.DOC_CATEGORY_GIFT_CARDS`
- `...core.mutations.BaseBulkMutation`
- `...core.mutations.BaseMutation`
- `...core.mutations.ModelBulkDeleteMutation`
- `...core.scalars.Date`
- `...core.types.BaseInputObjectType`
- `...core.types.GiftCardError`
- `...core.types.NonNullList`
- `...core.types.PriceInput`
- `...core.utils.WebhookEventInfo`
- `...core.validators.validate_price_precision`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `..mutations.GiftCardCreate`
- `..types.GiftCard`
- `.gift_card_bulk_activate.GiftCardBulkActivate`
- `.gift_card_bulk_create.GiftCardBulkCreate`
- `.gift_card_bulk_deactivate.GiftCardBulkDeactivate`
- `.gift_card_bulk_delete.GiftCardBulkDelete`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b0162ca61612` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
