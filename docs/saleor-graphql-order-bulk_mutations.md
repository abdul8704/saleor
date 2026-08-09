## Purpose

`saleor/graphql/order/bulk_mutations` (`saleor/graphql/order/bulk_mutations`) groups 5 source file(s) exposing 101 top-level declaration(s).

## Public surface

**`saleor/graphql/order/bulk_mutations/draft_orders.py`**

- `DraftOrderBulkDelete` (class) — [saleor/graphql/order/bulk_mutations/draft_orders.py:24]
- `Arguments` (class) — [saleor/graphql/order/bulk_mutations/draft_orders.py:27]
- `Meta` (class) — [saleor/graphql/order/bulk_mutations/draft_orders.py:37]
- `get_ids_with_related_objects` (function) — [saleor/graphql/order/bulk_mutations/draft_orders.py:47]
- `clean_instance` (function) — [saleor/graphql/order/bulk_mutations/draft_orders.py:63]
- `clean_input` (function) — [saleor/graphql/order/bulk_mutations/draft_orders.py:87]
- `get_channel_ids` (function) — [saleor/graphql/order/bulk_mutations/draft_orders.py:123]
- `perform_mutation` (function) — [saleor/graphql/order/bulk_mutations/draft_orders.py:128]
- `DraftOrderLinesBulkDelete` (class) — [saleor/graphql/order/bulk_mutations/draft_orders.py:161]
- `Arguments` (class) — [saleor/graphql/order/bulk_mutations/draft_orders.py:164]
- `Meta` (class) — [saleor/graphql/order/bulk_mutations/draft_orders.py:174]
- `clean_instance` (function) — [saleor/graphql/order/bulk_mutations/draft_orders.py:184]
- `get_channel_ids` (function) — [saleor/graphql/order/bulk_mutations/draft_orders.py:196]

**`saleor/graphql/order/bulk_mutations/order_bulk_cancel.py`**

- `OrderBulkCancel` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_cancel.py:20]
- `Arguments` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_cancel.py:21]
- `Meta` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_cancel.py:26]
- `clean_instance` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_cancel.py:35]
- `bulk_action` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_cancel.py:39]
- `get_channel_ids` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_cancel.py:56]

**`saleor/graphql/order/bulk_mutations/order_bulk_create.py`**

- `OrderBulkError` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:90]
- `OrderBulkFulfillmentLine` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:97]
- `OrderBulkFulfillment` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:103]
- `OrderBulkOrderLine` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:109]
- `OrderBulkTransaction` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:116]
- `OrderBulkCreateData` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:122]
- `set_fulfillment_id` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:141]
- `set_quantity_fulfilled` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:146]
- `set_fulfillment_order` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:151]
- `set_transaction_id` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:157]
- `link_gift_cards` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:162]
- `post_create_order_update` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:166]
- `all_order_lines` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:172]
- `all_order_line_discounts` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:176]
- `all_fulfillment_lines` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:184]
- `all_transactions` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:192]
- `all_transaction_events` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:196]
- `all_invoices` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:204]
- `all_discounts` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:208]
- `orderline_fulfillmentlines_map` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:212]
- `orderline_quantityfulfilled_map` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:222]
- `unique_variant_ids` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:237]
- `unique_warehouse_ids` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:247]
- `total_order_quantity` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:251]
- `total_fulfillment_quantity` (function) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:255]
- `DeliveryMethod` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:264]
- `OrderAmounts` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:277]
- `LineAmounts` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:290]
- `ModelIdentifier` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:310]
- `ModelIdentifiers` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:316]
- `TaxedMoneyInput` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:361]
- `Meta` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:365]
- `OrderBulkCreateUserInput` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:369]
- `Meta` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:376]
- `OrderBulkCreateInvoiceInput` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:380]
- `Meta` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:397]
- `OrderBulkCreateDeliveryMethodInput` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:401]
- `Meta` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:425]
- `OrderBulkCreateNoteInput` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:429]
- `Meta` (class) — [saleor/graphql/order/bulk_mutations/order_bulk_create.py:441]
- _…and 41 more in this file_

**`saleor/graphql/order/bulk_mutations/utils.py`**

- `get_instance` (function) — [saleor/graphql/order/bulk_mutations/utils.py:10]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/order/bulk_mutations/__init__.py` (1 lines)
- `saleor/graphql/order/bulk_mutations/draft_orders.py` (203 lines)
- `saleor/graphql/order/bulk_mutations/order_bulk_cancel.py` (58 lines)
- `saleor/graphql/order/bulk_mutations/order_bulk_create.py` (2519 lines)
- `saleor/graphql/order/bulk_mutations/utils.py` (91 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/plugins/openid_connect`, `saleor/core`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.models.Address`
- `....account.models.User`
- `....account.utils.update_user_orders_count`
- `....app.models.App`
- `....channel.models`
- `....channel.models.Channel`
- `....core.JobStatus`
- `....core.prices.quantize_price`
- `....core.tracing.traced_atomic_transaction`
- `....core.utils.url.validate_storefront_url`
- `....core.weight.zero_weight`
- `....discount.tasks.release_voucher_code_usage_of_draft_orders`
- `....discount.utils.manual_discount.apply_discount_to_value`
- `....discount.utils.voucher.get_customer_email_for_voucher_usage`
- `....giftcard.models.GiftCard`
- `....invoice.models.Invoice`
- `....order.OrderStatus`
- `....order.actions.WEBHOOK_EVENTS_FOR_ORDER_CANCELED`
- `....order.actions.cancel_order`
- `....order.error_codes.OrderBulkCreateErrorCode`
- `....order.error_codes.OrderErrorCode`
- `....order.models`
- `....order.models.Fulfillment`
- `....order.models.FulfillmentLine`
- `....order.models.Order`
- `....order.models.OrderEvent`
- `....order.models.OrderLine`
- `....order.search.update_order_search_vector`
- `....order.utils.update_order_display_gross_prices`
- `....order.utils.updates_amounts_for_order`
- `....payment.TransactionEventType`
- `....payment.models.Payment`
- `....payment.models.TransactionEvent`
- `....payment.models.TransactionItem`
- `....permission.enums.OrderPermissions`
- `....product.models.Product`
- `....product.models.ProductVariant`
- `....shipping.models.ShippingMethod`
- `....shipping.models.ShippingMethodChannelListing`
- `....tax.models.TaxClass`
- `....tax.models.TaxConfiguration`
- `....warehouse.management.stock_bulk_update`
- `....warehouse.models.Stock`
- `....warehouse.models.Warehouse`
- `....webhook.utils.get_webhooks_for_multiple_events`
- `...account.i18n.I18nMixin`
- `...account.types.AddressInput`
- `...app.dataloaders.get_app_promise`
- `...core.ResolveInfo`
- `...core.context.SyncWebhookControlContext`
- `...core.doc_category.DOC_CATEGORY_ORDERS`
- `...core.enums.ErrorPolicy`
- `...core.enums.ErrorPolicyEnum`
- `...core.enums.LanguageCodeEnum`
- `...core.mutations.BaseBulkWithRestrictedChannelAccessMutation`
- `...core.mutations.BaseMutation`
- `...core.scalars.DateTime`
- `...core.scalars.PositiveDecimal`
- `...core.scalars.WeightScalar`
- `...core.types.BaseInputObjectType`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `ab486710f834` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
