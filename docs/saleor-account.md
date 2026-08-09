## Purpose

`saleor/account` (`saleor/account`) groups 18 source file(s) exposing 119 top-level declaration(s).

## Public surface

**`saleor/account/__init__.py`**

- `CustomerEvents` (class) — [saleor/account/__init__.py:1]

**`saleor/account/apps.py`**

- `AccountAppConfig` (class) — [saleor/account/apps.py:5]
- `ready` (function) — [saleor/account/apps.py:8]

**`saleor/account/error_codes.py`**

- `AccountErrorCode` (class) — [saleor/account/error_codes.py:4]
- `CustomerBulkUpdateErrorCode` (class) — [saleor/account/error_codes.py:45]
- `PermissionGroupErrorCode` (class) — [saleor/account/error_codes.py:56]
- `SendConfirmationEmailErrorCode` (class) — [saleor/account/error_codes.py:68]

**`saleor/account/events.py`**

- `customer_account_created_event` (function) — [saleor/account/events.py:7]
- `customer_account_activated_event` (function) — [saleor/account/events.py:11]
- `customer_account_deactivated_event` (function) — [saleor/account/events.py:22]
- `customer_password_reset_link_sent_event` (function) — [saleor/account/events.py:33]
- `customer_password_reset_event` (function) — [saleor/account/events.py:39]
- `customer_password_changed_event` (function) — [saleor/account/events.py:43]
- `customer_email_change_request_event` (function) — [saleor/account/events.py:47]
- `customer_email_changed_event` (function) — [saleor/account/events.py:55]
- `customer_placed_order_event` (function) — [saleor/account/events.py:63]
- `customer_added_to_note_order_event` (function) — [saleor/account/events.py:69]
- `customer_deleted_event` (function) — [saleor/account/events.py:80]
- `assigned_email_to_a_customer_event` (function) — [saleor/account/events.py:92]
- `assigned_name_to_a_customer_event` (function) — [saleor/account/events.py:104]

**`saleor/account/forms.py`**

- `get_address_form` (function) — [saleor/account/forms.py:6]

**`saleor/account/i18n_rules_override.py`**

- `patched_load_validation_data` (function) — [saleor/account/i18n_rules_override.py:18]
- `i18n_rules_override` (function) — [saleor/account/i18n_rules_override.py:27]

**`saleor/account/i18n_valid_address_extension.py`**

- `AddressFieldsToSubstitute` (class) — [saleor/account/i18n_valid_address_extension.py:6]

**`saleor/account/i18n.py`**

- `PossiblePhoneNumberFormField` (class) — [saleor/account/i18n.py:46]
- `CountryAreaChoiceField` (class) — [saleor/account/i18n.py:54]
- `valid_value` (function) — [saleor/account/i18n.py:57]
- `AddressMetaForm` (class) — [saleor/account/i18n.py:61]
- `Meta` (class) — [saleor/account/i18n.py:62]
- `clean` (function) — [saleor/account/i18n.py:67]
- `AddressForm` (class) — [saleor/account/i18n.py:72]
- `Meta` (class) — [saleor/account/i18n.py:88]
- `clean` (function) — [saleor/account/i18n.py:134]
- `CountryAwareAddressForm` (class) — [saleor/account/i18n.py:148]
- `Meta` (class) — [saleor/account/i18n.py:163]
- `add_field_errors` (function) — [saleor/account/i18n.py:167]
- `validate_address` (function) — [saleor/account/i18n.py:196]
- `clean` (function) — [saleor/account/i18n.py:221]
- `substitute_invalid_values` (function) — [saleor/account/i18n.py:226]
- `log_errors` (function) — [saleor/account/i18n.py:237]
- `get_address_form_class` (function) — [saleor/account/i18n.py:251]
- `get_form_i18n_lines` (function) — [saleor/account/i18n.py:255]
- `update_base_fields` (function) — [saleor/account/i18n.py:278]
- `construct_address_form` (function) — [saleor/account/i18n.py:312]

**`saleor/account/lock_objects.py`**

- `user_qs_select_for_update` (function) — [saleor/account/lock_objects.py:4]

**`saleor/account/models.py`**

- `PossiblePhoneNumberField` (class) — [saleor/account/models.py:29]
- `AddressQueryset` (class) — [saleor/account/models.py:35]
- `annotate_default` (function) — [saleor/account/models.py:36]
- `Address` (class) — [saleor/account/models.py:58]
- `Meta` (class) — [saleor/account/models.py:74]
- `as_data` (function) — [saleor/account/models.py:110]
- `get_copy` (function) — [saleor/account/models.py:122]
- `UserManager` (class) — [saleor/account/models.py:127]
- `customers` (function) — [saleor/account/models.py:128]
- `staff` (function) — [saleor/account/models.py:135]
- `User` (class) — [saleor/account/models.py:139]
- `Meta` (class) — [saleor/account/models.py:182]
- `effective_permissions` (function) — [saleor/account/models.py:248]
- `effective_permissions` (function) — [saleor/account/models.py:285]
- `get_full_name` (function) — [saleor/account/models.py:290]
- `get_short_name` (function) — [saleor/account/models.py:300]
- `has_perm` (function) — [saleor/account/models.py:303]
- `has_perms` (function) — [saleor/account/models.py:312]
- `can_login` (function) — [saleor/account/models.py:322]
- `CustomerNote` (class) — [saleor/account/models.py:330]
- `Meta` (class) — [saleor/account/models.py:341]
- `CustomerEvent` (class) — [saleor/account/models.py:345]
- `Meta` (class) — [saleor/account/models.py:362]
- `StaffNotificationRecipient` (class) — [saleor/account/models.py:369]
- `Meta` (class) — [saleor/account/models.py:380]
- `get_email` (function) — [saleor/account/models.py:383]
- `GroupManager` (class) — [saleor/account/models.py:387]
- `get_by_natural_key` (function) — [saleor/account/models.py:392]
- `Group` (class) — [saleor/account/models.py:396]
- `Meta` (class) — [saleor/account/models.py:426]
- `natural_key` (function) — [saleor/account/models.py:433]

**`saleor/account/notifications.py`**

- `get_default_user_payload` (function) — [saleor/account/notifications.py:15]
- `get_user_custom_payload` (function) — [saleor/account/notifications.py:33]
- `send_password_reset_notification` (function) — [saleor/account/notifications.py:42]
- `send_account_confirmation` (function) — [saleor/account/notifications.py:71]
- `send_request_user_change_email_notification` (function) — [saleor/account/notifications.py:100]
- `send_user_change_email_notification` (function) — [saleor/account/notifications.py:128]
- `send_account_delete_confirmation_notification` (function) — [saleor/account/notifications.py:150]
- `send_set_password_notification` (function) — [saleor/account/notifications.py:180]

**`saleor/account/search.py`**

- `update_user_search_vector` (function) — [saleor/account/search.py:17]
- `generate_user_search_vector_value` (function) — [saleor/account/search.py:38]
- `generate_email_vector` (function) — [saleor/account/search.py:66]
- `generate_address_search_vector_value` (function) — [saleor/account/search.py:83]

**`saleor/account/signals.py`**

- `delete_avatar` (function) — [saleor/account/signals.py:4]

**`saleor/account/tasks.py`**

- `trigger_send_password_reset_notification` (function) — [saleor/account/tasks.py:32]
- `finish_creating_user` (function) — [saleor/account/tasks.py:86]

**`saleor/account/throttling.py`**

- `authenticate_with_throttling` (function) — [saleor/account/throttling.py:21]
- `get_cache_key_failed_ip` (function) — [saleor/account/throttling.py:78]
- `get_cache_key_failed_ip_with_user` (function) — [saleor/account/throttling.py:82]
- `get_cache_key_blocked_ip` (function) — [saleor/account/throttling.py:86]
- `clear_cache` (function) — [saleor/account/throttling.py:90]
- `get_delay_time` (function) — [saleor/account/throttling.py:95]
- `override_block` (function) — [saleor/account/throttling.py:131]
- `add_block` (function) — [saleor/account/throttling.py:136]
- `increment_attempt` (function) — [saleor/account/throttling.py:141]

**`saleor/account/utils.py`**

- `RequestorAwareContext` (class) — [saleor/account/utils.py:22]
- `META` (function) — [saleor/account/utils.py:28]
- `from_context_data` (function) — [saleor/account/utils.py:42]
- `create_context_data` (function) — [saleor/account/utils.py:50]
- `store_user_address` (function) — [saleor/account/utils.py:58]
- `is_user_address_limit_reached` (function) — [saleor/account/utils.py:86]
- `remove_the_oldest_user_address_if_address_limit_is_reached` (function) — [saleor/account/utils.py:91]
- `remove_the_oldest_user_address` (function) — [saleor/account/utils.py:97]
- `set_user_default_billing_address` (function) — [saleor/account/utils.py:109]
- `set_user_default_shipping_address` (function) — [saleor/account/utils.py:114]
- `change_user_default_address` (function) — [saleor/account/utils.py:119]
- `retrieve_user_by_email` (function) — [saleor/account/utils.py:132]
- `get_user_groups_permissions` (function) — [saleor/account/utils.py:150]
- `send_user_event` (function) — [saleor/account/utils.py:162]
- `update_user_orders_count` (function) — [saleor/account/utils.py:174]

**`saleor/account/validators.py`**

- `validate_possible_number` (function) — [saleor/account/validators.py:8]

**`saleor/account/widgets.py`**

- `DatalistTextWidget` (class) — [saleor/account/widgets.py:4]
- `get_context` (function) — [saleor/account/widgets.py:7]
- `format_value` (function) — [saleor/account/widgets.py:12]

## How it works

The module's files, as provided to this run:

- `saleor/account/forms.py` (36 lines)
- `saleor/account/__init__.py` (42 lines)
- `saleor/account/models.py` (434 lines)
- `saleor/account/throttling.py` (145 lines)
- `saleor/account/apps.py` (16 lines)
- `saleor/account/error_codes.py` (72 lines)
- `saleor/account/events.py` (113 lines)
- `saleor/account/i18n_rules_override.py` (28 lines)
- `saleor/account/i18n_valid_address_extension.py` (45 lines)
- `saleor/account/i18n.py` (343 lines)
- `saleor/account/lock_objects.py` (5 lines)
- `saleor/account/notifications.py` (204 lines)
- `saleor/account/search.py` (139 lines)
- `saleor/account/signals.py` (6 lines)
- `saleor/account/tasks.py` (122 lines)
- `saleor/account/utils.py` (188 lines)
- `saleor/account/validators.py` (19 lines)
- `saleor/account/widgets.py` (14 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql/product/types`, `saleor/core/db`, `saleor/core/utils`, `saleor/plugins/openid_connect`
- Imported by: `saleor/account/migrations`, `saleor/graphql/core/filters`, `saleor/account/tests`, `saleor/graphql/checkout/mutations`, `saleor/app/tests`, `saleor/auth`, `saleor/checkout/migrations`, `saleor/core`, `saleor/order`, `saleor/tests/e2e/account/account`

Internal dependencies named in the source:

- `..CustomerEvents`
- `..app.models.App`
- `..celeryconf.app`
- `..checkout.AddressType`
- `..core.db.connection.allow_writer`
- `..core.models.ModelWithExternalReference`
- `..core.models.ModelWithMetadata`
- `..core.notification.utils.get_site_context`
- `..core.notify.NotifyEventType`
- `..core.notify.NotifyHandler`
- `..core.postgres.FlatConcatSearchVector`
- `..core.postgres.NoValidationSearchVector`
- `..core.tasks.delete_from_storage_task`
- `..core.tracing.traced_atomic_transaction`
- `..core.utils.events.call_event`
- `..core.utils.get_client_ip`
- `..core.utils.json_serializer.CustomJsonEncoder`
- `..core.utils.url.prepare_url`
- `..events`
- `..graphql.account.enums.CountryCodeEnum`
- `..graphql.core.utils.to_global_id_or_none`
- `..graphql.plugins.dataloaders.get_plugin_manager_promise`
- `..graphql.site.dataloaders.get_site_promise`
- `..models`
- `..notifications`
- `..order.models.Order`
- `..permission.enums.AccountPermissions`
- `..permission.enums.BasePermissionEnum`
- `..permission.enums.get_permissions`
- `..permission.models.Permission`
- `..permission.models.PermissionsMixin`
- `..permission.models._user_has_perm`
- `..plugins.manager.PluginsManager`
- `..plugins.manager.get_plugins_manager`
- `..search`
- `..site.models.SiteSettings`
- `.error_codes.AccountErrorCode`
- `.i18n.AddressMetaForm`
- `.i18n.get_address_form_class`
- `.i18n_valid_address_extension.VALID_ADDRESS_EXTENSION_MAP`
- `.lock_objects.user_qs_select_for_update`
- `.models.Address`
- `.models.CustomerEvent`
- `.models.Group`
- `.models.User`
- `.notifications.send_password_reset_notification`
- `.signals.delete_avatar`
- `.utils.RequestorAwareContext`
- `.utils.retrieve_user_by_email`
- `.validators.validate_possible_number`
- `.widgets.DatalistTextWidget`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `bcc8ac96a53c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
