## Purpose

`saleor/core` (`saleor/core`) groups 39 source file(s) exposing 237 top-level declaration(s).

## Public surface

**`saleor/core/__init__.py`**

- `JobStatus` (class) — [saleor/core/__init__.py:7]
- `TimePeriodType` (class) — [saleor/core/__init__.py:21]
- `EventDeliveryStatus` (class) — [saleor/core/__init__.py:30]
- `PrivateStorage` (class) — [saleor/core/__init__.py:46]

**`saleor/core/anonymize.py`**

- `obfuscate_email` (function) — [saleor/core/anonymize.py:1]
- `obfuscate_string` (function) — [saleor/core/anonymize.py:9]
- `obfuscate_address` (function) — [saleor/core/anonymize.py:19]

**`saleor/core/apps.py`**

- `CoreAppConfig` (class) — [saleor/core/apps.py:11]
- `ready` (function) — [saleor/core/apps.py:14]
- `validate_jwt_manager` (function) — [saleor/core/apps.py:21]

**`saleor/core/auth_backend.py`**

- `BaseBackend` (class) — [saleor/core/auth_backend.py:26]
- `authenticate` (function) — [saleor/core/auth_backend.py:27]
- `get_user` (function) — [saleor/core/auth_backend.py:30]
- `get_user_permissions` (function) — [saleor/core/auth_backend.py:33]
- `get_group_permissions` (function) — [saleor/core/auth_backend.py:36]
- `get_all_permissions` (function) — [saleor/core/auth_backend.py:39]
- `has_perm` (function) — [saleor/core/auth_backend.py:45]
- `JSONWebTokenBackend` (class) — [saleor/core/auth_backend.py:49]
- `authenticate` (function) — [saleor/core/auth_backend.py:50]
- `get_user` (function) — [saleor/core/auth_backend.py:53]
- `get_user_permissions` (function) — [saleor/core/auth_backend.py:85]
- `get_group_permissions` (function) — [saleor/core/auth_backend.py:90]
- `get_all_permissions` (function) — [saleor/core/auth_backend.py:95]
- `has_perm` (function) — [saleor/core/auth_backend.py:103]
- `PluginBackend` (class) — [saleor/core/auth_backend.py:107]
- `authenticate` (function) — [saleor/core/auth_backend.py:108]
- `load_user_from_request` (function) — [saleor/core/auth_backend.py:125]

**`saleor/core/auth.py`**

- `get_token_from_request` (function) — [saleor/core/auth.py:8]

**`saleor/core/context.py`**

- `with_promise_context` (function) — [saleor/core/context.py:4]
- `wrapper` (function) — [saleor/core/context.py:10]
- `promise_executor` (function) — [saleor/core/context.py:11]

**`saleor/core/db_routers.py`**

- `PrimaryReplicaRouter` (class) — [saleor/core/db_routers.py:4]
- `db_for_write` (function) — [saleor/core/db_routers.py:5]
- `allow_relation` (function) — [saleor/core/db_routers.py:9]

**`saleor/core/error_codes.py`**

- `ShopErrorCode` (class) — [saleor/core/error_codes.py:4]
- `MetadataErrorCode` (class) — [saleor/core/error_codes.py:15]
- `TranslationErrorCode` (class) — [saleor/core/error_codes.py:23]
- `UploadErrorCode` (class) — [saleor/core/error_codes.py:31]
- `CoreErrorCode` (class) — [saleor/core/error_codes.py:37]

**`saleor/core/exceptions.py`**

- `InsufficientStockData` (class) — [saleor/core/exceptions.py:18]
- `UnsupportedMediaProviderException` (class) — [saleor/core/exceptions.py:26]
- `NonExistingCheckoutLines` (class) — [saleor/core/exceptions.py:32]
- `NonExistingCheckout` (class) — [saleor/core/exceptions.py:38]
- `InsufficientStock` (class) — [saleor/core/exceptions.py:44]
- `AllocationError` (class) — [saleor/core/exceptions.py:52]
- `PreorderAllocationError` (class) — [saleor/core/exceptions.py:59]
- `ProductNotPublished` (class) — [saleor/core/exceptions.py:65]
- `PermissionDenied` (class) — [saleor/core/exceptions.py:72]
- `GiftCardNotApplicable` (class) — [saleor/core/exceptions.py:87]
- `CircularSubscriptionSyncEvent` (class) — [saleor/core/exceptions.py:94]
- `SyncEventError` (class) — [saleor/core/exceptions.py:98]

**`saleor/core/hashers.py`**

- `SHA512Base64PBKDF2PasswordHasher` (class) — [saleor/core/hashers.py:8]
- `encode` (function) — [saleor/core/hashers.py:18]
- `pbkdf2_round` (function) — [saleor/core/hashers.py:30]

**`saleor/core/jwt_manager.py`**

- `JWTManagerBase` (class) — [saleor/core/jwt_manager.py:26]
- `get_domain` (function) — [saleor/core/jwt_manager.py:28]
- `get_private_key` (function) — [saleor/core/jwt_manager.py:32]
- `get_public_key` (function) — [saleor/core/jwt_manager.py:36]
- `encode` (function) — [saleor/core/jwt_manager.py:40]
- `jws_encode` (function) — [saleor/core/jwt_manager.py:44]
- `decode` (function) — [saleor/core/jwt_manager.py:48]
- `validate_configuration` (function) — [saleor/core/jwt_manager.py:52]
- `get_jwks` (function) — [saleor/core/jwt_manager.py:56]
- `get_key_id` (function) — [saleor/core/jwt_manager.py:60]
- `get_issuer` (function) — [saleor/core/jwt_manager.py:64]
- `JWTManager` (class) — [saleor/core/jwt_manager.py:68]
- `get_domain` (function) — [saleor/core/jwt_manager.py:73]
- `get_private_key` (function) — [saleor/core/jwt_manager.py:78]
- `get_public_key` (function) — [saleor/core/jwt_manager.py:135]
- `get_jwks` (function) — [saleor/core/jwt_manager.py:144]
- `get_key_id` (function) — [saleor/core/jwt_manager.py:150]
- `encode` (function) — [saleor/core/jwt_manager.py:164]
- `jws_encode` (function) — [saleor/core/jwt_manager.py:173]
- `decode` (function) — [saleor/core/jwt_manager.py:183]
- `validate_configuration` (function) — [saleor/core/jwt_manager.py:202]
- `get_issuer` (function) — [saleor/core/jwt_manager.py:225]
- `get_jwt_manager` (function) — [saleor/core/jwt_manager.py:230]

**`saleor/core/jwt.py`**

- `jwt_base_payload` (function) — [saleor/core/jwt.py:32]
- `jwt_user_payload` (function) — [saleor/core/jwt.py:47]
- `jwt_encode` (function) — [saleor/core/jwt.py:69]
- `jwt_decode_with_exception_handler` (function) — [saleor/core/jwt.py:74]
- `jwt_decode` (function) — [saleor/core/jwt.py:81]
- `create_token` (function) — [saleor/core/jwt.py:86]
- `create_access_token` (function) — [saleor/core/jwt.py:104]
- `create_refresh_token` (function) — [saleor/core/jwt.py:113]
- `get_user_from_payload` (function) — [saleor/core/jwt.py:125]
- `is_saleor_token` (function) — [saleor/core/jwt.py:140]
- `get_user_from_access_payload` (function) — [saleor/core/jwt.py:152]
- `create_access_token_for_app` (function) — [saleor/core/jwt.py:202]
- `create_access_token_for_app_extension` (function) — [saleor/core/jwt.py:223]

**`saleor/core/logging.py`**

- `JsonFormatter` (class) — [saleor/core/logging.py:10]
- `add_fields` (function) — [saleor/core/logging.py:13]
- `JsonCeleryFormatter` (class) — [saleor/core/logging.py:23]
- `add_fields` (function) — [saleor/core/logging.py:24]
- `JsonCeleryTaskFormatter` (class) — [saleor/core/logging.py:38]
- `add_fields` (function) — [saleor/core/logging.py:39]

**`saleor/core/middleware.py`**

- `jwt_refresh_token_middleware` (function) — [saleor/core/middleware.py:18]
- `middleware` (function) — [saleor/core/middleware.py:19]

**`saleor/core/models.py`**

- `SortableModel` (class) — [saleor/core/models.py:16]
- `Meta` (class) — [saleor/core/models.py:19]
- `get_ordering_queryset` (function) — [saleor/core/models.py:22]
- `get_max_sort_order` (function) — [saleor/core/models.py:26]
- `save` (function) — [saleor/core/models.py:31]
- `delete` (function) — [saleor/core/models.py:39]
- `PublishedQuerySet` (class) — [saleor/core/models.py:57]
- `published` (function) — [saleor/core/models.py:58]
- `PublishableModel` (class) — [saleor/core/models.py:69]
- `Meta` (class) — [saleor/core/models.py:75]
- `is_visible` (function) — [saleor/core/models.py:79]
- `ModelWithMetadata` (class) — [saleor/core/models.py:86]
- `Meta` (class) — [saleor/core/models.py:94]
- `get_value_from_private_metadata` (function) — [saleor/core/models.py:101]
- `store_value_in_private_metadata` (function) — [saleor/core/models.py:104]
- `clear_private_metadata` (function) — [saleor/core/models.py:109]
- `delete_value_from_private_metadata` (function) — [saleor/core/models.py:112]
- `get_value_from_metadata` (function) — [saleor/core/models.py:118]
- `store_value_in_metadata` (function) — [saleor/core/models.py:121]
- `clear_metadata` (function) — [saleor/core/models.py:126]
- `delete_value_from_metadata` (function) — [saleor/core/models.py:129]
- `ModelWithExternalReference` (class) — [saleor/core/models.py:134]
- `Meta` (class) — [saleor/core/models.py:143]
- `Job` (class) — [saleor/core/models.py:147]
- `Meta` (class) — [saleor/core/models.py:155]
- `EventPayloadManager` (class) — [saleor/core/models.py:159]
- `create_with_payload_file` (function) — [saleor/core/models.py:161]
- `bulk_create_with_payload_files` (function) — [saleor/core/models.py:167]
- `EventPayload` (class) — [saleor/core/models.py:177]
- `get_payload` (function) — [saleor/core/models.py:189]
- `save_payload_file` (function) — [saleor/core/models.py:196]
- `save_as_file` (function) — [saleor/core/models.py:205]
- `EventDelivery` (class) — [saleor/core/models.py:212]
- `Meta` (class) — [saleor/core/models.py:225]
- `EventDeliveryAttempt` (class) — [saleor/core/models.py:229]
- `Meta` (class) — [saleor/core/models.py:246]

**`saleor/core/notify.py`**

- `NotifyHandler` (class) — [saleor/core/notify.py:5]
- `payload` (function) — [saleor/core/notify.py:18]
- `UserNotifyEvent` (class) — [saleor/core/notify.py:22]
- `AdminNotifyEvent` (class) — [saleor/core/notify.py:58]
- `NotifyEventType` (class) — [saleor/core/notify.py:74]

**`saleor/core/payments.py`**

- `PaymentInterface` (class) — [saleor/core/payments.py:15]
- `list_payment_gateways` (function) — [saleor/core/payments.py:17]
- `authorize_payment` (function) — [saleor/core/payments.py:28]
- `capture_payment` (function) — [saleor/core/payments.py:34]
- `refund_payment` (function) — [saleor/core/payments.py:40]
- `void_payment` (function) — [saleor/core/payments.py:46]
- `confirm_payment` (function) — [saleor/core/payments.py:52]
- `token_is_required_as_payment_input` (function) — [saleor/core/payments.py:58]
- `process_payment` (function) — [saleor/core/payments.py:64]
- `get_client_token` (function) — [saleor/core/payments.py:70]
- `list_payment_sources` (function) — [saleor/core/payments.py:76]

**`saleor/core/postgres.py`**

- `NoValidationSearchVectorCombinable` (class) — [saleor/core/postgres.py:16]
- `NoValidationCombinedSearchVector` (class) — [saleor/core/postgres.py:28]
- `NoValidationSearchVector` (class) — [saleor/core/postgres.py:35]
- `FlatConcat` (class) — [saleor/core/postgres.py:58]
- `get_source_expressions` (function) — [saleor/core/postgres.py:116]
- `set_source_expressions` (function) — [saleor/core/postgres.py:119]
- `copy` (function) — [saleor/core/postgres.py:122]
- `resolve_expression` (function) — [saleor/core/postgres.py:127]
- `as_sql` (function) — [saleor/core/postgres.py:138]
- `FlatConcatSearchVector` (class) — [saleor/core/postgres.py:150]

**`saleor/core/prices.py`**

- `quantize_price` (function) — [saleor/core/prices.py:21]
- `quantize_price_fields` (function) — [saleor/core/prices.py:29]

**`saleor/core/pricing/interface.py`**

- `LineInfo` (class) — [saleor/core/pricing/interface.py:21]
- `variant_discounted_price` (function) — [saleor/core/pricing/interface.py:33]
- `get_promotion_discounts` (function) — [saleor/core/pricing/interface.py:36]
- `get_catalogue_discounts` (function) — [saleor/core/pricing/interface.py:45]
- `get_voucher_discounts` (function) — [saleor/core/pricing/interface.py:54]

**`saleor/core/rlimit.py`**

- `is_soft_limit_set_without_hard_limit` (function) — [saleor/core/rlimit.py:8]
- `is_hard_limit_set_without_soft_limit` (function) — [saleor/core/rlimit.py:12]
- `validate_and_set_rlimit` (function) — [saleor/core/rlimit.py:16]

**`saleor/core/schedules.py`**

- `schedstate` (class) — [saleor/core/schedules.py:11]
- `promotion_webhook_schedule` (class) — [saleor/core/schedules.py:16]
- `remaining_estimate` (function) — [saleor/core/schedules.py:46]
- `is_due` (function) — [saleor/core/schedules.py:57]
- `TimeBaseSchedule` (class) — [saleor/core/schedules.py:129]
- `Meta` (class) — [saleor/core/schedules.py:142]
- `are_dirty` (function) — [saleor/core/schedules.py:157]
- `remaining_estimate` (function) — [saleor/core/schedules.py:160]
- `is_due` (function) — [saleor/core/schedules.py:171]
- `checkout_automatic_completion_schedule` (class) — [saleor/core/schedules.py:188]
- `are_dirty` (function) — [saleor/core/schedules.py:198]
- `page_search_update_schedule` (class) — [saleor/core/schedules.py:238]
- `are_dirty` (function) — [saleor/core/schedules.py:246]
- `product_search_update_schedule` (class) — [saleor/core/schedules.py:258]
- `are_dirty` (function) — [saleor/core/schedules.py:266]
- `gift_card_search_update_schedule` (class) — [saleor/core/schedules.py:278]
- `are_dirty` (function) — [saleor/core/schedules.py:286]
- `checkout_search_update_schedule` (class) — [saleor/core/schedules.py:298]
- `are_dirty` (function) — [saleor/core/schedules.py:306]

**`saleor/core/search_tasks.py`**

- `set_user_search_document_values` (function) — [saleor/core/search_tasks.py:33]
- `set_order_search_document_values` (function) — [saleor/core/search_tasks.py:62]
- `set_product_search_document_values` (function) — [saleor/core/search_tasks.py:123]
- `set_search_vector_values` (function) — [saleor/core/search_tasks.py:152]

**`saleor/core/search.py`**

- `parse_search_query` (function) — [saleor/core/search.py:89]
- `prefix_search` (function) — [saleor/core/search.py:144]

**`saleor/core/sqs.py`**

- `Channel` (class) — [saleor/core/sqs.py:12]
- `Transport` (class) — [saleor/core/sqs.py:65]

**`saleor/core/storages.py`**

- `S3MediaStorage` (class) — [saleor/core/storages.py:7]
- `S3MediaPrivateStorage` (class) — [saleor/core/storages.py:14]
- `GCSMediaStorage` (class) — [saleor/core/storages.py:21]
- `GCSMediaPrivateStorage` (class) — [saleor/core/storages.py:28]
- `AzureStorage` (class) — [saleor/core/storages.py:35]
- `AzureMediaStorage` (class) — [saleor/core/storages.py:44]
- `AzureMediaPrivateStorage` (class) — [saleor/core/storages.py:50]

**`saleor/core/tasks.py`**

- `RestrictWriterDBTask` (class) — [saleor/core/tasks.py:19]
- `delete_from_storage_task` (function) — [saleor/core/tasks.py:61]
- `delete_event_payloads_task` (function) — [saleor/core/tasks.py:66]
- `delete_files_from_storage_task` (function) — [saleor/core/tasks.py:96]
- `delete_files_from_private_storage_task` (function) — [saleor/core/tasks.py:102]

**`saleor/core/taxes.py`**

- `TaxError` (class) — [saleor/core/taxes.py:9]
- `TaxDataError` (class) — [saleor/core/taxes.py:13]
- `zero_money` (function) — [saleor/core/taxes.py:21]
- `zero_taxed_money` (function) — [saleor/core/taxes.py:29]
- `TaxType` (class) — [saleor/core/taxes.py:35]
- `TaxLineData` (class) — [saleor/core/taxes.py:43]
- `TaxData` (class) — [saleor/core/taxes.py:50]
- `TaxDataErrorMessage` (class) — [saleor/core/taxes.py:57]

**`saleor/core/templatetags/taxed_prices.py`**

- `price` (function) — [saleor/core/templatetags/taxed_prices.py:23]

**`saleor/core/tokens.py`**

- `BaseTokenGenerator` (class) — [saleor/core/tokens.py:14]
- `AccountDeleteTokenGenerator` (class) — [saleor/core/tokens.py:34]
- `try_generators` (function) — [saleor/core/tokens.py:44]

**`saleor/core/tracing.py`**

- `traced_atomic_transaction` (function) — [saleor/core/tracing.py:11]
- `otel_trace` (function) — [saleor/core/tracing.py:19]
- `webhooks_otel_trace` (function) — [saleor/core/tracing.py:26]

**`saleor/core/transactions.py`**

- `transaction_with_commit_on_errors` (function) — [saleor/core/transactions.py:9]

**`saleor/core/units.py`**

- `DistanceUnits` (class) — [saleor/core/units.py:1]
- `AreaUnits` (class) — [saleor/core/units.py:23]
- `VolumeUnits` (class) — [saleor/core/units.py:45]
- `WeightUnits` (class) — [saleor/core/units.py:77]
- `prepare_all_units_dict` (function) — [saleor/core/units.py:93]

**`saleor/core/views.py`**

- `home` (function) — [saleor/core/views.py:14]
- `jwks` (function) — [saleor/core/views.py:24]
- `serve_media_view` (function) — [saleor/core/views.py:28]

**`saleor/core/weight.py`**

- `zero_weight` (function) — [saleor/core/weight.py:20]
- `convert_weight` (function) — [saleor/core/weight.py:25]
- `get_default_weight_unit` (function) — [saleor/core/weight.py:35]
- `convert_weight_to_default_weight_unit` (function) — [saleor/core/weight.py:40]

## How it works

The module's files, as provided to this run:

- `saleor/core/postgres.py` (152 lines)
- `saleor/core/prices.py` (33 lines)
- `saleor/core/logging.py` (51 lines)
- `saleor/core/auth.py` (16 lines)
- `saleor/core/jwt.py` (237 lines)
- `saleor/core/hashers.py` (32 lines)
- `saleor/core/schedules.py` (325 lines)
- `saleor/core/__init__.py` (51 lines)
- `saleor/core/weight.py` (48 lines)
- `saleor/core/tokens.py` (84 lines)
- `saleor/core/taxes.py` (63 lines)
- `saleor/core/anonymize.py` (28 lines)
- `saleor/core/apps.py` (37 lines)
- `saleor/core/auth_backend.py` (189 lines)
- `saleor/core/context.py` (18 lines)
- `saleor/core/db_routers.py` (11 lines)
- `saleor/core/error_codes.py` (38 lines)
- `saleor/core/exceptions.py` (105 lines)
- `saleor/core/http_client.py` (14 lines)
- `saleor/core/jwt_manager.py` (231 lines)
- `saleor/core/languages.py` (808 lines)
- `saleor/core/middleware.py` (41 lines)
- `saleor/core/models.py` (247 lines)
- `saleor/core/notify.py` (75 lines)
- `saleor/core/payments.py` (79 lines)
- `saleor/core/pricing/__init__.py` (1 lines)
- `saleor/core/pricing/interface.py` (61 lines)
- `saleor/core/rlimit.py` (60 lines)
- `saleor/core/search_tasks.py` (163 lines)
- `saleor/core/search.py` (179 lines)
- `saleor/core/sqs.py` (66 lines)
- `saleor/core/storages.py` (53 lines)
- `saleor/core/tasks.py` (104 lines)
- `saleor/core/templatetags/__init__.py` (1 lines)
- `saleor/core/templatetags/taxed_prices.py` (28 lines)
- `saleor/core/tracing.py` (51 lines)
- `saleor/core/transactions.py` (20 lines)
- `saleor/core/units.py` (107 lines)
- `saleor/core/views.py` (61 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/plugins/openid_connect`, `saleor/webhook`, `saleor`, `saleor/graphql`, `saleor/account`
- Imported by: `saleor/order/migrations`, `saleor/product/migrations`, `saleor/account/migrations`, `saleor/payment/migrations`, `saleor/discount/migrations`, `saleor/checkout/migrations`, `saleor/checkout`, `saleor/graphql/order/tests/queries`, `saleor/attribute/migrations`, `saleor/checkout/tests`, `saleor/order`, `saleor/graphql/order/tests/mutations`, `saleor/order/tests`, `saleor/page/migrations`, `saleor/core/tests`, `saleor/giftcard/migrations`, `saleor/plugins/openid_connect`, `saleor/plugins/avatax`, `saleor/shipping`, `saleor/account`, `saleor/app`, `saleor/graphql/checkout/tests/mutations`, `saleor/payment`, `saleor/product`, `.semgrep`, `saleor/auth`, `saleor`, `saleor/core/utils`, `saleor/discount/utils`, `saleor/graphql/account/mutations/account`, `saleor/graphql/account/mutations/authentication`, `saleor/menu/migrations`, `saleor/order/tests/fixtures`, `saleor/payment/gateways`, `saleor/product/tests`, `saleor/shipping/migrations`, `saleor/tax/tests`, `saleor/webhook`, `saleor/webhook/response_schemas`, `saleor/app/migrations`, `saleor/attribute/models`, `saleor/checkout/tests/webhooks`, `saleor/checkout/webhooks`, `saleor/core/telemetry`, `saleor/graphql/core/validators`, `saleor/graphql/product/tests/mutations`, `saleor/graphql/product/tests/queries`, `saleor/graphql/tests`, `saleor/invoice/migrations`, `saleor/order/tests/webhooks`, `saleor/plugins`, `saleor/product/utils`, `saleor/schedulers`, `saleor/tax/calculations`, `saleor/warehouse/migrations`, `saleor/channel/migrations`, `saleor/checkout/tests/fixtures`, `saleor/core/db`, `saleor/discount`, `saleor/discount/tests/test_utils`, `saleor/giftcard`, `saleor/graphql/account`, `saleor/graphql/app/mutations`, `saleor/graphql/checkout/tests`, `saleor/graphql`, `saleor/graphql/core/types`, `saleor/graphql/order/tests/deprecated`, `saleor/graphql/order`, `saleor/graphql/product/tests`, `saleor/graphql/utils`, `saleor/graphql/webhook`, `saleor/order/webhooks`, `saleor/payment/tests/test_utils`, `saleor/plugins/sendgrid`, `saleor/plugins/tests`, `saleor/tax`, `saleor/tax/webhooks`, `saleor/webhook/migrations`, `saleor/webhook/transport`, `saleor/account/management`, `saleor/account/tests`, `saleor/app/tests`, `saleor/asgi`, `saleor/attribute/management`, `saleor/core/editorjs`, `saleor/discount/tests/fixtures`, `saleor/discount/tests`, `saleor/graphql/account/tests/fixtures`, `saleor/graphql/account/tests`, `saleor/graphql/app/dataloaders`, `saleor/graphql/channel/tests/queries`, `saleor/graphql/checkout/mutations`, `saleor/graphql/core/tests`, `saleor/graphql/giftcard`, `saleor/graphql/menu/tests/queries`, `saleor/graphql/order/bulk_mutations`, `saleor/graphql/order/mutations`, `saleor/graphql/order/tests`, `saleor/graphql/product`, `saleor/graphql/shipping`, `saleor/graphql/shipping/tests/mutations`, `saleor/invoice`, `saleor/page`, `saleor/permission`, `saleor/plugins/admin_email`, `saleor/plugins/user_email`, `saleor/plugins/webhook`, `saleor/product/management`, `saleor/shipping/tests`, `saleor/tests`, `saleor/thumbnail`, `saleor/warehouse`, `saleor/webhook/observability`, `saleor/webhook/tests`, `saleor/webhook/transport/asynchronous`, `saleor/webhook/transport/synchronous`

Internal dependencies named in the source:

- `...__version__`
- `...channel.models.Channel`
- `...checkout.models.CheckoutLine`
- `...discount.DiscountType`
- `...discount.models.CheckoutLineDiscount`
- `...discount.models.OrderLineDiscount`
- `...discount.models.Voucher`
- `...order.models.OrderLine`
- `...user_agent_version`
- `..EventDeliveryStatus`
- `..JobStatus`
- `..account.models.User`
- `..account.search.generate_user_search_vector_value`
- `..app.models.App`
- `..app.models.AppExtension`
- `..celeryconf.app`
- `..channel.models.Channel`
- `..checkout.CheckoutAuthorizeStatus`
- `..checkout.error_codes.CheckoutErrorCode`
- `..checkout.fetch.CheckoutInfo`
- `..checkout.fetch.CheckoutLineInfo`
- `..checkout.models.Checkout`
- `..checkout.models.CheckoutLine`
- `..core.db.connection.allow_writer`
- `..core.telemetry.Link`
- `..core.telemetry.Scope`
- `..core.telemetry.SpanKind`
- `..core.telemetry.saleor_attributes`
- `..core.telemetry.tracer`
- `..core.tracing.traced_atomic_transaction`
- `..discount.models.Promotion`
- `..giftcard.models.GiftCard`
- `..graphql.account.dataloaders.UserByEmailLoader`
- `..graphql.plugins.dataloaders.AnonymousPluginManagerLoader`
- `..graphql.site.dataloaders.get_site_promise`
- `..order.models.Order`
- `..order.models.OrderLine`
- `..order.search.prepare_order_search_vector_value`
- `..page.models.Page`
- `..permission.models.Permission`
- `..plugins.manager.get_plugins_manager`
- `..private_storage`
- `..product.models.Product`
- `..product.models.ProductVariant`
- `..schedulers.customschedule.CustomSchedule`
- `..site.PasswordLoginMode`
- `.auth.get_token_from_request`
- `.db.filters.PostgresILike`
- `.jwt.JWT_REFRESH_TOKEN_COOKIE_NAME`
- `.jwt.jwt_decode_with_exception_handler`
- `.jwt_manager.get_jwt_manager`
- `.models.EventDelivery`
- `.models.EventPayload`
- `.postgres.FlatConcatSearchVector`
- `.utils.build_absolute_uri`
- `.utils.get_domain`
- `.utils.json_serializer.CustomJsonEncoder`
- `.utils.text.strip_accents`
- `saleor.account.models.User`
- `saleor.settings`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `d35aa0292710` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
