## Purpose

`saleor/graphql/account/bulk_mutations` (`saleor/graphql/account/bulk_mutations`) groups 5 source file(s) exposing 36 top-level declaration(s).

## Public surface

**`saleor/graphql/account/bulk_mutations/customer_bulk_delete.py`**

- `UserBulkDelete` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_delete.py:20]
- `Arguments` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_delete.py:21]
- `Meta` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_delete.py:31]
- `CustomerBulkDelete` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_delete.py:35]
- `Meta` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_delete.py:36]
- `perform_mutation` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_delete.py:53]
- `bulk_action` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_delete.py:59]

**`saleor/graphql/account/bulk_mutations/customer_bulk_update.py`**

- `CustomerBulkResult` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:45]
- `Meta` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:53]
- `CustomerBulkUpdateInput` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:57]
- `Meta` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:67]
- `CustomerBulkUpdate` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:71]
- `Arguments` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:84]
- `Meta` (class) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:98]
- `format_errors` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:115]
- `validate_customer` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:132]
- `clean_address` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:179]
- `clean_metadata` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:206]
- `clean_customers` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:226]
- `get_customers` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:338]
- `update_address` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:364]
- `update_customers` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:381]
- `save_customers` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:485]
- `post_save_actions` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:581]
- `get_results` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:702]
- `perform_mutation` (function) — [saleor/graphql/account/bulk_mutations/customer_bulk_update.py:717]

**`saleor/graphql/account/bulk_mutations/staff_bulk_delete.py`**

- `StaffBulkDelete` (class) — [saleor/graphql/account/bulk_mutations/staff_bulk_delete.py:22]
- `Meta` (class) — [saleor/graphql/account/bulk_mutations/staff_bulk_delete.py:23]
- `perform_mutation` (function) — [saleor/graphql/account/bulk_mutations/staff_bulk_delete.py:42]
- `clean_instances` (function) — [saleor/graphql/account/bulk_mutations/staff_bulk_delete.py:60]
- `bulk_action` (function) — [saleor/graphql/account/bulk_mutations/staff_bulk_delete.py:72]

**`saleor/graphql/account/bulk_mutations/user_bulk_set_active.py`**

- `UserBulkSetActive` (class) — [saleor/graphql/account/bulk_mutations/user_bulk_set_active.py:14]
- `Arguments` (class) — [saleor/graphql/account/bulk_mutations/user_bulk_set_active.py:15]
- `Meta` (class) — [saleor/graphql/account/bulk_mutations/user_bulk_set_active.py:25]
- `clean_instance` (function) — [saleor/graphql/account/bulk_mutations/user_bulk_set_active.py:35]
- `bulk_action` (function) — [saleor/graphql/account/bulk_mutations/user_bulk_set_active.py:56]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/bulk_mutations/customer_bulk_delete.py` (70 lines)
- `saleor/graphql/account/bulk_mutations/__init__.py` (11 lines)
- `saleor/graphql/account/bulk_mutations/customer_bulk_update.py` (750 lines)
- `saleor/graphql/account/bulk_mutations/staff_bulk_delete.py` (83 lines)
- `saleor/graphql/account/bulk_mutations/user_bulk_set_active.py` (59 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: `saleor/graphql/account/tests/bulk_mutations`

Internal dependencies named in the source:

- `....account.error_codes.AccountErrorCode`
- `....account.events.CustomerEvents`
- `....account.models`
- `....account.search.update_user_search_vector`
- `....checkout.AddressType`
- `....core.tracing.traced_atomic_transaction`
- `....core.utils.metadata_manager`
- `....giftcard.search.mark_gift_cards_search_index_as_dirty_by_users`
- `....giftcard.utils.assign_user_gift_cards`
- `....giftcard.utils.deactivate_assigned_gift_cards`
- `....order.utils.match_orders_with_new_user`
- `....permission.enums.AccountPermissions`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.utils.get_webhooks_for_event`
- `...core.ResolveInfo`
- `...core.doc_category.DOC_CATEGORY_USERS`
- `...core.enums.CustomerBulkUpdateErrorCode`
- `...core.enums.ErrorPolicyEnum`
- `...core.mutations.BaseBulkMutation`
- `...core.mutations.BaseMutation`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelBulkDeleteMutation`
- `...core.types.AccountError`
- `...core.types.NonNullList`
- `...core.types.StaffError`
- `...core.utils.WebhookEventInfo`
- `...core.utils.get_duplicated_values`
- `...core.validators.validate_one_of_args_is_in_mutation`
- `...meta.inputs.MetadataInput`
- `...payment.utils.deprecated_metadata_contains_empty_key`
- `...plugins.dataloaders.get_app_promise`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...site.dataloaders.get_site_promise`
- `..i18n.I18nMixin`
- `..mutations.base.CustomerDeleteMixin`
- `..mutations.base.StaffDeleteMixin`
- `..types.User`
- `.customer_bulk_delete.CustomerBulkDelete`
- `.customer_bulk_delete.UserBulkDelete`
- `.customer_bulk_update.CustomerBulkUpdate`
- `.staff_bulk_delete.StaffBulkDelete`
- `.user_bulk_set_active.UserBulkSetActive`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `1658ab0c170e` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
