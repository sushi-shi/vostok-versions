# Survarium build evolution — interpreted changes (May 2013)

What the team was most likely working on, **inferred only from added and deleted
hand-written engine functions** across the consecutive internal builds
802 → 816 → 826 → 870 → 884 (9–28 May 2013). Added/deleted are unambiguous
"a function/class appeared or vanished" events, unlike fuzzy match-% drift.

## How to read this (and where it lies)

Three ways add/del can mislead, accounted for below:

- **Same-day refactors look like add-then-remove.** 816 and 826 are the same day
  (14 May). A class added in 816 and "removed" in 826 was almost certainly
  *renamed/restructured*, not introduced and deleted.
- **Offset-parameterized templates are layout drift, not features.** Containers
  like `intrusive_list<…,608,…>` or `single_size_buffer_allocator<108>` bake a
  struct's member offset / object size into a template argument. When a member
  moves, the argument changes and the old/new instantiations show up as
  delete+add — a *layout* change, not a feature.
- The trustworthy signal is **named gameplay/engine classes**
  (`weapon_core`, `sound_rms`, `medkit`, `booby_trap`, `new_sound_propagator`).

---

## 802 → 816 (9 → 14 May): weapons, streamed rendering, sound trim

- **A major weapon state-machine buildout.** `weapon_core` alone gained 44
  functions and lost 20 — a wave of aim/fire/reload predicates (`aimed_fire_pred`,
  `chamber_a_round_*`, `can_jump/can_reload/can_sprint`) — alongside reworked
  `weapon`, `weapon_user_animations_selector`, `weapon_core_shotgun_reload_state`
  and `damage_model`. New `character_dispersion_skill_influence` + reworked
  `character_dispersion_calculator` suggest **weapon spread/accuracy now responds
  to a character skill**.
- **Texture streaming and SpeedTree entered the renderer:** new
  `streaming_ready_texture`, `requested_streamable_texture`,
  `streamable_texture_info` (a streamed-texture pipeline), `speedtree_data`
  (vegetation), plus `game_scene` and instanced `animated_model_instance`.
- **The `sound_rms` subsystem was removed** (`sound_rms`, `sound_rms_cook`,
  `sound_rms_pinned` and its resource pointers) — an RMS/loudness analysis path
  dropped.

## 816 → 826 (14 May, same day): a streaming-texture refactor

Nearly everything "new" in 816's renderer — `streaming_ready_texture`,
`requested_streamable_texture`, `streamable_texture_info`, `speedtree_data`,
`animated_model_instance` — appears as **removed** the same day, while
`render::backend`, `shader_constant_buffer` and the `constants_handler` templates
are reworked. This is **not a feature reversal but a same-day refactor** of the
just-landed streaming-texture code (renamed or folded into other types).
`weapon_core` keeps churning; `particle::lod_entry` reappears.

## 826 → 870 (14 → 24 May): a sound-engine rearchitecture

The 10-day gap is the largest change in the window (101 reworked scopes), and the
dominant theme is **sound**:

- The old codec/"cook" pipeline was torn out — `ogg_sound_cook`,
  `ogg_source_cook`, `ogg_file_contents_cook`, `wav_encoded_sound_interface_cook`,
  `sound_environment_cook`, `ogg_sound`, `effect_cross_fader` all removed.
- A **new sound-propagation path** appears (`new_sound_propagator`) with heavily
  reworked `sound_scene`, `sound_voice`, `single_sound_cook`.
- **Memory pools were retuned:** allocator pools of size 28/108/136 removed and
  32/84/96 added — pooled object sizes changed (layout/tuning, not gameplay).
- Breadth elsewhere: `booby_trap_set_core` (mines/traps), `game_world_ui`,
  `network_client`, physics collision shapes as resources, a shader cache.

## 870 → 884 (24 → 28 May): resource/query layout + shadows

- Most add/del here is **layout drift, not features**: a cluster of
  `intrusive_list<resources::query_result, …, 600/608/616/624, …>` instantiations
  swap offsets — the `query_result` struct grew/shifted members, changing the
  baked-in offsets. It counts as +/− but is one structure changing shape.
- Real work shows in **rendering/shadows** (`stage_shadow_direct`, `sun_cascade`
  removed, `renderer`, `portal_sector_system` culling), **resources**
  (`resources_manager`, `hdd_manager`), a **new filesystem** layer
  (`fs_new::virtual_path_string`), and `medkit` gameplay.

---

---

# Part II — into 2014 (v0.20+)

The 10-month gap from build 884 (28 May 2013) to build 1916 (20 Mar 2014) is the
hinge of the dataset. One caveat first: across this jump the add/del counts carry
more noise than the 2013 steps — aligning a v0.20 build's folded symbols to the
year-older base 802 falls back heavily — so treat the **magnitude and the named
classes** as solid and the exact integers as approximate.

## 884 → 1916 (28 May 2013 → 20 Mar 2014): the pivot — AI shooter → PvP

Near-total rewrite: only **172 functions byte-identical** (+4163 / −6812 / ~4526).
The named-class signal is unambiguous and matches Survarium's real history:

- **Removed — the single-player AI/NPC combat system:** `human_npc` (with
  `attack`, `attack_from_cover`, `attack_melee`, `move_to_position`,
  `is_target_in_melee_range`), `ai::brain_unit`, `ai::ai_world`, `ai::planning`;
  also the `light_propagation_volumes` GI stage and the collision double-dispatchers.
- **Added — PvP match infrastructure:** `game_world_core`, `game_statistics_handler`,
  `player_respawn_rule`, `gather_victory_items_rule` (game-mode win rules),
  `artefact_spring_core`, an animation `n_ary_tree_serializer`.
- **Reworked broadly:** `render::effect_manager`, `weapon_core`, `player` /
  `base_player`, `memory`, `vfs`, `lobby_menu`, `game_world_ui`.

This is the cancelled-S.T.A.L.K.E.R.2 → free-to-play PvP shooter transition,
captured in which functions vanished and appeared. Build flags track it too (see
`BUILD_FLAGS.md`): `vostok_sound` flipped `-Od` → LTCG and `vostok_core` went
full-LTCG → explicit `-O1` — otherwise the toolchain/flags were unchanged.

## 1916 → 1923 (20 Mar → 1 Apr 2014): a hotfix

Essentially nothing: +1 / −3 / ~11, 8847 identical. A point release of the same
v0.20 engine; no flag changes.

## 1923 → 2010 (1 → 24 Apr 2014): netcode & match statistics

A normal ~3-week delta within v0.2x (+605 / −383 / ~2566 — not a rewrite),
concentrated on multiplayer plumbing:

- **New — a network telemetry subsystem:** `network_stats_packets`,
  `network_stats_ports`, `network_stats_sent_messages` / `_received_messages` /
  `_rejected_messages`, `network_stats_packets_sequence`,
  `network_stats_orders_channel`, `udp_match_stats`, `base_game_statistics_handler`
  — packet-loss / match-stats instrumentation.
- **Reworked:** `lobby_menu`, `lobby_client`, and a physics character-controller
  swap (`old_bullet_character_controller` removed, `bullet_character_controller`
  reworked).
- **Removed:** the debug renderer (`render::debug::renderer`, `draw_lines_command`,
  `draw_triangles_command`) and `jump_logic`.

---

## The full arc (May 2013 → Apr 2014)

**2013 (v0.1):** three weeks of iteration — weapon mechanics (dispersion-skill,
reload/chambering state machines) and a sound-engine rearchitecture (RMS → codec
cooks → new propagation), with renderer streaming-texture/SpeedTree churn.
**Early 2014 (v0.20):** the pivot — the single-player AI/NPC system torn out, PvP
match infrastructure (game modes, lobby, respawn rules, statistics) added, and the
audio path moved to LTCG. **Spring 2014 (v0.2x):** netcode and match-statistics
polish on the new PvP base, plus a physics character-controller swap.

From a S.T.A.L.K.E.R.2-style AI shooter to a free-to-play PvP match game, traced
function by function.

_Covers all ingested builds (802 → 2010). v0.23h-build2285 is stripped (no PDB),
so it stays out of the function-level diff._
