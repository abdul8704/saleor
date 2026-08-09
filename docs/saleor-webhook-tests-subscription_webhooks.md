## Purpose

`saleor/webhook/tests/subscription_webhooks` (`saleor/webhook/tests/subscription_webhooks`) groups 18 source file(s) exposing 260 top-level declaration(s).

## Public surface

**`saleor/webhook/tests/subscription_webhooks/payloads.py`**

- `generate_account_events_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:15]
- `generate_account_requested_events_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:23]
- `generate_app_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:46]
- `generate_attribute_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:63]
- `generate_attribute_value_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:80]
- `generate_taxed_money_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:96]
- `generate_variant_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:104]
- `generate_fulfillment_lines_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:115]
- `generate_fulfillment_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:131]
- `generate_address_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:160]
- `generate_customer_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:176]
- `generate_staff_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:208]
- `generate_collection_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:224]
- `generate_page_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:251]
- `generate_page_type_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:289]
- `generate_product_type_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:307]
- `generate_permission_group_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:324]
- `generate_invoice_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:340]
- `generate_category_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:365]
- `generate_shipping_method_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:396]
- `generate_sale_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:425]
- `generate_promotion_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:453]
- `generate_promotion_rule_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:469]
- `generate_voucher_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:491]
- `generate_voucher_code_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:508]
- `generate_voucher_created_payload_with_meta` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:528]
- `generate_gift_card_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:565]
- `generate_export_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:582]
- `generate_menu_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:601]
- `generate_menu_item_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:623]
- `generate_warehouse_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:648]
- `generate_payment_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:676]
- `generate_shop_payload` (function) — [saleor/webhook/tests/subscription_webhooks/payloads.py:692]

**`saleor/webhook/tests/subscription_webhooks/subscription_queries.py`**

- `TranslationQueryType` (class) — [saleor/webhook/tests/subscription_webhooks/subscription_queries.py:2513]
- `build_translation_query` (function) — [saleor/webhook/tests/subscription_webhooks/subscription_queries.py:2518]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_list_payment_methods.py`**

- `test_list_stored_payment_methods` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_list_payment_methods.py:27]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_gateway_initialize_session.py`**

- `test_payment_gateway_initialize_session_checkout_with_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_gateway_initialize_session.py:35]
- `test_payment_gateway_initialize_session_checkout_without_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_gateway_initialize_session.py:70]
- `test_payment_gateway_initialize_session_order_with_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_gateway_initialize_session.py:103]
- `test_payment_gateway_initialize_session_order_without_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_gateway_initialize_session.py:134]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_gateway_initialize_tokenization_session.py`**

- `test_payment_gateway_initialize_tokenization_without_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_gateway_initialize_tokenization_session.py:26]
- `test_payment_gateway_initialize_tokenization_with_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_gateway_initialize_tokenization_session.py:58]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_method_initialize_tokenization.py`**

- `test_payment_method_initialize_tokenization_without_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_method_initialize_tokenization.py:28]
- `test_payment_method_initialize_tokenization_with_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_method_initialize_tokenization.py:62]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_method_process_tokenization.py`**

- `test_payment_method_process_tokenization_without_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_method_process_tokenization.py:27]
- `test_payment_method_process_tokenization_with_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_method_process_tokenization.py:62]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_method_request_delete.py`**

- `test_stored_payment_method_request_delete` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_method_request_delete.py:26]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py`**

- `test_subscription_query_with_meta` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:62]
- `test_account_confirmation_requested` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:101]
- `test_account_confirmed` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:132]
- `test_account_confirmed_query_channel_without_channel_slug_in_payload` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:152]
- `test_account_change_email_requested` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:176]
- `test_account_email_changed` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:209]
- `test_account_delete_requested` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:230]
- `test_account_set_password_requested` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:259]
- `test_account_deleted_confirmed` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:290]
- `test_address_created` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:310]
- `test_address_updated` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:336]
- `test_address_deleted` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:361]
- `test_app_installed` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:391]
- `test_app_updated` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:409]
- `test_app_deleted` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:427]
- `test_app_status_changed` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:451]
- `test_attribute_created` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:473]
- `test_attribute_updated` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:492]
- `test_attribute_deleted` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:511]
- `test_attribute_value_created` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:535]
- `test_attribute_value_updated` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:556]
- `test_attribute_value_deleted` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:577]
- `test_category_created` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:603]
- `test_category_updated` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:626]
- `test_category_deleted` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:650]
- `test_channel_created` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:674]
- `test_channel_updated` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:690]
- `test_channel_deleted` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:706]
- `test_channel_status_changed` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:731]
- `test_gift_card_created` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:753]
- `test_gift_card_updated` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:771]
- `test_gift_card_deleted` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:789]
- `test_gift_card_sent` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:815]
- `test_gift_card_status_changed` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:853]
- `test_gift_card_metadata_updated` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:877]
- `test_gift_card_export_completed` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:897]
- `test_menu_created` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:927]
- `test_menu_updated` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:945]
- `test_menu_deleted` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:963]
- `test_menu_item_created` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py:989]
- _…and 120 more in this file_

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscriptions_payments.py`**

- `test_payment_authorize` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscriptions_payments.py:10]
- `test_payment_capture` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscriptions_payments.py:27]
- `test_payment_refund` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscriptions_payments.py:44]
- `test_payment_void` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscriptions_payments.py:61]
- `test_payment_confirm` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscriptions_payments.py:78]
- `test_payment_process` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscriptions_payments.py:95]
- `test_payment_list_gateways` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscriptions_payments.py:112]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_cancelation_requested.py`**

- `test_order_transaction_cancel_request` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_cancelation_requested.py:39]
- `test_checkout_transaction_cancel_request` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_cancelation_requested.py:113]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_charge_requested.py`**

- `test_order_transaction_charge_request` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_charge_requested.py:39]
- `test_checkout_transaction_charge_request` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_charge_requested.py:114]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_initialize_session.py`**

- `test_transaction_initialize_session_checkout_with_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_initialize_session.py:56]
- `test_transaction_initialize_session_checkout_without_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_initialize_session.py:133]
- `test_transaction_initialize_session_order_with_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_initialize_session.py:203]
- `test_transaction_initialize_session_order_without_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_initialize_session.py:273]
- `test_transaction_initialize_session_empty_customer_ip_addess` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_initialize_session.py:342]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_process_session.py`**

- `test_transaction_process_session_checkout_with_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_process_session.py:54]
- `test_transaction_process_session_checkout_without_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_process_session.py:127]
- `test_transaction_process_session_order_with_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_process_session.py:194]
- `test_transaction_process_session_order_without_data` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_process_session.py:268]
- `test_transaction_process_session_empty_customer_ip_address` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_process_session.py:334]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_refund_requested.py`**

- `test_order_transaction_refund_request` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_refund_requested.py:75]
- `test_checkout_transaction_refund_request` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_refund_requested.py:150]
- `test_transaction_refund_request_with_granted_refund` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_refund_requested.py:238]

**`saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py`**

- `test_translation_created_product` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:9]
- `test_translation_created_product_variant` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:41]
- `test_translation_created_collection` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:73]
- `test_translation_created_category` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:105]
- `test_translation_created_attribute` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:137]
- `test_translation_created_attribute_value` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:169]
- `test_translation_created_page` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:203]
- `test_translation_created_shipping_method` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:235]
- `test_translation_created_promotion` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:270]
- `test_translation_created_promotion_converted_from_sale` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:302]
- `test_translation_created_promotion_rule` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:333]
- `test_translation_created_voucher` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:366]
- `test_translation_created_menu_item` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:398]
- `test_translation_updated_product` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:430]
- `test_translation_updated_product_variant` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:462]
- `test_translation_updated_collection` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:494]
- `test_translation_updated_category` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:526]
- `test_translation_updated_attribute` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:558]
- `test_translation_updated_attribute_value` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:590]
- `test_translation_updated_page` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:624]
- `test_translation_updated_shipping_method` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:656]
- `test_translation_updated_promotion` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:691]
- `test_translation_updated_promotion_rule` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:723]
- `test_translation_updated_voucher` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:756]
- `test_translation_updated_menu_item` (function) — [saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py:788]

**`saleor/webhook/tests/subscription_webhooks/test_webhook.py`**

- `test_trigger_webhooks_async` (function) — [saleor/webhook/tests/subscription_webhooks/test_webhook.py:22]
- `test_trigger_webhooks_async_for_multiple_objects` (function) — [saleor/webhook/tests/subscription_webhooks/test_webhook.py:59]
- `test_trigger_webhooks_async_no_subscription_webhooks` (function) — [saleor/webhook/tests/subscription_webhooks/test_webhook.py:124]
- `test_trigger_webhook_sync_with_subscription` (function) — [saleor/webhook/tests/subscription_webhooks/test_webhook.py:138]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/tests/subscription_webhooks/__init__.py` (1 lines)
- `saleor/webhook/tests/subscription_webhooks/payloads.py` (699 lines)
- `saleor/webhook/tests/subscription_webhooks/subscription_queries.py` (3289 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_list_payment_methods.py` (54 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_gateway_initialize_session.py` (161 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_gateway_initialize_tokenization_session.py` (89 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_method_initialize_tokenization.py` (95 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_method_process_tokenization.py` (95 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_payment_method_request_delete.py` (54 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscription.py` (3276 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_subscriptions_payments.py` (127 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_cancelation_requested.py` (196 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_charge_requested.py` (198 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_initialize_session.py` (408 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_process_session.py` (397 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_transaction_refund_requested.py` (334 lines)
- `saleor/webhook/tests/subscription_webhooks/test_create_deliveries_for_translation_subscription.py` (817 lines)
- `saleor/webhook/tests/subscription_webhooks/test_webhook.py` (159 lines)

## Interactions

- Imports from: `saleor/webhook/transport/asynchronous`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....__version__`
- `....channel.TransactionFlowStrategy`
- `....channel.models.Channel`
- `....core.models.EventDelivery`
- `....core.prices.quantize_price`
- `....core.utils.build_absolute_uri`
- `....discount.models.Promotion`
- `....giftcard.models.GiftCard`
- `....graphql.attribute.enums.AttributeInputTypeEnum`
- `....graphql.attribute.enums.AttributeTypeEnum`
- `....graphql.discount.utils.get_categories_from_predicate`
- `....graphql.shop.types.SHOP_ID`
- `....graphql.tests.queries.fragments`
- `....graphql.webhook.subscription_query.SubscriptionQuery`
- `....graphql.webhook.subscription_types.TRANSLATIONS_TYPES_MAP`
- `....menu.models.Menu`
- `....menu.models.MenuItem`
- `....payment.TokenizedPaymentFlow`
- `....payment.TransactionAction`
- `....payment.TransactionEventType`
- `....payment.interface.ListStoredPaymentMethodsRequestData`
- `....payment.interface.PaymentGatewayInitializeTokenizationRequestData`
- `....payment.interface.PaymentMethodInitializeTokenizationRequestData`
- `....payment.interface.PaymentMethodProcessTokenizationRequestData`
- `....payment.interface.StoredPaymentMethodRequestDeleteData`
- `....payment.interface.TransactionActionData`
- `....payment.models.TransactionItem`
- `....product.interface.VariantDiscountedPriceChange`
- `....product.models.Category`
- `....product.models.Product`
- `....site.models.SiteSettings`
- `...event_types.WebhookEventAsyncType`
- `...event_types.WebhookEventSyncType`
- `...models.Webhook`
- `...transport.asynchronous.create_deliveries_for_subscriptions`
- `...transport.asynchronous.transport.create_deliveries_for_subscriptions`
- `...transport.asynchronous.trigger_webhooks_async`
- `...transport.synchronous.transport.trigger_webhook_sync_promise`
- `...transport.utils.get_sqs_message_group_id`
- `..subscription_queries`
- `.payloads.generate_payment_payload`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `841e17ce744a` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
