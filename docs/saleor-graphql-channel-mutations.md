## Purpose

`saleor/graphql/channel/mutations` (`saleor/graphql/channel/mutations`) groups 9 source file(s) exposing 71 top-level declaration(s).

## Public surface

**`saleor/graphql/channel/mutations/base_channel_listing.py`**

- `BaseChannelListingMutation` (class) — [saleor/graphql/channel/mutations/base_channel_listing.py:17]
- `Meta` (class) — [saleor/graphql/channel/mutations/base_channel_listing.py:20]
- `validate_duplicated_channel_ids` (function) — [saleor/graphql/channel/mutations/base_channel_listing.py:24]
- `validate_duplicated_channel_values` (function) — [saleor/graphql/channel/mutations/base_channel_listing.py:45]
- `clean_channels` (function) — [saleor/graphql/channel/mutations/base_channel_listing.py:59]
- `clean_publication_date` (function) — [saleor/graphql/channel/mutations/base_channel_listing.py:103]

**`saleor/graphql/channel/mutations/channel_activate.py`**

- `ChannelActivate` (class) — [saleor/graphql/channel/mutations/channel_activate.py:16]
- `Arguments` (class) — [saleor/graphql/channel/mutations/channel_activate.py:19]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_activate.py:22]
- `clean_channel_availability` (function) — [saleor/graphql/channel/mutations/channel_activate.py:36]
- `perform_mutation` (function) — [saleor/graphql/channel/mutations/channel_activate.py:48]

**`saleor/graphql/channel/mutations/channel_create.py`**

- `StockSettingsInput` (class) — [saleor/graphql/channel/mutations/channel_create.py:45]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_create.py:54]
- `CheckoutAutoCompleteInput` (class) — [saleor/graphql/channel/mutations/channel_create.py:58]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_create.py:93]
- `CheckoutSettingsInput` (class) — [saleor/graphql/channel/mutations/channel_create.py:97]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_create.py:138]
- `OrderSettingsInput` (class) — [saleor/graphql/channel/mutations/channel_create.py:142]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_create.py:224]
- `PaymentSettingsInput` (class) — [saleor/graphql/channel/mutations/channel_create.py:228]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_create.py:259]
- `ChannelInput` (class) — [saleor/graphql/channel/mutations/channel_create.py:263]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_create.py:312]
- `ChannelCreateInput` (class) — [saleor/graphql/channel/mutations/channel_create.py:316]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_create.py:331]
- `ChannelCreate` (class) — [saleor/graphql/channel/mutations/channel_create.py:335]
- `Arguments` (class) — [saleor/graphql/channel/mutations/channel_create.py:336]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_create.py:341]
- `get_type_for_model` (function) — [saleor/graphql/channel/mutations/channel_create.py:358]
- `clean_input` (function) — [saleor/graphql/channel/mutations/channel_create.py:362]
- `post_save_action` (function) — [saleor/graphql/channel/mutations/channel_create.py:395]

**`saleor/graphql/channel/mutations/channel_deactivate.py`**

- `ChannelDeactivate` (class) — [saleor/graphql/channel/mutations/channel_deactivate.py:16]
- `Arguments` (class) — [saleor/graphql/channel/mutations/channel_deactivate.py:19]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_deactivate.py:22]
- `clean_channel_availability` (function) — [saleor/graphql/channel/mutations/channel_deactivate.py:36]
- `perform_mutation` (function) — [saleor/graphql/channel/mutations/channel_deactivate.py:48]

**`saleor/graphql/channel/mutations/channel_delete.py`**

- `ChannelDeleteInput` (class) — [saleor/graphql/channel/mutations/channel_delete.py:21]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_delete.py:30]
- `ChannelDelete` (class) — [saleor/graphql/channel/mutations/channel_delete.py:34]
- `Arguments` (class) — [saleor/graphql/channel/mutations/channel_delete.py:35]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_delete.py:39]
- `validate_input` (function) — [saleor/graphql/channel/mutations/channel_delete.py:58]
- `migrate_orders_to_target_channel` (function) — [saleor/graphql/channel/mutations/channel_delete.py:83]
- `delete_checkouts` (function) — [saleor/graphql/channel/mutations/channel_delete.py:89]
- `perform_delete_with_order_migration` (function) — [saleor/graphql/channel/mutations/channel_delete.py:95]
- `perform_delete_channel_without_order` (function) — [saleor/graphql/channel/mutations/channel_delete.py:104]
- `post_save_action` (function) — [saleor/graphql/channel/mutations/channel_delete.py:119]
- `perform_mutation` (function) — [saleor/graphql/channel/mutations/channel_delete.py:124]

**`saleor/graphql/channel/mutations/channel_reorder_warehouses.py`**

- `ChannelReorderWarehouses` (class) — [saleor/graphql/channel/mutations/channel_reorder_warehouses.py:19]
- `Arguments` (class) — [saleor/graphql/channel/mutations/channel_reorder_warehouses.py:24]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_reorder_warehouses.py:37]
- `perform_mutation` (function) — [saleor/graphql/channel/mutations/channel_reorder_warehouses.py:44]
- `get_operations` (function) — [saleor/graphql/channel/mutations/channel_reorder_warehouses.py:60]

**`saleor/graphql/channel/mutations/channel_update.py`**

- `ChannelUpdateInput` (class) — [saleor/graphql/channel/mutations/channel_update.py:46]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_update.py:67]
- `ChannelUpdate` (class) — [saleor/graphql/channel/mutations/channel_update.py:71]
- `Arguments` (class) — [saleor/graphql/channel/mutations/channel_update.py:72]
- `Meta` (class) — [saleor/graphql/channel/mutations/channel_update.py:78]
- `perform_mutation` (function) — [saleor/graphql/channel/mutations/channel_update.py:115]
- `clean_input` (function) — [saleor/graphql/channel/mutations/channel_update.py:151]
- `check_permissions` (function) — [saleor/graphql/channel/mutations/channel_update.py:186]
- `emit_events` (function) — [saleor/graphql/channel/mutations/channel_update.py:312]

**`saleor/graphql/channel/mutations/utils.py`**

- `clean_expire_orders_after` (function) — [saleor/graphql/channel/mutations/utils.py:41]
- `clean_delete_expired_orders_after` (function) — [saleor/graphql/channel/mutations/utils.py:47]
- `clean_checkout_ttl_before_releasing_funds` (function) — [saleor/graphql/channel/mutations/utils.py:66]
- `clean_input_order_settings` (function) — [saleor/graphql/channel/mutations/utils.py:81]
- `clean_input_checkout_settings` (function) — [saleor/graphql/channel/mutations/utils.py:131]
- `clean_automatic_completion` (function) — [saleor/graphql/channel/mutations/utils.py:148]
- `clean_automatic_completion_delay` (function) — [saleor/graphql/channel/mutations/utils.py:191]
- `clean_automatic_completion_cut_off_date` (function) — [saleor/graphql/channel/mutations/utils.py:231]
- `clean_input_payment_settings` (function) — [saleor/graphql/channel/mutations/utils.py:270]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/channel/mutations/channel_update.py` (321 lines)
- `saleor/graphql/channel/mutations/__init__.py` (17 lines)
- `saleor/graphql/channel/mutations/base_channel_listing.py` (134 lines)
- `saleor/graphql/channel/mutations/channel_activate.py` (55 lines)
- `saleor/graphql/channel/mutations/channel_create.py` (398 lines)
- `saleor/graphql/channel/mutations/channel_deactivate.py` (55 lines)
- `saleor/graphql/channel/mutations/channel_delete.py` (151 lines)
- `saleor/graphql/channel/mutations/channel_reorder_warehouses.py` (96 lines)
- `saleor/graphql/channel/mutations/utils.py` (303 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core/utils`
- Imported by: `saleor/graphql/channel/tests/mutations`

Internal dependencies named in the source:

- `....channel.error_codes.ChannelErrorCode`
- `....channel.models`
- `....channel.models.Channel`
- `....checkout.models.Checkout`
- `....core.tracing.traced_atomic_transaction`
- `....core.utils.date_time.convert_to_utc_date_time`
- `....core.utils.update_mutation_manager.InstanceTracker`
- `....order.models.Order`
- `....permission.enums.ChannelPermissions`
- `....tax.models.TaxConfiguration`
- `....webhook.event_types.WebhookEventAsyncType`
- `...account.enums.CountryCodeEnum`
- `...core.ResolveInfo`
- `...core.doc_category.DOC_CATEGORY_CHANNELS`
- `...core.enums.ChannelErrorCode`
- `...core.inputs.ReorderInput`
- `...core.mutations.BaseMutation`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.scalars.DateTime`
- `...core.scalars.Day`
- `...core.scalars.Hour`
- `...core.scalars.Minute`
- `...core.types.BaseInputObjectType`
- `...core.types.ChannelError`
- `...core.types.NonNullList`
- `...core.types.common`
- `...core.utils.WebhookEventInfo`
- `...core.utils.get_duplicated_values`
- `...core.utils.get_duplicates_items`
- `...core.utils.reordering.perform_reordering`
- `...meta.inputs.MetadataInput`
- `...meta.inputs.MetadataInputDescription`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...site.dataloaders.get_site_promise`
- `...utils.validators.check_for_duplicates`
- `...warehouse.types.Warehouse`
- `..types.Channel`
- `..utils.delete_invalid_warehouse_to_shipping_zone_relations`
- `.base_channel_listing.BaseChannelListingMutation`
- `.channel_activate.ChannelActivate`
- `.channel_create.ChannelCreate`
- `.channel_create.ChannelInput`
- `.channel_deactivate.ChannelDeactivate`
- `.channel_delete.ChannelDelete`
- `.channel_reorder_warehouses.ChannelReorderWarehouses`
- `.channel_update.ChannelUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `f08ff2b643ea` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
