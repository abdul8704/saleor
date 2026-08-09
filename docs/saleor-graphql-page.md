## Purpose

`saleor/graphql/page` (`saleor/graphql/page`) groups 8 source file(s) exposing 104 top-level declaration(s).

## Public surface

**`saleor/graphql/page/bulk_mutations.py`**

- `PageBulkDelete` (class) — [saleor/graphql/page/bulk_mutations.py:26]
- `Arguments` (class) — [saleor/graphql/page/bulk_mutations.py:27]
- `Meta` (class) — [saleor/graphql/page/bulk_mutations.py:37]
- `perform_mutation` (function) — [saleor/graphql/page/bulk_mutations.py:48]
- `update_products_search_index` (function) — [saleor/graphql/page/bulk_mutations.py:62]
- `delete_assigned_attribute_values` (function) — [saleor/graphql/page/bulk_mutations.py:79]
- `PageBulkPublish` (class) — [saleor/graphql/page/bulk_mutations.py:101]
- `Arguments` (class) — [saleor/graphql/page/bulk_mutations.py:102]
- `Meta` (class) — [saleor/graphql/page/bulk_mutations.py:110]
- `bulk_action` (function) — [saleor/graphql/page/bulk_mutations.py:119]
- `PageTypeBulkDelete` (class) — [saleor/graphql/page/bulk_mutations.py:125]
- `Arguments` (class) — [saleor/graphql/page/bulk_mutations.py:126]
- `Meta` (class) — [saleor/graphql/page/bulk_mutations.py:136]
- `perform_mutation` (function) — [saleor/graphql/page/bulk_mutations.py:147]
- `update_products_search_index` (function) — [saleor/graphql/page/bulk_mutations.py:161]
- `bulk_action` (function) — [saleor/graphql/page/bulk_mutations.py:182]
- `delete_assigned_attribute_values` (function) — [saleor/graphql/page/bulk_mutations.py:191]

**`saleor/graphql/page/dataloaders.py`**

- `PageByIdLoader` (class) — [saleor/graphql/page/dataloaders.py:13]
- `batch_load` (function) — [saleor/graphql/page/dataloaders.py:16]
- `PageTypeByIdLoader` (class) — [saleor/graphql/page/dataloaders.py:21]
- `batch_load` (function) — [saleor/graphql/page/dataloaders.py:24]
- `PagesByPageTypeIdLoader` (class) — [saleor/graphql/page/dataloaders.py:29]
- `batch_load` (function) — [saleor/graphql/page/dataloaders.py:34]
- `BasePageAttributesByPageTypeIdLoader` (class) — [saleor/graphql/page/dataloaders.py:46]
- `filter_attributes` (function) — [saleor/graphql/page/dataloaders.py:52]
- `batch_load` (function) — [saleor/graphql/page/dataloaders.py:56]
- `map_attributes` (function) — [saleor/graphql/page/dataloaders.py:64]
- `PageAttributesAllByPageTypeIdLoader` (class) — [saleor/graphql/page/dataloaders.py:87]
- `PageAttributesVisibleInStorefrontByPageTypeIdLoader` (class) — [saleor/graphql/page/dataloaders.py:93]
- `filter_attributes` (function) — [saleor/graphql/page/dataloaders.py:101]

**`saleor/graphql/page/filters.py`**

- `filter_page_page_types` (function) — [saleor/graphql/page/filters.py:65]
- `filter_page_type_search` (function) — [saleor/graphql/page/filters.py:72]
- `filter_by_slug_or_name` (function) — [saleor/graphql/page/filters.py:104]
- `filter_by_numeric_attribute` (function) — [saleor/graphql/page/filters.py:120]
- `filter_by_boolean_attribute` (function) — [saleor/graphql/page/filters.py:136]
- `filter_by_date_attribute` (function) — [saleor/graphql/page/filters.py:152]
- `filter_by_date_time_attribute` (function) — [saleor/graphql/page/filters.py:168]
- `filter_by_contains_referenced_page_slugs` (function) — [saleor/graphql/page/filters.py:199]
- `filter_by_contains_referenced_product_slugs` (function) — [saleor/graphql/page/filters.py:239]
- `filter_by_contains_referenced_category_slugs` (function) — [saleor/graphql/page/filters.py:279]
- `filter_by_contains_referenced_collection_slugs` (function) — [saleor/graphql/page/filters.py:319]
- `filter_by_contains_referenced_variant_skus` (function) — [saleor/graphql/page/filters.py:361]
- `filter_by_contains_referenced_object_ids` (function) — [saleor/graphql/page/filters.py:522]
- `filter_objects_by_reference_attributes` (function) — [saleor/graphql/page/filters.py:560]
- `filter_pages_by_attributes` (function) — [saleor/graphql/page/filters.py:616]
- `PageWhere` (class) — [saleor/graphql/page/filters.py:698]
- `filter_page_slug` (function) — [saleor/graphql/page/filters.py:717]
- `filter_page_type` (function) — [saleor/graphql/page/filters.py:721]
- `filter_attributes` (function) — [saleor/graphql/page/filters.py:727]
- `is_valid` (function) — [saleor/graphql/page/filters.py:732]
- `filter_page_search` (function) — [saleor/graphql/page/filters.py:738]
- `PageFilter` (class) — [saleor/graphql/page/filters.py:743]
- `Meta` (class) — [saleor/graphql/page/filters.py:749]
- `PageFilterInput` (class) — [saleor/graphql/page/filters.py:754]
- `Meta` (class) — [saleor/graphql/page/filters.py:755]
- `PageWhereInput` (class) — [saleor/graphql/page/filters.py:760]
- `Meta` (class) — [saleor/graphql/page/filters.py:761]
- `PageTypeFilter` (class) — [saleor/graphql/page/filters.py:766]
- `PageTypeFilterInput` (class) — [saleor/graphql/page/filters.py:771]
- `Meta` (class) — [saleor/graphql/page/filters.py:772]

**`saleor/graphql/page/resolvers.py`**

- `resolve_page` (function) — [saleor/graphql/page/resolvers.py:10]
- `resolve_pages` (function) — [saleor/graphql/page/resolvers.py:43]
- `resolve_page_type` (function) — [saleor/graphql/page/resolvers.py:57]
- `resolve_page_types` (function) — [saleor/graphql/page/resolvers.py:65]

**`saleor/graphql/page/schema.py`**

- `PageQueries` (class) — [saleor/graphql/page/schema.py:38]
- `resolve_page` (function) — [saleor/graphql/page/schema.py:93]
- `resolve_pages` (function) — [saleor/graphql/page/schema.py:116]
- `resolve_page_type` (function) — [saleor/graphql/page/schema.py:139]
- `resolve_page_types` (function) — [saleor/graphql/page/schema.py:144]
- `PageMutations` (class) — [saleor/graphql/page/schema.py:152]

**`saleor/graphql/page/sorters.py`**

- `PageSortField` (class) — [saleor/graphql/page/sorters.py:5]
- `Meta` (class) — [saleor/graphql/page/sorters.py:15]
- `description` (function) — [saleor/graphql/page/sorters.py:19]
- `deprecation_reason` (function) — [saleor/graphql/page/sorters.py:37]
- `PageSortingInput` (class) — [saleor/graphql/page/sorters.py:47]
- `Meta` (class) — [saleor/graphql/page/sorters.py:48]
- `PageTypeSortField` (class) — [saleor/graphql/page/sorters.py:54]
- `Meta` (class) — [saleor/graphql/page/sorters.py:58]
- `description` (function) — [saleor/graphql/page/sorters.py:62]
- `PageTypeSortingInput` (class) — [saleor/graphql/page/sorters.py:69]
- `Meta` (class) — [saleor/graphql/page/sorters.py:70]

**`saleor/graphql/page/types.py`**

- `PageType` (class) — [saleor/graphql/page/types.py:55]
- `Meta` (class) — [saleor/graphql/page/types.py:87]
- `get_model` (function) — [saleor/graphql/page/types.py:96]
- `resolve_attributes` (function) — [saleor/graphql/page/types.py:100]
- `wrap_with_channel_context` (function) — [saleor/graphql/page/types.py:101]
- `resolve_available_attributes` (function) — [saleor/graphql/page/types.py:117]
- `resolve_has_pages` (function) — [saleor/graphql/page/types.py:132]
- `PageTypeCountableConnection` (class) — [saleor/graphql/page/types.py:147]
- `Meta` (class) — [saleor/graphql/page/types.py:148]
- `Page` (class) — [saleor/graphql/page/types.py:153]
- `Meta` (class) — [saleor/graphql/page/types.py:222]
- `resolve_publication_date` (function) — [saleor/graphql/page/types.py:232]
- `resolve_created` (function) — [saleor/graphql/page/types.py:236]
- `resolve_page_type` (function) — [saleor/graphql/page/types.py:240]
- `resolve_content_json` (function) — [saleor/graphql/page/types.py:244]
- `resolve_assigned_attributes` (function) — [saleor/graphql/page/types.py:249]
- `resolve_assigned_attribute` (function) — [saleor/graphql/page/types.py:258]
- `resolve_attributes` (function) — [saleor/graphql/page/types.py:264]
- `get_assigned_attributes` (function) — [saleor/graphql/page/types.py:276]
- `resolve_attribute` (function) — [saleor/graphql/page/types.py:295]
- `with_assigned_attribute` (function) — [saleor/graphql/page/types.py:306]
- `PageCountableConnection` (class) — [saleor/graphql/page/types.py:327]
- `Meta` (class) — [saleor/graphql/page/types.py:328]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/page/__init__.py` (1 lines)
- `saleor/graphql/page/bulk_mutations.py` (210 lines)
- `saleor/graphql/page/dataloaders.py` (102 lines)
- `saleor/graphql/page/filters.py` (774 lines)
- `saleor/graphql/page/resolvers.py` (68 lines)
- `saleor/graphql/page/schema.py` (171 lines)
- `saleor/graphql/page/sorters.py` (73 lines)
- `saleor/graphql/page/types.py` (330 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...attribute.AttributeInputType`
- `...attribute.lock_objects.attribute_value_qs_select_for_update`
- `...attribute.models`
- `...attribute.models.Attribute`
- `...attribute.models.AttributePage`
- `...channel.models.Channel`
- `...core.search.prefix_search`
- `...core.tracing.traced_atomic_transaction`
- `...page.models`
- `...page.models.Page`
- `...page.models.PageType`
- `...permission.enums.PagePermissions`
- `...permission.enums.PageTypePermissions`
- `...permission.utils.all_permissions_required`
- `...product.models.Product`
- `...webhook.event_types.WebhookEventAsyncType`
- `...webhook.utils.get_webhooks_for_event`
- `..attribute.utils.shared.AssignedAttributeData`
- `..channel.dataloaders.by_self.ChannelBySlugLoader`
- `..core.ResolveInfo`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.const.DEFAULT_NESTED_LIST_LIMIT`
- `..core.context.ChannelContext`
- `..core.context.ChannelQsContext`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.descriptions.ADDED_IN_322`
- `..core.descriptions.DEPRECATED_IN_3X_INPUT`
- `..core.descriptions.RICH_CONTENT`
- `..core.doc_category.DOC_CATEGORY_PAGES`
- `..core.enums.LanguageCodeEnum`
- `..core.federation.federated_entity`
- `..core.federation.resolve_federation_references`
- `..core.fields.BaseField`
- `..core.fields.FilterConnectionField`
- `..core.fields.JSONString`
- `..core.fields.PermissionsField`
- `..core.mutations.BaseBulkMutation`
- `..core.mutations.ModelBulkDeleteMutation`
- `..core.scalars.Date`
- `..core.scalars.DateTime`
- `..core.scalars.PositiveInt`
- `..core.types.BaseEnum`
- `..core.types.ModelObjectType`
- `..core.types.NonNullList`
- `..core.types.PageError`
- `..core.types.SortInputObjectType`
- `..core.types.context.ChannelContextType`
- `..core.utils.from_global_id_or_error`
- `..core.utils.validate_and_apply_search_rank_sorting`
- `..core.validators.validate_one_of_args_is_in_query`
- `..meta.types.ObjectWithMetadata`
- `..plugins.dataloaders.get_plugin_manager_promise`
- `..translations.fields.TranslationField`
- `..translations.mutations.PageTranslate`
- `..translations.types.PageTranslation`
- `..utils.get_user_or_app_from_context`
- `..utils.resolve_global_ids_to_primary_keys`
- `.bulk_mutations.PageBulkDelete`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `f04acc6dd5df` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
