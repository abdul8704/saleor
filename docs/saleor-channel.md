## Purpose

`saleor/channel` (`saleor/channel`) groups 7 source file(s) exposing 10 top-level declaration(s).

## Public surface

**`saleor/channel/__init__.py`**

- `AllocationStrategy` (class) — [saleor/channel/__init__.py:1]
- `MarkAsPaidStrategy` (class) — [saleor/channel/__init__.py:19]
- `TransactionFlowStrategy` (class) — [saleor/channel/__init__.py:39]

**`saleor/channel/error_codes.py`**

- `ChannelErrorCode` (class) — [saleor/channel/error_codes.py:4]

**`saleor/channel/exceptions.py`**

- `ChannelNotDefined` (class) — [saleor/channel/exceptions.py:1]
- `NoDefaultChannel` (class) — [saleor/channel/exceptions.py:8]

**`saleor/channel/models.py`**

- `Channel` (class) — [saleor/channel/models.py:12]
- `Meta` (class) — [saleor/channel/models.py:77]

**`saleor/channel/tasks/saleor3_22.py`**

- `set_automatic_completion_delay_task` (function) — [saleor/channel/tasks/saleor3_22.py:8]

**`saleor/channel/utils.py`**

- `get_default_channel` (function) — [saleor/channel/utils.py:15]

## How it works

The module's files, as provided to this run:

- `saleor/channel/__init__.py` (49 lines)
- `saleor/channel/error_codes.py` (13 lines)
- `saleor/channel/exceptions.py` (12 lines)
- `saleor/channel/models.py` (88 lines)
- `saleor/channel/tasks/__init__.py` (1 lines)
- `saleor/channel/tasks/saleor3_22.py` (12 lines)
- `saleor/channel/utils.py` (47 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....celeryconf.app`
- `....core.db.connection.allow_writer`
- `...models.Channel`
- `..AllocationStrategy`
- `..MarkAsPaidStrategy`
- `..TransactionFlowStrategy`
- `..core.models.ModelWithMetadata`
- `..permission.enums.ChannelPermissions`
- `.exceptions.ChannelNotDefined`
- `.exceptions.NoDefaultChannel`
- `.models.Channel`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `160b5e33b93c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
