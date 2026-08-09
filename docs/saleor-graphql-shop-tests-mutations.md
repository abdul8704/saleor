## Purpose

`saleor/graphql/shop/tests/mutations` (`saleor/graphql/shop/tests/mutations`) groups 10 source file(s) exposing 81 top-level declaration(s).

## Public surface

**`saleor/graphql/shop/tests/mutations/test_gift_card_settings_update.py`**

- `test_gift_card_settings_update_by_staff` (function) — [saleor/graphql/shop/tests/mutations/test_gift_card_settings_update.py:27]
- `test_gift_card_settings_update_by_app` (function) — [saleor/graphql/shop/tests/mutations/test_gift_card_settings_update.py:65]
- `test_gift_card_settings_update_by_customer` (function) — [saleor/graphql/shop/tests/mutations/test_gift_card_settings_update.py:103]
- `test_gift_card_settings_update_with_the_same_type` (function) — [saleor/graphql/shop/tests/mutations/test_gift_card_settings_update.py:128]
- `test_gift_card_settings_update_change_to_expiry_period_no_data_given` (function) — [saleor/graphql/shop/tests/mutations/test_gift_card_settings_update.py:159]
- `test_gift_card_settings_update_change_to_never_expire` (function) — [saleor/graphql/shop/tests/mutations/test_gift_card_settings_update.py:190]

**`saleor/graphql/shop/tests/mutations/test_reason_reference_type_clear.py`**

- `test_refund_reason_reference_type_clear_by_staff_success` (function) — [saleor/graphql/shop/tests/mutations/test_reason_reference_type_clear.py:24]
- `test_refund_reason_reference_type_clear_by_app_success` (function) — [saleor/graphql/shop/tests/mutations/test_reason_reference_type_clear.py:53]
- `test_refund_reason_reference_type_clear_when_already_none` (function) — [saleor/graphql/shop/tests/mutations/test_reason_reference_type_clear.py:81]
- `test_refund_reason_reference_type_clear_multiple_page_types` (function) — [saleor/graphql/shop/tests/mutations/test_reason_reference_type_clear.py:110]
- `test_refund_reason_reference_type_clear_no_permission_staff` (function) — [saleor/graphql/shop/tests/mutations/test_reason_reference_type_clear.py:147]
- `test_refund_reason_reference_type_clear_no_permission_customer` (function) — [saleor/graphql/shop/tests/mutations/test_reason_reference_type_clear.py:160]
- `test_refund_reason_reference_type_clear_no_permission_anonymous` (function) — [saleor/graphql/shop/tests/mutations/test_reason_reference_type_clear.py:171]
- `test_refund_reason_reference_type_clear_app_no_permission` (function) — [saleor/graphql/shop/tests/mutations/test_reason_reference_type_clear.py:182]

**`saleor/graphql/shop/tests/mutations/test_refund_settings_update.py`**

- `test_refund_settings_update_by_staff_success` (function) — [saleor/graphql/shop/tests/mutations/test_refund_settings_update.py:27]
- `test_refund_settings_update_by_app_success` (function) — [saleor/graphql/shop/tests/mutations/test_refund_settings_update.py:59]
- `test_refund_settings_update_change_page_type` (function) — [saleor/graphql/shop/tests/mutations/test_refund_settings_update.py:88]
- `test_refund_settings_update_empty_id_returns_error` (function) — [saleor/graphql/shop/tests/mutations/test_refund_settings_update.py:122]
- `test_refund_settings_update_invalid_id_format` (function) — [saleor/graphql/shop/tests/mutations/test_refund_settings_update.py:148]
- `test_refund_settings_update_nonexistent_page_type` (function) — [saleor/graphql/shop/tests/mutations/test_refund_settings_update.py:174]
- `test_refund_settings_update_wrong_page_type` (function) — [saleor/graphql/shop/tests/mutations/test_refund_settings_update.py:200]
- `test_refund_settings_update_no_permission_staff` (function) — [saleor/graphql/shop/tests/mutations/test_refund_settings_update.py:230]
- `test_refund_settings_update_no_permission_customer` (function) — [saleor/graphql/shop/tests/mutations/test_refund_settings_update.py:242]
- `test_refund_settings_update_no_permission_anonymous` (function) — [saleor/graphql/shop/tests/mutations/test_refund_settings_update.py:254]
- `test_refund_settings_update_app_no_permission` (function) — [saleor/graphql/shop/tests/mutations/test_refund_settings_update.py:266]

**`saleor/graphql/shop/tests/mutations/test_return_reason_reference_type_clear.py`**

- `test_by_staff_success` (function) — [saleor/graphql/shop/tests/mutations/test_return_reason_reference_type_clear.py:23]
- `test_by_app_success` (function) — [saleor/graphql/shop/tests/mutations/test_return_reason_reference_type_clear.py:50]
- `test_when_already_none` (function) — [saleor/graphql/shop/tests/mutations/test_return_reason_reference_type_clear.py:76]
- `test_no_permission_staff` (function) — [saleor/graphql/shop/tests/mutations/test_return_reason_reference_type_clear.py:101]
- `test_no_permission_customer` (function) — [saleor/graphql/shop/tests/mutations/test_return_reason_reference_type_clear.py:113]
- `test_no_permission_anonymous` (function) — [saleor/graphql/shop/tests/mutations/test_return_reason_reference_type_clear.py:123]
- `test_app_no_permission` (function) — [saleor/graphql/shop/tests/mutations/test_return_reason_reference_type_clear.py:133]

**`saleor/graphql/shop/tests/mutations/test_return_settings_update.py`**

- `test_by_staff_success` (function) — [saleor/graphql/shop/tests/mutations/test_return_settings_update.py:27]
- `test_by_app_success` (function) — [saleor/graphql/shop/tests/mutations/test_return_settings_update.py:59]
- `test_change_page_type` (function) — [saleor/graphql/shop/tests/mutations/test_return_settings_update.py:88]
- `test_empty_id_returns_error` (function) — [saleor/graphql/shop/tests/mutations/test_return_settings_update.py:122]
- `test_nonexistent_page_type` (function) — [saleor/graphql/shop/tests/mutations/test_return_settings_update.py:148]
- `test_wrong_node_type` (function) — [saleor/graphql/shop/tests/mutations/test_return_settings_update.py:178]
- `test_invalid_id_format` (function) — [saleor/graphql/shop/tests/mutations/test_return_settings_update.py:202]
- `test_no_permission_staff` (function) — [saleor/graphql/shop/tests/mutations/test_return_settings_update.py:225]
- `test_no_permission_customer` (function) — [saleor/graphql/shop/tests/mutations/test_return_settings_update.py:237]
- `test_no_permission_anonymous` (function) — [saleor/graphql/shop/tests/mutations/test_return_settings_update.py:249]
- `test_app_no_permission` (function) — [saleor/graphql/shop/tests/mutations/test_return_settings_update.py:261]

**`saleor/graphql/shop/tests/mutations/test_shop_address_update.py`**

- `test_mutation_update_company_address` (function) — [saleor/graphql/shop/tests/mutations/test_shop_address_update.py:16]
- `test_mutation_update_company_address_remove_address` (function) — [saleor/graphql/shop/tests/mutations/test_shop_address_update.py:53]
- `test_mutation_update_company_address_remove_address_without_address` (function) — [saleor/graphql/shop/tests/mutations/test_shop_address_update.py:77]
- `test_shop_address_update_skip_validation` (function) — [saleor/graphql/shop/tests/mutations/test_shop_address_update.py:98]

**`saleor/graphql/shop/tests/mutations/test_shop_settings_update.py`**

- `test_shop_settings_mutation` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:48]
- `test_shop_reservation_settings_mutation` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:95]
- `test_shop_reservation_disable_settings_mutation` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:122]
- `test_shop_reservation_set_negative_settings_mutation` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:149]
- `test_limit_quantity_per_checkout_mutation` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:177]
- `test_limit_quantity_per_checkout_neg_or_zero_value` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:199]
- `test_shop_customer_set_password_url_update` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:226]
- `test_shop_customer_set_password_url_update_invalid_url` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:258]
- `test_shop_settings_update_preserve_all_address_fields_enable` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:303]
- `test_shop_settings_update_preserve_all_address_fields_disable` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:326]
- `test_shop_settings_update_use_legacy_shipping_zone_stock_availability_disable` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:366]
- `test_shop_settings_update_use_legacy_shipping_zone_stock_availability_enable` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:403]
- `test_update_default_sender_settings` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:455]
- `test_update_default_sender_settings_invalid_name` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:490]
- `test_update_default_sender_settings_invalid_email` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:523]
- `test_shop_settings_update_password_login_mode_blocked_for_password_auth` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:565]
- `test_shop_settings_update_password_login_mode_allowed_for_oidc_auth` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:597]
- `test_shop_settings_update_password_login_mode_preserves_when_not_provided` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:623]
- `test_shop_settings_update_account_merge_requires_permission` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:664]
- `test_shop_settings_update_account_merge_mode` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:727]
- `test_shop_settings_update_account_merge_mode_omitted` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:763]
- `test_shop_settings_update_account_merge_only_valid_values` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:790]
- `test_shop_settings_update_name` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:835]
- `test_shop_settings_update_name_too_long` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:861]
- `test_shop_settings_update_sets_allow_storefront_traffic` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:899]
- `test_shop_settings_update_allow_storefront_traffic_requires_permission` (function) — [saleor/graphql/shop/tests/mutations/test_shop_settings_update.py:932]

**`saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_create.py`**

- `test_staff_notification_create_mutation` (function) — [saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_create.py:28]
- `test_staff_notification_create_mutation_with_staffs_email` (function) — [saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_create.py:60]
- `test_staff_notification_create_mutation_with_customer_user` (function) — [saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_create.py:92]
- `test_staff_notification_create_mutation_with_email` (function) — [saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_create.py:117]
- `test_staff_notification_create_mutation_with_empty_email` (function) — [saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_create.py:144]

**`saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_update.py`**

- `test_staff_notification_update_mutation` (function) — [saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_update.py:30]
- `test_staff_notification_update_mutation_with_empty_user` (function) — [saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_update.py:57]
- `test_staff_notification_update_mutation_with_empty_email` (function) — [saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_update.py:92]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/shop/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/shop/tests/mutations/test_gift_card_settings_update.py` (218 lines)
- `saleor/graphql/shop/tests/mutations/test_reason_reference_type_clear.py` (190 lines)
- `saleor/graphql/shop/tests/mutations/test_refund_settings_update.py` (275 lines)
- `saleor/graphql/shop/tests/mutations/test_return_reason_reference_type_clear.py` (140 lines)
- `saleor/graphql/shop/tests/mutations/test_return_settings_update.py` (270 lines)
- `saleor/graphql/shop/tests/mutations/test_shop_address_update.py` (121 lines)
- `saleor/graphql/shop/tests/mutations/test_shop_settings_update.py` (948 lines)
- `saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_create.py` (170 lines)
- `saleor/graphql/shop/tests/mutations/test_staff_notification_recipient_update.py` (124 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.models.Address`
- `.....core.TimePeriodType`
- `.....core.error_codes.ShopErrorCode`
- `.....core.jwt.JWT_OWNER_FIELD`
- `.....page.models.PageType`
- `.....site.GiftCardSettingsExpiryType`
- `.....site.error_codes.GiftCardSettingsErrorCode`
- `.....site.error_codes.RefundSettingsErrorCode`
- `.....site.error_codes.ReturnSettingsErrorCode`
- `.....site.models.Site`
- `....core.enums.TimePeriodTypeEnum`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...enums.AccountConfirmModeEnum`
- `...enums.GiftCardSettingsExpiryTypeEnum`
- `...enums.PasswordLoginModeEnum`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c0652c8b3007` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
