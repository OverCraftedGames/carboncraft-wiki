---
icon: material/shield-home
---

<!-- Sources (live): GriefPreventionData/config.yml (InitialBlocks, accrual, max accrued,
     MinimumWidth, MinimumArea, AutomaticNewPlayerClaimsRadius, tools, AbandonReturnRatio,
     ExtendIntoGroundDistance); DeluxeMenus votetiers.yml (+100 claimblocks per tier);
     rtp.yml (claims disabled in Nether/End). Checked 2026-10-24. -->

# Claiming land

CarbonCraft uses **GriefPrevention**. A claim is an area only you, and the people you
trust, can build in, break blocks in or open chests in. Anything outside a claim is
fair game.

Claims only work in the **Overworld**. The Nether and End can't be claimed.

## Claim blocks

Every claim costs **claim blocks**: one per block of floor area. A 10 × 10 claim costs
100 blocks. Claims reach from the sky down to bedrock, so height is free.

| How you get them | Amount |
|---|---|
| Starting amount | 100 |
| Playing | 100 per hour, up to 25,000 in total |
| Each vote tier | +100 |

Check what you have with `/claimslist`, or on the Player Stats head in `/help`.

## Your first claim is automatic

The first time you place a **chest**, a small claim is created around it for free. That
covers a starter base. Expand it as you build.

## Claiming with the golden shovel

1. Hold a **golden shovel**.
2. Right-click one corner of the area you want.
3. Right-click the opposite corner.

That's a claim. The smallest allowed claim is 5 blocks wide with an area of 100 blocks.

**To resize a claim**, hold the golden shovel, right-click a corner of your existing
claim, then right-click where you want that corner to be.

**To see claims**, hold a **stick** and right-click a block. The edges of the claim
there light up, along with the owner's name.

## Letting friends in

| Command | What it allows |
|---|---|
| `/trust <player>` | Build, break and everything below |
| `/containertrust <player>` | Open chests, use furnaces, farm animals and crops |
| `/accesstrust <player>` | Use buttons, levers, doors and beds |
| `/untrust <player>` | Remove someone's trust |
| `/trustlist` | See who you've trusted in this claim |

Stand inside the claim when you run these.

## Removing a claim

Stand in the claim and type `/abandonclaim`. You get **all** of its claim blocks back.

!!! danger "`/abandonallclaims`"
    This removes **every** claim you own at once. Everything you built becomes unprotected.

## Good habits

- Put your shop chests inside your claim. An unclaimed shop can be robbed by anyone.
- Claim before you build. Not after.
- Don't set homes inside other players' land; it's against the [rules](rules.md).
