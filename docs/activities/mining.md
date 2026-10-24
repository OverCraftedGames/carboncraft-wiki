---
icon: material/pickaxe
---

<!-- Sources (live): PyroMining config.yml (Fluxes = Carbon, Gemstones, MysteriousDust,
     Artifacts, Vessels, Runes, Oracles, Zeta, MiningLevels; Halloween event disabled),
     messages.yml (journal text, vessel list, gemstone names, command list),
     DeluxeMenus help.yml (PyroMining button). Checked 2026-10-24.
     Blacksmith is "not implemented" per the plugin's own journal text, so it's left out. -->

# Mining

CarbonCraft runs **PyroMining**, which turns every ore you break into progress. Ores
give mining XP and **Zeta** (mining's own currency), and they sometimes drop Carbon,
gemstones, artifacts and Mysterious Dust. Further in, you summon bosses and add
**Vessels** to your pickaxe: permanent, levelable pickaxe enchantments.

The plugin has its own in-game guide: `/mine journal`.

## Commands

| Command | Opens |
|---|---|
| `/mine menu` | The main mining menu |
| `/mine journal` | The Miner's Journal: an in-game guide to every item and system |
| `/mine shop` | Sell Carbon, gemstones and artifacts |
| `/mine stats` | Your mining level, XP, Zeta and finds |
| `/mine artifacts` | Identify artifacts and fossils, and buy upgrades |
| `/mine vessels` | Fight and manage the Vessels on your pickaxe |
| `/mine singularity` | Spend runes on permanent upgrades |
| `/mine zeta` | Your Zeta balance |

**Shift-click with your pickaxe** to open a mining menu instantly. Choose which menu in
`/mine menu` under **Pickaxe View**.

## Mining level and Zeta

Every ore you break gives mining XP and Zeta.

| Ore | Mining XP | Zeta |
|---|---|---|
| Coal, Nether quartz | 15 | 30 |
| Iron | 25 | 40 |
| Redstone | 35 | 70 |
| Gold | 40 | 90 |
| Lapis | 50 | 130 |
| Diamond | 150 | 350 |
| Emerald | 200 | 400 |

Deepslate versions count the same. Level 1 needs 2,000 XP, and each level after that
needs 12.5% more than the one before. Your level unlocks later content: Mysterious Dust
gives better drops from level 20, and you can summon Oracles from level 40.

Zeta pays for artifact upgrades and Vessels. `/mine menu` can withdraw it 10,000 at a
time as an item, so you can trade it with other players.

## What ores drop

### Carbon

**Carbon** is CarbonCraft's core resource. Every Overworld ore (coal, iron, copper,
gold, redstone, lapis, diamond and emerald) has a 5% chance to drop one. Nether ores
never do.

Carbon sells for only $10 in `/mine shop`. It's worth more spent elsewhere:

- hand it to a [Syndicate faction](../syndicates/index.md#requisitions-hand-in-carbon) for standing
- deliver it to the current megaproject (`/megaproject`)

### Gemstones

Each gemstone has a 2% chance to drop from its own ore.

| Gemstone | Ore | Base price |
|---|---|---|
| Peridot | Coal | $50 |
| Ruby | Redstone | $75 |
| Topaz | Nether quartz | $100 |
| Amethyst | Lapis | $150 |
| Sapphire | Emerald | $200 |
| Tiger's Eye | Diamond | $250 |

Sell them as they are, or **right-click** one first to examine its quality. Examining is
a gamble: quality ranges from Ruined (70% of base price) to Pristine (150%).

### Artifacts

Rarely, an ore drops a sealed artifact. Right-click it to unseal it, then place it in
`/mine artifacts` to identify it. Identifying takes real time (20 minutes for Basic, up
to almost 5 hours for Divine), and can turn up a **fossil**: a piece of a Vessel.

| Tier | Chance | Identify time | Sell price |
|---|---|---|---|
| Basic | 42% | 20 min | $50 |
| Unusual | 21% | 40 min | $80 |
| Epic | 14% | 1 h | $150 |
| Exceptional | 10% | 1 h 30 min | $300 |
| Legendary | 6% | 2 h | $400 |
| Fabled | 4% | 2 h 40 min | $500 |
| Mythic | 2.4% | 3 h 20 min | $600 |
| Celestial | 0.5% | 4 h | $750 |
| Divine | 0.1% | 4 h 40 min | $1,000 |

Don't want to wait? Sell the artifact unidentified in `/mine shop` instead. Fossils
take another hour to identify, and each one becomes one part of a random Vessel.

### Mysterious Dust

Ores have a 1% chance to drop Mysterious Dust. Process it in a **Refinery**: place a
dropper facing up, put a fence on top of it, put the dust inside, then interact with
the fence. Each dust can yield:

| Item | Chance | Needs mining level | Used for |
|---|---|---|---|
| Rune Dust | 75% | any | Summoning Rune Guardians |
| Shattered Requium Orb | 10% | 30 | Making Requiums |
| Ancient Relic | 7% | 25 | Raising a sealed artifact's tier by 1 |
| Oracleite | 4% | 20 | Summoning Oracles |

## Vessels

Vessels are permanent enchantments for your pickaxe, and getting one means beating a
boss.

1. **Collect all 8 parts** of a Vessel by identifying fossils.
2. **Craft it**: put all 8 parts in a Refinery.
3. **Drag the Vessel onto your pickaxe** to start it. The item shows the mining level
   and Zeta it needs.
4. **Defeat the Vessel's boss with Requiums.** You need three Requiums in the right
   order, set in `/mine vessels`. You can guess, or kill the **Thralls** that turn up
   while you mine (at most one every 2 minutes); each kill reveals more of the correct
   order. Once the boss is dead, the Vessel's effect is added to your pickaxe.

There are 12 Requiums, and you get them from Tier 3 or higher artifacts once you've
bought the *Final Whisper* upgrade in `/mine artifacts`. Adding a second Vessel of the
same type levels it up.

| Vessel | What it does | Max level bonus |
|---|---|---|
| Aurora's Blaze | Auto-smelts iron and gold ore | 25% chance of a bonus ingot |
| Valakas' Nightfall | Chance of Haste II for 30–100 seconds when you break ore | Haste III instead |
| Neptulus' Wave | Bonus mining XP | 10% chance of triple XP |
| Skylark's Dream | Carbon sells for more | 20% chance of bonus Carbon |
| Rezoth's Destruction | Chance for an ore to drop another ore's mineral too | 10% chance to double it |
| Imperos' Winds | Better chance of rarer artifacts | +5% fossil chance |
| Nagyn's Tranquility | Better chance of Mysterious Dust | 20% chance of double dust |
| Nefaris' Shadows | Better rune drops from Rune Guardians | 60% chance of a bonus rune |
| Xostran's Glare | Better Oracle drops | 20% chance of double drops |

The full list, including each Vessel's quirks, is in `/mine journal`.

!!! warning "Removing Vessels costs 100,000 Zeta"
    **Remove all Vessels** in `/mine vessels` returns every Vessel on the pickaxe you're
    holding. There's no confirmation step.

## Rune Guardians and the Singularity

Hold **Rune Dust** and right-click redstone ore to summon a **Rune Guardian**, a
mini-boss with 270 health that hits for 12. It's immune to damage while standing in
water, and you can summon one every 60 seconds. Guardians drop **runes** (Nature,
Ghost, Water, Fire, Fairy, Lightning and Ground).

Spend runes in `/mine singularity` to level your **Singularity**. Each level needs one
more rune than the last, and there's no level cap. Each level gives a point to spend on:

- **Cheaper Upgrades:** artifact-menu upgrades cost less
- **Requium Progress:** more progress per Thrall kill
- **Rune Drop Chance:** Rune Guardians drop runes more often
- **More Zeta:** more Zeta from every source
- **Oracle Damage:** take less damage from Oracles

## Oracles

Oracles are PyroMining's end-game bosses. Uncharged **Oracleite** (from Mysterious
Dust) becomes charged after you mine 35 diamond ore. Use the charged Oracleite on
emerald ore to summon the first Oracle. Each Oracle drops the rune that summons the next one, and you can summon one
once an hour.

| Phase | Oracle | Element | Health | Mining level | Summoned with |
|---|---|---|---|---|---|
| 1 | Radalite | Fire (stronger if you fight in water) | 1,100 | 40 | Charged Oracleite |
| 2 | Impulse | Lightning (explodes) | 1,600 | 45 | Hell Rune |
| 3 | Tohka | Darkness (swaps immunities every 20 seconds) | 2,000 | 50 | Light Rune |

Oracles bring minions, and they teleport to you if you trap them. They drop high-tier
artifacts, Zeta Tears and other rare materials. Every Oracle kill is announced to the
whole server.
