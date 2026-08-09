## Purpose

`saleor/plugins/sendgrid` (`saleor/plugins/sendgrid`) groups 7 source file(s) exposing 56 top-level declaration(s).

## Public surface

**`saleor/plugins/sendgrid/__init__.py`**

- `SendgridConfiguration` (class) — [saleor/plugins/sendgrid/__init__.py:5]

**`saleor/plugins/sendgrid/plugin.py`**

- `DeprecatedSendgridEmailPlugin` (class) — [saleor/plugins/sendgrid/plugin.py:100]
- `notify` (function) — [saleor/plugins/sendgrid/plugin.py:230]
- `validate_plugin_configuration` (function) — [saleor/plugins/sendgrid/plugin.py:265]

**`saleor/plugins/sendgrid/tasks.py`**

- `send_email` (function) — [saleor/plugins/sendgrid/tasks.py:22]
- `send_account_confirmation_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:41]
- `send_password_reset_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:56]
- `send_request_email_change_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:76]
- `send_user_change_email_notification_task` (function) — [saleor/plugins/sendgrid/tasks.py:100]
- `send_account_delete_confirmation_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:124]
- `send_set_user_password_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:139]
- `send_invoice_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:154]
- `send_order_confirmation_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:183]
- `send_fulfillment_confirmation_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:205]
- `send_fulfillment_update_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:227]
- `send_payment_confirmation_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:242]
- `send_order_canceled_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:263]
- `send_order_refund_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:285]
- `send_gift_card_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:307]
- `send_order_confirmed_email_task` (function) — [saleor/plugins/sendgrid/tasks.py:333]
- `send_email_with_dynamic_template_id` (function) — [saleor/plugins/sendgrid/tasks.py:355]

**`saleor/plugins/sendgrid/tests/conftest.py`**

- `sendgrid_email_plugin` (function) — [saleor/plugins/sendgrid/tests/conftest.py:8]
- `fun` (function) — [saleor/plugins/sendgrid/tests/conftest.py:9]

**`saleor/plugins/sendgrid/tests/test_plugin.py`**

- `test_get_event_map` (function) — [saleor/plugins/sendgrid/tests/test_plugin.py:15]
- `test_notify_via_external_notification_trigger_with_extra_payload` (function) — [saleor/plugins/sendgrid/tests/test_plugin.py:21]
- `test_send_notification_to_customers_with_product_variant_payload` (function) — [saleor/plugins/sendgrid/tests/test_plugin.py:43]
- `test_notify_when_plugin_disabled` (function) — [saleor/plugins/sendgrid/tests/test_plugin.py:68]
- `test_notify_not_valid_event_type` (function) — [saleor/plugins/sendgrid/tests/test_plugin.py:87]
- `test_notify_missing_handler` (function) — [saleor/plugins/sendgrid/tests/test_plugin.py:106]
- `test_notify_missing_template_id` (function) — [saleor/plugins/sendgrid/tests/test_plugin.py:127]
- `test_notify` (function) — [saleor/plugins/sendgrid/tests/test_plugin.py:152]
- `test_save_plugin_configuration_missing_api_key` (function) — [saleor/plugins/sendgrid/tests/test_plugin.py:177]

**`saleor/plugins/sendgrid/tests/test_tasks.py`**

- `sample_payload` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:41]
- `test_send_email` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:55]
- `test_send_account_confirmation_email_task` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:85]
- `test_send_password_reset_email_task` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:114]
- `test_send_request_email_change_email_task` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:149]
- `test_send_user_change_email_notification_task` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:190]
- `test_send_account_delete_confirmation_email_task` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:229]
- `test_send_set_user_password_email_task` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:262]
- `test_send_invoice_email_task_by_user` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:295]
- `test_send_invoice_email_task_by_app` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:342]
- `test_send_order_confirmation_email_task` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:389]
- `test_send_fulfillment_confirmation_email_task_by_user` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:426]
- `test_send_fulfillment_confirmation_email_task_by_app` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:461]
- `test_send_fulfillment_update_email_task` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:496]
- `test_send_payment_confirmation_email_task` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:520]
- `test_send_order_canceled_email_task_by_user` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:565]
- `test_send_order_canceled_email_task_by_app` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:606]
- `test_send_order_refund_email_task_by_user` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:647]
- `test_send_order_refund_email_task_by_app` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:690]
- `test_send_gift_card_email_task_by_user` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:733]
- `test_send_gift_card_email_task_by_user_resending` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:778]
- `test_send_gift_card_email_task_by_app` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:823]
- `test_send_order_confirmed_email_task_by_user` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:868]
- `test_send_order_confirmed_email_task_by_app` (function) — [saleor/plugins/sendgrid/tests/test_tasks.py:911]

## How it works

The module's files, as provided to this run:

- `saleor/plugins/sendgrid/__init__.py` (23 lines)
- `saleor/plugins/sendgrid/plugin.py` (284 lines)
- `saleor/plugins/sendgrid/tasks.py` (363 lines)
- `saleor/plugins/sendgrid/tests/__init__.py` (1 lines)
- `saleor/plugins/sendgrid/tests/conftest.py` (110 lines)
- `saleor/plugins/sendgrid/tests/test_plugin.py` (185 lines)
- `saleor/plugins/sendgrid/tests/test_tasks.py` (950 lines)

## Interactions

- Imports from: `saleor/plugins/openid_connect`, `saleor/core`, `saleor/graphql/product/types`, `saleor/webhook/response_schemas`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.CustomerEvents`
- `....account.models.CustomerEvent`
- `....account.notifications.get_default_user_payload`
- `....account.notifications.get_user_custom_payload`
- `....core.notify.AdminNotifyEvent`
- `....core.notify.UserNotifyEvent`
- `....giftcard.GiftCardEvents`
- `....giftcard.models.GiftCardEvent`
- `....graphql.core.utils.to_global_id_or_none`
- `....invoice.InvoiceEvents`
- `....invoice.models.Invoice`
- `....invoice.models.InvoiceEvent`
- `....order.OrderEvents`
- `....order.OrderEventsEmails`
- `....order.models.OrderEvent`
- `....plugins.sendgrid.plugin.DeprecatedSendgridEmailPlugin`
- `....webhook.payloads.generate_product_variant_payload`
- `...account.events`
- `...celeryconf.app`
- `...core.db.connection.allow_writer`
- `...core.notify.NotifyEventType`
- `...core.notify.UserNotifyEvent`
- `...giftcard.events`
- `...graphql.core.utils.from_global_id_or_none`
- `...invoice.events`
- `...manager.get_plugins_manager`
- `...models.PluginConfiguration`
- `...order.events`
- `...plugins.sendgrid.tasks.send_email_with_dynamic_template_id`
- `..SendgridConfiguration`
- `..base_plugin.BasePlugin`
- `..base_plugin.ConfigurationTypeField`
- `..error_codes.PluginErrorCode`
- `..models.PluginConfiguration`
- `..plugin.EVENT_MAP`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7ce53e31952a` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
