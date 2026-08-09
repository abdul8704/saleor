## Purpose

`saleor/graphql/channel/dataloaders` (`saleor/graphql/channel/dataloaders`) groups 5 source file(s) exposing 18 top-level declaration(s).

## Public surface

**`saleor/graphql/channel/dataloaders/by_checkout.py`**

- `ChannelByCheckoutIDLoader` (class) — [saleor/graphql/channel/dataloaders/by_checkout.py:9]
- `batch_load` (function) — [saleor/graphql/channel/dataloaders/by_checkout.py:12]
- `with_checkouts` (function) — [saleor/graphql/channel/dataloaders/by_checkout.py:13]
- `with_channels` (function) — [saleor/graphql/channel/dataloaders/by_checkout.py:14]

**`saleor/graphql/channel/dataloaders/by_order.py`**

- `ChannelByOrderIdLoader` (class) — [saleor/graphql/channel/dataloaders/by_order.py:12]
- `batch_load` (function) — [saleor/graphql/channel/dataloaders/by_order.py:15]
- `with_orders` (function) — [saleor/graphql/channel/dataloaders/by_order.py:16]
- `with_channels` (function) — [saleor/graphql/channel/dataloaders/by_order.py:17]
- `ChannelWithHasOrdersByIdLoader` (class) — [saleor/graphql/channel/dataloaders/by_order.py:34]
- `batch_load` (function) — [saleor/graphql/channel/dataloaders/by_order.py:37]

**`saleor/graphql/channel/dataloaders/by_self.py`**

- `ChannelByIdLoader` (class) — [saleor/graphql/channel/dataloaders/by_self.py:5]
- `batch_load` (function) — [saleor/graphql/channel/dataloaders/by_self.py:8]
- `ChannelBySlugLoader` (class) — [saleor/graphql/channel/dataloaders/by_self.py:13]
- `batch_load` (function) — [saleor/graphql/channel/dataloaders/by_self.py:16]

**`saleor/graphql/channel/dataloaders/by_transaction.py`**

- `ChannelByTransactionIdLoader` (class) — [saleor/graphql/channel/dataloaders/by_transaction.py:12]
- `batch_load` (function) — [saleor/graphql/channel/dataloaders/by_transaction.py:15]
- `resolve_channels` (function) — [saleor/graphql/channel/dataloaders/by_transaction.py:48]
- `get_channel_for_transaction` (function) — [saleor/graphql/channel/dataloaders/by_transaction.py:56]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/channel/dataloaders/__init__.py` (1 lines)
- `saleor/graphql/channel/dataloaders/by_checkout.py` (28 lines)
- `saleor/graphql/channel/dataloaders/by_order.py` (46 lines)
- `saleor/graphql/channel/dataloaders/by_self.py` (20 lines)
- `saleor/graphql/channel/dataloaders/by_transaction.py` (70 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....channel.models.Channel`
- `....order.models.Order`
- `....payment.models.TransactionItem`
- `...checkout.dataloaders.CheckoutByTokenLoader`
- `...core.dataloaders.DataLoader`
- `...order.dataloaders.OrderByIdLoader`
- `.by_checkout.ChannelByCheckoutIDLoader`
- `.by_order.ChannelByOrderIdLoader`
- `.by_self.ChannelByIdLoader`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `72d218d7e6d5` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
