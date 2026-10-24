---
icon: material/arrow-up-bold-circle-outline
---

<!-- Sources (live): EcoSkills skills/*.yml xp-gain-methods and xp-requirements.
     mine_block values are per block. Exploration (move, chance arg), Fishing (catch_fish x0.1), Combat (kill x0.33),
     Armory (take_damage x1.44) and Enchanting (enchant_item x3, enchant_special x175)
     are described without numbers because the trigger values depend on the event.
     Checked 2026-10-24. -->

# Earning XP

How each skill earns XP. The numbers are the base amount before your **Wisdom** stat
and any boosts.

## Mining

Break blocks the world generated. Blocks placed by players give nothing.

| XP per block | Blocks |
|---|---|
| 0.3 | Netherrack |
| 1 | Stone, cobblestone, granite, diorite, andesite, sandstone, red sandstone, terracotta (plain, white, orange, yellow, brown, red, light gray) |
| 1.5 | Deepslate, tuff, blackstone, basalt |
| 2.5 | Calcite, cinnabar, sulfur, potent sulfur |
| 3 | End stone, obsidian |
| 4 | Gravel |
| 5 | Coal, iron, copper and nether quartz ore, amethyst block |
| 6 | Gold ore, nether gold ore |
| 7 | Lapis and redstone ore |
| 7.5 | Deepslate coal, iron and copper ore |
| 8.5 | Budding amethyst, crying obsidian |
| 9 | Emerald ore, deepslate gold ore |
| 10 | Diamond ore, gilded blackstone |
| 10.5 | Deepslate lapis and redstone ore |
| 13.5 | Deepslate emerald ore |
| 15 | Deepslate diamond ore |
| 22 | Ancient debris |

## Woodcutting

Chop logs from natural trees. Logs placed by players give nothing.

| XP per block | Blocks |
|---|---|
| 6 | Every overworld log and wood block: oak, birch, spruce, jungle, acacia, dark oak, mangrove, cherry and pale oak |
| 14 | Crimson and warped stems |

## Farming

Harvest crops when they're **fully grown**. Breaking a young crop gives nothing.

| XP per block | Crops |
|---|---|
| 1 | Bamboo (every block in the stalk) |
| 2 | Cactus, sugar cane (every block in the stalk, natural only) |
| 3 | Cocoa, sweet berries, glow berries |
| 4 | Wheat, carrots, nether wart, melon (natural only) |
| 4.5 | Pumpkin, melon (natural only) |
| 5 | Potatoes, beetroots |

## Alchemy

Brew potions. The ingredient you brew with decides the XP.

| XP | Ingredient |
|---|---|
| 1 | Nether wart, redstone, glowstone dust, fermented spider eye, gunpowder |
| 2 | Spider eye |
| 3 | Sugar |
| 4 | Pufferfish, magma cream, ghast tear |
| 6 | Rabbit's foot, glistering melon slice, golden carrot, blaze powder |
| 12 | Dragon's breath, phantom membrane |
| 20 | Turtle shell |

## Everything else

| Skill | How |
|---|---|
| Fishing | Catch fish. Any catch counts, custom fish included. |
| Combat | Kill mobs. |
| Armory | Take damage. Damage from cactus and berry bushes doesn't count. |
| Exploration | Walk, run, swim or fly. XP comes in small random chunks as you move. |
| Enchanting | Enchant items at an enchanting table. Enchants that land a custom enchant give far more XP. |

## XP needed per level

Every skill has 50 levels. The cost of each level climbs steeply, so the last few
levels take far longer than the first twenty.

| Skill | Level 1 | Level 50 |
|---|---|---|
| Mining, Woodcutting, Farming, Combat, Armory | 50 XP | 4,000,000 XP |
| Exploration | 25 XP | 2,000,000 XP |
| Enchanting | 10 XP | 400,000 XP |
| Alchemy | 5 XP | 200,000 XP |
| Fishing | 5 XP | 100,000 XP |

`/skills` shows exactly how much XP you need for your next level.
