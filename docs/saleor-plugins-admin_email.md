## Purpose

`saleor/plugins/admin_email` (`saleor/plugins/admin_email`) groups 15 source file(s) exposing 60 top-level declaration(s).

## Public surface

**`saleor/plugins/admin_email/notify_events.py`**

- `send_set_staff_password_email` (function) — [saleor/plugins/admin_email/notify_events.py:18]
- `send_csv_export_success` (function) — [saleor/plugins/admin_email/notify_events.py:42]
- `send_staff_order_confirmation` (function) — [saleor/plugins/admin_email/notify_events.py:68]
- `send_csv_export_failed` (function) — [saleor/plugins/admin_email/notify_events.py:92]
- `send_staff_reset_password` (function) — [saleor/plugins/admin_email/notify_events.py:118]

**`saleor/plugins/admin_email/plugin.py`**

- `get_admin_event_map` (function) — [saleor/plugins/admin_email/plugin.py:36]
- `AdminEmailPlugin` (class) — [saleor/plugins/admin_email/plugin.py:46]
- `resolve_plugin_configuration` (function) — [saleor/plugins/admin_email/plugin.py:206]
- `map_templates_to_configuration` (function) — [saleor/plugins/admin_email/plugin.py:213]
- `notify` (function) — [saleor/plugins/admin_email/plugin.py:239]
- `validate_plugin_configuration` (function) — [saleor/plugins/admin_email/plugin.py:262]
- `save_plugin_configuration` (function) — [saleor/plugins/admin_email/plugin.py:277]

**`saleor/plugins/admin_email/tasks.py`**

- `send_set_staff_password_email_task` (function) — [saleor/plugins/admin_email/tasks.py:9]
- `send_email_with_link_to_download_file_task` (function) — [saleor/plugins/admin_email/tasks.py:23]
- `send_export_failed_email_task` (function) — [saleor/plugins/admin_email/tasks.py:42]
- `send_staff_order_confirmation_email_task` (function) — [saleor/plugins/admin_email/tasks.py:61]
- `send_staff_password_reset_email_task` (function) — [saleor/plugins/admin_email/tasks.py:75]

**`saleor/plugins/admin_email/tests/conftest.py`**

- `email_dict_config` (function) — [saleor/plugins/admin_email/tests/conftest.py:30]
- `admin_email_plugin` (function) — [saleor/plugins/admin_email/tests/conftest.py:42]
- `fun` (function) — [saleor/plugins/admin_email/tests/conftest.py:43]
- `admin_email_template` (function) — [saleor/plugins/admin_email/tests/conftest.py:134]
- `default_admin_email_plugin` (function) — [saleor/plugins/admin_email/tests/conftest.py:145]
- `fun` (function) — [saleor/plugins/admin_email/tests/conftest.py:146]

**`saleor/plugins/admin_email/tests/test_notify_events.py`**

- `test_send_account_password_reset_event` (function) — [saleor/plugins/admin_email/tests/test_notify_events.py:19]
- `test_send_account_password_reset_event_empty_template` (function) — [saleor/plugins/admin_email/tests/test_notify_events.py:45]
- `test_send_set_staff_password_email` (function) — [saleor/plugins/admin_email/tests/test_notify_events.py:70]
- `test_send_set_staff_password_email_empty_template` (function) — [saleor/plugins/admin_email/tests/test_notify_events.py:89]
- `test_send_csv_export_success` (function) — [saleor/plugins/admin_email/tests/test_notify_events.py:111]
- `test_send_csv_product_export_success_empty_template` (function) — [saleor/plugins/admin_email/tests/test_notify_events.py:130]
- `test_send_staff_order_confirmation` (function) — [saleor/plugins/admin_email/tests/test_notify_events.py:151]
- `test_send_staff_order_confirmation_empty_template` (function) — [saleor/plugins/admin_email/tests/test_notify_events.py:171]
- `test_send_csv_export_failed` (function) — [saleor/plugins/admin_email/tests/test_notify_events.py:192]
- `test_send_csv_export_failed_empty_template` (function) — [saleor/plugins/admin_email/tests/test_notify_events.py:209]

**`saleor/plugins/admin_email/tests/test_plugin.py`**

- `test_event_map` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:36]
- `test_notify` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:57]
- `test_notify_event_not_related` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:72]
- `test_notify_event_missing_handler` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:89]
- `test_notify_event_plugin_is_not_active` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:106]
- `test_save_plugin_configuration_tls_and_ssl_are_mutually_exclusive` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:119]
- `test_save_plugin_configuration` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:135]
- `test_save_plugin_configuration_incorrect_email_backend_configuration` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:151]
- `test_save_plugin_configuration_incorrect_template` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:169]
- `test_get_email_template` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:207]
- `test_save_plugin_configuration_creates_email_template_instance` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:228]
- `test_configuration_resolver_returns_email_template_value` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:270]
- `test_plugin_manager_doesnt_load_email_templates_from_db` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:296]
- `test_plugin_dont_change_default_help_text_config_value` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:316]
- `test_default_plugin_configuration` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:343]
- `test_override_default_config` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:363]
- `test_set_and_unset_custom_email_template` (function) — [saleor/plugins/admin_email/tests/test_plugin.py:412]

**`saleor/plugins/admin_email/tests/test_tasks.py`**

- `test_send_staff_password_reset_email_task_default_template` (function) — [saleor/plugins/admin_email/tests/test_tasks.py:19]
- `test_send_staff_password_reset_email_task_custom_template` (function) — [saleor/plugins/admin_email/tests/test_tasks.py:46]
- `test_send_set_staff_password_email_task_default_template` (function) — [saleor/plugins/admin_email/tests/test_tasks.py:85]
- `test_send_set_staff_password_email_task_custom_template` (function) — [saleor/plugins/admin_email/tests/test_tasks.py:112]
- `test_send_email_with_link_to_download_file_task_default_template` (function) — [saleor/plugins/admin_email/tests/test_tasks.py:151]
- `test_send_email_with_link_to_download_file_task_custom_template` (function) — [saleor/plugins/admin_email/tests/test_tasks.py:182]
- `test_send_export_failed_email_task_default_template` (function) — [saleor/plugins/admin_email/tests/test_tasks.py:226]
- `test_send_export_failed_email_task_custom_template` (function) — [saleor/plugins/admin_email/tests/test_tasks.py:255]
- `test_send_staff_order_confirmation_email_task_default_template` (function) — [saleor/plugins/admin_email/tests/test_tasks.py:296]
- `test_send_staff_order_confirmation_email_task_custom_template` (function) — [saleor/plugins/admin_email/tests/test_tasks.py:322]

## How it works

The module's files, as provided to this run:

- `saleor/plugins/admin_email/__init__.py` (1 lines)
- `saleor/plugins/admin_email/notify_events.py` (141 lines)
- `saleor/plugins/admin_email/plugin.py` (319 lines)
- `saleor/plugins/admin_email/constants.py` (44 lines)
- `saleor/plugins/admin_email/default_email_templates/export_failed.html` (262 lines)
- `saleor/plugins/admin_email/default_email_templates/export_success.html` (300 lines)
- `saleor/plugins/admin_email/default_email_templates/password_reset.html` (324 lines)
- `saleor/plugins/admin_email/default_email_templates/set_password.html` (208 lines)
- `saleor/plugins/admin_email/default_email_templates/staff_confirm_order.html` (454 lines)
- `saleor/plugins/admin_email/tasks.py` (85 lines)
- `saleor/plugins/admin_email/tests/__init__.py` (1 lines)
- `saleor/plugins/admin_email/tests/conftest.py` (169 lines)
- `saleor/plugins/admin_email/tests/test_notify_events.py` (220 lines)
- `saleor/plugins/admin_email/tests/test_plugin.py` (446 lines)
- `saleor/plugins/admin_email/tests/test_tasks.py` (356 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/plugins/openid_connect`, `saleor/graphql`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.notifications.get_default_user_payload`
- `....core.notify.NotifyEventType`
- `....core.notify.NotifyHandler`
- `....csv.ExportEvents`
- `....csv.models.ExportEvent`
- `....csv.notifications.get_default_export_payload`
- `....graphql.tests.utils.get_graphql_content`
- `....order.notifications.get_default_order_payload`
- `....plugins.models.EmailTemplate`
- `....plugins.models.PluginConfiguration`
- `...celeryconf.app`
- `...core.db.connection.allow_writer`
- `...core.notify.AdminNotifyEvent`
- `...core.notify.NotifyEventType`
- `...csv.events.export_failed_info_sent_event`
- `...csv.events.export_file_sent_event`
- `...email_common.DEFAULT_EMAIL_VALUE`
- `...email_common.EmailConfig`
- `...graphql.core.utils.from_global_id_or_none`
- `...graphql.plugins.dataloaders.EmailTemplatesByPluginConfigurationLoader`
- `...manager.get_plugins_manager`
- `...models.EmailTemplate`
- `...models.PluginConfiguration`
- `..base_plugin.BasePlugin`
- `..base_plugin.ConfigurationTypeField`
- `..base_plugin.PluginConfigurationType`
- `..constants`
- `..email_common.EmailConfig`
- `..email_common.get_email_subject`
- `..email_common.get_email_template_or_default`
- `..email_common.send_email`
- `..models.EmailTemplate`
- `..models.PluginConfiguration`
- `..plugin.AdminEmailPlugin`
- `..plugin.get_admin_event_map`
- `.plugin.AdminEmailPlugin`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `99142c829105` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
