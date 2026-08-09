## Purpose

`saleor/graphql/order` (`saleor/graphql/order`) groups 9 source file(s) exposing 362 top-level declaration(s).

## Public surface

**`saleor/graphql/order/dataloaders.py`**

- `OrderLinesByVariantIdAndChannelIdLoader` (class) — [saleor/graphql/order/dataloaders.py:42]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:47]
- `OrderByIdLoader` (class) — [saleor/graphql/order/dataloaders.py:69]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:72]
- `OrderByNumberLoader` (class) — [saleor/graphql/order/dataloaders.py:77]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:80]
- `OrdersByUserLoader` (class) — [saleor/graphql/order/dataloaders.py:89]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:92]
- `OrderLineByIdLoader` (class) — [saleor/graphql/order/dataloaders.py:102]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:105]
- `OrderLinesByOrderIdLoader` (class) — [saleor/graphql/order/dataloaders.py:112]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:115]
- `OrderEventsByOrderIdLoader` (class) — [saleor/graphql/order/dataloaders.py:127]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:130]
- `OrderEventsByIdLoader` (class) — [saleor/graphql/order/dataloaders.py:142]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:145]
- `OrderGrantedRefundByIdLoader` (class) — [saleor/graphql/order/dataloaders.py:154]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:157]
- `OrderGrantedRefundsByOrderIdLoader` (class) — [saleor/graphql/order/dataloaders.py:164]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:167]
- `OrderGrantedRefundLinesByOrderGrantedRefundIdLoader` (class) — [saleor/graphql/order/dataloaders.py:178]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:183]
- `AllocationsByOrderLineIdLoader` (class) — [saleor/graphql/order/dataloaders.py:196]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:199]
- `FulfillmentByIdLoader` (class) — [saleor/graphql/order/dataloaders.py:211]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:214]
- `FulfillmentsByOrderIdLoader` (class) — [saleor/graphql/order/dataloaders.py:221]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:224]
- `FulfillmentLinesByIdLoader` (class) — [saleor/graphql/order/dataloaders.py:236]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:239]
- `FulfillmentLinesByFulfillmentIdLoader` (class) — [saleor/graphql/order/dataloaders.py:246]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:249]
- `TransactionItemsByOrderIDLoader` (class) — [saleor/graphql/order/dataloaders.py:267]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:270]
- `TransactionEventsByOrderGrantedRefundIdLoader` (class) — [saleor/graphql/order/dataloaders.py:282]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:287]
- `OrderPromotionCalculateByOrderIdLoaderAndWebhookSyncLoader` (class) — [saleor/graphql/order/dataloaders.py:299]
- `batch_load` (function) — [saleor/graphql/order/dataloaders.py:304]
- `refresh_lines` (function) — [saleor/graphql/order/dataloaders.py:314]
- `calculate_prices` (function) — [saleor/graphql/order/dataloaders.py:334]
- _…and 9 more in this file_

**`saleor/graphql/order/enums.py`**

- `order_event_enum_description` (function) — [saleor/graphql/order/enums.py:22]
- `OrderStatusFilter` (class) — [saleor/graphql/order/enums.py:85]
- `Meta` (class) — [saleor/graphql/order/enums.py:94]

**`saleor/graphql/order/filters.py`**

- `filter_payment_status` (function) — [saleor/graphql/order/filters.py:87]
- `filter_authorize_status` (function) — [saleor/graphql/order/filters.py:96]
- `filter_charge_status` (function) — [saleor/graphql/order/filters.py:102]
- `get_payment_id_from_query` (function) — [saleor/graphql/order/filters.py:108]
- `filter_order_by_payment` (function) — [saleor/graphql/order/filters.py:115]
- `filter_status` (function) — [saleor/graphql/order/filters.py:121]
- `filter_customer` (function) — [saleor/graphql/order/filters.py:165]
- `filter_created_range` (function) — [saleor/graphql/order/filters.py:176]
- `filter_updated_at_range` (function) — [saleor/graphql/order/filters.py:180]
- `filter_order_search` (function) — [saleor/graphql/order/filters.py:184]
- `filter_channels` (function) — [saleor/graphql/order/filters.py:188]
- `filter_checkouts` (function) — [saleor/graphql/order/filters.py:195]
- `filter_is_click_and_collect` (function) — [saleor/graphql/order/filters.py:202]
- `filter_is_preorder` (function) — [saleor/graphql/order/filters.py:211]
- `filter_gift_card_used` (function) — [saleor/graphql/order/filters.py:232]
- `filter_gift_card_bought` (function) — [saleor/graphql/order/filters.py:236]
- `filter_by_gift_card` (function) — [saleor/graphql/order/filters.py:240]
- `filter_order_by_id` (function) — [saleor/graphql/order/filters.py:250]
- `filter_by_order_number` (function) — [saleor/graphql/order/filters.py:264]
- `filter_by_checkout_tokens` (function) — [saleor/graphql/order/filters.py:270]
- `filter_where_has_invoices` (function) — [saleor/graphql/order/filters.py:276]
- `filter_where_invoices` (function) — [saleor/graphql/order/filters.py:285]
- `filter_has_fulfillments` (function) — [saleor/graphql/order/filters.py:301]
- `filter_fulfillments_by_warehouse_details` (function) — [saleor/graphql/order/filters.py:310]
- `filter_fulfillments` (function) — [saleor/graphql/order/filters.py:345]
- `DraftOrderFilter` (class) — [saleor/graphql/order/filters.py:373]
- `Meta` (class) — [saleor/graphql/order/filters.py:379]
- `OrderFilter` (class) — [saleor/graphql/order/filters.py:384]
- `Meta` (class) — [saleor/graphql/order/filters.py:417]
- `is_valid` (function) — [saleor/graphql/order/filters.py:421]
- `OrderStatusEnumFilterInput` (class) — [saleor/graphql/order/filters.py:429]
- `Meta` (class) — [saleor/graphql/order/filters.py:437]
- `OrderAuthorizeStatusEnumFilterInput` (class) — [saleor/graphql/order/filters.py:442]
- `Meta` (class) — [saleor/graphql/order/filters.py:452]
- `OrderChargeStatusEnumFilterInput` (class) — [saleor/graphql/order/filters.py:457]
- `Meta` (class) — [saleor/graphql/order/filters.py:465]
- `InvoiceFilterInput` (class) — [saleor/graphql/order/filters.py:470]
- `Meta` (class) — [saleor/graphql/order/filters.py:475]
- `FulfillmentStatusEnumFilterInput` (class) — [saleor/graphql/order/filters.py:480]
- `Meta` (class) — [saleor/graphql/order/filters.py:488]
- _…and 58 more in this file_

**`saleor/graphql/order/resolvers.py`**

- `resolve_orders` (function) — [saleor/graphql/order/resolvers.py:20]
- `resolve_draft_orders` (function) — [saleor/graphql/order/resolvers.py:45]
- `resolve_orders_total` (function) — [saleor/graphql/order/resolvers.py:58]
- `resolve_order` (function) — [saleor/graphql/order/resolvers.py:90]
- `resolve_homepage_events` (function) — [saleor/graphql/order/resolvers.py:105]
- `resolve_order_by_token` (function) — [saleor/graphql/order/resolvers.py:126]

**`saleor/graphql/order/schema.py`**

- `OrderFilterInput` (class) — [saleor/graphql/order/schema.py:92]
- `Meta` (class) — [saleor/graphql/order/schema.py:101]
- `OrderDraftFilterInput` (class) — [saleor/graphql/order/schema.py:106]
- `Meta` (class) — [saleor/graphql/order/schema.py:107]
- `OrderQueries` (class) — [saleor/graphql/order/schema.py:112]
- `resolve_homepage_events` (function) — [saleor/graphql/order/schema.py:209]
- `resolve_order` (function) — [saleor/graphql/order/schema.py:216]
- `resolve_orders` (function) — [saleor/graphql/order/schema.py:239]
- `resolve_draft_orders` (function) — [saleor/graphql/order/schema.py:255]
- `resolve_orders_total` (function) — [saleor/graphql/order/schema.py:271]
- `resolve_order_by_token` (function) — [saleor/graphql/order/schema.py:275]
- `OrderMutations` (class) — [saleor/graphql/order/schema.py:284]

**`saleor/graphql/order/sorters.py`**

- `OrderSortField` (class) — [saleor/graphql/order/sorters.py:9]
- `Meta` (class) — [saleor/graphql/order/sorters.py:20]
- `description` (function) — [saleor/graphql/order/sorters.py:24]
- `deprecation_reason` (function) — [saleor/graphql/order/sorters.py:43]
- `qs_with_payment` (function) — [saleor/graphql/order/sorters.py:54]
- `OrderSortingInput` (class) — [saleor/graphql/order/sorters.py:65]
- `Meta` (class) — [saleor/graphql/order/sorters.py:66]

**`saleor/graphql/order/types.py`**

- `get_order_discount_event` (function) — [saleor/graphql/order/types.py:188]
- `get_payment_status_for_order` (function) — [saleor/graphql/order/types.py:216]
- `OrderGrantedRefundLine` (class) — [saleor/graphql/order/types.py:240]
- `Meta` (class) — [saleor/graphql/order/types.py:260]
- `resolve_order_line` (function) — [saleor/graphql/order/types.py:268]
- `resolve_reason_reference` (function) — [saleor/graphql/order/types.py:283]
- `wrap_page_with_context` (function) — [saleor/graphql/order/types.py:289]
- `OrderGrantedRefund` (class) — [saleor/graphql/order/types.py:317]
- `Meta` (class) — [saleor/graphql/order/types.py:368]
- `resolve_user` (function) — [saleor/graphql/order/types.py:376]
- `resolve_app` (function) — [saleor/graphql/order/types.py:400]
- `resolve_lines` (function) — [saleor/graphql/order/types.py:407]
- `resolve_transaction_events` (function) — [saleor/graphql/order/types.py:426]
- `resolve_transaction` (function) — [saleor/graphql/order/types.py:437]
- `resolve_reason_reference` (function) — [saleor/graphql/order/types.py:448]
- `wrap_page_with_context` (function) — [saleor/graphql/order/types.py:454]
- `OrderDiscount` (class) — [saleor/graphql/order/types.py:473]
- `Meta` (class) — [saleor/graphql/order/types.py:488]
- `OrderEventDiscountObject` (class) — [saleor/graphql/order/types.py:492]
- `Meta` (class) — [saleor/graphql/order/types.py:506]
- `OrderEventOrderLineObject` (class) — [saleor/graphql/order/types.py:510]
- `Meta` (class) — [saleor/graphql/order/types.py:518]
- `OrderEvent` (class) — [saleor/graphql/order/types.py:522]
- `Meta` (class) — [saleor/graphql/order/types.py:583]
- `resolve_user` (function) — [saleor/graphql/order/types.py:592]
- `resolve_app` (function) — [saleor/graphql/order/types.py:614]
- `resolve_email` (function) — [saleor/graphql/order/types.py:636]
- `resolve_email_type` (function) — [saleor/graphql/order/types.py:640]
- `resolve_amount` (function) — [saleor/graphql/order/types.py:644]
- `resolve_payment_id` (function) — [saleor/graphql/order/types.py:649]
- `resolve_payment_gateway` (function) — [saleor/graphql/order/types.py:653]
- `resolve_quantity` (function) — [saleor/graphql/order/types.py:659]
- `resolve_message` (function) — [saleor/graphql/order/types.py:664]
- `resolve_composed_id` (function) — [saleor/graphql/order/types.py:668]
- `resolve_oversold_items` (function) — [saleor/graphql/order/types.py:672]
- `resolve_order_number` (function) — [saleor/graphql/order/types.py:678]
- `resolve_invoice_number` (function) — [saleor/graphql/order/types.py:689]
- `resolve_lines` (function) — [saleor/graphql/order/types.py:696]
- `resolve_fulfilled_items` (function) — [saleor/graphql/order/types.py:738]
- `resolve_warehouse` (function) — [saleor/graphql/order/types.py:761]
- _…and 129 more in this file_

**`saleor/graphql/order/utils.py`**

- `OrderLineData` (class) — [saleor/graphql/order/utils.py:39]
- `validate_total_quantity` (function) — [saleor/graphql/order/utils.py:48]
- `get_shipping_method_availability_error` (function) — [saleor/graphql/order/utils.py:59]
- `get_valid_shipping_methods` (function) — [saleor/graphql/order/utils.py:68]
- `validate_shipping_method` (function) — [saleor/graphql/order/utils.py:95]
- `append_error` (function) — [saleor/graphql/order/utils.py:146]
- `validate_billing_address` (function) — [saleor/graphql/order/utils.py:153]
- `validate_shipping_address` (function) — [saleor/graphql/order/utils.py:163]
- `validate_order_lines` (function) — [saleor/graphql/order/utils.py:173]
- `validate_variants_is_available` (function) — [saleor/graphql/order/utils.py:208]
- `validate_product_is_published` (function) — [saleor/graphql/order/utils.py:226]
- `validate_product_is_published_in_channel` (function) — [saleor/graphql/order/utils.py:247]
- `validate_variant_channel_listings` (function) — [saleor/graphql/order/utils.py:289]
- `validate_product_is_available_for_purchase` (function) — [saleor/graphql/order/utils.py:308]
- `validate_channel_is_active` (function) — [saleor/graphql/order/utils.py:339]
- `validate_draft_order` (function) — [saleor/graphql/order/utils.py:364]
- `raise_errors` (function) — [saleor/graphql/order/utils.py:418]
- `prepare_insufficient_stock_order_validation_errors` (function) — [saleor/graphql/order/utils.py:425]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/order/schema.py` (328 lines)
- `saleor/graphql/order/types.py` (3205 lines)
- `saleor/graphql/order/__init__.py` (1 lines)
- `saleor/graphql/order/dataloaders.py` (481 lines)
- `saleor/graphql/order/enums.py` (95 lines)
- `saleor/graphql/order/filters.py` (1247 lines)
- `saleor/graphql/order/resolvers.py` (137 lines)
- `saleor/graphql/order/sorters.py` (69 lines)
- `saleor/graphql/order/utils.py` (450 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`, `saleor/core`, `saleor/plugins/openid_connect`
- Imported by: `saleor/graphql/core/federation`, `saleor/graphql/core/tests`

Internal dependencies named in the source:

- `...account.models.Address`
- `...account.models.User`
- `...app.models.App`
- `...channel.models.Channel`
- `...core.anonymize.obfuscate_address`
- `...core.anonymize.obfuscate_email`
- `...core.db.connection.allow_writer_in_context`
- `...core.exceptions.InsufficientStock`
- `...core.exceptions.PermissionDenied`
- `...core.postgres.FlatConcat`
- `...core.prices.quantize_price`
- `...core.search.prefix_search`
- `...core.taxes.zero_money`
- `...discount.DiscountType`
- `...discount.interface.VariantPromotionRuleInfo`
- `...discount.models`
- `...discount.models.NotApplicable`
- `...discount.utils.voucher.validate_voucher_in_order`
- `...giftcard.GiftCardEvents`
- `...giftcard.models.GiftCardEvent`
- `...graphql.checkout.types.DeliveryMethod`
- `...graphql.core.federation.entities.federated_entity`
- `...graphql.order.resolvers.resolve_orders`
- `...graphql.utils.get_user_or_app_from_context`
- `...graphql.warehouse.dataloaders.StockByIdLoader`
- `...graphql.warehouse.dataloaders.WarehouseByIdLoader`
- `...invoice.models.Invoice`
- `...order.OrderOrigin`
- `...order.OrderStatus`
- `...order.delivery_context.get_valid_shipping_methods_for_order`
- `...order.error_codes.OrderErrorCode`
- `...order.events.OrderEvents`
- `...order.models`
- `...order.models.Fulfillment`
- `...order.models.FulfillmentLine`
- `...order.models.FulfillmentStatus`
- `...order.models.Order`
- `...order.models.OrderEvent`
- `...order.models.OrderLine`
- `...order.utils.get_total_quantity`
- `...order.utils.sum_order_totals`
- `...payment.ChargeStatus`
- `...payment.PaymentMethodType`
- `...payment.TransactionKind`
- `...payment.dataloaders.PaymentsByOrderIdLoader`
- `...payment.model_helpers.get_last_payment`
- `...payment.model_helpers.get_total_authorized`
- `...payment.models.Payment`
- `...payment.models.TransactionEvent`
- `...payment.models.TransactionItem`
- `...permission.auth_filters.AuthorizationFilters`
- `...permission.auth_filters.is_app`
- `...permission.auth_filters.is_staff_user`
- `...permission.enums.OrderPermissions`
- `...permission.utils.has_one_of_permissions`
- `...product.models.ALL_PRODUCTS_PERMISSIONS`
- `...product.models.Product`
- `...product.models.ProductChannelListing`
- `...product.models.ProductMedia`
- `...product.models.ProductMediaTypes`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `367fbaf457fc` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
