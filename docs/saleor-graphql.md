## Purpose

`saleor/graphql` (`saleor/graphql`) groups 18 source file(s) exposing 118 top-level declaration(s).

## Public surface

**`saleor/graphql/__init__.py`**

- `GraphQLOperationResult` (class) — [saleor/graphql/__init__.py:4]

**`saleor/graphql/AGENTS.md`**

- `resolve_parent` (function) — [saleor/graphql/AGENTS.md:24]
- `Migration` (class) — [saleor/graphql/AGENTS.md:61]

**`saleor/graphql/api.py`**

- `monitor_fields_usage` (function) — [saleor/graphql/api.py:59]
- `wrapper` (function) — [saleor/graphql/api.py:79]
- `Query` (class) — [saleor/graphql/api.py:92]
- `Mutation` (class) — [saleor/graphql/api.py:119]
- `serialize_webhook_event` (function) — [saleor/graphql/api.py:168]
- `SaleorGraphQLBackend` (class) — [saleor/graphql/api.py:234]
- `document_from_string` (function) — [saleor/graphql/api.py:235]

**`saleor/graphql/CLAUDE.md`**

- `resolve_parent` (function) — [saleor/graphql/CLAUDE.md:24]
- `Migration` (class) — [saleor/graphql/CLAUDE.md:61]

**`saleor/graphql/context.py`**

- `get_context_value` (function) — [saleor/graphql/context.py:17]
- `clear_context` (function) — [saleor/graphql/context.py:29]
- `RequestWithUser` (class) — [saleor/graphql/context.py:64]
- `set_decoded_auth_token` (function) — [saleor/graphql/context.py:69]
- `set_app_on_context` (function) — [saleor/graphql/context.py:77]
- `get_user` (function) — [saleor/graphql/context.py:82]
- `set_auth_on_context` (function) — [saleor/graphql/context.py:88]
- `user` (function) — [saleor/graphql/context.py:93]

**`saleor/graphql/decorators.py`**

- `context` (function) — [saleor/graphql/decorators.py:27]
- `decorator` (function) — [saleor/graphql/decorators.py:28]
- `wrapper` (function) — [saleor/graphql/decorators.py:30]
- `account_passes_test` (function) — [saleor/graphql/decorators.py:39]
- `decorator` (function) — [saleor/graphql/decorators.py:42]
- `wrapper` (function) — [saleor/graphql/decorators.py:45]
- `account_passes_test_for_attribute` (function) — [saleor/graphql/decorators.py:54]
- `decorator` (function) — [saleor/graphql/decorators.py:57]
- `wrapper` (function) — [saleor/graphql/decorators.py:60]
- `permission_required` (function) — [saleor/graphql/decorators.py:70]
- `check_perms` (function) — [saleor/graphql/decorators.py:71]
- `one_of_permissions_required` (function) — [saleor/graphql/decorators.py:84]
- `check_perms` (function) — [saleor/graphql/decorators.py:85]
- `check_attribute_required_permissions` (function) — [saleor/graphql/decorators.py:117]
- `check_perms` (function) — [saleor/graphql/decorators.py:124]

**`saleor/graphql/error.py`**

- `pydantic_to_validation_error` (function) — [saleor/graphql/error.py:6]
- `clear_traceback_locals` (function) — [saleor/graphql/error.py:31]
- `clear_exception_locals` (function) — [saleor/graphql/error.py:46]
- `clear_errors` (function) — [saleor/graphql/error.py:59]

**`saleor/graphql/graphql_core.py`**

- `patch_executor` (function) — [saleor/graphql/graphql_core.py:15]
- `patch_execution_context` (function) — [saleor/graphql/graphql_core.py:33]
- `patch_execution_result` (function) — [saleor/graphql/graphql_core.py:48]

**`saleor/graphql/metrics.py`**

- `record_graphql_query_count` (function) — [saleor/graphql/metrics.py:124]
- `record_graphql_query_duration` (function) — [saleor/graphql/metrics.py:139]
- `record_graphql_query_cost` (function) — [saleor/graphql/metrics.py:165]
- `record_request_count` (function) — [saleor/graphql/metrics.py:177]
- `record_request_duration` (function) — [saleor/graphql/metrics.py:187]
- `record_field_usage` (function) — [saleor/graphql/metrics.py:192]
- `record_graphql_batch_size` (function) — [saleor/graphql/metrics.py:202]
- `record_graphql_alias_count` (function) — [saleor/graphql/metrics.py:206]
- `record_graphql_mutation_count` (function) — [saleor/graphql/metrics.py:210]

**`saleor/graphql/middleware.py`**

- `process_view` (function) — [saleor/graphql/middleware.py:4]

**`saleor/graphql/promise.py`**

- `patch_promise` (function) — [saleor/graphql/promise.py:15]

**`saleor/graphql/schema_printer.py`**

- `is_specified_directive` (function) — [saleor/graphql/schema_printer.py:33]
- `print_schema` (function) — [saleor/graphql/schema_printer.py:37]
- `is_introspection_type` (function) — [saleor/graphql/schema_printer.py:43]
- `print_introspection_schema` (function) — [saleor/graphql/schema_printer.py:47]
- `is_specified_scalar_type` (function) — [saleor/graphql/schema_printer.py:54]
- `is_defined_type` (function) — [saleor/graphql/schema_printer.py:58]
- `print_filtered_schema` (function) — [saleor/graphql/schema_printer.py:62]
- `print_schema_definition` (function) — [saleor/graphql/schema_printer.py:81]
- `is_schema_of_common_names` (function) — [saleor/graphql/schema_printer.py:99]
- `print_object_directives_for_category` (function) — [saleor/graphql/schema_printer.py:126]
- `print_object_directvie_for_webhook_events_info` (function) — [saleor/graphql/schema_printer.py:131]
- `print_object_directives` (function) — [saleor/graphql/schema_printer.py:152]
- `print_field_directives_for_category` (function) — [saleor/graphql/schema_printer.py:158]
- `print_field_directives_for_webhook_events_info` (function) — [saleor/graphql/schema_printer.py:171]
- `print_field_directives` (function) — [saleor/graphql/schema_printer.py:198]
- `print_type` (function) — [saleor/graphql/schema_printer.py:206]
- `print_scalar` (function) — [saleor/graphql/schema_printer.py:230]
- `print_implemented_interfaces` (function) — [saleor/graphql/schema_printer.py:234]
- `print_object` (function) — [saleor/graphql/schema_printer.py:239]
- `print_interface` (function) — [saleor/graphql/schema_printer.py:254]
- `print_union` (function) — [saleor/graphql/schema_printer.py:263]
- `print_enum` (function) — [saleor/graphql/schema_printer.py:269]
- `print_input_object` (function) — [saleor/graphql/schema_printer.py:284]
- `print_fields` (function) — [saleor/graphql/schema_printer.py:297]
- `print_block` (function) — [saleor/graphql/schema_printer.py:313]
- `print_args` (function) — [saleor/graphql/schema_printer.py:317]
- `print_input_value` (function) — [saleor/graphql/schema_printer.py:341]
- `print_directive` (function) — [saleor/graphql/schema_printer.py:356]
- `print_deprecated` (function) — [saleor/graphql/schema_printer.py:366]
- `is_printable_as_block_string` (function) — [saleor/graphql/schema_printer.py:375]
- `print_block_string` (function) — [saleor/graphql/schema_printer.py:412]
- `print_description` (function) — [saleor/graphql/schema_printer.py:466]

**`saleor/graphql/site/dataloaders.py`**

- `SiteByIdLoader` (class) — [saleor/graphql/site/dataloaders.py:15]
- `batch_load` (function) — [saleor/graphql/site/dataloaders.py:18]
- `SiteByHostLoader` (class) — [saleor/graphql/site/dataloaders.py:23]
- `batch_load` (function) — [saleor/graphql/site/dataloaders.py:26]
- `get_site_promise` (function) — [saleor/graphql/site/dataloaders.py:35]
- `execute_callback_if_site_not_none` (function) — [saleor/graphql/site/dataloaders.py:48]
- `ensure_that_site_is_not_none` (function) — [saleor/graphql/site/dataloaders.py:59]
- `load_site_callback` (function) — [saleor/graphql/site/dataloaders.py:74]

**`saleor/graphql/storefront_traffic.py`**

- `set_allow_storefront_traffic_cache` (function) — [saleor/graphql/storefront_traffic.py:29]
- `clear_allow_storefront_traffic_cache` (function) — [saleor/graphql/storefront_traffic.py:37]
- `get_allow_storefront_traffic` (function) — [saleor/graphql/storefront_traffic.py:41]
- `is_storefront_traffic_blocked` (function) — [saleor/graphql/storefront_traffic.py:88]

**`saleor/graphql/views.py`**

- `default_serializer` (function) — [saleor/graphql/views.py:81]
- `JsonResponse` (class) — [saleor/graphql/views.py:87]
- `GraphQLView` (class) — [saleor/graphql/views.py:104]
- `import_middleware` (function) — [saleor/graphql/views.py:150]
- `dispatch` (function) — [saleor/graphql/views.py:162]
- `render_playground` (function) — [saleor/graphql/views.py:174]
- `handle_query` (function) — [saleor/graphql/views.py:240]
- `get_response` (function) — [saleor/graphql/views.py:305]
- `get_root_value` (function) — [saleor/graphql/views.py:335]
- `parse_query` (function) — [saleor/graphql/views.py:338]
- `execute_graphql_request` (function) — [saleor/graphql/views.py:364]
- `parse_body` (function) — [saleor/graphql/views.py:562]
- `get_graphql_params` (function) — [saleor/graphql/views.py:577]
- `format_error` (function) — [saleor/graphql/views.py:602]
- `format_span_error_description` (function) — [saleor/graphql/views.py:605]
- `get_key` (function) — [saleor/graphql/views.py:613]
- `get_shallow_property` (function) — [saleor/graphql/views.py:622]
- `obj_set` (function) — [saleor/graphql/views.py:631]
- `instantiate_middleware` (function) — [saleor/graphql/views.py:658]
- `generate_cache_key` (function) — [saleor/graphql/views.py:666]
- `set_query_cost_on_result` (function) — [saleor/graphql/views.py:675]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/promise.py` (22 lines)
- `saleor/graphql/error.py` (67 lines)
- `saleor/graphql/__init__.py` (7 lines)
- `saleor/graphql/decorators.py` (144 lines)
- `saleor/graphql/storefront_traffic.py` (104 lines)
- `saleor/graphql/AGENTS.md` (74 lines)
- `saleor/graphql/api.py` (259 lines)
- `saleor/graphql/CLAUDE.md` (74 lines)
- `saleor/graphql/conftest.py` (22 lines)
- `saleor/graphql/context.py` (96 lines)
- `saleor/graphql/graphql_core.py` (57 lines)
- `saleor/graphql/metrics.py` (211 lines)
- `saleor/graphql/middleware.py` (8 lines)
- `saleor/graphql/query_cost_map.py` (445 lines)
- `saleor/graphql/schema_printer.py` (498 lines)
- `saleor/graphql/site/__init__.py` (1 lines)
- `saleor/graphql/site/dataloaders.py` (80 lines)
- `saleor/graphql/views.py` (685 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`, `saleor/core/utils`, `saleor/core/db`, `saleor/graphql/core`, `saleor/core/telemetry`, `saleor`
- Imported by: `saleor/graphql/checkout/dataloaders`, `saleor/graphql/order`, `saleor/graphql/product/types`, `saleor/graphql/translations/mutations`, `saleor/graphql/webhook`, `saleor/payment/gateways`, `saleor/checkout/tests`, `saleor/checkout/webhooks`, `saleor/graphql/checkout/tests/mutations`, `saleor/graphql/core`, `saleor/graphql/utils`, `saleor/checkout`, `saleor/checkout/tests/webhooks`, `saleor/graphql/attribute/utils`, `saleor/graphql/channel`, `saleor/graphql/core/tests`, `saleor/graphql/giftcard`, `saleor/order`, `saleor/order/tests`, `saleor/order/tests/webhooks`, `saleor/order/webhooks`, `saleor/core`, `saleor/graphql/account`, `saleor/graphql/app/dataloaders`, `saleor/graphql/attribute/dataloaders`, `saleor/graphql/attribute/mutations`, `saleor/graphql/attribute`, `saleor/graphql/channel/dataloaders`, `saleor/graphql/checkout/mutations`, `saleor/graphql/checkout`, `saleor/graphql/core/federation`, `saleor/graphql/core/tests/garbage_collection`, `saleor/graphql/core/types`, `saleor/graphql/core/validators`, `saleor/graphql/discount`, `saleor/graphql/discount/mutations/promotion`, `saleor/graphql/order/bulk_mutations`, `saleor/graphql/order/mutations`, `saleor/graphql/order/tests/mutations`, `saleor/graphql/order/tests/queries`, `saleor/graphql/payment`, `saleor/graphql/plugins`, `saleor/graphql/product`, `saleor/graphql/shipping/tests/mutations`, `saleor/graphql/tax`, `saleor/graphql/tests`, `saleor/graphql/warehouse`, `saleor/graphql/webhook/tests`, `saleor/plugins/admin_email`, `saleor/plugins`, `saleor/plugins/user_email`, `saleor/plugins/webhook`, `saleor/shipping/tests`, `saleor/shipping`, `saleor/tax/webhooks`, `saleor/thumbnail`, `saleor`, `saleor/webhook`, `saleor/webhook/response_schemas`, `saleor/webhook/tests/circuit_breaker`, `saleor/webhook/transport/asynchronous`, `saleor/webhook/transport/synchronous`

Internal dependencies named in the source:

- `...__version__`
- `..GraphQLOperationResult`
- `..account.models.User`
- `..app.models.App`
- `..attribute.AttributeType`
- `..attribute.models.Attribute`
- `..core.auth.get_token_from_request`
- `..core.dataloaders.DataLoader`
- `..core.exceptions.PermissionDenied`
- `..core.jwt.jwt_decode_with_exception_handler`
- `..core.telemetry.Scope`
- `..core.telemetry.SpanKind`
- `..core.telemetry.saleor_attributes`
- `..core.telemetry.tracer`
- `..core.utils.cache.CacheDict`
- `..graphql.notifications.schema.ExternalNotificationMutations`
- `..permission.auth_filters.is_app`
- `..permission.auth_filters.is_staff_user`
- `..permission.utils.permission_required`
- `..site.models.SiteSettings`
- `..webhook.event_types.WebhookEventAsyncType`
- `..webhook.event_types.WebhookEventSyncType`
- `..webhook.observability`
- `.account.schema.AccountMutations`
- `.account.schema.AccountQueries`
- `.api.API_PATH`
- `.api.schema`
- `.app.dataloaders.get_app_promise`
- `.app.schema.AppMutations`
- `.app.schema.AppQueries`
- `.attribute.schema.AttributeMutations`
- `.attribute.schema.AttributeQueries`
- `.attribute.types.ASSIGNED_ATTRIBUTE_TYPES`
- `.channel.schema.ChannelMutations`
- `.channel.schema.ChannelQueries`
- `.checkout.schema.CheckoutMutations`
- `.checkout.schema.CheckoutQueries`
- `.context.clear_context`
- `.context.get_context_value`
- `.core.SaleorContext`
- `.core.context.ChannelContext`
- `.core.enums.unit_enums`
- `.core.federation.schema.build_federated_schema`
- `.core.schema.CoreMutations`
- `.core.schema.CoreQueries`
- `.core.validators.validate_query`
- `.csv.schema.CsvMutations`
- `.csv.schema.CsvQueries`
- `.discount.schema.DiscountMutations`
- `.discount.schema.DiscountQueries`
- `.error.clear_errors`
- `.giftcard.schema.GiftCardMutations`
- `.giftcard.schema.GiftCardQueries`
- `.invoice.schema.InvoiceMutations`
- `.menu.schema.MenuMutations`
- `.menu.schema.MenuQueries`
- `.meta.schema.MetaMutations`
- `.metrics.record_field_usage`
- `.order.schema.OrderMutations`
- `.order.schema.OrderQueries`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `e7b9b3aa17b1` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
