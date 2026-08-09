## Purpose

`saleor/product/utils` (`saleor/product/utils`) groups 8 source file(s) exposing 29 top-level declaration(s).

## Public surface

**`saleor/product/utils/__init__.py`**

- `calculate_revenue_for_variant` (function) — [saleor/product/utils/__init__.py:21]
- `delete_categories` (function) — [saleor/product/utils/__init__.py:38]
- `collect_categories_tree_products` (function) — [saleor/product/utils/__init__.py:70]
- `get_products_ids_without_variants` (function) — [saleor/product/utils/__init__.py:79]

**`saleor/product/utils/availability.py`**

- `ProductAvailability` (class) — [saleor/product/utils/availability.py:13]
- `VariantAvailability` (class) — [saleor/product/utils/availability.py:23]
- `get_product_price_range` (function) — [saleor/product/utils/availability.py:56]
- `get_product_availability` (function) — [saleor/product/utils/availability.py:119]
- `get_variant_availability` (function) — [saleor/product/utils/availability.py:178]

**`saleor/product/utils/costs.py`**

- `CostsData` (class) — [saleor/product/utils/costs.py:15]
- `get_product_costs_data` (function) — [saleor/product/utils/costs.py:24]
- `get_cost_data_from_variant_channel_listing` (function) — [saleor/product/utils/costs.py:41]
- `get_variant_costs_data` (function) — [saleor/product/utils/costs.py:53]
- `get_cost_price` (function) — [saleor/product/utils/costs.py:65]
- `get_margin_for_variant_channel_listing` (function) — [saleor/product/utils/costs.py:71]

**`saleor/product/utils/product.py`**

- `get_channel_to_products_map_from_rules` (function) — [saleor/product/utils/product.py:12]
- `mark_products_in_channels_as_dirty_based_on_rules` (function) — [saleor/product/utils/product.py:65]
- `mark_products_in_channels_as_dirty` (function) — [saleor/product/utils/product.py:82]

**`saleor/product/utils/search_helpers.py`**

- `mark_products_search_vector_as_dirty_in_batches` (function) — [saleor/product/utils/search_helpers.py:7]

**`saleor/product/utils/tasks_utils.py`**

- `validate_status_code` (function) — [saleor/product/utils/tasks_utils.py:11]
- `validate_content_type_header` (function) — [saleor/product/utils/tasks_utils.py:19]
- `create_image` (function) — [saleor/product/utils/tasks_utils.py:27]
- `validate_image_mime_type` (function) — [saleor/product/utils/tasks_utils.py:32]
- `validate_image_exif` (function) — [saleor/product/utils/tasks_utils.py:40]
- `update_product_media` (function) — [saleor/product/utils/tasks_utils.py:56]

**`saleor/product/utils/variant_prices.py`**

- `update_discounted_prices_for_promotion` (function) — [saleor/product/utils/variant_prices.py:29]

**`saleor/product/utils/variants.py`**

- `generate_and_set_variant_name` (function) — [saleor/product/utils/variants.py:16]
- `get_variant_selection_attributes` (function) — [saleor/product/utils/variants.py:41]
- `fetch_variants_for_promotion_rules` (function) — [saleor/product/utils/variants.py:56]

## How it works

The module's files, as provided to this run:

- `saleor/product/utils/__init__.py` (85 lines)
- `saleor/product/utils/availability.py` (228 lines)
- `saleor/product/utils/costs.py` (81 lines)
- `saleor/product/utils/product.py` (136 lines)
- `saleor/product/utils/search_helpers.py` (11 lines)
- `saleor/product/utils/tasks_utils.py` (59 lines)
- `saleor/product/utils/variant_prices.py` (363 lines)
- `saleor/product/utils/variants.py` (74 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`, `saleor/plugins/openid_connect`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...attribute.AttributeType`
- `...attribute.models.AssignedVariantAttribute`
- `...attribute.models.Attribute`
- `...channel.models.Channel`
- `...core.taxes.TaxedMoney`
- `...core.taxes.zero_money`
- `...core.taxes.zero_taxed_money`
- `...core.tracing.traced_atomic_transaction`
- `...core.utils.create_file_from_response`
- `...core.utils.events.call_event`
- `...core.utils.validators.is_valid_image_content_type`
- `...discount.PromotionRuleInfo`
- `...discount.models.PromotionRule`
- `...discount.utils.promotion.mark_active_catalogue_promotion_rules_as_dirty`
- `...discount.utils.promotion.update_rule_variant_relation`
- `...graphql.discount.utils.get_variants_for_catalogue_predicate`
- `...order.models.Order`
- `...order.models.OrderLine`
- `...product.models.ProductChannelListing`
- `...product.models.ProductVariantChannelListing`
- `...tax.TaxCalculationStrategy`
- `...tax.calculations.calculate_flat_rate_tax`
- `...thumbnail.utils.ProcessedImage`
- `...thumbnail.utils.get_filename_from_url`
- `...webhook.event_types.WebhookEventAsyncType`
- `...webhook.utils.get_webhooks_for_event`
- `..interface.VariantDiscountedPriceChange`
- `..managers.ProductVariantQueryset`
- `..managers.ProductsQueryset`
- `..models.Category`
- `..models.Product`
- `..models.ProductChannelListing`
- `..models.ProductVariant`
- `..models.ProductVariantChannelListing`
- `..tasks.mark_products_search_vector_as_dirty`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `f670f640d2ee` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
