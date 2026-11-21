---
icon: material/handshake
title: The Syndicate
---

<!-- Sources (live): DeluxeMenus gui_menus/syndicate/standing.yml (open commands, blurbs),
     syndicate/<faction>/detail.yml (rank ladder, requisition buttons), lore.yml (28 entries,
     one per 100 standing, 2 written per faction); CarbonContribute config.yml (requisitions:
     10 per rep, daily cap 15, ceiling 1000) and shop-items.yml (all 28 items: 250/$50k/+10,
     1000/$150k/+20, 2500/$300k/+40); megaproject_rewards.yml (+20 CarbonCorp, +5 others);
     EcoAnvilFix config.yml (locked-enchants: syndicate_tech). Images: wiki-images/syndicates
     (recreations built 2026-10-08, matched against live 2026-10-24).
     Re-checked 2026-11-15: standing.yml is now one hub (row per faction: shop, daily,
     weekly, requisition, lore; /carboncorp etc. open it too); lore.yml view thresholds
     0..2500 (uneven), entries 1-10 written; CarbonCore/CarbonContribute/config.yml
     contracts (1 daily + 1 weekly per faction, 20 daily 10 rep/$1,000, 8 weekly
     60 rep/$7,500, deliver or kill, ignore-spawner-mobs, America/Edmonton, weeks start
     Monday). Image 02 still shows the old standing screen. -->

# The Syndicate

![The Syndicate: four factions, one planet, pick a side](../assets/syndicates/01-title-card.webp)

Four factions are fighting over Isernium, the planet OCG Survival takes place on. Each
one tracks your **standing** separately. Raise it, and that faction opens its shop of
gear you can't get anywhere else.

| Faction | Who they are | Their gear is for |
|---|---|---|
| [CarbonCorp™](carboncorp.md) | The megacorporation that brought everyone to Isernium | Mining and farming |
| [ISD](isd.md) | Isernium Sentinel Division: law, order and oversight | Combat |
| [The Union](union.md) | The workers. Reform, not revolution. For now. | Playing in a group |
| [Vivec's Rebels](rebels.md) | Deserters and saboteurs selling jailbroken tech | Solo risk-takers |

You don't have to pick only one. Standing with one faction never lowers your standing
with another, so you can work your way up with all four.

## 1. Check your standing

Type `/syndicate` (or `/rep`, `/standing`, or a faction's name such as `/union`) to
open the Syndicate hub. Each faction has one row: your standing with it, then its
shop, its daily and weekly contracts, its requisition desk and its lore archive.

![The standing menu and rank ladder](../assets/syndicates/02-standing-menu.webp)

| Rank | Standing |
|---|---|
| Hostile | below 0 |
| Neutral | 0 – 249 |
| **Associate** | 250 – 999 |
| **Trusted** | 1,000 – 2,499 |
| **Inner Circle** | 2,500+ |

Everyone starts at 0 (Neutral) with all four factions.

## 2. Earn standing

### Requisitions: hand in Carbon

In the hub, click a faction's requisition button to hand Carbon straight to that
faction. **Carbon** turns up while you mine ore in the Overworld.

![Handing in Carbon at the requisition desk](../assets/syndicates/03-requisition.webp)

| | |
|---|---|
| Rate | 10 Carbon = +1 standing |
| Daily limit | 150 Carbon (+15 standing) per faction |
| Ceiling | Carbon stops counting once you reach 1,000 standing with that faction |
| Left-click / Shift-left-click / Right-click | hand in 10 / 50 / 100 |

!!! warning "There is no confirmation"
    Carbon is taken the moment you click and can't be refunded. If a click would go
    over the daily limit or the ceiling, nothing is taken.

The daily limit is per faction, so you can hand in 150 Carbon to each of the four
every day.

### Contracts

Every faction posts one **daily** and one **weekly** contract on its board. Everyone
sees the same contracts, and each one is either a delivery or a kill count.

| | Daily | Weekly |
|---|---|---|
| Standing | +10 | +60 |
| Money | $1,000 | $7,500 |
| Resets | every day | every Monday |

- **Deliveries:** click the contract in the hub to hand in what you're carrying. You
  can deliver in several trips; the contract tracks your progress.
- **Kill contracts** count up as you fight. Mobs from spawners don't count.

Contracts have no daily limit beyond the board itself and keep paying standing past
1,000. Days and weeks reset on Mountain Time (America/Edmonton).

### Buying from the faction shop

Every shop purchase raises your standing with that faction: **+10** for an Associate
item, **+20** for Trusted and **+40** for Inner Circle. Past 1,000 standing, the
shop and contracts are how you keep climbing.

### Server projects

Some server-wide events pay standing too. Qualifying for the rewards of the Planetary
Refinery megaproject (`/megaproject`) gives +20 CarbonCorp and +5 with each of the
other three.

## 3. Spend it in the faction shop

Each faction sells seven pieces of gear across three tiers. Your standing decides which
tier you can buy from.

![A faction shop, showing price, requirement and availability](../assets/syndicates/04-faction-shop.webp)

| Tier | Standing needed | Price | Standing gained |
|---|---|---|---|
| 1 · Associate | 250+ | $50,000 | +10 |
| 2 · Trusted | 1,000+ | $150,000 | +20 |
| 3 · Inner Circle | 2,500+ | $300,000 | +40 |

- You can buy **each item once every 30 days**. The item's tooltip shows when you can
  buy it again.
- Tier 1 gear is iron, Tier 2 is diamond, and Tier 3 is netherite.
- Every item carries one faction **perk**, a custom enchant you can't get any other way.

## Syndicate Tech

Every shop item carries **Syndicate Tech**: the faction's proprietary technology. It
locks the item exactly as you bought it.

![Syndicate Tech blocks anvils, grindstones and smithing tables](../assets/syndicates/09-syndicate-tech.webp)

- **No anvil:** no enchanting, combining, renaming or repairing.
- **No grindstone:** the enchants stay on.
- **No smithing table:** no netherite upgrade and no armour trims.

Tier 3 gear has Mending. Tier 1 and 2 gear doesn't, so when it wears out, buy a
replacement.

## Lore archives

Each faction has a lore archive with 28 entries, opened from its row in the hub. The
first entry is free, and the rest unlock as your standing with that faction rises,
roughly every 100 standing, up to the last one at 2,500. The first ten entries are
written for every faction, and more are on the way.
