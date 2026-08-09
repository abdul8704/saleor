## Purpose

`saleor/order` (`saleor/order`) groups 15 source file(s) exposing 303 top-level declaration(s).

## Public surface

**`saleor/order/__init__.py`**

- `OrderStatus` (class) — [saleor/order/__init__.py:9]
- `OrderOrigin` (class) — [saleor/order/__init__.py:43]
- `FulfillmentStatus` (class) — [saleor/order/__init__.py:57]
- `OrderEvents` (class) — [saleor/order/__init__.py:81]
- `OrderEventsEmails` (class) — [saleor/order/__init__.py:210]
- `OrderAuthorizeStatus` (class) — [saleor/order/__init__.py:234]
- `OrderChargeStatus` (class) — [saleor/order/__init__.py:269]
- `FulfillmentLineData` (class) — [saleor/order/__init__.py:304]
- `StockUpdatePolicy` (class) — [saleor/order/__init__.py:312]
- `OrderGrantedRefundStatus` (class) — [saleor/order/__init__.py:331]

**`saleor/order/actions.py`**

- `OrderFulfillmentLineInfo` (class) — [saleor/order/actions.py:90]
- `call_order_events` (function) — [saleor/order/actions.py:245]
- `call_order_event` (function) — [saleor/order/actions.py:267]
- `order_created` (function) — [saleor/order/actions.py:287]
- `order_confirmed` (function) — [saleor/order/actions.py:356]
- `handle_fully_paid_order` (function) — [saleor/order/actions.py:383]
- `cancel_order` (function) — [saleor/order/actions.py:422]
- `order_refunded` (function) — [saleor/order/actions.py:457]
- `order_voided` (function) — [saleor/order/actions.py:526]
- `order_returned` (function) — [saleor/order/actions.py:537]
- `order_fulfilled` (function) — [saleor/order/actions.py:547]
- `order_awaits_fulfillment_approval` (function) — [saleor/order/actions.py:630]
- `order_authorized` (function) — [saleor/order/actions.py:644]
- `order_charged` (function) — [saleor/order/actions.py:664]
- `order_transaction_updated` (function) — [saleor/order/actions.py:716]
- `fulfillment_tracking_updated` (function) — [saleor/order/actions.py:786]
- `cancel_fulfillment` (function) — [saleor/order/actions.py:808]
- `decrease_fulfilled_quantity` (function) — [saleor/order/actions.py:854]
- `approve_fulfillment` (function) — [saleor/order/actions.py:864]
- `mark_order_as_paid_with_transaction` (function) — [saleor/order/actions.py:945]
- `mark_order_as_paid_with_payment` (function) — [saleor/order/actions.py:986]
- `clean_mark_order_as_paid` (function) — [saleor/order/actions.py:1054]
- `fulfill_order_lines` (function) — [saleor/order/actions.py:1076]
- `create_fulfillments` (function) — [saleor/order/actions.py:1223]
- `create_refund_fulfillment` (function) — [saleor/order/actions.py:1525]
- `create_replace_order` (function) — [saleor/order/actions.py:1625]
- `create_return_fulfillment` (function) — [saleor/order/actions.py:1796]
- `process_replace` (function) — [saleor/order/actions.py:1857]
- `create_fulfillments_for_returned_products` (function) — [saleor/order/actions.py:1909]

**`saleor/order/base_calculations.py`**

- `base_order_shipping` (function) — [saleor/order/base_calculations.py:20]
- `base_order_subtotal` (function) — [saleor/order/base_calculations.py:24]
- `base_order_total` (function) — [saleor/order/base_calculations.py:42]
- `base_order_line_total` (function) — [saleor/order/base_calculations.py:60]
- `propagate_order_discount_on_order_prices` (function) — [saleor/order/base_calculations.py:85]
- `calculate_prices` (function) — [saleor/order/base_calculations.py:169]
- `propagate_order_discount_on_order_lines_prices` (function) — [saleor/order/base_calculations.py:215]
- `get_total_price_with_subtotal_discount_for_order_line` (function) — [saleor/order/base_calculations.py:266]
- `apply_subtotal_discount_to_order_lines` (function) — [saleor/order/base_calculations.py:280]
- `assign_order_line_prices` (function) — [saleor/order/base_calculations.py:293]
- `assign_order_prices` (function) — [saleor/order/base_calculations.py:311]
- `undiscounted_order_shipping` (function) — [saleor/order/base_calculations.py:334]
- `undiscounted_order_subtotal` (function) — [saleor/order/base_calculations.py:345]
- `undiscounted_order_total` (function) — [saleor/order/base_calculations.py:355]

**`saleor/order/calculations.py`**

- `should_refresh_prices` (function) — [saleor/order/calculations.py:70]
- `prepare_order_lines_for_refresh` (function) — [saleor/order/calculations.py:90]
- `process_order_promotion` (function) — [saleor/order/calculations.py:106]
- `process_order_prices` (function) — [saleor/order/calculations.py:117]
- `process_calculation_result` (function) — [saleor/order/calculations.py:124]
- `fetch_order_prices_if_expired` (function) — [saleor/order/calculations.py:192]
- `get_expired_line_ids` (function) — [saleor/order/calculations.py:242]
- `promise_calculate_taxes_with_error_handling` (function) — [saleor/order/calculations.py:256]
- `process_error` (function) — [saleor/order/calculations.py:266]
- `calculate_taxes` (function) — [saleor/order/calculations.py:288]
- `remove_tax_if_needed` (function) — [saleor/order/calculations.py:304]
- `process_flat_taxes` (function) — [saleor/order/calculations.py:350]
- `recalculate_with_tax_app_data` (function) — [saleor/order/calculations.py:373]
- `recalculate_with_plugins` (function) — [saleor/order/calculations.py:397]
- `recalculate_with_tax_app_data` (function) — [saleor/order/calculations.py:415]
- `process_error` (function) — [saleor/order/calculations.py:440]
- `process_response` (function) — [saleor/order/calculations.py:445]
- `remove_tax` (function) — [saleor/order/calculations.py:615]
- `refresh_order_base_prices_and_discounts` (function) — [saleor/order/calculations.py:677]
- `refresh_all_order_base_prices_and_discounts` (function) — [saleor/order/calculations.py:764]
- `order_line_unit` (function) — [saleor/order/calculations.py:770]
- `process_result` (function) — [saleor/order/calculations.py:788]
- `order_line_total` (function) — [saleor/order/calculations.py:807]
- `process_result` (function) — [saleor/order/calculations.py:825]
- `order_line_tax_rate` (function) — [saleor/order/calculations.py:844]
- `process_result` (function) — [saleor/order/calculations.py:861]
- `order_line_unit_discount` (function) — [saleor/order/calculations.py:877]
- `process_result` (function) — [saleor/order/calculations.py:898]
- `order_line_unit_discount_value` (function) — [saleor/order/calculations.py:913]
- `process_result` (function) — [saleor/order/calculations.py:929]
- `order_line_unit_discount_type` (function) — [saleor/order/calculations.py:944]
- `process_result` (function) — [saleor/order/calculations.py:960]
- `order_undiscounted_shipping` (function) — [saleor/order/calculations.py:975]
- `process_result` (function) — [saleor/order/calculations.py:992]
- `order_shipping` (function) — [saleor/order/calculations.py:1007]
- `process_result` (function) — [saleor/order/calculations.py:1024]
- `order_shipping_tax_rate` (function) — [saleor/order/calculations.py:1039]
- `process_result` (function) — [saleor/order/calculations.py:1055]
- `order_subtotal` (function) — [saleor/order/calculations.py:1070]
- `process_result` (function) — [saleor/order/calculations.py:1087]
- _…and 4 more in this file_

**`saleor/order/delivery_context.py`**

- `get_all_shipping_methods_for_order` (function) — [saleor/order/delivery_context.py:30]
- `get_valid_shipping_methods_for_order` (function) — [saleor/order/delivery_context.py:71]
- `handle_excluded_methods` (function) — [saleor/order/delivery_context.py:105]
- `get_external_shipping_id` (function) — [saleor/order/delivery_context.py:112]
- `is_shipping_required` (function) — [saleor/order/delivery_context.py:118]
- `get_valid_collection_points_for_order` (function) — [saleor/order/delivery_context.py:122]

**`saleor/order/error_codes.py`**

- `OrderErrorCode` (class) — [saleor/order/error_codes.py:4]
- `OrderGrantRefundCreateErrorCode` (class) — [saleor/order/error_codes.py:44]
- `OrderGrantRefundUpdateErrorCode` (class) — [saleor/order/error_codes.py:54]
- `OrderGrantRefundCreateLineErrorCode` (class) — [saleor/order/error_codes.py:64]
- `OrderGrantRefundUpdateLineErrorCode` (class) — [saleor/order/error_codes.py:72]
- `OrderBulkCreateErrorCode` (class) — [saleor/order/error_codes.py:80]
- `OrderNoteAddErrorCode` (class) — [saleor/order/error_codes.py:101]
- `OrderNoteUpdateErrorCode` (class) — [saleor/order/error_codes.py:106]

**`saleor/order/events.py`**

- `event_transaction_charge_requested` (function) — [saleor/order/events.py:37]
- `event_transaction_refund_requested` (function) — [saleor/order/events.py:56]
- `event_transaction_cancel_requested` (function) — [saleor/order/events.py:75]
- `event_order_refunded_notification` (function) — [saleor/order/events.py:89]
- `event_order_confirmed_notification` (function) — [saleor/order/events.py:104]
- `event_order_cancelled_notification` (function) — [saleor/order/events.py:119]
- `event_order_confirmation_notification` (function) — [saleor/order/events.py:134]
- `event_fulfillment_confirmed_notification` (function) — [saleor/order/events.py:148]
- `event_payment_confirmed_notification` (function) — [saleor/order/events.py:163]
- `invoice_requested_event` (function) — [saleor/order/events.py:174]
- `invoice_generated_event` (function) — [saleor/order/events.py:185]
- `invoice_updated_event` (function) — [saleor/order/events.py:201]
- `event_invoice_sent_notification` (function) — [saleor/order/events.py:219]
- `email_resent_event` (function) — [saleor/order/events.py:231]
- `draft_order_created_event` (function) — [saleor/order/events.py:237]
- `order_added_products_event` (function) — [saleor/order/events.py:245]
- `order_removed_products_event` (function) — [saleor/order/events.py:267]
- `draft_order_created_from_replace_event` (function) — [saleor/order/events.py:289]
- `order_created_event` (function) — [saleor/order/events.py:310]
- `order_confirmed_event` (function) — [saleor/order/events.py:333]
- `order_canceled_event` (function) — [saleor/order/events.py:341]
- `order_manually_marked_as_paid_event` (function) — [saleor/order/events.py:349]
- `order_fully_paid_event` (function) — [saleor/order/events.py:368]
- `order_replacement_created` (function) — [saleor/order/events.py:387]
- `payment_authorized_event` (function) — [saleor/order/events.py:404]
- `payment_captured_event` (function) — [saleor/order/events.py:421]
- `payment_refunded_event` (function) — [saleor/order/events.py:438]
- `payment_voided_event` (function) — [saleor/order/events.py:455]
- `payment_failed_event` (function) — [saleor/order/events.py:467]
- `transaction_mark_order_as_paid_failed_event` (function) — [saleor/order/events.py:489]
- `transaction_event` (function) — [saleor/order/events.py:503]
- `external_notification_event` (function) — [saleor/order/events.py:521]
- `fulfillment_canceled_event` (function) — [saleor/order/events.py:541]
- `fulfillment_restocked_items_event` (function) — [saleor/order/events.py:557]
- `fulfillment_fulfilled_items_event` (function) — [saleor/order/events.py:577]
- `fulfillment_awaits_approval_event` (function) — [saleor/order/events.py:597]
- `order_returned_event` (function) — [saleor/order/events.py:613]
- `fulfillment_replaced_event` (function) — [saleor/order/events.py:634]
- `fulfillment_refunded_event` (function) — [saleor/order/events.py:650]
- `fulfillment_tracking_updated_event` (function) — [saleor/order/events.py:675]
- _…and 13 more in this file_

**`saleor/order/fetch.py`**

- `OrderInfo` (class) — [saleor/order/fetch.py:35]
- `OrderLineInfo` (class) — [saleor/order/fetch.py:44]
- `fetch_order_info` (function) — [saleor/order/fetch.py:53]
- `fetch_order_lines` (function) — [saleor/order/fetch.py:65]
- `EditableOrderLineInfo` (class) — [saleor/order/fetch.py:82]
- `variant_discounted_price` (function) — [saleor/order/fetch.py:90]
- `get_manual_line_discount` (function) — [saleor/order/fetch.py:101]
- `fetch_draft_order_lines_info` (function) — [saleor/order/fetch.py:110]
- `attach_voucher_info` (function) — [saleor/order/fetch.py:186]
- `reattach_apply_once_per_order_voucher_info` (function) — [saleor/order/fetch.py:202]

**`saleor/order/interface.py`**

- `OrderTaxedPricesData` (class) — [saleor/order/interface.py:7]

**`saleor/order/lock_objects.py`**

- `order_lines_qs_select_for_update` (function) — [saleor/order/lock_objects.py:6]
- `order_qs_select_for_update` (function) — [saleor/order/lock_objects.py:10]

**`saleor/order/models.py`**

- `OrderQueryset` (class) — [saleor/order/models.py:48]
- `get_by_checkout_token` (function) — [saleor/order/models.py:49]
- `confirmed` (function) — [saleor/order/models.py:53]
- `non_draft` (function) — [saleor/order/models.py:57]
- `drafts` (function) — [saleor/order/models.py:61]
- `ready_to_fulfill` (function) — [saleor/order/models.py:65]
- `ready_to_capture` (function) — [saleor/order/models.py:79]
- `ready_to_confirm` (function) — [saleor/order/models.py:94]
- `get_order_number` (function) — [saleor/order/models.py:102]
- `Order` (class) — [saleor/order/models.py:109]
- `Meta` (class) — [saleor/order/models.py:373]
- `is_fully_paid` (function) — [saleor/order/models.py:416]
- `is_partly_paid` (function) — [saleor/order/models.py:419]
- `get_customer_email` (function) — [saleor/order/models.py:422]
- `get_last_payment` (function) — [saleor/order/models.py:435]
- `is_pre_authorized` (function) — [saleor/order/models.py:439]
- `is_captured` (function) — [saleor/order/models.py:450]
- `get_subtotal` (function) — [saleor/order/models.py:461]
- `is_shipping_required` (function) — [saleor/order/models.py:464]
- `get_total_quantity` (function) — [saleor/order/models.py:472]
- `is_draft` (function) — [saleor/order/models.py:475]
- `is_unconfirmed` (function) — [saleor/order/models.py:478]
- `is_expired` (function) — [saleor/order/models.py:481]
- `is_open` (function) — [saleor/order/models.py:484]
- `can_cancel` (function) — [saleor/order/models.py:488]
- `can_capture` (function) — [saleor/order/models.py:506]
- `can_void` (function) — [saleor/order/models.py:518]
- `can_refund` (function) — [saleor/order/models.py:525]
- `can_mark_as_paid` (function) — [saleor/order/models.py:532]
- `total_balance` (function) — [saleor/order/models.py:538]
- `OrderLine` (class) — [saleor/order/models.py:542]
- `Meta` (class) — [saleor/order/models.py:731]
- `quantity_unfulfilled` (function) — [saleor/order/models.py:747]
- `Fulfillment` (class) — [saleor/order/models.py:751]
- `Meta` (class) — [saleor/order/models.py:789]
- `save` (function) — [saleor/order/models.py:807]
- `composed_id` (function) — [saleor/order/models.py:817]
- `can_edit` (function) — [saleor/order/models.py:820]
- `get_total_quantity` (function) — [saleor/order/models.py:823]
- `is_tracking_number_url` (function) — [saleor/order/models.py:827]
- _…and 8 more in this file_

**`saleor/order/notifications.py`**

- `AttributeData` (class) — [saleor/order/notifications.py:37]
- `get_attribute_data_from_order_lines` (function) — [saleor/order/notifications.py:44]
- `get_image_payload` (function) — [saleor/order/notifications.py:88]
- `get_default_images_payload` (function) — [saleor/order/notifications.py:100]
- `get_product_attributes_payload` (function) — [saleor/order/notifications.py:111]
- `get_product_payload` (function) — [saleor/order/notifications.py:159]
- `get_product_variant_payload` (function) — [saleor/order/notifications.py:170]
- `get_order_line_payload` (function) — [saleor/order/notifications.py:183]
- `get_lines_payload` (function) — [saleor/order/notifications.py:223]
- `get_address_payload` (function) — [saleor/order/notifications.py:247]
- `get_discounts_payload` (function) — [saleor/order/notifications.py:256]
- `get_custom_order_payload` (function) — [saleor/order/notifications.py:305]
- `get_default_order_payload` (function) — [saleor/order/notifications.py:314]
- `get_default_fulfillment_line_payload` (function) — [saleor/order/notifications.py:366]
- `get_default_fulfillment_payload` (function) — [saleor/order/notifications.py:376]
- `prepare_order_details_url` (function) — [saleor/order/notifications.py:403]
- `send_order_confirmation` (function) — [saleor/order/notifications.py:408]
- `send_order_confirmed` (function) — [saleor/order/notifications.py:450]
- `send_fulfillment_confirmation_to_customer` (function) — [saleor/order/notifications.py:470]
- `send_fulfillment_update` (function) — [saleor/order/notifications.py:485]
- `send_payment_confirmation` (function) — [saleor/order/notifications.py:496]
- `send_order_canceled_confirmation` (function) — [saleor/order/notifications.py:532]
- `send_order_refunded_confirmation` (function) — [saleor/order/notifications.py:552]
- `attach_requester_payload_data` (function) — [saleor/order/notifications.py:579]

**`saleor/order/search.py`**

- `update_order_search_vector` (function) — [saleor/order/search.py:15]
- `prepare_order_search_vector_value` (function) — [saleor/order/search.py:23]
- `generate_order_transactions_search_vector_value` (function) — [saleor/order/search.py:96]
- `generate_order_payments_search_vector_value` (function) — [saleor/order/search.py:132]
- `generate_order_discounts_search_vector_value` (function) — [saleor/order/search.py:155]
- `generate_order_lines_search_vector_value` (function) — [saleor/order/search.py:181]
- `generate_order_invoices_search_vector_value` (function) — [saleor/order/search.py:229]
- `generate_order_events_search_vector_value` (function) — [saleor/order/search.py:246]

**`saleor/order/tasks.py`**

- `recalculate_orders_task` (function) — [saleor/order/tasks.py:40]
- `send_order_updated` (function) — [saleor/order/tasks.py:51]
- `expire_orders_task` (function) — [saleor/order/tasks.py:175]
- `delete_expired_orders_task` (function) — [saleor/order/tasks.py:183]
- `reduce_user_number_of_orders` (function) — [saleor/order/tasks.py:230]

**`saleor/order/utils.py`**

- `get_order_country` (function) — [saleor/order/utils.py:82]
- `get_voucher_discount_assigned_to_order` (function) — [saleor/order/utils.py:89]
- `invalidate_order_prices` (function) — [saleor/order/utils.py:93]
- `recalculate_order_weight` (function) — [saleor/order/utils.py:111]
- `refresh_order_status` (function) — [saleor/order/utils.py:159]
- `update_order_status` (function) — [saleor/order/utils.py:192]
- `determine_order_status` (function) — [saleor/order/utils.py:210]
- `create_order_line` (function) — [saleor/order/utils.py:230]
- `add_variant_to_order` (function) — [saleor/order/utils.py:356]
- `update_line_base_unit_prices_with_custom_price` (function) — [saleor/order/utils.py:410]
- `add_gift_cards_to_order` (function) — [saleor/order/utils.py:443]
- `update_gift_card_balance` (function) — [saleor/order/utils.py:498]
- `set_gift_card_user` (function) — [saleor/order/utils.py:514]
- `change_order_line_quantity` (function) — [saleor/order/utils.py:559]
- `create_order_event` (function) — [saleor/order/utils.py:634]
- `delete_order_line` (function) — [saleor/order/utils.py:653]
- `restock_fulfillment_lines` (function) — [saleor/order/utils.py:662]
- `sum_order_totals` (function) — [saleor/order/utils.py:677]
- `get_total_quantity` (function) — [saleor/order/utils.py:685]
- `get_discounted_lines` (function) — [saleor/order/utils.py:689]
- `match_orders_with_new_user` (function) — [saleor/order/utils.py:713]
- `get_total_order_discount` (function) — [saleor/order/utils.py:717]
- `get_total_order_discount_excluding_shipping` (function) — [saleor/order/utils.py:728]
- `get_order_discounts` (function) — [saleor/order/utils.py:744]
- `create_manual_order_discount` (function) — [saleor/order/utils.py:749]
- `remove_order_discount_from_order` (function) — [saleor/order/utils.py:787]
- `update_discount_for_order_line` (function) — [saleor/order/utils.py:799]
- `remove_discount_from_order_line` (function) — [saleor/order/utils.py:920]
- `update_order_charge_status` (function) — [saleor/order/utils.py:954]
- `update_order_charge_data` (function) — [saleor/order/utils.py:993]
- `update_order_authorize_status` (function) — [saleor/order/utils.py:1032]
- `update_order_authorize_data` (function) — [saleor/order/utils.py:1059]
- `updates_amounts_for_order` (function) — [saleor/order/utils.py:1085]
- `update_order_display_gross_prices` (function) — [saleor/order/utils.py:1115]
- `calculate_order_granted_refund_status` (function) — [saleor/order/utils.py:1138]
- `log_address_if_validation_skipped_for_order` (function) — [saleor/order/utils.py:1177]
- `get_address_for_order_taxes` (function) — [saleor/order/utils.py:1187]
- `order_info_for_logs` (function) — [saleor/order/utils.py:1195]
- `clean_order_line_quantities` (function) — [saleor/order/utils.py:1261]
- `store_user_addresses_from_draft_order` (function) — [saleor/order/utils.py:1287]
- _…and 1 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/order/__init__.py` (350 lines)
- `saleor/order/models.py` (996 lines)
- `saleor/order/tasks.py` (243 lines)
- `saleor/order/events.py` (934 lines)
- `saleor/order/actions.py` (2110 lines)
- `saleor/order/base_calculations.py` (365 lines)
- `saleor/order/calculations.py` (1163 lines)
- `saleor/order/delivery_context.py` (135 lines)
- `saleor/order/error_codes.py` (109 lines)
- `saleor/order/fetch.py` (285 lines)
- `saleor/order/interface.py` (16 lines)
- `saleor/order/lock_objects.py` (11 lines)
- `saleor/order/notifications.py` (583 lines)
- `saleor/order/search.py` (262 lines)
- `saleor/order/utils.py` (1325 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql/product/types`, `saleor/plugins/openid_connect`, `saleor/graphql`, `saleor/core/db`, `saleor/account`
- Imported by: `saleor/order/tests`, `saleor/order/migrations`, `saleor/graphql/order/tests/integration`

Internal dependencies named in the source:

- `..ORDER_EDITABLE_STATUS`
- `..OrderEvents`
- `..OrderEventsEmails`
- `..OrderStatus`
- `..account.events`
- `..account.lock_objects.user_qs_select_for_update`
- `..account.models.StaffNotificationRecipient`
- `..account.models.User`
- `..account.models.User  # noqa: F401`
- `..account.search.generate_address_search_vector_value`
- `..account.search.generate_email_vector`
- `..account.utils.store_user_address`
- `..app.models.App`
- `..celeryconf.app`
- `..channel.models.Channel`
- `..checkout.AddressType`
- `..checkout.fetch.CheckoutInfo`
- `..checkout.models.Checkout`
- `..core.db.connection.allow_writer`
- `..core.db.fields.MoneyField`
- `..core.db.fields.TaxedMoneyField`
- `..core.exceptions.AllocationError`
- `..core.exceptions.InsufficientStock`
- `..core.exceptions.InsufficientStockData`
- `..core.models.ModelWithExternalReference`
- `..core.models.ModelWithMetadata`
- `..core.notification.utils.get_site_context`
- `..core.notify.NotifyEventType`
- `..core.notify.NotifyHandler`
- `..core.postgres.FlatConcatSearchVector`
- `..core.postgres.NoValidationSearchVector`
- `..core.prices.quantize_price`
- `..core.prices.quantize_price_fields`
- `..core.pricing.interface.LineInfo`
- `..core.taxes.TAX_ERROR_FIELD_LENGTH`
- `..core.taxes.zero_money`
- `..core.tracing.traced_atomic_transaction`
- `..core.transactions.transaction_with_commit_on_errors`
- `..core.units.WeightUnits`
- `..core.utils.country.get_active_country`
- `..core.utils.json_serializer.CustomJsonEncoder`
- `..core.utils.translations.get_translation`
- `..core.utils.url.build_absolute_uri`
- `..core.utils.url.prepare_url`
- `..core.weight.zero_weight`
- `..discount.DiscountType`
- `..discount.DiscountValueType`
- `..discount.VoucherType`
- `..discount.models.OrderDiscount`
- `..discount.models.OrderLineDiscount`
- `..discount.models.Voucher`
- `..discount.models.VoucherCode`
- `..discount.models.VoucherCustomer`
- `..discount.models.VoucherType`
- `..discount.utils.manual_discount.apply_discount_to_value`
- `..discount.utils.promotion.delete_gift_lines_qs`
- `..discount.utils.promotion.get_sale_id`
- `..discount.utils.shared.discount_info_for_logs`
- `..discount.utils.voucher.is_order_level_voucher`
- `..discount.utils.voucher.is_shipping_voucher`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `20da2388e33c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
