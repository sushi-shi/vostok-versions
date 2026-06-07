# v0.1.1a-build816 -> v0.1.1b-build826

Lists below: **engine only** (`vostok/*`). Third-party counts shown for transparency.

| bucket | engine (`vostok/*`) | third-party |
| --- | ---: | ---: |
| identical | **14136** | 10213 |
| changed | **286** | 9 |
| new / rewritten | **328** | 403 |
| units removed | **4** | 3 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
| 6.08 | vostok/game/sources/game_project.cpp | `public: class survarium::victory_items_container_core * __thiscall survarium::simple_game_project::get_items_container(unsigned char)` |
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
| 7.39 | vostok/animation/anim_track_common.h | `vostok::animation::`dynamic initializer for 'zero''` |
| 9.96 | vostok/game/sources/game.cpp | `private: void __thiscall survarium::game::register_console_commands(void)` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 16.09 | vostok/render/core/dx11/sources/backend_handlers.cpp | `private: void __thiscall vostok::render::constants_handler<1>::update_buffers(void)` |
| 16.09 | vostok/render/core/dx11/sources/backend_handlers.cpp | `private: void __thiscall vostok::render::constants_handler<1>::update_buffers(void)` |
| 16.09 | vostok/render/core/dx11/sources/backend_handlers.cpp | `private: void __thiscall vostok::render::constants_handler<1>::update_buffers(void)` |
| 23.90 | vostok/render/core/dx11/sources/shader_constant_buffer.cpp | `public: void __thiscall vostok::render::shader_constant_buffer::update(void)` |
| 24.99 | vostok/render/engine/sources/stage_lights.cpp | `private: void __thiscall vostok::render::stage_lights::render_particle_lighting(class vostok::render::render_particle_emitter_instance *, class vostok::render::light *, unsigned int)` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.20 | vostok/math_curve_inline.h | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 28.38 | vostok/render/engine/sources/radiance_volume.cpp | `public: void __thiscall vostok::render::radiance_volume::inject_camera_occluders(class vostok::render::renderer_context *)` |
| 29.48 | vostok/render/engine/sources/stage_lights.cpp | `private: void __thiscall vostok::render::stage_lights::render_model_lighting(struct vostok::render::render_surface_instance *, class vostok::render::light *)` |
| 31.50 | vostok/render/core/dx11/backend_inline.h | `public: void __thiscall vostok::render::backend::set_ps_constant<unsigned int>(class vostok::render::shader_constant_host const *, unsigned int const &)` |
| 31.50 | vostok/render/core/dx11/backend_inline.h | `public: void __thiscall vostok::render::backend::set_ps_constant<unsigned int>(class vostok::render::shader_constant_host const *, unsigned int const &)` |
| 31.50 | vostok/render/core/dx11/backend_inline.h | `public: void __thiscall vostok::render::backend::set_ps_constant<unsigned int>(class vostok::render::shader_constant_host const *, unsigned int const &)` |

## Engine units in base but gone in target

- vostok/ai/fsm_state.h
- vostok/core/engine.h
- vostok/render/core/dx11/backend_handlers_inline.h
- vostok/render/facade/base_command.h
