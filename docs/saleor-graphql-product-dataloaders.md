## Purpose

`saleor/graphql/product/dataloaders` (`saleor/graphql/product/dataloaders`) groups 3 source file(s) exposing 94 top-level declaration(s).

## Public surface

**`saleor/graphql/product/dataloaders/attributes.py`**

- `BaseProductAttributesByProductTypeIdLoader` (class) — [saleor/graphql/product/dataloaders/attributes.py:12]
- `filter_attributes` (function) — [saleor/graphql/product/dataloaders/attributes.py:19]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/attributes.py:23]
- `map_attributes` (function) — [saleor/graphql/product/dataloaders/attributes.py:35]
- `ProductAttributesAllByProductTypeIdLoader` (class) — [saleor/graphql/product/dataloaders/attributes.py:59]
- `ProductAttributesVisibleInStorefrontByProductTypeIdLoader` (class) — [saleor/graphql/product/dataloaders/attributes.py:66]
- `filter_attributes` (function) — [saleor/graphql/product/dataloaders/attributes.py:73]
- `VariantAttributesAllByProductTypeIdLoader` (class) — [saleor/graphql/product/dataloaders/attributes.py:77]
- `VariantAttributesVisibleInStorefrontByProductTypeIdLoader` (class) — [saleor/graphql/product/dataloaders/attributes.py:87]
- `filter_attributes` (function) — [saleor/graphql/product/dataloaders/attributes.py:97]

**`saleor/graphql/product/dataloaders/products.py`**

- `CategoryByIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:30]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:33]
- `CategoryBySlugLoader` (class) — [saleor/graphql/product/dataloaders/products.py:38]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:41]
- `ProductByIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:48]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:51]
- `ProductByVariantIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:56]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:59]
- `with_variants` (function) — [saleor/graphql/product/dataloaders/products.py:60]
- `ProductChannelListingByIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:69]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:72]
- `ProductChannelListingByProductIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:79]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:82]
- `ProductChannelListingByProductIdAndChannelSlugLoader` (class) — [saleor/graphql/product/dataloaders/products.py:99]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:104]
- `batch_load_channel` (function) — [saleor/graphql/product/dataloaders/products.py:129]
- `ProductTypeByIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:150]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:153]
- `MediaByProductIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:160]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:163]
- `ImagesByProductIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:173]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:176]
- `ProductVariantByIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:187]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:190]
- `ProductVariantsByProductIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:197]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:200]
- `ProductVariantsByProductIdAndChannel` (class) — [saleor/graphql/product/dataloaders/products.py:212]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:217]
- `with_channels` (function) — [saleor/graphql/product/dataloaders/products.py:222]
- `get_variants_filter` (function) — [saleor/graphql/product/dataloaders/products.py:252]
- `AvailableProductVariantsByProductIdAndChannel` (class) — [saleor/graphql/product/dataloaders/products.py:259]
- `get_variants_filter` (function) — [saleor/graphql/product/dataloaders/products.py:264]
- `ProductVariantChannelListingByIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:271]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:274]
- `VariantChannelListingByVariantIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:281]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:284]
- `VariantChannelListingByVariantIdAndChannelSlugLoader` (class) — [saleor/graphql/product/dataloaders/products.py:305]
- `batch_load` (function) — [saleor/graphql/product/dataloaders/products.py:310]
- `with_channels` (function) — [saleor/graphql/product/dataloaders/products.py:313]
- `VariantChannelListingByVariantIdAndChannelIdLoader` (class) — [saleor/graphql/product/dataloaders/products.py:330]
- _…and 44 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/dataloaders/products.py` (745 lines)
- `saleor/graphql/product/dataloaders/__init__.py` (83 lines)
- `saleor/graphql/product/dataloaders/attributes.py` (98 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: `saleor/graphql/checkout/tests/mutations`

Internal dependencies named in the source:

- `....core.db.connection.allow_writer_in_context`
- `....product.ProductMediaTypes`
- `...attribute.dataloaders.attributes.AttributesByAttributeId`
- `...channel.dataloaders.by_self.ChannelBySlugLoader`
- `...core.dataloaders.BaseThumbnailBySizeAndFormatLoader`
- `...core.dataloaders.DataLoader`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `4975d0909939` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
