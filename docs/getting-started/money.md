---
icon: material/cash-multiple
---

<!-- Sources (live): CMI config.yml (StartingAmount); DeluxeMenus help.yml, chestshop.yml,
     wallet.yml, votetiers.yml; CMI CustomAlias (wallet, coinshop, voteshop, crates, pw);
     tip_crates.txt. Checked 2026-10-24.
     Re-checked 2026-11-15: VoteSites.yml ($50 per vote); DailyRewardsPlus Rewards.yml
     (monthly rotation, money on several days); ExcellentCrates crates/ (vote, carbon,
     plasma, fusion, iridium, fishing, zombie, seasonal halloween); wallet.yml keys. -->

# Money & currencies

OCG Survival has four things you can earn and spend. `/wallet` shows all of them at once.

| Currency | How you earn it | Where you spend it |
|---|---|---|
| **Dollars ($)** | Selling to players, $50 per vote, vote tiers, daily login rewards, Zombies runs | Player shops, auctions |
| **Credits** | A perfect vote day (all 6 sites), OCG+, the store | `/coinshop` |
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

## Credits

Credits are the OCG Network currency. Your balance is shared by every OCG server, so a
Credit spent on one server is gone on the others too.

- **Earn them** by voting on all six sites in one day: the reward climbs every day of the
  week, up to 56 Credits for a perfect week (see [Credits week](voting.md#credits-week)).
- **Buy them** in packs on the [store](https://minecraft.ocgames.xyz/credits.html). Every
  [OCG+](https://minecraft.ocgames.xyz/plus.html) tier also pays Credits each month.
- **Spend them** in `/coinshop` on tags, join messages, plushies, crate keys and more.

`/credits` shows your balance, `/credits history` lists everything you've bought and spent
(and on which server), and `/credits top` shows the highest balances. Credits can't be
sent to other players directly; ask staff if you need to move some to a friend.

!!! note "Had CarbonCoins?"
    CarbonCoins became Credits when CarbonCraft joined OCG Network. Every balance carried
    over 1:1, automatically.

## Crate keys

Keys go straight into your account, so they don't take up inventory space. Type
`/crates` to warp to the crates and open them. The main crates, from common to rare,
are **Vote**, **Carbon**, **Plasma**, **Fusion** and **Iridium**. Rarer crates have
better rewards and longer odds.

Two more have their own source:

- **Fishing** keys are sold in `/coinshop` and `/voteshop`.
- **Zombie** keys are wave rewards in the Zombies arena.

Seasonal crates, like the Halloween crate, show up during events.
