---
icon: material/cash-multiple
---

<!-- Sources (live): CMI config.yml (StartingAmount); DeluxeMenus help.yml, chestshop.yml,
     wallet.yml, votetiers.yml; CMI CustomAlias (wallet, coinshop, voteshop, crates, pw);
     tip_crates.txt. Checked 2026-10-24. -->

# Money & currencies

CarbonCraft has four things you can earn and spend. `/wallet` shows all of them at once.

| Currency | How you earn it | Where you spend it |
|---|---|---|
| **Dollars ($)** | Selling to players, vote tiers, Zombies runs | Player shops, auctions |
| **CarbonCoins** | A perfect vote day (all 6 sites), the store | `/coinshop` |
| **Vote points** | Every vote | `/voteshop` |
| **Crate keys** | Voting, milestones, the store | `/crates` |

You start with **$200**.

## A player-run economy

The server doesn't sell or buy items at fixed prices. Every price was set by a player
who had to collect the item first. Two places to trade:

### Chest shops

A shop is a chest with a sign on it.

1. Place a chest (or barrel) **inside your claim**.
2. Put a sign on the chest, or on the block above it.
3. Fill in the four lines:

| Line | What goes there | Example |
|---|---|---|
| 1 | Leave blank (your name is filled in) | |
| 2 | How many per purchase | `64` |
| 3 | The price | `B 100` |
| 4 | The item, or `?` to fill it in automatically | `?` |

4. Stock the chest with what you're selling.

If a line is wrong, chat tells you which one. `/shophelp` walks you through it in
game, price formats included.

### Player warps

Set a warp to your shop so other players can find it: `/pw` opens the warp list. Your
first warp unlocks at vote tier I, with more at higher tiers.

## CarbonCoins

CarbonCoins are CarbonCraft's premium currency. You earn them by voting on all six
sites in one day: the reward climbs every day of the week, up to 56 coins for a perfect
week. They're also sold on the [store](https://store.carboncraft.xyz). Spend them in
`/coinshop`.

## Crate keys

Keys go straight into your account, so they don't take up inventory space. Type
`/crates` to warp to the crates and open them. There are five crates, from common to
rare: **Vote**, **Carbon**, **Plasma**, **Fusion** and **Iridium**. Rarer crates have
better rewards and longer odds.
