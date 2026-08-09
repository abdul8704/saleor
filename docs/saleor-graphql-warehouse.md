## Purpose

`saleor/graphql/warehouse` (`saleor/graphql/warehouse`) groups 10 source file(s) exposing 119 top-level declaration(s).

## Public surface

**`saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py`**

- `StockBulkResult` (class) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:33]
- `Meta` (class) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:41]
- `StockBulkUpdateInput` (class) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:45]
- `Meta` (class) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:58]
- `StockBulkUpdate` (class) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:62]
- `Arguments` (class) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:75]
- `Meta` (class) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:89]
- `validate_variant` (function) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:106]
- `validate_warehouse` (function) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:153]
- `get_selectors` (function) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:205]
- `clean_stocks` (function) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:248]
- `update_stocks` (function) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:296]
- `get_stocks` (function) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:340]
- `save_stocks` (function) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:384]
- `post_save_actions` (function) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:397]
- `get_results` (function) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:411]
- `perform_mutation` (function) — [saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py:427]

**`saleor/graphql/warehouse/dataloaders.py`**

- `WithAvailableQuantity` (class) — [saleor/graphql/warehouse/dataloaders.py:38]
- `AvailableQuantityByProductVariantIdCountryCodeAndChannelSlugLoader` (class) — [saleor/graphql/warehouse/dataloaders.py:50]
- `batch_load` (function) — [saleor/graphql/warehouse/dataloaders.py:62]
- `batch_load_quantities_by_country` (function) — [saleor/graphql/warehouse/dataloaders.py:94]
- `get_warehouse_shipping_zones` (function) — [saleor/graphql/warehouse/dataloaders.py:161]
- `get_click_and_collect_warehouses` (function) — [saleor/graphql/warehouse/dataloaders.py:209]
- `prepare_stocks_reservations_map` (function) — [saleor/graphql/warehouse/dataloaders.py:235]
- `prepare_warehouse_ids_by_shipping_zone_and_variant_map` (function) — [saleor/graphql/warehouse/dataloaders.py:254]
- `prepare_quantity_map` (function) — [saleor/graphql/warehouse/dataloaders.py:320]
- `StocksWithAvailableQuantityByProductVariantIdCountryCodeAndChannelLoader` (class) — [saleor/graphql/warehouse/dataloaders.py:377]
- `batch_load` (function) — [saleor/graphql/warehouse/dataloaders.py:388]
- `with_channels` (function) — [saleor/graphql/warehouse/dataloaders.py:389]
- `with_shipping_zones` (function) — [saleor/graphql/warehouse/dataloaders.py:390]
- `with_warehouses` (function) — [saleor/graphql/warehouse/dataloaders.py:391]
- `get_relevant_warehouses` (function) — [saleor/graphql/warehouse/dataloaders.py:518]
- `AvailableQuantityByProductVariantIdAndChannelSlugLoader` (class) — [saleor/graphql/warehouse/dataloaders.py:573]
- `prepare_stocks_reservations_map` (function) — [saleor/graphql/warehouse/dataloaders.py:584]
- `batch_load` (function) — [saleor/graphql/warehouse/dataloaders.py:599]
- `with_stocks_and_site` (function) — [saleor/graphql/warehouse/dataloaders.py:600]
- `StocksWithAvailableQuantityByProductVariantIdAndChannelSlugLoader` (class) — [saleor/graphql/warehouse/dataloaders.py:637]
- `batch_load` (function) — [saleor/graphql/warehouse/dataloaders.py:647]
- `with_channels` (function) — [saleor/graphql/warehouse/dataloaders.py:652]
- `with_warehouses` (function) — [saleor/graphql/warehouse/dataloaders.py:653]
- `StocksReservationsByCheckoutTokenLoader` (class) — [saleor/graphql/warehouse/dataloaders.py:715]
- `batch_load` (function) — [saleor/graphql/warehouse/dataloaders.py:718]
- `with_checkouts_lines` (function) — [saleor/graphql/warehouse/dataloaders.py:721]
- `with_lines_reservations` (function) — [saleor/graphql/warehouse/dataloaders.py:727]
- `ActiveReservationsByCheckoutLineIdLoader` (class) — [saleor/graphql/warehouse/dataloaders.py:749]
- `batch_load` (function) — [saleor/graphql/warehouse/dataloaders.py:752]
- `PreorderQuantityReservedByVariantChannelListingIdLoader` (class) — [saleor/graphql/warehouse/dataloaders.py:775]
- `batch_load` (function) — [saleor/graphql/warehouse/dataloaders.py:778]
- `WarehouseByIdLoader` (class) — [saleor/graphql/warehouse/dataloaders.py:799]
- `batch_load` (function) — [saleor/graphql/warehouse/dataloaders.py:802]
- `StockByIdLoader` (class) — [saleor/graphql/warehouse/dataloaders.py:809]
- `batch_load` (function) — [saleor/graphql/warehouse/dataloaders.py:812]
- `StocksByWarehouseIdLoader` (class) — [saleor/graphql/warehouse/dataloaders.py:817]
- `batch_load` (function) — [saleor/graphql/warehouse/dataloaders.py:820]
- `WarehousesByChannelIdLoader` (class) — [saleor/graphql/warehouse/dataloaders.py:830]
- `batch_load` (function) — [saleor/graphql/warehouse/dataloaders.py:833]
- `map_warehouses` (function) — [saleor/graphql/warehouse/dataloaders.py:843]
- _…and 5 more in this file_

**`saleor/graphql/warehouse/filters.py`**

- `prefech_qs_for_filter` (function) — [saleor/graphql/warehouse/filters.py:23]
- `filter_search_warehouse` (function) — [saleor/graphql/warehouse/filters.py:27]
- `filter_click_and_collect_option` (function) — [saleor/graphql/warehouse/filters.py:49]
- `filter_channels` (function) — [saleor/graphql/warehouse/filters.py:63]
- `filter_search_stock` (function) — [saleor/graphql/warehouse/filters.py:74]
- `WarehouseFilter` (class) — [saleor/graphql/warehouse/filters.py:101]
- `Meta` (class) — [saleor/graphql/warehouse/filters.py:112]
- `WarehouseFilterInput` (class) — [saleor/graphql/warehouse/filters.py:117]
- `Meta` (class) — [saleor/graphql/warehouse/filters.py:118]
- `StockFilter` (class) — [saleor/graphql/warehouse/filters.py:123]
- `Meta` (class) — [saleor/graphql/warehouse/filters.py:126]
- `StockFilterInput` (class) — [saleor/graphql/warehouse/filters.py:131]
- `Meta` (class) — [saleor/graphql/warehouse/filters.py:132]

**`saleor/graphql/warehouse/resolvers.py`**

- `resolve_stock` (function) — [saleor/graphql/warehouse/resolvers.py:5]
- `resolve_stocks` (function) — [saleor/graphql/warehouse/resolvers.py:13]
- `resolve_warehouses` (function) — [saleor/graphql/warehouse/resolvers.py:17]

**`saleor/graphql/warehouse/schema.py`**

- `WarehouseQueries` (class) — [saleor/graphql/warehouse/schema.py:34]
- `resolve_warehouse` (function) — [saleor/graphql/warehouse/schema.py:63]
- `resolve_warehouses` (function) — [saleor/graphql/warehouse/schema.py:71]
- `WarehouseMutations` (class) — [saleor/graphql/warehouse/schema.py:79]
- `StockQueries` (class) — [saleor/graphql/warehouse/schema.py:87]
- `resolve_stock` (function) — [saleor/graphql/warehouse/schema.py:104]
- `resolve_stocks` (function) — [saleor/graphql/warehouse/schema.py:109]
- `StockMutations` (class) — [saleor/graphql/warehouse/schema.py:117]

**`saleor/graphql/warehouse/sorters.py`**

- `WarehouseSortField` (class) — [saleor/graphql/warehouse/sorters.py:5]
- `Meta` (class) — [saleor/graphql/warehouse/sorters.py:8]
- `description` (function) — [saleor/graphql/warehouse/sorters.py:12]
- `WarehouseSortingInput` (class) — [saleor/graphql/warehouse/sorters.py:19]
- `Meta` (class) — [saleor/graphql/warehouse/sorters.py:20]

**`saleor/graphql/warehouse/types.py`**

- `WarehouseInput` (class) — [saleor/graphql/warehouse/types.py:31]
- `Meta` (class) — [saleor/graphql/warehouse/types.py:38]
- `WarehouseCreateInput` (class) — [saleor/graphql/warehouse/types.py:42]
- `Meta` (class) — [saleor/graphql/warehouse/types.py:56]
- `WarehouseUpdateInput` (class) — [saleor/graphql/warehouse/types.py:60]
- `Meta` (class) — [saleor/graphql/warehouse/types.py:76]
- `Warehouse` (class) — [saleor/graphql/warehouse/types.py:80]
- `Meta` (class) — [saleor/graphql/warehouse/types.py:119]
- `resolve_shipping_zones` (function) — [saleor/graphql/warehouse/types.py:125]
- `resolve_stocks` (function) — [saleor/graphql/warehouse/types.py:145]
- `resolve_address` (function) — [saleor/graphql/warehouse/types.py:156]
- `resolve_company_name` (function) — [saleor/graphql/warehouse/types.py:163]
- `WarehouseCountableConnection` (class) — [saleor/graphql/warehouse/types.py:174]
- `Meta` (class) — [saleor/graphql/warehouse/types.py:175]
- `Stock` (class) — [saleor/graphql/warehouse/types.py:180]
- `Meta` (class) — [saleor/graphql/warehouse/types.py:221]
- `resolve_quantity` (function) — [saleor/graphql/warehouse/types.py:227]
- `resolve_quantity_allocated` (function) — [saleor/graphql/warehouse/types.py:231]
- `resolve_quantity_reserved` (function) — [saleor/graphql/warehouse/types.py:236]
- `resolve_warehouse` (function) — [saleor/graphql/warehouse/types.py:253]
- `resolve_product_variant` (function) — [saleor/graphql/warehouse/types.py:259]
- `StockCountableConnection` (class) — [saleor/graphql/warehouse/types.py:267]
- `Meta` (class) — [saleor/graphql/warehouse/types.py:268]
- `Allocation` (class) — [saleor/graphql/warehouse/types.py:273]
- `Meta` (class) — [saleor/graphql/warehouse/types.py:294]
- `get_node` (function) — [saleor/graphql/warehouse/types.py:301]
- `resolve_warehouse` (function) — [saleor/graphql/warehouse/types.py:308]
- `resolve_quantity` (function) — [saleor/graphql/warehouse/types.py:312]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/warehouse/bulk_mutations/stock_bulk_update.py` (460 lines)
- `saleor/graphql/warehouse/types.py` (313 lines)
- `saleor/graphql/warehouse/__init__.py` (1 lines)
- `saleor/graphql/warehouse/bulk_mutations/__init__.py` (3 lines)
- `saleor/graphql/warehouse/dataloaders.py` (902 lines)
- `saleor/graphql/warehouse/enums.py` (12 lines)
- `saleor/graphql/warehouse/filters.py` (134 lines)
- `saleor/graphql/warehouse/resolvers.py` (20 lines)
- `saleor/graphql/warehouse/schema.py` (118 lines)
- `saleor/graphql/warehouse/sorters.py` (23 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`
- Imported by: `saleor/graphql/warehouse/tests`, `saleor/graphql/product/filters`

Internal dependencies named in the source:

- `....core.tracing.traced_atomic_transaction`
- `....core.utils.events.call_event`
- `....permission.enums.ProductPermissions`
- `....warehouse.error_codes.StockBulkUpdateErrorCode`
- `....warehouse.lock_objects.stock_qs_select_for_update`
- `....warehouse.models`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.utils.get_webhooks_for_event`
- `...account.models.Address`
- `...channel.models.Channel`
- `...core.doc_category.DOC_CATEGORY_PRODUCTS`
- `...core.enums.ErrorPolicyEnum`
- `...core.mutations.BaseMutation`
- `...core.utils.WebhookEventInfo`
- `...core.validators.validate_one_of_args_is_in_mutation`
- `...graphql.core.enums.to_enum`
- `...permission.enums.OrderPermissions`
- `...permission.enums.ProductPermissions`
- `...product.models.Product`
- `...product.models.ProductVariant`
- `...product.models.ProductVariantChannelListing`
- `...utils.get_user_or_app_from_context`
- `...warehouse.WarehouseClickAndCollectOption`
- `...warehouse.models`
- `...warehouse.models.Stock`
- `...warehouse.models.Warehouse`
- `...warehouse.reservations.is_reservation_enabled`
- `..account.dataloaders.AddressByIdLoader`
- `..channel.dataloaders.by_self.ChannelBySlugLoader`
- `..channel.types.Channel`
- `..checkout.dataloaders.CheckoutLinesByCheckoutTokenLoader`
- `..core.ResolveInfo`
- `..core.connection.CountableConnection`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.context.ChannelContext`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.doc_category.DOC_CATEGORY_PRODUCTS`
- `..core.fields.ConnectionField`
- `..core.fields.FilterConnectionField`
- `..core.fields.PermissionsField`
- `..core.types.BaseEnum`
- `..core.types.SortInputObjectType`
- `..core.utils.from_global_id_or_error`
- `..core.utils.resolvers.resolve_by_global_id_or_ext_ref`
- `..meta.types.ObjectWithMetadata`
- `..product.dataloaders.ProductVariantByIdLoader`
- `..shipping.types.ShippingZoneCountableConnection`
- `..site.dataloaders.get_site_promise`
- `..site.dataloaders.load_site_callback`
- `..types.Stock`
- `..utils.filters.filter_slug_list`
- `..utils.resolve_global_ids_to_primary_keys`
- `..warehouse.enums.WarehouseClickAndCollectOptionEnum`
- `.bulk_mutations.StockBulkUpdate`
- `.dataloaders.StocksByWarehouseIdLoader`
- `.dataloaders.WarehouseByIdLoader`
- `.enums.WarehouseClickAndCollectOptionEnum`
- `.filters.StockFilterInput`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `bf3adf04ccde` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
