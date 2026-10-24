---
icon: material/chart-line-variant
title: Skills
---

<!-- Sources (live): EcoSkills config.yml (gui, level-up message, prevent-levelling-while-afk,
     disabled-in-worlds zombies + world_2, leaderboard enabled, action bar disabled),
     lang.yml, skills/*.yml (9 skills: rewards, start-levels, 50 levels, xp-requirements,
     hide-before-level-1), stats/*.yml, effects/*.yml. Jar EcoSkills-2026.40 on live.
     world_2 isn't a live Multiverse world, so only the Zombies world is mentioned.
     Checked 2026-10-24. -->

# Skills

Almost everything you do levels up a **skill**. There are nine, each with 50 levels.
Every level gives you permanent **stats** (more damage, less damage taken, faster
movement) and makes the skill's **effects** stronger.

Type `/skills` to see your levels, progress and what the next level gives you.

## The nine skills

| Skill | Earn XP by | Stats | Effects |
|---|---|---|---|
| Mining | Breaking stone and ores | Defense, Ferocity | Versatile Tools, Spelunking, Dynamic Mining |
| Woodcutting | Chopping logs | Strength, Crit Damage | Craftsmanship, Master Lumberjack |
| Farming | Harvesting fully grown crops | Crit Damage, Wisdom | Bountiful Harvest, Satiation, Golden Yield |
| Fishing | Catching fish | Defense, Wisdom | Eye of the Depths, Magnetic Rod |
| Combat | Killing mobs | Strength, Ferocity | Serrated Strikes, Dazzle, Strong Impact, Endangering |
| Armory | Taking damage | Defense, Speed | Shamanism, Infernal Resistance, Bravery |
| Exploration | Moving around | Speed, Crit Chance | Seamless Movement, Dodging, Accelerated Escape |
| Enchanting | Enchanting items | Wisdom, Crit Chance | Second Chance, Reimbursement, Overcompensation |
| Alchemy | Brewing potions | Crit Chance, Wisdom | Potionmaster, Mystic Resilience, Efficient Brewing |

[Stats & effects](stats-and-effects.md) lists what each one does and how much you get.
[Earning XP](earning-xp.md) lists how much XP each block, crop and ingredient gives.

!!! note "Not the same as PyroMining and PyroFishing"
    [Mining](../activities/mining.md) and [Fishing](../activities/fishing.md) also have
    their own levels (`/mine stats`, `/fish stats`). Those are separate systems. A mined ore or
    a caught fish counts towards both.

## How levelling works

- Each action gives skill XP, shown on your action bar as you earn it.
- When you level up, chat lists the rewards you just got.
- A skill stays hidden as an **Unknown Skill** in `/skills` until you reach level 1 in it.
- Skills don't gain XP while you're **AFK**, or in the **Zombies** arena.
- Blocks placed by a player give no Mining or Woodcutting XP, so you can't place and
  break the same block for XP. The same goes for melons, pumpkins, cactus and sugar
  cane in Farming. Planted crops do count once they're fully grown.

## The skills menu

`/skills` shows each skill's level, a progress bar to the next level and the effects
it gives. **Click a skill** to see every level and its rewards: green levels are done,
yellow is the one you're on, and red are still to come.

**Click your head** at the top of the menu to see all your stats in one place. Your
total skill level is also on your head in `/help`.

## Commands

| Command | Does |
|---|---|
| `/skills` | Your skills, levels and stats |
| `/skills top` | The skills leaderboard |
| `/skills togglesound` | Turn the XP gain sound on or off |
