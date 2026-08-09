## Purpose

`saleor/graphql/giftcard` (`saleor/graphql/giftcard`) groups 8 source file(s) exposing 100 top-level declaration(s).

## Public surface

**`saleor/graphql/giftcard/dataloaders.py`**

- `GiftCardsByUserLoader` (class) — [saleor/graphql/giftcard/dataloaders.py:12]
- `batch_load` (function) — [saleor/graphql/giftcard/dataloaders.py:15]
- `GiftCardEventsByGiftCardIdLoader` (class) — [saleor/graphql/giftcard/dataloaders.py:30]
- `batch_load` (function) — [saleor/graphql/giftcard/dataloaders.py:33]
- `GiftCardTagsByGiftCardIdLoader` (class) — [saleor/graphql/giftcard/dataloaders.py:43]
- `batch_load` (function) — [saleor/graphql/giftcard/dataloaders.py:46]
- `GiftCardsByOrderIdLoader` (class) — [saleor/graphql/giftcard/dataloaders.py:67]
- `batch_load` (function) — [saleor/graphql/giftcard/dataloaders.py:70]
- `GiftCardsByCheckoutIdLoader` (class) — [saleor/graphql/giftcard/dataloaders.py:87]
- `batch_load` (function) — [saleor/graphql/giftcard/dataloaders.py:90]

**`saleor/graphql/giftcard/filters.py`**

- `filter_products` (function) — [saleor/graphql/giftcard/filters.py:30]
- `filter_gift_cards_by_products` (function) — [saleor/graphql/giftcard/filters.py:37]
- `filter_used_by` (function) — [saleor/graphql/giftcard/filters.py:42]
- `filter_gift_cards_by_used_by_user` (function) — [saleor/graphql/giftcard/filters.py:49]
- `filter_assigned_to` (function) — [saleor/graphql/giftcard/filters.py:60]
- `filter_tags_list` (function) — [saleor/graphql/giftcard/filters.py:68]
- `filter_gift_card_used` (function) — [saleor/graphql/giftcard/filters.py:75]
- `filter_currency` (function) — [saleor/graphql/giftcard/filters.py:81]
- `filter_code` (function) — [saleor/graphql/giftcard/filters.py:96]
- `filter_created_by_email` (function) — [saleor/graphql/giftcard/filters.py:102]
- `GiftCardFilter` (class) — [saleor/graphql/giftcard/filters.py:108]
- `Meta` (class) — [saleor/graphql/giftcard/filters.py:136]
- `filter_current_balance` (function) — [saleor/graphql/giftcard/filters.py:140]
- `filter_initial_balance` (function) — [saleor/graphql/giftcard/filters.py:144]
- `check_currency_in_filter_data` (function) — [saleor/graphql/giftcard/filters.py:149]
- `GiftCardFilterInput` (class) — [saleor/graphql/giftcard/filters.py:157]
- `Meta` (class) — [saleor/graphql/giftcard/filters.py:158]
- `filter_events_by_type` (function) — [saleor/graphql/giftcard/filters.py:163]
- `filter_events_by_orders` (function) — [saleor/graphql/giftcard/filters.py:171]
- `GiftCardEventFilterInput` (class) — [saleor/graphql/giftcard/filters.py:205]
- `Meta` (class) — [saleor/graphql/giftcard/filters.py:209]
- `filter_gift_card_tag_search` (function) — [saleor/graphql/giftcard/filters.py:213]
- `GiftCardTagFilter` (class) — [saleor/graphql/giftcard/filters.py:219]
- `GiftCardTagFilterInput` (class) — [saleor/graphql/giftcard/filters.py:223]
- `Meta` (class) — [saleor/graphql/giftcard/filters.py:224]

**`saleor/graphql/giftcard/resolvers.py`**

- `resolve_gift_card` (function) — [saleor/graphql/giftcard/resolvers.py:5]
- `resolve_gift_cards` (function) — [saleor/graphql/giftcard/resolvers.py:13]
- `resolve_gift_card_tags` (function) — [saleor/graphql/giftcard/resolvers.py:19]

**`saleor/graphql/giftcard/schema.py`**

- `GiftCardQueries` (class) — [saleor/graphql/giftcard/schema.py:41]
- `resolve_gift_card` (function) — [saleor/graphql/giftcard/schema.py:89]
- `resolve_gift_cards` (function) — [saleor/graphql/giftcard/schema.py:94]
- `resolve_gift_card_currencies` (function) — [saleor/graphql/giftcard/schema.py:124]
- `resolve_gift_card_tags` (function) — [saleor/graphql/giftcard/schema.py:132]
- `GiftCardMutations` (class) — [saleor/graphql/giftcard/schema.py:140]

**`saleor/graphql/giftcard/sorters.py`**

- `GiftCardSortField` (class) — [saleor/graphql/giftcard/sorters.py:5]
- `Meta` (class) — [saleor/graphql/giftcard/sorters.py:12]
- `description` (function) — [saleor/graphql/giftcard/sorters.py:16]
- `GiftCardSortingInput` (class) — [saleor/graphql/giftcard/sorters.py:30]
- `Meta` (class) — [saleor/graphql/giftcard/sorters.py:31]

**`saleor/graphql/giftcard/types.py`**

- `GiftCardEventBalance` (class) — [saleor/graphql/giftcard/types.py:49]
- `Meta` (class) — [saleor/graphql/giftcard/types.py:68]
- `GiftCardEventAssignment` (class) — [saleor/graphql/giftcard/types.py:72]
- `Meta` (class) — [saleor/graphql/giftcard/types.py:104]
- `resolve_old_assigned_to` (function) — [saleor/graphql/giftcard/types.py:108]
- `resolve_current_assigned_to` (function) — [saleor/graphql/giftcard/types.py:112]
- `resolve_old_assigned_to_email` (function) — [saleor/graphql/giftcard/types.py:116]
- `resolve_current_assigned_to_email` (function) — [saleor/graphql/giftcard/types.py:120]
- `GiftCardEvent` (class) — [saleor/graphql/giftcard/types.py:145]
- `Meta` (class) — [saleor/graphql/giftcard/types.py:197]
- `resolve_user` (function) — [saleor/graphql/giftcard/types.py:203]
- `resolve_app` (function) — [saleor/graphql/giftcard/types.py:220]
- `resolve_message` (function) — [saleor/graphql/giftcard/types.py:234]
- `resolve_email` (function) — [saleor/graphql/giftcard/types.py:238]
- `resolve_order_id` (function) — [saleor/graphql/giftcard/types.py:242]
- `resolve_order_number` (function) — [saleor/graphql/giftcard/types.py:247]
- `resolve_tags` (function) — [saleor/graphql/giftcard/types.py:261]
- `resolve_old_tags` (function) — [saleor/graphql/giftcard/types.py:265]
- `resolve_balance` (function) — [saleor/graphql/giftcard/types.py:270]
- `resolve_assigned_to` (function) — [saleor/graphql/giftcard/types.py:289]
- `resolve_expiry_date` (function) — [saleor/graphql/giftcard/types.py:298]
- `resolve_old_expiry_date` (function) — [saleor/graphql/giftcard/types.py:309]
- `GiftCardTag` (class) — [saleor/graphql/giftcard/types.py:320]
- `Meta` (class) — [saleor/graphql/giftcard/types.py:328]
- `GiftCard` (class) — [saleor/graphql/giftcard/types.py:334]
- `Meta` (class) — [saleor/graphql/giftcard/types.py:463]
- `resolve_created` (function) — [saleor/graphql/giftcard/types.py:472]
- `resolve_last_4_code_chars` (function) — [saleor/graphql/giftcard/types.py:476]
- `resolve_code` (function) — [saleor/graphql/giftcard/types.py:480]
- `resolve_created_by` (function) — [saleor/graphql/giftcard/types.py:502]
- `resolve_used_by` (function) — [saleor/graphql/giftcard/types.py:516]
- `resolve_created_by_email` (function) — [saleor/graphql/giftcard/types.py:535]
- `resolve_used_by_email` (function) — [saleor/graphql/giftcard/types.py:554]
- `resolve_assigned_to` (function) — [saleor/graphql/giftcard/types.py:573]
- `resolve_assigned_to_email` (function) — [saleor/graphql/giftcard/types.py:590]
- `resolve_app` (function) — [saleor/graphql/giftcard/types.py:613]
- `resolve_product` (function) — [saleor/graphql/giftcard/types.py:627]
- `resolve_events` (function) — [saleor/graphql/giftcard/types.py:636]
- `filter_events` (function) — [saleor/graphql/giftcard/types.py:637]
- `resolve_tags` (function) — [saleor/graphql/giftcard/types.py:670]
- _…and 11 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/graphql/giftcard/__init__.py` (1 lines)
- `saleor/graphql/giftcard/dataloaders.py` (105 lines)
- `saleor/graphql/giftcard/enums.py` (10 lines)
- `saleor/graphql/giftcard/filters.py` (226 lines)
- `saleor/graphql/giftcard/resolvers.py` (22 lines)
- `saleor/graphql/giftcard/schema.py` (155 lines)
- `saleor/graphql/giftcard/sorters.py` (34 lines)
- `saleor/graphql/giftcard/types.py` (749 lines)

## Interactions

- Imports from: `saleor/graphql`, `saleor/graphql/product/types`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...account.models`
- `...checkout.models.Checkout`
- `...core.anonymize.obfuscate_email`
- `...core.exceptions.PermissionDenied`
- `...core.search.prefix_search`
- `...giftcard.GiftCardEvents`
- `...giftcard.models`
- `...giftcard.models.GiftCard`
- `...giftcard.models.GiftCardEvent`
- `...giftcard.models.GiftCardTag`
- `...order.models`
- `...order.models.Order`
- `...permission.auth_filters.AuthorizationFilters`
- `...permission.enums.GiftcardPermissions`
- `...product.models`
- `..account.dataloaders.UserByUserIdLoader`
- `..app.dataloaders.AppByIdLoader`
- `..app.types.App`
- `..channel.dataloaders.by_self.ChannelByIdLoader`
- `..core.ResolveInfo`
- `..core.connection.CountableConnection`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.context.ChannelContext`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.descriptions.ADDED_IN_323`
- `..core.descriptions.DEFAULT_DEPRECATION_REASON`
- `..core.descriptions.DEPRECATED_IN_3X_INPUT`
- `..core.doc_category.DOC_CATEGORY_GIFT_CARDS`
- `..core.enums.to_enum`
- `..core.fields.FilterConnectionField`
- `..core.fields.PermissionsField`
- `..core.scalars.Date`
- `..core.scalars.DateTime`
- `..core.tracing.traced_resolver`
- `..core.types.BaseEnum`
- `..core.types.BaseObjectType`
- `..core.types.ModelObjectType`
- `..core.types.Money`
- `..core.types.NonNullList`
- `..core.types.SortInputObjectType`
- `..meta.types.ObjectWithMetadata`
- `..order.dataloaders.OrderByIdLoader`
- `..product.dataloaders.products.ProductByIdLoader`
- `..utils.get_user_or_app_from_context`
- `..utils.resolve_global_ids_to_primary_keys`
- `.enums.GiftCardEventsEnum`
- `.filters.GiftCardFilterInput`
- `.filters.GiftCardTagFilterInput`
- `.resolvers.resolve_gift_card`
- `.resolvers.resolve_gift_card_tags`
- `.resolvers.resolve_gift_cards`
- `.sorters.GiftCardSortField`
- `.sorters.GiftCardSortingInput`
- `.types.GiftCard`
- `.types.GiftCardCountableConnection`
- `.types.GiftCardTagCountableConnection`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `9e0ff6ef02c8` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
