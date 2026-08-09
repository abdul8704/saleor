## Purpose

`saleor/graphql/webhook` (`saleor/graphql/webhook`) groups 13 source file(s) exposing 589 top-level declaration(s).

## Public surface

**`saleor/graphql/webhook/dataloaders/models.py`**

- `PayloadByIdLoader` (class) — [saleor/graphql/webhook/dataloaders/models.py:13]
- `batch_load` (function) — [saleor/graphql/webhook/dataloaders/models.py:16]
- `WebhookEventsByWebhookIdLoader` (class) — [saleor/graphql/webhook/dataloaders/models.py:27]
- `batch_load` (function) — [saleor/graphql/webhook/dataloaders/models.py:30]
- `WebhooksByAppIdLoader` (class) — [saleor/graphql/webhook/dataloaders/models.py:42]
- `batch_load` (function) — [saleor/graphql/webhook/dataloaders/models.py:45]
- `WebhookEventsByEventTypeLoader` (class) — [saleor/graphql/webhook/dataloaders/models.py:55]
- `batch_load` (function) — [saleor/graphql/webhook/dataloaders/models.py:58]
- `ActiveWebhooksByIdLoader` (class) — [saleor/graphql/webhook/dataloaders/models.py:68]
- `batch_load` (function) — [saleor/graphql/webhook/dataloaders/models.py:71]
- `WebhooksByEventTypeLoader` (class) — [saleor/graphql/webhook/dataloaders/models.py:80]
- `batch_load` (function) — [saleor/graphql/webhook/dataloaders/models.py:83]
- `fetch_webhooks` (function) — [saleor/graphql/webhook/dataloaders/models.py:88]
- `fetch_apps` (function) — [saleor/graphql/webhook/dataloaders/models.py:101]
- `return_webhooks_by_event_type` (function) — [saleor/graphql/webhook/dataloaders/models.py:110]

**`saleor/graphql/webhook/enums.py`**

- `description` (function) — [saleor/graphql/webhook/enums.py:276]
- `deprecation_reason` (function) — [saleor/graphql/webhook/enums.py:282]
- `EventDeliveryStatusEnum` (class) — [saleor/graphql/webhook/enums.py:340]
- `Meta` (class) — [saleor/graphql/webhook/enums.py:345]

**`saleor/graphql/webhook/filters.py`**

- `filter_status` (function) — [saleor/graphql/webhook/filters.py:7]
- `filter_event_type` (function) — [saleor/graphql/webhook/filters.py:13]
- `EventDeliveryFilter` (class) — [saleor/graphql/webhook/filters.py:19]
- `EventDeliveryFilterInput` (class) — [saleor/graphql/webhook/filters.py:24]
- `Meta` (class) — [saleor/graphql/webhook/filters.py:25]

**`saleor/graphql/webhook/mixins.py`**

- `NotifyUserEventValidationMixin` (class) — [saleor/graphql/webhook/mixins.py:7]
- `validate_events` (function) — [saleor/graphql/webhook/mixins.py:9]

**`saleor/graphql/webhook/resolvers.py`**

- `resolve_webhook` (function) — [saleor/graphql/webhook/resolvers.py:16]
- `resolve_webhook_events` (function) — [saleor/graphql/webhook/resolvers.py:36]
- `resolve_sample_payload` (function) — [saleor/graphql/webhook/resolvers.py:44]

**`saleor/graphql/webhook/schema.py`**

- `WebhookQueries` (class) — [saleor/graphql/webhook/schema.py:23]
- `resolve_webhook_sample_payload` (function) — [saleor/graphql/webhook/schema.py:58]
- `resolve_webhook` (function) — [saleor/graphql/webhook/schema.py:63]
- `resolve_webhook_events` (function) — [saleor/graphql/webhook/schema.py:67]
- `WebhookMutations` (class) — [saleor/graphql/webhook/schema.py:71]

**`saleor/graphql/webhook/sorters.py`**

- `EventDeliverySortField` (class) — [saleor/graphql/webhook/sorters.py:5]
- `Meta` (class) — [saleor/graphql/webhook/sorters.py:8]
- `description` (function) — [saleor/graphql/webhook/sorters.py:12]
- `EventDeliverySortingInput` (class) — [saleor/graphql/webhook/sorters.py:19]
- `Meta` (class) — [saleor/graphql/webhook/sorters.py:20]
- `EventDeliveryAttemptSortField` (class) — [saleor/graphql/webhook/sorters.py:26]
- `Meta` (class) — [saleor/graphql/webhook/sorters.py:29]
- `description` (function) — [saleor/graphql/webhook/sorters.py:33]
- `EventDeliveryAttemptSortingInput` (class) — [saleor/graphql/webhook/sorters.py:40]
- `Meta` (class) — [saleor/graphql/webhook/sorters.py:41]

**`saleor/graphql/webhook/subscription_payload.py`**

- `initialize_request` (function) — [saleor/graphql/webhook/subscription_payload.py:26]
- `get_event_payload` (function) — [saleor/graphql/webhook/subscription_payload.py:62]
- `process_single_payload` (function) — [saleor/graphql/webhook/subscription_payload.py:76]
- `generate_payload_promise_from_subscription` (function) — [saleor/graphql/webhook/subscription_payload.py:102]
- `return_payload_promise` (function) — [saleor/graphql/webhook/subscription_payload.py:141]
- `check_errors` (function) — [saleor/graphql/webhook/subscription_payload.py:171]
- `generate_payload_from_subscription` (function) — [saleor/graphql/webhook/subscription_payload.py:189]
- `get_pre_save_payload_key` (function) — [saleor/graphql/webhook/subscription_payload.py:259]
- `generate_pre_save_payloads` (function) — [saleor/graphql/webhook/subscription_payload.py:263]

**`saleor/graphql/webhook/subscription_query.py`**

- `IsFragment` (class) — [saleor/graphql/webhook/subscription_query.py:20]
- `SubscriptionQuery` (class) — [saleor/graphql/webhook/subscription_query.py:25]
- `get_filterable_channel_slugs` (function) — [saleor/graphql/webhook/subscription_query.py:35]
- `validate_query` (function) — [saleor/graphql/webhook/subscription_query.py:81]
- `get_events_from_subscription` (function) — [saleor/graphql/webhook/subscription_query.py:125]

**`saleor/graphql/webhook/subscription_types.py`**

- `IssuingPrincipal` (class) — [saleor/graphql/webhook/subscription_types.py:107]
- `Meta` (class) — [saleor/graphql/webhook/subscription_types.py:108]
- `resolve_type` (function) — [saleor/graphql/webhook/subscription_types.py:112]
- `Event` (class) — [saleor/graphql/webhook/subscription_types.py:118]
- `get_type` (function) — [saleor/graphql/webhook/subscription_types.py:131]
- `resolve_type` (function) — [saleor/graphql/webhook/subscription_types.py:135]
- `resolve_issued_at` (function) — [saleor/graphql/webhook/subscription_types.py:140]
- `resolve_version` (function) — [saleor/graphql/webhook/subscription_types.py:144]
- `resolve_recipient` (function) — [saleor/graphql/webhook/subscription_types.py:148]
- `resolve_issuing_principal` (function) — [saleor/graphql/webhook/subscription_types.py:152]
- `AccountOperationBase` (class) — [saleor/graphql/webhook/subscription_types.py:158]
- `resolve_user` (function) — [saleor/graphql/webhook/subscription_types.py:175]
- `resolve_redirect_url` (function) — [saleor/graphql/webhook/subscription_types.py:180]
- `resolve_channel` (function) — [saleor/graphql/webhook/subscription_types.py:185]
- `resolve_token` (function) — [saleor/graphql/webhook/subscription_types.py:197]
- `resolve_shop` (function) — [saleor/graphql/webhook/subscription_types.py:202]
- `AccountConfirmed` (class) — [saleor/graphql/webhook/subscription_types.py:206]
- `Meta` (class) — [saleor/graphql/webhook/subscription_types.py:207]
- `AccountConfirmationRequested` (class) — [saleor/graphql/webhook/subscription_types.py:215]
- `Meta` (class) — [saleor/graphql/webhook/subscription_types.py:216]
- `AccountChangeEmailRequested` (class) — [saleor/graphql/webhook/subscription_types.py:227]
- `Meta` (class) — [saleor/graphql/webhook/subscription_types.py:232]
- `resolve_new_email` (function) — [saleor/graphql/webhook/subscription_types.py:240]
- `AccountEmailChanged` (class) — [saleor/graphql/webhook/subscription_types.py:245]
- `Meta` (class) — [saleor/graphql/webhook/subscription_types.py:250]
- `AccountSetPasswordRequested` (class) — [saleor/graphql/webhook/subscription_types.py:258]
- `Meta` (class) — [saleor/graphql/webhook/subscription_types.py:259]
- `AccountDeleteRequested` (class) — [saleor/graphql/webhook/subscription_types.py:267]
- `Meta` (class) — [saleor/graphql/webhook/subscription_types.py:268]
- `AccountDeleted` (class) — [saleor/graphql/webhook/subscription_types.py:276]
- `Meta` (class) — [saleor/graphql/webhook/subscription_types.py:277]
- `AddressBase` (class) — [saleor/graphql/webhook/subscription_types.py:285]
- `resolve_address` (function) — [saleor/graphql/webhook/subscription_types.py:292]
- `AddressCreated` (class) — [saleor/graphql/webhook/subscription_types.py:297]
- `Meta` (class) — [saleor/graphql/webhook/subscription_types.py:298]
- `AddressUpdated` (class) — [saleor/graphql/webhook/subscription_types.py:305]
- `Meta` (class) — [saleor/graphql/webhook/subscription_types.py:306]
- `AddressDeleted` (class) — [saleor/graphql/webhook/subscription_types.py:313]
- `Meta` (class) — [saleor/graphql/webhook/subscription_types.py:314]
- `AppBase` (class) — [saleor/graphql/webhook/subscription_types.py:321]
- _…and 466 more in this file_

**`saleor/graphql/webhook/types.py`**

- `WebhookEvent` (class) — [saleor/graphql/webhook/types.py:28]
- `Meta` (class) — [saleor/graphql/webhook/types.py:34]
- `resolve_name` (function) — [saleor/graphql/webhook/types.py:39]
- `WebhookEventAsync` (class) — [saleor/graphql/webhook/types.py:43]
- `Meta` (class) — [saleor/graphql/webhook/types.py:49]
- `resolve_name` (function) — [saleor/graphql/webhook/types.py:54]
- `WebhookEventSync` (class) — [saleor/graphql/webhook/types.py:60]
- `Meta` (class) — [saleor/graphql/webhook/types.py:66]
- `resolve_name` (function) — [saleor/graphql/webhook/types.py:71]
- `EventDeliveryAttempt` (class) — [saleor/graphql/webhook/types.py:77]
- `Meta` (class) — [saleor/graphql/webhook/types.py:100]
- `EventDeliveryAttemptCountableConnection` (class) — [saleor/graphql/webhook/types.py:106]
- `Meta` (class) — [saleor/graphql/webhook/types.py:107]
- `EventDelivery` (class) — [saleor/graphql/webhook/types.py:111]
- `Meta` (class) — [saleor/graphql/webhook/types.py:127]
- `resolve_attempts` (function) — [saleor/graphql/webhook/types.py:133]
- `resolve_payload` (function) — [saleor/graphql/webhook/types.py:145]
- `EventDeliveryCountableConnection` (class) — [saleor/graphql/webhook/types.py:151]
- `Meta` (class) — [saleor/graphql/webhook/types.py:152]
- `Webhook` (class) — [saleor/graphql/webhook/types.py:156]
- `Meta` (class) — [saleor/graphql/webhook/types.py:208]
- `resolve_async_events` (function) — [saleor/graphql/webhook/types.py:214]
- `resolve_sync_events` (function) — [saleor/graphql/webhook/types.py:229]
- `resolve_events` (function) — [saleor/graphql/webhook/types.py:244]
- `resolve_event_deliveries` (function) — [saleor/graphql/webhook/types.py:248]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/webhook/__init__.py` (1 lines)
- `saleor/graphql/webhook/dataloaders/__init__.py` (13 lines)
- `saleor/graphql/webhook/dataloaders/models.py` (144 lines)
- `saleor/graphql/webhook/enums.py` (346 lines)
- `saleor/graphql/webhook/filters.py` (26 lines)
- `saleor/graphql/webhook/mixins.py` (21 lines)
- `saleor/graphql/webhook/resolvers.py` (55 lines)
- `saleor/graphql/webhook/schema.py` (77 lines)
- `saleor/graphql/webhook/sorters.py` (44 lines)
- `saleor/graphql/webhook/subscription_payload.py` (309 lines)
- `saleor/graphql/webhook/subscription_query.py` (211 lines)
- `saleor/graphql/webhook/subscription_types.py` (3335 lines)
- `saleor/graphql/webhook/types.py` (257 lines)

## Interactions

- Imports from: `saleor/graphql`, `saleor/graphql/product/types`, `saleor/core`
- Imported by: `saleor/graphql/webhook/mutations`

Internal dependencies named in the source:

- `....__version__`
- `....core.models.EventPayload`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.models.Webhook`
- `....webhook.models.WebhookEvent`
- `...account.models.User`
- `...app.dataloaders.ActiveAppByIdLoader`
- `...app.models.App`
- `...attribute.models.AttributeTranslation`
- `...attribute.models.AttributeValueTranslation`
- `...channel.models.Channel`
- `...core.dataloaders.DataLoader`
- `...core.exceptions.PermissionDenied`
- `...core.models`
- `...core.prices.quantize_price`
- `...core.utils.get_domain`
- `...graphql.shop.types.Shop`
- `...menu.models.MenuItemTranslation`
- `...page.models.PageTranslation`
- `...permission.auth_filters.AuthorizationFilters`
- `...permission.enums.AppPermission`
- `...product.interface.VariantDiscountedPriceChange`
- `...shipping.models.ShippingMethodTranslation`
- `...thumbnail.views.TYPE_TO_MODEL_DATA_MAPPING`
- `...warehouse.interface.VariantChannelStockInfo`
- `...webhook.const.MAX_FILTERABLE_CHANNEL_SLUGS_LIMIT`
- `...webhook.deprecated_event_types.WebhookEventType`
- `...webhook.error_codes.WebhookErrorCode`
- `...webhook.event_types.WebhookEventAsyncType`
- `...webhook.event_types.WebhookEventSyncType`
- `...webhook.models`
- `...webhook.models.Webhook`
- `...webhook.payloads`
- `..account.types.User`
- `..api.schema`
- `..app.dataloaders.app_promise_callback`
- `..app.types.App`
- `..channel.dataloaders.by_self.ChannelBySlugLoader`
- `..channel.enums.TransactionFlowStrategyEnum`
- `..context.get_context_value`
- `..core.ResolveInfo`
- `..core.SaleorContext`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.descriptions.ADDED_IN_323`
- `..core.doc_category.DOC_CATEGORY_WEBHOOKS`
- `..core.fields.BaseField`
- `..core.fields.FilterConnectionField`
- `..core.fields.JSONString`
- `..core.fields.PermissionsField`
- `..core.filters.EnumFilter`
- `..core.filters.FilterInputObjectType`
- `..core.scalars.DateTime`
- `..core.scalars.JSON`
- `..core.scalars.PositiveDecimal`
- `..core.tracing.traced_resolver`
- `..core.types.BaseEnum`
- `..core.types.ModelObjectType`
- `..core.types.NonNullList`
- `..core.types.SortInputObjectType`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `40f30a5ad409` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
