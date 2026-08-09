## Purpose

`saleor/graphql/product/mutations` (`saleor/graphql/product/mutations`) groups 4 source file(s) exposing 91 top-level declaration(s).

## Public surface

**`saleor/graphql/product/mutations/attributes.py`**

- `ProductAttributeAssignInput` (class) — [saleor/graphql/product/mutations/attributes.py:32]
- `Meta` (class) — [saleor/graphql/product/mutations/attributes.py:45]
- `ProductAttributeAssignmentUpdateInput` (class) — [saleor/graphql/product/mutations/attributes.py:49]
- `Meta` (class) — [saleor/graphql/product/mutations/attributes.py:59]
- `VariantAssignmentValidationMixin` (class) — [saleor/graphql/product/mutations/attributes.py:63]
- `check_allowed_types` (function) — [saleor/graphql/product/mutations/attributes.py:65]
- `ProductAttributeAssign` (class) — [saleor/graphql/product/mutations/attributes.py:96]
- `Arguments` (class) — [saleor/graphql/product/mutations/attributes.py:99]
- `Meta` (class) — [saleor/graphql/product/mutations/attributes.py:110]
- `get_operations` (function) — [saleor/graphql/product/mutations/attributes.py:118]
- `check_attributes_types` (function) — [saleor/graphql/product/mutations/attributes.py:142]
- `check_operations_not_assigned_already` (function) — [saleor/graphql/product/mutations/attributes.py:162]
- `check_type_and_variant_coherence` (function) — [saleor/graphql/product/mutations/attributes.py:190]
- `check_product_operations_are_assignable` (function) — [saleor/graphql/product/mutations/attributes.py:206]
- `clean_operations` (function) — [saleor/graphql/product/mutations/attributes.py:224]
- `save_field_values` (function) — [saleor/graphql/product/mutations/attributes.py:261]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/attributes.py:280]
- `ProductAttributeUnassign` (class) — [saleor/graphql/product/mutations/attributes.py:302]
- `Arguments` (class) — [saleor/graphql/product/mutations/attributes.py:305]
- `Meta` (class) — [saleor/graphql/product/mutations/attributes.py:318]
- `save_field_values` (function) — [saleor/graphql/product/mutations/attributes.py:326]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/attributes.py:331]
- `ProductAttributeAssignmentUpdate` (class) — [saleor/graphql/product/mutations/attributes.py:361]
- `Arguments` (class) — [saleor/graphql/product/mutations/attributes.py:364]
- `Meta` (class) — [saleor/graphql/product/mutations/attributes.py:375]
- `get_operations` (function) — [saleor/graphql/product/mutations/attributes.py:385]
- `check_attribute_assignment_exsistence` (function) — [saleor/graphql/product/mutations/attributes.py:398]
- `check_attribute_assignment_to_product_variant` (function) — [saleor/graphql/product/mutations/attributes.py:429]
- `check_for_duplicates` (function) — [saleor/graphql/product/mutations/attributes.py:453]
- `clean_operations` (function) — [saleor/graphql/product/mutations/attributes.py:469]
- `update_field_values` (function) — [saleor/graphql/product/mutations/attributes.py:504]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/attributes.py:524]
- `ProductTypeReorderAttributes` (class) — [saleor/graphql/product/mutations/attributes.py:553]
- `Meta` (class) — [saleor/graphql/product/mutations/attributes.py:558]
- `Arguments` (class) — [saleor/graphql/product/mutations/attributes.py:565]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/attributes.py:579]
- `ProductReorderAttributeValues` (class) — [saleor/graphql/product/mutations/attributes.py:619]
- `Meta` (class) — [saleor/graphql/product/mutations/attributes.py:624]
- `Arguments` (class) — [saleor/graphql/product/mutations/attributes.py:631]
- `perform` (function) — [saleor/graphql/product/mutations/attributes.py:645]
- _…and 8 more in this file_

**`saleor/graphql/product/mutations/channels.py`**

- `PublishableChannelListingInput` (class) — [saleor/graphql/product/mutations/channels.py:52]
- `Meta` (class) — [saleor/graphql/product/mutations/channels.py:65]
- `ProductChannelListingAddInput` (class) — [saleor/graphql/product/mutations/channels.py:69]
- `Meta` (class) — [saleor/graphql/product/mutations/channels.py:109]
- `ProductChannelListingUpdateInput` (class) — [saleor/graphql/product/mutations/channels.py:113]
- `Meta` (class) — [saleor/graphql/product/mutations/channels.py:127]
- `ProductChannelListingUpdate` (class) — [saleor/graphql/product/mutations/channels.py:131]
- `Arguments` (class) — [saleor/graphql/product/mutations/channels.py:134]
- `Meta` (class) — [saleor/graphql/product/mutations/channels.py:141]
- `clean_available_for_purchase` (function) — [saleor/graphql/product/mutations/channels.py:149]
- `clean_available_fo_purchase_date` (function) — [saleor/graphql/product/mutations/channels.py:191]
- `validate_product_without_category` (function) — [saleor/graphql/product/mutations/channels.py:206]
- `update_channels` (function) — [saleor/graphql/product/mutations/channels.py:229]
- `get_available_for_purchase_date` (function) — [saleor/graphql/product/mutations/channels.py:254]
- `validate_variants` (function) — [saleor/graphql/product/mutations/channels.py:268]
- `add_variants` (function) — [saleor/graphql/product/mutations/channels.py:278]
- `remove_variants` (function) — [saleor/graphql/product/mutations/channels.py:304]
- `remove_channels` (function) — [saleor/graphql/product/mutations/channels.py:323]
- `save` (function) — [saleor/graphql/product/mutations/channels.py:332]
- `post_save_actions` (function) — [saleor/graphql/product/mutations/channels.py:338]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/channels.py:355]
- `ProductVariantChannelListingAddInput` (class) — [saleor/graphql/product/mutations/channels.py:385]
- `Meta` (class) — [saleor/graphql/product/mutations/channels.py:400]
- `ProductVariantChannelListingUpdate` (class) — [saleor/graphql/product/mutations/channels.py:404]
- `Arguments` (class) — [saleor/graphql/product/mutations/channels.py:409]
- `Meta` (class) — [saleor/graphql/product/mutations/channels.py:425]
- `clean_channels` (function) — [saleor/graphql/product/mutations/channels.py:433]
- `validate_product_assigned_to_channel` (function) — [saleor/graphql/product/mutations/channels.py:460]
- `clean_price` (function) — [saleor/graphql/product/mutations/channels.py:491]
- `clean_prices` (function) — [saleor/graphql/product/mutations/channels.py:502]
- `save` (function) — [saleor/graphql/product/mutations/channels.py:519]
- `post_save_actions` (function) — [saleor/graphql/product/mutations/channels.py:550]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/channels.py:564]
- `CollectionChannelListingUpdateInput` (class) — [saleor/graphql/product/mutations/channels.py:601]
- `Meta` (class) — [saleor/graphql/product/mutations/channels.py:613]
- `CollectionChannelListingUpdate` (class) — [saleor/graphql/product/mutations/channels.py:617]
- `Arguments` (class) — [saleor/graphql/product/mutations/channels.py:622]
- `Meta` (class) — [saleor/graphql/product/mutations/channels.py:631]
- `add_channels` (function) — [saleor/graphql/product/mutations/channels.py:639]
- `remove_channels` (function) — [saleor/graphql/product/mutations/channels.py:650]
- _…and 2 more in this file_

**`saleor/graphql/product/mutations/utils.py`**

- `clean_tax_code` (function) — [saleor/graphql/product/mutations/utils.py:20]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/mutations/__init__.py` (59 lines)
- `saleor/graphql/product/mutations/attributes.py` (785 lines)
- `saleor/graphql/product/mutations/channels.py` (683 lines)
- `saleor/graphql/product/mutations/utils.py` (34 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....attribute.AttributeInputType`
- `....attribute.AttributeType`
- `....attribute.models`
- `....channel.models.Channel`
- `....core.tracing.traced_atomic_transaction`
- `....core.utils.date_time.convert_to_utc_date_time`
- `....permission.enums.ProductPermissions`
- `....permission.enums.ProductTypePermissions`
- `....product.error_codes.CollectionErrorCode`
- `....product.error_codes.ProductErrorCode`
- `....product.models`
- `....product.models.Collection`
- `....product.models.Product`
- `....product.models.ProductVariant`
- `....product.utils.product.mark_products_in_channels_as_dirty`
- `....tax.models.TaxClass`
- `...attribute.types.Attribute`
- `...channel.mutations.BaseChannelListingMutation`
- `...channel.types.Channel`
- `...core.ResolveInfo`
- `...core.context.ChannelContext`
- `...core.descriptions.DEPRECATED_IN_3X_INPUT`
- `...core.doc_category.DOC_CATEGORY_PRODUCTS`
- `...core.inputs.ReorderInput`
- `...core.mutations.BaseMutation`
- `...core.scalars.Date`
- `...core.scalars.DateTime`
- `...core.scalars.PositiveDecimal`
- `...core.types.BaseInputObjectType`
- `...core.types.NonNullList`
- `...core.types.ProductError`
- `...core.utils.get_duplicated_values`
- `...core.utils.reordering.perform_reordering`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...product.types.Product`
- `...product.types.ProductType`
- `...product.types.ProductVariant`
- `...utils.validators.check_for_duplicates`
- `..enums.ProductAttributeType`
- `..types.collections.Collection`
- `..types.products.Product`
- `..types.products.ProductVariant`
- `.category.CategoryCreate`
- `.category.CategoryDelete`
- `.category.CategoryUpdate`
- `.product_type.ProductTypeCreate`
- `.product_type.ProductTypeDelete`
- `.product_type.ProductTypeUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `652d5243784b` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
