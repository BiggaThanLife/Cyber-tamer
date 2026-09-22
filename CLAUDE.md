# Digital Explorer: Cyber Tamer (published as `index.html`; currently v25)

Single-file HTML5/CSS/vanilla JS monster-taming RPG. No backend; saves in localStorage (`cybertamer_save`) with JSON export/import. All code sits in one IIFE (`state` is a closure variable). `render()` dispatches on `state.screen`, and `migrateState(s)` sanitizes every load and import.

## Systems

### Core (v20 and earlier)
- Town hub, 4 seeded biomes (mulberry32; same seed = same layout, fresh fog each visit), favorited/recent seeds.
- Turn-based combat with 8-type effectiveness, SPD dodge/flee, Medicine.
- Capture, Wanted Board, breeding, Dex with milestones.
- Training Ground, Job Board, Evolution Crests (cap 3 per partner), Server Farm (5 tiers of pods).
- Data Mine (multi-hit blocks, depth scaling, resumable dives, mine-only gear).
- Custom in-app modals only. Native `confirm`/`prompt`/`alert` are unreliable in webviews.

### Species (v21-v23)
- `EVOLUTION_LINES[id]` is an array of stage forms, any length. Optional stage-1 fields: `roamer:true` or `habitat:[biomeId|'mine']`; `specialMove`/`ultimateMove` overrides (default from `TYPE_MOVES[type]`); `parts:{tail,eyes,pattern}` (0-4) and `shape:{head,body,wing}`.
- 20 species (8 legacy + 12 exclusive).
- Spawn pools: `encounterPool(biome)` (favored/habitat at weight 2 plus all roamers), `minePool()`, `anomalyPool(biome)`.
- Sprites: cached data URLs via `spriteDataUrl`; uncached renderer is `spriteDataUrlRaw`.
- Unknown species are kept as `missingSpeciesId` and restored when the species exists again.

### Lists (v21)
Active partner pinned first on Storage, Jobs, Training, Breeding. `SORT_OPTIONS` gives 11 sorts, saved as `state.listSort`.

### Biomes 4 and 5 (v23)
- Overclocked Foundry (4): `role:'hazard'` heat-vent tiles (11% of open ground). `hazard.typeMult`: Fire immune, Metal/Earth x0.5, Water/Nature x1.5. Vents never drop HP below 1. Boss: Forgemaster (ferrocog).
- The Ghost Server (5): `fadeFog:{radius:2}` via `applyFog()` (gate always visible), boss ghost-signal hint (`bossSignalText`). Boss: Ghost Admin (glitchling).
- Biome fields: `mapSize`, `levelOffset`, `bossLevelOffset`, `mechanic`.
- Defeating boss N unlocks biome N+1; `migrateState` back-fills unlocks.

### Daily Ops (v23)
- Clock: local date via injectable `clockFn`; monotonic (`lastSeenDay`).
- Login streak: 7-day cycle, +25% per completed cycle (max +100%). One missed day forgiven; 4+ days away gives a welcome-back gift.
- 3 quests/day seeded by date, gated by unlocks, never all chores, bonus cache for clearing all 3. `questEvent(kind, n, meta)` is called from real code paths.
- Daily sector: seeded map with one `role:'cache'` tile from its own PRNG. Every 5th claim gives a Crest.

### Items (v24)
- Shop: 5 tabs from `SHOP_TABS`, `SHOP_ITEMS`, `SUPPLY_ITEMS`, `MODULES`.
- Supplies via `useItem`. Exp Capsules call `gainXpCore` (not boosted by XP Amplifier). Stat Drives use `driveBonus` (cap +10, HP +40), folded into `recalcStats`.
- Battle chips: `battleAction('item', id)`.
- Modules: one slot per monster, `m.module = {uid,id,ticksLeft}`; bag is `inventory.modules[]`. `tickModules()` runs from `advanceTick`. Burn only while active partner (Sync Link burns on bench too). `lastStand`/`legacyLock` have `ticks:null`.
- Gear: sold via `sellGear`; equipping needs a spare (`gearSpare`); discoveries in `state.gearSeen`.
- Farm automation (Large Estate): `FARM_AUTOMATION` 20k/35k/100k. `harvestAll`, `plantAllPods`, `runAutopilot` share `collectPod`. State in `state.farm.auto`.

## v25 changes (mobile pass)
- CSS: at `max-width:600px` or coarse pointer, every button in `#screen` has `min-height:40px`; tab rows gap 8px.
- Wilderness map and Data Mine: `render()` toggles class `wild-screen` on `#screen` for `wild` and `mine` screens. It removes the fixed height and scroll box so text never gets cut off. Map tiles 26px (was 30).
- Controls: small d-pad (`.dpad-sm`, 36px) on the left. Wilderness has EXIT on the right (`.wild-exit`). Mine has Disconnect and Abandon stacked on the right (`.mine-side`); the centre 🔌 button was removed (`#mn-disconnect2` gone, `#mn-disconnect` is now the right-hand button).
- Town menu reordered into related pairs: Gate/Mine, Wanted/Daily, Jobs/Farm, Training/Breeding, Play/Rest, Storage/Inventory, Shop/Dex, Stats Guide/System.
- Logs: `logMsg` also appends to `state.battle.log` during a fight; the battle screen shows it in `#battle-log` (auto-scrolls to newest). A 📜 Log button (`#log-open`, in `renderStatusbar`) opens `openLogModal()` on every in-game screen; `logSeq`/`logSeenSeq` drive the unread dot (not saved).
- Help + tutorial: `HELP_SECTIONS` (9 topics) drive the Help hub, which reuses screen id `statsGuide` (`renderStatsGuide`, transient `helpSection`). `TUTORIAL_STEPS`/`showTutorial(step)` is a 7-step modal shown on New Game (and on Continue if `state.tutorialDone` is false); replayable from Help. `tutorialDone` defaults false in `defaultState()` and true in `migrateState()` for older saves. When mechanics change, update the Help text.
- Updates: `BUILD` (version/date/notes) near the end of `index.html` is the single source of truth. `tools/sync_version.py` writes it to `version.json`, which the game polls (on load, on tab focus, every 10 min; max once per 5 min) via `checkForUpdate()`; a newer remote version shows a non-blocking banner (Refresh now / Later). After updating, `maybeShowWhatsNew()` shows the notes once (per-browser key `cybertamer_seen_build`). **Release checklist:** bump `BUILD.version` (numeric compare, so 25.10 > 25.9), write player-facing notes, run `python tools/sync_version.py`, commit `index.html` + `version.json` together, then push.
- Play (minigame) costs Energy/Hunger every try and has a per-monster `playCooldown` (3 tries then a break, decays while exploring); it no longer restores Hunger/Energy.
- Motion/FX (v25.2): one FX section before the BUILD block. Logic emits cosmetic events with `fx({k:...})`; `afterRenderFx()` (called at the end of `render()`) plays them via Web Animations (`animate()` helper returns null when motion is off). Battle cards are `#bt-enemy`/`#bt-player`; HP bars slide via `battleHpMemo` + `.hpslide`; the Trap Sphere throw (`playThrow`) runs BEFORE the catch resolves (`battleAction('catch', id, skipAnim)`); `queueEvolution()` (from `checkEvolution`) feeds the full-screen `playNextEvolution()` overlay; Bits count up in the status bar. Motion preference = `localStorage cybertamer_motion` (full/reduced, defaults to the device's reduce-motion setting; `.motion-reduced` on `<html>` also kills CSS animation). Effects must never block or delay game state, and every locked-input path has a fallback timer. Note: the in-app preview browser does not paint frames (rAF and animations don't tick), so visual timing needs a real browser or phone.
- Not yet run: the headless suites against v25 (the harness is not on this machine). Browser smoke tests at 375px passed.

## Invariants (don't break)
- Seeded layouts: don't change RNG call order or pool array length/order for biomes 0-3. Extra features use separate derived PRNGs (`useSeed ^ constant`) placed after base generation.
- Species IDs are append-only.
- Legacy sprites stay byte-identical (except Ferrocog, which got `parts` on purpose).
- New save fields need defaults in both `defaultState()` and `migrateState()`.

## Verification method
Headless jsdom + `node-canvas` harness. Copy the game, inject a hook before the final `init();\n})();` anchor exposing closure functions (`window.__t = {...}`). Never ship the hook. Control time with `clockFn`; patch `window.setTimeout` for synchronous encounter flows. For layout, use the in-app browser at 375x812.

## Open items
- Weekly challenges / event weeks.
- Personality traits, day/night cycle, static town map.
- Mine bosses.
- Balance: Sync Link, gear drop rate, biome level offsets (+6/+8) for a level 50 partner.
- Never checked on a real phone with a full save: long Inventory, the sort bar, Daily screen. Open legend and boss-hint lines on the wilderness map are also unchecked.
