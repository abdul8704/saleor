## Purpose

`saleor/graphql/meta/mutations` (`saleor/graphql/meta/mutations`) groups 7 source file(s) exposing 36 top-level declaration(s).

## Public surface

**`saleor/graphql/meta/mutations/base.py`**

- `MetadataPermissionOptions` (class) — [saleor/graphql/meta/mutations/base.py:27]
- `BaseMetadataMutation` (class) — [saleor/graphql/meta/mutations/base.py:31]
- `Meta` (class) — [saleor/graphql/meta/mutations/base.py:32]
- `get_instance` (function) — [saleor/graphql/meta/mutations/base.py:57]
- `get_instance_by_token` (function) — [saleor/graphql/meta/mutations/base.py:80]
- `get_old_sale_instance` (function) — [saleor/graphql/meta/mutations/base.py:94]
- `validate_model_is_model_with_metadata` (function) — [saleor/graphql/meta/mutations/base.py:108]
- `get_permissions` (function) — [saleor/graphql/meta/mutations/base.py:123]
- `get_model_for_type_name` (function) — [saleor/graphql/meta/mutations/base.py:139]
- `mutate` (function) — [saleor/graphql/meta/mutations/base.py:156]
- `get_object_type_name_and_pk` (function) — [saleor/graphql/meta/mutations/base.py:214]
- `perform_model_extra_actions` (function) — [saleor/graphql/meta/mutations/base.py:236]
- `success_response` (function) — [saleor/graphql/meta/mutations/base.py:243]

**`saleor/graphql/meta/mutations/delete_metadata.py`**

- `DeleteMetadata` (class) — [saleor/graphql/meta/mutations/delete_metadata.py:13]
- `Meta` (class) — [saleor/graphql/meta/mutations/delete_metadata.py:14]
- `Arguments` (class) — [saleor/graphql/meta/mutations/delete_metadata.py:23]
- `perform_mutation` (function) — [saleor/graphql/meta/mutations/delete_metadata.py:35]

**`saleor/graphql/meta/mutations/delete_private_metadata.py`**

- `DeletePrivateMetadata` (class) — [saleor/graphql/meta/mutations/delete_private_metadata.py:10]
- `Meta` (class) — [saleor/graphql/meta/mutations/delete_private_metadata.py:11]
- `Arguments` (class) — [saleor/graphql/meta/mutations/delete_private_metadata.py:20]
- `perform_mutation` (function) — [saleor/graphql/meta/mutations/delete_private_metadata.py:32]

**`saleor/graphql/meta/mutations/update_metadata.py`**

- `UpdateMetadata` (class) — [saleor/graphql/meta/mutations/update_metadata.py:14]
- `Meta` (class) — [saleor/graphql/meta/mutations/update_metadata.py:15]
- `Arguments` (class) — [saleor/graphql/meta/mutations/update_metadata.py:24]
- `perform_mutation` (function) — [saleor/graphql/meta/mutations/update_metadata.py:36]

**`saleor/graphql/meta/mutations/update_private_metadata.py`**

- `UpdatePrivateMetadata` (class) — [saleor/graphql/meta/mutations/update_private_metadata.py:11]
- `Meta` (class) — [saleor/graphql/meta/mutations/update_private_metadata.py:12]
- `Arguments` (class) — [saleor/graphql/meta/mutations/update_private_metadata.py:21]
- `perform_mutation` (function) — [saleor/graphql/meta/mutations/update_private_metadata.py:33]

**`saleor/graphql/meta/mutations/utils.py`**

- `get_valid_metadata_instance` (function) — [saleor/graphql/meta/mutations/utils.py:16]
- `get_updated_field_name` (function) — [saleor/graphql/meta/mutations/utils.py:60]
- `get_extra_update_field` (function) — [saleor/graphql/meta/mutations/utils.py:74]
- `update_metadata` (function) — [saleor/graphql/meta/mutations/utils.py:81]
- `update_private_metadata` (function) — [saleor/graphql/meta/mutations/utils.py:98]
- `delete_metadata_keys` (function) — [saleor/graphql/meta/mutations/utils.py:120]
- `delete_private_metadata_keys` (function) — [saleor/graphql/meta/mutations/utils.py:148]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/meta/mutations/__init__.py` (11 lines)
- `saleor/graphql/meta/mutations/base.py` (282 lines)
- `saleor/graphql/meta/mutations/delete_metadata.py` (42 lines)
- `saleor/graphql/meta/mutations/delete_private_metadata.py` (40 lines)
- `saleor/graphql/meta/mutations/update_metadata.py` (46 lines)
- `saleor/graphql/meta/mutations/update_private_metadata.py` (47 lines)
- `saleor/graphql/meta/mutations/utils.py` (179 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....attribute.models`
- `....checkout.models`
- `....checkout.models.Checkout`
- `....checkout.models.CheckoutMetadata`
- `....checkout.utils.get_or_create_checkout_metadata`
- `....core.db.connection.allow_writer`
- `....core.db.expressions.PostgresJsonConcatenate`
- `....core.error_codes.MetadataErrorCode`
- `....core.exceptions.PermissionDenied`
- `....core.models`
- `....core.models.ModelWithMetadata`
- `....discount.models`
- `....discount.models.Promotion`
- `....menu.models`
- `....order.models`
- `....page.models`
- `....product.models`
- `....shipping.models`
- `...core.ResolveInfo`
- `...core.context.BaseContext`
- `...core.context.ChannelContext`
- `...core.context.SyncWebhookControlContext`
- `...core.mutations.BaseMutation`
- `...core.types.MetadataError`
- `...core.types.NonNullList`
- `...core.utils.from_global_id_or_error`
- `..extra_methods.TYPE_EXTRA_METHODS`
- `..inputs.MetadataInput`
- `..inputs.MetadataInputDescription`
- `..permissions.PRIVATE_META_PERMISSION_MAP`
- `..permissions.PUBLIC_META_PERMISSION_MAP`
- `..types.ObjectWithMetadata`
- `.base.BaseMetadataMutation`
- `.delete_metadata.DeleteMetadata`
- `.delete_private_metadata.DeletePrivateMetadata`
- `.update_metadata.UpdateMetadata`
- `.update_private_metadata.UpdatePrivateMetadata`
- `.utils.delete_metadata_keys`
- `.utils.delete_private_metadata_keys`
- `.utils.get_valid_metadata_instance`
- `.utils.update_metadata`
- `.utils.update_private_metadata`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `27910c650761` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
