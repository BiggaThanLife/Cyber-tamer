# Digital Explorer: Cyber Tamer

A monster-taming RPG that runs in your browser. Explore seeded wilderness maps, catch and breed monsters, train a partner, run a farm, dig the Data Mine and take down each biome's boss. It works on phones and desktops, needs no install and has no account. Your progress saves on your own device.

**Play:** https://biggathanlife.github.io/Cyber-tamer/

> Status: early playtest build (v25). Expect rough edges, and please tell the developer what you find.

## Contents
- [Quick start](#quick-start)
- [How to play](#how-to-play)
- [Reference](#reference): [Monsters](#monsters) · [Types and moves](#types-and-moves) · [Biomes and bosses](#biomes-and-bosses) · [Items](#items) · [Farm](#server-farm) · [Dex milestones](#dex-milestones)
- [Saving, backups and privacy](#saving-backups-and-privacy)
- [Playing on a phone](#playing-on-a-phone)
- [Giving feedback](#giving-feedback)
- [For developers](#for-developers)

## Quick start
1. Open the link and tap **New Game**. A short tutorial walks you through the basics (you can skip it, and replay it from **Help**).
2. From the town of Neon Haven, tap **Wilderness Gate**, pick a biome and tap **New Map**.
3. Walk with the arrow pad. When a wild monster appears, weaken it with moves, then run a **capture program** (start with Basic Capture.exe) to acquire it.
4. Beat a biome's boss to unlock the next biome and new features.

Stuck at any point? Open **Help** from the town menu. It has the same information as this page, split into topics. The **📜 Log** button at the top of every screen shows what just happened.

## How to play

### The goal
Explore, catch monsters, grow your partner stronger, and defeat each biome's boss. Beating a boss unlocks the next biome.

### Your partner
One monster is your **active partner**, the one who explores and fights. The rest wait in the **Network Registry**, where you can swap partners, sort lists and sell spares. Your active partner and your last monster can't be sold. Tap the 🔓/🔒 icon on any card (or on its Inspect screen) to lock a monster you never want to sell by mistake — a locked monster's Sell button is disabled until you unlock it again.

### The town menu
The buttons are grouped in pairs:

| Pair | What they are for |
|---|---|
| Wilderness Gate / Data Mine | Go out and explore |
| Wanted Board / Daily | Goals and rewards |
| Job Board / Server Farm | Earn Bits |
| Training Ground / Splice Lab | Grow and improve monsters |
| Play / Rest Partner | Look after your partner |
| Network Registry / Inventory | Manage what you own |
| Shop / Dex | Buy things, track your collection |
| Help / System | Help topics, save export and import |

A 🔒 means it isn't unlocked yet. Tap it to see how to unlock it.

### Exploring the wilderness
- Step around the map with the arrow pad. Each step costs **1 Energy** and **2 Hunger** and gives your partner **1 XP**.
- Stepping onto open ground has about a **20% chance** of a wild encounter.
- If Hunger reaches 0, your partner is too weak to explore and you return to town.
- Fog hides the map until you get close. Every map has a **seed number**: the same seed always gives the same layout. ☆ favorite a seed to return to a map you liked, ⧉ copy it to share, or **Enter Seed** to type one in.
- Tap **❓ Legend** on the map to see the symbols:

| Symbol | Meaning |
|---|---|
| ⛩ | Gate, the exit back to town |
| ▪ | Chest: Bits or a capture program |
| ✦ | Shrine: Bits and XP |
| ⚷ and ▣ | A key, which opens a vault with Bits and capture programs |
| ✕ | Anomaly: a stronger, charged monster in a fixed spot |
| ☠ | The biome boss |
| ♨ | Heat vent (Foundry only) |
| ✪ | Daily cache (Daily sector only) |

Some tiles block your way.

### Battles
- Pick a move, then the enemy hits back. Every partner has two universal moves, plus type moves learned as they level.
- Move buttons show **▲** if the move is strong against this enemy and **▼** if it is weak.
- **Use Medicine** restores HP to full mid-fight. **Flee** depends on your SPD against the enemy's and always stays between 20% and 90%.
- A faster partner can also **dodge** counterattacks completely.
- A running log of the fight sits under the monsters.
- Hits, dodges, catches, level-ups and evolutions are animated. If that bothers you or slows your phone, set **System → Motion** to Reduced. It follows your device's reduce-motion setting by default.
- If your partner faints, you retreat to town with 20% HP and lose 10% of their progress toward the next level. This never costs you a level you already have — it only sets back how close you are to the next one.

### Catching monsters
- Encountering a wild monster opens with a quick scan, then the fight. Once it's weakened, run a **capture program** — each one shows its own live odds, starting around 5% and rising steeply as the enemy's HP drops (capped at 95%). Basic Capture.exe is the starting tool; Advanced Capture.exe, Hunter.exe and Containment.exe are pricier and noticeably better.
- Anomalies are a bit easier (+15%) and Wanted monsters easier still (+20%).
- **Pressure Point** is a lighter hit that leaves foes easier to capture.
- Bosses **cannot** be caught. You have to defeat them.
- If a monster escapes, you may be offered to add it to your **Wanted Board**.
- Rare glowing **✦ Marked** monsters (about 1 in 128) are worth catching. They count toward the Dex.

### Looking after your partner
- **Hunger** and **Energy** drain as you explore.
- Feed with **Prime Meat** from the Inventory (+40 Hunger). **Rest Partner** in town gives +35 Energy for a little Hunger.
- **Play** is a short timing game that earns small amounts of Bits and XP. Every try costs Energy and Hunger, hit or miss, and only a few tries fit in a row before your partner needs a break. Exploring shortens the break.
- Jobs and Training need a minimum amount of Energy.

### Stats
| Stat | What it does |
|---|---|
| HP | How much damage your partner can take before fainting |
| STR | Powers the damage of every move |
| DEF | Reduces damage taken |
| SPD | Improves dodging and fleeing |

Every monster also has hidden **IVs**, ±15% variance on each stat, fixed for life when it's caught or hatched. They show up as a **Potential** star rating (☆ to ★★★★★). Breeding can pass IVs down, sometimes with a mutation.

Every monster also rolls one of 8 **personalities** at capture or hatch, fixed for life and shown on its Inspect screen. Half trade one stat for another (Aggressive, Guarded, Swift, Sturdy, Reckless, Calm); the other half are passive perks that don't touch stats — Focused adds dodge and flee chance, Adaptive cuts Hunger/Energy drain while exploring. It's hidden until you check Inspect, same as IVs. Splicing two parents gives the hybrid a coin-flip chance at either parent's personality.

Monsters gain XP from exploring and battles. Every species has a second, stronger form, reached at level 10.

### Growing stronger
- **Evolution Crests:** bought in the Shop or grown on the farm. They apply instantly and boost all four stats a little. Capped at 3 per monster.
- **Training Ground:** unlocks after your first boss. Pick a stat (STR, DEF or SPD) and play a timing game. Each stat can be trained up to +10 per partner. It costs Energy and Hunger and starts a cooldown that shortens as you explore.
- **Splice Lab** (formerly Breeding Lab): unlocks when your farm reaches a **Server Shack**. Pick two different monsters and pay 50 Bits to splice their genomes. A full-screen reveal shows the new hybrid, then opens straight to its Inspect screen.
- **Modules:** each monster holds one. Timed modules burn one tick per step or dig, only while that monster is your active partner. Sync Link is the exception and keeps running on the bench.
- **Stat Drives:** permanent stats, capped per partner.
- **Gear:** found only in the Data Mine. Each monster has two gear slots.

### Earning Bits
Win battles, open chests and shrines, do jobs, play, complete daily quests, harvest crops, or sell spare monsters.

- **Job Board:** send a partner on a job for an instant payout that depends on their stats. Each job costs 15 Energy to start, uses some Hunger, and starts a cooldown that shortens as you explore.

| Job | Pays best with |
|---|---|
| Databank Mining | High STR |
| Grid Sentry | High DEF |
| Data Courier | High SPD |
| Signal Busking | High HP |

### The Data Mine
Unlocks after you defeat **two** biome bosses.
- Move the arrow pad toward a block to dig it. Tougher blocks take several hits, and the ⛏ number shows how many are left.
- Depth is how far down you've gone. Your best depth is kept as a record.
- You'll find ore, treasure, seed caches (including Deepweed), gear components and ambush monsters. The 📡 line tells you if a cache or component is within a few tiles, and in which direction.
- **Disconnect** pauses your dive and keeps all progress. **Abandon** throws the dive away but keeps your depth record.

### Locked Nodes and Explorer Tools
- While exploring you may find a 🧩 **Locked Node** — a sealed data cache you can't open without the right tool.
- **Decrypter:** a one-time Explorer Tool bought once in the Shop's Tools tab (◈500). It's a permanent unlock, not a consumable.
- With a Decrypter, stepping onto a Locked Node opens a **Data Breach** — a match-3 grid. Swap two adjacent tiles to line up 3 or more of the same type (Data, Code, Packets, Keys, Encryption, Protocols); matches clear, tiles cascade down, and empty spots refill.
- 🛡 **Firewall** tiles sit on some cells and take damage from any match cleared next to them — breach every Firewall on the board before you run out of moves to win.
- A 4-match creates a **Data Packet** that clears its whole row or column; a 5-match creates an **Exploit** that clears the area around it.
- Later biomes use a bigger board, more tile types and more Firewalls, and give fewer moves — the challenge comes from all of those together, not just a shrinking move count.
- Solving it pays Bits and a capture program. Running out of moves just re-locks the node — no other penalty, and you can try again any time. **Abandon** leaves it for later.
- **Packet Tracer** (◈300): shows the boss's direction and how close it is on *any* map, not just the Ghost Server.
- **Port Scanner** (◈350): reveals Locked Nodes through the fog, so you can spot one before you've walked near it.
- **Restricted Zones:** a rare ⛔ tile that blocks the way outright, like a wall — until you own a **Firewall Breaker** (◈900). Walking into one with the tool forces the path open for good, for a one-time reward of Bits and a Basic Capture.exe. Old maps and favorited seeds are never blocked by a tool you don't own — it only ever opens up new ground.

### Field Barriers
- A rare tile that blocks the way like a wall unless your active partner's type matches the one it needs — Fire, Water, Earth, Electric, Nature, Void, Metal, or Glitch.
- Walk up to it with the right type fielded and it opens for good, paying Bits and a capture program, same as a Restricted Zone.
- No Shop tool unlocks these — you need to have actually caught, and be fielding, that type. A map can have several, of different types, so fully looting one may mean swapping partners more than once.

### Layer 2
- Beat a biome's boss and a 🌀 **Layer 2** option opens up on that biome's card at the Wilderness Gate — a harder second pass through the same biome.
- Favored species spawn even more often, the biome's own mechanic gets denser (more heat vents in the Foundry, a tighter fading-signal radius on the Ghost Server), and a new ⚡ **power surge** hazard shows up that no Layer 1 map has.
- Layer 2 has its own, much stronger boss under a new title, and its own defeat tracking separate from Layer 1 — beating it doesn't unlock a new biome, but it does pay out bigger Bits and XP.
- Layer 2's layout is derived from the same seed you use for Layer 1, so favoriting a seed favorites both.

### Daily Ops and the Wanted Board
- **Login streak:** claim a reward each day on a 7-day cycle. Each finished cycle adds a 25% Bits bonus, up to +100%. One missed day is forgiven, and a long break earns a welcome-back gift.
- **Daily quests:** three new quests every day, based on what you've unlocked. Clear all three for a bonus cache.
- **Daily sector:** a special map with one ✪ cache tile. Every fifth claim gives an Evolution Crest.
- **Wanted Board:** monsters that escaped can be added here. They can reappear while you explore, and you get a real edge on catching them.

## Reference

### Monsters
There are 20 species. Each has a first form and an evolved form (evolves at level 10). **Roamers** can appear in any biome. **Habitat** species only appear in the biome shown.

| Species | Type | Evolves into | Where |
|---|---|---|---|
| Pyrelix | Fire | Pyroclast | Roamer |
| Hydrune | Water | Tsunareth | Roamer |
| Terrabit | Earth | Colossite | Roamer |
| Volteon | Electric | Fulgorex | Roamer |
| Sylvyx | Nature | Verdanth | Roamer |
| Nyxbyte | Void | Abyssyx | Roamer |
| Ferrocog | Metal | Titanrend | Roamer |
| Glitchling | Glitch | Corruptor | Roamer |
| Fernling | Nature | Bramblor | Neon Outskirts |
| Ripplet | Water | Torrentail | Neon Outskirts |
| Kilnpup | Fire | Furnacor | Sunbaked Wastes |
| Mirageling | Glitch | Halluxis | Sunbaked Wastes |
| Rimebit | Metal | Glaciron | Frostbyte Tundra |
| Sleetkin | Electric | Auroraith | Frostbyte Tundra |
| Shardling | Earth | Prismarch | The Undergrid and the Data Mine |
| Umbrite | Void | Eclipsoid | The Undergrid |
| Ashwyrm | Fire | Pyrewyrm | Overclocked Foundry |
| Slagback | Earth | Slagbulwark | Overclocked Foundry |
| Wispwire | Electric | Spectrowire | The Ghost Server |
| Gloomcap | Nature | Necrobloom | The Ghost Server |

Each biome also favours a few roamers, so they show up more often there. Rare **Marked** versions of every species exist.

### Types and moves
There are eight types. A type move deals **1.5×** damage when strong and **0.67×** when weak. The two universal moves are typeless.

| Type | Strong against | Weak against |
|---|---|---|
| Fire | Nature, Metal | Water, Earth |
| Water | Fire, Earth | Electric, Nature |
| Earth | Electric, Fire | Water, Nature |
| Electric | Water, Metal | Earth, Glitch |
| Nature | Water, Earth | Fire, Glitch |
| Void | Glitch, Nature | Metal, Electric |
| Metal | Nature, Void | Fire, Electric |
| Glitch | Electric, Metal | Void, Earth |

| Move kind | Power | Notes |
|---|---|---|
| Strike | 1.0× | Basic direct hit |
| Pressure Point | 0.55× | Lighter hit, leaves foes easier to capture |
| Special (one per type) | 1.3× | Cinder Lash, Tide Crush, Crag Slam, Arc Snap, Thorn Pulse, Null Bite, Gear Ram, Error Spike |
| Ultimate (one per type) | 1.75× | Magma Nova, Tidal Reckoning, Seismic Verdict, Thunder Collapse, Bloomstorm, Void Eclipse, Titan Shear, Segfault |
| Thermal Burst / Frost Lance | 1.4× | Granted by equipping a Thermal Core or Frost Core |

### Biomes and bosses
Wild monsters' levels are based on your partner's level plus a biome bonus, so you can't simply out-level the danger.

| # | Biome | Boss | Notes |
|---|---|---|---|
| 1 | Neon Outskirts | The Crag Warden (Terrabit line) | A gentle introduction |
| 2 | Sunbaked Wastes | The Cinder Sovereign (Pyrelix line) | |
| 3 | Frostbyte Tundra | The Glacial Tyrant (Hydrune line) | |
| 4 | The Undergrid | The Kernel Corruptor (Nyxbyte line) | |
| 5 | Overclocked Foundry | The Forgemaster (Ferrocog line) | Heat vents hurt your partner. Fire is immune, Metal and Earth take half, Water and Nature take extra. Vents never faint you. |
| 6 | The Ghost Server | The Ghost Admin (Glitchling line) | You only see 2 tiles around you, and explored ground is forgotten. A ghost signal hints where the boss is. |

Beating boss #1 unlocks the Training Ground. Beating two unlocks the Data Mine.

### Items

**Supplies (Shop, Supplies tab)**

| Item | Price | Effect |
|---|---|---|
| Basic Capture.exe | 20 | Run from the battle screen to try to acquire a wild monster |
| Advanced Capture.exe | 60 | Better odds than Basic |
| Hunter.exe | 160 | Strong odds even against sturdy targets |
| Containment.exe | 420 | About as close to a guarantee as it gets |
| Prime Meat | 15 | Fills hunger, restores a little energy |
| Medicine | 25 | Restores HP to full |
| Evolution Crest | 100 | Permanently boosts stats (max 3 per monster) |
| Nano Patch | 12 | Restores 30% of max HP, also usable in battle |
| Charge Cell | 18 | Restores 50 Energy |
| Prime Sirloin | 45 | Fills Hunger and restores 25 Energy |
| Reboot Kit | 70 | Restores HP, Hunger and Energy to full |
| Pod Overclock | 350 | Doubles farm growth speed for 100 ticks of exploring |

**Growth (Shop, Growth tab)**

| Item | Price | Effect |
|---|---|---|
| Exp Capsule | 100 | +250 XP |
| Exp Capsule L | 450 | +1,500 XP |
| HP Drive | 120 | +4 max HP each, up to +40 per partner |
| STR / DEF / SPD Drive | 200 | +1 to that stat each, up to +10 per partner |

**Battle chips (Shop, Battle tab)**

| Item | Price | Effect |
|---|---|---|
| Overload Chip | 60 | One typeless blast worth 2.2× STR. Single use, from the battle screen |
| Firewall Chip | 45 | Absorbs the enemy's next attack. Single use |

**Modules (Shop, Modules tab).** One per monster. Timed modules burn ticks only while that monster is your active partner.

| Module | Price | Ticks | Effect |
|---|---|---|---|
| XP Amplifier | 600 | 300 | +50% XP from everything |
| Sync Link | 700 | 400 | Shares 50% of your active partner's XP, even on the bench |
| Power Amp | 400 | 250 | +20% STR |
| Guard Shell | 400 | 250 | +20% DEF |
| Turbo Scarf | 400 | 250 | +20% SPD |
| Leftover Cache | 450 | 250 | Restores 1% of max HP every tick |
| Bit Magnet | 600 | 300 | +50% Bits from battles and captures |
| Stealth Mask | 150 | 150 | Wild encounters half as often |
| Signal Lure | 150 | 150 | Wild encounters 60% more often |
| Trap Assist | 350 | 200 | +25% capture chance (max 95%) |
| Nutrient Cell | 300 | 250 | Exploring drains half as much Hunger |
| Drill Bit | 500 | 150 | Data Mine blocks take double damage per dig |
| Safety Buffer | 500 | one use | Survive one lethal hit with 1 HP |
| Legacy Lock | 250 | never wears out | Holder will not evolve while equipped |

**Gear (Data Mine only, 2 slots per monster).** Not sold in shops. Extras can be sold.

| Gear | Effect | Sells for |
|---|---|---|
| Core Battery | +10 HP | 60 |
| Servo Booster | +5 SPD | 75 |
| Reinforced Plate | +5 DEF | 75 |
| Overclock Chip | +5 STR | 90 |
| Balanced Core | +2 STR, DEF and SPD | 100 |
| Thermal Core | Grants Thermal Burst (Fire) to any partner | 140 |
| Frost Core | Grants Frost Lance (Water) to any partner | 140 |

**Cosmetics (Shop, Cosmetics tab).** Top Hat (40), Cyber Shades (35), Bowtie (30), Bandana (45), Golden Crown (120).

### Server Farm
Buy seeds, plant them in pods, and charge them to start growing. Crops grow as you take steps, not in real time. A ripe crop waits for you, however long you're out exploring.

| Crop | Seed price | Grows in | Gives |
|---|---|---|---|
| Bitshoot | 15 | 15 ticks | 40 Bits |
| Byte Berry | 25 | 25 ticks | 3 Prime Meat |
| Cache Crystal | 50 | 40 ticks | 2 Medicine |
| Crest Shard | 120 | 70 ticks | 1 Evolution Crest |
| Deepweed | Not sold (Data Mine only) | 30 ticks | 90 Bits |

| Farm level | Cost | Pods |
|---|---|---|
| Vacant Plot | Free | 6 |
| Server Shack | 300 | 10 (unlocks the Splice Lab) |
| Small Farm | 800 | 16 |
| Farmhouse | 2,000 | 24 |
| Large Estate | 5,000 | 36 (unlocks automation) |

**Automation (Large Estate only):** Auto-Harvester (20,000) harvests every ripe pod with one button. Seed Drill (35,000) plants and charges every empty pod. Autopilot Loop (100,000) does the whole cycle and needs both of the others first.

### Dex milestones
| Milestone | Goal | Reward |
|---|---|---|
| First Marked Catch | Catch a Marked monster | 150 Bits, 1 Crest |
| Half the Dex | Catch half of the 20 lines | 200 Bits, 3 Basic Capture.exe runs |
| Dex Complete | Catch all 20 lines | 400 Bits, 2 Crests |
| Full Evolution | Catch every line's evolved form | 500 Bits, 2 Crests |
| Living Dex | Catch a Marked monster of every line | 1,000 Bits, 3 Crests |

## Saving, backups and privacy
- The game **saves automatically** to your browser on your own device. There are no accounts and no servers, and nothing is sent anywhere.
- Your save belongs to **one browser on one device, at one web address**. It doesn't follow you to another phone, another browser or a different link.
- Browsers can clear this kind of storage, especially if you clear site data, use a private window, or (on iPhones) don't visit for a long time. **Back up your save now and then:** System → **Export Save File**. To restore it or move to another device, use System → **Import Save File**. Importing replaces your current progress.
- **Update Notes:** System → **🗓 Update Notes** lists every update ever pushed to the game, newest first, with the version and date of each.

## Playing on a phone
- Open the link in your phone's browser.
- To keep it handy, use your browser's **Add to Home Screen** option.
- Always open the game the same way, from the same link and browser, so your save is there.

## Giving feedback
Tell the developer what you find. Helpful things to include:
- What you were doing and what happened.
- Your device and browser.
- The last few lines from the **📜 Log**.
- Anything confusing, unfair or boring, and where you stopped playing.

## For developers
- It's a single file, `index.html`, with HTML, CSS and vanilla JavaScript in one closure. There's no build step, no dependencies and no backend.
- To run it locally, open `index.html` in a browser or serve the folder with any static server.
- Saves are JSON in `localStorage` (key `cybertamer_save`). Every load and import passes through `migrateState`, and any new save field needs defaults in both `defaultState()` and `migrateState()`.
- Rules that keep saved maps and monsters working: seeded layouts must not change their random-number order, and species IDs are append-only.
- See `CLAUDE.md` for the architecture notes.
- **When you change a mechanic, update the in-game Help text (`HELP_SECTIONS`) and this README.**
