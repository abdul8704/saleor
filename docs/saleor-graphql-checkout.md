## Purpose

`saleor/graphql/checkout` (`saleor/graphql/checkout`) groups 8 source file(s) exposing 133 top-level declaration(s).

## Public surface

**`saleor/graphql/checkout/filters.py`**

- `get_checkout_token_from_query` (function) — [saleor/graphql/checkout/filters.py:30]
- `get_payment_id_from_query` (function) — [saleor/graphql/checkout/filters.py:39]
- `get_checkout_id_from_query` (function) — [saleor/graphql/checkout/filters.py:46]
- `filter_checkout_by_payment` (function) — [saleor/graphql/checkout/filters.py:53]
- `filter_created_range` (function) — [saleor/graphql/checkout/filters.py:60]
- `filter_authorize_status` (function) — [saleor/graphql/checkout/filters.py:64]
- `filter_charge_status` (function) — [saleor/graphql/checkout/filters.py:70]
- `filter_updated_at_range` (function) — [saleor/graphql/checkout/filters.py:76]
- `filter_customer` (function) — [saleor/graphql/checkout/filters.py:80]
- `filter_channels` (function) — [saleor/graphql/checkout/filters.py:94]
- `filter_checkout_search` (function) — [saleor/graphql/checkout/filters.py:101]
- `filter_checkout_metadata` (function) — [saleor/graphql/checkout/filters.py:105]
- `CheckoutFilter` (class) — [saleor/graphql/checkout/filters.py:118]
- `Meta` (class) — [saleor/graphql/checkout/filters.py:136]
- `CheckoutFilterInput` (class) — [saleor/graphql/checkout/filters.py:141]
- `Meta` (class) — [saleor/graphql/checkout/filters.py:142]
- `CheckoutDiscountedObjectWhere` (class) — [saleor/graphql/checkout/filters.py:147]
- `Meta` (class) — [saleor/graphql/checkout/filters.py:148]
- `filter_base_subtotal_price` (function) — [saleor/graphql/checkout/filters.py:152]
- `filter_base_total_price` (function) — [saleor/graphql/checkout/filters.py:156]

**`saleor/graphql/checkout/resolvers.py`**

- `resolve_checkout_lines` (function) — [saleor/graphql/checkout/resolvers.py:19]
- `resolve_checkouts` (function) — [saleor/graphql/checkout/resolvers.py:26]
- `resolve_checkout` (function) — [saleor/graphql/checkout/resolvers.py:36]
- `with_checkout` (function) — [saleor/graphql/checkout/resolvers.py:43]

**`saleor/graphql/checkout/schema.py`**

- `CheckoutQueries` (class) — [saleor/graphql/checkout/schema.py:50]
- `resolve_checkout` (function) — [saleor/graphql/checkout/schema.py:102]
- `resolve_checkouts` (function) — [saleor/graphql/checkout/schema.py:106]
- `resolve_checkout_lines` (function) — [saleor/graphql/checkout/schema.py:119]
- `CheckoutMutations` (class) — [saleor/graphql/checkout/schema.py:126]

**`saleor/graphql/checkout/sorters.py`**

- `CheckoutSortField` (class) — [saleor/graphql/checkout/sorters.py:9]
- `Meta` (class) — [saleor/graphql/checkout/sorters.py:15]
- `description` (function) — [saleor/graphql/checkout/sorters.py:19]
- `deprecation_reason` (function) — [saleor/graphql/checkout/sorters.py:33]
- `qs_with_payment` (function) — [saleor/graphql/checkout/sorters.py:39]
- `CheckoutSortingInput` (class) — [saleor/graphql/checkout/sorters.py:50]
- `Meta` (class) — [saleor/graphql/checkout/sorters.py:51]

**`saleor/graphql/checkout/types.py`**

- `get_dataloaders_for_recalculate_discounts` (function) — [saleor/graphql/checkout/types.py:112]
- `CheckoutLineProblemInsufficientStock` (class) — [saleor/graphql/checkout/types.py:124]
- `Meta` (class) — [saleor/graphql/checkout/types.py:139]
- `resolve_line` (function) — [saleor/graphql/checkout/types.py:148]
- `CheckoutLineProblemVariantNotAvailable` (class) — [saleor/graphql/checkout/types.py:157]
- `Meta` (class) — [saleor/graphql/checkout/types.py:166]
- `resolve_line` (function) — [saleor/graphql/checkout/types.py:174]
- `CheckoutProblemDeliveryMethodStale` (class) — [saleor/graphql/checkout/types.py:201]
- `Meta` (class) — [saleor/graphql/checkout/types.py:206]
- `CheckoutProblemDeliveryMethodInvalid` (class) — [saleor/graphql/checkout/types.py:212]
- `Meta` (class) — [saleor/graphql/checkout/types.py:217]
- `CheckoutLineProblem` (class) — [saleor/graphql/checkout/types.py:225]
- `Meta` (class) — [saleor/graphql/checkout/types.py:226]
- `resolve_type` (function) — [saleor/graphql/checkout/types.py:235]
- `CheckoutProblem` (class) — [saleor/graphql/checkout/types.py:246]
- `Meta` (class) — [saleor/graphql/checkout/types.py:247]
- `resolve_type` (function) — [saleor/graphql/checkout/types.py:256]
- `CheckoutLine` (class) — [saleor/graphql/checkout/types.py:274]
- `Meta` (class) — [saleor/graphql/checkout/types.py:347]
- `resolve_variant` (function) — [saleor/graphql/checkout/types.py:356]
- `resolve_unit_price` (function) — [saleor/graphql/checkout/types.py:368]
- `resolve_undiscounted_unit_price` (function) — [saleor/graphql/checkout/types.py:393]
- `resolve_total_price` (function) — [saleor/graphql/checkout/types.py:419]
- `resolve_undiscounted_total_price` (function) — [saleor/graphql/checkout/types.py:443]
- `resolve_prior_total_price` (function) — [saleor/graphql/checkout/types.py:468]
- `resolve_requires_shipping` (function) — [saleor/graphql/checkout/types.py:482]
- `is_shipping_required` (function) — [saleor/graphql/checkout/types.py:485]
- `resolve_problems` (function) — [saleor/graphql/checkout/types.py:496]
- `get_problem_for_line` (function) — [saleor/graphql/checkout/types.py:503]
- `CheckoutLineCountableConnection` (class) — [saleor/graphql/checkout/types.py:515]
- `Meta` (class) — [saleor/graphql/checkout/types.py:516]
- `DeliveryMethod` (class) — [saleor/graphql/checkout/types.py:521]
- `Meta` (class) — [saleor/graphql/checkout/types.py:522]
- `resolve_type` (function) — [saleor/graphql/checkout/types.py:531]
- `Delivery` (class) — [saleor/graphql/checkout/types.py:540]
- `Meta` (class) — [saleor/graphql/checkout/types.py:547]
- `resolve_id` (function) — [saleor/graphql/checkout/types.py:551]
- `resolve_shipping_method` (function) — [saleor/graphql/checkout/types.py:554]
- `get_shipping_method` (function) — [saleor/graphql/checkout/types.py:569]
- `Checkout` (class) — [saleor/graphql/checkout/types.py:582]
- _…and 54 more in this file_

**`saleor/graphql/checkout/utils.py`**

- `prepare_insufficient_stock_checkout_validation_error` (function) — [saleor/graphql/checkout/utils.py:8]
- `prevent_sync_event_circular_query` (function) — [saleor/graphql/checkout/utils.py:21]
- `wrapper` (function) — [saleor/graphql/checkout/utils.py:32]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/checkout/__init__.py` (1 lines)
- `saleor/graphql/checkout/enums.py` (34 lines)
- `saleor/graphql/checkout/filters.py` (169 lines)
- `saleor/graphql/checkout/resolvers.py` (83 lines)
- `saleor/graphql/checkout/schema.py` (151 lines)
- `saleor/graphql/checkout/sorters.py` (54 lines)
- `saleor/graphql/checkout/types.py` (1513 lines)
- `saleor/graphql/checkout/utils.py` (46 lines)

## Interactions

- Imports from: `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...account.models.User`
- `...checkout.CheckoutAuthorizeStatus`
- `...checkout.CheckoutChargeStatus`
- `...checkout.calculations.recalculate_discounts`
- `...checkout.error_codes`
- `...checkout.fetch.CheckoutInfo`
- `...checkout.fetch.CheckoutLineInfo`
- `...checkout.models`
- `...checkout.models.Checkout`
- `...checkout.problems`
- `...core.db.connection.allow_writer_in_context`
- `...core.exceptions.CircularSubscriptionSyncEvent`
- `...core.exceptions.PermissionDenied`
- `...core.prices.quantize_price`
- `...core.search.prefix_search`
- `...core.taxes.zero_money`
- `...core.taxes.zero_taxed_money`
- `...payment.gateway.get_payment_gateways`
- `...payment.interface.ListStoredPaymentMethodsRequestData`
- `...payment.models.Payment`
- `...permission.auth_filters.AuthorizationFilters`
- `...plugins.manager.PluginsManager`
- `...shipping.interface.ShippingMethodData`
- `...shipping.utils.convert_checkout_delivery_to_shipping_method_data`
- `...tax.utils.get_display_gross_prices`
- `...warehouse.models`
- `...warehouse.reservations.is_reservation_enabled`
- `...webhook.event_types.WebhookEventSyncType`
- `..account.dataloaders.AddressByIdLoader`
- `..account.dataloaders.UserByUserIdLoader`
- `..account.utils.check_is_owner_or_has_one_of_perms`
- `..channel.dataloaders.by_checkout.ChannelByCheckoutIDLoader`
- `..channel.dataloaders.by_self.ChannelByIdLoader`
- `..channel.filters.get_currency_from_filter_data`
- `..channel.types.Channel`
- `..core.ResolveInfo`
- `..core.connection.CountableConnection`
- `..core.context.ChannelContext`
- `..core.context.SyncWebhookControlContext`
- `..core.context.get_database_connection_name`
- `..core.descriptions.DEPRECATED_IN_3X_INPUT`
- `..core.descriptions.DEPRECATED_LEGACY_PAYMENTS`
- `..core.doc_category.DOC_CATEGORY_CHECKOUT`
- `..core.doc_category.DOC_CATEGORY_ORDERS`
- `..core.enums.LanguageCodeEnum`
- `..core.enums.to_enum`
- `..core.fields.BaseField`
- `..core.fields.ConnectionField`
- `..core.fields.FilterConnectionField`
- `..core.fields.PermissionsField`
- `..core.scalars.DateTime`
- `..core.scalars.PositiveDecimal`
- `..core.scalars.UUID`
- `..core.tracing.traced_resolver`
- `..core.types.BaseEnum`
- `..core.types.DateRangeInput`
- `..core.types.Money`
- `..core.types.NonNullList`
- `..core.types.SortInputObjectType`
- `..core.types.TaxedMoney`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c43428e5cc05` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
