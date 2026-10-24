---
icon: material/tag
---

<!-- Sources (live): DeluxeTags config.yml (63 tags: display, description, permission);
     DeluxeMenus shop/tags.yml + confirm_tagpack_1..8.yml (8 packs, 350 CarbonCoins, no
     ownership check), sink/sink_tags.yml + sink_hub.yml (7 flex tags, [takemoney], open
     commands exchange/sink), voteshop.yml (vote tag, 1000 vote points),
     megaproject_rewards.yml (carboncorp); DailyRewardsPlus Rewards.yml Day 31 + Config.yml
     (PauseStreakWhenMissed true); CarbonSpend config.yml (mvp, held for a month);
     ExcellentCrates crates/*.yml (carbon, fusion, plasma, zombie tag rewards).
     Staff-only and one-off tags (builder, viibe, spider, craft, autobot, jungle, CptJack)
     left out. Rendered tag HTML comes from scripts/render-tags.py. Checked 2026-10-24. -->

# Tags

A tag is a short coloured label shown next to your name in chat. You can own as many
as you like and wear one at a time.

## Wearing a tag

Type `/tags` to open your tag menu. It lists every tag you own.

- **Click a tag** to wear it.
- **Click your head** at the bottom of the menu to take your current tag off.

The menu title shows how many tags you own.

## Tag packs

The tag shop is in `/coinshop` → **Tags**. Each pack is **350 CarbonCoins** and unlocks
five tags at once.

| Pack | Theme | Tags |
|---|---|---|
| Enderborn | Pulled from the void beyond the world's edge | Ender, Wraith, Voider, Chorus, Dragon |
| Ashborn | Forged in the fire and ash of the Nether | Blaze, Ghast, Wither, Piglin, Magma |
| Starforged | Charted from the stars | Nebula, Comet, Rocket, Cosmic, Nova |
| Tideborn | Reeled up from the deep water | Angler, Reeler, Caster, Baiter, Diver |
| Deepdweller | Dug up from the deepest tunnels | Miner, Digger, Delver, Borer, Drill |
| Yuletide | Carried in on the long winter | Yule, Frosty, Tinsel, Krampus, Jolly |
| Hallowed | Dragged back from the other side | Ghoul, Hexed, Cursed, Reaper, Spook |
| Bountiful | Gathered at the end of the harvest | Feast, Gobble, Harvest, Gravy, Carver |

You confirm each purchase before the coins are taken.

!!! warning "Don't buy a pack twice"
    The shop doesn't check which packs you already own. Buying a pack again takes
    another 350 CarbonCoins and gives you nothing new.

## Flex tags

Seven tags that do nothing except prove you had the money. Open them with `/exchange`
(or `/sink`) → **Flex Tags**. They cost **dollars**, not CarbonCoins, and the money is
destroyed rather than paid to anyone.

| Tag | Price |
|---|---|
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#FFD700;font-weight:700">$</span><span style="color:#FFC300;font-weight:700">$</span><span style="color:#FFAA00;font-weight:700">$</span><span style="color:#555555">]</span></span> | $250,000 |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#FFD700;font-weight:700">$</span><span style="color:#F5C518;font-weight:700">R</span><span style="color:#EBB330;font-weight:700">I</span><span style="color:#E1A148;font-weight:700">C</span><span style="color:#D78F60;font-weight:700">H</span><span style="color:#555555">]</span></span> | $500,000 |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#A4DE02;font-weight:700">L</span><span style="color:#B5CE02;font-weight:700">O</span><span style="color:#C6BE01;font-weight:700">A</span><span style="color:#D7AE01;font-weight:700">D</span><span style="color:#E89E00;font-weight:700">E</span><span style="color:#F98E00;font-weight:700">D</span><span style="color:#555555">]</span></span> | $1,000,000 |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#1E5631;font-weight:700">T</span><span style="color:#36722C;font-weight:700">Y</span><span style="color:#4E8E27;font-weight:700">C</span><span style="color:#66AA22;font-weight:700">O</span><span style="color:#7EC61D;font-weight:700">O</span><span style="color:#96E218;font-weight:700">N</span><span style="color:#555555">]</span></span> | $2,500,000 |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#6A2C91;font-weight:700">M</span><span style="color:#8339A4;font-weight:700">O</span><span style="color:#9C46B7;font-weight:700">G</span><span style="color:#B553CA;font-weight:700">U</span><span style="color:#CE60DD;font-weight:700">L</span><span style="color:#555555">]</span></span> | $5,000,000 |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#0B6E8C;font-weight:700">W</span><span style="color:#2489A6;font-weight:700">H</span><span style="color:#3DA4C0;font-weight:700">A</span><span style="color:#56BFDA;font-weight:700">L</span><span style="color:#6FDAF4;font-weight:700">E</span><span style="color:#555555">]</span></span> | $10,000,000 |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#FFD700;font-weight:700">1</span><span style="color:#E8B800;font-weight:700">%</span><span style="color:#555555">]</span></span> | $25,000,000 |

!!! danger "No confirmation"
    The money is taken the moment you click. Tags you already own show as **OWNED**
    and can't be bought again.

## Tags you earn

| Tag | How to get it |
|---|---|
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#A7C188;font-weight:700">V</span><span style="color:#82BE64;font-weight:700">O</span><span style="color:#5DBB40;font-weight:700">T</span><span style="color:#39B81D;font-weight:700">E</span><span style="color:#555555">]</span></span> | 1,000 vote points in `/voteshop` |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#0B3D91;font-weight:700">D</span><span style="color:#1D5097;font-weight:700">a</span><span style="color:#2F649E;font-weight:700">i</span><span style="color:#4177A4;font-weight:700">l</span><span style="color:#548BAB;font-weight:700">y</span><span style="color:#555555">]</span></span> | Claim the day 31 reward in your daily login rewards (`/daily`). A missed day pauses your streak instead of resetting it. |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#00CBFF;font-weight:700">C</span><span style="color:#0187FF;font-weight:700">O</span><span style="color:#0244FF;font-weight:700">R</span><span style="color:#0300FF;font-weight:700">P</span><span style="color:#555555">]</span></span> | Qualify for the rewards of the Planetary Refinery megaproject (`/megaproject`) |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#0B3D91;font-weight:700">M</span><span style="color:#2F649E;font-weight:700">V</span><span style="color:#548BAB;font-weight:700">P</span><span style="color:#FFFFFF">™</span><span style="color:#555555">]</span></span> | Be the server's top store supporter for the month. You keep it until the next month's MVP is announced. |

### Crate tags

These can drop as crate rewards.

| Tag | Crate |
|---|---|
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#8B5A2B;font-weight:700">M</span><span style="color:#A87920;font-weight:700">i</span><span style="color:#C59816;font-weight:700">n</span><span style="color:#E2B80B;font-weight:700">e</span><span style="color:#FFD700;font-weight:700">r</span><span style="color:#555555">]</span></span> | Carbon Crate |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#023E8A;font-weight:700">A</span><span style="color:#1E5E9E;font-weight:700">n</span><span style="color:#3B7FB2;font-weight:700">g</span><span style="color:#579FC7;font-weight:700">l</span><span style="color:#74C0DB;font-weight:700">e</span><span style="color:#90E0EF;font-weight:700">r</span><span style="color:#555555">]</span></span> | Carbon Crate |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#0B3D91;font-weight:700">N</span><span style="color:#095CA7;font-weight:700">e</span><span style="color:#077BBD;font-weight:700">b</span><span style="color:#049BD3;font-weight:700">u</span><span style="color:#02BAE9;font-weight:700">l</span><span style="color:#00D9FF;font-weight:700">a</span><span style="color:#555555">]</span></span> | Fusion Crate |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#2D0B4E;font-weight:700">E</span><span style="color:#40136A;font-weight:700">n</span><span style="color:#541C86;font-weight:700">d</span><span style="color:#6824A3;font-weight:700">e</span><span style="color:#7B2CBF;font-weight:700">r</span><span style="color:#555555">]</span></span> | Fusion Crate |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#FF6B00;font-weight:700">B</span><span style="color:#FF8602;font-weight:700">l</span><span style="color:#FFA005;font-weight:700">a</span><span style="color:#FFBB08;font-weight:700">z</span><span style="color:#FFD60A;font-weight:700">e</span><span style="color:#555555">]</span></span> | Plasma Crate |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#1B1B1B;font-weight:700">G</span><span style="color:#371414;font-weight:700">h</span><span style="color:#530E0E;font-weight:700">a</span><span style="color:#6F0707;font-weight:700">s</span><span style="color:#8B0000;font-weight:700">t</span><span style="color:#555555">]</span></span> | Plasma Crate |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#4F7942;font-weight:700">I</span><span style="color:#678B56;font-weight:700">m</span><span style="color:#809C6B;font-weight:700">m</span><span style="color:#98AE7F;font-weight:700">u</span><span style="color:#B1BF94;font-weight:700">n</span><span style="color:#C9D1A8;font-weight:700">e</span><span style="color:#555555">]</span></span> | Zombie Crate |
| <span class="mc-tag"><span style="color:#555555">[</span><span style="color:#4F7942;font-weight:700">R</span><span style="color:#638853;font-weight:700">o</span><span style="color:#789664;font-weight:700">t</span><span style="color:#8CA575;font-weight:700">b</span><span style="color:#A0B486;font-weight:700">a</span><span style="color:#B5C297;font-weight:700">n</span><span style="color:#C9D1A8;font-weight:700">e</span><span style="color:#555555">]</span></span> | Zombie Crate |

A tag you win from a crate is the same tag as the one in the shop. If you already own
it, a pack that includes it still costs the full 350 CarbonCoins.

Every fifth [vote tier](../getting-started/voting.md) also adds a suffix after your
name. That suffix is part of your rank, not a tag, so you can wear both.
