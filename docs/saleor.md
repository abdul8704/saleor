## Purpose

`saleor` (`saleor`) groups 26 source file(s) exposing 21 top-level declaration(s).

## Public surface

**`saleor/__init__.py`**

- `PatchedSubscriberExecutionContext` (class) — [saleor/__init__.py:7]
- `reset` (function) — [saleor/__init__.py:14]

**`saleor/celeryconf.py`**

- `setup_celery_logging` (function) — [saleor/celeryconf.py:15]
- `init_celery_telemetry` (function) — [saleor/celeryconf.py:26]

**`saleor/patch_local.py`**

- `patch_local` (function) — [saleor/patch_local.py:46]

**`saleor/seo/models.py`**

- `SeoModel` (class) — [saleor/seo/models.py:7]
- `Meta` (class) — [saleor/seo/models.py:15]
- `SeoModelTranslation` (class) — [saleor/seo/models.py:19]
- `Meta` (class) — [saleor/seo/models.py:27]
- `get_translated_keys` (function) — [saleor/seo/models.py:30]
- `SeoModelTranslationWithSlug` (class) — [saleor/seo/models.py:37]
- `Meta` (class) — [saleor/seo/models.py:40]
- `get_translated_keys` (function) — [saleor/seo/models.py:43]

**`saleor/settings.py`**

- `get_list` (function) — [saleor/settings.py:55]
- `get_bool_from_env` (function) — [saleor/settings.py:59]
- `get_url_from_env` (function) — [saleor/settings.py:70]
- `SENTRY_INIT` (function) — [saleor/settings.py:843]

**`saleor/translations/error_codes.py`**

- `AttributeTranslateErrorCode` (class) — [saleor/translations/error_codes.py:4]
- `AttributeValueTranslateErrorCode` (class) — [saleor/translations/error_codes.py:11]
- `ProductTranslateErrorCode` (class) — [saleor/translations/error_codes.py:18]
- `ProductVariantTranslateErrorCode` (class) — [saleor/translations/error_codes.py:25]

## How it works

The module's files, as provided to this run:

- `saleor/__init__.py` (23 lines)
- `saleor/celeryconf.py` (70 lines)
- `saleor/__main__.py` (7 lines)
- `saleor/json_schemas/CheckoutCalculateTaxes.json` (108 lines)
- `saleor/json_schemas/CheckoutFilterShippingMethods.json` (34 lines)
- `saleor/json_schemas/ListStoredPaymentMethods.json` (127 lines)
- `saleor/json_schemas/OrderCalculateTaxes.json` (108 lines)
- `saleor/json_schemas/OrderFilterShippingMethods.json` (34 lines)
- `saleor/json_schemas/PaymentGatewayInitializeSession.json` (42 lines)
- `saleor/json_schemas/PaymentGatewayInitializeTokenizationSession.json` (128 lines)
- `saleor/json_schemas/ShippingListMethodsForCheckout.json` (93 lines)
- `saleor/json_schemas/ShippingListMethodsForOrder.json` (93 lines)
- `saleor/json_schemas/StoredPaymentMethodDeleteRequested.json` (38 lines)
- `saleor/json_schemas/TransactionCancelationRequested.json` (192 lines)
- `saleor/json_schemas/TransactionChargeRequested.json` (192 lines)
- `saleor/json_schemas/TransactionInitializeSession.json` (487 lines)
- `saleor/json_schemas/TransactionProcessSession.json` (487 lines)
- `saleor/json_schemas/TransactionRefundRequested.json` (192 lines)
- `saleor/patch_local.py` (53 lines)
- `saleor/seo/__init__.py` (1 lines)
- `saleor/seo/models.py` (47 lines)
- `saleor/settings.py` (1293 lines)
- `saleor/static/populatedb_data.json` (10417 lines)
- `saleor/translations/__init__.py` (1 lines)
- `saleor/translations/error_codes.py` (29 lines)
- `saleor/urls.py` (63 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/core/utils`, `saleor/product`, `saleor/graphql`
- Imported by: `saleor/app`, `saleor/core`, `.semgrep`, `saleor/asgi`, `saleor/graphql`, `saleor/webhook`

Internal dependencies named in the source:

- `..PatchedSubscriberExecutionContext`
- `..__version__`
- `..core.utils.translations.Translation`
- `.account.i18n_rules_override.i18n_rules_override`
- `.celeryconf.app`
- `.core.cleaners.html.HtmlCleanerSettings`
- `.core.db.patch.patch_db`
- `.core.languages.LANGUAGES`
- `.core.rlimit.validate_and_set_rlimit`
- `.core.telemetry.initialize_telemetry`
- `.core.views`
- `.core.views.jwks`
- `.core.views.serve_media_view`
- `.graphql.api.backend`
- `.graphql.api.schema`
- `.graphql.promise.patch_promise`
- `.graphql.views.GraphQLView`
- `.patch_local.patch_local`
- `.plugins.discover_plugins_modules`
- `.thumbnail.views.handle_original_image`
- `.thumbnail.views.handle_thumbnail`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `0313abcfaf71` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
