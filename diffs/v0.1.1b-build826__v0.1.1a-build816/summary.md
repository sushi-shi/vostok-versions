# v0.1.1b-build826 -> v0.1.1a-build816

Lists below: **engine only** (`vostok/*`). Third-party counts shown for transparency.

| bucket | engine (`vostok/*`) | third-party |
| --- | ---: | ---: |
| identical | **14136** | 10213 |
| changed | **278** | 9 |
| new / rewritten | **272** | 513 |
| units removed | **2** | 1 |

## Most-changed engine functions (50 shown)

| match % | unit | function |
| ---: | --- | --- |
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
| 11.05 | vostok/render/engine/sources/decal_instance.cpp | `public: void __thiscall vostok::render::decal_shader_constants_and_geometry::set(class vostok::render::renderer_context *, class vostok::math::float4x4const &, class vostok::math::float4x4const &, float, float, class vostok::math::float3const &, class vostok::math::float4x4const &)` |
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
| 13.91 | vostok/render/engine/sources/renderer_context.cpp | `public: void __thiscall vostok::render::renderer_context::set_w(class vostok::math::float4x4const &)` |
| 18.91 | vostok/render/engine/sources/renderer_context.cpp | `public: void __thiscall vostok::render::renderer_context::set_v(class vostok::math::float4x4const &)` |
| 19.77 | vostok/render/engine/sources/stage_postprocess.cpp | `public: void __thiscall vostok::render::scene_shader_constants::set(class vostok::render::renderer_context *, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, float, float, float, class vostok::math::float4const &, struct vostok::render::post_process_parameters const &)` |
| 20.68 | vostok/render/engine/sources/stage_lights.cpp | `private: void __thiscall vostok::render::stage_lights::draw_geometry(class vostok::render::light *)` |
| 24.83 | vostok/render/engine/sources/stage_light_propagation_volumes.cpp | `private: void __thiscall vostok::render::stage_light_propagation_volumes::set_rsm_contants(class vostok::math::float3const &, class vostok::math::float3const &, float)` |
| 26.25 | vostok/render/engine/sources/stage_particles.cpp | `public: void __thiscall vostok::render::particle_shader_constants::set_time(float)` |
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
| 29.64 | vostok/render/engine/sources/renderer_context.cpp | `public: void __thiscall vostok::render::renderer_context::set_p(class vostok::math::float4x4const &)` |
| 32.18 | vostok/render/engine/sources/stage_light_propagation_volumes.cpp | `private: void __thiscall vostok::render::stage_light_propagation_volumes::pre_lpv_batch_render(class vostok::math::float3const &, float, struct vostok::render::geometry_batch const &)` |
| 32.57 | vostok/render/engine/sources/stage_postprocess.cpp | `public: void __thiscall vostok::render::dof_shader_constants::set(class vostok::math::float3const &, float, float, float, float, float, float, float)` |
| 34.44 | vostok/render/engine/sources/grass_world.cpp | `public: void __thiscall vostok::render::grass_world::set_shadow_parameters(unsigned int)` |
| 35.79 | vostok/render/engine/sources/stage_particles.cpp | `public: void __thiscall vostok::render::particle_shader_constants::set(class vostok::math::float3, class vostok::math::float3, class vostok::math::float3, enum vostok::particle::enum_particle_locked_axis, enum vostok::particle::enum_particle_screen_alignment)` |

## Engine units in base but gone in target

- vostok/core_debug_engine.h
- vostok/engine/sources/apc.h
