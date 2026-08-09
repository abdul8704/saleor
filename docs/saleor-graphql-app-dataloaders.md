## Purpose

`saleor/graphql/app/dataloaders` (`saleor/graphql/app/dataloaders`) groups 8 source file(s) exposing 31 top-level declaration(s).

## Public surface

**`saleor/graphql/app/dataloaders/app_extension.py`**

- `AppExtensionByIdLoader` (class) — [saleor/graphql/app/dataloaders/app_extension.py:7]
- `batch_load` (function) — [saleor/graphql/app/dataloaders/app_extension.py:10]
- `AppExtensionByAppIdLoader` (class) — [saleor/graphql/app/dataloaders/app_extension.py:17]
- `batch_load` (function) — [saleor/graphql/app/dataloaders/app_extension.py:20]

**`saleor/graphql/app/dataloaders/app_problems.py`**

- `AppProblemsByAppIdLoader` (class) — [saleor/graphql/app/dataloaders/app_problems.py:7]
- `batch_load` (function) — [saleor/graphql/app/dataloaders/app_problems.py:10]

**`saleor/graphql/app/dataloaders/app_tokens.py`**

- `AppTokensByAppIdLoader` (class) — [saleor/graphql/app/dataloaders/app_tokens.py:7]
- `batch_load` (function) — [saleor/graphql/app/dataloaders/app_tokens.py:10]

**`saleor/graphql/app/dataloaders/app.py`**

- `create_app_cache_key_from_token` (function) — [saleor/graphql/app/dataloaders/app.py:15]
- `AppByIdLoader` (class) — [saleor/graphql/app/dataloaders/app.py:20]
- `batch_load` (function) — [saleor/graphql/app/dataloaders/app.py:23]
- `TokenInfo` (class) — [saleor/graphql/app/dataloaders/app.py:33]
- `last_4` (function) — [saleor/graphql/app/dataloaders/app.py:38]
- `cache_key` (function) — [saleor/graphql/app/dataloaders/app.py:42]
- `AppByTokenLoader` (class) — [saleor/graphql/app/dataloaders/app.py:49]
- `get_and_cache_app_id` (function) — [saleor/graphql/app/dataloaders/app.py:52]
- `remove_not_valid_tokens_from_cache` (function) — [saleor/graphql/app/dataloaders/app.py:67]
- `batch_load` (function) — [saleor/graphql/app/dataloaders/app.py:76]
- `ActiveAppByIdLoader` (class) — [saleor/graphql/app/dataloaders/app.py:116]
- `batch_load` (function) — [saleor/graphql/app/dataloaders/app.py:119]

**`saleor/graphql/app/dataloaders/apps.py`**

- `ActiveAppsByAppIdentifierLoader` (class) — [saleor/graphql/app/dataloaders/apps.py:9]
- `batch_load` (function) — [saleor/graphql/app/dataloaders/apps.py:12]
- `AppsByEventTypeLoader` (class) — [saleor/graphql/app/dataloaders/apps.py:22]
- `batch_load` (function) — [saleor/graphql/app/dataloaders/apps.py:25]
- `return_apps_for_webhooks` (function) — [saleor/graphql/app/dataloaders/apps.py:29]
- `return_apps` (function) — [saleor/graphql/app/dataloaders/apps.py:35]

**`saleor/graphql/app/dataloaders/thumbnail.py`**

- `ThumbnailByAppIdSizeAndFormatLoader` (class) — [saleor/graphql/app/dataloaders/thumbnail.py:4]
- `ThumbnailByAppInstallationIdSizeAndFormatLoader` (class) — [saleor/graphql/app/dataloaders/thumbnail.py:9]

**`saleor/graphql/app/dataloaders/utils.py`**

- `promise_app` (function) — [saleor/graphql/app/dataloaders/utils.py:13]
- `get_app_promise` (function) — [saleor/graphql/app/dataloaders/utils.py:20]
- `app_promise_callback` (function) — [saleor/graphql/app/dataloaders/utils.py:30]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/app/dataloaders/__init__.py` (26 lines)
- `saleor/graphql/app/dataloaders/app_extension.py` (29 lines)
- `saleor/graphql/app/dataloaders/app_problems.py` (17 lines)
- `saleor/graphql/app/dataloaders/app_tokens.py` (17 lines)
- `saleor/graphql/app/dataloaders/app.py` (126 lines)
- `saleor/graphql/app/dataloaders/apps.py` (53 lines)
- `saleor/graphql/app/dataloaders/thumbnail.py` (13 lines)
- `saleor/graphql/app/dataloaders/utils.py` (37 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/plugins/openid_connect`, `saleor/core`, `saleor/core/utils`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....app.models.App`
- `....app.models.AppExtension`
- `....app.models.AppProblem`
- `....app.models.AppToken`
- `....core.auth.get_token_from_request`
- `....core.utils.lazyobjects.unwrap_lazy`
- `...core.SaleorContext`
- `...core.dataloaders.BaseThumbnailBySizeAndFormatLoader`
- `...core.dataloaders.DataLoader`
- `...webhook.dataloaders.models.WebhooksByEventTypeLoader`
- `.app.ActiveAppByIdLoader`
- `.app.AppByIdLoader`
- `.app.AppByTokenLoader`
- `.app_extension.AppExtensionByAppIdLoader`
- `.app_extension.AppExtensionByIdLoader`
- `.app_problems.AppProblemsByAppIdLoader`
- `.app_tokens.AppTokensByAppIdLoader`
- `.apps.ActiveAppsByAppIdentifierLoader`
- `.apps.AppsByEventTypeLoader`
- `.utils.app_promise_callback`
- `.utils.get_app_promise`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `9d495225083b` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
