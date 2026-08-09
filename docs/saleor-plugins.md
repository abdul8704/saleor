## Purpose

`saleor/plugins` (`saleor/plugins`) groups 9 source file(s) exposing 239 top-level declaration(s).

## Public surface

**`saleor/plugins/__init__.py`**

- `discover_plugins_modules` (function) — [saleor/plugins/__init__.py:6]

**`saleor/plugins/apps.py`**

- `PluginConfig` (class) — [saleor/plugins/apps.py:12]
- `ready` (function) — [saleor/plugins/apps.py:16]
- `load_and_check_plugin` (function) — [saleor/plugins/apps.py:22]
- `check_plugin_fields` (function) — [saleor/plugins/apps.py:30]

**`saleor/plugins/base_plugin.py`**

- `ConfigurationTypeField` (class) — [saleor/plugins/base_plugin.py:73]
- `ExternalAccessTokens` (class) — [saleor/plugins/base_plugin.py:93]
- `BasePlugin` (class) — [saleor/plugins/base_plugin.py:100]
- `check_plugin_id` (function) — [saleor/plugins/base_plugin.py:119]
- `token_is_required_as_payment_input` (function) — [saleor/plugins/base_plugin.py:1705]
- `get_payment_gateways` (function) — [saleor/plugins/base_plugin.py:1708]
- `validate_plugin_configuration` (function) — [saleor/plugins/base_plugin.py:1792]
- `pre_save_plugin_configuration` (function) — [saleor/plugins/base_plugin.py:1802]
- `save_plugin_configuration` (function) — [saleor/plugins/base_plugin.py:1810]
- `get_default_active` (function) — [saleor/plugins/base_plugin.py:1877]
- `get_plugin_configuration` (function) — [saleor/plugins/base_plugin.py:1880]
- `resolve_plugin_configuration` (function) — [saleor/plugins/base_plugin.py:1891]
- `is_event_active` (function) — [saleor/plugins/base_plugin.py:1897]

**`saleor/plugins/email_common.py`**

- `EmailConfig` (class) — [saleor/plugins/email_common.py:47]
- `format_address` (function) — [saleor/plugins/email_common.py:127]
- `format_datetime` (function) — [saleor/plugins/email_common.py:142]
- `get_product_image_thumbnail` (function) — [saleor/plugins/email_common.py:150]
- `compare` (function) — [saleor/plugins/email_common.py:158]
- `price` (function) — [saleor/plugins/email_common.py:173]
- `get_plain_text_message_for_email` (function) — [saleor/plugins/email_common.py:194]
- `send_email` (function) — [saleor/plugins/email_common.py:210]
- `validate_email_config` (function) — [saleor/plugins/email_common.py:249]
- `validate_default_email_configuration` (function) — [saleor/plugins/email_common.py:266]
- `validate_format_of_provided_templates` (function) — [saleor/plugins/email_common.py:341]
- `get_email_template` (function) — [saleor/plugins/email_common.py:369]
- `get_email_template_or_default` (function) — [saleor/plugins/email_common.py:385]
- `get_email_subject` (function) — [saleor/plugins/email_common.py:405]
- `get_default_email_template` (function) — [saleor/plugins/email_common.py:419]

**`saleor/plugins/error_codes.py`**

- `PluginErrorCode` (class) — [saleor/plugins/error_codes.py:4]

**`saleor/plugins/manager.py`**

- `PluginsManager` (class) — [saleor/plugins/manager.py:89]
- `database` (function) — [saleor/plugins/manager.py:97]
- `check_payment_balance` (function) — [saleor/plugins/manager.py:257]
- `calculate_checkout_total` (function) — [saleor/plugins/manager.py:262]
- `calculate_checkout_subtotal` (function) — [saleor/plugins/manager.py:296]
- `calculate_checkout_shipping` (function) — [saleor/plugins/manager.py:320]
- `calculate_order_total` (function) — [saleor/plugins/manager.py:342]
- `calculate_order_shipping` (function) — [saleor/plugins/manager.py:369]
- `get_checkout_shipping_tax_rate` (function) — [saleor/plugins/manager.py:390]
- `get_order_shipping_tax_rate` (function) — [saleor/plugins/manager.py:409]
- `calculate_checkout_line_total` (function) — [saleor/plugins/manager.py:424]
- `calculate_order_line_total` (function) — [saleor/plugins/manager.py:455]
- `calculate_checkout_line_unit_price` (function) — [saleor/plugins/manager.py:498]
- `calculate_order_line_unit` (function) — [saleor/plugins/manager.py:530]
- `get_checkout_line_tax_rate` (function) — [saleor/plugins/manager.py:576]
- `get_order_line_tax_rate` (function) — [saleor/plugins/manager.py:597]
- `get_tax_rate_type_choices` (function) — [saleor/plugins/manager.py:620]
- `preprocess_order_creation` (function) — [saleor/plugins/manager.py:659]
- `customer_created` (function) — [saleor/plugins/manager.py:675]
- `customer_deleted` (function) — [saleor/plugins/manager.py:683]
- `customer_updated` (function) — [saleor/plugins/manager.py:695]
- `customer_metadata_updated` (function) — [saleor/plugins/manager.py:707]
- `collection_created` (function) — [saleor/plugins/manager.py:719]
- `collection_updated` (function) — [saleor/plugins/manager.py:727]
- `collection_deleted` (function) — [saleor/plugins/manager.py:735]
- `collection_metadata_updated` (function) — [saleor/plugins/manager.py:747]
- `product_created` (function) — [saleor/plugins/manager.py:755]
- `product_updated` (function) — [saleor/plugins/manager.py:767]
- `product_deleted` (function) — [saleor/plugins/manager.py:779]
- `product_type_created` (function) — [saleor/plugins/manager.py:792]
- `product_type_updated` (function) — [saleor/plugins/manager.py:800]
- `product_type_deleted` (function) — [saleor/plugins/manager.py:808]
- `product_media_created` (function) — [saleor/plugins/manager.py:820]
- `product_media_updated` (function) — [saleor/plugins/manager.py:828]
- `product_media_deleted` (function) — [saleor/plugins/manager.py:836]
- `product_metadata_updated` (function) — [saleor/plugins/manager.py:844]
- `product_variant_created` (function) — [saleor/plugins/manager.py:852]
- `product_variant_updated` (function) — [saleor/plugins/manager.py:864]
- `product_variant_discounted_price_updated` (function) — [saleor/plugins/manager.py:877]
- `product_variant_deleted` (function) — [saleor/plugins/manager.py:891]
- _…and 159 more in this file_

**`saleor/plugins/models.py`**

- `PluginConfiguration` (class) — [saleor/plugins/models.py:9]
- `Meta` (class) — [saleor/plugins/models.py:19]
- `EmailTemplate` (class) — [saleor/plugins/models.py:27]

**`saleor/plugins/views.py`**

- `handle_plugin_webhook` (function) — [saleor/plugins/views.py:9]
- `handle_global_plugin_webhook` (function) — [saleor/plugins/views.py:15]
- `handle_plugin_per_channel_webhook` (function) — [saleor/plugins/views.py:23]

## How it works

The module's files, as provided to this run:

- `saleor/plugins/__init__.py` (16 lines)
- `saleor/plugins/base_plugin.py` (1898 lines)
- `saleor/plugins/manager.py` (2854 lines)
- `saleor/plugins/apps.py` (35 lines)
- `saleor/plugins/const.py` (1 lines)
- `saleor/plugins/email_common.py` (426 lines)
- `saleor/plugins/error_codes.py` (10 lines)
- `saleor/plugins/models.py` (35 lines)
- `saleor/plugins/views.py` (27 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`, `saleor/plugins/openid_connect`, `saleor/graphql`, `saleor/tax/webhooks`
- Imported by: `saleor/plugins/avatax`, `saleor/plugins/tests`, `saleor/shipping/migrations`

Internal dependencies named in the source:

- `..account.models.Address`
- `..account.models.Group`
- `..account.models.User`
- `..app.models.App`
- `..attribute.models.Attribute`
- `..attribute.models.AttributeValue`
- `..channel.models.Channel`
- `..checkout.base_calculations`
- `..checkout.fetch.CheckoutInfo`
- `..checkout.fetch.CheckoutLineInfo`
- `..checkout.models.Checkout`
- `..core.db.connection.allow_writer`
- `..core.middleware.Requestor`
- `..core.models.EventDelivery`
- `..core.notify.NotifyEventType`
- `..core.payments.PaymentInterface`
- `..core.prices.quantize_price`
- `..core.taxes.TaxData`
- `..core.taxes.TaxDataError`
- `..core.taxes.TaxType`
- `..core.taxes.zero_money`
- `..core.taxes.zero_taxed_money`
- `..core.telemetry.tracer`
- `..core.utils.json_serializer.CustomJsonEncoder`
- `..core.utils.translations.Translation`
- `..csv.models.ExportFile`
- `..discount.models.Promotion`
- `..discount.models.PromotionRule`
- `..discount.models.Voucher`
- `..discount.models.VoucherCode`
- `..giftcard.models.GiftCard`
- `..graphql.core.SaleorContext`
- `..invoice.models.Invoice`
- `..menu.models.Menu`
- `..menu.models.MenuItem`
- `..order.base_calculations`
- `..order.interface.OrderTaxedPricesData`
- `..order.models.Fulfillment`
- `..order.models.Order`
- `..order.models.OrderLine`
- `..page.models.Page`
- `..page.models.PageType`
- `..payment.interface.PaymentGatewayData`
- `..payment.interface.TransactionSessionData`
- `..payment.models.TransactionItem`
- `..permission.enums.PluginsPermissions`
- `..plugins.base_plugin.BasePlugin`
- `..plugins.models.PluginConfiguration`
- `..shipping.models.ShippingMethod`
- `..shipping.models.ShippingZone`
- `..site.models.SiteSettings`
- `..tax.models.TaxClass`
- `..tax.utils.calculate_tax_rate`
- `..thumbnail.models.Thumbnail`
- `..thumbnail.utils.get_thumbnail_size`
- `..warehouse.models.Warehouse`
- `.base_plugin.BasePlugin`
- `.base_plugin.ConfigurationTypeField`
- `.base_plugin.ExternalAccessTokens`
- `.error_codes.PluginErrorCode`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `2a3dafa99bbf` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
