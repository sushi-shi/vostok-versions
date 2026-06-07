# v0.1.1c-build870 -> v0.1.1b-build826

Lists below: **engine only** (`vostok/*`). Third-party counts shown for transparency.

| bucket | engine (`vostok/*`) | third-party |
| --- | ---: | ---: |
| identical | **12804** | 10011 |
| changed | **1432** | 45 |
| new / rewritten | **514** | 569 |
| units removed | **10** | 2 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
| 0.97 | vostok/render/engine/sources/stage_shadow_direct.cpp | `public: void __thiscall vostok::render::stage_shadow_direct::execute_cascade(unsigned int, unsigned int, unsigned int)` |
| 3.10 | vostok/sound/sources/debug_statistic.cpp | `public: void __thiscall vostok::sound::proxy_statistic::fill_text_tree(class vostok::strings::text_tree_item *, bool) const` |
| 5.00 | vostok/render/engine/sources/render_engine_world_pc_dx11.cpp | `public: void __thiscall vostok::render::engine::world::build_lpv_geometry(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 6.12 | vostok/sound/sources/sound_voice_callbacks.cpp | `public: void __thiscall vostok::sound::sound_voice::on_buffer_start(void *)` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.97 | vostok/game/sources/base_game_scene.cpp | `public: __thiscall survarium::base_game_scene::base_game_scene(class survarium::game &)` |
| 13.62 | vostok/sound/sources/ogg_encoded_sound_interface_cook.cpp | `public: virtual void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 14.00 | vostok/game/sources/game_world_ui.cpp | `public: void __thiscall survarium::game_world_ui::on_unload(void)` |
| 18.00 | vostok/game_core/sources/damage_zone_core.cpp | `survarium::compare_bone_data_predicate` |
| 19.91 | vostok/sound/sources/sound_propagator.cpp | `public: __thiscall vostok::sound::new_sound_propagator::~new_sound_propagator(void)` |
| 22.57 | vostok/game_core/sources/weapon_core.cpp | `public: void __thiscall survarium::weapon_core::instant_show(void)` |
| 25.45 | vostok/sound/sources/sound_scene_proxies.cpp | `public: void __thiscall vostok::sound::sound_scene::free_sound_instance_proxy(class vostok::sound::sound_instance_proxy *)` |
| 27.22 | vostok/resources_resource_ptr_inline.h | `class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 27.88 | vostok/sound/sources/sound_spl.cpp | `public: void __thiscall vostok::sound::sound_spl::load(class vostok::configs::binary_config_value const &)` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.57 | vostok/strings_functions_inline.h | `char * __cdecl vostok::strings::copy(char *, unsigned int, char const *)` |
| 28.85 | vostok/render/engine/sources/effect_motion_blur.cpp | `public: virtual void __thiscall vostok::render::effect_motion_blur::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 29.29 | vostok/animation/sources/cubic_spline_skeleton_animation_cook.cpp | `public: virtual void __thiscall vostok::animation::cubic_spline_skeleton_animation_cook::destroy_resource(class vostok::resources::managed_resource *)` |
| 29.29 | vostok/render/core/dx11/sources/texture_cook.cpp | `public: virtual void __thiscall vostok::render::texture_cook::destroy_resource(class vostok::resources::managed_resource *)` |
| 31.00 | vostok/game_core/sources/animation_analysis_result_cook.cpp | `public: virtual void __thiscall survarium::animation_analysis_result_cook::delete_resource(class vostok::resources::resource_base *)` |
| 31.00 | vostok/game_core/sources/items_cook.cpp | `public: virtual void __thiscall survarium::items_cook::delete_resource(class vostok::resources::resource_base *)` |
| 31.00 | vostok/game_core/sources/items_dictionary_cook.cpp | `public: virtual void __thiscall survarium::items_dictionary_cook::delete_resource(class vostok::resources::resource_base *)` |
| 31.00 | vostok/game_core/sources/player_parameters_cook.cpp | `public: virtual void __thiscall survarium::player_parameters_modifyer_cook::delete_resource(class vostok::resources::resource_base *)` |

## Engine units in base but gone in target

- vostok/ai/fsm_state.h
- vostok/core/engine.h
- vostok/render/engine/sources/effect_environment_probe_lighting.cpp
- vostok/render/engine/sources/effect_gstage_default_materials.h
- vostok/sound/sources/sound_scene_cross_fade.cpp
- vostok/sound/sources/sound_scene_hdr.cpp
- vostok/sound/sources/sound_scene_initialize.cpp
- vostok/sound/sources/sound_scene_path_computation.cpp
- vostok/sound/sources/sound_scene_receivers.cpp
- vostok/sound/sources/sound_scene_statistic.cpp
