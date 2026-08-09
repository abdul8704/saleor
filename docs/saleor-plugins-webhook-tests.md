## Purpose

`saleor/plugins/webhook/tests` (`saleor/plugins/webhook/tests`) groups 15 source file(s) exposing 180 top-level declaration(s).

## Public surface

**`saleor/plugins/webhook/tests/conftest.py`**

- `webhook_plugin` (function) — [saleor/plugins/webhook/tests/conftest.py:8]
- `factory` (function) — [saleor/plugins/webhook/tests/conftest.py:9]

**`saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py`**

- `app_with_lifecycle_webhook` (function) — [saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py:39]
- `factory` (function) — [saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py:42]
- `test_app_receives_own_app_installed_without_manage_apps` (function) — [saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py:61]
- `test_app_receives_own_app_updated_without_manage_apps` (function) — [saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py:79]
- `test_app_receives_own_app_deleted_without_manage_apps` (function) — [saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py:97]
- `test_app_receives_own_app_status_changed_on_deactivate` (function) — [saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py:124]
- `test_unrelated_app_without_manage_apps_does_not_receive_lifecycle_event` (function) — [saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py:149]
- `test_admin_app_with_manage_apps_does_not_receive_events_about_other_apps` (function) — [saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py:166]
- `test_app_deleted_delivery_survives_worker_active_check` (function) — [saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py:186]
- `test_app_status_changed_delivery_survives_worker_active_check` (function) — [saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py:214]
- `test_app_status_changed_subscription_payload_snapshots_state_per_event` (function) — [saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py:238]

**`saleor/plugins/webhook/tests/test_list_stored_payment_methods_webhook.py`**

- `test_list_stored_payment_methods_with_static_payload` (function) — [saleor/plugins/webhook/tests/test_list_stored_payment_methods_webhook.py:38]
- `test_list_stored_payment_methods_subscription_issuing_principal` (function) — [saleor/plugins/webhook/tests/test_list_stored_payment_methods_webhook.py:95]
- `test_list_stored_payment_methods_subscription_issuing_principal_as_app` (function) — [saleor/plugins/webhook/tests/test_list_stored_payment_methods_webhook.py:143]
- `test_list_stored_payment_methods_with_subscription_payload` (function) — [saleor/plugins/webhook/tests/test_list_stored_payment_methods_webhook.py:194]
- `test_list_stored_payment_methods_uses_cache_if_available` (function) — [saleor/plugins/webhook/tests/test_list_stored_payment_methods_webhook.py:255]
- `test_list_stored_payment_methods_app_returns_incorrect_response` (function) — [saleor/plugins/webhook/tests/test_list_stored_payment_methods_webhook.py:309]

**`saleor/plugins/webhook/tests/test_payment_gateway_initialize_session_webhook.py`**

- `test_gateway_initialize_checkout_without_request_data_and_static_payload` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_session_webhook.py:93]
- `test_gateway_initialize_checkout_with_request_data_and_static_payload` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_session_webhook.py:129]
- `test_gateway_initialize_checkout_without_request_data` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_session_webhook.py:169]
- `test_gateway_initialize_checkout_with_request_data` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_session_webhook.py:207]
- `test_gateway_initialize_session_skips_app_without_identifier` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_session_webhook.py:248]
- `test_gateway_initialize_order_without_request_data_static_payload` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_session_webhook.py:280]
- `test_gateway_initialize_order_with_request_data_static_payload` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_session_webhook.py:316]
- `test_gateway_initialize_session_for_order_without_request_data` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_session_webhook.py:356]
- `test_gateway_initialize_session_for_order_with_request_data` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_session_webhook.py:395]

**`saleor/plugins/webhook/tests/test_payment_gateway_initialize_tokenization.py`**

- `webhook_payment_gateway_initialize_tokenization_response` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_tokenization.py:33]
- `test_payment_gateway_initialize_tokenization_with_static_payload` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_tokenization.py:43]
- `test_payment_gateway_initialize_tokenization_with_subscription_payload` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_tokenization.py:95]
- `test_payment_gateway_initialize_tokenization_missing_correct_response_from_webhook` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_tokenization.py:152]
- `test_payment_gateway_initialize_tokenization_failure_from_app` (function) — [saleor/plugins/webhook/tests/test_payment_gateway_initialize_tokenization.py:201]

**`saleor/plugins/webhook/tests/test_payment_method_initialize_tokenization.py`**

- `webhook_payment_method_initialize_tokenization_response` (function) — [saleor/plugins/webhook/tests/test_payment_method_initialize_tokenization.py:43]
- `test_payment_method_initialize_tokenization_with_static_payload` (function) — [saleor/plugins/webhook/tests/test_payment_method_initialize_tokenization.py:52]
- `test_payment_method_initialize_tokenization_with_subscription_payload` (function) — [saleor/plugins/webhook/tests/test_payment_method_initialize_tokenization.py:110]
- `test_payment_method_initialize_tokenization_missing_correct_response_from_webhook` (function) — [saleor/plugins/webhook/tests/test_payment_method_initialize_tokenization.py:173]
- `test_payment_method_initialize_tokenization_failure_from_app` (function) — [saleor/plugins/webhook/tests/test_payment_method_initialize_tokenization.py:224]
- `test_payment_method_initialize_tokenization_additional_action_required` (function) — [saleor/plugins/webhook/tests/test_payment_method_initialize_tokenization.py:283]
- `test_payment_method_initialize_tokenization_missing_required_id` (function) — [saleor/plugins/webhook/tests/test_payment_method_initialize_tokenization.py:352]
- `test_expected_result_invalidates_cache_for_app` (function) — [saleor/plugins/webhook/tests/test_payment_method_initialize_tokenization.py:422]

**`saleor/plugins/webhook/tests/test_payment_method_process_tokenization.py`**

- `webhook_payment_method_process_tokenization_response` (function) — [saleor/plugins/webhook/tests/test_payment_method_process_tokenization.py:42]
- `test_payment_method_process_tokenization_with_static_payload` (function) — [saleor/plugins/webhook/tests/test_payment_method_process_tokenization.py:51]
- `test_payment_method_process_tokenization_with_subscription_payload` (function) — [saleor/plugins/webhook/tests/test_payment_method_process_tokenization.py:112]
- `test_payment_method_process_tokenization_missing_correct_response_from_webhook` (function) — [saleor/plugins/webhook/tests/test_payment_method_process_tokenization.py:178]
- `test_payment_method_process_tokenization_failure_from_app` (function) — [saleor/plugins/webhook/tests/test_payment_method_process_tokenization.py:230]
- `test_payment_method_process_tokenization_additional_action_required` (function) — [saleor/plugins/webhook/tests/test_payment_method_process_tokenization.py:292]
- `test_payment_method_process_tokenization_missing_required_id` (function) — [saleor/plugins/webhook/tests/test_payment_method_process_tokenization.py:363]
- `test_expected_result_invalidates_cache_for_app` (function) — [saleor/plugins/webhook/tests/test_payment_method_process_tokenization.py:434]

**`saleor/plugins/webhook/tests/test_payment_webhook.py`**

- `payment_invalid_app` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:37]
- `payment_removed_app` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:47]
- `WebhookTestData` (class) — [saleor/plugins/webhook/tests/test_payment_webhook.py:58]
- `webhook_data` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:66]
- `test_send_webhook_request_sync_failed_attempt` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:78]
- `test_send_webhook_request_sync_successful_attempt` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:111]
- `test_send_webhook_request_sync_request_exception` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:147]
- `test_send_webhook_request_sync_when_exception_with_response` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:179]
- `test_send_webhook_request_sync_json_parsing_error` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:200]
- `test_send_webhook_request_with_proper_timeout` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:231]
- `test_send_webhook_request_sync_invalid_scheme` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:240]
- `test_get_payment_gateways` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:258]
- `test_get_payment_gateways_with_transactions` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:300]
- `test_get_payment_gateways_with_transactions_and_app_without_identifier` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:331]
- `test_get_payment_gateways_multiple_webhooks_in_the_same_app` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:358]
- `test_get_payment_gateways_filters_out_unsupported_currencies` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:402]
- `test_get_payment_gateways_for_checkout` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:421]
- `test_run_payment_webhook` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:451]
- `test_run_payment_webhook_invalid_app` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:473]
- `test_run_payment_webhook_removed_app_by_id` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:485]
- `test_run_payment_webhook_removed_app_by_app_identifier` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:500]
- `test_run_payment_webhook_no_payment_app_data` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:521]
- `test_run_payment_webhook_inactive_plugin` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:534]
- `test_run_payment_webhook_no_response` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:549]
- `test_run_payment_webhook_empty_response` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:564]
- `test_check_plugin_id` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:579]
- `test_webhook_plugin_token_is_not_required` (function) — [saleor/plugins/webhook/tests/test_payment_webhook.py:586]

**`saleor/plugins/webhook/tests/test_stored_payment_method_request_delete.py`**

- `webhook_stored_payment_method_request_delete_response` (function) — [saleor/plugins/webhook/tests/test_stored_payment_method_request_delete.py:41]
- `test_stored_payment_method_request_delete_with_static_payload` (function) — [saleor/plugins/webhook/tests/test_stored_payment_method_request_delete.py:48]
- `test_stored_payment_method_request_delete_with_subscription_payload` (function) — [saleor/plugins/webhook/tests/test_stored_payment_method_request_delete.py:101]
- `test_stored_payment_method_request_delete_failure_from_app` (function) — [saleor/plugins/webhook/tests/test_stored_payment_method_request_delete.py:158]
- `test_stored_payment_method_request_delete_missing_response_from_webhook` (function) — [saleor/plugins/webhook/tests/test_stored_payment_method_request_delete.py:216]
- `test_stored_payment_method_request_delete_incorrect_result_response_from_webhook` (function) — [saleor/plugins/webhook/tests/test_stored_payment_method_request_delete.py:265]
- `test_stored_payment_method_request_delete_missing_result_in_response_from_webhook` (function) — [saleor/plugins/webhook/tests/test_stored_payment_method_request_delete.py:316]
- `test_stored_payment_method_request_delete_invalidates_cache_for_app` (function) — [saleor/plugins/webhook/tests/test_stored_payment_method_request_delete.py:366]

**`saleor/plugins/webhook/tests/test_tax_webhook.py`**

- `tax_type` (function) — [saleor/plugins/webhook/tests/test_tax_webhook.py:9]
- `test_get_tax_code_from_object_meta_no_app` (function) — [saleor/plugins/webhook/tests/test_tax_webhook.py:16]
- `test_get_tax_code_from_object_meta` (function) — [saleor/plugins/webhook/tests/test_tax_webhook.py:31]
- `test_get_tax_code_from_object_meta_default_code` (function) — [saleor/plugins/webhook/tests/test_tax_webhook.py:51]

**`saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py`**

- `test_transaction_initialize_checkout_without_request_data_and_static_payload` (function) — [saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py:137]
- `test_transaction_initialize_checkout_with_request_data_and_static_payload` (function) — [saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py:205]
- `test_transaction_initialize_checkout_without_request_data` (function) — [saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py:274]
- `test_transaction_initialize_checkout_without_request_data_app_requestor` (function) — [saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py:351]
- `test_transaction_initialize_checkout_with_request_data` (function) — [saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py:427]
- `test_transaction_initialize_session_skips_app_without_identifier` (function) — [saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py:500]
- `test_transaction_initialize_order_without_request_data_and_static_payload` (function) — [saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py:565]
- `test_transaction_initialize_order_with_request_data_and_static_payload` (function) — [saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py:633]
- `test_transaction_initialize_order_without_request_data` (function) — [saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py:702]
- `test_transaction_initialize_order_with_request_data` (function) — [saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py:774]

**`saleor/plugins/webhook/tests/test_transaction_process_session_webhook.py`**

- `test_transaction_process_checkout_without_request_data_and_static_payload` (function) — [saleor/plugins/webhook/tests/test_transaction_process_session_webhook.py:121]
- `test_transaction_process_checkout_with_request_data_and_static_payload` (function) — [saleor/plugins/webhook/tests/test_transaction_process_session_webhook.py:189]
- `test_transaction_process_checkout_without_request_data` (function) — [saleor/plugins/webhook/tests/test_transaction_process_session_webhook.py:258]
- `test_transaction_process_checkout_with_request_data` (function) — [saleor/plugins/webhook/tests/test_transaction_process_session_webhook.py:327]
- `test_transaction_process_session_skips_app_without_identifier` (function) — [saleor/plugins/webhook/tests/test_transaction_process_session_webhook.py:397]
- `test_transaction_process_order_without_request_data_and_static_payload` (function) — [saleor/plugins/webhook/tests/test_transaction_process_session_webhook.py:462]
- `test_transaction_process_order_with_request_data_and_static_payload` (function) — [saleor/plugins/webhook/tests/test_transaction_process_session_webhook.py:530]
- `test_transaction_process_order_without_request_data` (function) — [saleor/plugins/webhook/tests/test_transaction_process_session_webhook.py:599]
- `test_transaction_process_order_with_request_data` (function) — [saleor/plugins/webhook/tests/test_transaction_process_session_webhook.py:668]

**`saleor/plugins/webhook/tests/test_webhook.py`**

- `test_trigger_webhooks_for_event_calls_expected_events` (function) — [saleor/plugins/webhook/tests/test_webhook.py:83]
- `test_order_created` (function) — [saleor/plugins/webhook/tests/test_webhook.py:137]
- `test_order_confirmed` (function) — [saleor/plugins/webhook/tests/test_webhook.py:165]
- `test_draft_order_created` (function) — [saleor/plugins/webhook/tests/test_webhook.py:194]
- `test_draft_order_deleted` (function) — [saleor/plugins/webhook/tests/test_webhook.py:223]
- `test_draft_order_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:252]
- `test_customer_created` (function) — [saleor/plugins/webhook/tests/test_webhook.py:281]
- `test_customer_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:309]
- `test_customer_metadata_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:337]
- `test_order_fully_paid` (function) — [saleor/plugins/webhook/tests/test_webhook.py:365]
- `test_order_paid` (function) — [saleor/plugins/webhook/tests/test_webhook.py:393]
- `test_order_refunded` (function) — [saleor/plugins/webhook/tests/test_webhook.py:426]
- `test_order_fully_refunded` (function) — [saleor/plugins/webhook/tests/test_webhook.py:459]
- `test_collection_created` (function) — [saleor/plugins/webhook/tests/test_webhook.py:492]
- `test_collection_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:520]
- `test_collection_deleted` (function) — [saleor/plugins/webhook/tests/test_webhook.py:548]
- `test_collection_metadata_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:576]
- `test_product_created` (function) — [saleor/plugins/webhook/tests/test_webhook.py:605]
- `test_product_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:633]
- `test_product_deleted` (function) — [saleor/plugins/webhook/tests/test_webhook.py:661]
- `test_product_metadata_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:705]
- `test_product_variant_created` (function) — [saleor/plugins/webhook/tests/test_webhook.py:734]
- `test_product_variant_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:762]
- `test_product_variant_deleted` (function) — [saleor/plugins/webhook/tests/test_webhook.py:790]
- `test_product_variant_metadata_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:818]
- `test_order_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:847]
- `test_order_cancelled` (function) — [saleor/plugins/webhook/tests/test_webhook.py:876]
- `test_order_expired` (function) — [saleor/plugins/webhook/tests/test_webhook.py:905]
- `test_order_metadata_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:934]
- `test_checkout_created` (function) — [saleor/plugins/webhook/tests/test_webhook.py:963]
- `test_checkout_payload_includes_promotions` (function) — [saleor/plugins/webhook/tests/test_webhook.py:990]
- `test_checkout_payload_includes_order_promotion_discount` (function) — [saleor/plugins/webhook/tests/test_webhook.py:1055]
- `test_checkout_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:1110]
- `test_checkout_fully_paid` (function) — [saleor/plugins/webhook/tests/test_webhook.py:1140]
- `test_checkout_fully_authorized` (function) — [saleor/plugins/webhook/tests/test_webhook.py:1174]
- `test_checkout_metadata_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:1207]
- `test_page_created` (function) — [saleor/plugins/webhook/tests/test_webhook.py:1236]
- `test_page_updated` (function) — [saleor/plugins/webhook/tests/test_webhook.py:1260]
- `test_page_deleted` (function) — [saleor/plugins/webhook/tests/test_webhook.py:1284]
- `test_invoice_request` (function) — [saleor/plugins/webhook/tests/test_webhook.py:1311]
- _…and 32 more in this file_

**`saleor/plugins/webhook/tests/utils.py`**

- `generate_request_headers` (function) — [saleor/plugins/webhook/tests/utils.py:1]

## How it works

The module's files, as provided to this run:

- `saleor/plugins/webhook/tests/__init__.py` (1 lines)
- `saleor/plugins/webhook/tests/conftest.py` (15 lines)
- `saleor/plugins/webhook/tests/test_app_lifecycle_webhooks.py` (276 lines)
- `saleor/plugins/webhook/tests/test_list_stored_payment_methods_webhook.py` (359 lines)
- `saleor/plugins/webhook/tests/test_payment_gateway_initialize_session_webhook.py` (432 lines)
- `saleor/plugins/webhook/tests/test_payment_gateway_initialize_tokenization.py` (253 lines)
- `saleor/plugins/webhook/tests/test_payment_method_initialize_tokenization.py` (535 lines)
- `saleor/plugins/webhook/tests/test_payment_method_process_tokenization.py` (545 lines)
- `saleor/plugins/webhook/tests/test_payment_webhook.py` (588 lines)
- `saleor/plugins/webhook/tests/test_stored_payment_method_request_delete.py` (469 lines)
- `saleor/plugins/webhook/tests/test_tax_webhook.py` (66 lines)
- `saleor/plugins/webhook/tests/test_transaction_initialize_session_webhook.py` (842 lines)
- `saleor/plugins/webhook/tests/test_transaction_process_session_webhook.py` (733 lines)
- `saleor/plugins/webhook/tests/test_webhook.py` (2451 lines)
- `saleor/plugins/webhook/tests/utils.py` (12 lines)

## Interactions

- Imports from: `saleor/webhook/transport/asynchronous`, `saleor/webhook`, `saleor/webhook/transport/synchronous`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....__version__`
- `....app.models.App`
- `....channel.TransactionFlowStrategy`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....core.EventDeliveryStatus`
- `....core.models.EventDelivery`
- `....core.models.EventDeliveryAttempt`
- `....core.models.EventPayload`
- `....core.notification.utils.get_site_context`
- `....core.notify.NotifyEventType`
- `....core.taxes.TaxType`
- `....core.tokens.account_confirm_token_generator`
- `....core.utils.url.prepare_url`
- `....discount.DiscountType`
- `....discount.DiscountValueType`
- `....discount.RewardType`
- `....discount.RewardValueType`
- `....discount.interface.VariantPromotionRuleInfo`
- `....graphql.discount.enums.DiscountValueTypeEnum`
- `....graphql.discount.utils.convert_migrated_sale_predicate_to_catalogue_info`
- `....graphql.order.tests.mutations.test_order_discount.ORDER_DISCOUNT_UPDATE`
- `....payment.PaymentError`
- `....payment.TokenizedPaymentFlow`
- `....payment.TransactionAction`
- `....payment.TransactionEventType`
- `....payment.TransactionKind`
- `....payment.interface.ListStoredPaymentMethodsRequestData`
- `....payment.interface.PaymentGateway`
- `....payment.interface.PaymentGatewayData`
- `....payment.interface.TransactionActionData`
- `....payment.models.TransactionItem`
- `....payment.utils.create_payment_information`
- `....plugins.manager.get_plugins_manager`
- `....plugins.webhook.plugin.WebhookPlugin`
- `....settings.WEBHOOK_SYNC_TIMEOUT`
- `....site.models.SiteSettings`
- `....webhook.const`
- `....webhook.const.WEBHOOK_CACHE_DEFAULT_TTL`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.event_types.WebhookEventSyncType`
- `....webhook.models.Webhook`
- `....webhook.models.WebhookEvent`
- `....webhook.transport.signature_for_payload`
- `....webhook.transport.utils.attempt_update`
- `....webhook.transport.utils.generate_cache_key_for_webhook`
- `....webhook.transport.utils.get_multiple_deliveries_for_webhooks`
- `....webhook.utils.get_webhooks_for_event`
- `...manager.get_plugins_manager`
- `.utils.generate_request_headers`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `feb5bb43e7b3` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
