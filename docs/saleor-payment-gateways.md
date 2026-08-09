## Purpose

`saleor/payment/gateways` (`saleor/payment/gateways`) groups 13 source file(s) exposing 151 top-level declaration(s).

## Public surface

**`saleor/payment/gateways/stripe/plugin.py`**

- `StripeGatewayPlugin` (class) — [saleor/payment/gateways/stripe/plugin.py:56]
- `webhook` (function) — [saleor/payment/gateways/stripe/plugin.py:131]
- `token_is_required_as_payment_input` (function) — [saleor/payment/gateways/stripe/plugin.py:144]
- `get_supported_currencies` (function) — [saleor/payment/gateways/stripe/plugin.py:149]
- `order_auto_confirmation` (function) — [saleor/payment/gateways/stripe/plugin.py:155]
- `process_payment` (function) — [saleor/payment/gateways/stripe/plugin.py:190]
- `confirm_payment` (function) — [saleor/payment/gateways/stripe/plugin.py:293]
- `capture_payment` (function) — [saleor/payment/gateways/stripe/plugin.py:369]
- `refund_payment` (function) — [saleor/payment/gateways/stripe/plugin.py:406]
- `void_payment` (function) — [saleor/payment/gateways/stripe/plugin.py:438]
- `list_payment_sources` (function) — [saleor/payment/gateways/stripe/plugin.py:467]
- `pre_save_plugin_configuration` (function) — [saleor/payment/gateways/stripe/plugin.py:496]
- `validate_plugin_configuration` (function) — [saleor/payment/gateways/stripe/plugin.py:567]
- `get_payment_config` (function) — [saleor/payment/gateways/stripe/plugin.py:599]

**`saleor/payment/gateways/stripe/stripe_api.py`**

- `stripe_otel_trace` (function) — [saleor/payment/gateways/stripe/stripe_api.py:32]
- `is_secret_api_key_valid` (function) — [saleor/payment/gateways/stripe/stripe_api.py:37]
- `subscribe_webhook` (function) — [saleor/payment/gateways/stripe/stripe_api.py:58]
- `delete_webhook` (function) — [saleor/payment/gateways/stripe/stripe_api.py:84]
- `get_or_create_customer` (function) — [saleor/payment/gateways/stripe/stripe_api.py:96]
- `create_payment_intent` (function) — [saleor/payment/gateways/stripe/stripe_api.py:121]
- `update_payment_method` (function) — [saleor/payment/gateways/stripe/stripe_api.py:176]
- `list_customer_payment_methods` (function) — [saleor/payment/gateways/stripe/stripe_api.py:195]
- `retrieve_payment_intent` (function) — [saleor/payment/gateways/stripe/stripe_api.py:210]
- `capture_payment_intent` (function) — [saleor/payment/gateways/stripe/stripe_api.py:228]
- `refund_payment_intent` (function) — [saleor/payment/gateways/stripe/stripe_api.py:247]
- `cancel_payment_intent` (function) — [saleor/payment/gateways/stripe/stripe_api.py:266]
- `construct_stripe_event` (function) — [saleor/payment/gateways/stripe/stripe_api.py:285]
- `get_payment_method_details` (function) — [saleor/payment/gateways/stripe/stripe_api.py:294]

**`saleor/payment/gateways/stripe/tests/conftest.py`**

- `payment_stripe_for_checkout` (function) — [saleor/payment/gateways/stripe/tests/conftest.py:16]
- `inactive_payment_stripe_for_checkout` (function) — [saleor/payment/gateways/stripe/tests/conftest.py:41]
- `payment_stripe_for_order` (function) — [saleor/payment/gateways/stripe/tests/conftest.py:48]
- `stripe_plugin` (function) — [saleor/payment/gateways/stripe/tests/conftest.py:70]
- `fun` (function) — [saleor/payment/gateways/stripe/tests/conftest.py:71]
- `stripe_payment_intent` (function) — [saleor/payment/gateways/stripe/tests/conftest.py:120]
- `stripe_payment_intent_with_details` (function) — [saleor/payment/gateways/stripe/tests/conftest.py:135]

**`saleor/payment/gateways/stripe/tests/test_plugin_deprecated.py`**

- `test_process_payment_with_customer_and_future_usage` (function) — [saleor/payment/gateways/stripe/tests/test_plugin_deprecated.py:10]

**`saleor/payment/gateways/stripe/tests/test_plugin.py`**

- `test_validate_plugin_configuration_correct_configuration` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:28]
- `test_validate_plugin_configuration_incorrect_configuration` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:43]
- `test_validate_plugin_configuration_missing_required_fields` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:60]
- `test_validate_plugin_configuration_validate_only_when_active` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:80]
- `test_pre_save_plugin_configuration_removes_webhook_when_disabled` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:100]
- `get_field_from_plugin_configuration` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:121]
- `test_pre_save_plugin_configuration` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:132]
- `test_process_payment` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:158]
- `test_process_payment_with_disabled_include_receipt_email` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:215]
- `test_process_payment_with_enabled_include_receipt_email` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:274]
- `test_process_payment_with_customer` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:334]
- `test_process_payment_with_customer_and_future_usage` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:409]
- `test_process_payment_with_customer_and_future_usage_no_store` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:503]
- `test_process_payment_with_customer_and_payment_method` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:580]
- `test_process_payment_with_payment_method_types` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:677]
- `test_process_payment_offline` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:774]
- `test_process_payment_with_customer_and_payment_method_raises_authentication_error` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:872]
- `test_process_payment_with_customer_and_payment_method_raises_error` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:975]
- `test_process_payment_with_disabled_order_auto_confirmation` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1052]
- `test_process_payment_with_manual_capture` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1109]
- `test_process_payment_with_error` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1164]
- `test_confirm_payment_for_webhook` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1204]
- `test_confirm_payment_intent_without_details` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1247]
- `test_confirm_payment_intent_with_details` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1304]
- `test_confirm_payment_incorrect_payment_intent` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1361]
- `test_confirm_payment_action_required_status` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1402]
- `test_confirm_payment_processing_status` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1446]
- `test_capture_payment` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1490]
- `test_refund_payment` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1540]
- `test_void_payment` (function) — [saleor/payment/gateways/stripe/tests/test_plugin.py:1590]

**`saleor/payment/gateways/stripe/tests/test_stripe_api.py`**

- `test_is_secret_api_key_valid_incorrect_key` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:35]
- `test_is_secret_api_key_valid_correct_key` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:44]
- `test_subscribe_webhook_returns_webhook_object` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:54]
- `test_delete_webhook` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:73]
- `test_create_payment_intent_returns_intent_object` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:87]
- `test_create_payment_intent_with_customer` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:109]
- `test_create_payment_intent_manual_auto_capture` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:133]
- `test_create_payment_intent_returns_error` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:152]
- `test_update_payment_method` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:173]
- `test_retrieve_payment_intent` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:193]
- `test_retrieve_payment_intent_stripe_returns_error` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:211]
- `test_capture_payment_intent` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:231]
- `test_capture_payment_intent_stripe_returns_error` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:253]
- `test_refund_payment_intent` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:277]
- `test_refund_payment_intent_returns_error` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:299]
- `test_cancel_payment_intent` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:322]
- `test_cancel_payment_intent_stripe_returns_error` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:339]
- `test_get_or_create_customer_retrieve` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:358]
- `test_get_or_create_customer_failed_retrieve` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:377]
- `test_get_or_create_customer_create` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:398]
- `test_get_or_create_customer_failed_create` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:415]
- `test_list_customer_payment_methods` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:434]
- `test_list_customer_payment_methods_failed_to_fetch` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:455]
- `test_get_payment_method_details` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:476]
- `test_get_payment_method_details_missing_charges` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:505]
- `test_get_payment_method_details_missing_charges_data` (function) — [saleor/payment/gateways/stripe/tests/test_stripe_api.py:514]

**`saleor/payment/gateways/stripe/tests/test_webhooks.py`**

- `test_handle_successful_payment_intent_for_checkout` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:49]
- `test_handle_successful_payment_intent_for_checkout_inactive_payment` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:95]
- `test_handle_successful_payment_intent_when_order_creation_raises_exception` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:133]
- `test_handle_successful_payment_intent_with_metadata` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:174]
- `test_handle_successful_payment_intent_for_order` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:218]
- `test_handle_successful_payment_intent_for_order_with_auth_payment` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:242]
- `test_handle_successful_payment_intent_for_order_with_pending_payment` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:277]
- `test_handle_successful_payment_intent_different_checkout_channel_slug` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:317]
- `test_handle_successful_payment_intent_different_order_channel_slug` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:361]
- `test_handle_successful_payment_intent_checkout_with_voucher_ongoing_completing` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:392]
- `call_webhook_success_event` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:449]
- `test_handle_authorized_payment_intent_for_checkout` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:477]
- `test_handle_authorized_payment_intent_for_checkout_with_payment_details` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:523]
- `test_handle_authorized_payment_intent_for_checkout_inactive_payment` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:566]
- `test_handle_authorized_payment_intent_when_order_creation_raises_exception` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:597]
- `test_handle_authorized_payment_intent_for_order` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:635]
- `test_handle_authorized_payment_intent_for_processing_order_payment` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:658]
- `test_handle_authorized_payment_intent_with_metadata` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:685]
- `test_handle_authorized_payment_intent_different_order_channel_slug` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:729]
- `test_handle_authorized_payment_intent_different_checkout_channel_slug` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:765]
- `test_handle_processing_payment_intent_for_order` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:805]
- `test_handle_processing_payment_intent_for_checkout` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:826]
- `test_handle_processing_payment_intent_for_checkout_inactive_payment` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:865]
- `test_handle_processing_payment_intent_when_order_creation_raises_exception` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:898]
- `test_handle_processing_payment_intent_different_order_channel_slug` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:941]
- `test_handle_processing_payment_intent_different_checkout_channel_slug` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:971]
- `test_handle_failed_payment_intent_for_checkout` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1007]
- `test_handle_failed_payment_intent_for_order` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1038]
- `test_handle_failed_payment_intent_different_order_channel_slug` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1074]
- `test_handle_failed_payment_intent_different_checkout_channel_slug` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1117]
- `test_handle_fully_refund` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1154]
- `test_handle_partial_refund` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1188]
- `test_handle_refund_already_processed` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1222]
- `test_handle_refund_missing_refunds` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1262]
- `test_handle_refund_different_order_channel_slug` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1314]
- `test_handle_refund_different_checkout_channel_slug` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1366]
- `test_handle_webhook_events` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1420]
- `test_handle_webhook_events_when_secret_is_missing` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1459]
- `test_finalize_checkout_not_created_order_payment_refund` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1489]
- `test_finalize_checkout_not_created_checkout_variant_unavailable_order_refund` (function) — [saleor/payment/gateways/stripe/tests/test_webhooks.py:1517]
- _…and 11 more in this file_

**`saleor/payment/gateways/stripe/webhooks.py`**

- `handle_webhook` (function) — [saleor/payment/gateways/stripe/webhooks.py:51]
- `update_payment_method_details_from_intent` (function) — [saleor/payment/gateways/stripe/webhooks.py:291]
- `handle_authorized_payment_intent` (function) — [saleor/payment/gateways/stripe/webhooks.py:301]
- `handle_failed_payment_intent` (function) — [saleor/payment/gateways/stripe/webhooks.py:361]
- `handle_processing_payment_intent` (function) — [saleor/payment/gateways/stripe/webhooks.py:390]
- `handle_successful_payment_intent` (function) — [saleor/payment/gateways/stripe/webhooks.py:431]
- `handle_refund` (function) — [saleor/payment/gateways/stripe/webhooks.py:500]

**`saleor/payment/gateways/utils.py`**

- `get_supported_currencies` (function) — [saleor/payment/gateways/utils.py:8]

## How it works

The module's files, as provided to this run:

- `saleor/payment/gateways/utils.py` (25 lines)
- `saleor/payment/gateways/__init__.py` (1 lines)
- `saleor/payment/gateways/stripe/__init__.py` (1 lines)
- `saleor/payment/gateways/stripe/consts.py` (46 lines)
- `saleor/payment/gateways/stripe/plugin.py` (607 lines)
- `saleor/payment/gateways/stripe/stripe_api.py` (319 lines)
- `saleor/payment/gateways/stripe/tests/__init__.py` (1 lines)
- `saleor/payment/gateways/stripe/tests/conftest.py` (166 lines)
- `saleor/payment/gateways/stripe/tests/test_plugin_deprecated.py` (80 lines)
- `saleor/payment/gateways/stripe/tests/test_plugin.py` (1636 lines)
- `saleor/payment/gateways/stripe/tests/test_stripe_api.py` (520 lines)
- `saleor/payment/gateways/stripe/tests/test_webhooks.py` (1812 lines)
- `saleor/payment/gateways/stripe/webhooks.py` (558 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql`, `saleor/payment`
- Imported by: `saleor/plugins/tests`

Internal dependencies named in the source:

- `.....ChargeStatus`
- `.....TransactionKind`
- `.....checkout.calculations`
- `.....checkout.calculations.calculate_checkout_total_with_gift_cards`
- `.....checkout.complete_checkout.complete_checkout`
- `.....checkout.fetch.fetch_checkout_info`
- `.....checkout.fetch.fetch_checkout_lines`
- `.....order.actions.order_charged`
- `.....order.actions.order_refunded`
- `.....order.actions.order_voided`
- `.....payment.models.Transaction`
- `.....plugins.manager.get_plugins_manager`
- `.....plugins.models.PluginConfiguration`
- `.....tests.race_condition`
- `....ChargeStatus`
- `....PaymentError`
- `....TransactionKind`
- `....checkout.calculations.calculate_checkout_total_with_gift_cards`
- `....checkout.complete_checkout.complete_checkout`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....checkout.models.Checkout`
- `....core.tracing.otel_trace`
- `....core.transactions.transaction_with_commit_on_errors`
- `....core.utils.build_absolute_uri`
- `....core.utils.get_domain`
- `....graphql.core.SaleorContext`
- `....graphql.core.enums.PluginErrorCode`
- `....interface.GatewayResponse`
- `....interface.PaymentMethodInfo`
- `....interface.StorePaymentMethodEnum`
- `....models.Transaction`
- `....order.actions.order_charged`
- `....order.actions.order_refunded`
- `....order.actions.order_voided`
- `....order.fetch.fetch_order_info`
- `....order.models.Order`
- `....plugins.base_plugin.BasePlugin`
- `....plugins.base_plugin.ConfigurationTypeField`
- `....plugins.manager.get_plugins_manager`
- `....plugins.models.PluginConfiguration`
- `....utils.create_payment`
- `....utils.create_payment_information`
- `....utils.price_to_minor_unit`
- `...gateway.payment_refund_or_void`
- `...interface.GatewayConfig`
- `...interface.GatewayResponse`
- `...interface.PaymentMethodInfo`
- `...models.Payment`
- `...models.Transaction`
- `...utils.price_from_minor_unit`
- `...utils.price_to_minor_unit`
- `..consts.AUTOMATIC_CAPTURE_METHOD`
- `..consts.SUCCESS_STATUS`
- `..interface.GatewayConfig`
- `..plugin.StripeGatewayPlugin`
- `..utils.get_supported_currencies`
- `.webhooks.handle_webhook`
- `saleor.payment.interface.PaymentMethodInfo`
- `saleor.payment.utils.price_to_minor_unit`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `61bc46588f2e` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
