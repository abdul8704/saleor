## Purpose

`saleor/plugins/user_email` (`saleor/plugins/user_email`) groups 25 source file(s) exposing 120 top-level declaration(s).

## Public surface

**`saleor/plugins/user_email/notify_events.py`**

- `send_account_password_reset_event` (function) — [saleor/plugins/user_email/notify_events.py:28]
- `send_account_confirmation` (function) — [saleor/plugins/user_email/notify_events.py:56]
- `send_account_change_email_request` (function) — [saleor/plugins/user_email/notify_events.py:80]
- `send_account_change_email_confirm` (function) — [saleor/plugins/user_email/notify_events.py:104]
- `send_account_delete` (function) — [saleor/plugins/user_email/notify_events.py:128]
- `send_gift_card` (function) — [saleor/plugins/user_email/notify_events.py:152]
- `send_account_set_customer_password` (function) — [saleor/plugins/user_email/notify_events.py:174]
- `send_invoice` (function) — [saleor/plugins/user_email/notify_events.py:198]
- `send_order_confirmation` (function) — [saleor/plugins/user_email/notify_events.py:220]
- `send_fulfillment_confirmation` (function) — [saleor/plugins/user_email/notify_events.py:244]
- `send_fulfillment_update` (function) — [saleor/plugins/user_email/notify_events.py:268]
- `send_payment_confirmation` (function) — [saleor/plugins/user_email/notify_events.py:292]
- `send_order_canceled` (function) — [saleor/plugins/user_email/notify_events.py:316]
- `send_order_refund` (function) — [saleor/plugins/user_email/notify_events.py:340]
- `send_order_confirmed` (function) — [saleor/plugins/user_email/notify_events.py:364]

**`saleor/plugins/user_email/plugin.py`**

- `get_user_event_map` (function) — [saleor/plugins/user_email/plugin.py:50]
- `UserEmailPlugin` (class) — [saleor/plugins/user_email/plugin.py:72]
- `resolve_plugin_configuration` (function) — [saleor/plugins/user_email/plugin.py:359]
- `map_templates_to_configuration` (function) — [saleor/plugins/user_email/plugin.py:366]
- `notify` (function) — [saleor/plugins/user_email/plugin.py:392]
- `validate_plugin_configuration` (function) — [saleor/plugins/user_email/plugin.py:415]
- `save_plugin_configuration` (function) — [saleor/plugins/user_email/plugin.py:431]

**`saleor/plugins/user_email/tasks.py`**

- `send_account_confirmation_email_task` (function) — [saleor/plugins/user_email/tasks.py:12]
- `send_password_reset_email_task` (function) — [saleor/plugins/user_email/tasks.py:27]
- `send_request_email_change_email_task` (function) — [saleor/plugins/user_email/tasks.py:45]
- `send_user_change_email_notification_task` (function) — [saleor/plugins/user_email/tasks.py:69]
- `send_account_delete_confirmation_email_task` (function) — [saleor/plugins/user_email/tasks.py:93]
- `send_set_user_password_email_task` (function) — [saleor/plugins/user_email/tasks.py:107]
- `send_gift_card_email_task` (function) — [saleor/plugins/user_email/tasks.py:121]
- `send_invoice_email_task` (function) — [saleor/plugins/user_email/tasks.py:144]
- `send_order_confirmation_email_task` (function) — [saleor/plugins/user_email/tasks.py:170]
- `send_fulfillment_confirmation_email_task` (function) — [saleor/plugins/user_email/tasks.py:191]
- `send_fulfillment_update_email_task` (function) — [saleor/plugins/user_email/tasks.py:212]
- `send_payment_confirmation_email_task` (function) — [saleor/plugins/user_email/tasks.py:226]
- `send_order_canceled_email_task` (function) — [saleor/plugins/user_email/tasks.py:246]
- `send_order_refund_email_task` (function) — [saleor/plugins/user_email/tasks.py:265]
- `send_order_confirmed_email_task` (function) — [saleor/plugins/user_email/tasks.py:284]

**`saleor/plugins/user_email/tests/conftest.py`**

- `user_email_dict_config` (function) — [saleor/plugins/user_email/tests/conftest.py:56]
- `user_email_plugin` (function) — [saleor/plugins/user_email/tests/conftest.py:68]
- `fun` (function) — [saleor/plugins/user_email/tests/conftest.py:69]
- `user_email_template` (function) — [saleor/plugins/user_email/tests/conftest.py:250]

**`saleor/plugins/user_email/tests/test_notify_events.py`**

- `test_send_account_password_reset_event` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:30]
- `test_send_account_password_reset_event_with_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:55]
- `test_send_account_confirmation` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:80]
- `test_send_account_confirmation_with_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:103]
- `test_send_account_change_email_request` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:128]
- `test_send_account_change_email_request_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:155]
- `test_send_account_change_email_confirm` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:183]
- `test_send_account_change_email_confirm_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:206]
- `test_send_account_delete` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:229]
- `test_send_account_delete_with_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:253]
- `test_send_account_set_customer_password` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:278]
- `test_send_account_set_customer_password_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:303]
- `test_send_invoice` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:326]
- `test_send_invoice_with_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:348]
- `test_send_order_confirmation` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:372]
- `test_send_order_confirmation_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:392]
- `test_send_fulfillment_confirmation` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:415]
- `test_send_fulfillment_confirmation_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:433]
- `test_send_fulfillment_update` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:450]
- `test_send_fulfillment_update_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:467]
- `test_send_payment_confirmation` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:484]
- `test_send_payment_confirmation_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:514]
- `test_send_order_canceled` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:544]
- `test_send_order_canceled_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:564]
- `test_send_order_refund` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:586]
- `test_send_order_refund_with_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:608]
- `test_send_order_confirmed` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:632]
- `test_send_order_confirmed_empty_template` (function) — [saleor/plugins/user_email/tests/test_notify_events.py:652]

**`saleor/plugins/user_email/tests/test_plugin.py`**

- `test_event_map` (function) — [saleor/plugins/user_email/tests/test_plugin.py:39]
- `test_notify` (function) — [saleor/plugins/user_email/tests/test_plugin.py:82]
- `test_notify_event_not_related` (function) — [saleor/plugins/user_email/tests/test_plugin.py:107]
- `test_notify_event_missing_handler` (function) — [saleor/plugins/user_email/tests/test_plugin.py:134]
- `test_notify_event_plugin_is_not_active` (function) — [saleor/plugins/user_email/tests/test_plugin.py:161]
- `test_save_plugin_configuration_tls_and_ssl_are_mutually_exclusive` (function) — [saleor/plugins/user_email/tests/test_plugin.py:184]
- `test_save_plugin_configuration` (function) — [saleor/plugins/user_email/tests/test_plugin.py:200]
- `test_save_plugin_configuration_incorrect_email_backend_configuration` (function) — [saleor/plugins/user_email/tests/test_plugin.py:216]
- `test_save_plugin_configuration_incorrect_template` (function) — [saleor/plugins/user_email/tests/test_plugin.py:235]
- `test_get_email_template` (function) — [saleor/plugins/user_email/tests/test_plugin.py:263]
- `test_save_plugin_configuration_creates_email_template_instance` (function) — [saleor/plugins/user_email/tests/test_plugin.py:275]
- `test_configuration_resolver_returns_email_template_value` (function) — [saleor/plugins/user_email/tests/test_plugin.py:320]
- `test_plugin_manager_doesnt_load_email_templates_from_db` (function) — [saleor/plugins/user_email/tests/test_plugin.py:344]
- `test_adding_missing_configuration_from_settings` (function) — [saleor/plugins/user_email/tests/test_plugin.py:371]
- `test_adding_missing_configuration_from_settings_with_defaults` (function) — [saleor/plugins/user_email/tests/test_plugin.py:404]

**`saleor/plugins/user_email/tests/test_tasks.py`**

- `test_send_account_confirmation_email_task_default_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:35]
- `test_send_account_confirmation_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:58]
- `test_send_password_reset_email_task_default_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:93]
- `test_send_password_reset_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:120]
- `test_send_request_email_change_email_task_default_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:159]
- `test_send_request_email_change_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:184]
- `test_send_user_change_email_notification_task_default_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:228]
- `test_send_user_change_email_notification_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:257]
- `test_send_account_delete_confirmation_email_task_default_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:295]
- `test_send_account_delete_confirmation_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:318]
- `test_send_set_user_password_email_task_default_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:357]
- `test_send_set_user_password_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:380]
- `test_send_invoice_email_task_default_template_by_user` (function) — [saleor/plugins/user_email/tests/test_tasks.py:419]
- `test_send_invoice_email_task_default_template_by_app` (function) — [saleor/plugins/user_email/tests/test_tasks.py:462]
- `test_send_invoice_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:505]
- `test_send_order_confirmation_email_task_default_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:561]
- `test_send_order_confirmation_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:581]
- `test_send_fulfillment_confirmation_email_task_default_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:617]
- `test_send_fulfillment_confirmation_email_task_custom_template_by_user` (function) — [saleor/plugins/user_email/tests/test_tasks.py:644]
- `test_send_fulfillment_confirmation_email_task_custom_template_by_app` (function) — [saleor/plugins/user_email/tests/test_tasks.py:690]
- `test_send_fulfillment_update_email_task_default_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:736]
- `test_send_fulfillment_update_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:754]
- `test_send_payment_confirmation_email_task_default_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:789]
- `test_send_payment_confirmation_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:823]
- `test_send_order_canceled_email_task_default_template_by_user` (function) — [saleor/plugins/user_email/tests/test_tasks.py:866]
- `test_send_order_canceled_email_task_default_template_by_app` (function) — [saleor/plugins/user_email/tests/test_tasks.py:888]
- `test_send_order_canceled_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:910]
- `test_send_order_refund_email_task_default_template_by_user` (function) — [saleor/plugins/user_email/tests/test_tasks.py:947]
- `test_send_order_refund_email_task_default_template_by_app` (function) — [saleor/plugins/user_email/tests/test_tasks.py:977]
- `test_send_order_refund_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:1007]
- `test_send_order_confirmed_email_task_default_template_by_user` (function) — [saleor/plugins/user_email/tests/test_tasks.py:1051]
- `test_send_order_confirmed_email_task_default_template_by_app` (function) — [saleor/plugins/user_email/tests/test_tasks.py:1081]
- `test_send_order_confirmed_email_task_custom_template` (function) — [saleor/plugins/user_email/tests/test_tasks.py:1111]
- `test_send_gift_card_email_task_by_user` (function) — [saleor/plugins/user_email/tests/test_tasks.py:1156]
- `test_send_gift_card_email_task_by_user_resending` (function) — [saleor/plugins/user_email/tests/test_tasks.py:1209]
- `test_send_gift_card_email_task_by_app` (function) — [saleor/plugins/user_email/tests/test_tasks.py:1262]

## How it works

The module's files, as provided to this run:

- `saleor/plugins/user_email/notify_events.py` (385 lines)
- `saleor/plugins/user_email/__init__.py` (1 lines)
- `saleor/plugins/user_email/plugin.py` (487 lines)
- `saleor/plugins/user_email/constants.py` (98 lines)
- `saleor/plugins/user_email/default_email_templates/account_delete.html` (205 lines)
- `saleor/plugins/user_email/default_email_templates/confirm_fulfillment.html` (267 lines)
- `saleor/plugins/user_email/default_email_templates/confirm_order.html` (381 lines)
- `saleor/plugins/user_email/default_email_templates/confirm_payment.html` (195 lines)
- `saleor/plugins/user_email/default_email_templates/confirm.html` (205 lines)
- `saleor/plugins/user_email/default_email_templates/confirmed_order.html` (381 lines)
- `saleor/plugins/user_email/default_email_templates/email_changed_notification.html` (195 lines)
- `saleor/plugins/user_email/default_email_templates/gift_card.html` (219 lines)
- `saleor/plugins/user_email/default_email_templates/order_cancel.html` (194 lines)
- `saleor/plugins/user_email/default_email_templates/order_refund.html` (194 lines)
- `saleor/plugins/user_email/default_email_templates/password_reset.html` (205 lines)
- `saleor/plugins/user_email/default_email_templates/request_email_change.html` (205 lines)
- `saleor/plugins/user_email/default_email_templates/send_invoice.html` (204 lines)
- `saleor/plugins/user_email/default_email_templates/set_customer_password.html` (205 lines)
- `saleor/plugins/user_email/default_email_templates/update_fulfillment.html` (262 lines)
- `saleor/plugins/user_email/tasks.py` (301 lines)
- `saleor/plugins/user_email/tests/__init__.py` (1 lines)
- `saleor/plugins/user_email/tests/conftest.py` (257 lines)
- `saleor/plugins/user_email/tests/test_notify_events.py` (668 lines)
- `saleor/plugins/user_email/tests/test_plugin.py` (426 lines)
- `saleor/plugins/user_email/tests/test_tasks.py` (1310 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/plugins/openid_connect`, `saleor/graphql`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.notifications.get_default_user_payload`
- `....core.notify.NotifyEventType`
- `....core.notify.NotifyHandler`
- `....giftcard.GiftCardEvents`
- `....giftcard.models.GiftCardEvent`
- `....graphql.core.utils.to_global_id_or_none`
- `....graphql.tests.utils.get_graphql_content`
- `....invoice.InvoiceEvents`
- `....invoice.models.Invoice`
- `....invoice.models.InvoiceEvent`
- `....order.OrderEvents`
- `....order.OrderEventsEmails`
- `....plugins.models.EmailTemplate`
- `....plugins.models.PluginConfiguration`
- `...account.events`
- `...celeryconf.app`
- `...core.db.connection.allow_writer`
- `...core.notify.NotifyEventType`
- `...core.notify.UserNotifyEvent`
- `...email_common.DEFAULT_EMAIL_VALUE`
- `...email_common.EmailConfig`
- `...email_common.get_email_template`
- `...giftcard.events`
- `...graphql.core.utils.from_global_id_or_none`
- `...graphql.plugins.dataloaders.EmailTemplatesByPluginConfigurationLoader`
- `...invoice.events`
- `...manager.get_plugins_manager`
- `...models.PluginConfiguration`
- `...order.events`
- `...plugins.models.EmailTemplate`
- `..base_plugin.BasePlugin`
- `..base_plugin.ConfigurationTypeField`
- `..base_plugin.PluginConfigurationType`
- `..constants`
- `..email_common.EmailConfig`
- `..email_common.get_email_subject`
- `..email_common.get_email_template_or_default`
- `..email_common.send_email`
- `..models.PluginConfiguration`
- `..plugin.UserEmailPlugin`
- `..plugin.get_user_event_map`
- `.constants.TEMPLATE_FIELDS`
- `.plugin.UserEmailPlugin`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `0bc4bb036a2e` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
