# Architecture

## What this system is

A codebase documented as 339 module(s) with 579 measured
import edge(s) between them.

## System overview

- **`.semgrep`** — `.semgrep` (`.semgrep`) groups 15 source file(s) exposing 46 top-level declaration(s).
- **`(root)`** — `(root)` (`(root)`) groups 23 source file(s) exposing 25 top-level declaration(s).
- **`saleor`** — `saleor` (`saleor`) groups 26 source file(s) exposing 21 top-level declaration(s).
- **`saleor/account`** — `saleor/account` (`saleor/account`) groups 18 source file(s) exposing 119 top-level declaration(s).
- **`saleor/account/management`** — `saleor/account/management` (`saleor/account/management`) groups 4 source file(s) exposing 6 top-level declaration(s).
- **`saleor/account/migrations`** — `saleor/account/migrations` (`saleor/account/migrations`) groups 116 source file(s) exposing 156 top-level declaration(s).
- **`saleor/account/migrations/tasks`** — `saleor/account/migrations/tasks` (`saleor/account/migrations/tasks`) groups 3 source file(s) exposing 2 top-level declaration(s).
- **`saleor/account/tests`** — `saleor/account/tests` (`saleor/account/tests`) groups 9 source file(s) exposing 70 top-level declaration(s).
- **`saleor/app`** — `saleor/app` (`saleor/app`) groups 16 source file(s) exposing 60 top-level declaration(s).
- **`saleor/app/management`** — `saleor/app/management` (`saleor/app/management`) groups 6 source file(s) exposing 12 top-level declaration(s).
- **`saleor/app/migrations`** — `saleor/app/migrations` (`saleor/app/migrations`) groups 46 source file(s) exposing 65 top-level declaration(s).
- **`saleor/app/tests`** — `saleor/app/tests` (`saleor/app/tests`) groups 20 source file(s) exposing 140 top-level declaration(s).
- **`saleor/app/tests/fixtures`** — `saleor/app/tests/fixtures` (`saleor/app/tests/fixtures`) groups 8 source file(s) exposing 32 top-level declaration(s).
- **`saleor/asgi`** — `saleor/asgi` (`saleor/asgi`) groups 15 source file(s) exposing 51 top-level declaration(s).
- **`saleor/attribute`** — `saleor/attribute` (`saleor/attribute`) groups 5 source file(s) exposing 13 top-level declaration(s).
- **`saleor/attribute/management`** — `saleor/attribute/management` (`saleor/attribute/management`) groups 3 source file(s) exposing 2 top-level declaration(s).
- **`saleor/attribute/migrations`** — `saleor/attribute/migrations` (`saleor/attribute/migrations`) groups 66 source file(s) exposing 104 top-level declaration(s).
- **`saleor/attribute/models`** — `saleor/attribute/models` (`saleor/attribute/models`) groups 5 source file(s) exposing 60 top-level declaration(s).
- **`saleor/attribute/tests`** — `saleor/attribute/tests` (`saleor/attribute/tests`) groups 7 source file(s) exposing 81 top-level declaration(s).
- **`saleor/auth`** — `saleor/auth` (`saleor/auth`) groups 15 source file(s) exposing 15 top-level declaration(s).
- **`saleor/channel`** — `saleor/channel` (`saleor/channel`) groups 7 source file(s) exposing 10 top-level declaration(s).
- **`saleor/channel/migrations`** — `saleor/channel/migrations` (`saleor/channel/migrations`) groups 33 source file(s) exposing 43 top-level declaration(s).
- **`saleor/channel/tests`** — `saleor/channel/tests` (`saleor/channel/tests`) groups 4 source file(s) exposing 8 top-level declaration(s).
- **`saleor/checkout`** — `saleor/checkout` (`saleor/checkout`) groups 15 source file(s) exposing 190 top-level declaration(s).
- **`saleor/checkout/migrations`** — `saleor/checkout/migrations` (`saleor/checkout/migrations`) groups 119 source file(s) exposing 151 top-level declaration(s).
- **`saleor/checkout/migrations/tasks`** — `saleor/checkout/migrations/tasks` (`saleor/checkout/migrations/tasks`) groups 4 source file(s) exposing 3 top-level declaration(s).
- **`saleor/checkout/search`** — `saleor/checkout/search` (`saleor/checkout/search`) groups 3 source file(s) exposing 10 top-level declaration(s).
- **`saleor/checkout/tests`** — `saleor/checkout/tests` (`saleor/checkout/tests`) groups 21 source file(s) exposing 395 top-level declaration(s).
- **`saleor/checkout/tests/fixtures`** — `saleor/checkout/tests/fixtures` (`saleor/checkout/tests/fixtures`) groups 10 source file(s) exposing 79 top-level declaration(s).
- **`saleor/checkout/tests/webhooks`** — `saleor/checkout/tests/webhooks` (`saleor/checkout/tests/webhooks`) groups 11 source file(s) exposing 57 top-level declaration(s).
- **`saleor/checkout/webhooks`** — `saleor/checkout/webhooks` (`saleor/checkout/webhooks`) groups 4 source file(s) exposing 6 top-level declaration(s).
- **`saleor/core`** — `saleor/core` (`saleor/core`) groups 39 source file(s) exposing 237 top-level declaration(s).
- **`saleor/core/cleaners`** — `saleor/core/cleaners` (`saleor/core/cleaners`) groups 5 source file(s) exposing 15 top-level declaration(s).
- **`saleor/core/db`** — `saleor/core/db` (`saleor/core/db`) groups 9 source file(s) exposing 45 top-level declaration(s).
- **`saleor/core/editorjs`** — `saleor/core/editorjs` (`saleor/core/editorjs`) groups 9 source file(s) exposing 71 top-level declaration(s).
- **`saleor/core/management`** — `saleor/core/management` (`saleor/core/management`) groups 10 source file(s) exposing 38 top-level declaration(s).
- **`saleor/core/migrations`** — `saleor/core/migrations` (`saleor/core/migrations`) groups 12 source file(s) exposing 26 top-level declaration(s).
- **`saleor/core/notification`** — `saleor/core/notification` (`saleor/core/notification`) groups 4 source file(s) exposing 8 top-level declaration(s).
- **`saleor/core/telemetry`** — `saleor/core/telemetry` (`saleor/core/telemetry`) groups 10 source file(s) exposing 104 top-level declaration(s).
- **`saleor/core/tests`** — `saleor/core/tests` (`saleor/core/tests`) groups 28 source file(s) exposing 258 top-level declaration(s).
- **`saleor/core/tests/commands`** — `saleor/core/tests/commands` (`saleor/core/tests/commands`) groups 3 source file(s) exposing 9 top-level declaration(s).
- **`saleor/core/utils`** — `saleor/core/utils` (`saleor/core/utils`) groups 17 source file(s) exposing 127 top-level declaration(s).
- **`saleor/core/utils/tests`** — `saleor/core/utils/tests` (`saleor/core/utils/tests`) groups 9 source file(s) exposing 24 top-level declaration(s).
- **`saleor/csv`** — `saleor/csv` (`saleor/csv`) groups 6 source file(s) exposing 21 top-level declaration(s).
- **`saleor/csv/migrations`** — `saleor/csv/migrations` (`saleor/csv/migrations`) groups 5 source file(s) exposing 4 top-level declaration(s).
- **`saleor/csv/tests`** — `saleor/csv/tests` (`saleor/csv/tests`) groups 10 source file(s) exposing 115 top-level declaration(s).
- **`saleor/csv/utils`** — `saleor/csv/utils` (`saleor/csv/utils`) groups 4 source file(s) exposing 33 top-level declaration(s).
- **`saleor/discount`** — `saleor/discount` (`saleor/discount`) groups 6 source file(s) exposing 98 top-level declaration(s).
- **`saleor/discount/migrations`** — `saleor/discount/migrations` (`saleor/discount/migrations`) groups 108 source file(s) exposing 152 top-level declaration(s).
- **`saleor/discount/tests`** — `saleor/discount/tests` (`saleor/discount/tests`) groups 4 source file(s) exposing 55 top-level declaration(s).
- **`saleor/discount/tests/fixtures`** — `saleor/discount/tests/fixtures` (`saleor/discount/tests/fixtures`) groups 5 source file(s) exposing 33 top-level declaration(s).
- **`saleor/discount/tests/test_utils`** — `saleor/discount/tests/test_utils` (`saleor/discount/tests/test_utils`) groups 14 source file(s) exposing 107 top-level declaration(s).
- **`saleor/discount/utils`** — `saleor/discount/utils` (`saleor/discount/utils`) groups 7 source file(s) exposing 73 top-level declaration(s).
- **`saleor/giftcard`** — `saleor/giftcard` (`saleor/giftcard`) groups 11 source file(s) exposing 72 top-level declaration(s).
- **`saleor/giftcard/migrations`** — `saleor/giftcard/migrations` (`saleor/giftcard/migrations`) groups 29 source file(s) exposing 33 top-level declaration(s).
- **`saleor/giftcard/tests`** — `saleor/giftcard/tests` (`saleor/giftcard/tests`) groups 12 source file(s) exposing 71 top-level declaration(s).
- **`saleor/graphql`** — `saleor/graphql` (`saleor/graphql`) groups 18 source file(s) exposing 118 top-level declaration(s).
- **`saleor/graphql/account`** — `saleor/graphql/account` (`saleor/graphql/account`) groups 11 source file(s) exposing 188 top-level declaration(s).
- **`saleor/graphql/account/bulk_mutations`** — `saleor/graphql/account/bulk_mutations` (`saleor/graphql/account/bulk_mutations`) groups 5 source file(s) exposing 36 top-level declaration(s).
- **`saleor/graphql/account/mutations`** — `saleor/graphql/account/mutations` (`saleor/graphql/account/mutations`) groups 2 source file(s) exposing 39 top-level declaration(s).
- **`saleor/graphql/account/mutations/account`** — `saleor/graphql/account/mutations/account` (`saleor/graphql/account/mutations/account`) groups 15 source file(s) exposing 64 top-level declaration(s).
- **`saleor/graphql/account/mutations/authentication`** — `saleor/graphql/account/mutations/authentication` (`saleor/graphql/account/mutations/authentication`) groups 14 source file(s) exposing 61 top-level declaration(s).
- **`saleor/graphql/account/mutations/permission_group`** — `saleor/graphql/account/mutations/permission_group` (`saleor/graphql/account/mutations/permission_group`) groups 4 source file(s) exposing 43 top-level declaration(s).
- **`saleor/graphql/account/mutations/staff`** — `saleor/graphql/account/mutations/staff` (`saleor/graphql/account/mutations/staff`) groups 15 source file(s) exposing 70 top-level declaration(s).
- **`saleor/graphql/account/tests`** — `saleor/graphql/account/tests` (`saleor/graphql/account/tests`) groups 4 source file(s) exposing 66 top-level declaration(s).
- **`saleor/graphql/account/tests/benchmark`** — `saleor/graphql/account/tests/benchmark` (`saleor/graphql/account/tests/benchmark`) groups 3 source file(s) exposing 13 top-level declaration(s).
- **`saleor/graphql/account/tests/bulk_mutations`** — `saleor/graphql/account/tests/bulk_mutations` (`saleor/graphql/account/tests/bulk_mutations`) groups 5 source file(s) exposing 39 top-level declaration(s).
- **`saleor/graphql/account/tests/fixtures`** — `saleor/graphql/account/tests/fixtures` (`saleor/graphql/account/tests/fixtures`) groups 3 source file(s) exposing 4 top-level declaration(s).
- **`saleor/graphql/account/tests/mutations`** — `saleor/graphql/account/tests/mutations` (`saleor/graphql/account/tests/mutations`) groups 2 source file(s) exposing 1 top-level declaration(s).
- **`saleor/graphql/account/tests/mutations/account`** — `saleor/graphql/account/tests/mutations/account` (`saleor/graphql/account/tests/mutations/account`) groups 14 source file(s) exposing 110 top-level declaration(s).
- **`saleor/graphql/account/tests/mutations/authentication`** — `saleor/graphql/account/tests/mutations/authentication` (`saleor/graphql/account/tests/mutations/authentication`) groups 13 source file(s) exposing 86 top-level declaration(s).
- **`saleor/graphql/account/tests/mutations/permission_group`** — `saleor/graphql/account/tests/mutations/permission_group` (`saleor/graphql/account/tests/mutations/permission_group`) groups 4 source file(s) exposing 58 top-level declaration(s).
- **`saleor/graphql/account/tests/mutations/staff`** — `saleor/graphql/account/tests/mutations/staff` (`saleor/graphql/account/tests/mutations/staff`) groups 13 source file(s) exposing 100 top-level declaration(s).
- **`saleor/graphql/account/tests/queries`** — `saleor/graphql/account/tests/queries` (`saleor/graphql/account/tests/queries`) groups 17 source file(s) exposing 154 top-level declaration(s).
- **`saleor/graphql/app`** — `saleor/graphql/app` (`saleor/graphql/app`) groups 8 source file(s) exposing 114 top-level declaration(s).
- **`saleor/graphql/app/dataloaders`** — `saleor/graphql/app/dataloaders` (`saleor/graphql/app/dataloaders`) groups 8 source file(s) exposing 31 top-level declaration(s).
- **`saleor/graphql/app/mutations`** — `saleor/graphql/app/mutations` (`saleor/graphql/app/mutations`) groups 16 source file(s) exposing 96 top-level declaration(s).
- **`saleor/graphql/app/tests`** — `saleor/graphql/app/tests` (`saleor/graphql/app/tests`) groups 3 source file(s) exposing 14 top-level declaration(s).
- **`saleor/graphql/app/tests/benchmarks`** — `saleor/graphql/app/tests/benchmarks` (`saleor/graphql/app/tests/benchmarks`) groups 3 source file(s) exposing 4 top-level declaration(s).
- **`saleor/graphql/app/tests/mutations`** — `saleor/graphql/app/tests/mutations` (`saleor/graphql/app/tests/mutations`) groups 30 source file(s) exposing 162 top-level declaration(s).
- **`saleor/graphql/app/tests/queries`** — `saleor/graphql/app/tests/queries` (`saleor/graphql/app/tests/queries`) groups 8 source file(s) exposing 96 top-level declaration(s).
- **`saleor/graphql/attribute`** — `saleor/graphql/attribute` (`saleor/graphql/attribute`) groups 11 source file(s) exposing 239 top-level declaration(s).
- **`saleor/graphql/attribute/dataloaders`** — `saleor/graphql/attribute/dataloaders` (`saleor/graphql/attribute/dataloaders`) groups 4 source file(s) exposing 53 top-level declaration(s).
- **`saleor/graphql/attribute/mutations`** — `saleor/graphql/attribute/mutations` (`saleor/graphql/attribute/mutations`) groups 15 source file(s) exposing 113 top-level declaration(s).
- **`saleor/graphql/attribute/tests`** — `saleor/graphql/attribute/tests` (`saleor/graphql/attribute/tests`) groups 8 source file(s) exposing 122 top-level declaration(s).
- **`saleor/graphql/attribute/tests/mutations`** — `saleor/graphql/attribute/tests/mutations` (`saleor/graphql/attribute/tests/mutations`) groups 11 source file(s) exposing 180 top-level declaration(s).
- **`saleor/graphql/attribute/tests/queries`** — `saleor/graphql/attribute/tests/queries` (`saleor/graphql/attribute/tests/queries`) groups 8 source file(s) exposing 175 top-level declaration(s).
- **`saleor/graphql/attribute/utils`** — `saleor/graphql/attribute/utils` (`saleor/graphql/attribute/utils`) groups 4 source file(s) exposing 55 top-level declaration(s).
- **`saleor/graphql/channel`** — `saleor/graphql/channel` (`saleor/graphql/channel`) groups 7 source file(s) exposing 37 top-level declaration(s).
- **`saleor/graphql/channel/dataloaders`** — `saleor/graphql/channel/dataloaders` (`saleor/graphql/channel/dataloaders`) groups 5 source file(s) exposing 18 top-level declaration(s).
- **`saleor/graphql/channel/mutations`** — `saleor/graphql/channel/mutations` (`saleor/graphql/channel/mutations`) groups 9 source file(s) exposing 71 top-level declaration(s).
- **`saleor/graphql/channel/tests`** — `saleor/graphql/channel/tests` (`saleor/graphql/channel/tests`) groups 5 source file(s) exposing 11 top-level declaration(s).
- **`saleor/graphql/channel/tests/mutations`** — `saleor/graphql/channel/tests/mutations` (`saleor/graphql/channel/tests/mutations`) groups 8 source file(s) exposing 122 top-level declaration(s).
- **`saleor/graphql/channel/tests/queries`** — `saleor/graphql/channel/tests/queries` (`saleor/graphql/channel/tests/queries`) groups 3 source file(s) exposing 31 top-level declaration(s).
- **`saleor/graphql/checkout`** — `saleor/graphql/checkout` (`saleor/graphql/checkout`) groups 8 source file(s) exposing 133 top-level declaration(s).
- **`saleor/graphql/checkout/dataloaders`** — `saleor/graphql/checkout/dataloaders` (`saleor/graphql/checkout/dataloaders`) groups 7 source file(s) exposing 46 top-level declaration(s).
- **`saleor/graphql/checkout/mutations`** — `saleor/graphql/checkout/mutations` (`saleor/graphql/checkout/mutations`) groups 21 source file(s) exposing 145 top-level declaration(s).
- **`saleor/graphql/checkout/tests`** — `saleor/graphql/checkout/tests` (`saleor/graphql/checkout/tests`) groups 12 source file(s) exposing 222 top-level declaration(s).
- **`saleor/graphql/checkout/tests/benchmark`** — `saleor/graphql/checkout/tests/benchmark` (`saleor/graphql/checkout/tests/benchmark`) groups 5 source file(s) exposing 34 top-level declaration(s).
- **`saleor/graphql/checkout/tests/deprecated`** — `saleor/graphql/checkout/tests/deprecated` (`saleor/graphql/checkout/tests/deprecated`) groups 14 source file(s) exposing 54 top-level declaration(s).
- **`saleor/graphql/checkout/tests/mutations`** — `saleor/graphql/checkout/tests/mutations` (`saleor/graphql/checkout/tests/mutations`) groups 26 source file(s) exposing 318 top-level declaration(s).
- **`saleor/graphql/core`** — `saleor/graphql/core` (`saleor/graphql/core`) groups 14 source file(s) exposing 173 top-level declaration(s).
- **`saleor/graphql/core/federation`** — `saleor/graphql/core/federation` (`saleor/graphql/core/federation`) groups 7 source file(s) exposing 18 top-level declaration(s).
- **`saleor/graphql/core/filters`** — `saleor/graphql/core/filters` (`saleor/graphql/core/filters`) groups 6 source file(s) exposing 77 top-level declaration(s).
- **`saleor/graphql/core/tests`** — `saleor/graphql/core/tests` (`saleor/graphql/core/tests`) groups 24 source file(s) exposing 263 top-level declaration(s).
- **`saleor/graphql/core/tests/garbage_collection`** — `saleor/graphql/core/tests/garbage_collection` (`saleor/graphql/core/tests/garbage_collection`) groups 9 source file(s) exposing 15 top-level declaration(s).
- **`saleor/graphql/core/types`** — `saleor/graphql/core/types` (`saleor/graphql/core/types`) groups 16 source file(s) exposing 272 top-level declaration(s).
- **`saleor/graphql/core/utils`** — `saleor/graphql/core/utils` (`saleor/graphql/core/utils`) groups 4 source file(s) exposing 29 top-level declaration(s).
- **`saleor/graphql/core/validators`** — `saleor/graphql/core/validators` (`saleor/graphql/core/validators`) groups 8 source file(s) exposing 45 top-level declaration(s).
- **`saleor/graphql/csv`** — `saleor/graphql/csv` (`saleor/graphql/csv`) groups 8 source file(s) exposing 37 top-level declaration(s).
- **`saleor/graphql/csv/mutations`** — `saleor/graphql/csv/mutations` (`saleor/graphql/csv/mutations`) groups 5 source file(s) exposing 29 top-level declaration(s).
- **`saleor/graphql/csv/tests`** — `saleor/graphql/csv/tests` (`saleor/graphql/csv/tests`) groups 8 source file(s) exposing 48 top-level declaration(s).
- **`saleor/graphql/discount`** — `saleor/graphql/discount` (`saleor/graphql/discount`) groups 9 source file(s) exposing 146 top-level declaration(s).
- **`saleor/graphql/discount/mutations`** — `saleor/graphql/discount/mutations` (`saleor/graphql/discount/mutations`) groups 3 source file(s) exposing 18 top-level declaration(s).
- **`saleor/graphql/discount/mutations/promotion`** — `saleor/graphql/discount/mutations/promotion` (`saleor/graphql/discount/mutations/promotion`) groups 9 source file(s) exposing 63 top-level declaration(s).
- **`saleor/graphql/discount/mutations/sale`** — `saleor/graphql/discount/mutations/sale` (`saleor/graphql/discount/mutations/sale`) groups 8 source file(s) exposing 61 top-level declaration(s).
- **`saleor/graphql/discount/mutations/voucher`** — `saleor/graphql/discount/mutations/voucher` (`saleor/graphql/discount/mutations/voucher`) groups 8 source file(s) exposing 64 top-level declaration(s).
- **`saleor/graphql/discount/tests`** — `saleor/graphql/discount/tests` (`saleor/graphql/discount/tests`) groups 3 source file(s) exposing 40 top-level declaration(s).
- **`saleor/graphql/discount/tests/benchmark`** — `saleor/graphql/discount/tests/benchmark` (`saleor/graphql/discount/tests/benchmark`) groups 11 source file(s) exposing 15 top-level declaration(s).
- **`saleor/graphql/discount/tests/deprecated`** — `saleor/graphql/discount/tests/deprecated` (`saleor/graphql/discount/tests/deprecated`) groups 5 source file(s) exposing 18 top-level declaration(s).
- **`saleor/graphql/discount/tests/mutations`** — `saleor/graphql/discount/tests/mutations` (`saleor/graphql/discount/tests/mutations`) groups 23 source file(s) exposing 221 top-level declaration(s).
- **`saleor/graphql/discount/tests/queries`** — `saleor/graphql/discount/tests/queries` (`saleor/graphql/discount/tests/queries`) groups 15 source file(s) exposing 82 top-level declaration(s).
- **`saleor/graphql/discount/types`** — `saleor/graphql/discount/types` (`saleor/graphql/discount/types`) groups 6 source file(s) exposing 89 top-level declaration(s).
- **`saleor/graphql/giftcard`** — `saleor/graphql/giftcard` (`saleor/graphql/giftcard`) groups 8 source file(s) exposing 100 top-level declaration(s).
- **`saleor/graphql/giftcard/bulk_mutations`** — `saleor/graphql/giftcard/bulk_mutations` (`saleor/graphql/giftcard/bulk_mutations`) groups 5 source file(s) exposing 25 top-level declaration(s).
- **`saleor/graphql/giftcard/mutations`** — `saleor/graphql/giftcard/mutations` (`saleor/graphql/giftcard/mutations`) groups 12 source file(s) exposing 64 top-level declaration(s).
- **`saleor/graphql/giftcard/tests`** — `saleor/graphql/giftcard/tests` (`saleor/graphql/giftcard/tests`) groups 2 source file(s) exposing 5 top-level declaration(s).
- **`saleor/graphql/giftcard/tests/benchmark`** — `saleor/graphql/giftcard/tests/benchmark` (`saleor/graphql/giftcard/tests/benchmark`) groups 3 source file(s) exposing 9 top-level declaration(s).
- **`saleor/graphql/giftcard/tests/bulk_mutations`** — `saleor/graphql/giftcard/tests/bulk_mutations` (`saleor/graphql/giftcard/tests/bulk_mutations`) groups 5 source file(s) exposing 23 top-level declaration(s).
- **`saleor/graphql/giftcard/tests/deprecated`** — `saleor/graphql/giftcard/tests/deprecated` (`saleor/graphql/giftcard/tests/deprecated`) groups 3 source file(s) exposing 3 top-level declaration(s).
- **`saleor/graphql/giftcard/tests/mutations`** — `saleor/graphql/giftcard/tests/mutations` (`saleor/graphql/giftcard/tests/mutations`) groups 11 source file(s) exposing 79 top-level declaration(s).
- **`saleor/graphql/giftcard/tests/queries`** — `saleor/graphql/giftcard/tests/queries` (`saleor/graphql/giftcard/tests/queries`) groups 9 source file(s) exposing 61 top-level declaration(s).
- **`saleor/graphql/invoice`** — `saleor/graphql/invoice` (`saleor/graphql/invoice`) groups 4 source file(s) exposing 6 top-level declaration(s).
- **`saleor/graphql/invoice/mutations`** — `saleor/graphql/invoice/mutations` (`saleor/graphql/invoice/mutations`) groups 7 source file(s) exposing 33 top-level declaration(s).
- **`saleor/graphql/invoice/tests`** — `saleor/graphql/invoice/tests` (`saleor/graphql/invoice/tests`) groups 7 source file(s) exposing 38 top-level declaration(s).
- **`saleor/graphql/management`** — `saleor/graphql/management` (`saleor/graphql/management`) groups 3 source file(s) exposing 2 top-level declaration(s).
- **`saleor/graphql/menu`** — `saleor/graphql/menu` (`saleor/graphql/menu`) groups 8 source file(s) exposing 59 top-level declaration(s).
- **`saleor/graphql/menu/bulk_mutations`** — `saleor/graphql/menu/bulk_mutations` (`saleor/graphql/menu/bulk_mutations`) groups 3 source file(s) exposing 8 top-level declaration(s).
- **`saleor/graphql/menu/mutations`** — `saleor/graphql/menu/mutations` (`saleor/graphql/menu/mutations`) groups 9 source file(s) exposing 50 top-level declaration(s).
- **`saleor/graphql/menu/tests`** — `saleor/graphql/menu/tests` (`saleor/graphql/menu/tests`) groups 3 source file(s) exposing 1 top-level declaration(s).
- **`saleor/graphql/menu/tests/bulk_mutations`** — `saleor/graphql/menu/tests/bulk_mutations` (`saleor/graphql/menu/tests/bulk_mutations`) groups 3 source file(s) exposing 6 top-level declaration(s).
- **`saleor/graphql/menu/tests/mutations`** — `saleor/graphql/menu/tests/mutations` (`saleor/graphql/menu/tests/mutations`) groups 9 source file(s) exposing 31 top-level declaration(s).
- **`saleor/graphql/menu/tests/queries`** — `saleor/graphql/menu/tests/queries` (`saleor/graphql/menu/tests/queries`) groups 7 source file(s) exposing 29 top-level declaration(s).
- **`saleor/graphql/meta`** — `saleor/graphql/meta` (`saleor/graphql/meta`) groups 7 source file(s) exposing 55 top-level declaration(s).
- **`saleor/graphql/meta/mutations`** — `saleor/graphql/meta/mutations` (`saleor/graphql/meta/mutations`) groups 7 source file(s) exposing 36 top-level declaration(s).
- **`saleor/graphql/meta/tests`** — `saleor/graphql/meta/tests` (`saleor/graphql/meta/tests`) groups 3 source file(s) exposing 187 top-level declaration(s).
- **`saleor/graphql/meta/tests/mutations`** — `saleor/graphql/meta/tests/mutations` (`saleor/graphql/meta/tests/mutations`) groups 22 source file(s) exposing 297 top-level declaration(s).
- **`saleor/graphql/meta/tests/queries`** — `saleor/graphql/meta/tests/queries` (`saleor/graphql/meta/tests/queries`) groups 16 source file(s) exposing 211 top-level declaration(s).
- **`saleor/graphql/notifications`** — `saleor/graphql/notifications` (`saleor/graphql/notifications`) groups 9 source file(s) exposing 12 top-level declaration(s).
- **`saleor/graphql/order`** — `saleor/graphql/order` (`saleor/graphql/order`) groups 9 source file(s) exposing 362 top-level declaration(s).
- **`saleor/graphql/order/bulk_mutations`** — `saleor/graphql/order/bulk_mutations` (`saleor/graphql/order/bulk_mutations`) groups 5 source file(s) exposing 101 top-level declaration(s).
- **`saleor/graphql/order/mutations`** — `saleor/graphql/order/mutations` (`saleor/graphql/order/mutations`) groups 37 source file(s) exposing 296 top-level declaration(s).
- **`saleor/graphql/order/tests`** — `saleor/graphql/order/tests` (`saleor/graphql/order/tests`) groups 10 source file(s) exposing 64 top-level declaration(s).
- **`saleor/graphql/order/tests/benchmark`** — `saleor/graphql/order/tests/benchmark` (`saleor/graphql/order/tests/benchmark`) groups 8 source file(s) exposing 13 top-level declaration(s).
- **`saleor/graphql/order/tests/deprecated`** — `saleor/graphql/order/tests/deprecated` (`saleor/graphql/order/tests/deprecated`) groups 3 source file(s) exposing 11 top-level declaration(s).
- **`saleor/graphql/order/tests/integration`** — `saleor/graphql/order/tests/integration` (`saleor/graphql/order/tests/integration`) groups 4 source file(s) exposing 8 top-level declaration(s).
- **`saleor/graphql/order/tests/mutations`** — `saleor/graphql/order/tests/mutations` (`saleor/graphql/order/tests/mutations`) groups 39 source file(s) exposing 334 top-level declaration(s).
- **`saleor/graphql/order/tests/queries`** — `saleor/graphql/order/tests/queries` (`saleor/graphql/order/tests/queries`) groups 28 source file(s) exposing 436 top-level declaration(s).
- **`saleor/graphql/page`** — `saleor/graphql/page` (`saleor/graphql/page`) groups 8 source file(s) exposing 104 top-level declaration(s).
- **`saleor/graphql/page/mutations`** — `saleor/graphql/page/mutations` (`saleor/graphql/page/mutations`) groups 11 source file(s) exposing 67 top-level declaration(s).
- **`saleor/graphql/page/tests`** — `saleor/graphql/page/tests` (`saleor/graphql/page/tests`) groups 3 source file(s) exposing 3 top-level declaration(s).
- **`saleor/graphql/page/tests/deprecated`** — `saleor/graphql/page/tests/deprecated` (`saleor/graphql/page/tests/deprecated`) groups 4 source file(s) exposing 5 top-level declaration(s).
- **`saleor/graphql/page/tests/mutations`** — `saleor/graphql/page/tests/mutations` (`saleor/graphql/page/tests/mutations`) groups 14 source file(s) exposing 132 top-level declaration(s).
- **`saleor/graphql/page/tests/queries`** — `saleor/graphql/page/tests/queries` (`saleor/graphql/page/tests/queries`) groups 6 source file(s) exposing 61 top-level declaration(s).
- **`saleor/graphql/page/tests/queries/pages_with_where`** — `saleor/graphql/page/tests/queries/pages_with_where` (`saleor/graphql/page/tests/queries/pages_with_where`) groups 19 source file(s) exposing 39 top-level declaration(s).
- **`saleor/graphql/payment`** — `saleor/graphql/payment` (`saleor/graphql/payment`) groups 9 source file(s) exposing 138 top-level declaration(s).
- **`saleor/graphql/payment/mutations`** — `saleor/graphql/payment/mutations` (`saleor/graphql/payment/mutations`) groups 2 source file(s) exposing 4 top-level declaration(s).
- **`saleor/graphql/payment/mutations/payment`** — `saleor/graphql/payment/mutations/payment` (`saleor/graphql/payment/mutations/payment`) groups 7 source file(s) exposing 41 top-level declaration(s).
- **`saleor/graphql/payment/mutations/stored_payment_methods`** — `saleor/graphql/payment/mutations/stored_payment_methods` (`saleor/graphql/payment/mutations/stored_payment_methods`) groups 6 source file(s) exposing 17 top-level declaration(s).
- **`saleor/graphql/payment/mutations/transaction`** — `saleor/graphql/payment/mutations/transaction` (`saleor/graphql/payment/mutations/transaction`) groups 11 source file(s) exposing 85 top-level declaration(s).
- **`saleor/graphql/payment/tests`** — `saleor/graphql/payment/tests` (`saleor/graphql/payment/tests`) groups 7 source file(s) exposing 19 top-level declaration(s).
- **`saleor/graphql/payment/tests/mutations`** — `saleor/graphql/payment/tests/mutations` (`saleor/graphql/payment/tests/mutations`) groups 21 source file(s) exposing 325 top-level declaration(s).
- **`saleor/graphql/payment/tests/queries`** — `saleor/graphql/payment/tests/queries` (`saleor/graphql/payment/tests/queries`) groups 10 source file(s) exposing 93 top-level declaration(s).
- **`saleor/graphql/plugins`** — `saleor/graphql/plugins` (`saleor/graphql/plugins`) groups 15 source file(s) exposing 77 top-level declaration(s).
- **`saleor/graphql/product`** — `saleor/graphql/product` (`saleor/graphql/product`) groups 6 source file(s) exposing 102 top-level declaration(s).
- **`saleor/graphql/product/bulk_mutations`** — `saleor/graphql/product/bulk_mutations` (`saleor/graphql/product/bulk_mutations`) groups 13 source file(s) exposing 127 top-level declaration(s).
- **`saleor/graphql/product/dataloaders`** — `saleor/graphql/product/dataloaders` (`saleor/graphql/product/dataloaders`) groups 3 source file(s) exposing 94 top-level declaration(s).
- **`saleor/graphql/product/filters`** — `saleor/graphql/product/filters` (`saleor/graphql/product/filters`) groups 9 source file(s) exposing 150 top-level declaration(s).
- **`saleor/graphql/product/mutations`** — `saleor/graphql/product/mutations` (`saleor/graphql/product/mutations`) groups 4 source file(s) exposing 91 top-level declaration(s).
- **`saleor/graphql/product/mutations/category`** — `saleor/graphql/product/mutations/category` (`saleor/graphql/product/mutations/category`) groups 4 source file(s) exposing 17 top-level declaration(s).
- **`saleor/graphql/product/mutations/collection`** — `saleor/graphql/product/mutations/collection` (`saleor/graphql/product/mutations/collection`) groups 7 source file(s) exposing 35 top-level declaration(s).
- **`saleor/graphql/product/mutations/product`** — `saleor/graphql/product/mutations/product` (`saleor/graphql/product/mutations/product`) groups 9 source file(s) exposing 56 top-level declaration(s).
- **`saleor/graphql/product/mutations/product_type`** — `saleor/graphql/product/mutations/product_type` (`saleor/graphql/product/mutations/product_type`) groups 4 source file(s) exposing 21 top-level declaration(s).
- **`saleor/graphql/product/mutations/product_variant`** — `saleor/graphql/product/mutations/product_variant` (`saleor/graphql/product/mutations/product_variant`) groups 10 source file(s) exposing 60 top-level declaration(s).
- **`saleor/graphql/product/tests`** — `saleor/graphql/product/tests` (`saleor/graphql/product/tests`) groups 17 source file(s) exposing 222 top-level declaration(s).
- **`saleor/graphql/product/tests/benchmark`** — `saleor/graphql/product/tests/benchmark` (`saleor/graphql/product/tests/benchmark`) groups 9 source file(s) exposing 50 top-level declaration(s).
- **`saleor/graphql/product/tests/deprecated`** — `saleor/graphql/product/tests/deprecated` (`saleor/graphql/product/tests/deprecated`) groups 9 source file(s) exposing 60 top-level declaration(s).
- **`saleor/graphql/product/tests/mutations`** — `saleor/graphql/product/tests/mutations` (`saleor/graphql/product/tests/mutations`) groups 39 source file(s) exposing 326 top-level declaration(s).
- **`saleor/graphql/product/tests/queries`** — `saleor/graphql/product/tests/queries` (`saleor/graphql/product/tests/queries`) groups 20 source file(s) exposing 487 top-level declaration(s).
- **`saleor/graphql/product/tests/queries/products_filtrations`** — `saleor/graphql/product/tests/queries/products_filtrations` (`saleor/graphql/product/tests/queries/products_filtrations`) groups 15 source file(s) exposing 36 top-level declaration(s).
- **`saleor/graphql/product/tests/queries/variants_where`** — `saleor/graphql/product/tests/queries/variants_where` (`saleor/graphql/product/tests/queries/variants_where`) groups 15 source file(s) exposing 39 top-level declaration(s).
- **`saleor/graphql/product/types`** — `saleor/graphql/product/types` (`saleor/graphql/product/types`) groups 5 source file(s) exposing 170 top-level declaration(s).
- **`saleor/graphql/shipping`** — `saleor/graphql/shipping` (`saleor/graphql/shipping`) groups 8 source file(s) exposing 74 top-level declaration(s).
- **`saleor/graphql/shipping/bulk_mutations`** — `saleor/graphql/shipping/bulk_mutations` (`saleor/graphql/shipping/bulk_mutations`) groups 3 source file(s) exposing 9 top-level declaration(s).
- **`saleor/graphql/shipping/mutations`** — `saleor/graphql/shipping/mutations` (`saleor/graphql/shipping/mutations`) groups 12 source file(s) exposing 80 top-level declaration(s).
- **`saleor/graphql/shipping/tests`** — `saleor/graphql/shipping/tests` (`saleor/graphql/shipping/tests`) groups 1 source file(s) exposing 0 top-level declaration(s).
- **`saleor/graphql/shipping/tests/benchmark`** — `saleor/graphql/shipping/tests/benchmark` (`saleor/graphql/shipping/tests/benchmark`) groups 3 source file(s) exposing 6 top-level declaration(s).
- **`saleor/graphql/shipping/tests/mutations`** — `saleor/graphql/shipping/tests/mutations` (`saleor/graphql/shipping/tests/mutations`) groups 12 source file(s) exposing 87 top-level declaration(s).
- **`saleor/graphql/shipping/tests/queries`** — `saleor/graphql/shipping/tests/queries` (`saleor/graphql/shipping/tests/queries`) groups 4 source file(s) exposing 14 top-level declaration(s).
- **`saleor/graphql/shop`** — `saleor/graphql/shop` (`saleor/graphql/shop`) groups 7 source file(s) exposing 86 top-level declaration(s).
- **`saleor/graphql/shop/mutations`** — `saleor/graphql/shop/mutations` (`saleor/graphql/shop/mutations`) groups 11 source file(s) exposing 48 top-level declaration(s).
- **`saleor/graphql/shop/tests`** — `saleor/graphql/shop/tests` (`saleor/graphql/shop/tests`) groups 4 source file(s) exposing 5 top-level declaration(s).
- **`saleor/graphql/shop/tests/mutations`** — `saleor/graphql/shop/tests/mutations` (`saleor/graphql/shop/tests/mutations`) groups 10 source file(s) exposing 81 top-level declaration(s).
- **`saleor/graphql/shop/tests/queries`** — `saleor/graphql/shop/tests/queries` (`saleor/graphql/shop/tests/queries`) groups 5 source file(s) exposing 55 top-level declaration(s).
- **`saleor/graphql/tax`** — `saleor/graphql/tax` (`saleor/graphql/tax`) groups 7 source file(s) exposing 64 top-level declaration(s).
- **`saleor/graphql/tax/mutations`** — `saleor/graphql/tax/mutations` (`saleor/graphql/tax/mutations`) groups 8 source file(s) exposing 70 top-level declaration(s).
- **`saleor/graphql/tax/tests`** — `saleor/graphql/tax/tests` (`saleor/graphql/tax/tests`) groups 2 source file(s) exposing 0 top-level declaration(s).
- **`saleor/graphql/tax/tests/mutations`** — `saleor/graphql/tax/tests/mutations` (`saleor/graphql/tax/tests/mutations`) groups 8 source file(s) exposing 58 top-level declaration(s).
- **`saleor/graphql/tax/tests/queries`** — `saleor/graphql/tax/tests/queries` (`saleor/graphql/tax/tests/queries`) groups 7 source file(s) exposing 24 top-level declaration(s).
- **`saleor/graphql/tests`** — `saleor/graphql/tests` (`saleor/graphql/tests`) groups 13 source file(s) exposing 99 top-level declaration(s).
- **`saleor/graphql/translations`** — `saleor/graphql/translations` (`saleor/graphql/translations`) groups 7 source file(s) exposing 149 top-level declaration(s).
- **`saleor/graphql/translations/mutations`** — `saleor/graphql/translations/mutations` (`saleor/graphql/translations/mutations`) groups 20 source file(s) exposing 125 top-level declaration(s).
- **`saleor/graphql/translations/tests`** — `saleor/graphql/translations/tests` (`saleor/graphql/translations/tests`) groups 4 source file(s) exposing 132 top-level declaration(s).
- **`saleor/graphql/translations/tests/mutations`** — `saleor/graphql/translations/tests/mutations` (`saleor/graphql/translations/tests/mutations`) groups 12 source file(s) exposing 64 top-level declaration(s).
- **`saleor/graphql/utils`** — `saleor/graphql/utils` (`saleor/graphql/utils`) groups 4 source file(s) exposing 29 top-level declaration(s).
- **`saleor/graphql/warehouse`** — `saleor/graphql/warehouse` (`saleor/graphql/warehouse`) groups 10 source file(s) exposing 119 top-level declaration(s).
- **`saleor/graphql/warehouse/mutations`** — `saleor/graphql/warehouse/mutations` (`saleor/graphql/warehouse/mutations`) groups 7 source file(s) exposing 29 top-level declaration(s).
- **`saleor/graphql/warehouse/tests`** — `saleor/graphql/warehouse/tests` (`saleor/graphql/warehouse/tests`) groups 3 source file(s) exposing 11 top-level declaration(s).
- **`saleor/graphql/warehouse/tests/benchmark`** — `saleor/graphql/warehouse/tests/benchmark` (`saleor/graphql/warehouse/tests/benchmark`) groups 3 source file(s) exposing 3 top-level declaration(s).
- **`saleor/graphql/warehouse/tests/mutations`** — `saleor/graphql/warehouse/tests/mutations` (`saleor/graphql/warehouse/tests/mutations`) groups 6 source file(s) exposing 39 top-level declaration(s).
- **`saleor/graphql/warehouse/tests/queries`** — `saleor/graphql/warehouse/tests/queries` (`saleor/graphql/warehouse/tests/queries`) groups 8 source file(s) exposing 42 top-level declaration(s).
- **`saleor/graphql/webhook`** — `saleor/graphql/webhook` (`saleor/graphql/webhook`) groups 13 source file(s) exposing 589 top-level declaration(s).
- **`saleor/graphql/webhook/mutations`** — `saleor/graphql/webhook/mutations` (`saleor/graphql/webhook/mutations`) groups 7 source file(s) exposing 41 top-level declaration(s).
- **`saleor/graphql/webhook/tests`** — `saleor/graphql/webhook/tests` (`saleor/graphql/webhook/tests`) groups 8 source file(s) exposing 34 top-level declaration(s).
- **`saleor/graphql/webhook/tests/mutations`** — `saleor/graphql/webhook/tests/mutations` (`saleor/graphql/webhook/tests/mutations`) groups 7 source file(s) exposing 75 top-level declaration(s).
- **`saleor/graphql/webhook/tests/queries`** — `saleor/graphql/webhook/tests/queries` (`saleor/graphql/webhook/tests/queries`) groups 6 source file(s) exposing 25 top-level declaration(s).
- **`saleor/invoice`** — `saleor/invoice` (`saleor/invoice`) groups 7 source file(s) exposing 19 top-level declaration(s).
- **`saleor/invoice/migrations`** — `saleor/invoice/migrations` (`saleor/invoice/migrations`) groups 12 source file(s) exposing 11 top-level declaration(s).
- **`saleor/menu`** — `saleor/menu` (`saleor/menu`) groups 3 source file(s) exposing 11 top-level declaration(s).
- **`saleor/menu/migrations`** — `saleor/menu/migrations` (`saleor/menu/migrations`) groups 25 source file(s) exposing 34 top-level declaration(s).
- **`saleor/menu/tests`** — `saleor/menu/tests` (`saleor/menu/tests`) groups 5 source file(s) exposing 5 top-level declaration(s).
- **`saleor/order`** — `saleor/order` (`saleor/order`) groups 15 source file(s) exposing 303 top-level declaration(s).
- **`saleor/order/migrations`** — `saleor/order/migrations` (`saleor/order/migrations`) groups 291 source file(s) exposing 383 top-level declaration(s).
- **`saleor/order/migrations/tasks`** — `saleor/order/migrations/tasks` (`saleor/order/migrations/tasks`) groups 3 source file(s) exposing 3 top-level declaration(s).
- **`saleor/order/tests`** — `saleor/order/tests` (`saleor/order/tests`) groups 24 source file(s) exposing 282 top-level declaration(s).
- **`saleor/order/tests/fixtures`** — `saleor/order/tests/fixtures` (`saleor/order/tests/fixtures`) groups 6 source file(s) exposing 60 top-level declaration(s).
- **`saleor/order/tests/webhooks`** — `saleor/order/tests/webhooks` (`saleor/order/tests/webhooks`) groups 9 source file(s) exposing 44 top-level declaration(s).
- **`saleor/order/webhooks`** — `saleor/order/webhooks` (`saleor/order/webhooks`) groups 3 source file(s) exposing 4 top-level declaration(s).
- **`saleor/page`** — `saleor/page` (`saleor/page`) groups 7 source file(s) exposing 21 top-level declaration(s).
- **`saleor/page/migrations`** — `saleor/page/migrations` (`saleor/page/migrations`) groups 36 source file(s) exposing 43 top-level declaration(s).
- **`saleor/page/tests`** — `saleor/page/tests` (`saleor/page/tests`) groups 8 source file(s) exposing 16 top-level declaration(s).
- **`saleor/payment`** — `saleor/payment` (`saleor/payment`) groups 11 source file(s) exposing 186 top-level declaration(s).
- **`saleor/payment/gateways`** — `saleor/payment/gateways` (`saleor/payment/gateways`) groups 13 source file(s) exposing 151 top-level declaration(s).
- **`saleor/payment/migrations`** — `saleor/payment/migrations` (`saleor/payment/migrations`) groups 89 source file(s) exposing 132 top-level declaration(s).
- **`saleor/payment/tests`** — `saleor/payment/tests` (`saleor/payment/tests`) groups 6 source file(s) exposing 141 top-level declaration(s).
- **`saleor/payment/tests/fixtures`** — `saleor/payment/tests/fixtures` (`saleor/payment/tests/fixtures`) groups 7 source file(s) exposing 22 top-level declaration(s).
- **`saleor/payment/tests/test_utils`** — `saleor/payment/tests/test_utils` (`saleor/payment/tests/test_utils`) groups 5 source file(s) exposing 117 top-level declaration(s).
- **`saleor/permission`** — `saleor/permission` (`saleor/permission`) groups 15 source file(s) exposing 87 top-level declaration(s).
- **`saleor/plugins`** — `saleor/plugins` (`saleor/plugins`) groups 9 source file(s) exposing 239 top-level declaration(s).
- **`saleor/plugins/admin_email`** — `saleor/plugins/admin_email` (`saleor/plugins/admin_email`) groups 15 source file(s) exposing 60 top-level declaration(s).
- **`saleor/plugins/avatax`** — `saleor/plugins/avatax` (`saleor/plugins/avatax`) groups 99 source file(s) exposing 53 top-level declaration(s).
- **`saleor/plugins/migrations`** — `saleor/plugins/migrations` (`saleor/plugins/migrations`) groups 12 source file(s) exposing 21 top-level declaration(s).
- **`saleor/plugins/openid_connect`** — `saleor/plugins/openid_connect` (`saleor/plugins/openid_connect`) groups 20 source file(s) exposing 160 top-level declaration(s).
- **`saleor/plugins/sendgrid`** — `saleor/plugins/sendgrid` (`saleor/plugins/sendgrid`) groups 7 source file(s) exposing 56 top-level declaration(s).
- **`saleor/plugins/tests`** — `saleor/plugins/tests` (`saleor/plugins/tests`) groups 14 source file(s) exposing 200 top-level declaration(s).
- **`saleor/plugins/user_email`** — `saleor/plugins/user_email` (`saleor/plugins/user_email`) groups 25 source file(s) exposing 120 top-level declaration(s).
- **`saleor/plugins/webhook`** — `saleor/plugins/webhook` (`saleor/plugins/webhook`) groups 3 source file(s) exposing 173 top-level declaration(s).
- **`saleor/plugins/webhook/tests`** — `saleor/plugins/webhook/tests` (`saleor/plugins/webhook/tests`) groups 15 source file(s) exposing 180 top-level declaration(s).
- **`saleor/plugins/webhook/tests/subscription_webhooks`** — `saleor/plugins/webhook/tests/subscription_webhooks` (`saleor/plugins/webhook/tests/subscription_webhooks`) groups 1 source file(s) exposing 0 top-level declaration(s).
- **`saleor/plugins/webhook/tests/subscription_webhooks/filterable_webhooks`** — `saleor/plugins/webhook/tests/subscription_webhooks/filterable_webhooks` (`saleor/plugins/webhook/tests/subscription_webhooks/filterable_webhooks`) groups 22 source file(s) exposing 83 top-level declaration(s).
- **`saleor/product`** — `saleor/product` (`saleor/product`) groups 11 source file(s) exposing 108 top-level declaration(s).
- **`saleor/product/management`** — `saleor/product/management` (`saleor/product/management`) groups 3 source file(s) exposing 3 top-level declaration(s).
- **`saleor/product/migrations`** — `saleor/product/migrations` (`saleor/product/migrations`) groups 248 source file(s) exposing 322 top-level declaration(s).
- **`saleor/product/tests`** — `saleor/product/tests` (`saleor/product/tests`) groups 17 source file(s) exposing 142 top-level declaration(s).
- **`saleor/product/tests/fixtures`** — `saleor/product/tests/fixtures` (`saleor/product/tests/fixtures`) groups 7 source file(s) exposing 82 top-level declaration(s).
- **`saleor/product/utils`** — `saleor/product/utils` (`saleor/product/utils`) groups 8 source file(s) exposing 29 top-level declaration(s).
- **`saleor/schedulers`** — `saleor/schedulers` (`saleor/schedulers`) groups 6 source file(s) exposing 22 top-level declaration(s).
- **`saleor/shipping`** — `saleor/shipping` (`saleor/shipping`) groups 9 source file(s) exposing 50 top-level declaration(s).
- **`saleor/shipping/migrations`** — `saleor/shipping/migrations` (`saleor/shipping/migrations`) groups 40 source file(s) exposing 45 top-level declaration(s).
- **`saleor/shipping/tests`** — `saleor/shipping/tests` (`saleor/shipping/tests`) groups 11 source file(s) exposing 36 top-level declaration(s).
- **`saleor/site`** — `saleor/site` (`saleor/site`) groups 6 source file(s) exposing 24 top-level declaration(s).
- **`saleor/site/migrations`** — `saleor/site/migrations` (`saleor/site/migrations`) groups 60 source file(s) exposing 65 top-level declaration(s).
- **`saleor/site/tests`** — `saleor/site/tests` (`saleor/site/tests`) groups 4 source file(s) exposing 4 top-level declaration(s).
- **`saleor/tax`** — `saleor/tax` (`saleor/tax`) groups 4 source file(s) exposing 40 top-level declaration(s).
- **`saleor/tax/calculations`** — `saleor/tax/calculations` (`saleor/tax/calculations`) groups 3 source file(s) exposing 5 top-level declaration(s).
- **`saleor/tax/migrations`** — `saleor/tax/migrations` (`saleor/tax/migrations`) groups 14 source file(s) exposing 24 top-level declaration(s).
- **`saleor/tax/tests`** — `saleor/tax/tests` (`saleor/tax/tests`) groups 11 source file(s) exposing 84 top-level declaration(s).
- **`saleor/tax/webhooks`** — `saleor/tax/webhooks` (`saleor/tax/webhooks`) groups 3 source file(s) exposing 6 top-level declaration(s).
- **`saleor/tests`** — `saleor/tests` (`saleor/tests`) groups 13 source file(s) exposing 126 top-level declaration(s).
- **`saleor/tests/e2e`** — `saleor/tests/e2e` (`saleor/tests/e2e`) groups 8 source file(s) exposing 19 top-level declaration(s).
- **`saleor/tests/e2e/account`** — `saleor/tests/e2e/account` (`saleor/tests/e2e/account`) groups 1 source file(s) exposing 0 top-level declaration(s).
- **`saleor/tests/e2e/account/account`** — `saleor/tests/e2e/account/account` (`saleor/tests/e2e/account/account`) groups 8 source file(s) exposing 7 top-level declaration(s).
- **`saleor/tests/e2e/account/staff`** — `saleor/tests/e2e/account/staff` (`saleor/tests/e2e/account/staff`) groups 4 source file(s) exposing 3 top-level declaration(s).
- **`saleor/tests/e2e/account/utils`** — `saleor/tests/e2e/account/utils` (`saleor/tests/e2e/account/utils`) groups 12 source file(s) exposing 12 top-level declaration(s).
- **`saleor/tests/e2e/apps`** — `saleor/tests/e2e/apps` (`saleor/tests/e2e/apps`) groups 3 source file(s) exposing 1 top-level declaration(s).
- **`saleor/tests/e2e/attributes`** — `saleor/tests/e2e/attributes` (`saleor/tests/e2e/attributes`) groups 6 source file(s) exposing 6 top-level declaration(s).
- **`saleor/tests/e2e/channel`** — `saleor/tests/e2e/channel` (`saleor/tests/e2e/channel`) groups 4 source file(s) exposing 2 top-level declaration(s).
- **`saleor/tests/e2e/checkout`** — `saleor/tests/e2e/checkout` (`saleor/tests/e2e/checkout`) groups 31 source file(s) exposing 40 top-level declaration(s).
- **`saleor/tests/e2e/checkout/discounts`** — `saleor/tests/e2e/checkout/discounts` (`saleor/tests/e2e/checkout/discounts`) groups 3 source file(s) exposing 10 top-level declaration(s).
- **`saleor/tests/e2e/checkout/discounts/promotions`** — `saleor/tests/e2e/checkout/discounts/promotions` (`saleor/tests/e2e/checkout/discounts/promotions`) groups 9 source file(s) exposing 12 top-level declaration(s).
- **`saleor/tests/e2e/checkout/discounts/sales`** — `saleor/tests/e2e/checkout/discounts/sales` (`saleor/tests/e2e/checkout/discounts/sales`) groups 6 source file(s) exposing 8 top-level declaration(s).
- **`saleor/tests/e2e/checkout/discounts/vouchers`** — `saleor/tests/e2e/checkout/discounts/vouchers` (`saleor/tests/e2e/checkout/discounts/vouchers`) groups 22 source file(s) exposing 44 top-level declaration(s).
- **`saleor/tests/e2e/checkout/shipping`** — `saleor/tests/e2e/checkout/shipping` (`saleor/tests/e2e/checkout/shipping`) groups 4 source file(s) exposing 3 top-level declaration(s).
- **`saleor/tests/e2e/checkout/taxes`** — `saleor/tests/e2e/checkout/taxes` (`saleor/tests/e2e/checkout/taxes`) groups 9 source file(s) exposing 10 top-level declaration(s).
- **`saleor/tests/e2e/checkout/utils`** — `saleor/tests/e2e/checkout/utils` (`saleor/tests/e2e/checkout/utils`) groups 15 source file(s) exposing 19 top-level declaration(s).
- **`saleor/tests/e2e/checkout/zero_total`** — `saleor/tests/e2e/checkout/zero_total` (`saleor/tests/e2e/checkout/zero_total`) groups 5 source file(s) exposing 4 top-level declaration(s).
- **`saleor/tests/e2e/gift_cards`** — `saleor/tests/e2e/gift_cards` (`saleor/tests/e2e/gift_cards`) groups 7 source file(s) exposing 11 top-level declaration(s).
- **`saleor/tests/e2e/metadata`** — `saleor/tests/e2e/metadata` (`saleor/tests/e2e/metadata`) groups 6 source file(s) exposing 4 top-level declaration(s).
- **`saleor/tests/e2e/orders`** — `saleor/tests/e2e/orders` (`saleor/tests/e2e/orders`) groups 32 source file(s) exposing 38 top-level declaration(s).
- **`saleor/tests/e2e/orders/discounts`** — `saleor/tests/e2e/orders/discounts` (`saleor/tests/e2e/orders/discounts`) groups 26 source file(s) exposing 48 top-level declaration(s).
- **`saleor/tests/e2e/orders/taxes`** — `saleor/tests/e2e/orders/taxes` (`saleor/tests/e2e/orders/taxes`) groups 6 source file(s) exposing 6 top-level declaration(s).
- **`saleor/tests/e2e/orders/utils`** — `saleor/tests/e2e/orders/utils` (`saleor/tests/e2e/orders/utils`) groups 26 source file(s) exposing 29 top-level declaration(s).
- **`saleor/tests/e2e/orders/zero_total`** — `saleor/tests/e2e/orders/zero_total` (`saleor/tests/e2e/orders/zero_total`) groups 3 source file(s) exposing 2 top-level declaration(s).
- **`saleor/tests/e2e/pages`** — `saleor/tests/e2e/pages` (`saleor/tests/e2e/pages`) groups 5 source file(s) exposing 3 top-level declaration(s).
- **`saleor/tests/e2e/payment`** — `saleor/tests/e2e/payment` (`saleor/tests/e2e/payment`) groups 3 source file(s) exposing 1 top-level declaration(s).
- **`saleor/tests/e2e/product`** — `saleor/tests/e2e/product` (`saleor/tests/e2e/product`) groups 6 source file(s) exposing 7 top-level declaration(s).
- **`saleor/tests/e2e/product/utils`** — `saleor/tests/e2e/product/utils` (`saleor/tests/e2e/product/utils`) groups 17 source file(s) exposing 21 top-level declaration(s).
- **`saleor/tests/e2e/promotions`** — `saleor/tests/e2e/promotions` (`saleor/tests/e2e/promotions`) groups 10 source file(s) exposing 28 top-level declaration(s).
- **`saleor/tests/e2e/promotions/utils`** — `saleor/tests/e2e/promotions/utils` (`saleor/tests/e2e/promotions/utils`) groups 9 source file(s) exposing 10 top-level declaration(s).
- **`saleor/tests/e2e/sales`** — `saleor/tests/e2e/sales` (`saleor/tests/e2e/sales`) groups 5 source file(s) exposing 4 top-level declaration(s).
- **`saleor/tests/e2e/shipping_zone`** — `saleor/tests/e2e/shipping_zone` (`saleor/tests/e2e/shipping_zone`) groups 6 source file(s) exposing 5 top-level declaration(s).
- **`saleor/tests/e2e/shop`** — `saleor/tests/e2e/shop` (`saleor/tests/e2e/shop`) groups 4 source file(s) exposing 4 top-level declaration(s).
- **`saleor/tests/e2e/taxes`** — `saleor/tests/e2e/taxes` (`saleor/tests/e2e/taxes`) groups 7 source file(s) exposing 5 top-level declaration(s).
- **`saleor/tests/e2e/transactions`** — `saleor/tests/e2e/transactions` (`saleor/tests/e2e/transactions`) groups 5 source file(s) exposing 4 top-level declaration(s).
- **`saleor/tests/e2e/vouchers`** — `saleor/tests/e2e/vouchers` (`saleor/tests/e2e/vouchers`) groups 15 source file(s) exposing 23 top-level declaration(s).
- **`saleor/tests/e2e/warehouse`** — `saleor/tests/e2e/warehouse` (`saleor/tests/e2e/warehouse`) groups 4 source file(s) exposing 2 top-level declaration(s).
- **`saleor/thumbnail`** — `saleor/thumbnail` (`saleor/thumbnail`) groups 7 source file(s) exposing 34 top-level declaration(s).
- **`saleor/thumbnail/migrations`** — `saleor/thumbnail/migrations` (`saleor/thumbnail/migrations`) groups 4 source file(s) exposing 3 top-level declaration(s).
- **`saleor/thumbnail/tests`** — `saleor/thumbnail/tests` (`saleor/thumbnail/tests`) groups 6 source file(s) exposing 61 top-level declaration(s).
- **`saleor/warehouse`** — `saleor/warehouse` (`saleor/warehouse`) groups 11 source file(s) exposing 100 top-level declaration(s).
- **`saleor/warehouse/migrations`** — `saleor/warehouse/migrations` (`saleor/warehouse/migrations`) groups 38 source file(s) exposing 49 top-level declaration(s).
- **`saleor/warehouse/tests`** — `saleor/warehouse/tests` (`saleor/warehouse/tests`) groups 12 source file(s) exposing 195 top-level declaration(s).
- **`saleor/warehouse/tests/fixtures`** — `saleor/warehouse/tests/fixtures` (`saleor/warehouse/tests/fixtures`) groups 5 source file(s) exposing 14 top-level declaration(s).
- **`saleor/warehouse/tests/webhooks`** — `saleor/warehouse/tests/webhooks` (`saleor/warehouse/tests/webhooks`) groups 6 source file(s) exposing 25 top-level declaration(s).
- **`saleor/warehouse/webhooks`** — `saleor/warehouse/webhooks` (`saleor/warehouse/webhooks`) groups 4 source file(s) exposing 8 top-level declaration(s).
- **`saleor/webhook`** — `saleor/webhook` (`saleor/webhook`) groups 14 source file(s) exposing 88 top-level declaration(s).
- **`saleor/webhook/migrations`** — `saleor/webhook/migrations` (`saleor/webhook/migrations`) groups 15 source file(s) exposing 16 top-level declaration(s).
- **`saleor/webhook/observability`** — `saleor/webhook/observability` (`saleor/webhook/observability`) groups 9 source file(s) exposing 85 top-level declaration(s).
- **`saleor/webhook/observability/tests`** — `saleor/webhook/observability/tests` (`saleor/webhook/observability/tests`) groups 7 source file(s) exposing 83 top-level declaration(s).
- **`saleor/webhook/response_schemas`** — `saleor/webhook/response_schemas` (`saleor/webhook/response_schemas`) groups 9 source file(s) exposing 63 top-level declaration(s).
- **`saleor/webhook/tests`** — `saleor/webhook/tests` (`saleor/webhook/tests`) groups 14 source file(s) exposing 156 top-level declaration(s).
- **`saleor/webhook/tests/circuit_breaker`** — `saleor/webhook/tests/circuit_breaker` (`saleor/webhook/tests/circuit_breaker`) groups 6 source file(s) exposing 25 top-level declaration(s).
- **`saleor/webhook/tests/fixtures`** — `saleor/webhook/tests/fixtures` (`saleor/webhook/tests/fixtures`) groups 7 source file(s) exposing 199 top-level declaration(s).
- **`saleor/webhook/tests/response_schemas`** — `saleor/webhook/tests/response_schemas` (`saleor/webhook/tests/response_schemas`) groups 7 source file(s) exposing 83 top-level declaration(s).
- **`saleor/webhook/tests/subscription_webhooks`** — `saleor/webhook/tests/subscription_webhooks` (`saleor/webhook/tests/subscription_webhooks`) groups 18 source file(s) exposing 260 top-level declaration(s).
- **`saleor/webhook/transport`** — `saleor/webhook/transport` (`saleor/webhook/transport`) groups 6 source file(s) exposing 45 top-level declaration(s).
- **`saleor/webhook/transport/asynchronous`** — `saleor/webhook/transport/asynchronous` (`saleor/webhook/transport/asynchronous`) groups 7 source file(s) exposing 52 top-level declaration(s).
- **`saleor/webhook/transport/synchronous`** — `saleor/webhook/transport/synchronous` (`saleor/webhook/transport/synchronous`) groups 4 source file(s) exposing 16 top-level declaration(s).
- **`saleor/webhook/transport/tests`** — `saleor/webhook/transport/tests` (`saleor/webhook/transport/tests`) groups 3 source file(s) exposing 33 top-level declaration(s).

## Component diagram

```mermaid
graph TD
  m44f235[".semgrep"]
  m44c4ce["(root)"]
  m9b3c4e["saleor"]
  m9725f5["saleor/account"]
  m35e373["saleor/account/management"]
  me49444["saleor/account/migrations"]
  m82c013["saleor/account/migrations/tasks"]
  m6dfebe["saleor/account/tests"]
  m8de4b3["saleor/app"]
  m5cb15b["saleor/app/management"]
  m8a4347["saleor/app/migrations"]
  mf0185d["saleor/app/tests"]
  m0a7422["saleor/app/tests/fixtures"]
  m25b504["saleor/asgi"]
  m5ac00e["saleor/attribute"]
  m98cff5["saleor/attribute/management"]
  me812a9["saleor/attribute/migrations"]
  m48c877["saleor/attribute/models"]
  m254daa["saleor/attribute/tests"]
  mddbb55["saleor/auth"]
  m93027a["saleor/channel"]
  m15bbc1["saleor/channel/migrations"]
  m32ee42["saleor/channel/tests"]
  md3112a["saleor/checkout"]
  m8a63c0["saleor/checkout/migrations"]
  m36a86b["saleor/checkout/migrations/tasks"]
  m896e04["saleor/checkout/search"]
  md40cb8["saleor/checkout/tests"]
  m74d739["saleor/checkout/tests/fixtures"]
  m6900a1["saleor/checkout/tests/webhooks"]
  m505731["saleor/checkout/webhooks"]
  m2dc3b7["saleor/core"]
  m5c41ab["saleor/core/cleaners"]
  m824cd0["saleor/core/db"]
  mb51b68["saleor/core/editorjs"]
  m0975f8["saleor/core/management"]
  mca8eec["saleor/core/migrations"]
  m73fa11["saleor/core/notification"]
  ma6ec13["saleor/core/telemetry"]
  m409911["saleor/core/tests"]
  m88ea2e["saleor/core/tests/commands"]
  me1f093["saleor/core/utils"]
  m09f7c4["saleor/core/utils/tests"]
  mbc1344["saleor/csv"]
  m7b893c["saleor/csv/migrations"]
  m8900e5["saleor/csv/tests"]
  mfd6e81["saleor/csv/utils"]
  m8778ad["saleor/discount"]
  m02661c["saleor/discount/migrations"]
  m926fc3["saleor/discount/tests"]
  m430c8d["saleor/discount/tests/fixtures"]
  md920d3["saleor/discount/tests/test_utils"]
  mc5aaca["saleor/discount/utils"]
  md996a0["saleor/giftcard"]
  mec3b50["saleor/giftcard/migrations"]
  m9bdbdd["saleor/giftcard/tests"]
  mdaa4f5["saleor/graphql"]
  m8f2419["saleor/graphql/account"]
  m065cdd["saleor/graphql/account/bulk_mutations"]
  mf943df["saleor/graphql/account/mutations"]
  mba1ef3["saleor/graphql/account/mutations/account"]
  m0d712b["saleor/graphql/account/mutations/authentication"]
  me5bece["saleor/graphql/account/mutations/permission_group"]
  m7fe89c["saleor/graphql/account/mutations/staff"]
  m03d64d["saleor/graphql/account/tests"]
  me643a5["saleor/graphql/account/tests/benchmark"]
  m553d41["saleor/graphql/account/tests/bulk_mutations"]
  mb11552["saleor/graphql/account/tests/fixtures"]
  m47a43e["saleor/graphql/account/tests/mutations"]
  m583f6f["saleor/graphql/account/tests/mutations/account"]
  m726974["saleor/graphql/account/tests/mutations/authentication"]
  m2cc29f["saleor/graphql/account/tests/mutations/permission_group"]
  m43d11d["saleor/graphql/account/tests/mutations/staff"]
  m96a729["saleor/graphql/account/tests/queries"]
  m6d6db4["saleor/graphql/app"]
  mc22155["saleor/graphql/app/dataloaders"]
  mc1a163["saleor/graphql/app/mutations"]
  m18a636["saleor/graphql/app/tests"]
  md1378e["saleor/graphql/app/tests/benchmarks"]
  m376622["saleor/graphql/app/tests/mutations"]
  mc970e4["saleor/graphql/app/tests/queries"]
  m65f051["saleor/graphql/attribute"]
  m663680["saleor/graphql/attribute/dataloaders"]
  m4bb0fe["saleor/graphql/attribute/mutations"]
  m68533c["saleor/graphql/attribute/tests"]
  m7c3d9b["saleor/graphql/attribute/tests/mutations"]
  m670f9d["saleor/graphql/attribute/tests/queries"]
  m524d3b["saleor/graphql/attribute/utils"]
  m058968["saleor/graphql/channel"]
  mf852b3["saleor/graphql/channel/dataloaders"]
  m28f5b9["saleor/graphql/channel/mutations"]
  med942a["saleor/graphql/channel/tests"]
  m62caf1["saleor/graphql/channel/tests/mutations"]
  maa2c69["saleor/graphql/channel/tests/queries"]
  mcb7e15["saleor/graphql/checkout"]
  m5717a7["saleor/graphql/checkout/dataloaders"]
  mb70ea4["saleor/graphql/checkout/mutations"]
  m36d3a0["saleor/graphql/checkout/tests"]
  mbb85b9["saleor/graphql/checkout/tests/benchmark"]
  m3b5d41["saleor/graphql/checkout/tests/deprecated"]
  m3a6fc2["saleor/graphql/checkout/tests/mutations"]
  mde612a["saleor/graphql/core"]
  mb69e33["saleor/graphql/core/federation"]
  m701347["saleor/graphql/core/filters"]
  mb751f6["saleor/graphql/core/tests"]
  m2a8005["saleor/graphql/core/tests/garbage_collection"]
  m3dbf96["saleor/graphql/core/types"]
  m923907["saleor/graphql/core/utils"]
  m83d2e5["saleor/graphql/core/validators"]
  m624c21["saleor/graphql/csv"]
  m0201da["saleor/graphql/csv/mutations"]
  m380587["saleor/graphql/csv/tests"]
  mc17e7d["saleor/graphql/discount"]
  m81cbda["saleor/graphql/discount/mutations"]
  ma7d473["saleor/graphql/discount/mutations/promotion"]
  m68195c["saleor/graphql/discount/mutations/sale"]
  md1083b["saleor/graphql/discount/mutations/voucher"]
  m14906f["saleor/graphql/discount/tests"]
  m0e9d4d["saleor/graphql/discount/tests/benchmark"]
  mb8c011["saleor/graphql/discount/tests/deprecated"]
  m8f5e60["saleor/graphql/discount/tests/mutations"]
  m14f3c0["saleor/graphql/discount/tests/queries"]
  m56c6eb["saleor/graphql/discount/types"]
  mc6f92e["saleor/graphql/giftcard"]
  m908892["saleor/graphql/giftcard/bulk_mutations"]
  mf331c0["saleor/graphql/giftcard/mutations"]
  m774c0c["saleor/graphql/giftcard/tests"]
  m9e9d8b["saleor/graphql/giftcard/tests/benchmark"]
  m979e0e["saleor/graphql/giftcard/tests/bulk_mutations"]
  m6393ac["saleor/graphql/giftcard/tests/deprecated"]
  mcb14b7["saleor/graphql/giftcard/tests/mutations"]
  m8aba19["saleor/graphql/giftcard/tests/queries"]
  m2a5acc["saleor/graphql/invoice"]
  m0c58ba["saleor/graphql/invoice/mutations"]
  m7a8d34["saleor/graphql/invoice/tests"]
  m11665e["saleor/graphql/management"]
  mff82f4["saleor/graphql/menu"]
  m42e653["saleor/graphql/menu/bulk_mutations"]
  m4ee999["saleor/graphql/menu/mutations"]
  m5297e3["saleor/graphql/menu/tests"]
  m84ead1["saleor/graphql/menu/tests/bulk_mutations"]
  m6c1bd7["saleor/graphql/menu/tests/mutations"]
  m7ec249["saleor/graphql/menu/tests/queries"]
  m2ac823["saleor/graphql/meta"]
  me8623d["saleor/graphql/meta/mutations"]
  md74adc["saleor/graphql/meta/tests"]
  m0be63f["saleor/graphql/meta/tests/mutations"]
  md5772f["saleor/graphql/meta/tests/queries"]
  m19a274["saleor/graphql/notifications"]
  m140bcd["saleor/graphql/order"]
  m4f7507["saleor/graphql/order/bulk_mutations"]
  mf57999["saleor/graphql/order/mutations"]
  m56fe87["saleor/graphql/order/tests"]
  m65906b["saleor/graphql/order/tests/benchmark"]
  mbdf25f["saleor/graphql/order/tests/deprecated"]
  m023429["saleor/graphql/order/tests/integration"]
  m179dbc["saleor/graphql/order/tests/mutations"]
  mc5989c["saleor/graphql/order/tests/queries"]
  m010ad4["saleor/graphql/page"]
  m9c6a97["saleor/graphql/page/mutations"]
  m0b845a["saleor/graphql/page/tests"]
  m01e40b["saleor/graphql/page/tests/deprecated"]
  md92534["saleor/graphql/page/tests/mutations"]
  mffd584["saleor/graphql/page/tests/queries"]
  ma5e85e["saleor/graphql/page/tests/queries/pages_with_where"]
  m073edb["saleor/graphql/payment"]
  m763fdb["saleor/graphql/payment/mutations"]
  m11e006["saleor/graphql/payment/mutations/payment"]
  m80365f["saleor/graphql/payment/mutations/stored_payment_methods"]
  m0bd03e["saleor/graphql/payment/mutations/transaction"]
  m9006ce["saleor/graphql/payment/tests"]
  m82bd9d["saleor/graphql/payment/tests/mutations"]
  m5b6eae["saleor/graphql/payment/tests/queries"]
  m53c378["saleor/graphql/plugins"]
  m512e66["saleor/graphql/product"]
  m421ef0["saleor/graphql/product/bulk_mutations"]
  mc7c2ea["saleor/graphql/product/dataloaders"]
  m346909["saleor/graphql/product/filters"]
  m5086aa["saleor/graphql/product/mutations"]
  m61e7ef["saleor/graphql/product/mutations/category"]
  medd5b6["saleor/graphql/product/mutations/collection"]
  m0663eb["saleor/graphql/product/mutations/product"]
  m860e05["saleor/graphql/product/mutations/product_type"]
  m428166["saleor/graphql/product/mutations/product_variant"]
  m85e134["saleor/graphql/product/tests"]
  m406164["saleor/graphql/product/tests/benchmark"]
  md56f47["saleor/graphql/product/tests/deprecated"]
  m1645c9["saleor/graphql/product/tests/mutations"]
  md06401["saleor/graphql/product/tests/queries"]
  me75f0b["saleor/graphql/product/tests/queries/products_filtrations"]
  m00b518["saleor/graphql/product/tests/queries/variants_where"]
  mc60ea4["saleor/graphql/product/types"]
  mf92728["saleor/graphql/shipping"]
  m4db290["saleor/graphql/shipping/bulk_mutations"]
  m75fab1["saleor/graphql/shipping/mutations"]
  me9cdbb["saleor/graphql/shipping/tests"]
  m009eb6["saleor/graphql/shipping/tests/benchmark"]
  m525e3e["saleor/graphql/shipping/tests/mutations"]
  m6dacda["saleor/graphql/shipping/tests/queries"]
  mfbe57b["saleor/graphql/shop"]
  m353bed["saleor/graphql/shop/mutations"]
  m80059d["saleor/graphql/shop/tests"]
  mdfb693["saleor/graphql/shop/tests/mutations"]
  mabfbcd["saleor/graphql/shop/tests/queries"]
  m0e4866["saleor/graphql/tax"]
  md8fb4d["saleor/graphql/tax/mutations"]
  m400e5e["saleor/graphql/tax/tests"]
  m45ceed["saleor/graphql/tax/tests/mutations"]
  ma7fa91["saleor/graphql/tax/tests/queries"]
  mc30ece["saleor/graphql/tests"]
  m405ca3["saleor/graphql/translations"]
  m58ef6b["saleor/graphql/translations/mutations"]
  m4edef8["saleor/graphql/translations/tests"]
  mddec38["saleor/graphql/translations/tests/mutations"]
  m3db96b["saleor/graphql/utils"]
  m877222["saleor/graphql/warehouse"]
  m6a2ec0["saleor/graphql/warehouse/mutations"]
  m03d133["saleor/graphql/warehouse/tests"]
  mfbe703["saleor/graphql/warehouse/tests/benchmark"]
  mb86bfc["saleor/graphql/warehouse/tests/mutations"]
  me09af5["saleor/graphql/warehouse/tests/queries"]
  mfd6ee0["saleor/graphql/webhook"]
  m3e83b0["saleor/graphql/webhook/mutations"]
  ma304c1["saleor/graphql/webhook/tests"]
  m3f9180["saleor/graphql/webhook/tests/mutations"]
  m224d4f["saleor/graphql/webhook/tests/queries"]
  m2ae093["saleor/invoice"]
  m9dd0ca["saleor/invoice/migrations"]
  m2a55e2["saleor/menu"]
  m012751["saleor/menu/migrations"]
  maee8eb["saleor/menu/tests"]
  m878739["saleor/order"]
  m872bbc["saleor/order/migrations"]
  me429e4["saleor/order/migrations/tasks"]
  mcf84c8["saleor/order/tests"]
  m59110b["saleor/order/tests/fixtures"]
  m71f606["saleor/order/tests/webhooks"]
  m0c27d8["saleor/order/webhooks"]
  mdd6624["saleor/page"]
  mdada24["saleor/page/migrations"]
  m70f237["saleor/page/tests"]
  m44867b["saleor/payment"]
  m2943ba["saleor/payment/gateways"]
  m2230c0["saleor/payment/migrations"]
  m1e1471["saleor/payment/tests"]
  m26ce79["saleor/payment/tests/fixtures"]
  mdf5304["saleor/payment/tests/test_utils"]
  m662c17["saleor/permission"]
  m7a3bed["saleor/plugins"]
  m1dae83["saleor/plugins/admin_email"]
  mdfcf6a["saleor/plugins/avatax"]
  md74163["saleor/plugins/migrations"]
  m55d337["saleor/plugins/openid_connect"]
  mc412c9["saleor/plugins/sendgrid"]
  m9d4d8b["saleor/plugins/tests"]
  md931fa["saleor/plugins/user_email"]
  m469ce0["saleor/plugins/webhook"]
  m0353e2["saleor/plugins/webhook/tests"]
  mf71a3b["saleor/plugins/webhook/tests/subscription_webhooks"]
  med8f4f["saleor/plugins/webhook/tests/subscription_webhooks/filterable_webhooks"]
  mdceda9["saleor/product"]
  m559711["saleor/product/management"]
  m1ff499["saleor/product/migrations"]
  m09665a["saleor/product/tests"]
  mbcc065["saleor/product/tests/fixtures"]
  m946dd3["saleor/product/utils"]
  mf7b8f6["saleor/schedulers"]
  m435001["saleor/shipping"]
  m18e7a9["saleor/shipping/migrations"]
  m7f6995["saleor/shipping/tests"]
  mce6bc7["saleor/site"]
  mcb93b3["saleor/site/migrations"]
  m707e09["saleor/site/tests"]
  m33e04e["saleor/tax"]
  m37d80c["saleor/tax/calculations"]
  ma789d5["saleor/tax/migrations"]
  m40e931["saleor/tax/tests"]
  m366d8e["saleor/tax/webhooks"]
  md90551["saleor/tests"]
  m19e2ac["saleor/tests/e2e"]
  ma741e9["saleor/tests/e2e/account"]
  m597684["saleor/tests/e2e/account/account"]
  m57dfc1["saleor/tests/e2e/account/staff"]
  m489c38["saleor/tests/e2e/account/utils"]
  m843b78["saleor/tests/e2e/apps"]
  mb75f22["saleor/tests/e2e/attributes"]
  m886138["saleor/tests/e2e/channel"]
  m2cde94["saleor/tests/e2e/checkout"]
  m78d833["saleor/tests/e2e/checkout/discounts"]
  m160fa9["saleor/tests/e2e/checkout/discounts/promotions"]
  m841b3e["saleor/tests/e2e/checkout/discounts/sales"]
  m0137ea["saleor/tests/e2e/checkout/discounts/vouchers"]
  mc449fd["saleor/tests/e2e/checkout/shipping"]
  maa120e["saleor/tests/e2e/checkout/taxes"]
  ma0f373["saleor/tests/e2e/checkout/utils"]
  m7658f2["saleor/tests/e2e/checkout/zero_total"]
  m8b6e32["saleor/tests/e2e/gift_cards"]
  m3bd007["saleor/tests/e2e/metadata"]
  mde9373["saleor/tests/e2e/orders"]
  mfe3437["saleor/tests/e2e/orders/discounts"]
  m301bbe["saleor/tests/e2e/orders/taxes"]
  m96c788["saleor/tests/e2e/orders/utils"]
  m7ed30b["saleor/tests/e2e/orders/zero_total"]
  m6131a9["saleor/tests/e2e/pages"]
  m6007ee["saleor/tests/e2e/payment"]
  m9ab6fe["saleor/tests/e2e/product"]
  mb28159["saleor/tests/e2e/product/utils"]
  m86157a["saleor/tests/e2e/promotions"]
  m2f7230["saleor/tests/e2e/promotions/utils"]
  m4d330e["saleor/tests/e2e/sales"]
  m86aa90["saleor/tests/e2e/shipping_zone"]
  me6b656["saleor/tests/e2e/shop"]
  m99b8a8["saleor/tests/e2e/taxes"]
  m7ad543["saleor/tests/e2e/transactions"]
  mac74ff["saleor/tests/e2e/vouchers"]
  m66a790["saleor/tests/e2e/warehouse"]
  md782d2["saleor/thumbnail"]
  m416bf2["saleor/thumbnail/migrations"]
  m2b9ee7["saleor/thumbnail/tests"]
  m4a7764["saleor/warehouse"]
  m4cf4a4["saleor/warehouse/migrations"]
  mcd4b88["saleor/warehouse/tests"]
  m19e26f["saleor/warehouse/tests/fixtures"]
  mab83e4["saleor/warehouse/tests/webhooks"]
  mea9bce["saleor/warehouse/webhooks"]
  m71d0b1["saleor/webhook"]
  mb8c7f1["saleor/webhook/migrations"]
  m169f7a["saleor/webhook/observability"]
  m778e60["saleor/webhook/observability/tests"]
  m8f41f6["saleor/webhook/response_schemas"]
  m3506a9["saleor/webhook/tests"]
  m58f268["saleor/webhook/tests/circuit_breaker"]
  m220c74["saleor/webhook/tests/fixtures"]
  m332c4b["saleor/webhook/tests/response_schemas"]
  m3d9f10["saleor/webhook/tests/subscription_webhooks"]
  m5f5973["saleor/webhook/transport"]
  m3ee7cc["saleor/webhook/transport/asynchronous"]
  m7b725e["saleor/webhook/transport/synchronous"]
  mbdf262["saleor/webhook/transport/tests"]
  m872bbc --> m2dc3b7
  m1ff499 --> m2dc3b7
  mde9373 --> m19e2ac
  me49444 --> m2dc3b7
  med8f4f --> m3ee7cc
  m2230c0 --> m2dc3b7
  m02661c --> m2dc3b7
  m1ff499 --> me1f093
  m8a63c0 --> m2dc3b7
  mcf84c8 --> m878739
  m96c788 --> mc30ece
  md3112a --> m2dc3b7
  mc5989c --> m2dc3b7
  me812a9 --> m2dc3b7
  md40cb8 --> m2dc3b7
  m878739 --> m2dc3b7
  m872bbc --> me1f093
  me49444 --> me1f093
  md40cb8 --> md3112a
  m3a6fc2 --> mb70ea4
  m878739 --> mc60ea4
  m4a7764 --> mc60ea4
  md3112a --> mc60ea4
  m2dc3b7 --> mc60ea4
  m02661c --> me1f093
  m5717a7 --> mc60ea4
  m179dbc --> m2dc3b7
  mcf84c8 --> m2dc3b7
  mdada24 --> m2dc3b7
  m8a63c0 --> me1f093
  m409911 --> m2dc3b7
  mec3b50 --> m2dc3b7
  m421ef0 --> mc60ea4
  m1645c9 --> m421ef0
  m55d337 --> m2dc3b7
  m71d0b1 --> mc60ea4
  mc5aaca --> m8778ad
  m1645c9 --> me1f093
  m44867b --> mc60ea4
  mdfcf6a --> m2dc3b7
  m435001 --> m2dc3b7
  m9725f5 --> m2dc3b7
  m8de4b3 --> m2dc3b7
  mc5aaca --> mc60ea4
  m583f6f --> mba1ef3
  mc22155 --> mc60ea4
  m663680 --> mc60ea4
  m5717a7 --> mdaa4f5
  m3a6fc2 --> m2dc3b7
  m140bcd --> mc60ea4
  m85e134 --> m421ef0
  m44867b --> m2dc3b7
  m7a3bed --> mc60ea4
  mdceda9 --> m2dc3b7
  mdceda9 --> mc60ea4
  m946dd3 --> mc60ea4
  mcd4b88 --> m4a7764
  m44f235 --> m2dc3b7
  me49444 --> m9725f5
  mddbb55 --> m2dc3b7
  m9b3c4e --> m2dc3b7
  ma6ec13 --> mc60ea4
  ma6ec13 --> mfd6e81
  me1f093 --> mc60ea4
  me1f093 --> m2dc3b7
  mc5aaca --> m2dc3b7
  mba1ef3 --> m2dc3b7
  m0d712b --> m2dc3b7
  mde612a --> mc60ea4
  m3dbf96 --> mde612a
  mdaa4f5 --> mc60ea4
  m140bcd --> mdaa4f5
  mf57999 --> mc60ea4
  m406164 --> m421ef0
  mc60ea4 --> mdaa4f5
  m58ef6b --> mdaa4f5
  mfd6ee0 --> mdaa4f5
  m012751 --> m2dc3b7
  m878739 --> m55d337
  m872bbc --> m878739
  m59110b --> m2dc3b7
  m2943ba --> m2dc3b7
  m2943ba --> mdaa4f5
  m1e1471 --> m44867b
  mc412c9 --> m55d337
  m09665a --> mdceda9
  m09665a --> m2dc3b7
  m18e7a9 --> m2dc3b7
  m18e7a9 --> me1f093
  m40e931 --> m2dc3b7
  m2cde94 --> m19e2ac
  mab83e4 --> mea9bce
  m71d0b1 --> m2dc3b7
  m8f41f6 --> m2dc3b7
  m8de4b3 --> m9b3c4e
  m8de4b3 --> mc60ea4
  m8a4347 --> me1f093
  m8a4347 --> m2dc3b7
  m48c877 --> m2dc3b7
  md3112a --> m55d337
  md40cb8 --> mdaa4f5
  m6900a1 --> m2dc3b7
  m6900a1 --> m505731
  m505731 --> mdaa4f5
  m505731 --> m2dc3b7
  m2dc3b7 --> m55d337
  ma6ec13 --> m2dc3b7
  m926fc3 --> m8778ad
  md996a0 --> mc60ea4
  m9bdbdd --> md996a0
  m4bb0fe --> mc60ea4
  m4bb0fe --> me1f093
  m7c3d9b --> me1f093
  m524d3b --> mc60ea4
  m28f5b9 --> mc60ea4
  m3b5d41 --> mb70ea4
  m3a6fc2 --> mdaa4f5
  mde612a --> mdaa4f5
  m701347 --> m9725f5
  m2a8005 --> m71d0b1
  m83d2e5 --> m2dc3b7
  ma7d473 --> mc60ea4
  m68195c --> mc60ea4
  m979e0e --> m908892
  m4f7507 --> mc60ea4
  m9c6a97 --> mc60ea4
  mc7c2ea --> mc60ea4
  m1645c9 --> m2dc3b7
  md06401 --> m2dc3b7
  ma7fa91 --> m33e04e
  mc30ece --> m2dc3b7
  m3db96b --> mdaa4f5
  m877222 --> mc60ea4
  m9dd0ca --> me1f093
  m9dd0ca --> m2dc3b7
  m012751 --> me1f093
  m71f606 --> m0c27d8
  m71f606 --> m2dc3b7
  mdada24 --> me1f093
  mdada24 --> m824cd0
  m2230c0 --> m71d0b1
  m2230c0 --> me1f093
  mdfcf6a --> m55d337
  m7a3bed --> m2dc3b7
  md74163 --> me1f093
  m0353e2 --> m3ee7cc
  m1ff499 --> mc60ea4
  m1ff499 --> m824cd0
  m946dd3 --> m2dc3b7
  mf7b8f6 --> m2dc3b7
  mcb93b3 --> me1f093
  m37d80c --> m2dc3b7
  m40e931 --> m33e04e
  m2b9ee7 --> md782d2
  m4cf4a4 --> me1f093
  m4cf4a4 --> m2dc3b7
  mea9bce --> mc60ea4
  m9725f5 --> mc60ea4
  me49444 --> m3dbf96
  m6dfebe --> m9725f5
  me812a9 --> me1f093
  me812a9 --> mc60ea4
  me812a9 --> m5c41ab
  m15bbc1 --> me1f093
  m15bbc1 --> m2dc3b7
  md3112a --> mdaa4f5
  m8a63c0 --> m824cd0
  m74d739 --> m2dc3b7
  md40cb8 --> m505731
  m6900a1 --> mdaa4f5
  m2dc3b7 --> m71d0b1
  m824cd0 --> m2dc3b7
  mb51b68 --> m5c41ab
  m2dc3b7 --> m9b3c4e
  me1f093 --> m71d0b1
  m7b893c --> me1f093
  m8900e5 --> mbc1344
  mfd6e81 --> mc60ea4
  m8778ad --> m55d337
  m8778ad --> m2dc3b7
  md920d3 --> m2dc3b7
  mc5aaca --> m55d337
  mec3b50 --> me1f093
  md996a0 --> m2dc3b7
  m065cdd --> mc60ea4
  m8f2419 --> mc60ea4
  me5bece --> mc60ea4
  m8f2419 --> m2dc3b7
  mc1a163 --> m2dc3b7
  m7c3d9b --> m4bb0fe
  m68533c --> mc60ea4
  m524d3b --> m824cd0
  m524d3b --> mdaa4f5
  m28f5b9 --> me1f093
  m62caf1 --> me1f093
  m058968 --> mdaa4f5
  m058968 --> mc60ea4
  mb70ea4 --> m9725f5
  mb70ea4 --> mc60ea4
  m3a6fc2 --> m505731
  m36d3a0 --> m2dc3b7
  m36d3a0 --> m505731
  m36d3a0 --> mb70ea4
  mdaa4f5 --> m2dc3b7
  mb751f6 --> mdaa4f5
  m3dbf96 --> m2dc3b7
  m923907 --> m55d337
  mc17e7d --> mc60ea4
  mc6f92e --> mdaa4f5
  mcb14b7 --> mf331c0
  m8aba19 --> md996a0
  m84ead1 --> m42e653
  mbdf25f --> m2dc3b7
  m140bcd --> m2dc3b7
  m9c6a97 --> m824cd0
  md92534 --> me1f093
  m0bd03e --> m662c17
  m53c378 --> mc60ea4
  m421ef0 --> m824cd0
  m421ef0 --> m32ee42
  m5086aa --> mc60ea4
  m1645c9 --> m4a7764
  m85e134 --> m2dc3b7
  mc60ea4 --> m55d337
  m512e66 --> mc60ea4
  mf92728 --> mc60ea4
  m75fab1 --> mc60ea4
  m525e3e --> m4db290
  m525e3e --> m75fab1
  mdaa4f5 --> me1f093
  m0e4866 --> mc60ea4
  mc30ece --> m71d0b1
  m58ef6b --> m405ca3
  m3db96b --> mc60ea4
  m3db96b --> m2dc3b7
  m03d133 --> m877222
  mb86bfc --> m6a2ec0
  mfd6ee0 --> mc60ea4
  m3e83b0 --> mfd6ee0
  mfd6ee0 --> m2dc3b7
  m3f9180 --> m3e83b0
  m878739 --> mdaa4f5
  m872bbc --> m824cd0
  mcf84c8 --> mdaa4f5
  mcf84c8 --> m55d337
  m71f606 --> mdaa4f5
  m0c27d8 --> mdaa4f5
  m0c27d8 --> m2dc3b7
  m2943ba --> m44867b
  m44867b --> m55d337
  m44867b --> m71d0b1
  mdf5304 --> m2dc3b7
  m662c17 --> mc60ea4
  m1dae83 --> mc60ea4
  m1dae83 --> m55d337
  mdfcf6a --> mc60ea4
  m7a3bed --> m55d337
  m55d337 --> me1f093
  mc412c9 --> m2dc3b7
  m9d4d8b --> m2dc3b7
  m9d4d8b --> m80365f
  md931fa --> mc60ea4
  md931fa --> m55d337
  m469ce0 --> mc60ea4
  m946dd3 --> m55d337
  m435001 --> mc60ea4
  m7f6995 --> m435001
  m37d80c --> mc60ea4
  ma789d5 --> me1f093
  ma789d5 --> m33e04e
  m33e04e --> mc60ea4
  m33e04e --> m2dc3b7
  m366d8e --> m2dc3b7
  md90551 --> me1f093
  m4a7764 --> m55d337
  m4a7764 --> m824cd0
  mb8c7f1 --> m71d0b1
  mb8c7f1 --> m2dc3b7
  m169f7a --> mc60ea4
  m169f7a --> m71d0b1
  m3506a9 --> m71d0b1
  m3ee7cc --> m55d337
  m3ee7cc --> ma6ec13
  m3ee7cc --> mc60ea4
  m5f5973 --> me1f093
  m5f5973 --> m2dc3b7
  m7b725e --> ma6ec13
  m44f235 --> m9b3c4e
  m44f235 --> m824cd0
  m44f235 --> m254daa
  m44c4ce --> md90551
  m35e373 --> m2dc3b7
  m35e373 --> me1f093
  me49444 --> mc60ea4
  m82c013 --> mc60ea4
  m9725f5 --> m824cd0
  m6dfebe --> m2dc3b7
  m9725f5 --> me1f093
  m9725f5 --> m55d337
  m8de4b3 --> m71d0b1
  m8a4347 --> m3dbf96
  m8de4b3 --> me1f093
  m8de4b3 --> m3dbf96
  mf0185d --> m8de4b3
  mf0185d --> m9725f5
  mf0185d --> m2dc3b7
  mf0185d --> m8f41f6
  m25b504 --> m8de4b3
  m25b504 --> m9b3c4e
  m25b504 --> m2dc3b7
  m98cff5 --> m2dc3b7
  me812a9 --> m824cd0
  m48c877 --> m5ac00e
  m254daa --> m824cd0
  m254daa --> m5ac00e
  m5ac00e --> mc60ea4
  mddbb55 --> m9725f5
  mddbb55 --> m662c17
  m8a63c0 --> md3112a
  m8a63c0 --> m9725f5
  md40cb8 --> m32ee42
  m6900a1 --> m7b725e
  m505731 --> md3112a
  m5c41ab --> m55d337
  m2dc3b7 --> mdaa4f5
  m824cd0 --> mc60ea4
  m824cd0 --> m55d337
  mb51b68 --> m2dc3b7
  m0975f8 --> m71d0b1
  m73fa11 --> m71d0b1
  ma6ec13 --> m55d337
  m409911 --> me1f093
  m409911 --> m71d0b1
  m2dc3b7 --> m9725f5
  me1f093 --> m55d337
  m09f7c4 --> mc60ea4
  mbc1344 --> m71d0b1
  mbc1344 --> m824cd0
  m8900e5 --> mc60ea4
  m8900e5 --> m824cd0
  mfd6e81 --> mbc1344
  mfd6e81 --> m55d337
  m02661c --> m824cd0
  m02661c --> m55d337
  m8778ad --> mc60ea4
  m430c8d --> m2dc3b7
  m926fc3 --> m2dc3b7
  md996a0 --> m55d337
  md996a0 --> m824cd0
  mf943df --> mc60ea4
  m7fe89c --> mc60ea4
  m553d41 --> m065cdd
  mb11552 --> m2dc3b7
  m726974 --> m0d712b
  m43d11d --> mc60ea4
  m03d64d --> m2dc3b7
  m8f2419 --> mdaa4f5
  mc22155 --> m55d337
  mc22155 --> m2dc3b7
  mc22155 --> me1f093
  mc22155 --> mdaa4f5
  mc1a163 --> m3dbf96
  m376622 --> mc1a163
  m663680 --> mdaa4f5
  m4bb0fe --> m55d337
  m4bb0fe --> mdaa4f5
  m68533c --> me1f093
  m65f051 --> mdaa4f5
  m524d3b --> m55d337
  m524d3b --> me1f093
  mf852b3 --> mc60ea4
  mf852b3 --> mdaa4f5
  m62caf1 --> mc60ea4
  m62caf1 --> m28f5b9
  maa2c69 --> m2dc3b7
  mb70ea4 --> md3112a
  mb70ea4 --> m71d0b1
  mb70ea4 --> mdaa4f5
  mb70ea4 --> m55d337
  mb70ea4 --> m2dc3b7
  m3b5d41 --> mc30ece
  m3a6fc2 --> mc7c2ea
  m3a6fc2 --> m9d4d8b
  mcb7e15 --> mdaa4f5
  mde612a --> m55d337
  mb69e33 --> mdaa4f5
  mb69e33 --> mc60ea4
  mb69e33 --> mde612a
  mb69e33 --> m140bcd
  mde612a --> m71d0b1
  m2a8005 --> mdaa4f5
  mb751f6 --> m71d0b1
  mb751f6 --> m140bcd
  mb751f6 --> m254daa
  mb751f6 --> ma6ec13
  mb751f6 --> m2dc3b7
  m3dbf96 --> m71d0b1
  m3dbf96 --> mdaa4f5
  m923907 --> mc60ea4
  m83d2e5 --> mdaa4f5
  m83d2e5 --> mc60ea4
  m624c21 --> mc60ea4
  m0201da --> mc60ea4
  mc17e7d --> mdaa4f5
  ma7d473 --> mdaa4f5
  m81cbda --> mc60ea4
  md1083b --> mc60ea4
  m14906f --> mc60ea4
  m908892 --> mc60ea4
  mc6f92e --> mc60ea4
  mf331c0 --> mc60ea4
  mc6f92e --> m2dc3b7
  mdaa4f5 --> m824cd0
  m2a5acc --> mc60ea4
  mff82f4 --> mc60ea4
  m4ee999 --> m55d337
  m7ec249 --> m2dc3b7
  m2ac823 --> mc60ea4
  m2ac823 --> m55d337
  m4f7507 --> m55d337
  m4f7507 --> m2dc3b7
  m4f7507 --> mdaa4f5
  mf57999 --> m2dc3b7
  mf57999 --> mdaa4f5
  m023429 --> m878739
  m023429 --> m44867b
  m179dbc --> mdaa4f5
  m179dbc --> mf57999
  mc5989c --> mdaa4f5
  mc5989c --> m0c27d8
  m56fe87 --> m2dc3b7
  m140bcd --> m55d337
  m010ad4 --> mc60ea4
  m01e40b --> me1f093
  m073edb --> mc60ea4
  m82bd9d --> m11e006
  m82bd9d --> m9d4d8b
  m82bd9d --> m0bd03e
  m073edb --> mdaa4f5
  m53c378 --> mdaa4f5
  m421ef0 --> me1f093
  m346909 --> mc60ea4
  m346909 --> m824cd0
  m346909 --> m512e66
  m346909 --> m877222
  m0663eb --> m824cd0
  m860e05 --> m824cd0
  m512e66 --> mdaa4f5
  md56f47 --> m421ef0
  m1645c9 --> m0663eb
  m1645c9 --> m5c41ab
  m512e66 --> m55d337
  m512e66 --> m2dc3b7
  mdaa4f5 --> mde612a
  mf92728 --> m2dc3b7
  m525e3e --> m2dc3b7
  m525e3e --> mdaa4f5
  m525e3e --> m505731
  mabfbcd --> mc60ea4
  m0e4866 --> mdaa4f5
  mc30ece --> m55d337
  mc30ece --> mdaa4f5
  mc30ece --> ma6ec13
  m405ca3 --> mc60ea4
  m58ef6b --> mc60ea4
  m4edef8 --> m254daa
  mdaa4f5 --> ma6ec13
  mdaa4f5 --> m9b3c4e
  m877222 --> mdaa4f5
  m6a2ec0 --> mc60ea4
  mb86bfc --> m4a7764
  m3e83b0 --> m55d337
  m3f9180 --> m3ee7cc
  ma304c1 --> mdaa4f5
  ma304c1 --> m71d0b1
  m2ae093 --> m2dc3b7
  m012751 --> mdd6624
  m012751 --> mdceda9
  m2a55e2 --> mdceda9
  m872bbc --> mc60ea4
  m878739 --> m824cd0
  m878739 --> m9725f5
  m71f606 --> m7b725e
  m0c27d8 --> mc60ea4
  mdd6624 --> m2dc3b7
  mdd6624 --> mc60ea4
  m2230c0 --> m44867b
  m26ce79 --> mc60ea4
  m662c17 --> m2dc3b7
  m662c17 --> m254daa
  m1dae83 --> mdaa4f5
  m1dae83 --> m2dc3b7
  mdfcf6a --> me1f093
  mdfcf6a --> m7a3bed
  m7a3bed --> mdaa4f5
  m7a3bed --> m366d8e
  md74163 --> mc60ea4
  m55d337 --> m3dbf96
  mc412c9 --> mc60ea4
  mc412c9 --> m8f41f6
  m9d4d8b --> m2943ba
  m9d4d8b --> m44867b
  m9d4d8b --> m7a3bed
  m9d4d8b --> mc60ea4
  md931fa --> mdaa4f5
  md931fa --> m2dc3b7
  m469ce0 --> mdaa4f5
  m469ce0 --> m2dc3b7
  m0353e2 --> m71d0b1
  m0353e2 --> m7b725e
  mdceda9 --> m55d337
  m559711 --> m2dc3b7
  mdceda9 --> m4a7764
  m1ff499 --> m55d337
  m1ff499 --> mdceda9
  m09665a --> mc60ea4
  mf7b8f6 --> m824cd0
  m9b3c4e --> me1f093
  m9b3c4e --> mdceda9
  m435001 --> m55d337
  m18e7a9 --> m7a3bed
  m18e7a9 --> m824cd0
  m18e7a9 --> m435001
  m7f6995 --> m2dc3b7
  m7f6995 --> mdaa4f5
  m7f6995 --> m7b725e
  m435001 --> mdaa4f5
  mce6bc7 --> mc60ea4
  ma789d5 --> m824cd0
  ma789d5 --> mc60ea4
  m366d8e --> mdaa4f5
  md90551 --> mc60ea4
  md90551 --> m2dc3b7
  m597684 --> m9725f5
  ma0f373 --> mc30ece
  m19e2ac --> m71d0b1
  m19e2ac --> m55d337
  md90551 --> m71d0b1
  md90551 --> mfd6e81
  md90551 --> ma6ec13
  m416bf2 --> md782d2
  md782d2 --> m71d0b1
  md782d2 --> mc60ea4
  md782d2 --> mdaa4f5
  md782d2 --> m2dc3b7
  m9b3c4e --> mdaa4f5
  m4a7764 --> m2dc3b7
  mcd4b88 --> mea9bce
  mab83e4 --> m71d0b1
  mab83e4 --> m3ee7cc
  m71d0b1 --> mdaa4f5
  m71d0b1 --> me1f093
  mb8c7f1 --> me1f093
  m778e60 --> me1f093
  m778e60 --> m169f7a
  m778e60 --> m3ee7cc
  m169f7a --> m55d337
  m169f7a --> me1f093
  m169f7a --> m2dc3b7
  m71d0b1 --> m9b3c4e
  m71d0b1 --> m55d337
  m8f41f6 --> mdaa4f5
  m58f268 --> mdaa4f5
  m58f268 --> m71d0b1
  m332c4b --> m8f41f6
  m3d9f10 --> m3ee7cc
  m3506a9 --> m8f41f6
  m3506a9 --> m55d337
  m3506a9 --> m2dc3b7
  m3ee7cc --> mdaa4f5
  m3ee7cc --> m2dc3b7
  m7b725e --> me1f093
  m7b725e --> mdaa4f5
  m7b725e --> m5f5973
  m7b725e --> m2dc3b7
  m5f5973 --> mc60ea4
  m5f5973 --> m55d337
  m5f5973 --> m71d0b1
  m71d0b1 --> m824cd0
```

## How a request flows

1. `saleor/app/tests/fixtures/app.py` receives the request and dispatches into the modules above.
1. `saleor/graphql/app/dataloaders/app.py` receives the request and dispatches into the modules above.

## Key decisions & gotchas

- Module boundaries came from directory structure, so a module is a folder, not
  necessarily a concept.
- Measured edges are import-derived; runtime-only wiring (events, DI, HTTP) does
  not appear as a solid arrow.
- Module set fingerprint: `50d80cc26d88` — this moves only when
  modules are added, removed, or renamed, which is the signal an architecture
  change was picked up.
