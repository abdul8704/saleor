## Purpose

`saleor/graphql/webhook/mutations` (`saleor/graphql/webhook/mutations`) groups 7 source file(s) exposing 41 top-level declaration(s).

## Public surface

**`saleor/graphql/webhook/mutations/event_delivery_retry.py`**

- `EventDeliveryRetry` (class) — [saleor/graphql/webhook/mutations/event_delivery_retry.py:16]
- `Arguments` (class) — [saleor/graphql/webhook/mutations/event_delivery_retry.py:19]
- `Meta` (class) — [saleor/graphql/webhook/mutations/event_delivery_retry.py:24]
- `perform_mutation` (function) — [saleor/graphql/webhook/mutations/event_delivery_retry.py:31]

**`saleor/graphql/webhook/mutations/webhook_create.py`**

- `WebhookCreateInput` (class) — [saleor/graphql/webhook/mutations/webhook_create.py:29]
- `Meta` (class) — [saleor/graphql/webhook/mutations/webhook_create.py:79]
- `WebhookCreate` (class) — [saleor/graphql/webhook/mutations/webhook_create.py:83]
- `Arguments` (class) — [saleor/graphql/webhook/mutations/webhook_create.py:84]
- `Meta` (class) — [saleor/graphql/webhook/mutations/webhook_create.py:89]
- `clean_input` (function) — [saleor/graphql/webhook/mutations/webhook_create.py:101]
- `get_instance` (function) — [saleor/graphql/webhook/mutations/webhook_create.py:191]
- `save` (function) — [saleor/graphql/webhook/mutations/webhook_create.py:198]

**`saleor/graphql/webhook/mutations/webhook_delete.py`**

- `WebhookDelete` (class) — [saleor/graphql/webhook/mutations/webhook_delete.py:18]
- `Arguments` (class) — [saleor/graphql/webhook/mutations/webhook_delete.py:19]
- `Meta` (class) — [saleor/graphql/webhook/mutations/webhook_delete.py:22]
- `perform_mutation` (function) — [saleor/graphql/webhook/mutations/webhook_delete.py:39]

**`saleor/graphql/webhook/mutations/webhook_dry_run.py`**

- `WebhookDryRun` (class) — [saleor/graphql/webhook/mutations/webhook_dry_run.py:26]
- `Arguments` (class) — [saleor/graphql/webhook/mutations/webhook_dry_run.py:31]
- `Meta` (class) — [saleor/graphql/webhook/mutations/webhook_dry_run.py:41]
- `validate_query` (function) — [saleor/graphql/webhook/mutations/webhook_dry_run.py:52]
- `validate_event_type` (function) — [saleor/graphql/webhook/mutations/webhook_dry_run.py:65]
- `validate_permissions` (function) — [saleor/graphql/webhook/mutations/webhook_dry_run.py:86]
- `validate_input` (function) — [saleor/graphql/webhook/mutations/webhook_dry_run.py:101]
- `get_instance` (function) — [saleor/graphql/webhook/mutations/webhook_dry_run.py:113]
- `perform_mutation` (function) — [saleor/graphql/webhook/mutations/webhook_dry_run.py:124]

**`saleor/graphql/webhook/mutations/webhook_trigger.py`**

- `WebhookTrigger` (class) — [saleor/graphql/webhook/mutations/webhook_trigger.py:39]
- `Arguments` (class) — [saleor/graphql/webhook/mutations/webhook_trigger.py:42]
- `Meta` (class) — [saleor/graphql/webhook/mutations/webhook_trigger.py:48]
- `validate_subscription_query` (function) — [saleor/graphql/webhook/mutations/webhook_trigger.py:60]
- `validate_event_type` (function) — [saleor/graphql/webhook/mutations/webhook_trigger.py:80]
- `validate_permissions` (function) — [saleor/graphql/webhook/mutations/webhook_trigger.py:117]
- `validate_input` (function) — [saleor/graphql/webhook/mutations/webhook_trigger.py:132]
- `get_instance` (function) — [saleor/graphql/webhook/mutations/webhook_trigger.py:151]
- `perform_mutation` (function) — [saleor/graphql/webhook/mutations/webhook_trigger.py:159]

**`saleor/graphql/webhook/mutations/webhook_update.py`**

- `WebhookUpdateInput` (class) — [saleor/graphql/webhook/mutations/webhook_update.py:21]
- `Meta` (class) — [saleor/graphql/webhook/mutations/webhook_update.py:77]
- `WebhookUpdate` (class) — [saleor/graphql/webhook/mutations/webhook_update.py:81]
- `Arguments` (class) — [saleor/graphql/webhook/mutations/webhook_update.py:82]
- `Meta` (class) — [saleor/graphql/webhook/mutations/webhook_update.py:88]
- `save` (function) — [saleor/graphql/webhook/mutations/webhook_update.py:100]
- `get_instance` (function) — [saleor/graphql/webhook/mutations/webhook_update.py:114]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/webhook/mutations/webhook_create.py` (206 lines)
- `saleor/graphql/webhook/mutations/__init__.py` (15 lines)
- `saleor/graphql/webhook/mutations/event_delivery_retry.py` (48 lines)
- `saleor/graphql/webhook/mutations/webhook_delete.py` (73 lines)
- `saleor/graphql/webhook/mutations/webhook_dry_run.py` (147 lines)
- `saleor/graphql/webhook/mutations/webhook_trigger.py` (209 lines)
- `saleor/graphql/webhook/mutations/webhook_update.py` (121 lines)

## Interactions

- Imports from: `saleor/graphql/webhook`, `saleor/plugins/openid_connect`
- Imported by: `saleor/graphql/webhook/tests/mutations`

Internal dependencies named in the source:

- `....app.models.App`
- `....core.EventDeliveryStatus`
- `....core.models`
- `....core.telemetry.get_task_context`
- `....core.utils.events.get_is_deferred_payload`
- `....core.utils.get_domain`
- `....discount.models`
- `....graphql.utils.get_user_or_app_from_context`
- `....permission.auth_filters.AuthorizationFilters`
- `....permission.enums.AppPermission`
- `....webhook.const.MAX_FILTERABLE_CHANNEL_SLUGS_LIMIT`
- `....webhook.error_codes.WebhookDryRunErrorCode`
- `....webhook.error_codes.WebhookErrorCode`
- `....webhook.error_codes.WebhookTriggerErrorCode`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.models`
- `....webhook.models.Webhook`
- `....webhook.validators.HEADERS_LENGTH_LIMIT`
- `....webhook.validators.HEADERS_NUMBER_LIMIT`
- `...app.dataloaders.get_app_promise`
- `...app.utils.validate_app_is_not_removed`
- `...core.ResolveInfo`
- `...core.context.SaleorContext`
- `...core.descriptions.ADDED_IN_323`
- `...core.descriptions.DEPRECATED_IN_3X_INPUT`
- `...core.doc_category.DOC_CATEGORY_WEBHOOKS`
- `...core.fields.JSONString`
- `...core.mutations.BaseMutation`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.types.BaseInputObjectType`
- `...core.types.NonNullList`
- `...core.types.WebhookDryRunError`
- `...core.types.WebhookError`
- `...core.types.common.WebhookTriggerError`
- `...core.utils.from_global_id_or_error`
- `...core.utils.raise_validation_error`
- `...enums`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...utils.get_user_or_app_from_context`
- `..WebhookCreate`
- `..mixins.NotifyUserEventValidationMixin`
- `..subscription_query.SubscriptionQuery`
- `..subscription_types.ASYNC_WEBHOOK_TYPES_MAP`
- `..subscription_types.WEBHOOK_TYPES_MAP`
- `..types.EventDelivery`
- `..types.Webhook`
- `.event_delivery_retry.EventDeliveryRetry`
- `.webhook_create.WebhookCreate`
- `.webhook_delete.WebhookDelete`
- `.webhook_dry_run.WebhookDryRun`
- `.webhook_trigger.WebhookTrigger`
- `.webhook_update.WebhookUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `3cceaeb6500e` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
