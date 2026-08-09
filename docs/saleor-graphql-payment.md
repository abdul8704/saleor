## Purpose

`saleor/graphql/payment` (`saleor/graphql/payment`) groups 9 source file(s) exposing 138 top-level declaration(s).

## Public surface

**`saleor/graphql/payment/dataloaders.py`**

- `TransactionEventByTransactionIdLoader` (class) — [saleor/graphql/payment/dataloaders.py:7]
- `batch_load` (function) — [saleor/graphql/payment/dataloaders.py:10]
- `TransactionItemByIDLoader` (class) — [saleor/graphql/payment/dataloaders.py:22]
- `batch_load` (function) — [saleor/graphql/payment/dataloaders.py:25]
- `TransactionByPaymentIdLoader` (class) — [saleor/graphql/payment/dataloaders.py:32]
- `batch_load` (function) — [saleor/graphql/payment/dataloaders.py:35]
- `PaymentsByCheckoutTokenLoader` (class) — [saleor/graphql/payment/dataloaders.py:47]
- `batch_load` (function) — [saleor/graphql/payment/dataloaders.py:50]

**`saleor/graphql/payment/enums.py`**

- `OrderAction` (class) — [saleor/graphql/payment/enums.py:56]
- `Meta` (class) — [saleor/graphql/payment/enums.py:62]
- `description` (function) — [saleor/graphql/payment/enums.py:66]
- `deprecation_reason` (function) — [saleor/graphql/payment/enums.py:78]
- `description` (function) — [saleor/graphql/payment/enums.py:84]

**`saleor/graphql/payment/filters.py`**

- `PaymentFilter` (class) — [saleor/graphql/payment/filters.py:33]
- `Meta` (class) — [saleor/graphql/payment/filters.py:37]
- `PaymentFilterInput` (class) — [saleor/graphql/payment/filters.py:42]
- `Meta` (class) — [saleor/graphql/payment/filters.py:43]
- `TransactionEventTypeEnumFilterInput` (class) — [saleor/graphql/payment/filters.py:52]
- `Meta` (class) — [saleor/graphql/payment/filters.py:62]
- `TransactionEventFilterInput` (class) — [saleor/graphql/payment/filters.py:66]
- `Meta` (class) — [saleor/graphql/payment/filters.py:74]
- `filter_transaction_by_ids` (function) — [saleor/graphql/payment/filters.py:79]
- `filter_where_created_at_range` (function) — [saleor/graphql/payment/filters.py:85]
- `filter_where_modified_at_range` (function) — [saleor/graphql/payment/filters.py:89]
- `filter_where_transaction_events` (function) — [saleor/graphql/payment/filters.py:93]
- `TransactionWhere` (class) — [saleor/graphql/payment/filters.py:120]
- `filter_psp_reference` (function) — [saleor/graphql/payment/filters.py:155]
- `filter_app_identifier` (function) — [saleor/graphql/payment/filters.py:159]
- `Meta` (class) — [saleor/graphql/payment/filters.py:162]
- `TransactionWhereInput` (class) — [saleor/graphql/payment/filters.py:166]
- `Meta` (class) — [saleor/graphql/payment/filters.py:167]

**`saleor/graphql/payment/resolvers.py`**

- `resolve_payment_by_id` (function) — [saleor/graphql/payment/resolvers.py:13]
- `resolve_payments` (function) — [saleor/graphql/payment/resolvers.py:21]
- `resolve_transaction` (function) — [saleor/graphql/payment/resolvers.py:35]
- `resolve_transactions` (function) — [saleor/graphql/payment/resolvers.py:47]

**`saleor/graphql/payment/schema.py`**

- `PaymentQueries` (class) — [saleor/graphql/payment/schema.py:59]
- `resolve_payment` (function) — [saleor/graphql/payment/schema.py:131]
- `resolve_payments` (function) — [saleor/graphql/payment/schema.py:136]
- `resolve_transaction` (function) — [saleor/graphql/payment/schema.py:144]
- `resolve_transactions` (function) — [saleor/graphql/payment/schema.py:158]
- `PaymentMutations` (class) — [saleor/graphql/payment/schema.py:166]

**`saleor/graphql/payment/sorters.py`**

- `TransactionSortField` (class) — [saleor/graphql/payment/sorters.py:6]
- `Meta` (class) — [saleor/graphql/payment/sorters.py:10]
- `description` (function) — [saleor/graphql/payment/sorters.py:14]
- `TransactionSortingInput` (class) — [saleor/graphql/payment/sorters.py:24]
- `Meta` (class) — [saleor/graphql/payment/sorters.py:25]

**`saleor/graphql/payment/types.py`**

- `Transaction` (class) — [saleor/graphql/payment/types.py:53]
- `Meta` (class) — [saleor/graphql/payment/types.py:80]
- `resolve_created` (function) — [saleor/graphql/payment/types.py:89]
- `resolve_amount` (function) — [saleor/graphql/payment/types.py:93]
- `CreditCard` (class) — [saleor/graphql/payment/types.py:97]
- `Meta` (class) — [saleor/graphql/payment/types.py:114]
- `PaymentSource` (class) — [saleor/graphql/payment/types.py:118]
- `Meta` (class) — [saleor/graphql/payment/types.py:119]
- `Payment` (class) — [saleor/graphql/payment/types.py:142]
- `Meta` (class) — [saleor/graphql/payment/types.py:216]
- `resolve_created` (function) — [saleor/graphql/payment/types.py:225]
- `resolve_modified` (function) — [saleor/graphql/payment/types.py:229]
- `resolve_customer_ip_address` (function) — [saleor/graphql/payment/types.py:233]
- `resolve_actions` (function) — [saleor/graphql/payment/types.py:237]
- `resolve_total` (function) — [saleor/graphql/payment/types.py:249]
- `resolve_captured_amount` (function) — [saleor/graphql/payment/types.py:253]
- `resolve_transactions` (function) — [saleor/graphql/payment/types.py:257]
- `resolve_available_refund_amount` (function) — [saleor/graphql/payment/types.py:261]
- `resolve_available_capture_amount` (function) — [saleor/graphql/payment/types.py:267]
- `resolve_credit_card` (function) — [saleor/graphql/payment/types.py:273]
- `resolve_metadata` (function) — [saleor/graphql/payment/types.py:286]
- `resolve_order` (function) — [saleor/graphql/payment/types.py:294]
- `resolve_checkout` (function) — [saleor/graphql/payment/types.py:310]
- `PaymentCountableConnection` (class) — [saleor/graphql/payment/types.py:326]
- `Meta` (class) — [saleor/graphql/payment/types.py:327]
- `PaymentInitialized` (class) — [saleor/graphql/payment/types.py:332]
- `Meta` (class) — [saleor/graphql/payment/types.py:333]
- `TransactionEvent` (class) — [saleor/graphql/payment/types.py:346]
- `Meta` (class) — [saleor/graphql/payment/types.py:390]
- `resolve_psp_reference` (function) — [saleor/graphql/payment/types.py:396]
- `resolve_external_url` (function) — [saleor/graphql/payment/types.py:400]
- `resolve_message` (function) — [saleor/graphql/payment/types.py:404]
- `resolve_created_by` (function) — [saleor/graphql/payment/types.py:408]
- `get_first_app_by_identifier` (function) — [saleor/graphql/payment/types.py:418]
- `get_active_app` (function) — [saleor/graphql/payment/types.py:423]
- `resolve_reason_reference` (function) — [saleor/graphql/payment/types.py:450]
- `wrap_page_with_context` (function) — [saleor/graphql/payment/types.py:454]
- `PaymentMethodDetails` (class) — [saleor/graphql/payment/types.py:475]
- `Meta` (class) — [saleor/graphql/payment/types.py:478]
- `resolve_type` (function) — [saleor/graphql/payment/types.py:484]
- _…and 49 more in this file_

**`saleor/graphql/payment/utils.py`**

- `deprecated_metadata_contains_empty_key` (function) — [saleor/graphql/payment/utils.py:13]
- `check_if_requestor_has_access` (function) — [saleor/graphql/payment/utils.py:22]
- `validate_reason_reference_context` (function) — [saleor/graphql/payment/utils.py:49]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/payment/__init__.py` (1 lines)
- `saleor/graphql/payment/dataloaders.py` (57 lines)
- `saleor/graphql/payment/enums.py` (135 lines)
- `saleor/graphql/payment/filters.py` (169 lines)
- `saleor/graphql/payment/resolvers.py` (73 lines)
- `saleor/graphql/payment/schema.py` (196 lines)
- `saleor/graphql/payment/sorters.py` (28 lines)
- `saleor/graphql/payment/types.py` (940 lines)
- `saleor/graphql/payment/utils.py` (94 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...account.models.User`
- `...app.models`
- `...app.models.App`
- `...checkout.models`
- `...core.exceptions.PermissionDenied`
- `...order.models`
- `...page.models.PageType`
- `...payment.PaymentMethodType`
- `...payment.interface.PaymentMethodData`
- `...payment.models`
- `...payment.models.Payment`
- `...payment.models.Transaction`
- `...payment.models.TransactionEvent`
- `...payment.models.TransactionItem`
- `...permission.enums.OrderPermissions`
- `...permission.enums.PaymentPermissions`
- `..account.dataloaders.UserByUserIdLoader`
- `..account.utils.get_user_accessible_channels`
- `..app.dataloaders.ActiveAppsByAppIdentifierLoader`
- `..app.dataloaders.AppByIdLoader`
- `..channel.dataloaders.by_transaction.ChannelByTransactionIdLoader`
- `..checkout.dataloaders.CheckoutByTokenLoader`
- `..core.ResolveInfo`
- `..core.connection.CountableConnection`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.context.ChannelContext`
- `..core.context.SyncWebhookControlContext`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.descriptions.ADDED_IN_323`
- `..core.descriptions.DEPRECATED_LEGACY_PAYMENTS`
- `..core.doc_category.DOC_CATEGORY_PAYMENTS`
- `..core.enums.to_enum`
- `..core.fields.FilterConnectionField`
- `..core.fields.JSONString`
- `..core.fields.PermissionsField`
- `..core.scalars.DateTime`
- `..core.scalars.JSON`
- `..core.scalars.UUID`
- `..core.tracing.traced_resolver`
- `..core.types.BaseEnum`
- `..core.types.BaseObjectType`
- `..core.types.ModelObjectType`
- `..core.types.Money`
- `..core.types.NonNullList`
- `..core.types.SortInputObjectType`
- `..core.types.base.BaseInputObjectType`
- `..core.types.common.DateTimeRangeInput`
- `..core.utils.from_global_id_or_error`
- `..meta.permissions.public_payment_permissions`
- `..meta.resolvers.resolve_metadata`
- `..meta.types.MetadataItem`
- `..meta.types.ObjectWithMetadata`
- `..order.dataloaders.OrderByIdLoader`
- `..page.dataloaders.PageByIdLoader`
- `..page.types.Page`
- `..utils.filters.filter_where_by_range_field`
- `..utils.filters.filter_where_by_value_field`
- `..utils.get_user_or_app_from_context`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `73898ac4c416` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
