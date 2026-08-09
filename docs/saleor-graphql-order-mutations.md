## Purpose

`saleor/graphql/order/mutations` (`saleor/graphql/order/mutations`) groups 37 source file(s) exposing 296 top-level declaration(s).

## Public surface

**`saleor/graphql/order/mutations/draft_order_cleaner.py`**

- `clean_redirect_url` (function) — [saleor/graphql/order/mutations/draft_order_cleaner.py:13]
- `clean_voucher_and_voucher_code` (function) — [saleor/graphql/order/mutations/draft_order_cleaner.py:26]
- `clean_voucher` (function) — [saleor/graphql/order/mutations/draft_order_cleaner.py:46]
- `clean_voucher_code` (function) — [saleor/graphql/order/mutations/draft_order_cleaner.py:83]
- `clean_voucher_listing` (function) — [saleor/graphql/order/mutations/draft_order_cleaner.py:108]

**`saleor/graphql/order/mutations/draft_order_complete.py`**

- `DraftOrderComplete` (class) — [saleor/graphql/order/mutations/draft_order_complete.py:45]
- `Arguments` (class) — [saleor/graphql/order/mutations/draft_order_complete.py:48]
- `Meta` (class) — [saleor/graphql/order/mutations/draft_order_complete.py:53]
- `update_user_fields` (function) — [saleor/graphql/order/mutations/draft_order_complete.py:61]
- `validate_order` (function) — [saleor/graphql/order/mutations/draft_order_complete.py:75]
- `handle_order_voucher` (function) — [saleor/graphql/order/mutations/draft_order_complete.py:87]
- `setup_voucher_customer` (function) — [saleor/graphql/order/mutations/draft_order_complete.py:93]
- `deactivate_single_use_voucher_codes` (function) — [saleor/graphql/order/mutations/draft_order_complete.py:107]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/draft_order_complete.py:118]

**`saleor/graphql/order/mutations/draft_order_create.py`**

- `OrderLineInput` (class) — [saleor/graphql/order/mutations/draft_order_create.py:55]
- `Meta` (class) — [saleor/graphql/order/mutations/draft_order_create.py:60]
- `OrderLineCreateInput` (class) — [saleor/graphql/order/mutations/draft_order_create.py:64]
- `Meta` (class) — [saleor/graphql/order/mutations/draft_order_create.py:85]
- `DraftOrderInput` (class) — [saleor/graphql/order/mutations/draft_order_create.py:89]
- `Meta` (class) — [saleor/graphql/order/mutations/draft_order_create.py:165]
- `DraftOrderCreateInput` (class) — [saleor/graphql/order/mutations/draft_order_create.py:169]
- `Meta` (class) — [saleor/graphql/order/mutations/draft_order_create.py:177]
- `DraftOrderCreate` (class) — [saleor/graphql/order/mutations/draft_order_create.py:181]
- `Arguments` (class) — [saleor/graphql/order/mutations/draft_order_create.py:186]
- `Meta` (class) — [saleor/graphql/order/mutations/draft_order_create.py:191]
- `get_instance_channel_id` (function) — [saleor/graphql/order/mutations/draft_order_create.py:202]
- `clean_input` (function) — [saleor/graphql/order/mutations/draft_order_create.py:219]
- `clean_addresses` (function) — [saleor/graphql/order/mutations/draft_order_create.py:266]
- `clean_lines` (function) — [saleor/graphql/order/mutations/draft_order_create.py:319]
- `save` (function) — [saleor/graphql/order/mutations/draft_order_create.py:392]
- `handle_order_voucher` (function) — [saleor/graphql/order/mutations/draft_order_create.py:453]
- `success_response` (function) — [saleor/graphql/order/mutations/draft_order_create.py:480]

**`saleor/graphql/order/mutations/draft_order_delete.py`**

- `DraftOrderDelete` (class) — [saleor/graphql/order/mutations/draft_order_delete.py:27]
- `Arguments` (class) — [saleor/graphql/order/mutations/draft_order_delete.py:30]
- `Meta` (class) — [saleor/graphql/order/mutations/draft_order_delete.py:37]
- `clean_instance` (function) — [saleor/graphql/order/mutations/draft_order_delete.py:46]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/draft_order_delete.py:70]
- `get_instance_channel_id` (function) — [saleor/graphql/order/mutations/draft_order_delete.py:83]
- `post_save_action` (function) — [saleor/graphql/order/mutations/draft_order_delete.py:87]
- `success_response` (function) — [saleor/graphql/order/mutations/draft_order_delete.py:98]

**`saleor/graphql/order/mutations/draft_order_update.py`**

- `DraftOrderUpdate` (class) — [saleor/graphql/order/mutations/draft_order_update.py:50]
- `Arguments` (class) — [saleor/graphql/order/mutations/draft_order_update.py:56]
- `Meta` (class) — [saleor/graphql/order/mutations/draft_order_update.py:66]
- `get_instance` (function) — [saleor/graphql/order/mutations/draft_order_update.py:79]
- `should_invalidate_prices` (function) — [saleor/graphql/order/mutations/draft_order_update.py:96]
- `clean_input` (function) — [saleor/graphql/order/mutations/draft_order_update.py:109]
- `clean_channel_id` (function) — [saleor/graphql/order/mutations/draft_order_update.py:142]
- `clean_shipping_method` (function) — [saleor/graphql/order/mutations/draft_order_update.py:155]
- `clean_addresses` (function) — [saleor/graphql/order/mutations/draft_order_update.py:191]
- `handle_order_voucher` (function) — [saleor/graphql/order/mutations/draft_order_update.py:323]
- `handle_shipping` (function) — [saleor/graphql/order/mutations/draft_order_update.py:363]
- `handle_metadata` (function) — [saleor/graphql/order/mutations/draft_order_update.py:379]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/draft_order_update.py:397]

**`saleor/graphql/order/mutations/fulfillment_approve.py`**

- `FulfillmentApprove` (class) — [saleor/graphql/order/mutations/fulfillment_approve.py:27]
- `Arguments` (class) — [saleor/graphql/order/mutations/fulfillment_approve.py:31]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_approve.py:40]
- `clean_input` (function) — [saleor/graphql/order/mutations/fulfillment_approve.py:54]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/fulfillment_approve.py:74]

**`saleor/graphql/order/mutations/fulfillment_cancel.py`**

- `FulfillmentCancelInput` (class) — [saleor/graphql/order/mutations/fulfillment_cancel.py:24]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_cancel.py:31]
- `FulfillmentCancel` (class) — [saleor/graphql/order/mutations/fulfillment_cancel.py:35]
- `Arguments` (class) — [saleor/graphql/order/mutations/fulfillment_cancel.py:39]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_cancel.py:45]
- `validate_fulfillment` (function) — [saleor/graphql/order/mutations/fulfillment_cancel.py:53]
- `validate_order` (function) — [saleor/graphql/order/mutations/fulfillment_cancel.py:78]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/fulfillment_cancel.py:91]

**`saleor/graphql/order/mutations/fulfillment_refund_and_return_product_base.py`**

- `FulfillmentRefundAndReturnProductBase` (class) — [saleor/graphql/order/mutations/fulfillment_refund_and_return_product_base.py:19]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_refund_and_return_product_base.py:20]
- `clean_order_payment` (function) — [saleor/graphql/order/mutations/fulfillment_refund_and_return_product_base.py:52]
- `clean_amount_to_refund` (function) — [saleor/graphql/order/mutations/fulfillment_refund_and_return_product_base.py:65]
- `raise_error_for_payment_error` (function) — [saleor/graphql/order/mutations/fulfillment_refund_and_return_product_base.py:112]
- `clean_fulfillment_lines` (function) — [saleor/graphql/order/mutations/fulfillment_refund_and_return_product_base.py:121]
- `clean_lines` (function) — [saleor/graphql/order/mutations/fulfillment_refund_and_return_product_base.py:193]

**`saleor/graphql/order/mutations/fulfillment_refund_products.py`**

- `OrderRefundLineInput` (class) — [saleor/graphql/order/mutations/fulfillment_refund_products.py:24]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_refund_products.py:35]
- `OrderRefundFulfillmentLineInput` (class) — [saleor/graphql/order/mutations/fulfillment_refund_products.py:39]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_refund_products.py:50]
- `OrderRefundProductsInput` (class) — [saleor/graphql/order/mutations/fulfillment_refund_products.py:54]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_refund_products.py:75]
- `FulfillmentRefundProducts` (class) — [saleor/graphql/order/mutations/fulfillment_refund_products.py:79]
- `Arguments` (class) — [saleor/graphql/order/mutations/fulfillment_refund_products.py:83]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_refund_products.py:92]
- `clean_input` (function) — [saleor/graphql/order/mutations/fulfillment_refund_products.py:100]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/fulfillment_refund_products.py:142]

**`saleor/graphql/order/mutations/fulfillment_return_products.py`**

- `OrderReturnLineInput` (class) — [saleor/graphql/order/mutations/fulfillment_return_products.py:28]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_return_products.py:50]
- `OrderReturnFulfillmentLineInput` (class) — [saleor/graphql/order/mutations/fulfillment_return_products.py:54]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_return_products.py:76]
- `OrderReturnProductsInput` (class) — [saleor/graphql/order/mutations/fulfillment_return_products.py:80]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_return_products.py:112]
- `FulfillmentReturnProducts` (class) — [saleor/graphql/order/mutations/fulfillment_return_products.py:116]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_return_products.py:129]
- `Arguments` (class) — [saleor/graphql/order/mutations/fulfillment_return_products.py:136]
- `clean_input` (function) — [saleor/graphql/order/mutations/fulfillment_return_products.py:146]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/fulfillment_return_products.py:220]

**`saleor/graphql/order/mutations/fulfillment_update_tracking.py`**

- `FulfillmentUpdateTracking` (class) — [saleor/graphql/order/mutations/fulfillment_update_tracking.py:22]
- `Arguments` (class) — [saleor/graphql/order/mutations/fulfillment_update_tracking.py:30]
- `Meta` (class) — [saleor/graphql/order/mutations/fulfillment_update_tracking.py:36]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/fulfillment_update_tracking.py:50]

**`saleor/graphql/order/mutations/order_cancel.py`**

- `clean_order_cancel` (function) — [saleor/graphql/order/mutations/order_cancel.py:21]
- `OrderCancel` (class) — [saleor/graphql/order/mutations/order_cancel.py:34]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_cancel.py:37]
- `Meta` (class) — [saleor/graphql/order/mutations/order_cancel.py:40]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_cancel.py:48]

**`saleor/graphql/order/mutations/order_capture.py`**

- `clean_order_capture` (function) — [saleor/graphql/order/mutations/order_capture.py:23]
- `OrderCapture` (class) — [saleor/graphql/order/mutations/order_capture.py:39]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_capture.py:42]
- `Meta` (class) — [saleor/graphql/order/mutations/order_capture.py:48]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_capture.py:56]

**`saleor/graphql/order/mutations/order_confirm.py`**

- `OrderConfirm` (class) — [saleor/graphql/order/mutations/order_confirm.py:32]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_confirm.py:35]
- `Meta` (class) — [saleor/graphql/order/mutations/order_confirm.py:38]
- `get_instance` (function) — [saleor/graphql/order/mutations/order_confirm.py:47]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_confirm.py:71]

**`saleor/graphql/order/mutations/order_discount_add.py`**

- `OrderDiscountAdd` (class) — [saleor/graphql/order/mutations/order_discount_add.py:24]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_discount_add.py:27]
- `Meta` (class) — [saleor/graphql/order/mutations/order_discount_add.py:34]
- `validate_order` (function) — [saleor/graphql/order/mutations/order_discount_add.py:42]
- `validate` (function) — [saleor/graphql/order/mutations/order_discount_add.py:58]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_discount_add.py:63]

**`saleor/graphql/order/mutations/order_discount_common.py`**

- `OrderDiscountCommonInput` (class) — [saleor/graphql/order/mutations/order_discount_common.py:15]
- `Meta` (class) — [saleor/graphql/order/mutations/order_discount_common.py:29]
- `OrderDiscountCommon` (class) — [saleor/graphql/order/mutations/order_discount_common.py:33]
- `Meta` (class) — [saleor/graphql/order/mutations/order_discount_common.py:34]
- `validate_order` (function) — [saleor/graphql/order/mutations/order_discount_common.py:38]
- `validate_order_discount_input` (function) — [saleor/graphql/order/mutations/order_discount_common.py:57]

**`saleor/graphql/order/mutations/order_discount_delete.py`**

- `OrderDiscountDelete` (class) — [saleor/graphql/order/mutations/order_discount_delete.py:20]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_discount_delete.py:23]
- `Meta` (class) — [saleor/graphql/order/mutations/order_discount_delete.py:28]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_discount_delete.py:36]

**`saleor/graphql/order/mutations/order_discount_update.py`**

- `OrderDiscountUpdate` (class) — [saleor/graphql/order/mutations/order_discount_update.py:23]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_discount_update.py:26]
- `Meta` (class) — [saleor/graphql/order/mutations/order_discount_update.py:35]
- `validate` (function) — [saleor/graphql/order/mutations/order_discount_update.py:43]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_discount_update.py:51]

**`saleor/graphql/order/mutations/order_fulfill.py`**

- `OrderFulfillStockInput` (class) — [saleor/graphql/order/mutations/order_fulfill.py:28]
- `Meta` (class) — [saleor/graphql/order/mutations/order_fulfill.py:38]
- `OrderFulfillLineInput` (class) — [saleor/graphql/order/mutations/order_fulfill.py:42]
- `Meta` (class) — [saleor/graphql/order/mutations/order_fulfill.py:52]
- `OrderFulfillInput` (class) — [saleor/graphql/order/mutations/order_fulfill.py:56]
- `Meta` (class) — [saleor/graphql/order/mutations/order_fulfill.py:75]
- `FulfillmentUpdateTrackingInput` (class) — [saleor/graphql/order/mutations/order_fulfill.py:79]
- `Meta` (class) — [saleor/graphql/order/mutations/order_fulfill.py:86]
- `OrderFulfill` (class) — [saleor/graphql/order/mutations/order_fulfill.py:90]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_fulfill.py:94]
- `Meta` (class) — [saleor/graphql/order/mutations/order_fulfill.py:102]
- `clean_lines` (function) — [saleor/graphql/order/mutations/order_fulfill.py:128]
- `check_warehouses_for_duplicates` (function) — [saleor/graphql/order/mutations/order_fulfill.py:132]
- `check_lines_for_duplicates` (function) — [saleor/graphql/order/mutations/order_fulfill.py:147]
- `check_lines_for_preorder` (function) — [saleor/graphql/order/mutations/order_fulfill.py:161]
- `check_total_quantity_of_items` (function) — [saleor/graphql/order/mutations/order_fulfill.py:178]
- `clean_input` (function) — [saleor/graphql/order/mutations/order_fulfill.py:191]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_fulfill.py:252]

**`saleor/graphql/order/mutations/order_grant_refund_create.py`**

- `OrderGrantRefundCreateLineError` (class) — [saleor/graphql/order/mutations/order_grant_refund_create.py:37]
- `OrderGrantRefundCreateError` (class) — [saleor/graphql/order/mutations/order_grant_refund_create.py:46]
- `Meta` (class) — [saleor/graphql/order/mutations/order_grant_refund_create.py:54]
- `OrderGrantRefundCreateLineInput` (class) — [saleor/graphql/order/mutations/order_grant_refund_create.py:58]
- `Meta` (class) — [saleor/graphql/order/mutations/order_grant_refund_create.py:69]
- `OrderGrantRefundCreateInput` (class) — [saleor/graphql/order/mutations/order_grant_refund_create.py:73]
- `Meta` (class) — [saleor/graphql/order/mutations/order_grant_refund_create.py:107]
- `OrderGrantRefundCreate` (class) — [saleor/graphql/order/mutations/order_grant_refund_create.py:111]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_grant_refund_create.py:119]
- `Meta` (class) — [saleor/graphql/order/mutations/order_grant_refund_create.py:126]
- `clean_input_lines` (function) — [saleor/graphql/order/mutations/order_grant_refund_create.py:133]
- `calculate_amount` (function) — [saleor/graphql/order/mutations/order_grant_refund_create.py:160]
- `validate_input` (function) — [saleor/graphql/order/mutations/order_grant_refund_create.py:177]
- `clean_input` (function) — [saleor/graphql/order/mutations/order_grant_refund_create.py:199]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_grant_refund_create.py:293]

**`saleor/graphql/order/mutations/order_grant_refund_update.py`**

- `OrderGrantRefundUpdateLineError` (class) — [saleor/graphql/order/mutations/order_grant_refund_update.py:38]
- `OrderGrantRefundUpdateError` (class) — [saleor/graphql/order/mutations/order_grant_refund_update.py:47]
- `Meta` (class) — [saleor/graphql/order/mutations/order_grant_refund_update.py:61]
- `OrderGrantRefundUpdateLineAddInput` (class) — [saleor/graphql/order/mutations/order_grant_refund_update.py:65]
- `Meta` (class) — [saleor/graphql/order/mutations/order_grant_refund_update.py:76]
- `OrderGrantRefundUpdateInput` (class) — [saleor/graphql/order/mutations/order_grant_refund_update.py:80]
- `Meta` (class) — [saleor/graphql/order/mutations/order_grant_refund_update.py:119]
- `OrderGrantRefundUpdate` (class) — [saleor/graphql/order/mutations/order_grant_refund_update.py:123]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_grant_refund_update.py:131]
- `Meta` (class) — [saleor/graphql/order/mutations/order_grant_refund_update.py:138]
- `validate_input` (function) — [saleor/graphql/order/mutations/order_grant_refund_update.py:145]
- `clean_remove_lines` (function) — [saleor/graphql/order/mutations/order_grant_refund_update.py:192]
- `clean_add_lines` (function) — [saleor/graphql/order/mutations/order_grant_refund_update.py:232]
- `clean_input` (function) — [saleor/graphql/order/mutations/order_grant_refund_update.py:250]
- `process_update_for_granted_refund` (function) — [saleor/graphql/order/mutations/order_grant_refund_update.py:389]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_grant_refund_update.py:450]

**`saleor/graphql/order/mutations/order_grant_refund_utils.py`**

- `GrantRefundLineDict` (class) — [saleor/graphql/order/mutations/order_grant_refund_utils.py:14]
- `shipping_costs_already_granted` (function) — [saleor/graphql/order/mutations/order_grant_refund_utils.py:21]
- `handle_lines_with_quantity_already_refunded` (function) — [saleor/graphql/order/mutations/order_grant_refund_utils.py:32]
- `validate_reason_references` (function) — [saleor/graphql/order/mutations/order_grant_refund_utils.py:83]
- `get_input_lines_data` (function) — [saleor/graphql/order/mutations/order_grant_refund_utils.py:158]
- `assign_order_lines` (function) — [saleor/graphql/order/mutations/order_grant_refund_utils.py:195]
- `resolve_reason_reference_page` (function) — [saleor/graphql/order/mutations/order_grant_refund_utils.py:219]
- `clean_grant_refund_lines` (function) — [saleor/graphql/order/mutations/order_grant_refund_utils.py:255]

**`saleor/graphql/order/mutations/order_line_delete.py`**

- `OrderLineDelete` (class) — [saleor/graphql/order/mutations/order_line_delete.py:30]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_line_delete.py:36]
- `Meta` (class) — [saleor/graphql/order/mutations/order_line_delete.py:39]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_line_delete.py:47]
- `validate` (function) — [saleor/graphql/order/mutations/order_line_delete.py:126]

**`saleor/graphql/order/mutations/order_line_discount_remove.py`**

- `OrderLineDiscountRemove` (class) — [saleor/graphql/order/mutations/order_line_discount_remove.py:18]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_line_discount_remove.py:26]
- `Meta` (class) — [saleor/graphql/order/mutations/order_line_discount_remove.py:31]
- `validate` (function) — [saleor/graphql/order/mutations/order_line_discount_remove.py:39]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_line_discount_remove.py:43]

**`saleor/graphql/order/mutations/order_line_discount_update.py`**

- `OrderLineDiscountUpdate` (class) — [saleor/graphql/order/mutations/order_line_discount_update.py:18]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_line_discount_update.py:26]
- `Meta` (class) — [saleor/graphql/order/mutations/order_line_discount_update.py:35]
- `validate` (function) — [saleor/graphql/order/mutations/order_line_discount_update.py:43]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_line_discount_update.py:53]

**`saleor/graphql/order/mutations/order_line_update.py`**

- `OrderLineUpdate` (class) — [saleor/graphql/order/mutations/order_line_update.py:27]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_line_update.py:32]
- `Meta` (class) — [saleor/graphql/order/mutations/order_line_update.py:38]
- `clean_input` (function) — [saleor/graphql/order/mutations/order_line_update.py:47]
- `save` (function) — [saleor/graphql/order/mutations/order_line_update.py:75]
- `success_response` (function) — [saleor/graphql/order/mutations/order_line_update.py:119]
- `get_instance_channel_id` (function) — [saleor/graphql/order/mutations/order_line_update.py:127]

**`saleor/graphql/order/mutations/order_lines_create.py`**

- `OrderLinesCreate` (class) — [saleor/graphql/order/mutations/order_lines_create.py:48]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_lines_create.py:52]
- `Meta` (class) — [saleor/graphql/order/mutations/order_lines_create.py:62]
- `validate_lines` (function) — [saleor/graphql/order/mutations/order_lines_create.py:71]
- `validate_variants` (function) — [saleor/graphql/order/mutations/order_lines_create.py:138]
- `add_lines_to_order` (function) — [saleor/graphql/order/mutations/order_lines_create.py:150]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_lines_create.py:179]

**`saleor/graphql/order/mutations/order_mark_as_paid.py`**

- `OrderMarkAsPaid` (class) — [saleor/graphql/order/mutations/order_mark_as_paid.py:36]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_mark_as_paid.py:39]
- `Meta` (class) — [saleor/graphql/order/mutations/order_mark_as_paid.py:45]
- `clean_billing_address` (function) — [saleor/graphql/order/mutations/order_mark_as_paid.py:53]
- `handle_mark_as_paid_for_payment` (function) — [saleor/graphql/order/mutations/order_mark_as_paid.py:61]
- `handle_mark_as_paid_for_transaction` (function) — [saleor/graphql/order/mutations/order_mark_as_paid.py:81]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_mark_as_paid.py:112]

**`saleor/graphql/order/mutations/order_note_add.py`**

- `OrderNoteAddError` (class) — [saleor/graphql/order/mutations/order_note_add.py:25]
- `Meta` (class) — [saleor/graphql/order/mutations/order_note_add.py:28]
- `OrderNoteAdd` (class) — [saleor/graphql/order/mutations/order_note_add.py:32]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_note_add.py:36]
- `Meta` (class) — [saleor/graphql/order/mutations/order_note_add.py:43]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_note_add.py:50]

**`saleor/graphql/order/mutations/order_note_common.py`**

- `OrderNoteInput` (class) — [saleor/graphql/order/mutations/order_note_common.py:11]
- `Meta` (class) — [saleor/graphql/order/mutations/order_note_common.py:16]
- `OrderNoteCommon` (class) — [saleor/graphql/order/mutations/order_note_common.py:20]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_note_common.py:21]
- `Meta` (class) — [saleor/graphql/order/mutations/order_note_common.py:26]
- `clean_input` (function) — [saleor/graphql/order/mutations/order_note_common.py:30]

**`saleor/graphql/order/mutations/order_note_update.py`**

- `OrderNoteUpdateError` (class) — [saleor/graphql/order/mutations/order_note_update.py:21]
- `Meta` (class) — [saleor/graphql/order/mutations/order_note_update.py:24]
- `OrderNoteUpdate` (class) — [saleor/graphql/order/mutations/order_note_update.py:28]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_note_update.py:32]
- `Meta` (class) — [saleor/graphql/order/mutations/order_note_update.py:39]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_note_update.py:46]

**`saleor/graphql/order/mutations/order_refund.py`**

- `clean_refund_payment` (function) — [saleor/graphql/order/mutations/order_refund.py:23]
- `clean_order_refund` (function) — [saleor/graphql/order/mutations/order_refund.py:39]
- `OrderRefund` (class) — [saleor/graphql/order/mutations/order_refund.py:52]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_refund.py:55]
- `Meta` (class) — [saleor/graphql/order/mutations/order_refund.py:61]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_refund.py:69]

**`saleor/graphql/order/mutations/order_update_shipping.py`**

- `OrderUpdateShippingInput` (class) — [saleor/graphql/order/mutations/order_update_shipping.py:29]
- `Meta` (class) — [saleor/graphql/order/mutations/order_update_shipping.py:36]
- `OrderUpdateShipping` (class) — [saleor/graphql/order/mutations/order_update_shipping.py:40]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_update_shipping.py:43]
- `Meta` (class) — [saleor/graphql/order/mutations/order_update_shipping.py:54]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_update_shipping.py:66]

**`saleor/graphql/order/mutations/order_update.py`**

- `OrderUpdateInput` (class) — [saleor/graphql/order/mutations/order_update.py:35]
- `Meta` (class) — [saleor/graphql/order/mutations/order_update.py:64]
- `OrderUpdate` (class) — [saleor/graphql/order/mutations/order_update.py:68]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_update.py:69]
- `Meta` (class) — [saleor/graphql/order/mutations/order_update.py:79]
- `get_instance` (function) — [saleor/graphql/order/mutations/order_update.py:92]
- `should_invalidate_prices` (function) — [saleor/graphql/order/mutations/order_update.py:107]
- `clean_input` (function) — [saleor/graphql/order/mutations/order_update.py:197]
- `get_instance_channel_id` (function) — [saleor/graphql/order/mutations/order_update.py:232]
- `handle_metadata` (function) — [saleor/graphql/order/mutations/order_update.py:236]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_update.py:253]

**`saleor/graphql/order/mutations/order_void.py`**

- `clean_void_payment` (function) — [saleor/graphql/order/mutations/order_void.py:20]
- `OrderVoid` (class) — [saleor/graphql/order/mutations/order_void.py:37]
- `Arguments` (class) — [saleor/graphql/order/mutations/order_void.py:40]
- `Meta` (class) — [saleor/graphql/order/mutations/order_void.py:43]
- `perform_mutation` (function) — [saleor/graphql/order/mutations/order_void.py:51]

**`saleor/graphql/order/mutations/utils.py`**

- `EditableOrderValidationMixin` (class) — [saleor/graphql/order/mutations/utils.py:85]
- `Meta` (class) — [saleor/graphql/order/mutations/utils.py:86]
- `validate_order` (function) — [saleor/graphql/order/mutations/utils.py:90]
- `ShippingMethodUpdateMixin` (class) — [saleor/graphql/order/mutations/utils.py:103]
- `clear_shipping_method_from_order` (function) — [saleor/graphql/order/mutations/utils.py:105]
- `update_shipping_method` (function) — [saleor/graphql/order/mutations/utils.py:119]
- `validate_shipping_channel_listing` (function) — [saleor/graphql/order/mutations/utils.py:137]
- `update_shipping_price` (function) — [saleor/graphql/order/mutations/utils.py:153]
- `assign_shipping_price` (function) — [saleor/graphql/order/mutations/utils.py:158]
- `update_shipping_discount` (function) — [saleor/graphql/order/mutations/utils.py:178]
- `process_shipping_method` (function) — [saleor/graphql/order/mutations/utils.py:196]
- `update_shipping` (function) — [saleor/graphql/order/mutations/utils.py:215]
- `clean_order_update_shipping` (function) — [saleor/graphql/order/mutations/utils.py:225]
- `check_shipping` (function) — [saleor/graphql/order/mutations/utils.py:230]
- `handle_availability_error` (function) — [saleor/graphql/order/mutations/utils.py:246]
- `call_event_by_order_status` (function) — [saleor/graphql/order/mutations/utils.py:255]
- `try_payment_action` (function) — [saleor/graphql/order/mutations/utils.py:266]
- `clean_payment` (function) — [saleor/graphql/order/mutations/utils.py:286]
- `VariantData` (class) — [saleor/graphql/order/mutations/utils.py:299]
- `get_variant_rule_info_map` (function) — [saleor/graphql/order/mutations/utils.py:304]
- `save_addresses` (function) — [saleor/graphql/order/mutations/utils.py:324]
- `update_meta_fields` (function) — [saleor/graphql/order/mutations/utils.py:339]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/order/mutations/__init__.py` (1 lines)
- `saleor/graphql/order/mutations/fulfillment_update_tracking.py` (81 lines)
- `saleor/graphql/order/mutations/draft_order_cleaner.py` (117 lines)
- `saleor/graphql/order/mutations/draft_order_complete.py` (263 lines)
- `saleor/graphql/order/mutations/draft_order_create.py` (482 lines)
- `saleor/graphql/order/mutations/draft_order_delete.py` (100 lines)
- `saleor/graphql/order/mutations/draft_order_update.py` (446 lines)
- `saleor/graphql/order/mutations/fulfillment_approve.py` (112 lines)
- `saleor/graphql/order/mutations/fulfillment_cancel.py` (132 lines)
- `saleor/graphql/order/mutations/fulfillment_refund_and_return_product_base.py` (261 lines)
- `saleor/graphql/order/mutations/fulfillment_refund_products.py` (167 lines)
- `saleor/graphql/order/mutations/fulfillment_return_products.py` (262 lines)
- `saleor/graphql/order/mutations/order_cancel.py` (67 lines)
- `saleor/graphql/order/mutations/order_capture.py` (102 lines)
- `saleor/graphql/order/mutations/order_confirm.py` (118 lines)
- `saleor/graphql/order/mutations/order_discount_add.py` (86 lines)
- `saleor/graphql/order/mutations/order_discount_common.py` (69 lines)
- `saleor/graphql/order/mutations/order_discount_delete.py` (73 lines)
- `saleor/graphql/order/mutations/order_discount_update.py` (103 lines)
- `saleor/graphql/order/mutations/order_fulfill.py` (305 lines)
- `saleor/graphql/order/mutations/order_grant_refund_create.py` (325 lines)
- `saleor/graphql/order/mutations/order_grant_refund_update.py` (468 lines)
- `saleor/graphql/order/mutations/order_grant_refund_utils.py` (283 lines)
- `saleor/graphql/order/mutations/order_line_delete.py` (134 lines)
- `saleor/graphql/order/mutations/order_line_discount_remove.py` (66 lines)
- `saleor/graphql/order/mutations/order_line_discount_update.py` (89 lines)
- `saleor/graphql/order/mutations/order_line_update.py` (129 lines)
- `saleor/graphql/order/mutations/order_lines_create.py` (256 lines)
- `saleor/graphql/order/mutations/order_mark_as_paid.py` (141 lines)
- `saleor/graphql/order/mutations/order_note_add.py` (70 lines)
- `saleor/graphql/order/mutations/order_note_common.py` (42 lines)
- `saleor/graphql/order/mutations/order_note_update.py` (72 lines)
- `saleor/graphql/order/mutations/order_refund.py` (117 lines)
- `saleor/graphql/order/mutations/order_update_shipping.py` (154 lines)
- `saleor/graphql/order/mutations/order_update.py` (295 lines)
- `saleor/graphql/order/mutations/order_void.py` (80 lines)
- `saleor/graphql/order/mutations/utils.py` (350 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`, `saleor/graphql`
- Imported by: `saleor/graphql/order/tests/mutations`

Internal dependencies named in the source:

- `....account.models.User`
- `....app.models.App`
- `....channel.MarkAsPaidStrategy`
- `....channel.models.Channel`
- `....checkout.AddressType`
- `....checkout.fetch.get_variant_channel_listing`
- `....core.exceptions.InsufficientStock`
- `....core.postgres.FlatConcatSearchVector`
- `....core.taxes.TaxError`
- `....core.taxes.zero_money`
- `....core.taxes.zero_taxed_money`
- `....core.tracing.traced_atomic_transaction`
- `....core.utils.metadata_manager`
- `....core.utils.update_mutation_manager.InstanceTracker`
- `....core.utils.url.validate_storefront_url`
- `....discount.VoucherType`
- `....discount.interface.VariantPromotionRuleInfo`
- `....discount.interface.fetch_variant_rules_info`
- `....discount.models.Voucher`
- `....discount.models.VoucherCode`
- `....discount.utils.manual_discount.apply_discount_to_value`
- `....giftcard.utils.deactivate_order_gift_cards`
- `....giftcard.utils.order_has_gift_card_lines`
- `....order.FulfillmentLineData`
- `....order.FulfillmentStatus`
- `....order.ORDER_EDITABLE_STATUS`
- `....order.OrderEvents`
- `....order.OrderGrantedRefundStatus`
- `....order.OrderOrigin`
- `....order.OrderStatus`
- `....order.actions.OrderFulfillmentLineInfo`
- `....order.actions.approve_fulfillment`
- `....order.actions.call_order_event`
- `....order.actions.cancel_fulfillment`
- `....order.actions.cancel_order`
- `....order.actions.create_fulfillments`
- `....order.actions.create_fulfillments_for_returned_products`
- `....order.actions.create_refund_fulfillment`
- `....order.actions.fulfillment_tracking_updated`
- `....order.actions.order_charged`
- `....order.actions.order_created`
- `....order.actions.order_refunded`
- `....order.actions.order_voided`
- `....order.calculations.fetch_order_prices_if_expired`
- `....order.error_codes`
- `....order.error_codes.OrderErrorCode`
- `....order.error_codes.OrderNoteAddErrorCode`
- `....order.events`
- `....order.events.transaction_mark_order_as_paid_failed_event`
- `....order.fetch.OrderInfo`
- `....order.fetch.OrderLineInfo`
- `....order.fetch.fetch_order_info`
- `....order.fetch.fetch_order_lines`
- `....order.lock_objects.order_qs_select_for_update`
- `....order.models`
- `....order.models.OrderLine`
- `....order.notifications.send_fulfillment_update`
- `....order.search.prepare_order_search_vector_value`
- `....order.search.update_order_search_vector`
- `....order.utils.clean_order_line_quantities`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `12a8239975a0` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
