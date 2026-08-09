## Purpose

`saleor/graphql/app` (`saleor/graphql/app`) groups 8 source file(s) exposing 114 top-level declaration(s).

## Public surface

**`saleor/graphql/app/enums.py`**

- `description` (function) — [saleor/graphql/app/enums.py:11]
- `breaker_description` (function) — [saleor/graphql/app/enums.py:28]
- `CircuitBreakerState` (class) — [saleor/graphql/app/enums.py:48]
- `AppProblemDismissedBy` (class) — [saleor/graphql/app/enums.py:69]

**`saleor/graphql/app/filters.py`**

- `filter_app_search` (function) — [saleor/graphql/app/filters.py:11]
- `filter_app_type` (function) — [saleor/graphql/app/filters.py:17]
- `filter_app_extension_mount_name` (function) — [saleor/graphql/app/filters.py:23]
- `filter_app_extension_target_name` (function) — [saleor/graphql/app/filters.py:29]
- `AppFilter` (class) — [saleor/graphql/app/filters.py:35]
- `Meta` (class) — [saleor/graphql/app/filters.py:40]
- `AppExtensionFilter` (class) — [saleor/graphql/app/filters.py:45]
- `Meta` (class) — [saleor/graphql/app/filters.py:56]

**`saleor/graphql/app/resolvers.py`**

- `resolve_apps_installations` (function) — [saleor/graphql/app/resolvers.py:18]
- `resolve_apps` (function) — [saleor/graphql/app/resolvers.py:24]
- `resolve_access_token_for_app` (function) — [saleor/graphql/app/resolvers.py:32]
- `resolve_access_token_for_app_extension` (function) — [saleor/graphql/app/resolvers.py:50]
- `resolve_app` (function) — [saleor/graphql/app/resolvers.py:73]
- `resolve_app_extensions` (function) — [saleor/graphql/app/resolvers.py:84]
- `resolve_app_extension_url` (function) — [saleor/graphql/app/resolvers.py:96]

**`saleor/graphql/app/schema.py`**

- `AppFilterInput` (class) — [saleor/graphql/app/schema.py:48]
- `Meta` (class) — [saleor/graphql/app/schema.py:49]
- `AppExtensionFilterInput` (class) — [saleor/graphql/app/schema.py:54]
- `Meta` (class) — [saleor/graphql/app/schema.py:55]
- `AppQueries` (class) — [saleor/graphql/app/schema.py:60]
- `resolve_apps_installations` (function) — [saleor/graphql/app/schema.py:125]
- `resolve_apps` (function) — [saleor/graphql/app/schema.py:129]
- `resolve_app` (function) — [saleor/graphql/app/schema.py:138]
- `resolve_app_extensions` (function) — [saleor/graphql/app/schema.py:150]
- `resolve_app_extension` (function) — [saleor/graphql/app/schema.py:160]
- `app_is_active` (function) — [saleor/graphql/app/schema.py:161]
- `is_active` (function) — [saleor/graphql/app/schema.py:162]
- `AppMutations` (class) — [saleor/graphql/app/schema.py:178]

**`saleor/graphql/app/sorters.py`**

- `AppSortField` (class) — [saleor/graphql/app/sorters.py:5]
- `Meta` (class) — [saleor/graphql/app/sorters.py:9]
- `description` (function) — [saleor/graphql/app/sorters.py:13]
- `AppSortingInput` (class) — [saleor/graphql/app/sorters.py:20]
- `Meta` (class) — [saleor/graphql/app/sorters.py:21]

**`saleor/graphql/app/types.py`**

- `has_required_permission` (function) — [saleor/graphql/app/types.py:84]
- `check_permission_for_access_to_meta` (function) — [saleor/graphql/app/types.py:92]
- `has_access_to_app_public_meta` (function) — [saleor/graphql/app/types.py:100]
- `AppManifestExtension` (class) — [saleor/graphql/app/types.py:115]
- `Meta` (class) — [saleor/graphql/app/types.py:153]
- `resolve_url` (function) — [saleor/graphql/app/types.py:157]
- `resolve_target_name` (function) — [saleor/graphql/app/types.py:162]
- `resolve_mount_name` (function) — [saleor/graphql/app/types.py:166]
- `resolve_settings` (function) — [saleor/graphql/app/types.py:170]
- `HttpMethod` (class) — [saleor/graphql/app/types.py:174]
- `AppExtension` (class) — [saleor/graphql/app/types.py:179]
- `Meta` (class) — [saleor/graphql/app/types.py:190]
- `resolve_url` (function) — [saleor/graphql/app/types.py:196]
- `resolve_mount_name` (function) — [saleor/graphql/app/types.py:209]
- `resolve_target_name` (function) — [saleor/graphql/app/types.py:213]
- `resolve_app` (function) — [saleor/graphql/app/types.py:218]
- `resolve_permissions` (function) — [saleor/graphql/app/types.py:241]
- `resolve_access_token` (function) — [saleor/graphql/app/types.py:248]
- `resolve_settings` (function) — [saleor/graphql/app/types.py:255]
- `AppExtensionCountableConnection` (class) — [saleor/graphql/app/types.py:283]
- `Meta` (class) — [saleor/graphql/app/types.py:284]
- `AppManifestWebhook` (class) — [saleor/graphql/app/types.py:289]
- `Meta` (class) — [saleor/graphql/app/types.py:306]
- `resolve_async_events` (function) — [saleor/graphql/app/types.py:310]
- `resolve_sync_events` (function) — [saleor/graphql/app/types.py:314]
- `resolve_target_url` (function) — [saleor/graphql/app/types.py:318]
- `AppManifestRequiredSaleorVersion` (class) — [saleor/graphql/app/types.py:322]
- `Meta` (class) — [saleor/graphql/app/types.py:332]
- `AppManifestBrandLogo` (class) — [saleor/graphql/app/types.py:336]
- `Meta` (class) — [saleor/graphql/app/types.py:343]
- `resolve_default` (function) — [saleor/graphql/app/types.py:348]
- `AppBrandLogo` (class) — [saleor/graphql/app/types.py:372]
- `Meta` (class) — [saleor/graphql/app/types.py:379]
- `resolve_default` (function) — [saleor/graphql/app/types.py:384]
- `AppBrand` (class) — [saleor/graphql/app/types.py:421]
- `Meta` (class) — [saleor/graphql/app/types.py:428]
- `resolve_logo` (function) — [saleor/graphql/app/types.py:433]
- `AppManifestBrand` (class) — [saleor/graphql/app/types.py:437]
- `Meta` (class) — [saleor/graphql/app/types.py:444]
- `Manifest` (class) — [saleor/graphql/app/types.py:449]
- _…and 34 more in this file_

**`saleor/graphql/app/utils.py`**

- `ensure_can_manage_permissions` (function) — [saleor/graphql/app/utils.py:10]
- `ensure_app_permissions_allowed` (function) — [saleor/graphql/app/utils.py:28]
- `validate_app_is_not_removed` (function) — [saleor/graphql/app/utils.py:52]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/app/__init__.py` (1 lines)
- `saleor/graphql/app/enums.py` (88 lines)
- `saleor/graphql/app/filters.py` (58 lines)
- `saleor/graphql/app/resolvers.py` (111 lines)
- `saleor/graphql/app/schema.py` (199 lines)
- `saleor/graphql/app/sorters.py` (24 lines)
- `saleor/graphql/app/types.py` (860 lines)
- `saleor/graphql/app/utils.py` (65 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...app.error_codes`
- `...app.models`
- `...app.models.App`
- `...app.types.AppType`
- `...app.types.DEFAULT_APP_TARGET`
- `...app.types.POPUP_EXTENSION_TARGET`
- `...core.exceptions.PermissionDenied`
- `...core.jwt.JWT_THIRDPARTY_ACCESS_TYPE`
- `...core.utils.build_absolute_uri`
- `...permission.auth_filters.AuthorizationFilters`
- `...permission.auth_filters.is_staff_user`
- `...permission.enums.AccountPermissions`
- `...permission.enums.AppPermission`
- `...permission.utils.message_one_of_permissions_required`
- `...thumbnail.PIL_IDENTIFIER_TO_MIME_TYPE`
- `..account.dataloaders.UserByUserIdLoader`
- `..account.utils.get_out_of_scope_permissions`
- `..account.utils.is_owner_or_has_one_of_perms`
- `..core.ResolveInfo`
- `..core.SaleorContext`
- `..core.connection.CountableConnection`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.descriptions.ADDED_IN_322`
- `..core.descriptions.ADDED_IN_323`
- `..core.doc_category.DOC_CATEGORY_APPS`
- `..core.enums.AppErrorCode`
- `..core.enums.to_enum`
- `..core.federation.federated_entity`
- `..core.federation.resolve_federation_references`
- `..core.fields.FilterConnectionField`
- `..core.fields.PermissionsField`
- `..core.filters.EnumFilter`
- `..core.filters.FilterInputObjectType`
- `..core.filters.ListObjectTypeFilter`
- `..core.scalars.DateTime`
- `..core.scalars.JSON`
- `..core.scalars.PositiveInt`
- `..core.types.BaseEnum`
- `..core.types.NonNullList`
- `..core.types.SortInputObjectType`
- `..core.utils.from_global_id_or_error`
- `..meta.types.ObjectWithMetadata`
- `..utils.format_permissions_for_display`
- `..utils.get_user_or_app_from_context`
- `..utils.requestor_is_superuser`
- `..webhook.dataloaders.WebhooksByAppIdLoader`
- `..webhook.enums.WebhookEventTypeAsyncEnum`
- `..webhook.enums.WebhookEventTypeSyncEnum`
- `..webhook.types.Webhook`
- `.dataloaders.AppByIdLoader`
- `.dataloaders.AppExtensionByIdLoader`
- `.dataloaders.app_promise_callback`
- `.enums.AppTypeEnum`
- `.filters.AppExtensionFilter`
- `.filters.AppFilter`
- `.resolvers.resolve_apps`
- `.sorters.AppSortingInput`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b3ae1b0bac15` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
