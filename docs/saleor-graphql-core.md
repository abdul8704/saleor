## Purpose

`saleor/graphql/core` (`saleor/graphql/core`) groups 14 source file(s) exposing 173 top-level declaration(s).

## Public surface

**`saleor/graphql/core/__init__.py`**

- `ResolveInfo` (class) — [saleor/graphql/core/__init__.py:9]

**`saleor/graphql/core/connection.py`**

- `to_global_cursor` (function) — [saleor/graphql/core/connection.py:38]
- `from_global_cursor` (function) — [saleor/graphql/core/connection.py:45]
- `get_field_value` (function) — [saleor/graphql/core/connection.py:53]
- `connection_from_queryset_slice` (function) — [saleor/graphql/core/connection.py:251]
- `get_total_count` (function) — [saleor/graphql/core/connection.py:301]
- `create_connection_slice` (function) — [saleor/graphql/core/connection.py:316]
- `slice_connection_iterable` (function) — [saleor/graphql/core/connection.py:444]
- `filter_connection_queryset` (function) — [saleor/graphql/core/connection.py:488]
- `update_args_with_channel` (function) — [saleor/graphql/core/connection.py:513]
- `filter_qs` (function) — [saleor/graphql/core/connection.py:519]
- `where_filter_qs` (function) — [saleor/graphql/core/connection.py:554]
- `contains_filter_operator` (function) — [saleor/graphql/core/connection.py:633]
- `create_connection_slice_for_sync_webhook_control_context` (function) — [saleor/graphql/core/connection.py:676]
- `NonNullConnection` (class) — [saleor/graphql/core/connection.py:702]
- `Meta` (class) — [saleor/graphql/core/connection.py:703]
- `EdgeBase` (class) — [saleor/graphql/core/connection.py:711]
- `CountableConnection` (class) — [saleor/graphql/core/connection.py:735]
- `Meta` (class) — [saleor/graphql/core/connection.py:736]
- `resolve_total_count` (function) — [saleor/graphql/core/connection.py:742]

**`saleor/graphql/core/context.py`**

- `SaleorContext` (class) — [saleor/graphql/core/context.py:16]
- `disallow_replica_in_context` (function) — [saleor/graphql/core/context.py:32]
- `get_database_connection_name` (function) — [saleor/graphql/core/context.py:46]
- `setup_context_user` (function) — [saleor/graphql/core/context.py:62]
- `BaseContext` (class) — [saleor/graphql/core/context.py:81]
- `SyncWebhookControlContext` (class) — [saleor/graphql/core/context.py:86]
- `ChannelContext` (class) — [saleor/graphql/core/context.py:95]
- `ChannelQsContext` (class) — [saleor/graphql/core/context.py:103]

**`saleor/graphql/core/dataloaders.py`**

- `DataLoader` (class) — [saleor/graphql/core/dataloaders.py:20]
- `batch_load_fn` (function) — [saleor/graphql/core/dataloaders.py:51]
- `did_fulfill` (function) — [saleor/graphql/core/dataloaders.py:71]
- `did_reject` (function) — [saleor/graphql/core/dataloaders.py:78]
- `batch_load` (function) — [saleor/graphql/core/dataloaders.py:84]
- `BaseThumbnailBySizeAndFormatLoader` (class) — [saleor/graphql/core/dataloaders.py:88]
- `batch_load` (function) — [saleor/graphql/core/dataloaders.py:93]

**`saleor/graphql/core/enums.py`**

- `OrderDirection` (class) — [saleor/graphql/core/enums.py:57]
- `description` (function) — [saleor/graphql/core/enums.py:62]
- `ReportingPeriod` (class) — [saleor/graphql/core/enums.py:72]
- `to_enum` (function) — [saleor/graphql/core/enums.py:77]
- `permission_enum_deprecation_reason` (function) — [saleor/graphql/core/enums.py:121]
- `ErrorPolicy` (class) — [saleor/graphql/core/enums.py:154]
- `error_policy_enum_description` (function) — [saleor/graphql/core/enums.py:166]
- `collection_error_deprecation_reason` (function) — [saleor/graphql/core/enums.py:416]

**`saleor/graphql/core/fields.py`**

- `BaseField` (class) — [saleor/graphql/core/fields.py:14]
- `get_resolver` (function) — [saleor/graphql/core/fields.py:35]
- `PermissionsField` (class) — [saleor/graphql/core/fields.py:43]
- `get_resolver` (function) — [saleor/graphql/core/fields.py:60]
- `ConnectionField` (class) — [saleor/graphql/core/fields.py:68]
- `type` (function) — [saleor/graphql/core/fields.py:113]
- `FilterConnectionField` (class) — [saleor/graphql/core/fields.py:133]
- `get_resolver` (function) — [saleor/graphql/core/fields.py:149]
- `new_resolver` (function) — [saleor/graphql/core/fields.py:153]
- `JSONString` (class) — [saleor/graphql/core/fields.py:163]
- `parse_literal` (function) — [saleor/graphql/core/fields.py:165]
- `parse_value` (function) — [saleor/graphql/core/fields.py:172]

**`saleor/graphql/core/inputs.py`**

- `ReorderInput` (class) — [saleor/graphql/core/inputs.py:4]

**`saleor/graphql/core/mutations.py`**

- `get_model_name` (function) — [saleor/graphql/core/mutations.py:67]
- `get_error_fields` (function) — [saleor/graphql/core/mutations.py:73]
- `validation_error_to_error_type` (function) — [saleor/graphql/core/mutations.py:87]
- `attach_error_params` (function) — [saleor/graphql/core/mutations.py:121]
- `ModelMutationOptions` (class) — [saleor/graphql/core/mutations.py:131]
- `BaseMutation` (class) — [saleor/graphql/core/mutations.py:143]
- `Meta` (class) — [saleor/graphql/core/mutations.py:144]
- `get_global_id_or_error` (function) — [saleor/graphql/core/mutations.py:263]
- `get_node_or_error` (function) — [saleor/graphql/core/mutations.py:279]
- `get_node_or_error` (function) — [saleor/graphql/core/mutations.py:292]
- `get_node_or_error` (function) — [saleor/graphql/core/mutations.py:305]
- `get_node_or_error` (function) — [saleor/graphql/core/mutations.py:318]
- `get_node_or_error` (function) — [saleor/graphql/core/mutations.py:331]
- `get_node_or_error` (function) — [saleor/graphql/core/mutations.py:343]
- `get_global_ids_or_error` (function) — [saleor/graphql/core/mutations.py:386]
- `get_nodes_or_error` (function) — [saleor/graphql/core/mutations.py:404]
- `get_nodes_or_error` (function) — [saleor/graphql/core/mutations.py:410]
- `get_nodes_or_error` (function) — [saleor/graphql/core/mutations.py:415]
- `remap_error_fields` (function) — [saleor/graphql/core/mutations.py:425]
- `clean_instance` (function) — [saleor/graphql/core/mutations.py:439]
- `construct_instance` (function) — [saleor/graphql/core/mutations.py:464]
- `check_permissions` (function) — [saleor/graphql/core/mutations.py:499]
- `mutate` (function) — [saleor/graphql/core/mutations.py:519]
- `perform_mutation` (function) — [saleor/graphql/core/mutations.py:535]
- `handle_errors` (function) — [saleor/graphql/core/mutations.py:539]
- `handle_typed_errors` (function) — [saleor/graphql/core/mutations.py:544]
- `call_event` (function) — [saleor/graphql/core/mutations.py:551]
- `validate_and_update_metadata` (function) — [saleor/graphql/core/mutations.py:555]
- `check_metadata_permissions` (function) — [saleor/graphql/core/mutations.py:571]
- `check_channel_permissions` (function) — [saleor/graphql/core/mutations.py:585]
- `create_metadata_from_graphql_input` (function) — [saleor/graphql/core/mutations.py:601]
- `is_list_of_ids` (function) — [saleor/graphql/core/mutations.py:626]
- `is_id_field` (function) — [saleor/graphql/core/mutations.py:635]
- `is_upload_field` (function) — [saleor/graphql/core/mutations.py:643]
- `DeprecatedModelMutation` (class) — [saleor/graphql/core/mutations.py:649]
- `Meta` (class) — [saleor/graphql/core/mutations.py:655]
- `clean_input` (function) — [saleor/graphql/core/mutations.py:705]
- `success_response` (function) — [saleor/graphql/core/mutations.py:759]
- `save` (function) — [saleor/graphql/core/mutations.py:764]
- `diff_instance_data_fields` (function) — [saleor/graphql/core/mutations.py:775]
- _…and 40 more in this file_

**`saleor/graphql/core/scalars.py`**

- `Decimal` (class) — [saleor/graphql/core/scalars.py:15]
- `parse_literal` (function) — [saleor/graphql/core/scalars.py:23]
- `parse_value` (function) — [saleor/graphql/core/scalars.py:32]
- `PositiveDecimal` (class) — [saleor/graphql/core/scalars.py:49]
- `parse_value` (function) — [saleor/graphql/core/scalars.py:56]
- `parse_literal` (function) — [saleor/graphql/core/scalars.py:65]
- `JSON` (class) — [saleor/graphql/core/scalars.py:74]
- `parse_literal` (function) — [saleor/graphql/core/scalars.py:76]
- `parse_value` (function) — [saleor/graphql/core/scalars.py:87]
- `WeightScalar` (class) — [saleor/graphql/core/scalars.py:95]
- `parse_value` (function) — [saleor/graphql/core/scalars.py:97]
- `serialize` (function) — [saleor/graphql/core/scalars.py:107]
- `parse_literal` (function) — [saleor/graphql/core/scalars.py:114]
- `parse_decimal` (function) — [saleor/graphql/core/scalars.py:122]
- `parse_literal_object` (function) — [saleor/graphql/core/scalars.py:131]
- `UUID` (class) — [saleor/graphql/core/scalars.py:146]
- `serialize` (function) — [saleor/graphql/core/scalars.py:148]
- `parse_literal` (function) — [saleor/graphql/core/scalars.py:152]
- `parse_value` (function) — [saleor/graphql/core/scalars.py:159]
- `DateTime` (class) — [saleor/graphql/core/scalars.py:172]
- `parse_value` (function) — [saleor/graphql/core/scalars.py:176]
- `Date` (class) — [saleor/graphql/core/scalars.py:192]
- `parse_value` (function) — [saleor/graphql/core/scalars.py:196]
- `NonNegativeInt` (class) — [saleor/graphql/core/scalars.py:204]
- `parse_value` (function) — [saleor/graphql/core/scalars.py:211]
- `parse_literal` (function) — [saleor/graphql/core/scalars.py:220]
- `Minute` (class) — [saleor/graphql/core/scalars.py:229]
- `Hour` (class) — [saleor/graphql/core/scalars.py:233]
- `Day` (class) — [saleor/graphql/core/scalars.py:237]
- `PositiveInt` (class) — [saleor/graphql/core/scalars.py:241]
- `parse_value` (function) — [saleor/graphql/core/scalars.py:248]
- `parse_literal` (function) — [saleor/graphql/core/scalars.py:257]

**`saleor/graphql/core/schema.py`**

- `CoreQueries` (class) — [saleor/graphql/core/schema.py:11]
- `resolve_tax_types` (function) — [saleor/graphql/core/schema.py:19]
- `CoreMutations` (class) — [saleor/graphql/core/schema.py:27]

**`saleor/graphql/core/tracing.py`**

- `traced_resolver` (function) — [saleor/graphql/core/tracing.py:8]
- `wrapper` (function) — [saleor/graphql/core/tracing.py:10]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/core/__init__.py` (10 lines)
- `saleor/graphql/core/descriptions.py` (45 lines)
- `saleor/graphql/core/connection.py` (754 lines)
- `saleor/graphql/core/const.py` (2 lines)
- `saleor/graphql/core/context.py` (105 lines)
- `saleor/graphql/core/dataloaders.py` (108 lines)
- `saleor/graphql/core/doc_category.py` (101 lines)
- `saleor/graphql/core/enums.py` (486 lines)
- `saleor/graphql/core/fields.py` (176 lines)
- `saleor/graphql/core/inputs.py` (12 lines)
- `saleor/graphql/core/mutations.py` (1251 lines)
- `saleor/graphql/core/scalars.py` (263 lines)
- `saleor/graphql/core/schema.py` (28 lines)
- `saleor/graphql/core/tracing.py` (21 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`, `saleor/plugins/openid_connect`, `saleor/webhook`
- Imported by: `saleor/graphql/core/types`, `saleor/graphql/core/federation`, `saleor/graphql`

Internal dependencies named in the source:

- `...account.error_codes`
- `...account.models.User`
- `...app.error_codes`
- `...app.models.App`
- `...attribute.error_codes`
- `...channel.error_codes`
- `...channel.exceptions.ChannelNotDefined`
- `...channel.exceptions.NoDefaultChannel`
- `...checkout.error_codes`
- `...core.JobStatus`
- `...core.TimePeriodType`
- `...core.db.connection.allow_writer`
- `...core.db.connection.allow_writer_in_context`
- `...core.error_codes`
- `...core.error_codes.UploadErrorCode`
- `...core.exceptions.PermissionDenied`
- `...core.telemetry.saleor_attributes`
- `...core.telemetry.tracer`
- `...core.utils.events.call_event`
- `...core.utils.metadata_manager`
- `...core.utils.update_mutation_manager.InstanceTracker`
- `...csv.error_codes`
- `...discount.error_codes`
- `...giftcard.error_codes`
- `...invoice.error_codes`
- `...menu.error_codes`
- `...order.error_codes`
- `...page.error_codes`
- `...payment.error_codes`
- `...permission.auth_filters.AuthorizationFilters`
- `...permission.enums.AppPermission`
- `...permission.enums.BasePermissionEnum`
- `...permission.enums.get_permissions_enum_list`
- `...permission.utils.message_one_of_permissions_required`
- `...plugins.error_codes`
- `...product.error_codes`
- `...shipping.error_codes`
- `...site.error_codes`
- `...thumbnail.IconThumbnailFormat`
- `...thumbnail.ThumbnailFormat`
- `...thumbnail.models.Thumbnail`
- `...thumbnail.utils.get_thumbnail_format`
- `...translations.error_codes`
- `...warehouse.error_codes`
- `...webhook.error_codes`
- `..ResolveInfo`
- `..SaleorContext`
- `..account.utils.get_user_accessible_channels`
- `..app.dataloaders.get_app_promise`
- `..channel.utils.get_default_channel_slug_or_graphql_error`
- `..core.ResolveInfo`
- `..core.context.ChannelContext`
- `..core.context.ChannelQsContext`
- `..core.doc_category.DOC_CATEGORY_MAP`
- `..core.doc_category.DOC_CATEGORY_TAXES`
- `..core.enums.OrderDirection`
- `..core.fields.BaseField`
- `..core.types.BaseConnection`
- `..core.types.NonNullList`
- `..core.validators.validate_one_of_args_is_in_mutation`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `edcf07723c53` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
