---
icon: material/sword-cross
---

<!-- Sources (live): EcoSkills stats/*.yml (placeholders and effect args; health and
     attack_speed have gui enabled: false and no skill grants them, so they're left out),
     effects/*.yml (placeholders), skills/*.yml rewards (levels per skill level,
     start-level). "At level 50" = effect level 50 - start-level + 1. Values are the ones
     the in-game description shows. Checked 2026-10-24. -->

# Stats & effects

Skills reward you in two ways:

- **Stats** are points that add up across all your skills and gear.
- **Effects** belong to one skill each and get stronger every level.

Both are permanent. You keep them however you play.

## Stats

| Stat | Each point gives |
|---|---|
| 🛡 Defense | 0.25% less damage taken |
| 🗡 Strength | 0.25% more damage (melee, bows and tridents) |
| ※ Crit Chance | 1% chance to land a critical hit (up to 100%) |
| ☠ Crit Damage | Crits deal 50% more damage to start with, plus 0.5% per point |
| 🔥 Ferocity | 0.5% chance to deal your damage twice |
| ✦ Speed | 1% faster movement |
| ✎ Wisdom | 1% more experience |

### Stats from each skill

| Skill | Every level | At level 50 |
|---|---|---|
| Mining | +2 Defense; +1 Ferocity from level 15 | 100 Defense, 36 Ferocity |
| Woodcutting | +2 Strength, +1 Crit Damage | 100 Strength, 50 Crit Damage |
| Farming | +2 Crit Damage, +1 Wisdom | 100 Crit Damage, 50 Wisdom |
| Fishing | +2 Defense, +1 Wisdom | 100 Defense, 50 Wisdom |
| Combat | +2 Strength; +1 Ferocity from level 15 | 100 Strength, 36 Ferocity |
| Armory | +2 Defense, +1 Speed | 100 Defense, 50 Speed |
| Exploration | +2 Speed, +1 Crit Chance | 100 Speed, 50 Crit Chance |
| Enchanting | +2 Wisdom, +1 Crit Chance | 100 Wisdom, 50 Crit Chance |
| Alchemy | +2 Crit Chance, +1 Wisdom | 100 Crit Chance, 50 Wisdom |

Stats from different skills add together. Mining, Fishing and Armory all give Defense,
for example, so levelling all three stacks it. Some custom enchants add stats as well.
Click your head in `/skills` to see your totals.

## Effects

Each effect starts at level 1 of its skill unless the table says otherwise, and goes
up one level with every skill level after that.

### Mining

| Effect | Does | Per level | At skill 50 |
|---|---|---|---|
| Versatile Tools | More damage with pickaxes | +4% | +200% |
| Spelunking (from level 10) | Chance of extra drops from ores | +8% | Always 4×, with a 28% chance of 5× |
| Dynamic Mining | Chance of Haste III when breaking blocks | +0.1% | 5% |

### Woodcutting

| Effect | Does | Per level | At skill 50 |
|---|---|---|---|
| Craftsmanship | Chance for an axe to take no durability damage | +2% | 100% |
| Master Lumberjack | Chance of extra drops from trees | +6% | Always 4× drops |

### Farming

| Effect | Does | Per level | At skill 50 |
|---|---|---|---|
| Bountiful Harvest | Chance of extra drops from crops | +8% | Always 5× drops |
| Satiation | Lose less hunger | 2% less | 100% less |
| Golden Yield (from level 10) | Chance of 6× drops from crops | +0.5% | 20.5% |

### Fishing

| Effect | Does | Per level | At skill 50 |
|---|---|---|---|
| Eye of the Depths | Chance of rare drops from fishing | +0.1% | 5% |
| Magnetic Rod | Rods pull in drops and mobs faster | +4% | +200% |

### Combat

| Effect | Does | Per level | At skill 50 |
|---|---|---|---|
| Serrated Strikes | Chance to make your opponent bleed | +2% | 100% |
| Dazzle | Chance to give your opponent nausea | +1.5% | 75% |
| Strong Impact (from level 10) | Chance to deal 3× damage | +0.2% | 8.2% |
| Endangering (from level 20) | Chance to remove your opponent's invulnerability frames | +3% | 93% |

### Armory

| Effect | Does | Per level | At skill 50 |
|---|---|---|---|
| Shamanism | Heal faster | +4% | +200% |
| Infernal Resistance | Chance to ignore fire damage | +2% | 100% |
| Bravery (from level 10) | Take less damage from bosses | 1.5% less | 61.5% less |

### Exploration

| Effect | Does | Per level | At skill 50 |
|---|---|---|---|
| Seamless Movement | Chance to ignore fall damage | +2% | 100% |
| Dodging | Chance to ignore incoming damage | +0.5% | 25% |
| Accelerated Escape (from level 10) | Run faster for 1.5 seconds after taking damage | +4% | +164% |

### Enchanting

| Effect | Does | Per level | At skill 50 |
|---|---|---|---|
| Second Chance | Chance for an item below 30 durability to repair itself | +0.1% | 5% |
| Reimbursement | Chance to get your levels back after enchanting | +0.5% | 25% |
| Overcompensation (from level 10) | Chance to get your lapis back after enchanting | +0.75% | 30.75% |

### Alchemy

| Effect | Does | Per level | At skill 50 |
|---|---|---|---|
| Potionmaster | Brewed potions last longer | +4% | +200% |
| Mystic Resilience | Chance to ignore negative potion effects | +0.5% | 25% |
| Efficient Brewing (from level 10) | Potions brew faster | 1.5% less time | 61.5% less time |

!!! tip "Extra-drop effects past 100%"
    Spelunking, Master Lumberjack and Bountiful Harvest don't stop at a 100% chance.
    Once the chance passes 100%, you always get the bigger multiplier, and the chance
    starts again for the next one up. At 160%, for example, you always get 2× drops
    with a 60% chance of 3×.
