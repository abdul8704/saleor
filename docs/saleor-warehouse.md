## Purpose

`saleor/warehouse` (`saleor/warehouse`) groups 11 source file(s) exposing 100 top-level declaration(s).

## Public surface

**`saleor/warehouse/__init__.py`**

- `WarehouseClickAndCollectOption` (class) — [saleor/warehouse/__init__.py:1]

**`saleor/warehouse/availability.py`**

- `ChannelListingPreorderAvailbilityInfo` (class) — [saleor/warehouse/availability.py:30]
- `VariantsChannelAvailbilityInfo` (class) — [saleor/warehouse/availability.py:36]
- `check_stock_and_preorder_quantity` (function) — [saleor/warehouse/availability.py:63]
- `check_stock_quantity` (function) — [saleor/warehouse/availability.py:103]
- `check_stock_and_preorder_quantity_bulk` (function) — [saleor/warehouse/availability.py:149]
- `check_stock_quantity_bulk` (function) — [saleor/warehouse/availability.py:244]
- `check_preorder_threshold_in_orders` (function) — [saleor/warehouse/availability.py:393]
- `check_preorder_threshold_bulk` (function) — [saleor/warehouse/availability.py:465]
- `get_available_quantity` (function) — [saleor/warehouse/availability.py:543]
- `is_product_in_stock` (function) — [saleor/warehouse/availability.py:564]
- `get_reserved_stock_quantity` (function) — [saleor/warehouse/availability.py:580]
- `get_reserved_stock_quantity_bulk` (function) — [saleor/warehouse/availability.py:597]

**`saleor/warehouse/channel_stock_availability.py`**

- `SourceWarehouseData` (class) — [saleor/warehouse/channel_stock_availability.py:34]
- `trigger_out_of_stock_in_channel_events_for_stocks` (function) — [saleor/warehouse/channel_stock_availability.py:48]
- `trigger_back_in_stock_in_channel_events_for_stocks` (function) — [saleor/warehouse/channel_stock_availability.py:109]
- `get_warehouse_to_channels_map` (function) — [saleor/warehouse/channel_stock_availability.py:345]
- `get_source_warehouses_data` (function) — [saleor/warehouse/channel_stock_availability.py:357]

**`saleor/warehouse/error_codes.py`**

- `WarehouseErrorCode` (class) — [saleor/warehouse/error_codes.py:4]
- `StockErrorCode` (class) — [saleor/warehouse/error_codes.py:13]
- `StockBulkUpdateErrorCode` (class) — [saleor/warehouse/error_codes.py:22]

**`saleor/warehouse/interface.py`**

- `VariantChannelStockInfo` (class) — [saleor/warehouse/interface.py:5]
- `pk` (function) — [saleor/warehouse/interface.py:10]

**`saleor/warehouse/lock_objects.py`**

- `stock_select_for_update_for_existing_qs` (function) — [saleor/warehouse/lock_objects.py:4]
- `stock_qs_select_for_update` (function) — [saleor/warehouse/lock_objects.py:8]
- `allocation_with_stock_qs_select_for_update` (function) — [saleor/warehouse/lock_objects.py:12]

**`saleor/warehouse/management.py`**

- `StockData` (class) — [saleor/warehouse/management.py:55]
- `delete_stocks` (function) — [saleor/warehouse/management.py:60]
- `stock_bulk_update` (function) — [saleor/warehouse/management.py:70]
- `delete_allocations` (function) — [saleor/warehouse/management.py:80]
- `allocate_stocks` (function) — [saleor/warehouse/management.py:91]
- `sort_stocks` (function) — [saleor/warehouse/management.py:268]
- `sort_stocks_by_highest_stocks` (function) — [saleor/warehouse/management.py:280]
- `sort_stocks_by_warehouse_sorting_order` (function) — [saleor/warehouse/management.py:290]
- `deallocate_stock` (function) — [saleor/warehouse/management.py:359]
- `increase_stock` (function) — [saleor/warehouse/management.py:456]
- `increase_allocations` (function) — [saleor/warehouse/management.py:520]
- `decrease_allocations` (function) — [saleor/warehouse/management.py:568]
- `decrease_stock` (function) — [saleor/warehouse/management.py:586]
- `get_order_lines_with_track_inventory` (function) — [saleor/warehouse/management.py:715]
- `get_order_lines_to_deallocate` (function) — [saleor/warehouse/management.py:734]
- `deallocate_stock_for_orders` (function) — [saleor/warehouse/management.py:763]
- `allocate_preorders` (function) — [saleor/warehouse/management.py:811]
- `get_order_lines_with_preorder` (function) — [saleor/warehouse/management.py:912]
- `deactivate_preorder_for_variant` (function) — [saleor/warehouse/management.py:970]

**`saleor/warehouse/models.py`**

- `WithAvailableQuantity` (class) — [saleor/warehouse/models.py:28]
- `WithTotalAvailableQuantity` (class) — [saleor/warehouse/models.py:31]
- `WarehouseQueryset` (class) — [saleor/warehouse/models.py:43]
- `for_channel` (function) — [saleor/warehouse/models.py:44]
- `for_channel_with_active_shipping_zone_or_cc` (function) — [saleor/warehouse/models.py:54]
- `for_country_and_channel` (function) — [saleor/warehouse/models.py:87]
- `applicable_for_click_and_collect_no_quantity_check` (function) — [saleor/warehouse/models.py:116]
- `applicable_for_click_and_collect` (function) — [saleor/warehouse/models.py:165]
- `ChannelWarehouse` (class) — [saleor/warehouse/models.py:265]
- `Meta` (class) — [saleor/warehouse/models.py:273]
- `get_ordering_queryset` (function) — [saleor/warehouse/models.py:277]
- `Warehouse` (class) — [saleor/warehouse/models.py:284]
- `Meta` (class) — [saleor/warehouse/models.py:305]
- `countries` (function) — [saleor/warehouse/models.py:319]
- `delete` (function) — [saleor/warehouse/models.py:323]
- `StockQuerySet` (class) — [saleor/warehouse/models.py:329]
- `annotate_available_quantity` (function) — [saleor/warehouse/models.py:330]
- `annotate_reserved_quantity` (function) — [saleor/warehouse/models.py:348]
- `for_channel_and_click_and_collect` (function) — [saleor/warehouse/models.py:359]
- `for_channel_and_country` (function) — [saleor/warehouse/models.py:377]
- `for_channel` (function) — [saleor/warehouse/models.py:440]
- `for_channel_or_country` (function) — [saleor/warehouse/models.py:454]
- `get_variant_stocks` (function) — [saleor/warehouse/models.py:474]
- `get_variants_stocks` (function) — [saleor/warehouse/models.py:489]
- `get_product_stocks` (function) — [saleor/warehouse/models.py:506]
- `Stock` (class) — [saleor/warehouse/models.py:527]
- `Meta` (class) — [saleor/warehouse/models.py:537]
- `increase_stock` (function) — [saleor/warehouse/models.py:541]
- `decrease_stock` (function) — [saleor/warehouse/models.py:547]
- `AllocationQueryset` (class) — [saleor/warehouse/models.py:553]
- `annotate_stock_available_quantity` (function) — [saleor/warehouse/models.py:554]
- `available_quantity_for_stock` (function) — [saleor/warehouse/models.py:560]
- `Allocation` (class) — [saleor/warehouse/models.py:573]
- `Meta` (class) — [saleor/warehouse/models.py:592]
- `PreorderAllocation` (class) — [saleor/warehouse/models.py:597]
- `Meta` (class) — [saleor/warehouse/models.py:614]
- `ReservationQuerySet` (class) — [saleor/warehouse/models.py:622]
- `not_expired` (function) — [saleor/warehouse/models.py:623]
- `exclude_checkout_lines` (function) — [saleor/warehouse/models.py:626]
- `PreorderReservation` (class) — [saleor/warehouse/models.py:636]
- _…and 3 more in this file_

**`saleor/warehouse/reservations.py`**

- `StockData` (class) — [saleor/warehouse/reservations.py:23]
- `reserve_stocks_and_preorders` (function) — [saleor/warehouse/reservations.py:29]
- `reserve_stocks` (function) — [saleor/warehouse/reservations.py:91]
- `reserve_preorders` (function) — [saleor/warehouse/reservations.py:247]
- `get_checkout_lines_to_reserve` (function) — [saleor/warehouse/reservations.py:385]
- `is_reservation_enabled` (function) — [saleor/warehouse/reservations.py:401]
- `get_reservation_length` (function) — [saleor/warehouse/reservations.py:408]
- `get_listings_reservations` (function) — [saleor/warehouse/reservations.py:414]

**`saleor/warehouse/tasks.py`**

- `delete_empty_allocations_task` (function) — [saleor/warehouse/tasks.py:16]
- `delete_expired_reservations_task` (function) — [saleor/warehouse/tasks.py:27]
- `update_stocks_quantity_allocated_task` (function) — [saleor/warehouse/tasks.py:45]

**`saleor/warehouse/validation.py`**

- `validate_warehouse_count` (function) — [saleor/warehouse/validation.py:5]

## How it works

The module's files, as provided to this run:

- `saleor/warehouse/channel_stock_availability.py` (379 lines)
- `saleor/warehouse/__init__.py` (10 lines)
- `saleor/warehouse/models.py` (689 lines)
- `saleor/warehouse/availability.py` (623 lines)
- `saleor/warehouse/error_codes.py` (26 lines)
- `saleor/warehouse/interface.py` (16 lines)
- `saleor/warehouse/lock_objects.py` (22 lines)
- `saleor/warehouse/management.py` (1077 lines)
- `saleor/warehouse/reservations.py` (437 lines)
- `saleor/warehouse/tasks.py` (68 lines)
- `saleor/warehouse/validation.py` (24 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/plugins/openid_connect`, `saleor/core/db`, `saleor/core`
- Imported by: `saleor/warehouse/tests`, `saleor/graphql/product/tests/mutations`, `saleor/graphql/warehouse/tests/mutations`, `saleor/product`

Internal dependencies named in the source:

- `..WarehouseClickAndCollectOption`
- `..account.models.Address`
- `..account.models.User`
- `..app.models.App`
- `..celeryconf.app`
- `..channel.AllocationStrategy`
- `..channel.models.Channel`
- `..checkout.error_codes.CheckoutErrorCode`
- `..checkout.fetch.CheckoutLine`
- `..checkout.fetch.CheckoutLineInfo`
- `..checkout.fetch.DeliveryMethodBase`
- `..checkout.models.CheckoutLine`
- `..core.db.connection.allow_writer`
- `..core.exceptions.InsufficientStock`
- `..core.exceptions.InsufficientStockData`
- `..core.models.ModelWithExternalReference`
- `..core.models.ModelWithMetadata`
- `..core.models.SortableModel`
- `..core.tracing.traced_atomic_transaction`
- `..core.utils.country.get_active_country`
- `..order.fetch.OrderLineInfo`
- `..order.models.OrderLine`
- `..order.utils.get_order_country`
- `..product.models.Product`
- `..product.models.ProductVariant`
- `..product.models.ProductVariantChannelListing`
- `..shipping.models.ShippingZone`
- `..site.models.SiteSettings`
- `..webhook.models.Webhook`
- `.interface.VariantChannelStockInfo`
- `.lock_objects.stock_qs_select_for_update`
- `.management.delete_allocations`
- `.management.sort_stocks`
- `.management.stock_bulk_update`
- `.models.Allocation`
- `.models.ChannelWarehouse`
- `.models.PreorderReservation`
- `.models.Reservation`
- `.models.Stock`
- `.models.StockQuerySet`
- `.models.Warehouse`
- `.reservations.get_listings_reservations`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c2c6a1514854` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
