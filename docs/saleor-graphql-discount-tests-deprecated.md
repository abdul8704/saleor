## Purpose

`saleor/graphql/discount/tests/deprecated` (`saleor/graphql/discount/tests/deprecated`) groups 5 source file(s) exposing 18 top-level declaration(s).

## Public surface

**`saleor/graphql/discount/tests/deprecated/test_discount.py`**

- `test_sales_with_sorting_and_without_channel` (function) — [saleor/graphql/discount/tests/deprecated/test_discount.py:20]
- `test_query_vouchers_with_sort` (function) — [saleor/graphql/discount/tests/deprecated/test_discount.py:66]
- `test_filter_sales_by_query` (function) — [saleor/graphql/discount/tests/deprecated/test_discount.py:88]
- `test_filter_vouchers_by_query` (function) — [saleor/graphql/discount/tests/deprecated/test_discount.py:119]

**`saleor/graphql/discount/tests/deprecated/test_voucher_create.py`**

- `test_create_voucher` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher_create.py:53]
- `test_create_voucher_trigger_webhook` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher_create.py:92]
- `test_create_voucher_with_empty_code` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher_create.py:154]
- `test_create_voucher_with_existing_gift_card_code` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher_create.py:182]
- `test_create_voucher_with_existing_voucher_code` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher_create.py:214]
- `test_create_voucher_with_enddate_before_startdate` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher_create.py:246]

**`saleor/graphql/discount/tests/deprecated/test_voucher_update.py`**

- `test_update_voucher` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher_update.py:41]
- `test_update_voucher_trigger_webhook` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher_update.py:72]
- `test_update_voucher_return_error_when_multiple_codes_already_exists` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher_update.py:120]

**`saleor/graphql/discount/tests/deprecated/test_voucher.py`**

- `test_staff_query_voucher` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher.py:21]
- `test_query_voucher_by_app` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher.py:31]
- `test_query_voucher_by_customer` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher.py:41]
- `test_staff_query_voucher_by_invalid_id` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher.py:47]
- `test_staff_query_voucher_with_invalid_object_type` (function) — [saleor/graphql/discount/tests/deprecated/test_voucher.py:66]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/discount/tests/deprecated/__init__.py` (1 lines)
- `saleor/graphql/discount/tests/deprecated/test_discount.py` (151 lines)
- `saleor/graphql/discount/tests/deprecated/test_voucher_create.py` (276 lines)
- `saleor/graphql/discount/tests/deprecated/test_voucher_update.py` (145 lines)
- `saleor/graphql/discount/tests/deprecated/test_voucher.py` (79 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....channel.utils.DEPRECATION_WARNING_MESSAGE`
- `.....core.utils.json_serializer.CustomJsonEncoder`
- `.....discount.DiscountValueType`
- `.....discount.VoucherType`
- `.....discount.error_codes.DiscountErrorCode`
- `.....discount.models.Promotion`
- `.....discount.models.Voucher`
- `.....discount.models.VoucherCode`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.payloads.generate_meta`
- `.....webhook.payloads.generate_requestor`
- `....tests.utils.get_graphql_content`
- `...enums.DiscountValueTypeEnum`
- `...enums.VoucherTypeEnum`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `32663c9eedef` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
