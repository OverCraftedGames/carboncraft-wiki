---
icon: material/fish
---

<!-- Sources (live): PyroFishingPro config.yml (tier prices/chances, Entropy, FishingXP,
     PartyFishing, Augments RequiredLevel, Scales, GuttingStation, Totems passives,
     Deliveries, SpecialFish, crabs, broadcasts, AllowAutoFishers false), fish.yml
     (157 fish: 34/21/25/26/31/20), bait.yml, tournaments.yml (AutoStart, min 10 players,
     600 s, 6 fixed times, rewards), messages.yml (descriptions, command list).
     Augments CheckForLevel is false; levels listed are the ones the augment item shows.
     Crab Crusher and Snow Globe (event augments) left out. Checked 2026-10-24. -->

# Fishing

CarbonCraft runs **PyroFishingPro**. On top of vanilla fishing you can catch 157
custom fish across six tiers. Catches level you up and earn **Entropy**, fishing's own
currency, which you spend on **augments** for your rod.

**Shift-click while holding a fishing rod** to open the fishing menu, or type `/fish menu`.

## Commands

| Command | Opens |
|---|---|
| `/fish menu` | The main fishing menu |
| `/fish codex` | Every fish, where it lives and which ones you've caught |
| `/fish shop` | Sell fish, including the Fish of the Day |
| `/fish bag` | Your fish bag |
| `/fish scales` | Weigh a fish to gamble on its price |
| `/fish gut` | The gutting station: turn fish into Entropy |
| `/fish augment` | Craft and apply augments |
| `/fish augments` | List every augment |
| `/fish deliveries` | Fish deliveries |
| `/fish skills` | Your fishing skills |
| `/fish stats` | Your fishing level and catches |
| `/fish entropy` | Your Entropy balance |
| `/fish boosters` | Lures and boosters currently active |

## Fish tiers

Each cast has a chance to land a custom fish instead of a vanilla one. Many fish only
bite in certain biomes, at certain times or in certain weather; `/fish codex` shows
where to find each one.

| Tier | Fish | Chance | Sells for | Entropy | Fishing XP |
|---|---|---|---|---|---|
| Bronze | 34 | 50% | $10 | 45 | 75 |
| Silver | 21 | 25% | $55 | 110 | 150 |
| Gold | 25 | 5% | $150 | 200 | 300 |
| Diamond | 26 | 2% | $500 | 350 | 700 |
| Platinum | 31 | 1% | $1,000 | 1,250 | 1,900 |
| Mythical | 20 | 0.04% | $2,500 | 10,000 | 6,000 |

Platinum and Mythical catches are announced to the whole server.

### Fish together

**Party fishing:** you earn more XP and Entropy when other players are fishing within
30 blocks of you. The full bonus kicks in with four players fishing nearby.

### Crabs

There's a 4% chance to reel in a **Crab** instead of a fish. Kill it for **Crab Claws**
and **Crab Scales**, which are augment ingredients. **Dolphin Tails** (from dolphins)
and **Squid Tentacles** (from squid) are ingredients too, and Looting improves the
drop chance.

## Selling and the Fish of the Day

Sell fish in `/fish shop`. One fish is the **Fish of the Day**: it sells for 1.5× its
normal price, and it changes every 6 hours.

### Scales

`/fish scales` lets you gamble on a fish's price. Pick a risk level:

| Risk | Chance of profit | Price swing |
|---|---|---|
| Low | 70% | ±20% |
| Medium | 60% | ±40% |
| High | 50% | ±60% |
| Extreme | 40% | ±80% |

A win raises the sell price by up to the swing; a loss lowers it by up to the same amount.

## Entropy

You earn Entropy from every custom fish you catch, and you can **gut** fish for more in
`/fish gut`:

| Gutting a… | Bronze | Silver | Gold | Diamond | Platinum |
|---|---|---|---|---|---|
| gives Entropy | 40 | 120 | 200 | 500 | 1,000 |

In `/fish augment` you can turn 10,000 Entropy into an **Entropy Crystal**, an item you
can trade to other players. Right-click a crystal to redeem it.

## Augments

Augments are upgrades for your fishing rod. Craft them in `/fish augment` from Entropy
plus ingredients (the recipe is on each augment), then apply them to your rod. Each
one has several levels.

| Augment | Level | What it does |
|---|---|---|
| Hot Spot | 10 | Chance to catch several fish in one cast (not while raining) |
| Call of the Storm | 12 | Chance to catch several fish in one cast, only while raining |
| Saturate | 12 | Chance to refill your hunger when you catch a fish |
| Sage | 12 | More fishing XP from catches |
| Biome Disruption | 16 | Chance to catch fish from any biome |
| Precision Cutting | 22 | More Entropy from gutting |
| Intellect | 25 | More vanilla XP from catches |
| Crab Bait | 25 | Higher chance to catch Crabs |
| Perception | 28 | More Entropy from catching custom fish |
| Solar Rage | 35 | More money when selling fish |
| Trophy | 35 | Better odds at the scales |
| Master Fisherman | 45 | Higher chance of higher-tier fish |

## Bait

Some rare fish only bite on a specific bait. Bait costs $1,000 in the bait store (in
`/fish menu`), needs fishing level 10, and lasts 50–75 catches. Drag it onto your rod
to apply it. The codex shows which fish need which bait. CarbonCraft's own **Pure
Carbon Spike** catches the Carbon Fiber Cutlass and the Man o' Carbon.

## Deliveries

For every **125 custom fish** you catch, you earn a delivery. Open `/fish deliveries`,
hand over the fish it asks for, and after a wait (15 minutes for common deliveries, up
to 10 hours for mythical ones) you collect the rewards: augment ingredients, Entropy
Crystals, **lures** that raise your Crab, Platinum or Mythical odds for 30 minutes,
and **Entropy boosters**.

## Totems

A totem is a structure you build that powers up fishing around it. `/fish menu` shows
the exact layout; build it block-for-block, then right-click the first observer with a
fishing rod and hand over the items it asks for. You can own one totem.

Totems have passives that unlock as your fishing level rises:

| Passive | Unlocks at level |
|---|---|
| Experienced Fisherman | 20 |
| Little Critters | 40 |
| Fish Schools | 40 |
| Random Drops | 55 |
| Mythical Waters | 60 |
| Treasure Hunter | 60 |
| Entropy Horder | 60 |
| Star Fall | 100 |

## Tournaments

Fishing tournaments start automatically every four hours (00:00, 04:00, 08:00, 12:00,
16:00 and 20:00 server time) **if at least 10 players are online**. Each one lasts 10
minutes, with a random goal: longest fish, shortest fish, most catches, most crabs
killed, longest cast, most biomes, most Entropy, or catching a specific fish.

| Place | Reward |
|---|---|
| 1st | $1,000 |
| 2nd | $650 |
| 3rd | $250 |
| Everyone who takes part | 500 Entropy |

!!! note "No autofishers"
    AFK fishing machines don't work here.
