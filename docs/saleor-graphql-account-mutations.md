## Purpose

`saleor/graphql/account/mutations` (`saleor/graphql/account/mutations`) groups 2 source file(s) exposing 39 top-level declaration(s).

## Public surface

**`saleor/graphql/account/mutations/base.py`**

- `check_can_edit_address` (function) — [saleor/graphql/account/mutations/base.py:40]
- `BaseAddressUpdate` (class) — [saleor/graphql/account/mutations/base.py:61]
- `Arguments` (class) — [saleor/graphql/account/mutations/base.py:68]
- `Meta` (class) — [saleor/graphql/account/mutations/base.py:74]
- `clean_input` (function) — [saleor/graphql/account/mutations/base.py:78]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/base.py:85]
- `BaseAddressDelete` (class) — [saleor/graphql/account/mutations/base.py:116]
- `Arguments` (class) — [saleor/graphql/account/mutations/base.py:123]
- `Meta` (class) — [saleor/graphql/account/mutations/base.py:126]
- `clean_instance` (function) — [saleor/graphql/account/mutations/base.py:130]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/base.py:137]
- `UserInput` (class) — [saleor/graphql/account/mutations/base.py:174]
- `Meta` (class) — [saleor/graphql/account/mutations/base.py:197]
- `UserAddressInput` (class) — [saleor/graphql/account/mutations/base.py:201]
- `Meta` (class) — [saleor/graphql/account/mutations/base.py:209]
- `CustomerInput` (class) — [saleor/graphql/account/mutations/base.py:213]
- `Meta` (class) — [saleor/graphql/account/mutations/base.py:224]
- `UserCreateInput` (class) — [saleor/graphql/account/mutations/base.py:228]
- `Meta` (class) — [saleor/graphql/account/mutations/base.py:251]
- `BaseCustomerCreate` (class) — [saleor/graphql/account/mutations/base.py:255]
- `Arguments` (class) — [saleor/graphql/account/mutations/base.py:258]
- `Meta` (class) — [saleor/graphql/account/mutations/base.py:263]
- `clean_input` (function) — [saleor/graphql/account/mutations/base.py:267]
- `post_save_action` (function) — [saleor/graphql/account/mutations/base.py:344]
- `save_default_addresses` (function) — [saleor/graphql/account/mutations/base.py:350]
- `UserDeleteMixin` (class) — [saleor/graphql/account/mutations/base.py:377]
- `Meta` (class) — [saleor/graphql/account/mutations/base.py:378]
- `clean_instance` (function) — [saleor/graphql/account/mutations/base.py:382]
- `CustomerDeleteMixin` (class) — [saleor/graphql/account/mutations/base.py:404]
- `Meta` (class) — [saleor/graphql/account/mutations/base.py:405]
- `clean_instance` (function) — [saleor/graphql/account/mutations/base.py:409]
- `post_process` (function) — [saleor/graphql/account/mutations/base.py:422]
- `StaffDeleteMixin` (class) — [saleor/graphql/account/mutations/base.py:431]
- `Meta` (class) — [saleor/graphql/account/mutations/base.py:432]
- `check_permissions` (function) — [saleor/graphql/account/mutations/base.py:436]
- `clean_instance` (function) — [saleor/graphql/account/mutations/base.py:450]
- `check_if_users_can_be_deleted` (function) — [saleor/graphql/account/mutations/base.py:464]
- `check_if_requestor_can_manage_users` (function) — [saleor/graphql/account/mutations/base.py:485]
- `check_if_removing_left_not_manageable_permissions` (function) — [saleor/graphql/account/mutations/base.py:502]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/mutations/__init__.py` (1 lines)
- `saleor/graphql/account/mutations/base.py` (522 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.error_codes.AccountErrorCode`
- `....account.events`
- `....account.models`
- `....account.search.update_user_search_vector`
- `....checkout.AddressType`
- `....core.exceptions.PermissionDenied`
- `....core.utils.metadata_manager`
- `....core.utils.url.validate_storefront_url`
- `....giftcard.search.mark_gift_cards_search_index_as_dirty`
- `....giftcard.utils.get_user_gift_cards`
- `....graphql.utils.get_user_or_app_from_context`
- `....permission.auth_filters.AuthorizationFilters`
- `....permission.enums.AccountPermissions`
- `...account.i18n.I18nMixin`
- `...account.types.Address`
- `...account.types.AddressInput`
- `...account.types.User`
- `...app.dataloaders.get_app_promise`
- `...core.ResolveInfo`
- `...core.SaleorContext`
- `...core.descriptions.DEPRECATED_IN_3X_INPUT`
- `...core.doc_category.DOC_CATEGORY_USERS`
- `...core.enums.LanguageCodeEnum`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.types.BaseInputObjectType`
- `...core.types.NonNullList`
- `...meta.inputs.MetadataInput`
- `...meta.inputs.MetadataInputDescription`
- `...plugins.dataloaders.get_plugin_manager_promise`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `3525b24690cb` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
