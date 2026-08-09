## Purpose

`saleor/graphql/checkout/dataloaders` (`saleor/graphql/checkout/dataloaders`) groups 7 source file(s) exposing 46 top-level declaration(s).

## Public surface

**`saleor/graphql/checkout/dataloaders/calculations.py`**

- `CheckoutPriceCalculationByCheckoutIdAndWebhookSyncAndForceStatusUpdateLoader` (class) — [saleor/graphql/checkout/dataloaders/calculations.py:18]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/calculations.py:25]
- `with_checkout_details` (function) — [saleor/graphql/checkout/dataloaders/calculations.py:36]
- `calculate_prices` (function) — [saleor/graphql/checkout/dataloaders/calculations.py:41]

**`saleor/graphql/checkout/dataloaders/checkout_delivery.py`**

- `CheckoutDeliveryByIdLoader` (class) — [saleor/graphql/checkout/dataloaders/checkout_delivery.py:14]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/checkout_delivery.py:17]
- `CheckoutDeliveriesOnlyValidByCheckoutIdAndWebhookSyncLoader` (class) — [saleor/graphql/checkout/dataloaders/checkout_delivery.py:24]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/checkout_delivery.py:31]
- `refresh_delivery_dataloader` (function) — [saleor/graphql/checkout/dataloaders/checkout_delivery.py:37]
- `with_checkout_infos` (function) — [saleor/graphql/checkout/dataloaders/checkout_delivery.py:45]

**`saleor/graphql/checkout/dataloaders/checkout_infos.py`**

- `CheckoutInfoByCheckoutTokenLoader` (class) — [saleor/graphql/checkout/dataloaders/checkout_infos.py:33]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/checkout_infos.py:36]
- `with_checkout` (function) — [saleor/graphql/checkout/dataloaders/checkout_infos.py:37]
- `with_channel` (function) — [saleor/graphql/checkout/dataloaders/checkout_infos.py:47]
- `with_checkout_info` (function) — [saleor/graphql/checkout/dataloaders/checkout_infos.py:87]
- `CheckoutLinesInfoByCheckoutTokenLoader` (class) — [saleor/graphql/checkout/dataloaders/checkout_infos.py:190]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/checkout_infos.py:195]
- `with_checkout_lines` (function) — [saleor/graphql/checkout/dataloaders/checkout_infos.py:196]
- `with_variants_products_collections` (function) — [saleor/graphql/checkout/dataloaders/checkout_infos.py:213]

**`saleor/graphql/checkout/dataloaders/models.py`**

- `CheckoutByTokenLoader` (class) — [saleor/graphql/checkout/dataloaders/models.py:11]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/models.py:14]
- `CheckoutByUserLoader` (class) — [saleor/graphql/checkout/dataloaders/models.py:19]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/models.py:22]
- `CheckoutByUserAndChannelLoader` (class) — [saleor/graphql/checkout/dataloaders/models.py:32]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/models.py:35]
- `CheckoutLineByIdLoader` (class) — [saleor/graphql/checkout/dataloaders/models.py:55]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/models.py:58]
- `CheckoutLinesByCheckoutTokenLoader` (class) — [saleor/graphql/checkout/dataloaders/models.py:65]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/models.py:68]
- `CheckoutMetadataByCheckoutIdLoader` (class) — [saleor/graphql/checkout/dataloaders/models.py:78]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/models.py:81]
- `TransactionItemsByCheckoutIDLoader` (class) — [saleor/graphql/checkout/dataloaders/models.py:88]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/models.py:91]

**`saleor/graphql/checkout/dataloaders/problems.py`**

- `CheckoutLinesProblemsByCheckoutIdLoader` (class) — [saleor/graphql/checkout/dataloaders/problems.py:36]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/problems.py:41]
- `get_variants_stocks` (function) — [saleor/graphql/checkout/dataloaders/problems.py:131]
- `CheckoutProblemsByCheckoutIdDataloader` (class) — [saleor/graphql/checkout/dataloaders/problems.py:158]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/problems.py:163]

**`saleor/graphql/checkout/dataloaders/promotion_rule_infos.py`**

- `VariantPromotionRuleInfoByCheckoutLineIdLoader` (class) — [saleor/graphql/checkout/dataloaders/promotion_rule_infos.py:23]
- `batch_load` (function) — [saleor/graphql/checkout/dataloaders/promotion_rule_infos.py:28]
- `with_checkout_lines` (function) — [saleor/graphql/checkout/dataloaders/promotion_rule_infos.py:29]
- `with_checkouts` (function) — [saleor/graphql/checkout/dataloaders/promotion_rule_infos.py:30]
- `with_channel_listings` (function) — [saleor/graphql/checkout/dataloaders/promotion_rule_infos.py:37]
- `with_channel_listing_promotion_rules` (function) — [saleor/graphql/checkout/dataloaders/promotion_rule_infos.py:38]
- `with_promotion_rules` (function) — [saleor/graphql/checkout/dataloaders/promotion_rule_infos.py:59]
- `with_promotion_translations` (function) — [saleor/graphql/checkout/dataloaders/promotion_rule_infos.py:71]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/checkout/dataloaders/__init__.py` (33 lines)
- `saleor/graphql/checkout/dataloaders/calculations.py` (64 lines)
- `saleor/graphql/checkout/dataloaders/checkout_delivery.py` (60 lines)
- `saleor/graphql/checkout/dataloaders/checkout_infos.py` (352 lines)
- `saleor/graphql/checkout/dataloaders/models.py` (100 lines)
- `saleor/graphql/checkout/dataloaders/problems.py` (211 lines)
- `saleor/graphql/checkout/dataloaders/promotion_rule_infos.py` (195 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....app.models.App`
- `....checkout.calculations.fetch_checkout_data`
- `....checkout.delivery_context.get_or_fetch_checkout_deliveries`
- `....checkout.fetch.CheckoutInfo`
- `....checkout.fetch.CheckoutLineInfo`
- `....checkout.models.Checkout`
- `....checkout.models.CheckoutDelivery`
- `....checkout.models.CheckoutLine`
- `....checkout.models.CheckoutMetadata`
- `....core.db.connection.allow_writer_in_context`
- `....discount.VoucherType`
- `....discount.interface.VariantPromotionRuleInfo`
- `....discount.utils.voucher.attach_voucher_to_line_info`
- `....payment.models.TransactionItem`
- `....product.models.ProductChannelListing`
- `....warehouse.models.Stock`
- `...account.dataloaders.AddressByIdLoader`
- `...account.dataloaders.UserByUserIdLoader`
- `...app.dataloaders.utils.get_app_promise`
- `...channel.dataloaders.by_self.ChannelByIdLoader`
- `...core.dataloaders.DataLoader`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...plugins.dataloaders.plugin_manager_promise`
- `...site.dataloaders.get_site_promise`
- `...tax.dataloaders.TaxClassByVariantIdLoader`
- `...tax.dataloaders.TaxConfigurationByChannelId`
- `...utils.get_user_or_app_from_context`
- `...warehouse.dataloaders.WarehouseByIdLoader`
- `.checkout_delivery.CheckoutDeliveryByIdLoader`
- `.checkout_infos.CheckoutInfoByCheckoutTokenLoader`
- `.models.CheckoutByTokenLoader`
- `.models.CheckoutLineByIdLoader`
- `.models.CheckoutLinesByCheckoutTokenLoader`
- `.promotion_rule_infos.VariantPromotionRuleInfoByCheckoutLineIdLoader`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `91c1ae451610` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
