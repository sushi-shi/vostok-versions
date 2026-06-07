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

## The arc (three weeks, late May 2013)

Two sustained pushes dominate: **weapon mechanics** (recoil/dispersion tied to a
skill, reload/chambering state machines) and **the sound engine** (RMS analysis
removed → codec "cooks" removed → a new propagation model introduced). In
parallel the **renderer** churned through a streaming-texture + SpeedTree
introduction and same-day refactor and began **shadow/culling** work. Underneath,
**memory pools and resource/query structures** were being resized — visible as
add/del noise, but really layout tuning rather than features.

_Covers the ingested 2013 builds. The 2014 jumps (v0.20e+) will extend this once
ingested — expect far larger, genuinely structural change there._
