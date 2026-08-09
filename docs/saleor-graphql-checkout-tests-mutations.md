## Purpose

`saleor/graphql/checkout/tests/mutations` (`saleor/graphql/checkout/tests/mutations`) groups 26 source file(s) exposing 318 top-level declaration(s).

## Public surface

**`saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py`**

- `test_checkout_add_voucher_for_entire_order` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:88]
- `test_checkout_add_voucher_code_by_token` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:116]
- `test_checkout_add_already_applied_voucher_for_entire_order` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:128]
- `test_checkout_add_voucher_code_with_display_gross_prices` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:163]
- `test_checkout_add_voucher_code_without_display_gross_prices` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:197]
- `test_checkout_add_voucher_code_line_without_listing` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:238]
- `test_checkout_add_products_voucher_code_checkout_with_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:258]
- `test_checkout_add_collection_voucher_code_checkout_with_promotion_collection_deleted` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:317]
- `delete_collections` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:338]
- `test_checkout_add_voucher_code_checkout_on_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:353]
- `test_checkout_add_specific_product_voucher_code_checkout_on_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:398]
- `test_checkout_add_collection_voucher_code_checkout_on_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:456]
- `test_checkout_add_category_code_checkout_on_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:522]
- `test_checkout_add_voucher_code_checkout_on_order_promotion_discount` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:582]
- `test_checkout_add_voucher_code_checkout_with_gift_reward` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:608]
- `test_checkout_add_variant_voucher_code_apply_once_per_order` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:640]
- `test_checkout_add_voucher_code_not_applicable_voucher` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:714]
- `test_checkout_add_voucher_code_not_assigned_to_channel` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:727]
- `test_checkout_add_voucher_code_lack_of_active_codes` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:740]
- `test_checkout_add_gift_card_code` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:762]
- `test_checkout_add_many_gift_card_code` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:776]
- `test_checkout_add_inactive_gift_card_code` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:793]
- `test_checkout_add_expired_gift_card_code` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:815]
- `test_checkout_add_used_gift_card_code` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:839]
- `test_checkout_get_total_with_gift_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:866]
- `test_checkout_get_total_with_many_gift_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:887]
- `test_checkout_get_total_with_more_money_on_gift_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:914]
- `test_checkout_add_same_gift_card_code` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:932]
- `test_checkout_add_gift_card_code_in_active_gift_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:949]
- `test_checkout_add_gift_card_code_in_expired_gift_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:965]
- `test_checkout_add_promo_code_invalid_checkout` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:983]
- `test_checkout_add_promo_code_invalid_promo_code` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:992]
- `test_checkout_add_promo_code_marks_shipping_methods_as_stale` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:1004]
- `test_checkout_add_promo_code_without_checkout_email` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:1063]
- `test_checkout_add_gift_card_without_checkout_email` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:1083]
- `test_checkout_add_gift_card_without_checkout_email_used_by_someone_else_email` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:1105]
- `test_checkout_add_gift_card_without_checkout_email_used_by_other_user` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:1129]
- `test_checkout_add_gift_card_disallowed_by_channel_flag` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:1153]
- `test_checkout_add_free_shipping_voucher_do_not_invalidate_shipping_method` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:1179]
- `test_checkout_add_shipping_voucher_do_not_invalidate_shipping_method` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py:1224]
- _…and 4 more in this file_

**`saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py`**

- `test_checkout_billing_address_update_by_id` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:45]
- `test_checkout_billing_address_update_when_line_without_listing` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:78]
- `test_checkout_billing_address_update_by_id_without_required_fields` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:112]
- `test_checkout_billing_address_update_by_id_without_street_address_2` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:149]
- `test_checkout_billing_address_update` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:183]
- `test_checkout_billing_address_update_with_skip_required_doesnt_raise_error` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:241]
- `test_checkout_billing_address_update_with_skip_required_overwrite_address` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:265]
- `test_checkout_billing_address_update_with_skip_required_raises_validation_error` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:298]
- `test_checkout_billing_address_update_with_skip_required_saves_address` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:324]
- `test_checkout_billing_address_update_with_skip_value_check_doesnt_raise_error` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:369]
- `test_checkout_billing_address_update_with_skip_value_raises_required_fields_error` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:409]
- `test_checkout_billing_address_update_with_skip_value_check_saves_address` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:435]
- `test_checkout_billing_address_update_with_skip_value_and_skip_required_fields` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:489]
- `test_checkout_address_update_with_skip_value_and_skip_required_saves_address` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:512]
- `test_checkout_billing_address_update_with_disabled_fields_normalization` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:550]
- `test_checkout_billing_address_update_with_disabled_normalization_and_preserve_all_fields` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:588]
- `test_checkout_billing_address_update_with_enabled_normalization_and_not_preserve_all_fields` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:629]
- `test_with_active_problems_flow` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:672]
- `test_checkout_billing_address_skip_validation_by_customer` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:698]
- `test_checkout_billing_address_skip_validation_by_app` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:720]
- `test_checkout_billing_address_triggers_webhooks` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:766]
- `test_checkout_billing_address_update_reset_the_save_address_flag_to_default_value` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:840]
- `test_checkout_billing_address_update_with_save_address_to_false` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:885]
- `test_checkout_billing_address_update_change_save_address_option_to_true` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:916]
- `test_checkout_billing_address_do_not_mark_shipping_as_stale` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py:951]

**`saleor/graphql/checkout/tests/mutations/test_checkout_complete_price_override.py`**

- `test_checkout_complete_price_override` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_price_override.py:38]
- `test_checkout_complete_with_price_override_and_catalogue_promotion_fixed` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_price_override.py:95]
- `test_checkout_complete_with_price_override_and_catalogue_promotion_percentage` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_price_override.py:175]
- `test_checkout_complete_with_price_override_and_voucher_entire_order` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_price_override.py:256]
- `test_checkout_complete_with_price_override_and_voucher_free_shipping` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_price_override.py:335]
- `test_checkout_complete_with_price_override_and_voucher_specific_product` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_price_override.py:411]
- `test_checkout_complete_with_price_override_and_order_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_price_override.py:495]
- `test_checkout_complete_with_price_override_and_gift_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_price_override.py:577]
- `test_checkout_complete_with_price_override_and_catalogue_promotion_and_entire_order_voucher` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_price_override.py:661]

**`saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py`**

- `test_checkout_complete_with_inactive_channel` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:132]
- `test_checkout_complete` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:191]
- `test_checkout_complete_with_metadata` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:360]
- `test_checkout_complete_with_metadata_updates_existing_keys` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:438]
- `test_checkout_complete_with_metadata_checkout_without_metadata` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:501]
- `test_checkout_complete_by_app` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:577]
- `test_checkout_complete_by_app_with_missing_permission` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:640]
- `test_checkout_complete_gift_card_bought` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:703]
- `test_checkout_complete_with_variant_without_sku` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:780]
- `test_checkout_complete_with_variant_without_price` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:838]
- `test_checkout_complete_with_line_without_channel_listing` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:880]
- `test_checkout_complete_requires_confirmation` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:921]
- `test_checkout_with_voucher_complete` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:965]
- `test_checkout_with_order_promotion_complete` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:1090]
- `test_checkout_complete_with_voucher_apply_once_per_order` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:1197]
- `test_checkout_with_voucher_complete_product_on_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:1322]
- `test_checkout_with_voucher_on_specific_product_complete` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:1488]
- `test_checkout_complete_with_voucher_single_use` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:1610]
- `test_checkout_complete_with_voucher_paid_with_gift_card_and_payment` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:1718]
- `test_checkout_complete_with_voucher_paid_by_gift_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:1845]
- `test_checkout_complete_free_shipping_voucher_and_gift_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:1956]
- `test_checkout_complete_product_on_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:2079]
- `test_checkout_complete_product_on_promotion_deleted_promotion_instance` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:2222]
- `delete_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:2314]
- `test_checkout_complete_price_override` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:2363]
- `test_checkout_complete_product_on_old_sale` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:2454]
- `test_checkout_with_voucher_on_specific_product_complete_with_product_on_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:2611]
- `test_checkout_with_voucher_not_increase_uses_on_preprocess_order_creation_failure` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:2801]
- `test_checkout_complete_without_inventory_tracking` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:2852]
- `test_checkout_complete_checkout_without_lines` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:2930]
- `test_checkout_complete_error_in_gateway_response_for_declined_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:2984]
- `error_side_effect` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:3062]
- `test_checkout_complete_does_not_delete_checkout_after_unsuccessful_payment` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:3067]
- `test_checkout_complete_invalid_id` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:3129]
- `test_checkout_complete_no_payment` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:3141]
- `test_checkout_complete_confirmation_needed` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:3166]
- `test_checkout_confirm` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:3228]
- `test_checkout_complete_insufficient_stock` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:3280]
- `test_checkout_complete_insufficient_stock_payment_refunded` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:3328]
- `test_checkout_complete_insufficient_stock_payment_voided` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py:3390]
- _…and 48 more in this file_

**`saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py`**

- `prepare_checkout_for_test` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:135]
- `test_checkout_without_any_transaction` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:196]
- `test_checkout_without_any_transaction_allow_to_create_order` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:243]
- `test_checkout_with_total_0` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:302]
- `test_checkout_with_authorized` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:364]
- `test_checkout_with_charged` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:481]
- `test_checkout_price_override` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:595]
- `test_checkout_paid_with_multiple_transactions` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:703]
- `test_checkout_partially_paid` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:766]
- `test_checkout_partially_paid_allow_unpaid_order` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:819]
- `test_checkout_with_pending_charged` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:877]
- `test_checkout_with_pending_authorized` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:946]
- `test_checkout_with_voucher_not_applicable` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1059]
- `test_checkout_with_voucher_inactive_code` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1101]
- `test_checkout_with_insufficient_stock` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1145]
- `test_checkout_with_gift_card_not_applicable` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1181]
- `test_checkout_with_variant_without_price` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1218]
- `test_checkout_with_line_without_channel_listing` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1266]
- `test_checkout_complete_with_inactive_channel` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1311]
- `test_checkout_complete` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1357]
- `test_checkout_complete_with_metadata` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1501]
- `test_checkout_complete_with_metadata_updates_existing_keys` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1567]
- `test_checkout_complete_with_metadata_checkout_without_metadata` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1621]
- `test_checkout_complete_by_app` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1683]
- `test_checkout_complete_by_app_with_missing_permission` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1740]
- `test_checkout_complete_gift_card_bought` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1795]
- `test_checkout_complete_with_shipping_voucher_and_gift_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1862]
- `test_checkout_complete_with_variant_without_sku` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:1989]
- `test_checkout_with_voucher_complete` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:2052]
- `test_checkout_with_order_promotion_complete` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:2159]
- `test_checkout_complete_with_entire_order_voucher_paid_with_gift_card_and_transaction` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:2239]
- `test_checkout_complete_with_voucher_paid_with_gift_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:2351]
- `test_checkout_complete_with_voucher_apply_once_per_order` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:2465]
- `test_checkout_complete_with_voucher_apply_once_per_order_and_gift_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:2569]
- `test_checkout_complete_with_voucher_single_use` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:2683]
- `test_checkout_complete_with_shipping_voucher` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:2766]
- `test_checkout_with_voucher_complete_product_on_sale` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:2884]
- `test_checkout_with_voucher_on_specific_product_complete` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:3024]
- `test_checkout_complete_with_voucher_on_specific_product_and_gift_card` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:3120]
- `test_checkout_complete_product_on_promotion` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py:3231]
- _…and 51 more in this file_

**`saleor/graphql/checkout/tests/mutations/test_checkout_complete.py`**

- `test_checkout_complete_unconfirmed_order_already_exists` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:98]
- `test_checkout_complete_order_already_exists` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:127]
- `test_checkout_complete_with_inactive_channel_order_already_exists` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:160]
- `test_checkout_complete_no_checkout_email` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:185]
- `test_checkout_complete_0_total_value_no_payment` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:204]
- `test_checkout_complete_0_total_value_from_voucher` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:266]
- `test_checkout_complete_0_total_value_from_giftcard` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:331]
- `test_checkout_complete_fails_with_invalid_tax_app` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:396]
- `test_checkout_complete_calls_correct_tax_app` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:449]
- `test_checkout_complete_calls_failing_plugin` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:504]
- `side_effect` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:515]
- `test_checkout_complete_calls_correct_force_tax_calculation_when_tax_error_was_saved` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:562]
- `test_checkout_complete_existing_user_address_save_address_options_off` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:618]
- `test_checkout_complete_builtin_shipping_method_metadata_denormalization` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:673]
- `clear_shipping_metadata` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:706]
- `test_checkout_complete_validate_checkout_addresses_raises_does_not_exist_error` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:754]
- `test_checkout_complete_validate_checkout_addresses_raises_does_not_exist_error_order_returned` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_complete.py:797]

**`saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py`**

- `test_checkout_create_from_order_with_same_user` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:57]
- `test_checkout_create_from_order_with_different_user` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:90]
- `test_checkout_create_from_order_with_anonymous_user` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:126]
- `test_checkout_create_from_anonymous_order_and_logged_in_user` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:154]
- `test_checkout_create_from_order_with_gift_reward` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:190]
- `test_checkout_create_from_order_when_order_not_found` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:245]
- `test_checkout_create_from_order_variant_not_found` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:266]
- `test_checkout_create_from_order_line_without_channel_listing` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:333]
- `test_checkout_create_from_order_variant_not_available_in_channel` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:390]
- `test_checkout_create_from_order_variant_not_published` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:442]
- `test_checkout_create_from_order_variant_exceed_variant_quantity_limit` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:492]
- `test_checkout_create_from_order_variant_exceed_global_quantity_limit` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:544]
- `test_checkout_create_from_order_variant_not_available_for_purchase` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:598]
- `test_checkout_create_from_order_variant_out_of_stock` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:653]
- `test_checkout_create_from_order_variant_not_enough_stock` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:702]
- `test_checkout_create_from_order_multiple_unavailable_variants` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:754]
- `test_checkout_create_from_order_with_the_same_variant_in_multiple_lines` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:815]
- `test_checkout_create_from_order_channel_without_shipping_zones` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:857]
- `test_checkout_create_from_order_channel_without_shipping_zones_excluded_from_stock_calculations` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py:879]

**`saleor/graphql/checkout/tests/mutations/test_checkout_create.py`**

- `test_checkout_create_triggers_async_webhooks` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_create.py:73]

**`saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py`**

- `test_checkout_customer_attach` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py:35]
- `test_checkout_customer_attach_when_line_without_channel_listing` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py:71]
- `test_checkout_customer_attach_with_customer_id_same_as_in_request` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py:113]
- `test_checkout_customer_attach_no_customer_id` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py:140]
- `test_checkout_customer_attach_by_app` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py:167]
- `test_checkout_customer_attach_by_app_no_customer_id` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py:193]
- `test_checkout_customer_attach_by_app_without_permission` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py:218]
- `test_checkout_customer_attach_user_to_checkout_with_user` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py:239]
- `test_with_active_problems_flow` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py:276]
- `test_checkout_customer_triggers_webhooks` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py:308]
- `test_checkout_customer_attach_do_not_mark_shipping_as_stale` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py:383]

**`saleor/graphql/checkout/tests/mutations/test_checkout_customer_detach.py`**

- `test_checkout_customer_detach` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_detach.py:31]

**`saleor/graphql/checkout/tests/mutations/test_checkout_customer_note_update.py`**

- `test_checkout_customer_note_update` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_customer_note_update.py:36]

**`saleor/graphql/checkout/tests/mutations/test_checkout_delete.py`**

- `test_checkout_delete_by_staff` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_delete.py:23]
- `test_checkout_delete_by_app` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_delete.py:45]
- `test_checkout_delete_without_permission_is_denied` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_delete.py:68]

**`saleor/graphql/checkout/tests/mutations/test_checkout_email_update.py`**

- `test_anonymous_checkout_email_update` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_email_update.py:37]
- `test_authenticated_checkout_email_update` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_email_update.py:63]

**`saleor/graphql/checkout/tests/mutations/test_checkout_language_code_update.py`**

- `test_checkout_update_language_code` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_language_code_update.py:32]
- `test_checkout_update_language_code_when_variant_without_channel_listing` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_language_code_update.py:62]

**`saleor/graphql/checkout/tests/mutations/test_checkout_lines_delete.py`**

- `test_checkout_lines_delete` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_lines_delete.py:54]

**`saleor/graphql/checkout/tests/mutations/test_checkout_shipping_method_update_nullable_shipping_method_id.py`**

- `test_checkout_shipping_method_update_nullable_shipping_method_id` (function) — [saleor/graphql/checkout/tests/mutations/test_checkout_shipping_method_update_nullable_shipping_method_id.py:41]

**`saleor/graphql/checkout/tests/mutations/test_utils.py`**

- `test_group_on_add_when_same_variants_in_multiple_lines` (function) — [saleor/graphql/checkout/tests/mutations/test_utils.py:11]
- `test_group_on_add_when_same_variants_in_multiple_lines_and_price_provided` (function) — [saleor/graphql/checkout/tests/mutations/test_utils.py:50]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/checkout/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_add_promo_code.py` (1466 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_billing_address_update.py` (990 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_complete_price_override.py` (751 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_payment.py` (6389 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_complete_with_transactions.py` (6109 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_complete.py` (838 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_create_from_order.py` (902 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_create.py` (78 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_customer_attach.py` (425 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_customer_detach.py` (58 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_customer_note_update.py` (66 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_delete.py` (75 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_delivery_method_update.py` (66 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_email_update.py` (66 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_language_code_update.py` (71 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_lines_add.py` (63 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_lines_delete.py` (65 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_lines_update.py` (56 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_remove_promo_code.py` (65 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_shipping_address_update.py` (64 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_shipping_method_update_nullable_shipping_method_id.py` (70 lines)
- `saleor/graphql/checkout/tests/mutations/test_checkout_shipping_method_update.py` (68 lines)
- `saleor/graphql/checkout/tests/mutations/test_order_create_from_checkout.py` (48 lines)
- `saleor/graphql/checkout/tests/mutations/test_price_override_reason.py` (78 lines)
- `saleor/graphql/checkout/tests/mutations/test_utils.py` (56 lines)

## Interactions

- Imports from: `saleor/graphql/checkout/mutations`, `saleor/core`, `saleor/graphql`, `saleor/checkout/webhooks`, `saleor/graphql/product/dataloaders`, `saleor/plugins/tests`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.models.Address`
- `.....account.tests.fixtures.user.dangerously_create_test_user`
- `.....channel.MarkAsPaidStrategy`
- `.....channel.utils.DEPRECATION_WARNING_MESSAGE`
- `.....checkout.AddressType`
- `.....checkout.actions.call_checkout_event`
- `.....checkout.actions.call_checkout_info_event`
- `.....checkout.base_calculations`
- `.....checkout.calculations`
- `.....checkout.calculations.fetch_checkout_data`
- `.....checkout.delivery_context.get_or_fetch_checkout_deliveries`
- `.....checkout.error_codes.CheckoutCreateFromOrderUnavailableVariantErrorCode`
- `.....checkout.error_codes.CheckoutErrorCode`
- `.....checkout.error_codes.OrderCreateFromCheckoutErrorCode`
- `.....checkout.fetch.fetch_checkout_info`
- `.....checkout.fetch.fetch_checkout_lines`
- `.....checkout.models.Checkout`
- `.....checkout.models.CheckoutDelivery`
- `.....checkout.models.CheckoutLine`
- `.....checkout.payment_utils.update_checkout_payment_statuses`
- `.....checkout.tests.utils.add_variant_to_checkout`
- `.....checkout.utils.add_voucher_code_to_checkout`
- `.....checkout.utils.add_voucher_to_checkout`
- `.....checkout.utils.calculate_checkout_quantity`
- `.....checkout.utils.invalidate_checkout`
- `.....core.EventDeliveryStatus`
- `.....core.exceptions.InsufficientStock`
- `.....core.exceptions.InsufficientStockData`
- `.....core.models.EventDelivery`
- `.....core.taxes.TaxDataError`
- `.....core.taxes.TaxError`
- `.....core.taxes.zero_money`
- `.....core.taxes.zero_taxed_money`
- `.....discount.DiscountType`
- `.....discount.DiscountValueType`
- `.....discount.RewardType`
- `.....discount.RewardValueType`
- `.....discount.VoucherType`
- `.....discount.models.CheckoutLineDiscount`
- `.....discount.models.OrderLineDiscount`
- `.....discount.models.Promotion`
- `.....discount.models.PromotionRule`
- `.....discount.models.Voucher`
- `.....discount.models.VoucherChannelListing`
- `.....discount.models.VoucherCode`
- `.....giftcard.GiftCardEvents`
- `.....giftcard.models.GiftCard`
- `.....giftcard.models.GiftCardEvent`
- `.....order.OrderAuthorizeStatus`
- `.....order.OrderChargeStatus`
- `.....order.OrderOrigin`
- `.....order.OrderStatus`
- `.....order.delivery_context.PRIVATE_META_APP_SHIPPING_ID`
- `.....order.models.Fulfillment`
- `.....order.models.Order`
- `.....payment.ChargeStatus`
- `.....payment.PaymentError`
- `.....payment.TransactionEventType`
- `.....payment.TransactionKind`
- `.....payment.error_codes.PaymentErrorCode`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `97086c667482` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
