## Purpose

`saleor/plugins/webhook` (`saleor/plugins/webhook`) groups 3 source file(s) exposing 173 top-level declaration(s).

## Public surface

**`saleor/plugins/webhook/conftest.py`**

- `webhook_plugin` (function) — [saleor/plugins/webhook/conftest.py:7]
- `factory` (function) — [saleor/plugins/webhook/conftest.py:8]

**`saleor/plugins/webhook/plugin.py`**

- `WebhookPlugin` (class) — [saleor/plugins/webhook/plugin.py:158]
- `check_plugin_id` (function) — [saleor/plugins/webhook/plugin.py:165]
- `trigger_webhooks_async` (function) — [saleor/plugins/webhook/plugin.py:248]
- `account_confirmed` (function) — [saleor/plugins/webhook/plugin.py:251]
- `account_confirmation_requested` (function) — [saleor/plugins/webhook/plugin.py:260]
- `account_change_email_requested` (function) — [saleor/plugins/webhook/plugin.py:279]
- `account_email_changed` (function) — [saleor/plugins/webhook/plugin.py:300]
- `account_set_password_requested` (function) — [saleor/plugins/webhook/plugin.py:313]
- `account_delete_requested` (function) — [saleor/plugins/webhook/plugin.py:332]
- `account_deleted` (function) — [saleor/plugins/webhook/plugin.py:351]
- `address_created` (function) — [saleor/plugins/webhook/plugin.py:382]
- `address_updated` (function) — [saleor/plugins/webhook/plugin.py:388]
- `address_deleted` (function) — [saleor/plugins/webhook/plugin.py:394]
- `app_installed` (function) — [saleor/plugins/webhook/plugin.py:414]
- `app_updated` (function) — [saleor/plugins/webhook/plugin.py:420]
- `app_deleted` (function) — [saleor/plugins/webhook/plugin.py:426]
- `app_status_changed` (function) — [saleor/plugins/webhook/plugin.py:432]
- `attribute_created` (function) — [saleor/plugins/webhook/plugin.py:456]
- `attribute_updated` (function) — [saleor/plugins/webhook/plugin.py:466]
- `attribute_deleted` (function) — [saleor/plugins/webhook/plugin.py:476]
- `attribute_value_created` (function) — [saleor/plugins/webhook/plugin.py:509]
- `attribute_value_updated` (function) — [saleor/plugins/webhook/plugin.py:521]
- `attribute_value_deleted` (function) — [saleor/plugins/webhook/plugin.py:531]
- `category_created` (function) — [saleor/plugins/webhook/plugin.py:559]
- `category_updated` (function) — [saleor/plugins/webhook/plugin.py:565]
- `category_deleted` (function) — [saleor/plugins/webhook/plugin.py:571]
- `channel_created` (function) — [saleor/plugins/webhook/plugin.py:598]
- `channel_updated` (function) — [saleor/plugins/webhook/plugin.py:604]
- `channel_deleted` (function) — [saleor/plugins/webhook/plugin.py:614]
- `channel_status_changed` (function) — [saleor/plugins/webhook/plugin.py:620]
- `channel_metadata_updated` (function) — [saleor/plugins/webhook/plugin.py:628]
- `gift_card_created` (function) — [saleor/plugins/webhook/plugin.py:657]
- `gift_card_updated` (function) — [saleor/plugins/webhook/plugin.py:667]
- `gift_card_deleted` (function) — [saleor/plugins/webhook/plugin.py:675]
- `gift_card_sent` (function) — [saleor/plugins/webhook/plugin.py:685]
- `gift_card_metadata_updated` (function) — [saleor/plugins/webhook/plugin.py:719]
- `gift_card_status_changed` (function) — [saleor/plugins/webhook/plugin.py:729]
- `gift_card_export_completed` (function) — [saleor/plugins/webhook/plugin.py:757]
- `order_created` (function) — [saleor/plugins/webhook/plugin.py:784]
- `menu_created` (function) — [saleor/plugins/webhook/plugin.py:820]
- _…and 131 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/plugins/webhook/__init__.py` (1 lines)
- `saleor/plugins/webhook/conftest.py` (14 lines)
- `saleor/plugins/webhook/plugin.py` (3510 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...account.models.Address`
- `...account.models.Group`
- `...account.models.User`
- `...app.models.App`
- `...attribute.models.Attribute`
- `...attribute.models.AttributeValue`
- `...channel.models.Channel`
- `...checkout.fetch.CheckoutInfo`
- `...checkout.fetch.CheckoutLineInfo`
- `...checkout.models.Checkout`
- `...core.EventDeliveryStatus`
- `...core.models.EventDelivery`
- `...core.notify.NotifyEventType`
- `...core.taxes.TaxType`
- `...core.telemetry.get_task_context`
- `...core.utils.build_absolute_uri`
- `...core.utils.get_domain`
- `...core.utils.json_serializer.CustomJsonEncoder`
- `...core.utils.lazyobjects.unwrap_lazy`
- `...core.utils.translations.Translation`
- `...csv.models.ExportFile`
- `...csv.notifications.get_default_export_payload`
- `...discount.models.Promotion`
- `...discount.models.PromotionRule`
- `...discount.models.Voucher`
- `...discount.models.VoucherCode`
- `...giftcard.models.GiftCard`
- `...graphql.core.context.SaleorContext`
- `...graphql.core.dataloaders.DataLoader`
- `...invoice.models.Invoice`
- `...menu.models.Menu`
- `...menu.models.MenuItem`
- `...order.models.Fulfillment`
- `...order.models.Order`
- `...page.models.Page`
- `...page.models.PageType`
- `...payment.PaymentError`
- `...payment.TransactionKind`
- `...payment.models.Payment`
- `...payment.models.TransactionItem`
- `...settings.WEBHOOK_SYNC_TIMEOUT`
- `...shipping.models.ShippingMethod`
- `...shipping.models.ShippingZone`
- `...site.models.SiteSettings`
- `...tax.models.TaxClass`
- `...thumbnail.models.Thumbnail`
- `...warehouse.models.Warehouse`
- `...webhook.const.WEBHOOK_CACHE_DEFAULT_TTL`
- `...webhook.event_types.WebhookEventAsyncType`
- `...webhook.event_types.WebhookEventSyncType`
- `...webhook.models.Webhook`
- `..base_plugin.BasePlugin`
- `..manager.get_plugins_manager`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b9e5840e4c50` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
