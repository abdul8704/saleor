## Purpose

`saleor/channel/tests` (`saleor/channel/tests`) groups 4 source file(s) exposing 8 top-level declaration(s).

## Public surface

**`saleor/channel/tests/fixtures/channel.py`**

- `channel_USD` (function) — [saleor/channel/tests/fixtures/channel.py:12]
- `other_channel_USD` (function) — [saleor/channel/tests/fixtures/channel.py:28]
- `channel_PLN` (function) — [saleor/channel/tests/fixtures/channel.py:42]
- `channel_JPY` (function) — [saleor/channel/tests/fixtures/channel.py:56]
- `channels_for_benchmark` (function) — [saleor/channel/tests/fixtures/channel.py:71]

**`saleor/channel/tests/test_utils.py`**

- `test_get_default_channel_without_channels` (function) — [saleor/channel/tests/test_utils.py:9]
- `test_get_default_channel_with_one_channels` (function) — [saleor/channel/tests/test_utils.py:14]
- `test_get_default_channel_with_many_channels` (function) — [saleor/channel/tests/test_utils.py:22]

## How it works

The module's files, as provided to this run:

- `saleor/channel/tests/fixtures/channel.py` (95 lines)
- `saleor/channel/tests/__init__.py` (1 lines)
- `saleor/channel/tests/fixtures/__init__.py` (1 lines)
- `saleor/channel/tests/test_utils.py` (24 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: `saleor/graphql/product/bulk_mutations`, `saleor/checkout/tests`

Internal dependencies named in the source:

- `....channel.AllocationStrategy`
- `....channel.models.Channel`
- `....graphql.channel.tests.benchmark.CHANNEL_COUNT_IN_BENCHMARKS`
- `....tax.tests.fixtures.utils.create_channel_tax_configuration`
- `....warehouse.models.Warehouse`
- `..exceptions.ChannelNotDefined`
- `..exceptions.NoDefaultChannel`
- `..utils.DEPRECATION_WARNING_MESSAGE`
- `..utils.get_default_channel`
- `.channel.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `6d5ec297ee59` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
