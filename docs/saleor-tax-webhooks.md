## Purpose

`saleor/tax/webhooks` (`saleor/tax/webhooks`) groups 3 source file(s) exposing 6 top-level declaration(s).

## Public surface

**`saleor/tax/webhooks/parser.py`**

- `parse_tax_data` (function) — [saleor/tax/webhooks/parser.py:14]

**`saleor/tax/webhooks/shared.py`**

- `get_taxes` (function) — [saleor/tax/webhooks/shared.py:24]
- `get_taxes_for_app_identifier` (function) — [saleor/tax/webhooks/shared.py:50]
- `process_response` (function) — [saleor/tax/webhooks/shared.py:88]
- `get_taxes_from_all_webhooks` (function) — [saleor/tax/webhooks/shared.py:98]
- `process_responses` (function) — [saleor/tax/webhooks/shared.py:127]

## How it works

The module's files, as provided to this run:

- `saleor/tax/webhooks/parser.py` (52 lines)
- `saleor/tax/webhooks/__init__.py` (1 lines)
- `saleor/tax/webhooks/shared.py` (139 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql`
- Imported by: `saleor/plugins`

Internal dependencies named in the source:

- `...account.models.User`
- `...app.models.App`
- `...checkout.models.Checkout`
- `...core.taxes.TAX_ERROR_FIELD_LENGTH`
- `...core.taxes.TaxData`
- `...core.taxes.TaxDataError`
- `...core.taxes.TaxLineData`
- `...core.utils.text.safe_truncate`
- `...order.models.Order`
- `...webhook.response_schemas.taxes.CalculateTaxesSchema`
- `...webhook.response_schemas.utils.helpers.parse_validation_error`
- `...webhook.utils.get_webhooks_for_event`
- `.parser.parse_tax_data`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b9cd1b108c28` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
