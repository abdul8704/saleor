## Purpose

`saleor/graphql/checkout/mutations` (`saleor/graphql/checkout/mutations`) groups 21 source file(s) exposing 145 top-level declaration(s).

## Public surface

**`saleor/graphql/checkout/mutations/checkout_add_promo_code.py`**

- `CheckoutAddPromoCode` (class) — [saleor/graphql/checkout/mutations/checkout_add_promo_code.py:31]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_add_promo_code.py:36]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_add_promo_code.py:55]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_add_promo_code.py:68]

**`saleor/graphql/checkout/mutations/checkout_billing_address_update.py`**

- `CheckoutBillingAddressUpdate` (class) — [saleor/graphql/checkout/mutations/checkout_billing_address_update.py:24]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_billing_address_update.py:27]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_billing_address_update.py:55]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_billing_address_update.py:68]

**`saleor/graphql/checkout/mutations/checkout_complete.py`**

- `CheckoutComplete` (class) — [saleor/graphql/checkout/mutations/checkout_complete.py:49]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_complete.py:65]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_complete.py:107]
- `validate_checkout_addresses` (function) — [saleor/graphql/checkout/mutations/checkout_complete.py:178]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_complete.py:242]

**`saleor/graphql/checkout/mutations/checkout_create_from_order.py`**

- `CheckoutCreateFromOrderUnavailableVariant` (class) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:37]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:49]
- `CheckoutCreateFromOrderError` (class) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:53]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:58]
- `CheckoutCreateFromOrder` (class) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:62]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:69]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:75]
- `handle_not_available_variants_in_channel` (function) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:95]
- `handle_not_found_variants` (function) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:124]
- `handle_not_published_variants` (function) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:143]
- `handle_not_available_variants_for_purchase` (function) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:171]
- `handle_variants_exceeding_quantity_limit` (function) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:199]
- `exclude_lines_unavailable_to_purchase` (function) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:229]
- `clean_order_lines` (function) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:287]
- `create_checkout` (function) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:366]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_create_from_order.py:383]

**`saleor/graphql/checkout/mutations/checkout_create.py`**

- `CheckoutAddressValidationRules` (class) — [saleor/graphql/checkout/mutations/checkout_create.py:55]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_create.py:82]
- `CheckoutValidationRules` (class) — [saleor/graphql/checkout/mutations/checkout_create.py:86]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_create.py:99]
- `CheckoutLineInput` (class) — [saleor/graphql/checkout/mutations/checkout_create.py:103]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_create.py:133]
- `CheckoutCreateInput` (class) — [saleor/graphql/checkout/mutations/checkout_create.py:137]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_create.py:209]
- `CheckoutCreate` (class) — [saleor/graphql/checkout/mutations/checkout_create.py:213]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_create.py:224]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_create.py:229]
- `clean_checkout_lines` (function) — [saleor/graphql/checkout/mutations/checkout_create.py:254]
- `retrieve_shipping_address` (function) — [saleor/graphql/checkout/mutations/checkout_create.py:301]
- `retrieve_billing_address` (function) — [saleor/graphql/checkout/mutations/checkout_create.py:323]
- `clean_input` (function) — [saleor/graphql/checkout/mutations/checkout_create.py:345]
- `save` (function) — [saleor/graphql/checkout/mutations/checkout_create.py:472]
- `get_instance` (function) — [saleor/graphql/checkout/mutations/checkout_create.py:526]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_create.py:534]

**`saleor/graphql/checkout/mutations/checkout_customer_attach.py`**

- `CheckoutCustomerAttach` (class) — [saleor/graphql/checkout/mutations/checkout_customer_attach.py:25]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_customer_attach.py:28]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_customer_attach.py:52]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_customer_attach.py:69]

**`saleor/graphql/checkout/mutations/checkout_customer_detach.py`**

- `CheckoutCustomerDetach` (class) — [saleor/graphql/checkout/mutations/checkout_customer_detach.py:22]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_customer_detach.py:25]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_customer_detach.py:41]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_customer_detach.py:58]

**`saleor/graphql/checkout/mutations/checkout_customer_note_update.py`**

- `CheckoutCustomerNoteUpdate` (class) — [saleor/graphql/checkout/mutations/checkout_customer_note_update.py:15]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_customer_note_update.py:18]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_customer_note_update.py:27]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_customer_note_update.py:40]

**`saleor/graphql/checkout/mutations/checkout_delete.py`**

- `CheckoutDeleteError` (class) — [saleor/graphql/checkout/mutations/checkout_delete.py:17]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_delete.py:20]
- `CheckoutDelete` (class) — [saleor/graphql/checkout/mutations/checkout_delete.py:24]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_delete.py:25]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_delete.py:31]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_delete.py:38]

**`saleor/graphql/checkout/mutations/checkout_delivery_method_update.py`**

- `CheckoutDeliveryMethodUpdate` (class) — [saleor/graphql/checkout/mutations/checkout_delivery_method_update.py:41]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_delivery_method_update.py:44]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_delivery_method_update.py:63]
- `get_collection_point` (function) — [saleor/graphql/checkout/mutations/checkout_delivery_method_update.py:94]
- `get_checkout_delivery` (function) — [saleor/graphql/checkout/mutations/checkout_delivery_method_update.py:146]
- `get_delivery_method_data` (function) — [saleor/graphql/checkout/mutations/checkout_delivery_method_update.py:182]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_delivery_method_update.py:207]

**`saleor/graphql/checkout/mutations/checkout_email_update.py`**

- `CheckoutEmailUpdate` (class) — [saleor/graphql/checkout/mutations/checkout_email_update.py:20]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_email_update.py:23]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_email_update.py:40]
- `clean_email` (function) — [saleor/graphql/checkout/mutations/checkout_email_update.py:53]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_email_update.py:65]

**`saleor/graphql/checkout/mutations/checkout_language_code_update.py`**

- `CheckoutLanguageCodeUpdate` (class) — [saleor/graphql/checkout/mutations/checkout_language_code_update.py:20]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_language_code_update.py:23]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_language_code_update.py:42]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_language_code_update.py:55]

**`saleor/graphql/checkout/mutations/checkout_lines_add.py`**

- `CheckoutLinesAdd` (class) — [saleor/graphql/checkout/mutations/checkout_lines_add.py:44]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_lines_add.py:47]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_lines_add.py:71]
- `validate_checkout_lines` (function) — [saleor/graphql/checkout/mutations/checkout_lines_add.py:87]
- `process_lines_input` (function) — [saleor/graphql/checkout/mutations/checkout_lines_add.py:114]
- `clean_input` (function) — [saleor/graphql/checkout/mutations/checkout_lines_add.py:156]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_lines_add.py:214]
- `mark_search_vectors_as_dirty` (function) — [saleor/graphql/checkout/mutations/checkout_lines_add.py:276]

**`saleor/graphql/checkout/mutations/checkout_lines_delete.py`**

- `CheckoutLinesDelete` (class) — [saleor/graphql/checkout/mutations/checkout_lines_delete.py:23]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_lines_delete.py:26]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_lines_delete.py:41]
- `validate_lines` (function) — [saleor/graphql/checkout/mutations/checkout_lines_delete.py:53]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_lines_delete.py:88]

**`saleor/graphql/checkout/mutations/checkout_lines_update.py`**

- `CheckoutLineUpdateInput` (class) — [saleor/graphql/checkout/mutations/checkout_lines_update.py:33]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_lines_update.py:73]
- `CheckoutLinesUpdate` (class) — [saleor/graphql/checkout/mutations/checkout_lines_update.py:77]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_lines_update.py:80]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_lines_update.py:104]
- `validate_checkout_lines` (function) — [saleor/graphql/checkout/mutations/checkout_lines_update.py:117]
- `clean_input` (function) — [saleor/graphql/checkout/mutations/checkout_lines_update.py:146]
- `process_lines_input` (function) — [saleor/graphql/checkout/mutations/checkout_lines_update.py:182]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_lines_update.py:221]
- `mark_search_vectors_as_dirty` (function) — [saleor/graphql/checkout/mutations/checkout_lines_update.py:242]

**`saleor/graphql/checkout/mutations/checkout_remove_promo_code.py`**

- `CheckoutRemovePromoCode` (class) — [saleor/graphql/checkout/mutations/checkout_remove_promo_code.py:31]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_remove_promo_code.py:36]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_remove_promo_code.py:59]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_remove_promo_code.py:72]
- `clean_promo_code_id` (function) — [saleor/graphql/checkout/mutations/checkout_remove_promo_code.py:130]
- `remove_promo_code_by_id_or_error` (function) — [saleor/graphql/checkout/mutations/checkout_remove_promo_code.py:159]

**`saleor/graphql/checkout/mutations/checkout_shipping_address_update.py`**

- `CheckoutShippingAddressUpdate` (class) — [saleor/graphql/checkout/mutations/checkout_shipping_address_update.py:46]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_shipping_address_update.py:49]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_shipping_address_update.py:78]
- `process_checkout_lines` (function) — [saleor/graphql/checkout/mutations/checkout_shipping_address_update.py:91]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_shipping_address_update.py:121]

**`saleor/graphql/checkout/mutations/checkout_shipping_method_update.py`**

- `CheckoutShippingMethodUpdate` (class) — [saleor/graphql/checkout/mutations/checkout_shipping_method_update.py:39]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/checkout_shipping_method_update.py:42]
- `Meta` (class) — [saleor/graphql/checkout/mutations/checkout_shipping_method_update.py:61]
- `get_checkout_delivery` (function) — [saleor/graphql/checkout/mutations/checkout_shipping_method_update.py:109]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/checkout_shipping_method_update.py:142]

**`saleor/graphql/checkout/mutations/order_create_from_checkout.py`**

- `OrderCreateFromCheckoutError` (class) — [saleor/graphql/checkout/mutations/order_create_from_checkout.py:40]
- `Meta` (class) — [saleor/graphql/checkout/mutations/order_create_from_checkout.py:55]
- `OrderCreateFromCheckout` (class) — [saleor/graphql/checkout/mutations/order_create_from_checkout.py:59]
- `Arguments` (class) — [saleor/graphql/checkout/mutations/order_create_from_checkout.py:62]
- `Meta` (class) — [saleor/graphql/checkout/mutations/order_create_from_checkout.py:87]
- `check_permissions` (function) — [saleor/graphql/checkout/mutations/order_create_from_checkout.py:154]
- `validate_checkout` (function) — [saleor/graphql/checkout/mutations/order_create_from_checkout.py:163]
- `perform_mutation` (function) — [saleor/graphql/checkout/mutations/order_create_from_checkout.py:185]

**`saleor/graphql/checkout/mutations/utils.py`**

- `CheckoutLineData` (class) — [saleor/graphql/checkout/mutations/utils.py:51]
- `mark_checkout_deliveries_as_stale_if_needed` (function) — [saleor/graphql/checkout/mutations/utils.py:63]
- `get_variants_and_total_quantities` (function) — [saleor/graphql/checkout/mutations/utils.py:72]
- `check_lines_quantity` (function) — [saleor/graphql/checkout/mutations/utils.py:94]
- `get_not_available_variants_for_purchase` (function) — [saleor/graphql/checkout/mutations/utils.py:161]
- `validate_variants_available_for_purchase` (function) — [saleor/graphql/checkout/mutations/utils.py:181]
- `get_not_published_variants` (function) — [saleor/graphql/checkout/mutations/utils.py:202]
- `validate_variants_are_published` (function) — [saleor/graphql/checkout/mutations/utils.py:215]
- `get_checkout_by_token` (function) — [saleor/graphql/checkout/mutations/utils.py:235]
- `get_checkout` (function) — [saleor/graphql/checkout/mutations/utils.py:260]
- `group_lines_input_on_add` (function) — [saleor/graphql/checkout/mutations/utils.py:302]
- `group_lines_input_data_on_update` (function) — [saleor/graphql/checkout/mutations/utils.py:382]
- `check_permissions_for_custom_prices` (function) — [saleor/graphql/checkout/mutations/utils.py:446]
- `validate_price_override_reason` (function) — [saleor/graphql/checkout/mutations/utils.py:486]
- `find_line_id_when_variant_parameter_used` (function) — [saleor/graphql/checkout/mutations/utils.py:521]
- `find_variant_id_when_line_parameter_used` (function) — [saleor/graphql/checkout/mutations/utils.py:556]
- `apply_gift_reward_if_applicable_on_checkout_creation` (function) — [saleor/graphql/checkout/mutations/utils.py:567]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/checkout/mutations/checkout_lines_add.py` (291 lines)
- `saleor/graphql/checkout/mutations/checkout_shipping_address_update.py` (220 lines)
- `saleor/graphql/checkout/mutations/checkout_billing_address_update.py` (124 lines)
- `saleor/graphql/checkout/mutations/checkout_complete.py` (383 lines)
- `saleor/graphql/checkout/mutations/checkout_lines_delete.py` (122 lines)
- `saleor/graphql/checkout/mutations/checkout_shipping_method_update.py` (199 lines)
- `saleor/graphql/checkout/mutations/order_create_from_checkout.py` (261 lines)
- `saleor/graphql/checkout/mutations/__init__.py` (41 lines)
- `saleor/graphql/checkout/mutations/checkout_add_promo_code.py` (129 lines)
- `saleor/graphql/checkout/mutations/checkout_create_from_order.py` (429 lines)
- `saleor/graphql/checkout/mutations/checkout_create.py` (564 lines)
- `saleor/graphql/checkout/mutations/checkout_customer_attach.py` (130 lines)
- `saleor/graphql/checkout/mutations/checkout_customer_detach.py` (80 lines)
- `saleor/graphql/checkout/mutations/checkout_customer_note_update.py` (61 lines)
- `saleor/graphql/checkout/mutations/checkout_delete.py` (58 lines)
- `saleor/graphql/checkout/mutations/checkout_delivery_method_update.py` (262 lines)
- `saleor/graphql/checkout/mutations/checkout_email_update.py` (90 lines)
- `saleor/graphql/checkout/mutations/checkout_language_code_update.py` (78 lines)
- `saleor/graphql/checkout/mutations/checkout_lines_update.py` (300 lines)
- `saleor/graphql/checkout/mutations/checkout_remove_promo_code.py` (190 lines)
- `saleor/graphql/checkout/mutations/utils.py` (636 lines)

## Interactions

- Imports from: `saleor/account`, `saleor/graphql/product/types`, `saleor/checkout`, `saleor/webhook`, `saleor/graphql`, `saleor/plugins/openid_connect`, `saleor/core`
- Imported by: `saleor/graphql/checkout/tests/mutations`, `saleor/graphql/checkout/tests/deprecated`, `saleor/graphql/checkout/tests`

Internal dependencies named in the source:

- `....account.models.Address`
- `....account.models.User`
- `....app.models.App`
- `....checkout.AddressType`
- `....checkout.actions.call_checkout_event`
- `....checkout.actions.call_checkout_info_event`
- `....checkout.checkout_cleaner.validate_checkout`
- `....checkout.complete_checkout.complete_checkout`
- `....checkout.complete_checkout.create_order_from_checkout`
- `....checkout.delivery_context.is_shipping_required`
- `....checkout.error_codes.CheckoutErrorCode`
- `....checkout.fetch.CheckoutLineInfo`
- `....checkout.fetch.DeliveryMethodBase`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....checkout.models`
- `....checkout.models.Checkout`
- `....checkout.models.CheckoutDelivery`
- `....checkout.utils.add_variants_to_checkout`
- `....checkout.utils.change_billing_address_in_checkout`
- `....checkout.utils.create_checkout_metadata`
- `....checkout.utils.delete_checkouts`
- `....checkout.utils.invalidate_checkout`
- `....core.exceptions.GiftCardNotApplicable`
- `....core.exceptions.InsufficientStock`
- `....core.exceptions.NonExistingCheckout`
- `....core.exceptions.NonExistingCheckoutLines`
- `....core.exceptions.PermissionDenied`
- `....core.taxes.TaxDataError`
- `....core.tracing.traced_atomic_transaction`
- `....core.utils.country.get_active_country`
- `....core.utils.metadata_manager`
- `....discount.DiscountType`
- `....discount.DiscountValueType`
- `....discount.interface.DiscountInfo`
- `....discount.models.CheckoutLineDiscount`
- `....discount.models.NotApplicable`
- `....discount.models.PromotionRule`
- `....graphql.account.mixins.AddressMetadataMixin`
- `....order.models`
- `....permission.auth_filters.AuthorizationFilters`
- `....permission.enums.AccountPermissions`
- `....permission.enums.CheckoutPermissions`
- `....product.models`
- `....product.models.ProductChannelListing`
- `....product.models.ProductVariant`
- `....warehouse.availability.check_stock_and_preorder_quantity_bulk`
- `....warehouse.models`
- `....warehouse.reservations.get_reservation_length`
- `....warehouse.reservations.is_reservation_enabled`
- `....webhook.const.APP_ID_PREFIX`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.event_types.WebhookEventSyncType`
- `...account.i18n.I18nMixin`
- `...account.types.AddressInput`
- `...account.types.User`
- `...app.dataloaders.get_app_promise`
- `...channel.utils.clean_channel`
- `...checkout.types.CheckoutLine`
- `...core.ResolveInfo`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `9b40e8b9cfdd` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
