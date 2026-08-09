## Purpose

`saleor/plugins/tests` (`saleor/plugins/tests`) groups 14 source file(s) exposing 200 top-level declaration(s).

## Public surface

**`saleor/plugins/tests/fixtures/gateway.py`**

- `setup_dummy_gateway` (function) — [saleor/plugins/tests/fixtures/gateway.py:5]
- `sample_gateway` (function) — [saleor/plugins/tests/fixtures/gateway.py:11]

**`saleor/plugins/tests/fixtures/plugin_configuration.py`**

- `plugin_configuration` (function) — [saleor/plugins/tests/fixtures/plugin_configuration.py:15]
- `email_configuration` (function) — [saleor/plugins/tests/fixtures/plugin_configuration.py:30]
- `channel_plugin_configurations` (function) — [saleor/plugins/tests/fixtures/plugin_configuration.py:44]
- `inactive_plugin_configuration` (function) — [saleor/plugins/tests/fixtures/plugin_configuration.py:72]
- `new_config` (function) — [saleor/plugins/tests/fixtures/plugin_configuration.py:85]
- `new_config_structure` (function) — [saleor/plugins/tests/fixtures/plugin_configuration.py:90]

**`saleor/plugins/tests/fixtures/plugin_manager.py`**

- `plugins_manager` (function) — [saleor/plugins/tests/fixtures/plugin_manager.py:8]
- `all_plugins_manager` (function) — [saleor/plugins/tests/fixtures/plugin_manager.py:13]

**`saleor/plugins/tests/gateways/dummy.py`**

- `dummy_success` (function) — [saleor/plugins/tests/gateways/dummy.py:41]
- `validate_token` (function) — [saleor/plugins/tests/gateways/dummy.py:45]
- `get_client_token` (function) — [saleor/plugins/tests/gateways/dummy.py:49]
- `authorize` (function) — [saleor/plugins/tests/gateways/dummy.py:83]
- `void` (function) — [saleor/plugins/tests/gateways/dummy.py:97]
- `capture` (function) — [saleor/plugins/tests/gateways/dummy.py:104]
- `confirm` (function) — [saleor/plugins/tests/gateways/dummy.py:118]
- `refund` (function) — [saleor/plugins/tests/gateways/dummy.py:127]
- `process_payment` (function) — [saleor/plugins/tests/gateways/dummy.py:134]
- `DummyGatewayPlugin` (class) — [saleor/plugins/tests/gateways/dummy.py:158]
- `authorize_payment` (function) — [saleor/plugins/tests/gateways/dummy.py:178]
- `capture_payment` (function) — [saleor/plugins/tests/gateways/dummy.py:185]
- `confirm_payment` (function) — [saleor/plugins/tests/gateways/dummy.py:192]
- `refund_payment` (function) — [saleor/plugins/tests/gateways/dummy.py:199]
- `void_payment` (function) — [saleor/plugins/tests/gateways/dummy.py:206]
- `process_payment` (function) — [saleor/plugins/tests/gateways/dummy.py:213]
- `get_client_token` (function) — [saleor/plugins/tests/gateways/dummy.py:220]
- `get_supported_currencies` (function) — [saleor/plugins/tests/gateways/dummy.py:225]
- `get_payment_config` (function) — [saleor/plugins/tests/gateways/dummy.py:231]

**`saleor/plugins/tests/sample_plugins.py`**

- `PluginSample` (class) — [saleor/plugins/tests/sample_plugins.py:29]
- `webhook` (function) — [saleor/plugins/tests/sample_plugins.py:70]
- `calculate_checkout_total` (function) — [saleor/plugins/tests/sample_plugins.py:79]
- `calculate_checkout_shipping` (function) — [saleor/plugins/tests/sample_plugins.py:83]
- `calculate_order_shipping` (function) — [saleor/plugins/tests/sample_plugins.py:89]
- `calculate_checkout_line_total` (function) — [saleor/plugins/tests/sample_plugins.py:93]
- `calculate_order_line_total` (function) — [saleor/plugins/tests/sample_plugins.py:107]
- `calculate_checkout_line_unit_price` (function) — [saleor/plugins/tests/sample_plugins.py:121]
- `calculate_order_line_unit` (function) — [saleor/plugins/tests/sample_plugins.py:133]
- `get_tax_rate_type_choices` (function) — [saleor/plugins/tests/sample_plugins.py:148]
- `external_authentication_url` (function) — [saleor/plugins/tests/sample_plugins.py:151]
- `external_obtain_access_tokens` (function) — [saleor/plugins/tests/sample_plugins.py:156]
- `external_refresh` (function) — [saleor/plugins/tests/sample_plugins.py:163]
- `external_verify` (function) — [saleor/plugins/tests/sample_plugins.py:170]
- `authenticate_user` (function) — [saleor/plugins/tests/sample_plugins.py:176]
- `external_logout` (function) — [saleor/plugins/tests/sample_plugins.py:181]
- `sale_created` (function) — [saleor/plugins/tests/sample_plugins.py:186]
- `sale_updated` (function) — [saleor/plugins/tests/sample_plugins.py:194]
- `sale_deleted` (function) — [saleor/plugins/tests/sample_plugins.py:203]
- `sale_toggle` (function) — [saleor/plugins/tests/sample_plugins.py:211]
- `promotion_created` (function) — [saleor/plugins/tests/sample_plugins.py:220]
- `promotion_updated` (function) — [saleor/plugins/tests/sample_plugins.py:223]
- `promotion_deleted` (function) — [saleor/plugins/tests/sample_plugins.py:226]
- `promotion_started` (function) — [saleor/plugins/tests/sample_plugins.py:229]
- `promotion_ended` (function) — [saleor/plugins/tests/sample_plugins.py:232]
- `get_checkout_line_tax_rate` (function) — [saleor/plugins/tests/sample_plugins.py:235]
- `get_order_line_tax_rate` (function) — [saleor/plugins/tests/sample_plugins.py:245]
- `get_checkout_shipping_tax_rate` (function) — [saleor/plugins/tests/sample_plugins.py:256]
- `get_order_shipping_tax_rate` (function) — [saleor/plugins/tests/sample_plugins.py:265]
- `sample_not_implemented` (function) — [saleor/plugins/tests/sample_plugins.py:268]
- `event_delivery_retry` (function) — [saleor/plugins/tests/sample_plugins.py:271]
- `payment_gateway_initialize_session` (function) — [saleor/plugins/tests/sample_plugins.py:274]
- `transaction_initialize_session` (function) — [saleor/plugins/tests/sample_plugins.py:283]
- `transaction_process_session` (function) — [saleor/plugins/tests/sample_plugins.py:292]
- `checkout_fully_paid` (function) — [saleor/plugins/tests/sample_plugins.py:301]
- `checkout_fully_authorized` (function) — [saleor/plugins/tests/sample_plugins.py:304]
- `order_fully_refunded` (function) — [saleor/plugins/tests/sample_plugins.py:307]
- `order_paid` (function) — [saleor/plugins/tests/sample_plugins.py:310]
- `order_refunded` (function) — [saleor/plugins/tests/sample_plugins.py:313]
- `list_stored_payment_methods` (function) — [saleor/plugins/tests/sample_plugins.py:316]
- _…and 24 more in this file_

**`saleor/plugins/tests/test_email_common.py`**

- `test_validate_default_email_configuration_bad_email` (function) — [saleor/plugins/tests/test_email_common.py:28]
- `test_validate_default_email_configuration_correct_email` (function) — [saleor/plugins/tests/test_email_common.py:41]
- `test_validate_default_email_configuration_backend_raises` (function) — [saleor/plugins/tests/test_email_common.py:49]
- `test_validate_default_email_configuration_missing_smtp_values` (function) — [saleor/plugins/tests/test_email_common.py:88]
- `test_get_product_image_thumbnail` (function) — [saleor/plugins/tests/test_email_common.py:99]
- `test_get_product_image_thumbnail_simulate_json_dump_and_load` (function) — [saleor/plugins/tests/test_email_common.py:110]
- `test_get_product_image_thumbnail_image_missing` (function) — [saleor/plugins/tests/test_email_common.py:122]
- `test_get_plain_text_message_for_email` (function) — [saleor/plugins/tests/test_email_common.py:152]
- `test_send_email` (function) — [saleor/plugins/tests/test_email_common.py:167]

**`saleor/plugins/tests/test_manager.py`**

- `test_get_plugins_manager` (function) — [saleor/plugins/tests/test_manager.py:59]
- `test_manager_with_default_configuration_for_channel_plugins` (function) — [saleor/plugins/tests/test_manager.py:68]
- `test_manager_with_channel_plugins` (function) — [saleor/plugins/tests/test_manager.py:94]
- `test_manager_get_plugins_with_channel_slug` (function) — [saleor/plugins/tests/test_manager.py:116]
- `test_manager_get_active_plugins_with_channel_slug` (function) — [saleor/plugins/tests/test_manager.py:130]
- `test_manager_get_plugins_without_channel_slug` (function) — [saleor/plugins/tests/test_manager.py:145]
- `test_manager_get_active_plugins_without_channel_slug` (function) — [saleor/plugins/tests/test_manager.py:159]
- `test_manager_calculates_checkout_total` (function) — [saleor/plugins/tests/test_manager.py:178]
- `test_manager_calculates_checkout_subtotal` (function) — [saleor/plugins/tests/test_manager.py:200]
- `test_manager_calculates_checkout_shipping` (function) — [saleor/plugins/tests/test_manager.py:224]
- `test_manager_calculates_order_shipping` (function) — [saleor/plugins/tests/test_manager.py:245]
- `test_manager_calculates_checkout_line_total` (function) — [saleor/plugins/tests/test_manager.py:262]
- `test_manager_calculates_order_line_total` (function) — [saleor/plugins/tests/test_manager.py:291]
- `test_manager_get_checkout_line_tax_rate_sample_plugin` (function) — [saleor/plugins/tests/test_manager.py:316]
- `test_manager_get_checkout_line_tax_rate_no_plugins` (function) — [saleor/plugins/tests/test_manager.py:342]
- `test_manager_get_order_line_tax_rate_sample_plugin` (function) — [saleor/plugins/tests/test_manager.py:359]
- `test_manager_get_order_line_tax_rate_no_plugins` (function) — [saleor/plugins/tests/test_manager.py:383]
- `test_manager_get_checkout_shipping_tax_rate_sample_plugin` (function) — [saleor/plugins/tests/test_manager.py:400]
- `test_manager_get_checkout_shipping_tax_rate_no_plugins` (function) — [saleor/plugins/tests/test_manager.py:424]
- `test_manager_get_order_shipping_tax_rate_sample_plugin` (function) — [saleor/plugins/tests/test_manager.py:440]
- `test_manager_get_order_shipping_tax_rate_no_plugins` (function) — [saleor/plugins/tests/test_manager.py:458]
- `test_manager_calculates_checkout_line_unit_price` (function) — [saleor/plugins/tests/test_manager.py:490]
- `test_manager_calculates_order_line` (function) — [saleor/plugins/tests/test_manager.py:518]
- `test_manager_uses_get_tax_rate_choices` (function) — [saleor/plugins/tests/test_manager.py:543]
- `test_manager_sale_created` (function) — [saleor/plugins/tests/test_manager.py:547]
- `test_manager_sale_updated` (function) — [saleor/plugins/tests/test_manager.py:561]
- `test_manager_sale_deleted` (function) — [saleor/plugins/tests/test_manager.py:581]
- `test_manager_sale_toggle` (function) — [saleor/plugins/tests/test_manager.py:596]
- `test_manager_get_plugin_configuration` (function) — [saleor/plugins/tests/test_manager.py:611]
- `test_manager_save_plugin_configuration` (function) — [saleor/plugins/tests/test_manager.py:624]
- `test_plugin_updates_configuration_shape` (function) — [saleor/plugins/tests/test_manager.py:632]
- `test_plugin_add_new_configuration` (function) — [saleor/plugins/tests/test_manager.py:657]
- `test_manager_serve_list_of_payment_gateways` (function) — [saleor/plugins/tests/test_manager.py:678]
- `test_manager_serve_list_all_payment_gateways` (function) — [saleor/plugins/tests/test_manager.py:694]
- `test_manager_serve_list_all_payment_gateways_specified_currency` (function) — [saleor/plugins/tests/test_manager.py:718]
- `test_manager_serve_list_all_payment_gateways_specified_currency_two_gateways` (function) — [saleor/plugins/tests/test_manager.py:746]
- `test_manager_webhook` (function) — [saleor/plugins/tests/test_manager.py:782]
- `test_manager_webhook_plugin_doesnt_have_webhook_support` (function) — [saleor/plugins/tests/test_manager.py:797]
- `test_manager_inncorrect_plugin` (function) — [saleor/plugins/tests/test_manager.py:810]
- `test_manager_external_authentication` (function) — [saleor/plugins/tests/test_manager.py:823]
- _…and 40 more in this file_

**`saleor/plugins/tests/test_plugin_config_checks.py`**

- `test_empty_plugin_path` (function) — [saleor/plugins/tests/test_plugin_config_checks.py:6]
- `test_invalid_plugin_path` (function) — [saleor/plugins/tests/test_plugin_config_checks.py:12]

**`saleor/plugins/tests/test_plugins.py`**

- `test_update_config_items_keeps_bool_value` (function) — [saleor/plugins/tests/test_plugins.py:7]
- `test_update_config_items_convert_to_bool_value` (function) — [saleor/plugins/tests/test_plugins.py:20]
- `test_update_config_items_skips_new_keys_when_doesnt_exsist_in_conf_structure` (function) — [saleor/plugins/tests/test_plugins.py:34]
- `test_update_config_items_adds_new_keys` (function) — [saleor/plugins/tests/test_plugins.py:50]
- `test_update_configuration_structure_removes_old_keys` (function) — [saleor/plugins/tests/test_plugins.py:80]
- `test_save_plugin_configuration` (function) — [saleor/plugins/tests/test_plugins.py:95]
- `test_save_plugin_configuration_adds_new_field` (function) — [saleor/plugins/tests/test_plugins.py:106]
- `test_save_plugin_configuration_skips_new_field_when_doesnt_exsist_in_conf_structure` (function) — [saleor/plugins/tests/test_plugins.py:129]
- `test_save_plugin_do_not_remove_the_existing_fields` (function) — [saleor/plugins/tests/test_plugins.py:142]
- `test_base_plugin__update_configuration_structure_when_old_config_is_empty` (function) — [saleor/plugins/tests/test_plugins.py:166]
- `test_base_plugin__update_configuration_structure_configuration_has_change` (function) — [saleor/plugins/tests/test_plugins.py:181]
- `test_base_plugin__append_config_structure_to_config` (function) — [saleor/plugins/tests/test_plugins.py:207]

**`saleor/plugins/tests/test_views.py`**

- `test_plugin_webhook_view` (function) — [saleor/plugins/tests/test_views.py:19]
- `test_plugin_per_channel_webhook_view` (function) — [saleor/plugins/tests/test_views.py:40]
- `test_plugin_global_webhook_view` (function) — [saleor/plugins/tests/test_views.py:63]

**`saleor/plugins/tests/utils.py`**

- `get_config_value` (function) — [saleor/plugins/tests/utils.py:1]

## How it works

The module's files, as provided to this run:

- `saleor/plugins/tests/gateways/dummy.py` (235 lines)
- `saleor/plugins/tests/sample_plugins.py` (473 lines)
- `saleor/plugins/tests/__init__.py` (1 lines)
- `saleor/plugins/tests/fixtures/__init__.py` (3 lines)
- `saleor/plugins/tests/fixtures/gateway.py` (15 lines)
- `saleor/plugins/tests/fixtures/plugin_configuration.py` (91 lines)
- `saleor/plugins/tests/fixtures/plugin_manager.py` (15 lines)
- `saleor/plugins/tests/gateways/__init__.py` (1 lines)
- `saleor/plugins/tests/test_email_common.py` (190 lines)
- `saleor/plugins/tests/test_manager.py` (1626 lines)
- `saleor/plugins/tests/test_plugin_config_checks.py` (15 lines)
- `saleor/plugins/tests/test_plugins.py` (232 lines)
- `saleor/plugins/tests/test_views.py` (72 lines)
- `saleor/plugins/tests/utils.py` (7 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql/payment/mutations/stored_payment_methods`, `saleor/payment/gateways`, `saleor/payment`, `saleor/plugins`, `saleor/graphql/product/types`
- Imported by: `saleor/graphql/checkout/tests/mutations`, `saleor/graphql/payment/tests/mutations`

Internal dependencies named in the source:

- `...account.models.Address`
- `...account.models.User`
- `...base_plugin.ConfigurationTypeField`
- `...channel.TransactionFlowStrategy`
- `...checkout.fetch.CheckoutInfo`
- `...checkout.fetch.CheckoutLineInfo`
- `...checkout.fetch.fetch_checkout_info`
- `...checkout.fetch.fetch_checkout_lines`
- `...checkout.models.Checkout`
- `...core.models.EventDelivery`
- `...core.prices.quantize_price`
- `...core.taxes.TaxType`
- `...core.taxes.zero_money`
- `...core.taxes.zero_taxed_money`
- `...discount.models.Promotion`
- `...graphql.core.SaleorContext`
- `...graphql.discount.utils.convert_migrated_sale_predicate_to_catalogue_info`
- `...manager.PluginsManager`
- `...models.PluginConfiguration`
- `...order.interface.OrderTaxedPricesData`
- `...order.models.Order`
- `...order.models.OrderLine`
- `...order.notifications.get_image_payload`
- `...payment.TokenizedPaymentFlow`
- `...product.models.Product`
- `...product.models.ProductVariant`
- `..apps.PluginConfig`
- `..base_plugin.BasePlugin`
- `..base_plugin.ConfigurationTypeField`
- `..base_plugin.ExternalAccessTokens`
- `..error_codes.PluginErrorCode`
- `..manager.PluginsManager`
- `..manager.get_plugins_manager`
- `..models.PluginConfiguration`
- `..sample_plugins.ALL_PLUGINS`
- `..tests.sample_plugins.PluginSample`
- `..tests.utils.get_config_value`
- `.gateway.*  # noqa: F403`
- `.plugin_configuration.*  # noqa: F403`
- `.plugin_manager.*  # noqa: F403`
- `saleor.payment.ChargeStatus`
- `saleor.payment.TransactionKind`
- `saleor.payment.gateways.utils.get_supported_currencies`
- `saleor.plugins.base_plugin.BasePlugin`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8e6f35e3dd0a` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
