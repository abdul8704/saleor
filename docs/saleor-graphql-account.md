## Purpose

`saleor/graphql/account` (`saleor/graphql/account`) groups 11 source file(s) exposing 188 top-level declaration(s).

## Public surface

**`saleor/graphql/account/dataloaders.py`**

- `AddressByIdLoader` (class) — [saleor/graphql/account/dataloaders.py:13]
- `batch_load` (function) — [saleor/graphql/account/dataloaders.py:16]
- `UserByUserIdLoader` (class) — [saleor/graphql/account/dataloaders.py:21]
- `batch_load` (function) — [saleor/graphql/account/dataloaders.py:24]
- `CustomerEventsByUserLoader` (class) — [saleor/graphql/account/dataloaders.py:29]
- `batch_load` (function) — [saleor/graphql/account/dataloaders.py:32]
- `ThumbnailByUserIdSizeAndFormatLoader` (class) — [saleor/graphql/account/dataloaders.py:42]
- `batch_load` (function) — [saleor/graphql/account/dataloaders.py:47]
- `UserByEmailLoader` (class) — [saleor/graphql/account/dataloaders.py:63]
- `batch_load` (function) — [saleor/graphql/account/dataloaders.py:66]
- `PermissionByCodenameLoader` (class) — [saleor/graphql/account/dataloaders.py:75]
- `batch_load` (function) — [saleor/graphql/account/dataloaders.py:78]
- `BaseAccessibleChannels` (class) — [saleor/graphql/account/dataloaders.py:90]
- `get_group_to_channels_map` (function) — [saleor/graphql/account/dataloaders.py:91]
- `get_group_channels` (function) — [saleor/graphql/account/dataloaders.py:115]
- `AccessibleChannelsByGroupIdLoader` (class) — [saleor/graphql/account/dataloaders.py:132]
- `batch_load` (function) — [saleor/graphql/account/dataloaders.py:135]
- `AccessibleChannelsByUserIdLoader` (class) — [saleor/graphql/account/dataloaders.py:140]
- `batch_load` (function) — [saleor/graphql/account/dataloaders.py:143]
- `RestrictedChannelAccessByUserIdLoader` (class) — [saleor/graphql/account/dataloaders.py:163]
- `batch_load` (function) — [saleor/graphql/account/dataloaders.py:166]

**`saleor/graphql/account/enums.py`**

- `StaffMemberStatus` (class) — [saleor/graphql/account/enums.py:40]
- `Meta` (class) — [saleor/graphql/account/enums.py:44]
- `description` (function) — [saleor/graphql/account/enums.py:49]

**`saleor/graphql/account/filters.py`**

- `filter_date_joined` (function) — [saleor/graphql/account/filters.py:42]
- `filter_updated_at` (function) — [saleor/graphql/account/filters.py:46]
- `filter_number_of_orders` (function) — [saleor/graphql/account/filters.py:50]
- `filter_placed_orders` (function) — [saleor/graphql/account/filters.py:55]
- `filter_staff_status` (function) — [saleor/graphql/account/filters.py:59]
- `filter_user_search` (function) — [saleor/graphql/account/filters.py:67]
- `filter_search` (function) — [saleor/graphql/account/filters.py:71]
- `filter_address` (function) — [saleor/graphql/account/filters.py:77]
- `CustomerFilter` (class) — [saleor/graphql/account/filters.py:88]
- `Meta` (class) — [saleor/graphql/account/filters.py:104]
- `CountryCodeEnumFilterInput` (class) — [saleor/graphql/account/filters.py:114]
- `Meta` (class) — [saleor/graphql/account/filters.py:127]
- `AddressFilterInput` (class) — [saleor/graphql/account/filters.py:132]
- `Meta` (class) — [saleor/graphql/account/filters.py:140]
- `CustomerWhereFilterInput` (class) — [saleor/graphql/account/filters.py:145]
- `filter_email` (function) — [saleor/graphql/account/filters.py:193]
- `filter_first_name` (function) — [saleor/graphql/account/filters.py:197]
- `filter_last_name` (function) — [saleor/graphql/account/filters.py:201]
- `filter_is_active` (function) — [saleor/graphql/account/filters.py:205]
- `filter_date_joined` (function) — [saleor/graphql/account/filters.py:211]
- `filter_updated_at` (function) — [saleor/graphql/account/filters.py:215]
- `filter_placed_orders_at` (function) — [saleor/graphql/account/filters.py:219]
- `filter_addresses` (function) — [saleor/graphql/account/filters.py:228]
- `filter_number_of_orders` (function) — [saleor/graphql/account/filters.py:239]
- `CustomerWhereInput` (class) — [saleor/graphql/account/filters.py:245]
- `Meta` (class) — [saleor/graphql/account/filters.py:246]
- `PermissionGroupFilter` (class) — [saleor/graphql/account/filters.py:251]
- `filter_ids` (function) — [saleor/graphql/account/filters.py:256]
- `StaffUserFilter` (class) — [saleor/graphql/account/filters.py:262]
- `Meta` (class) — [saleor/graphql/account/filters.py:269]
- `filter_ids` (function) — [saleor/graphql/account/filters.py:274]

**`saleor/graphql/account/i18n.py`**

- `I18nMixin` (class) — [saleor/graphql/account/i18n.py:58]
- `construct_instance` (function) — [saleor/graphql/account/i18n.py:65]
- `clean_instance` (function) — [saleor/graphql/account/i18n.py:69]
- `attach_params_to_address_form_errors` (function) — [saleor/graphql/account/i18n.py:125]
- `validate_address` (function) — [saleor/graphql/account/i18n.py:155]
- `can_skip_address_validation` (function) — [saleor/graphql/account/i18n.py:201]

**`saleor/graphql/account/mixins.py`**

- `AddressMetadataMixin` (class) — [saleor/graphql/account/mixins.py:12]
- `construct_instance` (function) — [saleor/graphql/account/mixins.py:14]
- `AppImpersonateMixin` (class) — [saleor/graphql/account/mixins.py:28]
- `get_user_instance` (function) — [saleor/graphql/account/mixins.py:30]

**`saleor/graphql/account/resolvers.py`**

- `resolve_customers` (function) — [saleor/graphql/account/resolvers.py:39]
- `resolve_permission_group` (function) — [saleor/graphql/account/resolvers.py:45]
- `resolve_permission_groups` (function) — [saleor/graphql/account/resolvers.py:53]
- `resolve_staff_users` (function) — [saleor/graphql/account/resolvers.py:57]
- `resolve_user` (function) — [saleor/graphql/account/resolvers.py:62]
- `resolve_users` (function) — [saleor/graphql/account/resolvers.py:107]
- `resolve_address_validation_rules` (function) — [saleor/graphql/account/resolvers.py:139]
- `resolve_payment_sources` (function) — [saleor/graphql/account/resolvers.py:185]
- `prepare_graphql_payment_sources_type` (function) — [saleor/graphql/account/resolvers.py:207]
- `resolve_address` (function) — [saleor/graphql/account/resolvers.py:228]
- `resolve_addresses` (function) — [saleor/graphql/account/resolvers.py:244]
- `resolve_permissions` (function) — [saleor/graphql/account/resolvers.py:259]

**`saleor/graphql/account/schema.py`**

- `CustomerFilterInput` (class) — [saleor/graphql/account/schema.py:99]
- `Meta` (class) — [saleor/graphql/account/schema.py:100]
- `PermissionGroupFilterInput` (class) — [saleor/graphql/account/schema.py:105]
- `Meta` (class) — [saleor/graphql/account/schema.py:106]
- `StaffUserInput` (class) — [saleor/graphql/account/schema.py:111]
- `Meta` (class) — [saleor/graphql/account/schema.py:112]
- `AccountQueries` (class) — [saleor/graphql/account/schema.py:117]
- `resolve_address_validation_rules` (function) — [saleor/graphql/account/schema.py:214]
- `resolve_customers` (function) — [saleor/graphql/account/schema.py:232]
- `resolve_permission_groups` (function) — [saleor/graphql/account/schema.py:246]
- `resolve_permission_group` (function) — [saleor/graphql/account/schema.py:254]
- `resolve_me` (function) — [saleor/graphql/account/schema.py:259]
- `resolve_staff_users` (function) — [saleor/graphql/account/schema.py:264]
- `resolve_user` (function) — [saleor/graphql/account/schema.py:272]
- `resolve_address` (function) — [saleor/graphql/account/schema.py:282]
- `AccountMutations` (class) — [saleor/graphql/account/schema.py:286]

**`saleor/graphql/account/sorters.py`**

- `UserSortField` (class) — [saleor/graphql/account/sorters.py:7]
- `Meta` (class) — [saleor/graphql/account/sorters.py:16]
- `description` (function) — [saleor/graphql/account/sorters.py:20]
- `qs_with_order_count` (function) — [saleor/graphql/account/sorters.py:34]
- `UserSortingInput` (class) — [saleor/graphql/account/sorters.py:38]
- `Meta` (class) — [saleor/graphql/account/sorters.py:39]
- `PermissionGroupSortField` (class) — [saleor/graphql/account/sorters.py:45]
- `Meta` (class) — [saleor/graphql/account/sorters.py:48]
- `description` (function) — [saleor/graphql/account/sorters.py:53]
- `PermissionGroupSortingInput` (class) — [saleor/graphql/account/sorters.py:61]
- `Meta` (class) — [saleor/graphql/account/sorters.py:62]

**`saleor/graphql/account/types.py`**

- `AddressInput` (class) — [saleor/graphql/account/types.py:80]
- `Address` (class) — [saleor/graphql/account/types.py:121]
- `Meta` (class) — [saleor/graphql/account/types.py:159]
- `resolve_country` (function) — [saleor/graphql/account/types.py:165]
- `resolve_is_default_shipping_address` (function) — [saleor/graphql/account/types.py:169]
- `resolve_is_default_billing_address` (function) — [saleor/graphql/account/types.py:188]
- `CustomerEvent` (class) — [saleor/graphql/account/types.py:225]
- `Meta` (class) — [saleor/graphql/account/types.py:237]
- `resolve_user` (function) — [saleor/graphql/account/types.py:244]
- `resolve_app` (function) — [saleor/graphql/account/types.py:262]
- `resolve_message` (function) — [saleor/graphql/account/types.py:270]
- `resolve_count` (function) — [saleor/graphql/account/types.py:274]
- `resolve_order` (function) — [saleor/graphql/account/types.py:278]
- `UserPermission` (class) — [saleor/graphql/account/types.py:291]
- `Meta` (class) — [saleor/graphql/account/types.py:303]
- `resolve_source_permission_groups` (function) — [saleor/graphql/account/types.py:309]
- `is_newly_created_user` (function) — [saleor/graphql/account/types.py:317]
- `User` (class) — [saleor/graphql/account/types.py:332]
- `Meta` (class) — [saleor/graphql/account/types.py:489]
- `resolve_addresses` (function) — [saleor/graphql/account/types.py:496]
- `resolve_checkout` (function) — [saleor/graphql/account/types.py:502]
- `resolve_checkout_tokens` (function) — [saleor/graphql/account/types.py:515]
- `return_checkout_tokens` (function) — [saleor/graphql/account/types.py:519]
- `resolve_checkout_ids` (function) — [saleor/graphql/account/types.py:541]
- `return_checkout_ids` (function) — [saleor/graphql/account/types.py:545]
- `resolve_checkouts` (function) — [saleor/graphql/account/types.py:566]
- `resolve_gift_cards` (function) — [saleor/graphql/account/types.py:588]
- `resolve_user_permissions` (function) — [saleor/graphql/account/types.py:604]
- `resolve_permission_groups` (function) — [saleor/graphql/account/types.py:612]
- `resolve_editable_groups` (function) — [saleor/graphql/account/types.py:618]
- `resolve_accessible_channels` (function) — [saleor/graphql/account/types.py:625]
- `resolve_restricted_access_to_channels` (function) — [saleor/graphql/account/types.py:633]
- `resolve_note` (function) — [saleor/graphql/account/types.py:641]
- `resolve_events` (function) — [saleor/graphql/account/types.py:645]
- `resolve_orders` (function) — [saleor/graphql/account/types.py:651]
- `resolve_avatar` (function) — [saleor/graphql/account/types.py:743]
- `resolve_stored_payment_sources` (function) — [saleor/graphql/account/types.py:771]
- `resolve_language_code` (function) — [saleor/graphql/account/types.py:786]
- `resolve_stored_payment_methods` (function) — [saleor/graphql/account/types.py:815]
- `get_stored_payment_methods` (function) — [saleor/graphql/account/types.py:826]
- _…and 20 more in this file_

**`saleor/graphql/account/utils.py`**

- `get_required_fields_camel_case` (function) — [saleor/graphql/account/utils.py:25]
- `get_upper_fields_camel_case` (function) — [saleor/graphql/account/utils.py:30]
- `validation_field_to_camel_case` (function) — [saleor/graphql/account/utils.py:35]
- `get_allowed_fields_camel_case` (function) — [saleor/graphql/account/utils.py:43]
- `get_user_permissions` (function) — [saleor/graphql/account/utils.py:51]
- `get_out_of_scope_permissions` (function) — [saleor/graphql/account/utils.py:56]
- `get_out_of_scope_users` (function) — [saleor/graphql/account/utils.py:67]
- `can_user_manage_group` (function) — [saleor/graphql/account/utils.py:77]
- `can_user_manage_group_permissions` (function) — [saleor/graphql/account/utils.py:84]
- `can_user_manage_group_channels` (function) — [saleor/graphql/account/utils.py:90]
- `can_manage_app` (function) — [saleor/graphql/account/utils.py:101]
- `get_group_permission_codes` (function) — [saleor/graphql/account/utils.py:109]
- `get_groups_which_user_can_manage` (function) — [saleor/graphql/account/utils.py:116]
- `get_not_manageable_permissions_when_deactivate_or_remove_users` (function) — [saleor/graphql/account/utils.py:143]
- `get_not_manageable_permissions_after_removing_perms_from_group` (function) — [saleor/graphql/account/utils.py:187]
- `get_not_manageable_permissions_after_removing_users_from_group` (function) — [saleor/graphql/account/utils.py:202]
- `get_not_manageable_permissions_after_group_deleting` (function) — [saleor/graphql/account/utils.py:234]
- `get_not_manageable_permissions` (function) — [saleor/graphql/account/utils.py:245]
- `get_group_to_permissions_and_users_mapping` (function) — [saleor/graphql/account/utils.py:274]
- `get_users_and_look_for_permissions_in_groups_with_manage_staff` (function) — [saleor/graphql/account/utils.py:312]
- `look_for_permission_in_users_with_manage_staff` (function) — [saleor/graphql/account/utils.py:340]
- `is_owner_or_has_one_of_perms` (function) — [saleor/graphql/account/utils.py:364]
- `check_is_owner_or_has_one_of_perms` (function) — [saleor/graphql/account/utils.py:379]
- `get_user_accessible_channels` (function) — [saleor/graphql/account/utils.py:397]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/__init__.py` (1 lines)
- `saleor/graphql/account/dataloaders.py` (185 lines)
- `saleor/graphql/account/enums.py` (54 lines)
- `saleor/graphql/account/filters.py` (277 lines)
- `saleor/graphql/account/i18n.py` (222 lines)
- `saleor/graphql/account/mixins.py` (56 lines)
- `saleor/graphql/account/resolvers.py` (263 lines)
- `saleor/graphql/account/schema.py` (343 lines)
- `saleor/graphql/account/sorters.py` (65 lines)
- `saleor/graphql/account/types.py` (1110 lines)
- `saleor/graphql/account/utils.py` (402 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...account.CustomerEvents`
- `...account.error_codes.AccountErrorCode`
- `...account.forms.get_address_form`
- `...account.models`
- `...account.models.Address`
- `...account.models.CustomerEvent`
- `...account.models.Group`
- `...account.models.User`
- `...account.validators.validate_possible_number`
- `...app.models.App`
- `...channel.models.Channel`
- `...checkout.AddressType`
- `...checkout.utils.get_user_checkout`
- `...core.exceptions.PermissionDenied`
- `...core.search.prefix_search`
- `...core.utils.metadata_manager`
- `...graphql.core.context.get_database_connection_name`
- `...graphql.core.enums.to_enum`
- `...graphql.meta.inputs.MetadataInput`
- `...graphql.meta.inputs.MetadataInputDescription`
- `...order.OrderStatus`
- `...order.models.Order`
- `...payment.gateway`
- `...payment.interface.ListStoredPaymentMethodsRequestData`
- `...payment.utils.fetch_customer_id`
- `...permission.auth_filters.AuthorizationFilters`
- `...permission.enums.AccountPermissions`
- `...permission.enums.AppPermission`
- `...permission.enums.OrderPermissions`
- `...permission.models.Permission`
- `...permission.utils.all_permissions_required`
- `...permission.utils.has_one_of_permissions`
- `...permission.utils.message_one_of_permissions_required`
- `...plugins.manager.PluginsManager`
- `...thumbnail.models.Thumbnail`
- `...thumbnail.utils.get_thumbnail_format`
- `..account.utils.check_is_owner_or_has_one_of_perms`
- `..app.dataloaders.AppByIdLoader`
- `..app.dataloaders.app_promise_callback`
- `..app.dataloaders.get_app_promise`
- `..app.types.App`
- `..channel.dataloaders.by_self.ChannelBySlugLoader`
- `..channel.types.Channel`
- `..checkout.dataloaders.CheckoutByUserAndChannelLoader`
- `..checkout.dataloaders.CheckoutByUserLoader`
- `..checkout.types.Checkout`
- `..checkout.types.CheckoutCountableConnection`
- `..core.ResolveInfo`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.context.SyncWebhookControlContext`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.descriptions.ADDED_IN_322`
- `..core.descriptions.DEPRECATED_IN_3X_INPUT`
- `..core.doc_category.DOC_CATEGORY_USERS`
- `..core.enums.LanguageCodeEnum`
- `..core.federation.federated_entity`
- `..core.federation.resolve_federation_references`
- `..core.fields.BaseField`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `34c18b8d0320` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
