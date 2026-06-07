# Survarium cross-version chain report

Engine (`vostok/*`) functions, deduped by demangled name. `changed` magnitude is the lowest match % across units.

## Overview

| step | from | to | +added | -deleted | ~changed | =identical |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | v0.100b-build802 | v0.1.1a-build816 | 108 | 78 | 429 | 12267 |
| 2 | v0.1.1a-build816 | v0.1.1b-build826 | 36 | 49 | 298 | 12457 |
| 3 | v0.1.1b-build826 | v0.1.1c-build870 | 173 | 202 | 1538 | 11051 |
| 4 | v0.1.1c-build870 | v0.1.1e-build884 | 47 | 58 | 514 | 12190 |

---

## v0.100b-build802 → v0.1.1a-build816
_2013-05-09 → 2013-05-14 · +108 / -78 / ~429_

### Changed (429)

| match % | function |
| ---: | --- |
| 0.00 | `[thunk]: __thiscall vostok::network::world::`vcall'{0, {flat}}` |
| 0.00 | `[thunk]: public: virtual void * __thiscall survarium::ladder::`vector deleting destructor'(unsigned int)` |
| 0.00 | `empty_stub` |
| 0.00 | `long __cdecl vostok::threading::interlocked_decrement(long volatile &)` |
| 0.00 | `private: bool __thiscall survarium::weapon_user_animations_selector::jump_predicate(void) const` |
| 0.00 | `private: virtual void * __thiscall survarium::booby_trap::`vector deleting destructor'(unsigned int)` |
| 0.00 | `private: virtual void __thiscall survarium::medkit::tick(void)` |
| 0.00 | `protected: virtual void __thiscall survarium::weapon_core_shotgun_reload_finish_substate::finalize(void)` |
| 0.00 | `public: __thiscall boost::function0<bool>::~function0<bool>(void)` |
| 0.00 | `public: __thiscall survarium::vector<class vostok::variant<32> const *>::~vector<class vostok::variant<32> const *>(void)` |
| 0.00 | `public: __thiscall vostok::ai::brain_unit_cook_params::~brain_unit_cook_params(void)` |
| 0.00 | `public: __thiscall vostok::animation::mixing::animation_interval::~animation_interval(void)` |
| 0.00 | `public: __thiscall vostok::math::float3::float3(void)` |
| 0.00 | `public: __thiscall vostok::network::order::order(void)` |
| 0.00 | `public: __thiscall vostok::one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >::~one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >(void)` |
| 0.00 | `public: __thiscall vostok::render::box_geometry::~box_geometry(void)` |
| 0.00 | `public: __thiscall vostok::render::stage_lights::lights_instance::lights_instance(void)` |
| 0.00 | `public: __thiscall vostok::render::sun_cascade::sun_cascade(struct vostok::render::sun_cascade const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::unmanaged_resource *)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::vfs::query_mount_arguments::~query_mount_arguments(void)` |
| 0.00 | `public: __thiscall vostok::vfs::vfs_mount::~vfs_mount(void)` |
| 0.00 | `public: class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::operator=(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 0.00 | `public: class vostok::vfs::query_mount_arguments & __thiscall vostok::vfs::query_mount_arguments::operator=(class vostok::vfs::query_mount_arguments const &)` |
| 0.00 | `public: virtual __thiscall survarium::inventory_cook::~inventory_cook(void)` |
| 0.00 | `public: virtual __thiscall vostok::render::functor_command::~functor_command(void)` |
| 0.00 | `public: virtual bool __thiscall Scaleform::MemoryFile::Flush(void)` |
| 0.00 | `public: virtual void * __thiscall Scaleform::GFx::State::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::artefact_base::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::empty_hands::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::lobby_camera::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::lobby_menu::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::player_cook::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::player_logic_base_state::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::planning::operator_base::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::sensors::smell_sensor::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::animation::mixing::addition_lexeme::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::detail::abstract_type_helper::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::memory::base_allocator::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::network::functor_order::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::physics::animated_model_instance::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::base_scene::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::effect_sun::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::render_model_instance_impl::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::render_surface::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::speedtree_tree_component::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::sound::sound_spl_cook::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void __thiscall survarium::game_camera::on_focus(bool)` |
| 0.00 | `public: virtual void __thiscall survarium::weapon_core::tick(void)` |
| 0.00 | `public: virtual void __thiscall vostok::network::functor_order::execute(void)` |
| 0.00 | `public: void * __thiscall boost::_bi::bind_t<void, class boost::_mfi::mf2<void, class survarium::object_wire, class vostok::resources::queries_result &, class boost::function<void __cdecl (class survarium::game_object_&)> &>, class boost::_bi::list3<class boost::_bi::value<class survarium::object_wire *>, struct boost::arg<1>, class boost::_bi::value<class boost::function<void __cdecl (class survarium::game_object_&)> > > >::`scalar deleting destructor'(unsigned int)` |
| 0.00 | `survarium::true_predicate` |
| 0.00 | `vec_begin` |
| 0.00 | `vostok::animation::`dynamic initializer for 'zero''` |
| 12.00 | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 21.12 | `protected: virtual void __thiscall survarium::weapon_core_aimed_fire_state_base::initialize(void)` |
| 39.68 | `protected: virtual void __thiscall survarium::weapon_core_aimed_fire_state_base::finalize(void)` |
| 40.13 | `public: bool __thiscall survarium::swf_input_translator::process_keyboard(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action, struct survarium::flash_movie *, unsigned int)` |
| 40.60 | `private: virtual void __thiscall survarium::weapon_core_aimed_fire_state_base::on_animation_end_impl(bool &)` |
| 40.60 | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::on_animation_end_impl(bool &)` |
| 48.57 | `private: virtual void __thiscall survarium::weapon_core_idle_state_base::finalize(void)` |
| 51.73 | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::finalize(void)` |
| 59.61 | `private: void __thiscall survarium::weapon_core_shotgun_reload_state::initialize_logic(class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *)` |
| 59.90 | `public: virtual void __thiscall survarium::weapon_core::instant_aim_start(void)` |
| 60.00 | `protected: virtual void __thiscall survarium::weapon_core_hide_state_base::finalize(void)` |
| 60.00 | `protected: virtual void __thiscall survarium::weapon_core_show_state_base::finalize(void)` |
| 65.95 | `private: virtual void __thiscall survarium::weapon::deactivate(void)` |
| 65.96 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_shotgun_reload_finish_substate::on_animation_end(struct vostok::animation::animation_callback_params &)` |
| 65.98 | `protected: virtual void __thiscall survarium::weapon_core_fire_state_base::initialize(void)` |
| 67.05 | `public: __thiscall survarium::player_profile::player_profile(void)` |
| 69.82 | `public: virtual void __thiscall survarium::relocate_item_func::call(struct survarium::flash_function_handler_params &)` |
| 70.00 | `protected: virtual void __thiscall survarium::weapon_core_hide_state_base::initialize(void)` |
| 70.00 | `protected: virtual void __thiscall survarium::weapon_core_show_state_base::initialize(void)` |
| 70.89 | `private: void __thiscall vostok::sound::single_sound_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 70.92 | `public: void __thiscall survarium::weapon_core::instant_idle_start(void)` |
| 71.11 | `public: virtual void __thiscall survarium::weapon_core::instant_aim_end(void)` |
| 73.21 | `private: bool __thiscall survarium::weapon_core_shotgun_reload_state::finish_reload_predicate(void) const` |
| 76.91 | `vostok::render::fill_light` |
| 80.30 | `void __cdecl vostok::render::register_samplers(void)` |
| 80.36 | `private: void __thiscall vostok::network::match_client::on_packet_received_impl(unsigned char, class vostok::network_core::packet_reader &)` |
| 80.70 | `private: void __thiscall survarium::weapon_core::initialize_weapon_logic(class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::weapon_core_base_state, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 82.15 | `protected: void __thiscall survarium::swf_input_translator::initialize(void)` |
| 85.60 | `private: virtual void __thiscall survarium::player_logic_sprint_state::initialize(void)` |
| 85.88 | `private: virtual void __thiscall survarium::weapon_core::serialize(class vostok::network_core::udp_match_packet &, unsigned int) const` |
| 86.81 | `public: bool __thiscall survarium::damage_model::hit_body_part(unsigned char, char const *, char const *, float, float, unsigned int, class survarium::bullet *const)` |
| 88.39 | `public: virtual __thiscall vostok::sound::single_sound::~single_sound(void)` |
| 88.88 | `public: void __thiscall survarium::weapon_user_animations_selector::serialize(class vostok::network_core::udp_match_packet &) const` |
| 89.35 | `private: virtual void __thiscall survarium::player::on_fire(void)` |
| 89.57 | `private: void __thiscall survarium::lobby_menu::request_status_from_server_impl(unsigned int, unsigned int)` |
| 89.61 | `public: void __thiscall survarium::weapon_user_animations_selector::tick(void)` |
| 90.17 | `public: void __thiscall survarium::character_dispersion_calculator::tick(enum survarium::weapon_user_state_enum, bool, bool, unsigned char, bool, unsigned int)` |
| 91.08 | `public: virtual void __thiscall vostok::sound::single_sound_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 91.11 | `private: void __thiscall vostok::sound::sound_world::register_sound_cooks(void)` |
| 91.19 | `public: void __thiscall survarium::weapon_user_animations_selector::deserialize(class vostok::network_core::packet_reader &)` |
| 91.20 | `public: virtual void __thiscall survarium::respawn_point_core::load(class vostok::configs::binary_config_value const &)` |
| 91.39 | `private: virtual void __thiscall survarium::weapon_core::deserialize(class vostok::network_core::packet_reader &)` |
| 92.18 | `public: void __thiscall survarium::weapon_core::instant_fire(unsigned int)` |
| 92.24 | `public: __thiscall survarium::weapon_core::weapon_core(void)` |
| 92.43 | `public: __thiscall survarium::respawn_point_core::respawn_point_core(void)` |
| 93.24 | `public: float __thiscall survarium::dispersion_calculator::get_dispersion(void) const` |
| 94.08 | `public: virtual bool __thiscall survarium::lobby_menu::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 94.08 | `private: void __thiscall survarium::player::insert_alive(void)` |
| 94.12 | `protected: void __thiscall survarium::swf_input_translator::register_ctl_bind(enum vostok::input::enum_keyboard, int)` |
| 94.19 | `public: __thiscall survarium::base_player_creation_params::base_player_creation_params(void)` |
| 94.32 | `public: void __thiscall survarium::player_profile::deserialize(class vostok::network_core::packet_reader &)` |
| 94.39 | `protected: __thiscall survarium::weapon_core_aimed_state_base::weapon_core_aimed_state_base(class survarium::weapon_core &)` |
| 94.39 | `protected: __thiscall survarium::weapon_core_idle_state_base::weapon_core_idle_state_base(class survarium::weapon_core &)` |
| 94.56 | `public: void __thiscall survarium::lobby_menu::on_stats_message_arrived(wchar_t const *, wchar_t const *, enum messaging::message_channel_enum)` |
| 95.10 | `public: void __thiscall survarium::player::tick(unsigned int)` |
| 95.13 | `public: virtual void __thiscall survarium::weapon_core::set_next_ammo_type(void)` |
| 95.56 | `public: __thiscall survarium::base_player::base_player(struct survarium::base_player_creation_params const &, class survarium::scheduler &)` |
| 95.91 | `public: virtual bool __thiscall survarium::chat_handler::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 96.39 | `protected: __thiscall survarium::weapon_core_aimed_fire_state_base::weapon_core_aimed_fire_state_base(class survarium::weapon_core &, float)` |
| 96.60 | `protected: __thiscall survarium::weapon_core_chamber_a_round_aimed_state_base::weapon_core_chamber_a_round_aimed_state_base(class survarium::weapon_core &, float)` |
| 96.60 | `protected: __thiscall survarium::weapon_core_chamber_a_round_state_base::weapon_core_chamber_a_round_state_base(class survarium::weapon_core &, float)` |
| 96.60 | `protected: __thiscall survarium::weapon_core_hide_state_base::weapon_core_hide_state_base(class survarium::weapon_core &, bool &)` |
| 96.60 | `protected: __thiscall survarium::weapon_core_reload_state_base::weapon_core_reload_state_base(class survarium::weapon_core &, float)` |
| 96.63 | `protected: __thiscall survarium::weapon_core_fire_state_base::weapon_core_fire_state_base(class survarium::weapon_core &, float)` |
| 96.63 | `protected: __thiscall survarium::weapon_core_show_state_base::weapon_core_show_state_base(class survarium::weapon_core &, bool &)` |
| 96.81 | `public: virtual class vostok::animation::mixing::expression __thiscall survarium::weapon_core::selected_animations(class vostok::mutable_buffer &, bool) const` |
| 96.81 | `public: __thiscall survarium::weapon_core_shotgun_reload_state::weapon_core_shotgun_reload_state(class survarium::weapon_core &, class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *, class survarium::weapon_core_shotgun_reload_base_substate *)` |
| 97.09 | `public: __thiscall survarium::damage_model::damage_model(enum survarium::affects_applying_type_enum)` |
| 97.59 | `public: void __thiscall survarium::weapon_core::reload_one_round(void)` |
| 98.08 | `private: void __thiscall vostok::render::stage_lights::render_to_hw_shadowmap(class vostok::render::light *, unsigned int, float, unsigned int, unsigned int, class vostok::math::float4x4const &, class vostok::math::float4x4const &, unsigned int)` |
| 98.42 | `private: void __thiscall survarium::player_cook::on_config_loaded(class vostok::resources::queries_result &)` |
| 98.44 | `public: virtual void __thiscall survarium::weapon_core_inactive_state_cook::create_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, class vostok::mutable_buffer)` |
| 98.61 | `public: __thiscall survarium::weapon_user_animations_selector::weapon_user_animations_selector(void)` |
| 98.62 | `private: void __thiscall vostok::network::login_client_impl::sign_up_on_connected(enum vostok::connection_error_types_enum, class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum, struct vostok::sign_up_info const &)> const &, struct vostok::sign_up_info const &)` |
| 98.71 | `public: virtual bool __thiscall survarium::game_options::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 98.93 | `private: void __thiscall vostok::render::stage_lights::make_spot_light_shadowmap(unsigned int, class vostok::render::light *)` |
| 99.21 | `private: void __thiscall vostok::render::stage_lights::make_plane_spot_light_shadowmap(unsigned int, class vostok::render::light *)` |
| 99.31 | `public: virtual void __thiscall survarium::weapon_core::activate(struct survarium::base_player &, struct survarium::engine &)` |
| 99.32 | `private: void __thiscall vostok::vfs::archive_mounter::mount_archive_to_parent(void **, class vostok::vfs::base_folder_node<1> *, class vostok::fs_new::synchronous_device_interface &)` |
| 99.33 | `public: __thiscall vostok::animation::animation_player::animation_player(void)` |
| 99.33 | `public: void __thiscall survarium::player::set_target_fov_factor(float, float)` |
| 99.40 | `public: void __thiscall survarium::player::reset_fov_factor(void)` |
| 99.50 | `private: virtual bool __thiscall survarium::player::is_replaying_history(void) const` |
| 99.50 | `private: virtual class survarium::player_stamina & __thiscall survarium::player::stamina(void)` |
| 99.50 | `private: virtual class vostok::animation::animation_player & __thiscall survarium::player::animation_player(void)` |
| 99.50 | `private: virtual class vostok::math::float3const & __thiscall survarium::player::position(void) const` |
| 99.50 | `private: virtual class vostok::math::float4x4const & __thiscall survarium::player::get_transform(void) const` |
| 99.50 | `private: virtual class vostok::physics::bt_character_controller & __thiscall survarium::player::physics_controller(void)` |
| 99.50 | `private: virtual float __thiscall survarium::player::get_look_pitch(void) const` |
| 99.50 | `private: virtual struct survarium::player_input const & __thiscall survarium::player::input(void) const` |
| 99.50 | `private: void __thiscall survarium::player::remove_oldest_history_item(void)` |
| 99.50 | `public: bool __thiscall survarium::base_player::is_alive(void) const` |
| 99.50 | `public: bool __thiscall survarium::weapon_core::round_is_chambered(void) const` |
| 99.50 | `public: struct survarium::base_player * __thiscall survarium::weapon_core::get_user(void) const` |
| 99.50 | `public: unsigned int __thiscall vostok::animation::animation_player::last_tick_time_in_ms(void) const` |
| 99.50 | `public: virtual class vostok::resources::resource_ptr<class survarium::damage_model, class vostok::resources::unmanaged_intrusive_base> const & __thiscall survarium::player::damage_model(void) const` |
| 99.50 | `public: virtual enum survarium::game_team_id __thiscall survarium::player::team(void) const` |
| 99.50 | `public: void __thiscall survarium::base_player::force_animation_selection(void)` |
| 99.53 | `private: virtual void __thiscall survarium::weapon::instant_aim_end(void)` |
| 99.53 | `private: void __thiscall survarium::player::remove_oldest_history_items(unsigned int)` |
| 99.62 | `private: void * __thiscall vostok::animation::animation_player::get_next_buffer(unsigned int)` |
| 99.66 | `public: __thiscall survarium::player::player(struct survarium::player_creation_params const &)` |
| 99.67 | `private: virtual class vostok::animation::skeleton const & __thiscall survarium::player::skeleton(void) const` |
| 99.67 | `public: virtual struct vostok::physics::world * __thiscall survarium::player::get_physics_world(void)` |
| 99.67 | `vostok::math::`dynamic initializer for 'SNaN''` |
| 99.68 | `private: void __thiscall survarium::network_client::on_connected_to_match(enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::lobby_server_message_types_enum)` |
| 99.68 | `private: void __thiscall vostok::render::stage_lights::render_shadowed_light(class vostok::render::light *)` |
| 99.68 | `private: void __thiscall survarium::player::remove_alive(void)` |
| 99.69 | `private: virtual void __thiscall survarium::weapon::instant_aim_start(void)` |
| 99.70 | `private: virtual void __thiscall survarium::player::end_jump(void)` |
| 99.75 | `public: unsigned short __thiscall survarium::weapon_core::fire_queue_length(void) const` |
| 99.75 | `public: void __thiscall survarium::player::attach_controller(class survarium::player_input_handler *, class survarium::stats_graph *, class survarium::stats_graph *, class survarium::game_world_ui *)` |
| 99.75 | `public: void __thiscall survarium::player::detach_controller(void)` |
| 99.75 | `survarium::is_alive` |
| 99.77 | `public: __thiscall survarium::character_dispersion_calculator::character_dispersion_calculator(void)` |
| 99.78 | `private: void __thiscall survarium::player::serialize_current_state(unsigned int)` |
| 99.79 | `public: void __thiscall survarium::dispersion_calculator::set_weapon(class survarium::weapon_core *)` |
| 99.80 | `public: void __thiscall survarium::player::time_warp(struct survarium::server_player_update const &, unsigned int)` |
| 99.80 | `private: void __thiscall vostok::intrusive_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::dec(void)` |
| 99.81 | `private: void __thiscall survarium::player::set_head_visibility(bool)` |
| 99.82 | `public: bool __thiscall vostok::animation::animation_player::tick(unsigned int)` |
| 99.83 | `public: __thiscall survarium::base_player_creation_params::~base_player_creation_params(void)` |
| 99.83 | `public: void __thiscall survarium::player::update_camera(void)` |
| 99.83 | `public: __thiscall vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 99.83 | `public: virtual __thiscall survarium::player::~player(void)` |
| 99.83 | `private: void __thiscall survarium::dispersion_calculator::apply_aim_speed(void)` |
| 99.83 | `private: void __thiscall survarium::player::replay_history(unsigned int, class vostok::math::float4x4&)` |
| 99.83 | `private: virtual void __thiscall survarium::player::subscribe_on_actions(class survarium::player_actions_subscriber *)` |
| 99.83 | `public: void __thiscall survarium::player::hide(void)` |
| 99.83 | `public: void __thiscall survarium::player::set_near_plane_factor(float)` |
| 99.83 | `public: void __thiscall survarium::player::show(void)` |
| 99.83 | `public: void __thiscall vostok::animation::animation_player::set_object_transform(class vostok::math::float4x4const &, void const *const)` |
| 99.83 | `survarium::is_dead` |
| 99.83 | `private: void __thiscall survarium::player::update_speed_info(void)` |
| 99.84 | `private: void __thiscall survarium::network_client::setup_camera_for_warmup(void)` |
| 99.84 | `public: void __thiscall survarium::player::insert(bool)` |
| 99.84 | `public: float __thiscall survarium::player::fov_factor(unsigned int) const` |
| 99.85 | `private: unsigned int __thiscall survarium::player::history_lower_bound_index(unsigned int) const` |
| 99.85 | `private: void __thiscall survarium::player::add_models_to_scene(void)` |
| 99.85 | `public: bool __thiscall vostok::animation::animation_player::tick_to_nearest_user_handled_callback(unsigned int)` |
| 99.86 | `private: virtual struct survarium::engine & __thiscall survarium::player::get_engine(void)` |
| 99.86 | `private: void __thiscall survarium::player::render(unsigned int, unsigned int)` |
| 99.86 | `public: __thiscall survarium::dispersion_calculator::dispersion_calculator(void)` |
| 99.86 | `public: void __thiscall vostok::animation::animation_player::convert_to_object_matrices(class vostok::animation::skeleton const &, class vostok::math::float4x4*, class vostok::math::float4x4*, void const *const) const` |
| 99.86 | `private: void __thiscall survarium::player::compute_bones(unsigned int)` |
| 99.87 | `private: void __thiscall survarium::player::notify_actions_subscribers(void)` |
| 99.87 | `private: struct survarium::player_input __thiscall survarium::player::remote_input(void) const` |
| 99.87 | `private: void __thiscall survarium::player::set_physics_controller_walk_vector(struct survarium::client_player_state &)` |
| 99.87 | `private: void __thiscall survarium::weapon_core::update_breath_vibration(bool, unsigned int, float)` |
| 99.87 | `public: void __thiscall survarium::client_player_state::update_transform(void)` |
| 99.87 | `public: void __thiscall survarium::player::remove(void)` |
| 99.87 | `private: virtual void __thiscall survarium::player::jump(void)` |
| 99.88 | `public: virtual bool __thiscall survarium::login_menu::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 99.88 | `public: void __thiscall survarium::player::set_character_transform(class vostok::math::float3const &, float, float)` |
| 99.88 | `public: __thiscall survarium::client_player_state::~client_player_state(void)` |
| 99.88 | `public: void __thiscall vostok::animation::animation_player::reset(bool)` |
| 99.88 | `public: virtual __thiscall survarium::weapon_core::~weapon_core(void)` |
| 99.89 | `private: void __thiscall survarium::player::restore_history_item(struct survarium::client_player_history_item &)` |
| 99.89 | `public: class vostok::math::float4x4 __thiscall vostok::animation::animation_player::get_object_transform(void const *const) const` |
| 99.89 | `public: virtual class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const & __thiscall vostok::sound::single_sound::get_sound_spl(void) const` |
| 99.89 | `public: void __thiscall survarium::player::set_use_physics_controller_for_current(bool)` |
| 99.89 | `public: void __thiscall survarium::weapon_core::remove_animation_callback(char const *, void const *)` |
| 99.89 | `public: void __thiscall survarium::weapon_core::remove_animation_callback(enum vostok::animation::reserved_channel_ids_enum, void const *)` |
| 99.89 | `public: void __thiscall vostok::animation::animation_player::compute_bones_local_matrices(class vostok::animation::skeleton const &, class vostok::math::float4x4*, class vostok::math::float4x4*, void const *const, unsigned int *) const` |
| 99.89 | `public: void __thiscall vostok::animation::animation_player::compute_bones_matrices(class vostok::animation::skeleton const &, class vostok::math::float4x4*, class vostok::math::float4x4*, void const *const, unsigned int *) const` |
| 99.89 | `public: void __thiscall survarium::player::kill(unsigned int)` |
| 99.89 | `private: void __thiscall survarium::player::remove_models_from_scene(void)` |
| 99.89 | `public: void __thiscall survarium::character_dispersion_calculator::set_character_dispersion_params(struct survarium::character_dispersion_params const *)` |
| 99.89 | `private: enum vostok::animation::body_part_masks_enum __thiscall survarium::weapon_core::get_body_part_mask_for_user(void) const` |
| 99.89 | `private: void __thiscall survarium::network_client::game_world_object_state_arrived(class vostok::network_core::packet_reader &)` |
| 99.90 | `public: char const * __thiscall vostok::network::login_client::host_ip_address(void) const` |
| 99.90 | `public: char const * __thiscall vostok::network::login_client::server_browser_address(void) const` |
| 99.90 | `public: char const * __thiscall vostok::network::login_client::server_browser_initial_query(void) const` |
| 99.90 | `public: void __thiscall survarium::dispersion_calculator::set_shooting_skill_coeff(float)` |
| 99.90 | `private: void __thiscall survarium::profile_character::character_model_ready(class vostok::resources::queries_result &)` |
| 99.90 | `public: void __thiscall survarium::base_network_client::attach_to_player(class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>)` |
| 99.90 | `public: void __thiscall vostok::animation::animation_player::serialize_state(void *, unsigned int)` |
| 99.90 | `private: void __thiscall survarium::network_client::damage_model_state_arrived(class vostok::network_core::packet_reader &)` |
| 99.91 | `private: void __thiscall survarium::network_client::player_visibility_change(class vostok::network_core::packet_reader &)` |
| 99.91 | `private: virtual void __thiscall survarium::player::unsubscribe_from_actions(class survarium::player_actions_subscriber *)` |
| 99.91 | `private: bool __thiscall vostok::animation::animation_player::try_get_transform(void const *, class vostok::math::float4x4&) const` |
| 99.91 | `public: virtual void __thiscall survarium::weapon_core::deactivate(void)` |
| 99.91 | `public: void __thiscall vostok::animation::animation_player::subscribe(char const *, class boost::function<enum vostok::animation::callback_return_type_enum __cdecl (struct vostok::animation::animation_callback_params &)> const &, void const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, unsigned char, void const *const)` |
| 99.91 | `private: void __thiscall survarium::weapon_core::update_dispersion(bool, unsigned int)` |
| 99.91 | `public: virtual class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base> __thiscall survarium::network_client::get_player(unsigned char) const` |
| 99.91 | `public: void __thiscall survarium::profile_player_character::clear_resources(void)` |
| 99.91 | `private: void __thiscall survarium::network_client::destroy_player_impl(unsigned char)` |
| 99.91 | `private: virtual void __thiscall survarium::network_client::apply_use_physics_controller_for_current(void)` |
| 99.92 | `private: virtual void __thiscall survarium::player::unsubscribe_animation_player(enum vostok::animation::reserved_channel_ids_enum, void const *)` |
| 99.92 | `private: virtual void __thiscall survarium::weapon::on_chamber_a_round(void)` |
| 99.92 | `private: virtual void __thiscall survarium::weapon::on_unload_chambered_round(void)` |
| 99.92 | `protected: bool __thiscall survarium::weapon_core_base_state::deserializing(void) const` |
| 99.92 | `public: void __thiscall survarium::dispersion_calculator::set_aiming_speed_coeff(float)` |
| 99.92 | `private: void __thiscall survarium::network_client::process_player_hit(class vostok::network_core::packet_reader &)` |
| 99.92 | `private: bool __thiscall vostok::animation::animation_player::set_target(class vostok::animation::mixing::expression const &, unsigned int, class boost::function<class vostok::math::float4x4 __cdecl (void const *)> const &)` |
| 99.92 | `private: bool __thiscall survarium::weapon_user_animations_selector::broken_legs_predicate(void) const` |
| 99.92 | `private: void __thiscall survarium::network_client::process_player_kill(class vostok::network_core::packet_reader &)` |
| 99.92 | `private: void __thiscall survarium::profile_player_character::on_player_ready(class vostok::resources::queries_result &, struct survarium::player_profile *)` |
| 99.92 | `private: virtual void __thiscall survarium::player::unsubscribe_animation_player(char const *, void const *)` |
| 99.92 | `private: virtual void __thiscall survarium::weapon::set_next_fire_queue_type(void)` |
| 99.92 | `private: void __thiscall survarium::network_client::on_trap_disarmed(class vostok::network_core::packet_reader &)` |
| 99.92 | `private: void __thiscall survarium::network_client::on_trap_fired(class vostok::network_core::packet_reader &)` |
| 99.92 | `private: void __thiscall survarium::network_client::on_trap_removed(class vostok::network_core::packet_reader &)` |
| 99.92 | `public: __thiscall vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>(class survarium::player *)` |
| 99.92 | `public: virtual void __thiscall survarium::base_player::insert_game_world_object(class survarium::game_world_object &)` |
| 99.92 | `public: void __thiscall survarium::weapon_core::set_skeleton(class vostok::resources::resource_ptr<class vostok::animation::skeleton, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 99.93 | `public: unsigned short __thiscall survarium::weapon_core::maximum_ammo_in_weapon(void) const` |
| 99.93 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon::on_foot_step(struct vostok::animation::animation_callback_params &)` |
| 99.93 | `private: void __thiscall survarium::player::apply_input(struct survarium::client_player_state &, class vostok::math::float2const &)` |
| 99.93 | `public: __thiscall vostok::animation::animation_player::~animation_player(void)` |
| 99.93 | `public: virtual void __thiscall survarium::base_player::remove_game_world_object(class survarium::game_world_object &)` |
| 99.93 | `public: void __thiscall survarium::weapon_core::set_ammunition(class vostok::resources::resource_ptr<class survarium::weapon_ammunition, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 99.93 | `private: void __thiscall survarium::weapon_core::load_ammo(void)` |
| 99.93 | `public: void __thiscall survarium::weapon_core::set_animation_callback(enum vostok::animation::reserved_channel_ids_enum, void const *, class boost::function<enum vostok::animation::callback_return_type_enum __cdecl (struct vostok::animation::animation_callback_params &)> const &)` |
| 99.93 | `protected: virtual void __thiscall survarium::weapon_core_aimed_state_base::initialize(void)` |
| 99.93 | `public: void __thiscall survarium::weapon_core::set_animation_callback(char const *, void const *, class boost::function<enum vostok::animation::callback_return_type_enum __cdecl (struct vostok::animation::animation_callback_params &)> const &)` |
| 99.94 | `private: void __thiscall survarium::damage_model::on_broken_limb_affect(char const *, enum survarium::hit_affects_type_enum, enum survarium::affect_event_type_enum)` |
| 99.94 | `public: bool __thiscall survarium::weapon_core::could_be_used(struct survarium::base_player const &) const` |
| 99.94 | `public: virtual __thiscall survarium::damage_model::~damage_model(void)` |
| 99.94 | `public: __thiscall vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 99.94 | `public: class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base> __thiscall survarium::base_network_client::get_current_player(void)` |
| 99.94 | `public: class vostok::resources::resource_ptr<class survarium::player, class vostok::resources::unmanaged_intrusive_base> __thiscall survarium::network_client::get_local_player(void)` |
| 99.94 | `public: float __thiscall survarium::animation_space_graph::max_speed(void) const` |
| 99.94 | `private: void __thiscall survarium::network_client::on_trap_placed(class vostok::network_core::packet_reader &)` |
| 99.94 | `protected: virtual void __thiscall survarium::weapon_core_chamber_a_round_aimed_state_base::finalize(void)` |
| 99.94 | `protected: virtual void __thiscall survarium::weapon_core_chamber_a_round_aimed_state_base::initialize(void)` |
| 99.94 | `private: void __thiscall survarium::network_client::process_player_respawn(class vostok::network_core::packet_reader &)` |
| 99.94 | `private: virtual void __thiscall survarium::player::take_inventory_item(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 99.94 | `protected: virtual void __thiscall survarium::weapon_core_aimed_state_base::finalize(void)` |
| 99.94 | `public: virtual class vostok::math::float3 __thiscall survarium::base_network_client::get_current_player_position(void) const` |
| 99.94 | `public: virtual void __thiscall survarium::network_client::unload(void)` |
| 99.95 | `public: void __thiscall survarium::weapon_core::unload_ammo(void)` |
| 99.95 | `public: void __thiscall survarium::base_network_client::detach_from_player(void)` |
| 99.95 | `private: void __thiscall survarium::player::apply_input_before_new_transform(struct survarium::client_player_state &, struct survarium::player_input const &, float)` |
| 99.95 | `private: void __thiscall survarium::network_client::process_affect_damage_model(class vostok::network_core::packet_reader &)` |
| 99.95 | `public: bool __thiscall vostok::animation::animation_player::set_target_and_tick(class vostok::animation::mixing::expression const &, unsigned int, class boost::function<class vostok::math::float4x4 __cdecl (void const *)> const &)` |
| 99.95 | `private: void __thiscall survarium::player_cook::on_hit_params_loaded(class vostok::resources::queries_result &, struct survarium::player_creation_params *)` |
| 99.95 | `private: virtual void __thiscall survarium::player::hit(struct survarium::hit_initiator const *const, unsigned int, char const *, float, float, class survarium::bullet *const)` |
| 99.95 | `public: void __thiscall survarium::player::apply_damage_model_affect(char const *, enum survarium::hit_affects_type_enum, enum survarium::affect_event_type_enum)` |
| 99.95 | `private: virtual void __thiscall survarium::player::crouch(void)` |
| 99.95 | `private: virtual void __thiscall survarium::player::stand_up(void)` |
| 99.95 | `private: virtual bool __thiscall survarium::player_logic_jump_state::is_ready_for_transition(void) const` |
| 99.95 | `private: void __thiscall survarium::game_world::clear_player_spawn_info(void)` |
| 99.95 | `private: void __thiscall survarium::player::select_animations(unsigned int)` |
| 99.95 | `private: struct survarium::player_input __thiscall survarium::player::local_input(void) const` |
| 99.95 | `private: void __thiscall survarium::player::smooth(float)` |
| 99.95 | `protected: void __thiscall survarium::weapon_core_cook::load_weapon_parameters(class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)` |
| 99.95 | `private: virtual void __thiscall survarium::weapon::on_after_fire(void)` |
| 99.96 | `public: void __thiscall survarium::player::apply_hit_directly(struct survarium::hit_info const &, unsigned int)` |
| 99.96 | `public: void __thiscall survarium::weapon_core::chamber_a_round(void)` |
| 99.96 | `private: void __thiscall survarium::player::render_crosshair_info(void)` |
| 99.96 | `public: virtual __thiscall survarium::base_network_client::~base_network_client(void)` |
| 99.96 | `public: void __thiscall vostok::animation::animation_player::deserialize_state(void *, unsigned int)` |
| 99.96 | `private: virtual float __thiscall survarium::player::get_speed(void) const` |
| 99.96 | `private: virtual void __thiscall survarium::player::on_before_active_object_changed(class vostok::resources::resource_ptr<class survarium::interactive_object, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class survarium::interactive_object, class vostok::resources::unmanaged_intrusive_base> const &) const` |
| 99.96 | `public: void __thiscall survarium::weapon_core::reset_fire_queue(void)` |
| 99.96 | `void __cdecl vostok::bind_pointer_to_buffer_mt_safe<class vostok::memory::doug_lea_mt_allocator, struct vostok::memory::inplace_constructor>(class vostok::memory::doug_lea_mt_allocator *&, char (&)[112], long volatile &, struct vostok::memory::inplace_constructor)` |
| 99.96 | `public: void __thiscall survarium::weapon_core::unload_chambered_round(void)` |
| 99.96 | `private: void __thiscall survarium::player::update_history_item(struct survarium::client_player_history_item &, struct survarium::client_player_history_item const *, struct survarium::server_player_update const &, unsigned int, class vostok::math::float4x4&, bool &)` |
| 99.96 | `public: virtual __thiscall survarium::network_client::~network_client(void)` |
| 99.96 | `public: virtual __thiscall survarium::base_player::~base_player(void)` |
| 99.97 | `private: void __thiscall survarium::player::process_quick_slots_for_current_player(void)` |
| 99.97 | `private: void __thiscall survarium::human_npc::tick_animation_player(unsigned int)` |
| 99.97 | `public: void __thiscall survarium::weapon_core::load_magazine(void)` |
| 99.97 | `private: void __thiscall survarium::network_client::on_world_sync_request(void)` |
| 99.97 | `private: float __thiscall survarium::weapon_core::computed_horizontal_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 99.97 | `private: float __thiscall survarium::weapon_core::computed_vertical_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 99.97 | `private: void __thiscall vostok::network::login_client::create_client(void)` |
| 99.97 | `protected: virtual void __thiscall survarium::weapon_core_reload_state_base::initialize(void)` |
| 99.97 | `private: virtual void __thiscall survarium::weapon_core::update_bones_matrices(class vostok::resources::resource_ptr<class vostok::animation::skeleton, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::float4x4*const, unsigned int, unsigned int, class vostok::math::float4x4&, class vostok::math::float4x4&, class vostok::animation::animation_player const &)` |
| 99.97 | `public: void __thiscall survarium::game_world_ui::update_minimap_local_player(void)` |
| 99.97 | `private: class vostok::animation::mixing::expression __thiscall survarium::weapon_core::get_weapon_and_hands_animation_expression(class vostok::mutable_buffer &, bool, enum survarium::weapon_user_state_enum, class vostok::animation::mixing::animation_lexeme &) const` |
| 99.97 | `public: virtual bool __thiscall survarium::weapon_core::is_ready_to_be_deactivated(void) const` |
| 99.97 | `public: virtual void __thiscall survarium::player_cook::delete_resource(class vostok::resources::resource_base *)` |
| 99.97 | `private: void __thiscall vostok::animation::animation_player::compact_callbacks(void)` |
| 99.97 | `private: void __thiscall survarium::animation_space_graph_cook::generate_graph_edges(class survarium::animation_space_graph *)` |
| 99.97 | `private: void __thiscall vostok::animation::animation_player::skip_time_if_needed(unsigned int)` |
| 99.97 | `private: void __thiscall survarium::player::update_history_item_from_previous(struct survarium::client_player_history_item const &, struct survarium::client_player_history_item &, class vostok::math::float4x4&)` |
| 99.97 | `private: void __thiscall survarium::network_client::on_players_ready(class vostok::resources::queries_result &, unsigned int)` |
| 99.97 | `private: virtual void __thiscall survarium::weapon::on_show(void)` |
| 99.97 | `private: void __thiscall survarium::player::detect_usable_objects(unsigned int)` |
| 99.97 | `private: float __thiscall survarium::weapon_core::computed_backward_recoil_time(float, float, unsigned int, unsigned int, unsigned int, float)` |
| 99.97 | `private: virtual void __thiscall survarium::player::hit(struct survarium::hit_initiator const *const, class vostok::collision::bone_collision_data const &, char const *, float, float, class survarium::bullet *const)` |
| 99.97 | `private: virtual void __thiscall survarium::weapon::on_skeleton_matrices_changed(unsigned int, class vostok::math::float4x4const &, class vostok::math::float4x4const *const, class vostok::math::float4x4const *const, class vostok::math::float4x4const &, class vostok::math::float4x4*const, class vostok::math::float4x4*const, class vostok::math::float4x4const &)` |
| 99.97 | `public: void __thiscall survarium::human_npc::set_transform(class vostok::math::float4x4const &)` |
| 99.97 | `private: virtual void __thiscall survarium::player::subscribe_animation_player(char const *, class boost::function<enum vostok::animation::callback_return_type_enum __cdecl (struct vostok::animation::animation_callback_params &)> const &, void const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, unsigned char, void const *const)` |
| 99.97 | `public: __thiscall vostok::network::login_client_impl::login_client_impl(class boost::asio::io_service &)` |
| 99.97 | `private: void __thiscall survarium::player_cook::on_subresources_loaded(class vostok::resources::queries_result &, struct survarium::player_creation_params *, struct survarium::inventory_cooker_data *, struct survarium::player_parameters_cooker_data *)` |
| 99.97 | `public: void __thiscall survarium::game_world_ui::update_minimap_players(void)` |
| 99.97 | `private: float __thiscall survarium::weapon_core::vertical_recoil_value(void) const` |
| 99.97 | `private: virtual void __thiscall survarium::player::subscribe_animation_player(enum vostok::animation::reserved_channel_ids_enum, class boost::function<enum vostok::animation::callback_return_type_enum __cdecl (struct vostok::animation::animation_callback_params &)> const &, void const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, void const *const)` |
| 99.98 | `private: float __thiscall survarium::weapon_core::horizontal_recoil_value(void) const` |
| 99.98 | `public: void __thiscall vostok::animation::animation_player::unsubscribe(char const *, void const *)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::sign_out_on_connected(enum vostok::connection_error_types_enum, class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &)` |
| 99.98 | `private: class vostok::math::float3 __thiscall survarium::weapon_core::get_dispersed_bullet_dir(void)` |
| 99.98 | `private: void __thiscall survarium::profile_character::character_animation_ready(class vostok::resources::queries_result &)` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::update_ui(unsigned int, unsigned int)` |
| 99.98 | `public: virtual void __thiscall survarium::animated_model_instance_cook::delete_resource(class vostok::resources::resource_base *)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::sign_in_on_connected(enum vostok::connection_error_types_enum, class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &)` |
| 99.98 | `private: virtual bool __thiscall survarium::player::set_new_active_item(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::on_player_killed(unsigned char, unsigned char, bool, unsigned int)` |
| 99.98 | `protected: virtual void __thiscall survarium::weapon_core_shotgun_reload_start_substate::initialize(void)` |
| 99.98 | `private: void __thiscall survarium::profile_character::weapon_resources_ready(class vostok::resources::queries_result &)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::on_sign_in_handshaked(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &, enum vostok::handshaking_error_types_enum)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::on_sign_out_handshaked(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &, enum vostok::handshaking_error_types_enum)` |
| 99.98 | `public: bool __thiscall vostok::animation::animation_player::set_target_and_tick(class vostok::animation::mixing::expression const &, unsigned int, class vostok::math::float4x4const &)` |
| 99.98 | `public: virtual void __thiscall survarium::lobby_menu::clear_resources(void)` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::set_victory_points(signed char, signed char)` |
| 99.98 | `private: virtual struct stlp_std::pair<class vostok::animation::mixing::expression, class vostok::animation::mixing::animation_lexeme> __thiscall survarium::player_logic_crouch_state::selected_animations(class vostok::mutable_buffer &, struct survarium::weapon_animation_parameters const &, bool) const` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::add_victory_points(signed char, signed char)` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::on_victory_item_put_take(unsigned char, bool, bool)` |
| 99.98 | `public: virtual void __thiscall survarium::network_client::tick(unsigned int, bool)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::on_sign_in_answer_received(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &, class boost::system::error_code const &, unsigned int)` |
| 99.98 | `private: void __thiscall survarium::network_client::on_connected_to_login(enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::sign_up_on_handshaked(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum, struct vostok::sign_up_info const &)> const &, struct vostok::sign_up_info const &, enum vostok::handshaking_error_types_enum)` |
| 99.98 | `private: void __thiscall vostok::network::login_client_impl::on_user_name_answer_received(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &, class boost::system::error_code const &, unsigned int)` |
| 99.98 | `public: void __thiscall survarium::game_world_ui::fill_quick_slots(void)` |
| 99.98 | `public: void __thiscall vostok::network::login_client_impl::sign_in(char const *, unsigned short, char const *, char const *, class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum)> const &)` |
| 99.99 | `private: virtual void __thiscall survarium::weapon::activate(struct survarium::base_player &, struct survarium::engine &)` |
| 99.99 | `public: void __thiscall vostok::input::receiver::keyboard::execute(void)` |
| 99.99 | `private: void __thiscall survarium::game_world_ui::update_quick_slot(enum survarium::profile_slot_enum)` |
| 99.99 | `private: void __thiscall survarium::network_client::process_sync_response(class vostok::network_core::packet_reader &)` |
| 99.99 | `protected: virtual enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_aimed_fire_state_base::on_shot_event(struct vostok::animation::animation_callback_params &)` |
| 99.99 | `protected: virtual enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_fire_state_base::on_shot_event(struct vostok::animation::animation_callback_params &)` |
| 99.99 | `private: void __thiscall survarium::network_client::on_http_error(class boost::system::error_code)` |
| 99.99 | `private: void __thiscall vostok::input::input_world::destroy_devices(void)` |
| 99.99 | `private: void __thiscall survarium::weapon::set_ui_ammo(bool)` |
| 99.99 | `private: void __thiscall survarium::damage_model_cook::on_hit_params_received(class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall survarium::human_npc::render_model(void)` |
| 99.99 | `private: enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core::on_animation_ik_interval(struct vostok::animation::animation_callback_params &)` |
| 99.99 | `public: void __thiscall vostok::input::receiver::keyboard::on_activate(void)` |
| 99.99 | `public: void __thiscall survarium::step_manager::on_step(class survarium::player const &, class vostok::math::float3const &, class vostok::math::float3const &, class survarium::game_world &) const` |
| 99.99 | `public: virtual void __thiscall survarium::player::deserialize(class vostok::network_core::packet_reader &)` |
| 99.99 | `private: void __thiscall survarium::network_client::process_initialize_victory_items(class vostok::network_core::packet_reader &)` |
| 99.99 | `private: void __thiscall vostok::network::login_client_impl::on_sign_up_account_answer_received(class boost::function<void __cdecl (enum vostok::connection_error_types_enum, enum vostok::handshaking_error_types_enum, enum vostok::socket_error_types_enum, enum vostok::login_server_message_types_enum, struct vostok::sign_up_info const &)> const &, struct vostok::sign_up_info const &, class boost::system::error_code const &, unsigned int)` |
| 99.99 | `public: void __thiscall survarium::weapon_core::get_ammo_info(struct survarium::weapon_ammo_info &)` |
| 99.99 | `public: __thiscall survarium::bullet::bullet(class survarium::bullet_manager &, class vostok::math::float3const &, class vostok::math::float3const &, unsigned int, float, class vostok::resources::resource_ptr<class survarium::weapon_ammunition, class vostok::resources::unmanaged_intrusive_base> const &, class survarium::weapon_core const &, struct survarium::hit_initiator const *const, struct survarium::hit_receiver const *const)` |
| 99.99 | `public: void __thiscall survarium::human_npc::enable(void)` |
| 99.99 | `survarium::calculate_model_size` |
| 99.99 | `public: void __thiscall survarium::inventory::setup_demo_profile(void)` |
- _...and 29 more_

### Added (108)

- `[thunk]: __thiscall vostok::sound::world::`vcall'{12, {flat}}`
- `private: bool __thiscall survarium::weapon_core::AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_fire_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_fire_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_fire_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_idle_AE_not_fire_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_idle_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::aimed_idle_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::auto_reload_AE_not_fire_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::auto_reload_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::can_reload(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_aimed_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_aimed_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_aimed_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_on_reload_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::chamber_a_round_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::fire_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::fire_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::fire_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::hide_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::hide_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::idle_AE_not_fire_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::idle_AE_or_reload_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::idle_transfer_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::inactive_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::is_aiming(void) const`
- `private: bool __thiscall survarium::weapon_core::is_aiming_and_will_not_break(void) const`
- `private: bool __thiscall survarium::weapon_core::is_trying_to_reload(void) const`
- `private: bool __thiscall survarium::weapon_core::not_inactive_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::reload_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::reload_pred(void) const`
- `private: bool __thiscall survarium::weapon_core_shotgun_reload_state::player_wants_to_fire_predicate(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_trying_to_jump(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_trying_to_sprint(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_weapon_allowing_to_jump(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_weapon_allowing_to_sprint(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::not_sprint_predicate(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::sprint_predicate(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::stand_from_crouch_predicate(void) const`
- `private: float __thiscall survarium::character_dispersion_calculator::get_skill_coef(enum survarium::weapon_user_state_enum, bool, bool) const`
- `private: virtual void * __thiscall survarium::medkit::`vector deleting destructor'(unsigned int)`
- `private: virtual void __thiscall survarium::weapon::on_fire_state_end(void)`
- `private: virtual void __thiscall survarium::weapon::on_fire_state_start(void)`
- `private: void __thiscall survarium::weapon::add_weapon_fire_light(void)`
- `private: void __thiscall survarium::weapon::remove_weapon_fire_light(void)`
- `private: void __thiscall survarium::weapon_core::check_for_fire_mode_or_ammunition_or_fire_queue_resetting(void)`
- `private: void __thiscall survarium::weapon_core::check_for_forcing_not_to_aim(void)`
- `private: void __thiscall survarium::weapon_core::check_for_no_ammo_message(void)`
- `private: void __thiscall survarium::weapon_core::check_for_sprint_transition(void)`
- `protected: __thiscall survarium::weapon_core_base_state::weapon_core_base_state(class survarium::weapon_core &, bool, enum survarium::weapon_state_id_enum)`
- `protected: void __thiscall survarium::swf_input_translator::register_char_bind(enum vostok::input::enum_keyboard, int, bool, bool)`
- `protected: void __thiscall survarium::swf_input_translator::register_char_bind(enum vostok::input::enum_keyboard, wchar_t, wchar_t, int, bool, bool)`
- `protected: wchar_t __thiscall survarium::swf_input_translator::translate_key_action(struct vostok::input::world *, bool, bool, struct survarium::dik_to_swf_bind &)`
- `public: __thiscall boost::_bi::storage3<class boost::_bi::value<class vostok::render::engine::world *>, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> >, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> > >::storage3<class boost::_bi::value<class vostok::render::engine::world *>, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> >, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> > >(struct boost::_bi::storage3<class boost::_bi::value<class vostok::render::engine::world *>, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> >, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> > > const &)`
- `public: __thiscall survarium::character_dispersion_skill_influence::character_dispersion_skill_influence(void)`
- `public: __thiscall survarium::game_scene::~game_scene(void)`
- `public: __thiscall vostok::ai::planning::plan_tracker::~plan_tracker(void)`
- `public: __thiscall vostok::detail::abstract_type_helper::abstract_type_helper(void)`
- `public: __thiscall vostok::intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>(class vostok::sound::encoded_sound_interface *)`
- `public: __thiscall vostok::render::geometry_batch::~geometry_batch(void)`
- `public: __thiscall vostok::render::requested_streamable_texture::requested_streamable_texture(struct vostok::render::requested_streamable_texture const &)`
- `public: __thiscall vostok::render::speedtree_data::speedtree_data(void)`
- `public: __thiscall vostok::render::streamable_texture_info::streamable_texture_info(struct vostok::render::streamable_texture_info const &)`
- `public: __thiscall vostok::render::streaming_ready_texture::streaming_ready_texture(struct vostok::render::streaming_ready_texture const &)`
- `public: __thiscall vostok::sound::single_sound::single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: bool __thiscall survarium::weapon_core::can_jump(void) const`
- `public: bool __thiscall survarium::weapon_core::can_sprint(void) const`
- `public: bool __thiscall survarium::weapon_core::is_chambering_a_round(void) const`
- `public: bool __thiscall survarium::weapon_core::is_firing(void) const`
- `public: bool __thiscall survarium::weapon_core::is_idle(void) const`
- `public: bool __thiscall survarium::weapon_core::is_reloading(void) const`
- `public: bool __thiscall survarium::weapon_core::ready_to_fire(void) const`
- `public: bool __thiscall survarium::weapon_core::tick_in_cycle_fire(bool) const`
- `public: bool __thiscall survarium::weapon_user_animations_selector::is_crouching(void) const`
- `public: bool __thiscall survarium::weapon_user_animations_selector::is_going_to_jump(void) const`
- `public: bool __thiscall survarium::weapon_user_animations_selector::is_going_to_sprint(void) const`
- `public: struct vostok::render::streaming_ready_texture & __thiscall vostok::render::streaming_ready_texture::operator=(struct vostok::render::streaming_ready_texture const &)`
- `public: virtual __thiscall survarium::animated_model_instance::~animated_model_instance(void)`
- `public: virtual __thiscall survarium::player_logic_sprint_state::~player_logic_sprint_state(void)`
- `public: virtual __thiscall vostok::ai::selectors::enemy_target_selector::~enemy_target_selector(void)`
- `public: virtual __thiscall vostok::console_commands::cc_u32::~cc_u32(void)`
- `public: virtual bool __thiscall vostok::input::receiver::keyboard::caps_lock_state(void) const`
- `public: virtual bool __thiscall vostok::input::receiver::keyboard::get_scan_unicode(int, wchar_t *, unsigned int) const`
- `public: virtual void * __thiscall btCollisionWorld::ContactResultCallback::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall btCollisionWorld::RayResultCallback::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall stlp_std::runtime_error::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::animated_model_instance::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::collision_geometry::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::jump_logic_base_state::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::ladder_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::player_logic_sprint_state::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::ai::selectors::enemy_target_selector::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::detail::concrete_type_helper<unsigned char>::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::memory::writer::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::memory::writer_base::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::particle::particle_system_wrapper_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::grass_world::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage_light_propagation_volumes::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage_translucency::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::static_render_surface::`vector deleting destructor'(unsigned int)`
- `public: virtual void __thiscall survarium::base_player::on_fire(void)`
- `public: void __thiscall survarium::character_dispersion_calculator::set_character_dispersion_skill_influence(struct survarium::character_dispersion_skill_influence const *)`
- `public: void __thiscall survarium::character_dispersion_skill_influence::load(class vostok::configs::binary_config_value const &)`
- `public: void __thiscall survarium::damage_model::reset(unsigned int)`
- `public: void __thiscall survarium::weapon_user_animations_selector::on_sprint_start(void)`
- `vostok::render::index_to_shadow_size`

### Deleted (78)

- `[thunk]: __thiscall survarium::weapon_core::`vcall'{196, {flat}}`
- `[thunk]: __thiscall survarium::weapon_core_cook::`vcall'{36, {flat}}`
- `[thunk]: public: virtual struct vostok::ui::window * __thiscall vostok::ui::ui_text_edit::w(void)`
- `[thunk]: public: virtual void * __thiscall vostok::ui::ui_text<struct vostok::ui::dynamic_text>::`vector deleting destructor'(unsigned int)`
- `[thunk]: public: virtual void * __thiscall vostok::ui::ui_text_edit::`vector deleting destructor'(unsigned int)`
- ``vostok::sound::sound_world::register_sound_cooks'::`2'::`dynamic atexit destructor for 's_sound_rms_cook''`
- `class vostok::resources::managed_resource * __cdecl vostok::resources::allocate_managed_resource(unsigned int, enum vostok::resources::class_id_enum)`
- `private: bool __thiscall survarium::weapon_core::can_and_must_reload_and_animation_ended_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::can_and_must_reload_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::instant_idle_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::is_not_trying_to_aim_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::is_trying_to_aim(void) const`
- `private: bool __thiscall survarium::weapon_core::must_chamber_a_round_aimed_and_animation_ended_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::must_chamber_a_round_aimed_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::must_chamber_a_round_and_animation_ended_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::must_chamber_a_round_predicate(void) const`
- `private: bool __thiscall survarium::weapon_core::target_and_animation_ended_predicate(enum survarium::weapon_targets) const`
- `private: bool __thiscall survarium::weapon_core::target_predicate(enum survarium::weapon_targets) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_weapon_firing(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_weapon_in_idle(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::is_weapon_toggling(void) const`
- `private: bool __thiscall survarium::weapon_user_animations_selector::stand_predicate(void) const`
- `private: virtual void __thiscall survarium::weapon::set_target(enum survarium::weapon_targets)`
- `private: void __thiscall vostok::sound::sound_rms_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `protected: __thiscall survarium::weapon_core_base_state::weapon_core_base_state(class survarium::weapon_core &, bool)`
- `protected: __thiscall vostok::resources::pinned_ptr_base<class vostok::sound::sound_rms>::pinned_ptr_base<class vostok::sound::sound_rms>(class vostok::resources::pinned_ptr_base<class vostok::sound::sound_rms> const &)`
- `protected: __thiscall vostok::resources::pinned_ptr_base<class vostok::sound::sound_rms>::pinned_ptr_base<class vostok::sound::sound_rms>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `protected: class vostok::resources::pinned_ptr_mutable<class vostok::sound::sound_rms> __thiscall vostok::resources::cook_base::pin_for_write<class vostok::sound::sound_rms>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `protected: virtual enum vostok::animation::callback_return_type_enum __thiscall survarium::weapon_core_aimed_fire_state_base::on_aiming_event(struct vostok::animation::animation_callback_params &)`
- `protected: void __thiscall survarium::swf_input_translator::register_char_bind(enum vostok::input::enum_keyboard, int, bool)`
- `protected: void __thiscall survarium::swf_input_translator::register_char_bind(enum vostok::input::enum_keyboard, wchar_t, wchar_t, int, bool)`
- `protected: wchar_t __thiscall survarium::swf_input_translator::translate_key_action(struct vostok::input::world *, bool, struct survarium::dik_to_swf_bind &)`
- `public: __thiscall vostok::particle::lod_entry::~lod_entry(void)`
- `public: __thiscall vostok::resources::pinned_ptr_base<class vostok::sound::sound_rms>::~pinned_ptr_base<class vostok::sound::sound_rms>(void)`
- `public: __thiscall vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base>(class vostok::sound::encoded_sound_with_qualities *)`
- `public: __thiscall vostok::sound::single_sound::single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall vostok::sound::sound_rms::sound_rms(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float)`
- `public: __thiscall vostok::sound::sound_rms::~sound_rms(void)`
- `public: __thiscall vostok::sound::sound_rms_cook::sound_rms_cook(void)`
- `public: __thiscall vostok::sound::sound_rms_pinned::sound_rms_pinned(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `public: bool __thiscall survarium::weapon_core::could_be_aimed(struct survarium::base_player const &) const`
- `public: bool __thiscall survarium::weapon_core::is_ready_to_shoot(void) const`
- `public: bool __thiscall survarium::weapon_core::ready_to_reload(void) const`
- `public: bool __thiscall survarium::weapon_user_animations_selector::sprint_predicate(void) const`
- `public: class survarium::weapon_user_animations_selector & __thiscall survarium::weapon_core::user_animations_selector(void)`
- `public: enum survarium::weapon_targets __thiscall survarium::weapon_core::get_target(void) const`
- `public: float __thiscall vostok::sound::sound_rms::get_rms_by_time(unsigned __int64) const`
- `public: unsigned __int64 __thiscall vostok::sound::sound_rms::find_min_value_time_in_interval(unsigned __int64, unsigned __int64, float) const`
- `public: virtual __thiscall survarium::rifle_scope::~rifle_scope(void)`
- `public: virtual __thiscall survarium::weapon_core_fire_state_base::~weapon_core_fire_state_base(void)`
- `public: virtual __thiscall vostok::particle::particle_system_instance::~particle_system_instance(void)`
- `public: virtual __thiscall vostok::sound::sound_rms_cook::~sound_rms_cook(void)`
- `public: virtual class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const & __thiscall vostok::sound::composite_sound::get_sound_rms(void) const`
- `public: virtual class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const & __thiscall vostok::sound::single_sound::get_sound_rms(void) const`
- `public: virtual void * __thiscall Scaleform::Render::MappedTextureBase::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall btClosestNotMeConvexResultCallback::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::collision_sensor::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::free_fly_camera::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::game_options::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::rifle_scope::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::usable_object::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::victory_item::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::weapon_core_shotgun_reload_state::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::animation::animation_collection::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::core::engine::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::memory::managed_node_owner::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::particle::particle_system_instance_impl::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage_forward::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::sound::sound_rms_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void __thiscall survarium::weapon_core::set_target(enum survarium::weapon_targets)`
- `public: virtual void __thiscall vostok::sound::sound_rms_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::sound_rms_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: void __thiscall survarium::damage_model::reset(void)`
- `public: void __thiscall survarium::weapon_core::instant_idle_end(void)`
- `public: void __thiscall survarium::weapon_core::instant_toggle_end(void)`
- `public: void __thiscall survarium::weapon_core::instant_toggle_start(void)`
- `void __cdecl vostok::memory::zero<char, 14>(char (&)[14])`
- `vostok::sound::`dynamic initializer for 's_discr_frequency''`

---

## v0.1.1a-build816 → v0.1.1b-build826
_2013-05-14 → 2013-05-14 · +36 / -49 / ~298_

### Changed (298)

| match % | function |
| ---: | --- |
| 0.00 | `[thunk]: __thiscall vostok::engine_user::world::`vcall'{20, {flat}}` |
| 0.00 | `[thunk]: __thiscall vostok::network::world::`vcall'{0, {flat}}` |
| 0.00 | `[thunk]: __thiscall vostok::sound::world::`vcall'{12, {flat}}` |
| 0.00 | `[thunk]: private: virtual char const * __thiscall vostok::engine::engine_world::get_resources_path(void) const` |
| 0.00 | `[thunk]: private: virtual void __thiscall vostok::engine::engine_world::enter_editor_mode(void)` |
| 0.00 | `[thunk]: public: virtual int __thiscall vostok::engine::engine_world::get_exit_code(void) const` |
| 0.00 | `[thunk]: public: virtual void * __thiscall survarium::ladder::`vector deleting destructor'(unsigned int)` |
| 0.00 | `[thunk]: public: virtual void * __thiscall vostok::engine::engine_world::`vector deleting destructor'(unsigned int)` |
| 0.00 | `[thunk]: public: virtual void __thiscall vostok::engine::engine_world::exit(int)` |
| 0.00 | `[thunk]: public: virtual void __thiscall vostok::engine::engine_world::set_exit_code(int)` |
| 0.00 | `empty_stub` |
| 0.00 | `long __cdecl vostok::threading::interlocked_increment(long volatile &)` |
| 0.00 | `private: void __thiscall vostok::render::stage_lights::draw_geometry(class vostok::render::light *)` |
| 0.00 | `public: __thiscall survarium::game_scene::~game_scene(void)` |
| 0.00 | `public: __thiscall vostok::ai::brain_unit_cook_params::~brain_unit_cook_params(void)` |
| 0.00 | `public: __thiscall vostok::animation::mixing::animation_interval::~animation_interval(void)` |
| 0.00 | `public: __thiscall vostok::intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::~intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>(void)` |
| 0.00 | `public: __thiscall vostok::one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >::~one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >(void)` |
| 0.00 | `public: __thiscall vostok::render::skeleton_combined_cook_data::~skeleton_combined_cook_data(void)` |
| 0.00 | `public: __thiscall vostok::render::stage_lights::lights_instance::lights_instance(void)` |
| 0.00 | `public: __thiscall vostok::render::sun_cascade::sun_cascade(struct vostok::render::sun_cascade const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::vfs::vfs_mount::~vfs_mount(void)` |
| 0.00 | `public: bool __thiscall boost::function_base::empty(void) const` |
| 0.00 | `public: virtual __thiscall survarium::inventory_cook::~inventory_cook(void)` |
| 0.00 | `public: virtual __thiscall vostok::console_commands::cc_u32::~cc_u32(void)` |
| 0.00 | `public: virtual __thiscall vostok::render::functor_command::~functor_command(void)` |
| 0.00 | `public: virtual bool __thiscall Scaleform::MemoryFile::Flush(void)` |
| 0.00 | `public: virtual void * __thiscall survarium::collision_geometry::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::console_command_bind::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::damage_protector::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::empty_hands::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::flash_external_handler::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::inventory_cook::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::lobby_camera::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::lobby_menu::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::player_cook::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::brain_unit::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::planning::operator_base::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::animation::mixing::addition_lexeme::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::collision::aabb_object::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::collision::box_geometry_instance::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::detail::abstract_type_helper::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::detail::concrete_type_helper<unsigned short>::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::memory::writer::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::memory::writer_base::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::physics::animated_model_instance::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::base_scene::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::effect_sun::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::functor_command::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::grass_world::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::render_surface::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::sound::sound_spl_cook::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void __thiscall survarium::game_camera::on_focus(bool)` |
| 0.00 | `public: void __thiscall vostok::render::backend::set_ps_constant<unsigned int>(class vostok::render::shader_constant_host const *, unsigned int const &)` |
| 0.00 | `vec_begin` |
| 0.00 | `vostok::animation::`dynamic initializer for 'zero''` |
| 6.08 | `public: class survarium::victory_items_container_core * __thiscall survarium::simple_game_project::get_items_container(unsigned char)` |
| 9.96 | `private: void __thiscall survarium::game::register_console_commands(void)` |
| 12.00 | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 16.09 | `private: void __thiscall vostok::render::constants_handler<1>::update_buffers(void)` |
| 23.90 | `public: void __thiscall vostok::render::shader_constant_buffer::update(void)` |
| 24.99 | `private: void __thiscall vostok::render::stage_lights::render_particle_lighting(class vostok::render::render_particle_emitter_instance *, class vostok::render::light *, unsigned int)` |
| 28.38 | `public: void __thiscall vostok::render::radiance_volume::inject_camera_occluders(class vostok::render::renderer_context *)` |
| 29.48 | `private: void __thiscall vostok::render::stage_lights::render_model_lighting(struct vostok::render::render_surface_instance *, class vostok::render::light *)` |
| 34.20 | `private: void __thiscall vostok::render::stage_lights::render_speedtree_lighting(struct vostok::render::lod_entry const *, class SpeedTree::CInstance const *, struct SpeedTree::SInstanceLod const *, class vostok::render::speedtree_tree_component *, class vostok::render::light *)` |
| 34.68 | `public: void __thiscall vostok::render::grass_world::set_trample_parameters(struct vostok::render::trample_desc &)` |
| 35.79 | `public: void __thiscall vostok::render::system_renderer::draw_triangles(struct vostok::render::vertex_colored const *const, struct vostok::render::vertex_colored const *const, unsigned short const *const, unsigned short const *const, bool)` |
| 37.90 | `private: bool __thiscall survarium::weapon_core::chamber_a_round_on_reload_break_pred(void) const` |
| 38.32 | `public: void __thiscall vostok::render::radiance_volume::propagate_lighting_iter(unsigned int, unsigned int)` |
| 40.29 | `private: void __thiscall vostok::render::stage_lights::render_light(class vostok::render::light *, bool)` |
| 42.34 | `public: virtual void __thiscall vostok::render::skeleton_render_model_instance::set_constants(void)` |
| 42.73 | `public: virtual void __thiscall vostok::render::stage_ambient_lighting::execute(void)` |
| 45.14 | `public: void __thiscall vostok::render::scene_shader_constants::set(class vostok::render::renderer_context *, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::math::float3const &, float, float, float, class vostok::math::float4const &, struct vostok::render::post_process_parameters const &)` |
| 46.13 | `public: void __thiscall vostok::render::decal_shader_constants_and_geometry::set(class vostok::render::renderer_context *, class vostok::math::float4x4const &, class vostok::math::float4x4const &, float, float, class vostok::math::float3const &, class vostok::math::float4x4const &)` |
| 50.52 | `public: void __thiscall vostok::render::renderer_context::set_v(class vostok::math::float4x4const &)` |
| 50.89 | `public: void __thiscall vostok::render::particle_shader_constants::set_time(float)` |
| 52.50 | `public: void __thiscall vostok::render::renderer_context::set_w(class vostok::math::float4x4const &)` |
| 52.83 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::set_rsm_contants(class vostok::math::float3const &, class vostok::math::float3const &, float)` |
| 52.95 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::pre_lpv_batch_render(class vostok::math::float3const &, float, struct vostok::render::geometry_batch const &)` |
| 53.18 | `private: void __thiscall vostok::render::stage_lights::make_skin_scattering_texture(struct vostok::render::render_surface_instance *, class vostok::render::light *)` |
| 54.07 | `public: void __thiscall vostok::render::dof_shader_constants::set(class vostok::math::float3const &, float, float, float, float, float, float, float)` |
| 54.67 | `public: void __thiscall vostok::render::grass_world::set_shadow_parameters(unsigned int)` |
| 54.76 | `private: bool __thiscall survarium::weapon_core::idle_AE_or_reload_break_pred(void) const` |
| 54.79 | `public: void __thiscall vostok::render::particle_shader_constants::set(class vostok::math::float3, class vostok::math::float3, class vostok::math::float3, enum vostok::particle::enum_particle_locked_axis, enum vostok::particle::enum_particle_screen_alignment)` |
| 54.97 | `public: void __thiscall vostok::render::speedtree_tree_parameters::set(class vostok::render::speedtree_tree_component *, class SpeedTree::CInstance const *, struct SpeedTree::SInstanceLod const *)` |
| 56.58 | `public: virtual void __thiscall vostok::render::stage_atmosphere::execute(void)` |
| 58.30 | `public: void __thiscall vostok::render::speedtree_wind_parameters::set(class SpeedTree::CWind const &)` |
| 58.72 | `public: void __thiscall vostok::render::renderer_context::set_p(class vostok::math::float4x4const &)` |
| 60.67 | `public: void __thiscall vostok::render::grass_world::set_wind_parameters(class vostok::math::float2const &, float)` |
| 60.74 | `public: void __thiscall vostok::render::radiance_volume::inject_lighting(class vostok::math::float3const &, class vostok::math::float3const &, float, unsigned int)` |
| 61.40 | `public: void __thiscall vostok::render::bloom_shader_constants::set(float, float, class vostok::math::float3const &)` |
| 62.14 | `public: void __thiscall vostok::render::speedtree_billboard_parameters::set(class vostok::render::renderer_context *, class vostok::render::speedtree_tree_component *)` |
| 62.23 | `public: void __thiscall vostok::render::grass_world::set_patch_parameters(struct vostok::render::grass_patch *)` |
| 63.25 | `private: void __thiscall vostok::render::stage_lights::render_shadowed_light(class vostok::render::light *)` |
| 63.42 | `public: virtual void __thiscall vostok::render::stage_sun::execute(void)` |
| 63.79 | `public: void __thiscall vostok::render::speedtree_common_parameters::set(class vostok::render::renderer_context *, class vostok::render::speedtree_tree_component *, class vostok::math::float3const &)` |
| 64.79 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::inject_occluders(unsigned int, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::render::vector<class vostok::math::float4x4>)` |
| 65.41 | `public: void __thiscall vostok::render::stage_forward::render_forward_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, unsigned int)` |
| 65.65 | `private: void __thiscall vostok::render::stage_gbuffer::render_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, unsigned int, unsigned int &, bool)` |
| 67.38 | `public: void __thiscall vostok::render::radiance_volume::inject_occluder_geometry(class vostok::render::renderer_context *, class vostok::math::float3const &, class vostok::math::float3const &, class vostok::render::vector<class vostok::math::float4x4> const &)` |
| 67.63 | `private: void __thiscall vostok::render::stage_lights::render_to_hw_shadowmap(class vostok::render::light *, unsigned int, float, unsigned int, unsigned int, class vostok::math::float4x4const &, class vostok::math::float4x4const &, unsigned int)` |
| 68.51 | `public: void __thiscall vostok::render::radiance_volume::inject_occluders(class vostok::render::renderer_context *, class vostok::math::float3const &, class vostok::math::float3const &, unsigned int)` |
| 70.45 | `public: void __thiscall vostok::render::radiance_volume::propagate_lighting(unsigned int)` |
| 71.01 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_rms(class vostok::math::float3const &, float, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::render::vector<class vostok::math::float4x4>, unsigned int)` |
| 72.87 | `public: void __thiscall vostok::render::stage_forward::accumulate_local_reflections(void)` |
| 73.75 | `private: void __thiscall vostok::render::constants_handler<0>::assign(class vostok::render::shader_constant_table const *)` |
| 73.75 | `private: void __thiscall vostok::render::constants_handler<1>::assign(class vostok::render::shader_constant_table const *)` |
| 73.75 | `private: void __thiscall vostok::render::constants_handler<2>::assign(class vostok::render::shader_constant_table const *)` |
| 75.84 | `public: virtual void __thiscall vostok::render::stage_volume_fog::execute(void)` |
| 75.97 | `public: void __thiscall vostok::render::stage_debug::render_environment_probe_preview(void)` |
| 76.85 | `public: virtual void __thiscall vostok::render::stage_translucency::execute(void)` |
| 77.12 | `public: void __thiscall vostok::render::hw_hiz_occlusion_manager::render_debug(class vostok::render::renderer_context *, class vostok::math::float4const *, unsigned char const *, unsigned int)` |
| 77.15 | `public: virtual void __thiscall vostok::render::stage_postprocess::execute(void)` |
| 77.46 | `public: __thiscall vostok::render::backend::~backend(void)` |
| 78.55 | `public: virtual void __thiscall vostok::render::stage_clouds::execute(void)` |
| 78.86 | `public: void __thiscall vostok::render::grass_patch::try_accumulate_trample(struct vostok::render::trample_desc &, struct vostok::render::grass_world *, class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 79.55 | `private: void __thiscall vostok::render::stage_lights::render_model_probe_lighting(struct vostok::render::render_surface_instance *, struct vostok::render::environment_probe *, float)` |
| 80.43 | `private: bool __thiscall survarium::weapon_core::chamber_a_round_aimed_transfer_pred(void) const` |
| 80.43 | `private: bool __thiscall survarium::weapon_core::chamber_a_round_transfer_pred(void) const` |
| 81.02 | `public: void __thiscall vostok::render::res_render_output::set_size(unsigned int, unsigned int, bool, bool)` |
| 81.40 | `public: void __thiscall vostok::render::render_particle_emitter_instance::render_sprites(void)` |
| 81.49 | `private: bool __thiscall survarium::weapon_core::chamber_a_round_pred(void) const` |
| 81.59 | `public: void __thiscall vostok::render::stage_shadow_direct::render_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, class vostok::math::float4x4const &, unsigned int, unsigned int, class vostok::math::float3const &, unsigned int, unsigned int)` |
| 81.84 | `public: virtual void __thiscall vostok::render::stage_gbuffer::execute(void)` |
| 82.64 | `private: void __thiscall vostok::render::speedtree_billboard_parameters::set_billboard_tangents(float)` |
| 82.88 | `private: void __thiscall vostok::render::stage_lights::render_particle_probe_lighting(class vostok::render::render_particle_emitter_instance *, struct vostok::render::environment_probe *, unsigned int)` |
| 83.31 | `private: void __thiscall vostok::render::hw_hiz_occlusion_manager::render_model_bounds(class vostok::render::renderer_context *, class vostok::math::float4const *, unsigned int)` |
| 83.37 | `public: void __thiscall vostok::render::stage_light_propagation_volumes::execute_smoothed_impl(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int)` |
| 83.37 | `public: void __thiscall vostok::render::system_renderer::draw_screen_lines(class vostok::math::float3const *, unsigned int, class vostok::math::color const &, float, unsigned int, bool, bool)` |
| 83.50 | `private: void __thiscall vostok::render::stage_postprocess::compute_per_pixel_eye_adaptated_luminance(void)` |
| 84.11 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_rms_smoothed2(class vostok::math::float3const &, float, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::render::vector<class vostok::math::float4x4>, unsigned int, unsigned int, unsigned int)` |
| 84.22 | `public: void __thiscall vostok::render::stage_resolve_lighting::render_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, unsigned int &)` |
| 85.31 | `private: void __thiscall survarium::network_client::process_victory_item_take_or_put(class vostok::network_core::packet_reader &)` |
| 86.00 | `public: virtual void __thiscall vostok::render::stage_postprocess::execute_disabled(void)` |
| 86.40 | `private: void __thiscall vostok::render::hw_hiz_occlusion_manager::downsample_occlusion_buffer(void)` |
| 86.45 | `private: class vostok::math::float4x4 __thiscall vostok::render::stage_pre_rain::render_rain_shadow_map(void)` |
| 86.63 | `private: void __thiscall vostok::render::stage_postprocess::accumulate_motion_vectors(void)` |
| 86.88 | `survarium::`dynamic initializer for 's_recoil_back_eanble_cc''` |
| 86.88 | `survarium::`dynamic initializer for 's_recoil_enable_cc''` |
| 86.88 | `survarium::`dynamic initializer for 's_recoil_horizontal_eanble_cc''` |
| 86.88 | `survarium::`dynamic initializer for 's_recoil_vertical_eanble_cc''` |
| 87.18 | `private: void __thiscall vostok::render::stage_postprocess::advanced_bloom(void)` |
| 87.19 | `public: virtual void __thiscall survarium::respawn_point_core::load(class vostok::configs::binary_config_value const &)` |
| 87.66 | `public: __thiscall vostok::render::render_cc_bool::render_cc_bool(char const *, enum vostok::render::enum_options_changes_result, char const *, bool &, bool &, bool, enum vostok::console_commands::command_type)` |
| 87.75 | `protected: __thiscall vostok::render::shader_constant_buffer::shader_constant_buffer(class vostok::fixed_string<64> const &, enum vostok::render::enum_shader_type, enum _D3D_CBUFFER_TYPE, unsigned int)` |
| 88.19 | `public: virtual void __thiscall vostok::render::stage_rain::execute(void)` |
| 89.67 | `private: bool __thiscall survarium::weapon_core::is_aiming(void) const` |
| 89.74 | `public: void __thiscall vostok::render::stage_light_propagation_volumes::execute_impl(void)` |
| 91.14 | `private: void __thiscall vostok::render::stage_postprocess::process_blur(class vostok::render::render_target *, class vostok::render::res_texture *, class vostok::render::render_target *, class vostok::render::res_texture *, unsigned int)` |
| 91.44 | `public: void __thiscall vostok::render::render_particle_emitter_instance::render_subuv_sprites(void)` |
| 91.98 | `public: __thiscall vostok::render::backend::backend(void)` |
| 92.65 | `public: void __thiscall vostok::render::render_output_window::set_size(unsigned int, unsigned int, bool, bool)` |
| 92.76 | `bool __cdecl vostok::render::set_client_rect(struct HWND__*, int, int, int, int)` |
| 92.82 | `private: void __thiscall survarium::network_client::process_initialize_victory_items(class vostok::network_core::packet_reader &)` |
| 93.01 | `public: virtual void __thiscall vostok::render::stage_ambient_occlusion::execute(void)` |
| 93.10 | `private: void __thiscall vostok::render::options::load_impl(class vostok::memory::reader &)` |
| 93.20 | `public: void __thiscall vostok::render::options::set_default_values(void)` |
| 93.63 | `public: virtual void __thiscall vostok::render::effect_god_rays::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 93.70 | `private: bool __thiscall survarium::weapon_core::can_reload(void) const` |
| 94.46 | `public: void __thiscall vostok::render::options::register_console_commands(void)` |
| 94.49 | `public: virtual void __thiscall vostok::render::stage_pre_rain::execute(void)` |
| 94.54 | `private: void __thiscall vostok::render::decal_instance::render(class vostok::render::renderer_context *, enum vostok::render::enum_render_stage_type)` |
| 95.31 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::downsample_rsm(class vostok::math::float3const &, class vostok::math::float3const &, float, unsigned int)` |
| 96.14 | `public: virtual bool __thiscall survarium::free_fly_camera::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 96.58 | `private: virtual bool __thiscall survarium::player_input_handler::on_keyboard_action(struct vostok::input::world *, enum vostok::input::enum_keyboard, enum vostok::input::enum_keyboard_action)` |
| 97.56 | `public: virtual void __thiscall vostok::render::stage_resolve_lighting::execute(void)` |
| 97.61 | `public: void __thiscall vostok::render::grass_world::accumulate_trample(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 98.49 | `private: void __thiscall vostok::render::shader_macros::register_available_macros(void)` |
| 98.88 | `private: void __thiscall survarium::game::on_configs_loaded(class vostok::resources::queries_result &)` |
| 98.92 | `private: bool __thiscall vostok::console_impl::on_text_commit(struct vostok::ui::window *, int, int)` |
| 99.33 | `public: void __thiscall vostok::render::backend::reset_depth_stencil_target(void)` |
| 99.50 | `public: void __thiscall vostok::render::backend::set_vb(class vostok::render::untyped_buffer *, unsigned int, unsigned int)` |
| 99.50 | `public: void __thiscall vostok::render::backend::set_vb_stream_1(class vostok::render::untyped_buffer *, unsigned int, unsigned int)` |
| 99.50 | `public: void __thiscall vostok::render::res_state::apply(void) const` |
| 99.54 | `private: void __thiscall survarium::player_input_handler::process_first_person_mode(bool)` |
| 99.56 | `public: void __thiscall vostok::render::res_geometry::apply(void)` |
| 99.57 | `private: void __thiscall vostok::render::backend::flush_rt(void)` |
| 99.57 | `public: virtual void __thiscall vostok::render::stage_debug::execute(void)` |
| 99.58 | `public: void __thiscall vostok::render::backend::reset(void)` |
| 99.62 | `public: void __thiscall vostok::render::grass_patch::remove_trample(void)` |
| 99.64 | `public: void __thiscall vostok::render::hw_hiz_point_list::render(unsigned int)` |
| 99.66 | `public: void __thiscall vostok::render::injection_geometry::draw(void)` |
| 99.67 | `public: void __thiscall vostok::render::backend::set_render_target(enum vostok::render::enum_render_target_enum, class vostok::render::render_target const *)` |
| 99.67 | `vostok::math::`dynamic initializer for 'SNaN''` |
| 99.68 | `public: void __thiscall vostok::render::radiance_volume::prepare_gv(void)` |
| 99.69 | `public: void __thiscall vostok::render::res_xs<struct vostok::render::vs_data>::apply(void) const` |
| 99.69 | `public: void __thiscall vostok::render::backend::set_render_targets(class vostok::render::render_target const *, class vostok::render::render_target const *, class vostok::render::render_target const *, class vostok::render::render_target const *)` |
| 99.70 | `public: void __thiscall vostok::render::backend::on_device_destroy(void)` |
| 99.70 | `public: void __thiscall vostok::render::backend::reset_render_targets(bool)` |
| 99.71 | `public: void __thiscall vostok::render::box_geometry::draw(void)` |
| 99.71 | `public: void __thiscall vostok::render::sky_dome_geometry::draw(void)` |
| 99.71 | `public: void __thiscall vostok::render::sphere_geometry::draw(void)` |
| 99.72 | `public: void __thiscall vostok::render::res_xs<struct vostok::render::ps_data>::apply(void) const` |
| 99.72 | `public: void __thiscall vostok::render::sliced_cube_geometry::draw(void)` |
| 99.72 | `public: virtual void __thiscall vostok::render::stage_lights::execute(void)` |
| 99.72 | `private: void __thiscall vostok::render::stage_postprocess::clear_surface(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)` |
| 99.73 | `private: void __thiscall vostok::render::backend::update_input_layout(void)` |
| 99.74 | `public: virtual void __thiscall vostok::render::stage_forward::execute(void)` |
| 99.75 | `public: void __thiscall vostok::render::res_xs<struct vostok::render::gs_data>::apply(void) const` |
| 99.76 | `private: virtual void __thiscall vostok::render::stage_light_propagation_volumes::execute_disabled(void)` |
| 99.78 | `public: void __thiscall vostok::render::backend::set_ps_texture(char const *, class vostok::render::res_texture *)` |
| 99.78 | `public: void __thiscall vostok::render::backend::flush(void)` |
| 99.79 | `public: virtual void __thiscall vostok::render::stage_decals_accumulate::execute_disabled(void)` |
| 99.80 | `public: virtual void __thiscall vostok::render::stage_shadow_direct::execute_disabled(void)` |
| 99.81 | `public: void __thiscall vostok::render::backend::set_render_output(class vostok::render::res_render_output const *)` |
| 99.81 | `private: void __thiscall vostok::render::radiance_volume::end_render_to_cells(void)` |
| 99.82 | `public: virtual void __thiscall vostok::render::stage_ambient_occlusion::execute_disabled(void)` |
| 99.84 | `public: void __thiscall vostok::render::backend::render(enum D3D_PRIMITIVE_TOPOLOGY, unsigned int, unsigned int)` |
| 99.84 | `public: virtual void __thiscall vostok::render::stage_lights::execute_disabled(void)` |
| 99.85 | `public: virtual void __thiscall vostok::render::stage_pre_lighting::execute(void)` |
| 99.85 | `public: void __thiscall vostok::render::stage_forward::render_opaque_models(void)` |
| 99.86 | `private: void __thiscall vostok::render::hw_hiz_occlusion_manager::render_occluders(class vostok::render::renderer_context *)` |
| 99.86 | `public: virtual void __thiscall vostok::render::stage_shadow_direct::execute(void)` |
| 99.87 | `public: void __thiscall vostok::render::engine::world::begin_render_options_changing(long volatile *)` |
| 99.87 | `public: void __thiscall vostok::render::statistics::start(void)` |
| 99.88 | `private: void __thiscall vostok::render::stage_lights::fill_surface(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)` |
| 99.88 | `public: void __thiscall vostok::render::fog_box_geometry::render(void)` |
| 99.88 | `public: void __thiscall vostok::render::sphere_occluder_geometry::render(void)` |
| 99.88 | `private: void __thiscall vostok::render::decal_instance::render_geometry(void)` |
| 99.88 | `private: void __thiscall vostok::render::stage_postprocess::fill_surface(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)` |
| 99.88 | `public: void __thiscall vostok::render::scene::flush(class boost::function<void __cdecl (bool)> const &, bool, bool)` |
| 99.89 | `public: void __thiscall vostok::render::backend::render_indexed(enum D3D_PRIMITIVE_TOPOLOGY, unsigned int, unsigned int, unsigned int)` |
| 99.89 | `public: void __thiscall vostok::render::stage_atmosphere::fill_surfaces(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, bool)` |
| 99.89 | `vostok::render::fill_surface` |
| 99.89 | `public: bool __thiscall vostok::render::ambient_volume::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::decal_instance::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::environment_probe::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::grass_patch::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::light::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::render_surface_instance::is_occluded(void) const` |
| 99.89 | `public: virtual bool __thiscall vostok::render::render_particle_emitter_instance::is_occluded(void) const` |
| 99.89 | `public: enum vostok::render::enum_options_changes_result __thiscall vostok::render::options::end_render_options_changing(class vostok::render::vector<class vostok::fs_new::virtual_path_string> &)` |
| 99.89 | `public: void __thiscall vostok::render::renderer::draw_debug(class vostok::render::scene *, class vostok::render::scene_view *, float, struct vostok::ui::font const *)` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::ambient_volume>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::decal_instance>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::environment_probe>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::grass_patch>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::render_surface_instance>` |
| 99.91 | `public: __thiscall vostok::render::render_output_window::render_output_window(struct vostok::render::output_window_configuration const &)` |
| 99.91 | `public: void __thiscall vostok::render::stage_screen_image::execute(class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)` |
| 99.91 | `private: void __thiscall vostok::render::stage_postprocess::fill_surface2(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>)` |
| 99.91 | `vostok::render::is_occluded_predicate_light` |
| 99.92 | `public: void __thiscall vostok::render::radiance_volume::prepare_final(void)` |
| 99.93 | `private: void __thiscall vostok::render::radiance_volume::begin_render_to_cells(void)` |
| 99.93 | `public: void __thiscall vostok::render::renderer::setup_render_output_window(class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base>, class vostok::math::rectangle<class vostok::math::float2> const &)` |
| 99.93 | `public: void __thiscall vostok::render::batched_geometry<struct vostok::render::lpv_vertex>::for_each_batch_render(class vostok::render::renderer_context *, class boost::function<void __cdecl (struct vostok::render::geometry_batch const &)> const &, class boost::function<void __cdecl (struct vostok::render::geometry_batch const &)> const &)` |
| 99.93 | `public: __thiscall singletons_on_preinitialize::singletons_on_preinitialize(class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, bool)` |
| 99.94 | `public: virtual void __thiscall vostok::render::stage_particles::execute(void)` |
| 99.94 | `public: void __thiscall vostok::render::renderer::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::rectangle<class vostok::math::float2> const &, class boost::function<void __cdecl (bool)> const &, bool, struct vostok::ui::font const *)` |
| 99.94 | `public: void __thiscall vostok::render::backend::clear_depth_stencil(unsigned int, float, unsigned char)` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::ambient_volume>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::decal_instance>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::environment_probe>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::grass_patch>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::render_surface_instance>` |
| 99.95 | `vostok::render::is_not_occluded_predicate_light` |
| 99.95 | `public: virtual void __thiscall vostok::render::stage_accumulate_distortion::execute(void)` |
| 99.95 | `public: void __thiscall vostok::render::system_renderer::draw_ui_vertices(struct vostok::render::vertex_formats::TL const *, unsigned int const &, int, int)` |
| 99.95 | `private: void __thiscall vostok::render::renderer_context_targets::create_targets(class vostok::math::uint2, bool)` |
| 99.95 | `public: class vostok::render::shader_constant_host * __thiscall vostok::render::backend::register_constant_host(class vostok::shared_string const &, enum vostok::render::enum_constant_type)` |
| 99.95 | `public: void __thiscall vostok::render::hw_hiz_occlusion_manager::process_culling(class vostok::render::renderer_context *, class vostok::math::float4const *, unsigned int)` |
| 99.96 | `private: void __thiscall vostok::render::stage_visibility::gather_statistics(void) const` |
| 99.96 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_quad(void)` |
| 99.96 | `public: void __thiscall vostok::render::system_renderer::fill_surface(class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, class vostok::intrusive_ptr<class vostok::render::render_target, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, bool, struct D3D11_VIEWPORT *, float, float, float, float)` |
| 99.96 | `public: virtual void __thiscall vostok::render::stage_lights::debug_render(void)` |
| 99.96 | `public: bool __thiscall vostok::render::remove_model_if_not_lod_predicate::operator()(struct vostok::render::render_surface_instance *)` |
| 99.97 | `private: void __thiscall vostok::render::stage_postprocess::measure_per_pixel_luminance(class vostok::render::res_texture *, class vostok::math::float4&)` |
| 99.97 | `public: virtual void __thiscall vostok::render::stage_apply_distortion::execute(void)` |
| 99.97 | `public: void __thiscall vostok::render::backend::clear_render_targets(float, float, float, float)` |
| 99.97 | `public: void __thiscall vostok::render::grass_world::render(class vostok::render::renderer_context *, class vostok::math::float3const &, enum vostok::render::enum_render_stage_type, unsigned int, float, bool, class vostok::render::res_effect *, bool, unsigned int)` |
| 99.97 | `private: void __thiscall vostok::render::renderer::draw_frame_histogram(void) const` |
| 99.98 | `public: void __thiscall vostok::render::backend::clear_render_targets(class vostok::math::color, class vostok::math::color, class vostok::math::color, class vostok::math::color)` |
| 99.98 | `public: void __thiscall vostok::render::engine::world::initialize(bool)` |
| 99.98 | `private: void __thiscall vostok::render::renderer::execute_stages(void)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_decals_accumulate::execute(void)` |
| 99.98 | `public: void __thiscall vostok::render::grass_patch::render(struct vostok::render::grass_world *, class vostok::render::renderer_context *, class vostok::math::float3const &, enum vostok::render::enum_render_stage_type, unsigned int, float, class vostok::render::res_effect *, unsigned int)` |
| 99.98 | `public: void __thiscall vostok::render::backend::flush_rt_shader_resources(void)` |
| 99.98 | `public: void __thiscall vostok::render::backend::clear_render_targets(class vostok::math::color)` |
| 99.99 | `public: bool __thiscall vostok::render::remove_inappropriate_models::operator()(struct vostok::render::render_surface_instance *)` |
| 99.99 | `vostok::render::get_format_block_size` |
| 99.99 | `void __cdecl vostok::console_commands::show_help(char const *)` |
| 99.99 | `public: void __thiscall vostok::render::render_particle_emitter_instance::render_trails(class vostok::math::float3const &, struct vostok::particle::base_particle *, unsigned int)` |
| 99.99 | `public: void __thiscall vostok::render::system_renderer::draw_3D_point(class vostok::math::float3const &, float, class vostok::math::color const &, bool)` |
| 99.99 | `public: class vostok::render::effect_compiler & __thiscall vostok::render::effect_compiler::set_texture(char const *, char const *, class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy> *, bool, unsigned int)` |
| 99.99 | `public: void __thiscall vostok::render::radiance_volume::prepare(class vostok::math::float3const &, class vostok::math::float3const &, float)` |
| 99.99 | `public: __thiscall vostok::render::grass_patch::grass_patch(struct vostok::collision::space_partitioning_tree *const, struct vostok::render::grass_template *, class vostok::math::float3const &, float)` |
| 99.99 | `public: void __thiscall vostok::render::scene::select_models(class vostok::math::float4x4const &, class vostok::render::vector<struct vostok::render::render_surface_instance *> &, class vostok::math::float3const &, unsigned int, bool)` |
| 99.99 | `public: void __thiscall vostok::render::stage_shadow_direct::execute_cascade(unsigned int, unsigned int, unsigned int)` |
| 99.99 | `public: void __thiscall vostok::render::cloud_simulation::generate(struct vostok::render::cloud_key_parameters const &, class vostok::math::float3const &)` |
| 100.00 | `public: __thiscall vostok::render::system_renderer::system_renderer(class vostok::render::renderer_context *)` |
| 100.00 | `public: virtual void __thiscall vostok::render::stage_visibility::execute(void)` |
| 100.00 | `public: __thiscall vostok::render::stage_atmosphere::stage_atmosphere(class vostok::render::renderer *, class vostok::render::renderer_context *, enum vostok::render::stage_atmosphere::stage_type)` |
| 100.00 | `public: __thiscall vostok::render::stage_volume_fog::stage_volume_fog(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 100.00 | `public: void __thiscall vostok::render::renderer::fill_opaque_models(void)` |

### Added (36)

- `[thunk]: __thiscall survarium::weapon_core::`vcall'{196, {flat}}`
- `bool __cdecl vostok::console_commands::execute_console_commands(class vostok::fs_new::native_path_string, enum vostok::console_commands::execution_filter, bool)`
- `private: bool __thiscall survarium::weapon_core::idle_AE_or_chamber_a_round_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::reload_break_pred(void) const`
- `public: __thiscall boost::intrusive::set_member_hook<struct boost::intrusive::link_mode<2>, struct boost::intrusive::none, struct boost::intrusive::none, struct boost::intrusive::none>::~set_member_hook<struct boost::intrusive::link_mode<2>, struct boost::intrusive::none, struct boost::intrusive::none, struct boost::intrusive::none>(void)`
- `public: __thiscall vostok::particle::lod_entry::~lod_entry(void)`
- `public: __thiscall vostok::vectora<struct vostok::resources::request>::~vectora<struct vostok::resources::request>(void)`
- `public: virtual __thiscall vostok::ai::selectors::sound_target_selector::~sound_target_selector(void)`
- `public: virtual __thiscall vostok::particle::particle_system_instance::~particle_system_instance(void)`
- `public: virtual __thiscall vostok::render::stage_postprocess::~stage_postprocess(void)`
- `public: virtual __thiscall vostok::resources::fs_task_unmount::~fs_task_unmount(void)`
- `public: virtual void * __thiscall Scaleform::Render::MappedTextureBase::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall btClosestNotMeConvexResultCallback::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::free_fly_camera::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::game_options::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::global_input_handler::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::usable_object::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::weapon_core_idle_state::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::ai::selectors::sound_target_selector::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::console_commands::cc_u32::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::memory::managed_node_owner::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::particle::particle_system_instance_impl::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::speedtree_instance::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage_forward::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage_postprocess::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::resources::fs_task_unmount::`vector deleting destructor'(unsigned int)`
- `public: void __thiscall survarium::game::load_cc_script(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, bool, bool)`
- `public: void __thiscall survarium::game::load_config_query(char const *, bool, bool)`
- `public: void __thiscall survarium::game::on_config_loaded(class vostok::resources::queries_result &, bool, bool)`
- `public: void __thiscall vostok::render::backend::set_gs_constant<float>(class vostok::render::shader_constant_host const *, float const &)`
- `public: void __thiscall vostok::render::backend::set_ps_constant<class vostok::math::float4>(class vostok::render::shader_constant_host const *, class vostok::math::float4const *, unsigned int)`
- `public: void __thiscall vostok::render::backend::set_vs_constant<float>(class vostok::render::shader_constant_host const *, float const &)`
- `public: void __thiscall vostok::render::shader_constant_buffer::set_typed<class vostok::math::float4>(class vostok::render::shader_constant_slot const &, class vostok::math::float4const *, unsigned int)`
- `public: void __thiscall vostok::render::shader_constant_buffer::set_typed<int>(class vostok::render::shader_constant_slot const &, int const &)`
- `void __cdecl vostok::console_commands::execute(char const *, enum vostok::console_commands::execution_filter, bool)`
- `void __cdecl vostok::console_commands::load(class vostok::memory::reader &, enum vostok::console_commands::execution_filter, bool)`

### Deleted (49)

- `[thunk]: __thiscall vostok::network::world::`vcall'{4, {flat}}`
- `[thunk]: public: virtual void __thiscall vostok::engine::editor_console::on_activate(void)`
- `[thunk]: public: virtual void __thiscall vostok::engine::editor_console::on_deactivate(void)`
- ``survarium::game::register_console_commands'::`2'::`dynamic atexit destructor for 'cfg_load_level''`
- ``survarium::game::register_console_commands'::`2'::`dynamic atexit destructor for 'cfg_unload_level''`
- ``vostok::render::options::register_console_commands'::`2'::`dynamic atexit destructor for 'use_parallax_cc''`
- `bool __cdecl vostok::console_commands::execute_console_commands(class vostok::fs_new::native_path_string, enum vostok::console_commands::execution_filter)`
- `private: void __thiscall survarium::game::load_cmd(char const *)`
- `private: void __thiscall survarium::game::unload_cmd(char const *)`
- `private: void __thiscall vostok::render::constants_handler<0>::set_constant<class vostok::math::float3>(class vostok::render::shader_constant_host const &, class vostok::math::float3const &)`
- `private: void __thiscall vostok::render::constants_handler<0>::set_constant_array<class vostok::math::float4>(class vostok::render::shader_constant_host const &, class vostok::math::float4const *, unsigned int)`
- `private: void __thiscall vostok::render::constants_handler<1>::set_constant<int>(class vostok::render::shader_constant_host const &, int const &)`
- `private: void __thiscall vostok::render::constants_handler<1>::set_constant_array<class vostok::math::float4>(class vostok::render::shader_constant_host const &, class vostok::math::float4const *, unsigned int)`
- `private: void __thiscall vostok::render::constants_handler<2>::set_constant<class vostok::math::float3>(class vostok::render::shader_constant_host const &, class vostok::math::float3const &)`
- `private: void __thiscall vostok::render::shader_constant_buffer::set_memory(unsigned int, char const *, unsigned int)`
- `public: __thiscall boost::_bi::storage3<class boost::_bi::value<class vostok::render::engine::world *>, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> >, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> > >::storage3<class boost::_bi::value<class vostok::render::engine::world *>, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> >, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> > >(struct boost::_bi::storage3<class boost::_bi::value<class vostok::render::engine::world *>, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> >, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> > > const &)`
- `public: __thiscall boost::function0<bool>::~function0<bool>(void)`
- `public: __thiscall vostok::detail::abstract_type_helper::abstract_type_helper(void)`
- `public: __thiscall vostok::render::geometry_batch::~geometry_batch(void)`
- `public: __thiscall vostok::render::render_target_instance::render_target_instance(void)`
- `public: __thiscall vostok::render::requested_streamable_texture::requested_streamable_texture(struct vostok::render::requested_streamable_texture const &)`
- `public: __thiscall vostok::render::speedtree_data::speedtree_data(void)`
- `public: __thiscall vostok::render::streamable_texture_info::streamable_texture_info(struct vostok::render::streamable_texture_info const &)`
- `public: __thiscall vostok::render::streaming_ready_texture::streaming_ready_texture(struct vostok::render::streaming_ready_texture const &)`
- `public: __thiscall vostok::threading::mutex::~mutex(void)`
- `public: struct vostok::render::streaming_ready_texture & __thiscall vostok::render::streaming_ready_texture::operator=(struct vostok::render::streaming_ready_texture const &)`
- `public: virtual __thiscall survarium::animated_model_instance::~animated_model_instance(void)`
- `public: virtual __thiscall survarium::player_logic_sprint_state::~player_logic_sprint_state(void)`
- `public: virtual void * __thiscall Scaleform::GFx::State::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall Scaleform::Log::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall Scaleform::Render::TextureFormat::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall btCollisionWorld::ContactResultCallback::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall btCollisionWorld::RayResultCallback::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall stlp_std::runtime_error::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::animated_model_instance::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::player_logic_sprint_state::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::console_impl::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::grass_render_surface::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage_light_propagation_volumes::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage_translucency::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::static_render_surface::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::resources::managed_resource::`vector deleting destructor'(unsigned int)`
- `public: void * __thiscall boost::_bi::bind_t<void, class boost::_mfi::mf2<void, class survarium::object_wire, class vostok::resources::queries_result &, class boost::function<void __cdecl (class survarium::game_object_&)> &>, class boost::_bi::list3<class boost::_bi::value<class survarium::object_wire *>, struct boost::arg<1>, class boost::_bi::value<class boost::function<void __cdecl (class survarium::game_object_&)> > > >::`scalar deleting destructor'(unsigned int)`
- `public: void __thiscall survarium::game::load_cc_script(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, bool)`
- `public: void __thiscall survarium::game::load_config_query(char const *, bool)`
- `public: void __thiscall survarium::game::on_config_loaded(class vostok::resources::queries_result &, bool)`
- `public: void __thiscall vostok::render::backend::set_vs_constant<class vostok::math::float4>(class vostok::render::shader_constant_host const *, class vostok::math::float4const &)`
- `void __cdecl vostok::console_commands::execute(char const *, enum vostok::console_commands::execution_filter)`
- `void __cdecl vostok::console_commands::load(class vostok::memory::reader &, enum vostok::console_commands::execution_filter)`

---

## v0.1.1b-build826 → v0.1.1c-build870
_2013-05-14 → 2013-05-24 · +173 / -202 / ~1538_

### Changed (1538)

| match % | function |
| ---: | --- |
| 0.00 | `[thunk]: __thiscall vostok::sound::world::`vcall'{12, {flat}}` |
| 0.00 | `[thunk]: protected: virtual class vostok::sound::sound_propagator_emitter const * __thiscall vostok::sound::single_sound::get_sound_propagator_emitter(unsigned __int64) const` |
| 0.00 | `[thunk]: public: virtual void * __thiscall survarium::ladder::`vector deleting destructor'(unsigned int)` |
| 0.00 | `[thunk]: public: virtual void * __thiscall vostok::sound::single_sound::`vector deleting destructor'(unsigned int)` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_aimed_fire_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_chamber_a_round_aimed_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_chamber_a_round_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_double_barreled_aimed_fire_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_double_barreled_fire_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_double_barreled_hide_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_double_barreled_reload_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_double_barreled_show_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_double_barreled_weapon_core_aimed_idle_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_double_barreled_weapon_core_idle_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_fire_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_hide_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_pistol_aimed_fire_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_pistol_fire_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_pistol_hide_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_pistol_reload_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_pistol_show_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_pistol_weapon_core_aimed_idle_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_pistol_weapon_core_idle_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_reload_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_shotgun_reload_finish_substate_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_shotgun_reload_one_round_substate_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_shotgun_reload_start_substate_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_shotgun_weapon_reload_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_show_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_weapon_core_aimed_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_weapon_core_idle_state_cook''` |
| 0.00 | ``survarium::weapon_cook::register_cooks_for_logic_states'::`2'::`dynamic atexit destructor for 's_weapon_core_inactive_state_cook''` |
| 0.00 | `empty_stub` |
| 0.00 | `long __cdecl vostok::threading::interlocked_increment(long volatile &)` |
| 0.00 | `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 0.00 | `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::destroy_resource(class vostok::resources::unmanaged_resource *)` |
| 0.00 | `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::destroy_resource(class vostok::resources::unmanaged_resource *)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_scene::init_allocators(class vostok::resources::query_result_for_cook &)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_scene::notify_receivers(void)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_scene::on_unmanaged_resources_allocated(class vostok::resources::queries_result &)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_scene::update_receivers_position(void)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_spl_cook::on_config_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)` |
| 0.00 | `private: void __thiscall vostok::sound::sound_voice::on_buffer_end_impl(void *)` |
| 0.00 | `protected: virtual bool __thiscall btCollisionObject::checkCollideWithOverride(class btCollisionObject *)` |
| 0.00 | `public: __thiscall boost::function1<void, class vostok::vfs::vfs_iterator &>::~function1<void, class vostok::vfs::vfs_iterator &>(void)` |
| 0.00 | `public: __thiscall survarium::vector<class vostok::variant<32> const *>::~vector<class vostok::variant<32> const *>(void)` |
| 0.00 | `public: __thiscall vostok::animation::mixing::animation_interval::~animation_interval(void)` |
| 0.00 | `public: __thiscall vostok::buffer_vector<unsigned int>::~buffer_vector<unsigned int>(void)` |
| 0.00 | `public: __thiscall vostok::intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::~intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>(void)` |
| 0.00 | `public: __thiscall vostok::math::float3::float3(void)` |
| 0.00 | `public: __thiscall vostok::render::box_geometry::~box_geometry(void)` |
| 0.00 | `public: __thiscall vostok::render::sun_cascade::sun_cascade(struct vostok::render::sun_cascade const &)` |
| 0.00 | `public: __thiscall vostok::resources::pinned_ptr_const<class vostok::animation::cubic_spline_skeleton_animation>::~pinned_ptr_const<class vostok::animation::cubic_spline_skeleton_animation>(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class survarium::inventory_item, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>(class vostok::resources::managed_resource *)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::unmanaged_resource *)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::size_policy::size_policy(void)` |
| 0.00 | `public: __thiscall vostok::sound::new_sound_propagator::~new_sound_propagator(void)` |
| 0.00 | `public: __thiscall vostok::sound::receiver_collision::receiver_collision(class vostok::sound::sound_receiver *, class vostok::sound::atomic_half3*)` |
| 0.00 | `public: __thiscall vostok::sound::receiver_collision::~receiver_collision(void)` |
| 0.00 | `public: __thiscall vostok::sound::sound_scene::sound_scene(class vostok::sound::sound_world &, struct vostok::sound::sound_scene_creation_params const &, struct IXAudio2SubmixVoice *, unsigned int, class vostok::resources::query_result_for_cook &)` |
| 0.00 | `public: bool __thiscall vostok::sound::sound_scene::graph_exist(void) const` |
| 0.00 | `public: bool __thiscall vostok::sound::sound_scene::is_segment_pass_portal(unsigned int, class vostok::math::float3, class vostok::math::float3) const` |
| 0.00 | `public: char const * __thiscall vostok::buffer_string::end(void) const` |
| 0.00 | `public: char const * __thiscall vostok::fs_new::path_string_impl::c_str(void) const` |
| 0.00 | `public: class vostok::buffer_string const & __thiscall vostok::buffer_string::operator=(class vostok::buffer_string const &)` |
| 0.00 | `public: class vostok::math::float3 __thiscall vostok::sound::sound_scene::get_portal_center(unsigned int) const` |
| 0.00 | `public: class vostok::math::float3 __thiscall vostok::sound::sound_scene::get_portal_nearest_point(unsigned int, class vostok::math::float3, class vostok::math::float3) const` |
| 0.00 | `public: class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base>::operator=(class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 0.00 | `public: class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::operator=(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 0.00 | `public: class vostok::sound::atomic_half3* __thiscall vostok::sound::sound_scene::create_receiver_position(void)` |
| 0.00 | `public: class vostok::variant<32> & __thiscall vostok::buffer_vector<class vostok::variant<32> >::operator[](unsigned int)` |
| 0.00 | `public: struct IXAudio2SubmixVoice * __thiscall vostok::sound::sound_world::create_submix_voice(unsigned char, unsigned char) const` |
| 0.00 | `public: struct vostok::sound::sound_scene_statistic * __thiscall vostok::sound::sound_scene::create_statistic(void) const` |
| 0.00 | `public: virtual __thiscall survarium::inventory_cook::~inventory_cook(void)` |
| 0.00 | `public: virtual __thiscall survarium::victory_items_container_core::~victory_items_container_core(void)` |
| 0.00 | `public: virtual bool __thiscall Scaleform::MemoryFile::Flush(void)` |
| 0.00 | `public: virtual void * __thiscall survarium::console_command_bind::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::damage_protector::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::empty_hands::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::flash_external_handler::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::inventory_cook::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::jump_logic_base_state::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::lobby_camera::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::player_cook::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::player_logic_base_state::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::victory_items_container::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::planning::operator_base::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::selectors::enemy_target_selector::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::selectors::sound_target_selector::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::sensors::smell_sensor::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::animation::mixing::addition_lexeme::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::collision::aabb_object::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::collision::box_geometry_instance::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::detail::abstract_type_helper::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::memory::base_allocator::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::network::functor_response::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::network::string_response::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::physics::animated_model_instance::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::base_scene::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::effect_sun::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::functor_command::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::render_model_instance_impl::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::render_surface::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::sound::sound_scene::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::sound::sound_spl_cook::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void __thiscall survarium::game_camera::on_focus(bool)` |
| 0.00 | `public: virtual void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 0.00 | `public: void __thiscall survarium::game_world_ui::on_unload(void)` |
| 0.00 | `public: void __thiscall vostok::render::engine::world::build_lpv_geometry(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 0.00 | `public: void __thiscall vostok::render::grass_world::accumulate_trample(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 0.00 | `public: void __thiscall vostok::render::stage_shadow_direct::execute_cascade(unsigned int, unsigned int, unsigned int)` |
| 0.00 | `public: void __thiscall vostok::sound::proxy_statistic::fill_text_tree(class vostok::strings::text_tree_item *, bool) const` |
| 0.00 | `public: void __thiscall vostok::sound::receiver_collision::delete_position(class vostok::sound::sound_scene &)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::clear_resources(void)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::delete_receiver_position(class vostok::sound::atomic_half3*)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::delete_statistic(struct vostok::sound::sound_scene_statistic *) const` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::fade_in(class vostok::sound::sound_world &, unsigned int)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::fade_out(unsigned int)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::find_path(class vostok::math::float3const &, class vostok::vectora<class vostok::fixed_vector<unsigned int, 32> > &) const` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::free_sound_instance_proxy(class vostok::sound::sound_instance_proxy *)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::register_receiver(class vostok::sound::sound_receiver *, class vostok::sound::atomic_half3*)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::set_graph(class vostok::resources::resource_ptr<class vostok::render::culling::portal_sector_structure, class vostok::resources::unmanaged_intrusive_base> &)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::unregister_receiver(class vostok::sound::world_user &, class vostok::sound::sound_receiver *)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_scene::update_stats(class vostok::sound::sound_debug_stats &) const` |
| 0.00 | `public: void __thiscall vostok::sound::sound_voice::on_buffer_start(void *)` |
| 0.00 | `public: void __thiscall vostok::sound::sound_voice::set_output_matrix(float const *)` |
| 0.00 | `vec_begin` |
| 0.00 | `void __cdecl vostok::memory::delete_helper<class vostok::memory::doug_lea_allocator, class vostok::render::stage>(class vostok::memory::doug_lea_allocator &, class vostok::render::stage *&)` |
| 0.00 | `void __cdecl vostok::memory::delete_helper<class vostok::memory::doug_lea_allocator, struct vostok::ai::sound_item_wrapper>(class vostok::memory::doug_lea_allocator &, struct vostok::ai::sound_item_wrapper *&)` |
| 0.00 | `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::base_allocator, class vostok::vfs::mounter, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::base_allocator &, class vostok::vfs::mounter *&, struct vostok::memory::detail::call_destructor_predicate const &)` |
| 0.00 | `vostok::animation::`dynamic initializer for 'zero''` |
| 0.00 | `vostok::sound::closest_point_on_segment` |
| 3.33 | `public: virtual bool __thiscall survarium::game_world::on_mouse_move(struct vostok::input::world *, int, int, int)` |
| 3.64 | `private: class survarium::double_barreled_weapon_core_hide_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_hide_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | `private: class survarium::double_barreled_weapon_core_show_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::double_barreled_weapon_core_show_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | `private: class survarium::pistol_weapon_core_hide_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::pistol_weapon_core_hide_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | `private: class survarium::pistol_weapon_core_show_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::pistol_weapon_core_show_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | `private: class survarium::weapon_core_hide_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_hide_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 3.64 | `private: class survarium::weapon_core_show_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_show_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 4.09 | `public: virtual void __thiscall vostok::sound::sound_world::clear_resources(void)` |
| 4.58 | `public: void __thiscall vostok::sound::sound_voice::on_buffer_end(void *)` |
| 5.59 | `public: virtual bool __thiscall survarium::game_world::on_mouse_key_action(struct vostok::input::world *, enum vostok::input::mouse_button, enum vostok::input::enum_mouse_key_action)` |
| 8.01 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnBufferEnd(void *)` |
| 8.89 | `public: void __thiscall vostok::resources::query_result_for_cook::finish_query(enum vostok::resources::query_result_for_user::error_type_enum, enum assert_on_fail_bool)` |
| 10.33 | `private: void __thiscall survarium::player::remove_alive(void)` |
| 12.00 | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 15.23 | `private: void __thiscall survarium::human_npc::set_brain_unit(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 22.38 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnBufferStart(void *)` |
| 22.38 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnLoopEnd(void *)` |
| 24.89 | `private: virtual void __thiscall survarium::weapon_core_hide_state_base::on_animation_end_impl(bool &)` |
| 24.89 | `private: virtual void __thiscall survarium::weapon_core_show_state_base::on_animation_end_impl(bool &)` |
| 25.00 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnVoiceProcessingPassStart(unsigned int)` |
| 25.17 | `public: virtual void __thiscall vostok::detail::concrete_type_helper<struct vostok::render::static_model_instance_user_data>::copy(class vostok::mutable_buffer, class vostok::const_buffer)` |
| 26.65 | `public: __thiscall vostok::render::grass_patch::grass_patch(struct vostok::collision::space_partitioning_tree *const, struct vostok::render::grass_template *, class vostok::math::float3const &, float)` |
| 27.67 | `class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __cdecl vostok::static_cast_resource_ptr<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>, class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)` |
| 28.57 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnVoiceProcessingPassEnd(void)` |
| 30.00 | `public: class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::operator=(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 31.00 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnVoiceError(void *, long)` |
| 32.07 | `private: virtual void __stdcall vostok::sound::voice_bridge::OnStreamEnd(void)` |
| 34.23 | `public: void __thiscall vostok::sound::voice_bridge::set_low_pass_filter_params(float)` |
| 34.82 | `private: virtual void __thiscall survarium::booby_trap_core::on_enter(class vostok::buffer_vector<class vostok::physics::base_physics_object *> const &)` |
| 35.21 | `public: virtual void __thiscall survarium::object_particle_visual::load(class vostok::configs::binary_config_value const &, char const *, class boost::function<void __cdecl (class survarium::game_object_&)> &)` |
| 35.60 | `public: virtual void __thiscall survarium::animation_analysis_result_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | `public: virtual void __thiscall survarium::items_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | `public: virtual void __thiscall survarium::items_dictionary_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | `public: virtual void __thiscall survarium::player_parameters_modifyer_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.60 | `public: virtual void __thiscall survarium::weapon_ammunition_cook::delete_resource(class vostok::resources::resource_base *)` |
| 35.71 | `private: void __thiscall vostok::sound::sound_scene::emit_sound_propagators_impl(struct vostok::sound::create_sound_propagator_params const &)` |
| 36.16 | `public: virtual bool __thiscall vostok::render::render_cc_u32::fill_macro(struct vostok::render::shader_macro &) const` |
| 38.05 | `public: virtual void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::delete_resource(class vostok::resources::resource_base *)` |
| 38.15 | `public: class vostok::intrusive_ptr<class vostok::sound::sound_instance_proxy, class vostok::sound::sound_instance_proxy, class vostok::threading::single_threading_policy> __thiscall vostok::sound::sound_scene::new_point_sound_instance_proxy(class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_propagator_emitter const &, class vostok::sound::world_user &)` |
| 38.94 | `public: class vostok::intrusive_ptr<class vostok::sound::sound_instance_proxy, class vostok::sound::sound_instance_proxy, class vostok::threading::single_threading_policy> __thiscall vostok::sound::sound_scene::new_spot_sound_instance_proxy(class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_propagator_emitter const &, class vostok::sound::world_user &, enum vostok::sound::sound_cone_type)` |
| 40.07 | `public: class vostok::intrusive_ptr<class vostok::sound::sound_instance_proxy, class vostok::sound::sound_instance_proxy, class vostok::threading::single_threading_policy> __thiscall vostok::sound::sound_scene::new_volumetric_sound_instance_proxy(class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_propagator_emitter const &, class vostok::sound::world_user &, class vostok::collision::geometry_instance &, float)` |
| 41.25 | `private: void __thiscall vostok::render::device::create_d3d(void)` |
| 41.50 | `public: virtual void __thiscall vostok::detail::concrete_type_helper<struct vostok::ai::brain_unit_cook_params>::copy(class vostok::mutable_buffer, class vostok::const_buffer)` |
| 42.11 | `public: void __thiscall vostok::sound::propagator_statistic::fill_text_tree(class vostok::strings::text_tree_item *) const` |
| 42.77 | `private: void __thiscall vostok::sound::sound_world::register_sound_cooks(void)` |
| 43.84 | `private: void __thiscall survarium::network_client::process_shop_action(class vostok::network_core::packet_reader &)` |
| 43.90 | `private: void __thiscall vostok::sound::voice_bridge::set_handler(class vostok::sound::sound_voice *)` |
| 44.82 | `public: class vostok::sound::new_sound_propagator * __thiscall vostok::sound::sound_scene::create_sound_propagator(class vostok::sound::sound_propagator_emitter const &, class vostok::sound::sound_instance_proxy_internal &, enum vostok::sound::playback_mode, unsigned int, unsigned int, unsigned int, unsigned int, class vostok::sound::sound_producer const *const, class vostok::sound::sound_receiver const *const)` |
| 45.29 | `public: virtual void __thiscall survarium::victory_item_core_cook::delete_resource(class vostok::resources::resource_base *)` |
| 45.29 | `public: virtual void __thiscall survarium::weapon_core_cook::delete_resource(class vostok::resources::resource_base *)` |
| 45.29 | `public: virtual void __thiscall survarium::weapon_user_animations_container_cook::delete_resource(class vostok::resources::resource_base *)` |
| 45.29 | `public: virtual void __thiscall vostok::ai::brain_unit_cook::delete_resource(class vostok::resources::resource_base *)` |
| 45.77 | `public: virtual void __thiscall survarium::object_environment_probe::insert(void)` |
| 47.35 | `public: void __thiscall vostok::resources::query_result_for_cook::set_managed_resource(class vostok::resources::managed_resource *)` |
| 48.63 | `survarium::compare_bone_data_predicate` |
| 50.76 | `private: void __thiscall vostok::ui::ui_text_edit::add_action(class vostok::ui::base_edit_action *)` |
| 51.04 | `public: void __thiscall vostok::sound::voice_bridge::set_output_matrix(float const *)` |
| 51.70 | `public: __thiscall survarium::base_game_scene::base_game_scene(class survarium::game &)` |
| 52.23 | `public: virtual void __thiscall survarium::network_client::send_local_player_input(struct survarium::player_input const &, unsigned int, class vostok::math::float4x4const &, float)` |
| 52.78 | `public: virtual void __thiscall vostok::animation::cubic_spline_skeleton_animation_cook::destroy_resource(class vostok::resources::managed_resource *)` |
| 52.78 | `public: virtual void __thiscall vostok::render::texture_cook::destroy_resource(class vostok::resources::managed_resource *)` |
| 52.79 | `public: __thiscall vostok::ui::ui_scroll_bar::ui_scroll_bar(class vostok::memory::base_allocator &)` |
| 53.01 | `public: class vostok::render::res_texture * __thiscall vostok::render::resource_manager::create_texture2d(char const *, unsigned int, unsigned int, struct D3D11_SUBRESOURCE_DATA const *, enum DXGI_FORMAT, enum D3D11_USAGE, unsigned int, unsigned int, bool)` |
| 53.11 | `protected: virtual void __thiscall survarium::weapon_core_hide_state_base::initialize(void)` |
| 53.11 | `protected: virtual void __thiscall survarium::weapon_core_show_state_base::initialize(void)` |
| 54.35 | `public: virtual void __thiscall vostok::render::effect_motion_blur::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 54.41 | `public: void __thiscall vostok::sound::sound_world::delete_sound_voice(class vostok::sound::sound_scene &, class vostok::sound::sound_voice *)` |
| 55.61 | `public: void __thiscall survarium::weapon_core::instant_show(void)` |
| 56.52 | `public: __thiscall vostok::render::radiance_volume::radiance_volume(unsigned int, unsigned int, unsigned int, float, float)` |
| 56.83 | `private: void __thiscall survarium::player_input_handler::process_third_person_mode(void)` |
| 57.29 | `public: void __thiscall vostok::intrusive_list<struct vostok::strings::text_tree_item_base, class vostok::strings::text_tree_item *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::for_each<struct vostok::intrusive_list<struct vostok::strings::text_tree_item_base, class vostok::strings::text_tree_item *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::void_predicate_ref<struct vostok::strings::text_tree_item::text_tree_item_deleter> >(struct vostok::intrusive_list<struct vostok::strings::text_tree_item_base, class vostok::strings::text_tree_item *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::void_predicate_ref<struct vostok::strings::text_tree_item::text_tree_item_deleter> const &) const` |
| 57.46 | `public: void __thiscall survarium::human_npc::get_available_weapons(class vostok::vectora<struct vostok::ai::weapon *> &) const` |
| 57.54 | `public: void __thiscall vostok::render::options::register_console_commands(void)` |
| 58.07 | `public: void __thiscall vostok::sound::sound_spl::load(class vostok::configs::binary_config_value const &)` |
| 58.18 | `public: __thiscall vostok::fixed_string<64>::fixed_string<64>(char const *)` |
| 58.33 | `char * __cdecl vostok::strings::copy(char *, unsigned int, char const *)` |
| 58.33 | `public: class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> __thiscall vostok::resources::query_result_for_user::get_managed_resource(void) const` |
| 58.50 | `private: void __thiscall survarium::player::insert_alive(void)` |
| 58.68 | `public: virtual void __thiscall vostok::render::effect_editor_show_batched_geometry::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 59.07 | `private: void __thiscall vostok::render::stage_lights::make_plane_spot_light_shadowmap(unsigned int, class vostok::render::light *)` |
| 60.26 | `private: void __thiscall survarium::network_client::on_match_disconnected(enum vostok::network_core::disconnect_event_types_enum)` |
| 60.28 | `public: void __thiscall vostok::render::engine::world::initialize(bool)` |
| 60.32 | `public: __thiscall survarium::game_world_ui::game_world_ui(class survarium::game_world &)` |
| 60.39 | `public: void __thiscall vostok::sound::sound_scene_statistic::fill_text_tree(class vostok::strings::text_tree_item *) const` |
| 60.80 | `public: __thiscall vostok::strings::text_tree::~text_tree(void)` |
| 60.94 | `public: __thiscall survarium::max_angular_velocity_command::max_angular_velocity_command(char const *, float, float, bool, enum vostok::console_commands::command_type, enum vostok::console_commands::execution_filter)` |
| 60.98 | `private: void __thiscall vostok::render::decal_instance::set_materail_effects(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 61.16 | `public: virtual void __thiscall vostok::sound::single_sound_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 61.58 | `private: virtual void __thiscall survarium::booby_trap_set::action(bool)` |
| 62.23 | `public: virtual void __thiscall vostok::particle::particle_action_billboard::init(class vostok::particle::particle_emitter_instance *, struct vostok::particle::base_particle *, float)` |
| 62.28 | `public: void __thiscall survarium::weapon_core::instant_hide(void)` |
| 62.47 | `public: void __thiscall vostok::render::renderer_context_targets::new_rt(enum vostok::render::enum_render_target_index, enum DXGI_FORMAT, class vostok::math::uint2, enum vostok::render::enum_rt_usage, bool)` |
| 63.27 | `public: virtual void __thiscall vostok::render::effect_fstage_default_view_angle_dependent_materials::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 63.28 | `public: __thiscall vostok::ui::ui_scroll_view::ui_scroll_view(class vostok::memory::base_allocator &)` |
| 63.28 | `public: void __thiscall vostok::sound::new_sound_propagator::stop_propagation(void)` |
| 63.57 | `public: __thiscall vostok::fs_new::virtual_path_string::ctor<char const *>(char const *const &)` |
| 64.67 | `public: virtual void __thiscall survarium::game_world::get_available_weapons(struct vostok::ai::npc *, class vostok::vectora<struct vostok::ai::weapon *> &) const` |
| 66.32 | `public: virtual __thiscall survarium::game_world_ui::~game_world_ui(void)` |
| 66.48 | `private: void __thiscall survarium::damage_zone_core::hit_on_enter(unsigned int, unsigned int)` |
| 66.51 | `bool __cdecl survarium::state_prio(struct survarium::anomaly_state *, struct survarium::anomaly_state *)` |
| 66.67 | `public: class vostok::buffer_string & __thiscall vostok::buffer_string::append(char const *, char const *)` |
| 66.72 | `private: class vostok::animation::mixing::animation_lexeme __thiscall survarium::player_logic_stand_state::movement_lexeme(class vostok::mutable_buffer &, unsigned int, enum vostok::animation::body_part_masks_enum, bool, bool, bool) const` |
| 66.88 | `private: void __thiscall vostok::render::stage_lights::make_spot_light_shadowmap(unsigned int, class vostok::render::light *)` |
| 67.00 | `public: __thiscall vostok::fs_new::path_string_impl::ctor<char const *>(char, char const *const &)` |
| 67.15 | `char * __cdecl vostok::strings::copy<32>(char (&)[32], char const *)` |
| 67.22 | `public: virtual void __thiscall vostok::render::effect_system_colored::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 67.41 | `public: __thiscall vostok::console_commands::cc_delegate::cc_delegate(char const *, class boost::function<void __cdecl (char const *)> const &, bool, enum vostok::console_commands::command_type)` |
| 67.84 | `public: void __thiscall vostok::resources::association_callback_helper::get_managed(struct vostok::vfs::vfs_association *&)` |
| 68.18 | `public: virtual void __thiscall vostok::render::effect_wireframe_colored::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 68.23 | `public: void __thiscall survarium::collision_geometry::query_objects_by_type<class survarium::usable_object>(class vostok::vectora<class survarium::usable_object *> &, class survarium::usable_object * (__thiscall survarium::collision_geometry_subscriber::*)(void))` |
| 68.42 | `private: void __thiscall vostok::render::hw_hiz_occlusion_manager::check_culling_buffer(unsigned int)` |
| 68.48 | `public: void __thiscall vostok::sound::new_sound_propagator::pause_propagation(void)` |
| 69.32 | `private: void __thiscall survarium::player::detect_usable_objects(unsigned int)` |
| 70.05 | `public: class vostok::intrusive_ptr<class vostok::sound::sound_instance_proxy, class vostok::sound::sound_instance_proxy, class vostok::threading::single_threading_policy> __thiscall vostok::sound::sound_scene::new_hud_sound_instance_proxy(class vostok::resources::resource_ptr<class vostok::sound::sound_emitter, class vostok::resources::unmanaged_intrusive_base>, class vostok::sound::sound_propagator_emitter const &, class vostok::sound::world_user &)` |
| 71.19 | `public: virtual void __thiscall vostok::render::effect_gather_luminance::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 71.50 | `public: class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> & __thiscall vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>::operator=(class vostok::resources::managed_resource *)` |
| 71.67 | `public: __thiscall vostok::strings::text_tree_item::~text_tree_item(void)` |
| 71.80 | `public: virtual void __thiscall survarium::object_environment_probe::load(class vostok::configs::binary_config_value const &, char const *, class boost::function<void __cdecl (class survarium::game_object_&)> &)` |
| 72.55 | `public: enum vostok::render::enum_options_changes_result __thiscall vostok::render::options::end_render_options_changing(class vostok::render::vector<class vostok::fs_new::virtual_path_string> &)` |
| 72.85 | `public: void __thiscall vostok::particle::particle_emitter_instance::change_material(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 73.00 | `public: __thiscall vostok::collision::collision_object::collision_object(class vostok::memory::base_allocator *, unsigned int, class vostok::collision::geometry_instance *, void *const)` |
| 73.08 | `survarium::distance_from_cylinder_center_to_point_on_shape` |
| 73.16 | `public: void __thiscall vostok::ai::planning::animation_filter::add_filtered_item(char const *)` |
| 73.16 | `public: void __thiscall vostok::ai::planning::sound_filter::add_filtered_item(char const *)` |
| 73.33 | `public: void __thiscall vostok::vfs::base_node<1>::set_name(char const *)` |
| 73.34 | `private: void __thiscall survarium::damage_zone_core::hit_on_inside(unsigned int, unsigned int)` |
| 73.50 | `public: void __thiscall vostok::particle::particle_system_instance_impl::set_template(unsigned int, class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>)` |
| 73.82 | ``dynamic initializer for 'cfg_save_system_cc''` |
| 74.13 | `public: virtual void __thiscall vostok::render::static_model_instance_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 74.18 | `public: __thiscall vostok::buffer_string::ctor<char const *>(char *, unsigned int const &, char const *const &, char const *const &)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::config_params)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::config_params)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::config_params)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::config_params)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::config_params)` |
| 74.67 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::config_params)` |
| 74.71 | `private: __thiscall vostok::sound::voice_bridge::voice_bridge(struct vostok::sound::voice_bridge::creation_parametrs &)` |
| 74.88 | `public: __thiscall survarium::client_player_history_item::client_player_history_item(void)` |
| 74.92 | `public: virtual void __thiscall vostok::render::effect_post_process_downsample_frame::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 75.00 | `public: class vostok::buffer_string & __thiscall vostok::buffer_string::assign<char const *>(char const *const &, char const *const &)` |
| 75.20 | `public: virtual void __thiscall vostok::ui::ui_window::add_child(struct vostok::ui::window *, bool)` |
| 75.45 | `private: void __thiscall survarium::damage_zone_core::hit_on_motion_inside(unsigned int, unsigned int)` |
| 75.71 | `public: __thiscall vostok::ai::animation_item::animation_item(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &, char const *)` |
| 75.71 | `public: __thiscall vostok::ai::sound_item::sound_item(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &, char const *)` |
| 75.90 | ``dynamic initializer for 'cfg_save_user_cc''` |
| 75.97 | `public: __thiscall vostok::render::render_cc_float::render_cc_float(char const *, enum vostok::render::enum_options_changes_result, char const *, float &, float &, float, float, bool, enum vostok::console_commands::command_type)` |
| 76.54 | `public: unsigned char __thiscall survarium::body_part_parameters::get_health_in_percentage(void)` |
| 76.87 | `public: void __thiscall survarium::body_part_parameters::regenerate(unsigned int, unsigned int)` |
| 77.04 | `public: virtual void __thiscall vostok::render::effect_hiz_occlusion::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 77.14 | `public: virtual void __thiscall survarium::game_object_static::load(class vostok::configs::binary_config_value const &, char const *, class boost::function<void __cdecl (class survarium::game_object_&)> &)` |
| 77.20 | `public: virtual void __thiscall vostok::render::effect_sky_sphere_default_materials::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 77.25 | `public: virtual void __thiscall vostok::render::effect_god_rays::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 77.46 | `public: class vostok::render::render_target * __thiscall vostok::render::resource_manager::create_render_target(char const *, unsigned int, unsigned int, enum DXGI_FORMAT, enum vostok::render::enum_rt_usage, class vostok::intrusive_ptr<class vostok::render::res_texture, class vostok::render::resource_intrusive_base, class vostok::threading::single_threading_policy>, unsigned int, enum D3D11_USAGE, unsigned int, unsigned int)` |
| 77.76 | `public: __thiscall vostok::ai::planning::operator_impl::operator_impl(char const *, unsigned int)` |
| 77.88 | `public: virtual void __thiscall vostok::render::effect_eye_adaptation::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 77.89 | `private: virtual void __thiscall vostok::animation::skeleton_animation_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 78.01 | `private: class vostok::render::res_texture * __thiscall vostok::render::resource_manager::create_texture2d_impl(unsigned int, unsigned int, struct D3D11_SUBRESOURCE_DATA const *, enum DXGI_FORMAT, enum D3D11_USAGE, unsigned int, unsigned int, bool)` |
| 78.14 | `public: virtual void __thiscall vostok::render::effect_gather_luminance_histogram::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 78.61 | `public: virtual void __thiscall vostok::render::effect_post_process_mlaa::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 78.79 | `private: void __thiscall survarium::sound_player_cook::on_sounds_loaded(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)` |
| 79.33 | `public: virtual void __thiscall survarium::victory_items_container_core::put_item(class survarium::victory_item_core *)` |
| 79.46 | `public: void __thiscall survarium::game_world_ui::update_ui(unsigned int, unsigned int)` |
| 79.75 | `public: virtual void __thiscall vostok::render::effect_light_propagation_volumes::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 79.86 | `class vostok::math::float4x4 __cdecl vostok::math::create_rotation(class vostok::math::float3const &)` |
| 79.97 | `public: virtual void __thiscall survarium::respawn_point_core::load(class vostok::configs::binary_config_value const &)` |
| 80.22 | `private: void __thiscall survarium::game::draw_debug_window(void)` |
| 80.33 | `public: bool __thiscall vostok::variant<32>::try_get<struct vostok::ai::brain_unit_cook_params>(struct vostok::ai::brain_unit_cook_params &)` |
| 80.48 | `public: __thiscall vostok::render::stage_ambient_lighting::stage_ambient_lighting(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 80.48 | `vostok::ai::clone_string_from_config` |
| 80.60 | `public: virtual void __thiscall survarium::object_sound::load(class vostok::configs::binary_config_value const &, char const *, class boost::function<void __cdecl (class survarium::game_object_&)> &)` |
| 80.62 | `public: virtual void __thiscall vostok::render::effect_post_process_sharpen::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 80.66 | `public: virtual void __thiscall vostok::render::effect_fstage_default_materials::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 80.68 | `public: class vostok::fs_new::path_string_impl & __thiscall vostok::fs_new::path_string_impl::append<class vostok::fixed_string<260> >(class vostok::fixed_string<260> const &)` |
| 80.78 | `public: __thiscall vostok::render::render_cc_u32::render_cc_u32(char const *, enum vostok::render::enum_options_changes_result, char const *, unsigned int &, unsigned int &, unsigned int, unsigned int, bool, enum vostok::console_commands::command_type)` |
| 80.83 | `private: bool __thiscall survarium::weapon_core::hide_pred(void) const` |
| 80.83 | `public: __thiscall vostok::console_commands::cc_value<bool>::cc_value<bool>(char const *, bool &, bool, bool, bool, enum vostok::console_commands::command_type, enum vostok::console_commands::execution_filter)` |
| 80.90 | `public: __thiscall vostok::render::render_cc_bool::render_cc_bool(char const *, enum vostok::render::enum_options_changes_result, char const *, bool &, bool &, bool, enum vostok::console_commands::command_type)` |
| 80.92 | `public: virtual void __thiscall vostok::render::effect_downsample_reflective_shadow_map::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 81.24 | `public: void __thiscall survarium::weapon_core::instant_fire(unsigned int)` |
| 81.33 | `private: void __thiscall vostok::resources::query_result::on_refered_query_ended(class vostok::resources::query_result *)` |
| 81.34 | `public: __thiscall vostok::network::login_client::login_client(struct vostok::network::world &)` |
| 81.49 | `private: struct vostok::ui::text * __thiscall vostok::console_impl::get_item(void)` |
| 81.57 | `public: void __thiscall vostok::render::grass_patch::render(struct vostok::render::grass_world *, class vostok::render::renderer_context *, class vostok::math::float3const &, enum vostok::render::enum_render_stage_type, unsigned int, float, class vostok::render::res_effect *, unsigned int)` |
| 81.59 | `survarium::`dynamic initializer for 'bullet_tracer_exposition''` |
| 81.59 | `survarium::`dynamic initializer for 's_ik_foot_capsule_radius_cc''` |
| 81.78 | `public: __thiscall vostok::console_commands::cc_float::cc_float(char const *, float &, float, float, bool, enum vostok::console_commands::command_type, enum vostok::console_commands::execution_filter)` |
| 81.82 | `private: virtual void __thiscall survarium::booby_trap_set::remove(void)` |
| 81.87 | `public: virtual void __thiscall vostok::render::stage_postprocess::execute(void)` |
| 81.90 | `private: void __thiscall vostok::render::effect_manager::on_effects_recompiled(class vostok::vectora<struct vostok::render::effect_manager::effect_to_recompile_struct> *, class vostok::resources::queries_result &)` |
| 82.12 | `public: __thiscall vostok::fixed_string<24>::fixed_string<24>(class vostok::fixed_string<24> const &)` |
| 82.12 | `public: __thiscall vostok::fixed_string<260>::fixed_string<260>(class vostok::buffer_string const &)` |
| 82.12 | `public: __thiscall vostok::fixed_string<46>::fixed_string<46>(class vostok::fixed_string<46> const &)` |
| 82.22 | `public: virtual float __thiscall vostok::sound::world::get_speed_of_sound(void) const` |
| 82.39 | `public: void __thiscall survarium::booby_trap_set::on_trap_placed_message(unsigned char, class vostok::math::float3const &, class vostok::math::float3const &)` |
| 82.40 | `public: __thiscall vostok::vfs::async_callbacks_data::async_callbacks_data(enum vostok::vfs::async_callbacks_data::type_enum, struct vostok::vfs::find_environment const &)` |
| 82.58 | `public: virtual void __thiscall vostok::render::render_model::load_properties(class vostok::configs::binary_config_value const &)` |
| 82.69 | `public: virtual void __thiscall vostok::render::effect_debug_environment_probe_preview::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 82.69 | `public: virtual void __thiscall vostok::render::sky_default_material_effect::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 82.71 | `public: class vostok::fs_new::path_string_impl const & __thiscall vostok::fs_new::path_string_impl::append_with_conversion<char const *>(char const *const, char const *const)` |
| 82.75 | `public: virtual void __thiscall vostok::render::effect_olta::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 82.87 | `private: bool __thiscall vostok::resources::query_result::check_fat_for_resource_reusage(void)` |
| 82.91 | `public: virtual void __thiscall vostok::render::effect_copy_image::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.00 | `public: virtual void __thiscall vostok::render::effect_downsample_skin_irradiance_texture::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.00 | `public: virtual void __thiscall vostok::render::effect_post_process_fxaa::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.14 | `public: virtual void __thiscall vostok::render::effect_atmospheric_scattering::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.21 | `private: void __thiscall survarium::human_npc_cook::on_subresources_loaded(class vostok::resources::queries_result &, class survarium::human_npc *const)` |
| 83.24 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_final_managed_resource_if_needed(void)` |
| 83.29 | `public: virtual void __thiscall vostok::render::effect_system_line::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.36 | `public: virtual void __thiscall vostok::render::effect_decal_mask::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.58 | `public: virtual void __thiscall vostok::render::effect_fill_reflective_shadow_map::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.77 | `public: __thiscall vostok::render::hw_hiz_occlusion_manager::hw_hiz_occlusion_manager(bool, unsigned int, unsigned int)` |
| 83.79 | `public: virtual void __thiscall vostok::render::scr_quad_effect::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 83.81 | `public: __thiscall survarium::console_command_bind::console_command_bind(class survarium::key_binder *, int)` |
| 83.82 | `public: struct stlp_std::pair<class vostok::vfs::overlapped_node_initializer, class vostok::vfs::overlapped_node_initializer> __thiscall vostok::vfs::vfs_hashset::equal_range(char const *, enum vostok::vfs::lock_type_enum)` |
| 83.94 | `public: class vostok::render::res_texture * __thiscall vostok::render::resource_manager::create_texture3d(char const *, unsigned int, unsigned int, unsigned int, struct D3D11_SUBRESOURCE_DATA const *, enum DXGI_FORMAT, unsigned int, unsigned int)` |
| 84.00 | `public: bool __thiscall vostok::vfs::vfs_hashset::find_no_branch_lock(class vostok::vfs::base_node<1> *&, char const *, enum vostok::vfs::lock_type_enum, enum vostok::vfs::lock_operation_enum)` |
| 84.00 | `public: void __thiscall vostok::sound::sound_voice::stop(void)` |
| 84.20 | `public: virtual void __thiscall vostok::render::effect_apply_distortion::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.22 | `class vostok::math::float4x4 __cdecl vostok::animation::calculated_head_matrix(class vostok::math::float4x4const &, class vostok::math::float4x4const &)` |
| 84.26 | `private: void __thiscall survarium::weapon_core_cook::query_weapon_states(class vostok::resources::query_result_for_cook *const, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)` |
| 84.32 | `public: virtual void __thiscall vostok::render::effect_simple_fog::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.33 | `public: virtual void __thiscall vostok::render::effect_ssao_downsample_position_and_normal::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.41 | `public: void __thiscall survarium::player::remove(void)` |
| 84.44 | `void __cdecl vostok::fs_new::get_path_without_last_item<class vostok::fs_new::native_path_string>(class vostok::fs_new::native_path_string *, char const *)` |
| 84.44 | `void __cdecl vostok::fs_new::get_path_without_last_item<class vostok::fs_new::virtual_path_string>(class vostok::fs_new::virtual_path_string *, char const *)` |
| 84.45 | `public: virtual void __thiscall vostok::render::stage_ambient_lighting::execute(void)` |
| 84.62 | `private: void __thiscall vostok::render::static_model_instance_cook::on_subresources_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)` |
| 84.67 | `public: virtual void __thiscall vostok::render::effect_aberration::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.67 | `public: virtual void __thiscall vostok::render::effect_downsample_gbuffer::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.67 | `public: virtual void __thiscall vostok::render::effect_fix_irradiance_texture::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.67 | `public: virtual void __thiscall vostok::render::effect_read_cloud_base::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 84.79 | `survarium::fill_damage_model` |
| 84.88 | `public: void __thiscall survarium::game::create_lobby_menu(void)` |
| 84.88 | `public: void __thiscall survarium::game::create_login_menu(void)` |
| 84.92 | `public: virtual void __thiscall vostok::render::effect_apply_indirect_lighting::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 85.05 | `class vostok::collision::object * __cdecl vostok::collision::new_collision_object(class vostok::memory::base_allocator *, unsigned int, class vostok::collision::geometry_instance *, void *)` |
| 85.08 | `private: void __thiscall vostok::ui::ui_text_edit::init_internals(enum vostok::ui::enum_text_edit_mode)` |
| 85.34 | `public: virtual void __thiscall vostok::render::effect_light_mask::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 85.46 | `private: virtual void __thiscall vostok::render::depth_accumulate_material_effect::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 85.49 | `public: virtual void __thiscall vostok::render::effect_apply_decal::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 85.68 | `private: virtual void __thiscall survarium::weapon::instant_aim_end(void)` |
| 85.73 | `public: virtual void __thiscall vostok::render::effect_rain::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 85.83 | `public: __thiscall survarium::main_menu::main_menu(class survarium::game &)` |
| 85.85 | `private: void __thiscall survarium::body_part_parameters::apply_affects(class survarium::affects_threshold const *, unsigned int)` |
| 85.89 | `private: bool __thiscall survarium::weapon_core::AE_pred(void) const` |
| 86.00 | `public: virtual void __thiscall vostok::render::effect_ssao_filter4x4::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.00 | `public: virtual void __thiscall vostok::render::effect_environment_probe_lighting<1, 1, 0>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.04 | `public: virtual void __thiscall vostok::render::effect_gather_bloom::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.04 | `public: virtual void __thiscall vostok::render::effect_grass_trample::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.04 | `public: virtual void __thiscall vostok::render::effect_post_process_sraa::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.06 | `public: class vostok::sound::voice_bridge * __thiscall vostok::sound::voice_factory::new_voice(class vostok::sound::sound_voice *, unsigned char, unsigned int)` |
| 86.14 | `public: void __thiscall survarium::player::insert(bool)` |
| 86.24 | `public: virtual void __thiscall vostok::render::effect_system_ui::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.28 | `public: bool __thiscall vostok::variant<32>::try_get<struct vostok::render::static_model_instance_user_data>(struct vostok::render::static_model_instance_user_data &)` |
| 86.43 | `private: void __thiscall vostok::render::renderer_context_targets::create_targets(class vostok::math::uint2, bool)` |
| 86.45 | `public: virtual void __thiscall vostok::render::effect_forward_system::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
| 86.47 | `public: __thiscall survarium::game_material::game_material(void)` |
| 86.50 | `private: class survarium::weapon_core_chamber_a_round_aimed_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_chamber_a_round_aimed_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 86.50 | `private: class survarium::weapon_core_chamber_a_round_state * __thiscall survarium::weapon_core_state_cook_template<class survarium::weapon_core_chamber_a_round_state>::new_object(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)` |
| 86.56 | `public: virtual void __thiscall vostok::render::effect_environment_probe_lighting<0, 1, 1>::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)` |
- _...and 1138 more_

### Added (173)

- `[thunk]: __thiscall survarium::booby_trap_core::`vcall'{16, {flat}}`
- `[thunk]: __thiscall survarium::weapon_core::`vcall'{200, {flat}}`
- `[thunk]: __thiscall survarium::weapon_core_cook::`vcall'{36, {flat}}`
- `[thunk]: __thiscall vostok::network::world::`vcall'{4, {flat}}`
- `[thunk]: public: virtual struct vostok::ui::window * __thiscall vostok::ui::ui_text_edit::w(void)`
- `[thunk]: public: virtual void * __thiscall survarium::free_fly_camera::`vector deleting destructor'(unsigned int)`
- `[thunk]: public: virtual void * __thiscall vostok::ui::ui_text<struct vostok::ui::dynamic_text>::`vector deleting destructor'(unsigned int)`
- `[thunk]: public: virtual void * __thiscall vostok::ui::ui_text_edit::`vector deleting destructor'(unsigned int)`
- ``dynamic initializer for 's_net_client_account_name_cl''`
- ``dynamic initializer for 's_net_client_account_password_cl''`
- `float __cdecl survarium::chamber_a_round_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `float __cdecl survarium::computed_hide_animation_time_scale(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float)`
- `float __cdecl survarium::hide_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `float __cdecl survarium::show_timescale_calculator(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, struct survarium::weapon_state_creation_params const &)`
- `int __cdecl vostok::strings::compare(char const *, char const *)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char)`
- `private: bool __thiscall survarium::weapon_core::hide_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::idle_AE_or_show_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::show_AE_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::show_pred(void) const`
- `private: bool __thiscall survarium::weapon_core_shotgun_reload_state::player_wants_to_aim_predicate(void) const`
- `private: class vostok::math::float3 __thiscall survarium::weapon_core::get_dispersed_buckshot_direction(class vostok::math::float3const &)`
- `private: unsigned int __thiscall vostok::render::stage_lights::index_to_shadow_size(class vostok::render::light *, unsigned int) const`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual float __thiscall survarium::player::get_movement_speed_factor(void) const`
- `private: virtual void __thiscall survarium::booby_trap_set_core::remove_game_world_objects(void)`
- `private: virtual void __thiscall survarium::network_client::close_current_match(enum vostok::network_core::disconnect_event_types_enum)`
- `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::destroy_resource(class vostok::resources::unmanaged_resource *)`
- `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::destroy_resource(class vostok::resources::unmanaged_resource *)`
- `private: void __thiscall survarium::damage_zone_core::contact_test_body_parts(struct survarium::hit_receiver_info const &, class vostok::vectora<struct stlp_std::pair<class vostok::collision::bone_collision_data *, float> > &)`
- `private: void __thiscall survarium::network_client::remove_player(class vostok::network_core::packet_reader &)`
- `private: void __thiscall vostok::intrusive_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::set(class vostok::intrusive_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock> const &)`
- `private: void __thiscall vostok::render::resource_manager::log_texture_stats(void)`
- `private: void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::on_ogg_resources_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::query_converted_resources(class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall vostok::sound::single_sound_cook::on_sound_options_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall vostok::sound::single_sound_cook::on_sub_resources_loaded(class vostok::resources::queries_result &, float)`
- `private: void __thiscall vostok::sound::sound_scene::calculate_channel_matrix(unsigned char, class vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_instance_proxy_internal const &, class vostok::math::float3const &, float, float, float *const, float &) const`
- `private: void __thiscall vostok::sound::sound_scene::calculate_hdr_audio_frame(class vostok::vectora<class vostok::sound::new_sound_propagator *> &, unsigned int)`
- `private: void __thiscall vostok::sound::sound_scene::notify_listener(unsigned int)`
- `private: void __thiscall vostok::sound::sound_scene::notify_listener2(unsigned int)`
- `private: void __thiscall vostok::sound::sound_scene::process_fade(unsigned __int64)`
- `private: void __thiscall vostok::sound::sound_scene::x3daudio_calculate(class vostok::sound::sound_voice &)`
- `protected: __thiscall survarium::double_barreled_weapon_core_hide_state::double_barreled_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::double_barreled_weapon_core_show_state::double_barreled_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::pistol_weapon_core_hide_state::pistol_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::pistol_weapon_core_show_state::pistol_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::weapon_core_hide_state::weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::weapon_core_hide_state_base::weapon_core_hide_state_base(class survarium::weapon_core &)`
- `protected: __thiscall survarium::weapon_core_show_state::weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int)`
- `protected: __thiscall survarium::weapon_core_show_state_base::weapon_core_show_state_base(class survarium::weapon_core &)`
- `protected: bool __thiscall survarium::booby_trap_set_core::try_place_trap(class survarium::booby_trap_core &)`
- `protected: class survarium::booby_trap_core * __thiscall survarium::booby_trap_set_core::find_free_trap(void)`
- `protected: virtual void * __thiscall Scaleform::SysAllocBase::`vector deleting destructor'(unsigned int)`
- `protected: virtual void * __thiscall survarium::booby_trap_core::`vector deleting destructor'(unsigned int)`
- `public: __thiscall boost::function0<bool>::~function0<bool>(void)`
- `public: __thiscall survarium::body_part_parameters::body_part_parameters(char const *, float, float, float, float, bool, class survarium::damage_model &, unsigned char)`
- `public: __thiscall survarium::client_player_update::client_player_update(void)`
- `public: __thiscall survarium::player_state::player_state(void)`
- `public: __thiscall survarium::vector<class vostok::variant<32> >::vector<class vostok::variant<32> >(unsigned int)`
- `public: __thiscall survarium::vector<class vostok::variant<32> >::~vector<class vostok::variant<32> >(void)`
- `public: __thiscall vostok::buffer_vector<float>::buffer_vector<float>(void *, unsigned int, unsigned int)`
- `public: __thiscall vostok::fixed_string<128>::fixed_string<128>(void)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::particle::particle_action_billboard::particle_action_billboard(void)`
- `public: __thiscall vostok::render::effect_compiler::shader_cache_info::shader_cache_info(void)`
- `public: __thiscall vostok::render::render_target_instance::render_target_instance(void)`
- `public: __thiscall vostok::render::vs_data::~vs_data(void)`
- `public: __thiscall vostok::render::xs_descriptor<struct vostok::render::gs_data>::~xs_descriptor<struct vostok::render::gs_data>(void)`
- `public: __thiscall vostok::render::xs_descriptor<struct vostok::render::ps_data>::~xs_descriptor<struct vostok::render::ps_data>(void)`
- `public: __thiscall vostok::resources::resource_ptr<class vostok::physics::bt_collision_shape, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::physics::bt_collision_shape, class vostok::resources::unmanaged_intrusive_base>(class vostok::physics::bt_collision_shape *)`
- `public: __thiscall vostok::shared_string::~shared_string(void)`
- `public: __thiscall vostok::sound::new_sound_propagator::new_sound_propagator(enum vostok::sound::playback_mode, unsigned int, unsigned int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &)`
- `public: __thiscall vostok::sound::ogg_encoded_sound_interface::ogg_encoded_sound_interface(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float const *, unsigned int, unsigned int)`
- `public: __thiscall vostok::sound::single_sound::single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &, float)`
- `public: __thiscall vostok::sound::sound_voice::sound_voice(class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall vostok::sound::voice_factory::voice_factory(unsigned char *, unsigned int, class vostok::sound::sound_world &, struct vostok::sound::pool_parametrs const &)`
- `public: __thiscall vostok::threading::mutex::~mutex(void)`
- `public: __thiscall vostok::vectora_allocator<class vostok::fixed_vector<unsigned int, 32> >::ctor<void *>(class vostok::vectora_allocator<void *> const &)`
- `public: __thiscall vostok::vfs::query_mount_arguments::query_mount_arguments(class vostok::vfs::query_mount_arguments const &)`
- `public: bool __thiscall survarium::contacted_bones_comparator::operator()(struct stlp_std::pair<class vostok::collision::bone_collision_data *, float> const &, struct stlp_std::pair<class vostok::collision::bone_collision_data *, float> const &) const`
- `public: bool __thiscall vostok::intrusive_list<class vostok::particle::particle_emitter_instance, class vostok::particle::particle_emitter_instance *, 228, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::erase(class vostok::particle::particle_emitter_instance *)`
- `public: class vostok::render::effect_compiler & __thiscall vostok::render::effect_compiler::begin_pass(char const *, char const *, char const *, struct vostok::render::shader_configuration, struct vostok::render::shader_include_getter *)`
- `public: class vostok::sound::sound_voice * __thiscall vostok::sound::sound_world::create_sound_voice(class vostok::sound::sound_scene &, class vostok::sound::sound_instance_proxy_internal *, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: float __thiscall survarium::calc_distance_functor::operator()(class vostok::physics::base_physics_object *const &)`
- `public: float __thiscall vostok::sound::new_sound_propagator::get_sound_rms_value(void) const`
- `public: float __thiscall vostok::sound::new_sound_propagator::get_sound_spl_value(float) const`
- `public: float __thiscall vostok::sound::new_sound_propagator::get_sound_spl_value(void) const`
- `public: static union vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static union vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static union vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static void __cdecl vostok::render::resource_intrusive_base::destroy<class vostok::render::light>(class vostok::render::light const *const)`
- `public: struct stlp_std::pair<struct stlp_std::pair<struct vostok::render::texture_stats_key, unsigned int> *, bool> __thiscall associative_vector<struct vostok::render::texture_stats_key, unsigned int, class vostok::render::vector, struct stlp_std::less<struct vostok::render::texture_stats_key> >::insert(struct stlp_std::pair<struct vostok::render::texture_stats_key, unsigned int> const &)`
- `public: struct vostok::ai::brain_unit_cook_params & __thiscall vostok::ai::brain_unit_cook_params::operator=(struct vostok::ai::brain_unit_cook_params const &)`
- `public: unsigned char __thiscall survarium::damage_model::get_pain_health(void)`
- `public: unsigned int __thiscall vostok::render::options::get_cascaded_shadow_map_size(void) const`
- `public: virtual __thiscall survarium::animated_model_instance::~animated_model_instance(void)`
- `public: virtual __thiscall survarium::rifle_scope::~rifle_scope(void)`
- `public: virtual float __thiscall vostok::sound::composite_sound::get_sound_spl_value(void) const`
- `public: virtual float __thiscall vostok::sound::ogg_encoded_sound_interface::get_rms_by_time(unsigned __int64) const`
- `public: virtual float __thiscall vostok::sound::single_sound::get_sound_spl_value(void) const`
- `public: virtual int __thiscall survarium::game_world::input_priority(void)`
- `public: virtual void * __thiscall Scaleform::Render::TextureFormat::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall stlp_std::runtime_error::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::animated_model_instance::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::game_world_object::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::items_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::rifle_scope::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::victory_item::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::animation::animation_collection::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::console_impl::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage_translucency::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::resources::managed_resource::`vector deleting destructor'(unsigned int)`
- `public: virtual void __thiscall survarium::base_player::remove_game_world_objects(void)`
- `public: virtual void __thiscall survarium::game_world_ui::callback(struct survarium::flash_movie *, char const *, struct survarium::flash_value const *, unsigned int)`
- `public: virtual void __thiscall vostok::render::effect_environment_probe_index::compile(class vostok::render::effect_compiler &, class vostok::render::custom_config_value const &)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::allocate(void)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>::malloc_impl(unsigned int)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<536, class vostok::threading::multi_threading_policy>::malloc_impl(unsigned int)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>::malloc_impl(unsigned int)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>::malloc_impl(unsigned int)`
- `public: void __thiscall survarium::game_world::on_finish_match(void)`
- `public: void __thiscall survarium::game_world::set_match_stats_state(void)`
- `public: void __thiscall survarium::game_world_ui::initialize_resources(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: void __thiscall survarium::game_world_ui::show_cursor(bool)`
- `public: void __thiscall survarium::game_world_ui::show_match_stats_wnd(void)`
- `public: void __thiscall survarium::inventory::remove_game_world_objects(void)`
- `public: void __thiscall survarium::jump_logic::end_jump(void)`
- `public: void __thiscall survarium::jump_logic::start_jump(void)`
- `public: void __thiscall survarium::lobby_client::sell_item(unsigned int, unsigned int)`
- `public: void __thiscall survarium::std_allocator<class vostok::variant<32> >::deallocate(class vostok::variant<32> *, unsigned int) const`
- `public: void __thiscall vostok::ai::fsm::append_transition(struct vostok::ai::fsm_state *, struct vostok::ai::fsm_state *, class boost::function<bool __cdecl (void)> const &)`
- `public: void __thiscall vostok::ai::fsm::prepend_transition(struct vostok::ai::fsm_state *, struct vostok::ai::fsm_state *, class boost::function<bool __cdecl (void)> const &)`
- `public: void __thiscall vostok::buffer_vector<float>::push_back(float const &)`
- `public: void __thiscall vostok::buffer_vector<struct survarium::client_player_update>::push_back(struct survarium::client_player_update const &)`
- `public: void __thiscall vostok::intrusive_list<class vostok::particle::particle_emitter_instance, class vostok::particle::particle_emitter_instance *, 228, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::particle::particle_emitter_instance *, bool *)`
- `public: void __thiscall vostok::intrusive_list<struct vostok::ai::fsm_state_transition, struct vostok::ai::fsm_state_transition *, 36, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::push_front(struct vostok::ai::fsm_state_transition *, bool *)`
- `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_environment_probe_index>(class vostok::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)`
- `public: void __thiscall vostok::render::resource_manager::tick(void)`
- `public: void __thiscall vostok::render::shader_configuration::merge_with(char const *, struct vostok::render::shader_configuration)`
- `public: void __thiscall vostok::render::stage_ambient_lighting::make_probe_indices_map(class vostok::render::vector<struct vostok::render::environment_probe *> &)`
- `public: void __thiscall vostok::sound::new_sound_propagator::attach_voice(void)`
- `public: void __thiscall vostok::sound::new_sound_propagator::detach_voice(void)`
- `public: void __thiscall vostok::sound::sound_instance_proxy_internal::tick(class vostok::math::float3const &, unsigned int)`
- `public: void __thiscall vostok::sound::sound_scene::tick(unsigned int)`
- `public: void __thiscall vostok::sound::sound_voice::set_volume(float)`
- `public: void __thiscall vostok::sound::voice_bridge::set_volume(float)`
- `survarium::`dynamic atexit destructor for 's_movement_speed_factor_cc''`
- `survarium::`dynamic initializer for 's_movement_speed_factor_cc''`
- `survarium::arbitrary_right`
- `survarium::call_item_remove_game_world_objects`
- `void __cdecl `public: void __thiscall vostok::render::effect_manager::create_effect<class vostok::render::effect_environment_probe_index>(class render::resources::resource_ptr<class vostok::render::res_effect, class vostok::resources::unmanaged_intrusive_base> *)'::`2'::descriptor_object::`dynamic atexit destructor'(void)`
- `void __cdecl vostok::debug::platform::terminate(int, char const *)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy>, class vostok::sound::voice_bridge, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<32, class vostok::threading::single_threading_policy> &, class vostok::sound::voice_bridge *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy>, class vostok::sound::new_sound_propagator, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<84, class vostok::threading::single_threading_policy> &, class vostok::sound::new_sound_propagator *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy>, class vostok::sound::sound_voice, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<96, class vostok::threading::single_threading_policy> &, class vostok::sound::sound_voice *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::sound::test_ogg_query(void)`
- `void __cdecl vostok::sound::test_snd_loaded(class vostok::resources::queries_result &)`
- `vostok::render::`dynamic atexit destructor for 's_log_texture_stats_cc''`
- `vostok::render::`dynamic initializer for 's_log_texture_stats_cc''`
- `vostok::render::`dynamic initializer for 's_no_render_targets''`
- `vostok::render::format_name`
- `vostok::render::modify_shader_configuration`
- `vostok::sound::`dynamic atexit destructor for 's_test''`
- `vostok::sound::`dynamic initializer for 's_test''`

### Deleted (202)

- `[thunk]: __thiscall survarium::weapon_core::`vcall'{196, {flat}}`
- `[thunk]: public: virtual void * __thiscall survarium::damage_zone::`vector deleting destructor'(unsigned int)`
- `[thunk]: public: virtual void * __thiscall survarium::game_world::`vector deleting destructor'(unsigned int)`
- `[thunk]: public: virtual void * __thiscall survarium::weapon_core_fire_state::`vector deleting destructor'(unsigned int)`
- ``dynamic initializer for 's_no_level''`
- ``vostok::render::options::register_console_commands'::`2'::`dynamic atexit destructor for 'cascaded_shadow_map_size_cc''`
- ``vostok::render::options::register_console_commands'::`2'::`dynamic atexit destructor for 'num_max_light_instances_cc''`
- ``vostok::render::options::register_console_commands'::`2'::`dynamic atexit destructor for 'ssao_num_samples_cc''`
- ``vostok::render::options::register_console_commands'::`2'::`dynamic atexit destructor for 'update_shadows_every_frame_cc''`
- ``vostok::render::options::register_console_commands'::`2'::`dynamic atexit destructor for 'use_16bit_rt_cc''`
- ``vostok::render::options::register_console_commands'::`2'::`dynamic atexit destructor for 'use_god_rays_cc''`
- ``vostok::render::options::register_console_commands'::`2'::`dynamic atexit destructor for 'use_poisson_disc_shadow_filter_cc''`
- ``vostok::render::options::register_console_commands'::`2'::`dynamic atexit destructor for 'use_screenspace_reflections_mask_cc''`
- ``vostok::render::options::register_console_commands'::`2'::`dynamic atexit destructor for 'use_vegetation_trample_cc''`
- ``vostok::sound::sound_world::register_sound_cooks'::`2'::`dynamic atexit destructor for 's_ogg_file_contents_cook''`
- ``vostok::sound::sound_world::register_sound_cooks'::`2'::`dynamic atexit destructor for 's_ogg_sound_cook''`
- ``vostok::sound::sound_world::register_sound_cooks'::`2'::`dynamic atexit destructor for 's_ogg_source_cook''`
- ``vostok::sound::sound_world::register_sound_cooks'::`2'::`dynamic atexit destructor for 's_sound_environment_cook''`
- ``vostok::sound::sound_world::register_sound_cooks'::`2'::`dynamic atexit destructor for 's_wav_encoded_sound_interface_cook''`
- `class vostok::animation::mixing::addition_lexeme & __cdecl vostok::animation::mixing::operator+<class vostok::animation::mixing::animation_lexeme, class vostok::animation::mixing::animation_lexeme>(class vostok::animation::mixing::animation_lexeme &, class vostok::animation::mixing::animation_lexeme &)`
- `float __cdecl survarium::computed_reload_animation_time_scale(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &, float)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: __thiscall survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>::weapon_sound_events_handler_state<class survarium::weapon_core_show_state>(class survarium::weapon &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, bool, unsigned char, bool &)`
- `private: bool __thiscall survarium::weapon_core::idle_AE_or_chamber_a_round_break_pred(void) const`
- `private: bool __thiscall survarium::weapon_core::not_inactive_pred(void) const`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::config_params const &)`
- `private: class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> * __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::new_state(class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *const, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *const, unsigned char, void *const, unsigned char, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::config_params const &)`
- `private: class vostok::sound::sound_voice * __thiscall vostok::sound::new_sound_propagator::attach_voice(unsigned int)`
- `private: struct IXAudio2SubmixVoice * __thiscall vostok::sound::sound_scene::create_environment_submix_voice(class vostok::sound::sound_world const &) const`
- `private: unsigned int __thiscall vostok::render::stage_lights::index_to_shadow_size(unsigned int) const`
- `private: virtual bool __thiscall survarium::weapon_core_hide_state_base::is_ready_for_transition(void) const`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual class vostok::mutable_buffer __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)`
- `private: virtual void __thiscall survarium::network_client::close_current_match(bool)`
- `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::destroy_resource(class vostok::resources::unmanaged_resource *)`
- `private: virtual void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::destroy_resource(class vostok::resources::unmanaged_resource *)`
- `private: void __thiscall vostok::intrusive_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base, class vostok::threading::simple_lock>::set(class vostok::resources::managed_resource *)`
- `private: void __thiscall vostok::intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::set(class vostok::intrusive_ptr<class vostok::sound::encoded_sound_interface, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock> const &)`
- `private: void __thiscall vostok::sound::new_sound_propagator::attach_voices(unsigned int, class vostok::vectora<struct vostok::sound::sound_voice_params> const &)`
- `private: void __thiscall vostok::sound::new_sound_propagator::detach_voice(class vostok::sound::sound_voice *)`
- `private: void __thiscall vostok::sound::new_sound_propagator::detach_voices(unsigned int)`
- `private: void __thiscall vostok::sound::new_sound_propagator::set_voice_channel_matrix(class vostok::sound::sound_voice *, float const *, float)`
- `private: void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall vostok::sound::ogg_file_contents_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall vostok::sound::ogg_sound_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall vostok::sound::ogg_source_cook::on_ogg_file_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)`
- `private: void __thiscall vostok::sound::single_sound_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall vostok::sound::sound_environment_cook::on_environment_options_loaded(class vostok::resources::queries_result &, class vostok::math::float4x4*)`
- `private: void __thiscall vostok::sound::sound_environment_cook::on_model_config_loaded(class vostok::resources::queries_result &)`
- `private: void __thiscall vostok::sound::sound_scene::calculate_channel_matrix(class vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::sound::sound_instance_proxy_internal const &, class vostok::math::float3const &, float, float, float *, float &) const`
- `private: void __thiscall vostok::sound::sound_scene::calculate_in_graph_position(class vostok::math::float3const &)`
- `private: void __thiscall vostok::sound::sound_scene::notify_listener(class vostok::sound::sound_world const &)`
- `private: void __thiscall vostok::sound::sound_scene::process_fade(class vostok::sound::sound_world &, unsigned __int64)`
- `private: void __thiscall vostok::sound::sound_scene::x3daudio_calculate(class vostok::sound::sound_world const &, class vostok::sound::sound_voice &)`
- `private: void __thiscall vostok::sound::sound_world::try_delete_stoping_voices(void)`
- `private: void __thiscall vostok::sound::wav_encoded_sound_interface::read_riff(void)`
- `private: void __thiscall vostok::sound::wav_encoded_sound_interface_cook::on_file_loaded(class vostok::resources::queries_result &)`
- `protected: __thiscall survarium::double_barreled_weapon_core_hide_state::double_barreled_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::double_barreled_weapon_core_show_state::double_barreled_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::pistol_weapon_core_hide_state::pistol_weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::pistol_weapon_core_show_state::pistol_weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::weapon_core_hide_state::weapon_core_hide_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::weapon_core_hide_state_base::weapon_core_hide_state_base(class survarium::weapon_core &, bool &)`
- `protected: __thiscall survarium::weapon_core_show_state::weapon_core_show_state(class survarium::weapon_core &, float, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const *, unsigned int, bool &)`
- `protected: __thiscall survarium::weapon_core_show_state_base::weapon_core_show_state_base(class survarium::weapon_core &, bool &)`
- `protected: class vostok::resources::resource_ptr<class survarium::booby_trap_core, class vostok::resources::unmanaged_intrusive_base> * __thiscall survarium::booby_trap_set_core::try_place_trap(void)`
- `protected: virtual void __thiscall survarium::booby_trap_set_core::remove(void)`
- `public: __thiscall Scaleform::Render::Color::Color(class Scaleform::Render::Color const &)`
- `public: __thiscall boost::intrusive::set_member_hook<struct boost::intrusive::link_mode<2>, struct boost::intrusive::none, struct boost::intrusive::none, struct boost::intrusive::none>::~set_member_hook<struct boost::intrusive::link_mode<2>, struct boost::intrusive::none, struct boost::intrusive::none, struct boost::intrusive::none>(void)`
- `public: __thiscall survarium::body_part_parameters::body_part_parameters(char const *, float, float, float, bool, class survarium::damage_model &, unsigned char)`
- `public: __thiscall vostok::buffer_vector<class vostok::variant<32> const *>::buffer_vector<class vostok::variant<32> const *>(void *, unsigned int, unsigned int)`
- `public: __thiscall vostok::fixed_string<256>::fixed_string<256>(void)`
- `public: __thiscall vostok::fixed_string<64>::fixed_string<64>(class vostok::fixed_string<64> const &)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>(void *, unsigned int)`
- `public: __thiscall vostok::particle::curve_line_ranged_float::curve_line_ranged_float(void)`
- `public: __thiscall vostok::render::cascaded_sun_shadow_statistics_group::~cascaded_sun_shadow_statistics_group(void)`
- `public: __thiscall vostok::render::debug_statistics_group::~debug_statistics_group(void)`
- `public: __thiscall vostok::render::lpv_statistics_group::~lpv_statistics_group(void)`
- `public: __thiscall vostok::render::particles_statistics_group::~particles_statistics_group(void)`
- `public: __thiscall vostok::render::visibility_statistics_group::~visibility_statistics_group(void)`
- `public: __thiscall vostok::resources::resource_ptr<class survarium::game_world_object, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class survarium::game_world_object, class vostok::resources::unmanaged_intrusive_base>(class survarium::game_world_object *)`
- `public: __thiscall vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::sound::panning_lut, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall vostok::sound::effect_cross_fader::effect_cross_fader(class vostok::sound::sound_scene &, unsigned int, struct IXAudio2SubmixVoice *, struct IXAudio2SubmixVoice *)`
- `public: __thiscall vostok::sound::new_sound_propagator::new_sound_propagator(class vostok::math::float3const &, class vostok::math::float3const &, enum vostok::sound::playback_mode, unsigned int, unsigned int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &)`
- `public: __thiscall vostok::sound::ogg_encoded_sound_interface::ogg_encoded_sound_interface(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `public: __thiscall vostok::sound::ogg_file_contents::ogg_file_contents(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `public: __thiscall vostok::sound::ogg_file_contents_cook::ogg_file_contents_cook(void)`
- `public: __thiscall vostok::sound::ogg_sound::ogg_sound(class vostok::resources::resource_ptr<class vostok::sound::ogg_file_contents, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> const &)`
- `public: __thiscall vostok::sound::ogg_sound_cook::ogg_sound_cook(void)`
- `public: __thiscall vostok::sound::ogg_source_cook::ogg_source_cook(void)`
- `public: __thiscall vostok::sound::single_sound::single_sound(class vostok::resources::resource_ptr<class vostok::sound::encoded_sound_with_qualities, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall vostok::sound::sound_environment::sound_environment(unsigned int)`
- `public: __thiscall vostok::sound::sound_environment_cook::sound_environment_cook(void)`
- `public: __thiscall vostok::sound::sound_voice::sound_voice(int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal &, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: __thiscall vostok::sound::unique_propagator_info::unique_propagator_info(void)`
- `public: __thiscall vostok::sound::voice_factory::voice_factory(unsigned char *, unsigned int, class vostok::sound::sound_world const &, struct vostok::sound::pool_parametrs const &)`
- `public: __thiscall vostok::sound::wav_encoded_sound_interface::wav_encoded_sound_interface(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base>)`
- `public: __thiscall vostok::sound::wav_encoded_sound_interface_cook::wav_encoded_sound_interface_cook(void)`
- `public: __thiscall vostok::vectora_allocator<struct vostok::sound::propagator_info>::ctor<void *>(class vostok::vectora_allocator<void *> const &)`
- `public: bool __thiscall survarium::body_part_parameters::can_affect_death(void)`
- `public: bool __thiscall survarium::player_input_handler::alt_is_held(void) const`
- `public: bool __thiscall survarium::weapon_core_base_state::has_animation_ended(void) const`
- `public: bool __thiscall vostok::intrusive_list<class vostok::particle::particle_emitter_instance, class vostok::particle::particle_emitter_instance *, 224, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::erase(class vostok::particle::particle_emitter_instance *)`
- `public: bool __thiscall vostok::intrusive_list<class vostok::sound::sound_voice, class vostok::sound::sound_voice *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::erase(class vostok::sound::sound_voice *)`
- `public: bool __thiscall vostok::sound::sound_voice::can_be_deleted(void) const`
- `public: class vostok::intrusive_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock> & __thiscall vostok::intrusive_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock>::operator=(class vostok::intrusive_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base, class vostok::threading::simple_lock> const &)`
- `public: class vostok::render::effect_compiler & __thiscall vostok::render::effect_compiler::begin_pass(char const *, char const *, char const *, struct vostok::render::shader_configuration const &, struct vostok::render::shader_include_getter *)`
- `public: class vostok::sound::sound_environment * __thiscall vostok::sound::sound_scene::get_current_environment(void)`
- `public: class vostok::sound::sound_voice * __thiscall vostok::sound::sound_world::create_sound_voice(class vostok::sound::sound_scene &, int, unsigned int, unsigned int, class vostok::sound::sound_instance_proxy_internal *, class vostok::sound::sound_propagator_emitter const &, class vostok::resources::resource_ptr<class vostok::sound::sound_spl, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: float __thiscall vostok::animation::cubic_spline_skeleton_animation::length_in_frames(void) const`
- `public: float __thiscall vostok::sound::sound_spl::get_loudness(float) const`
- `public: static union vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static union vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static union vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::node * __cdecl vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::node>::allocate(class vostok::memory::single_threading_single_size_allocator_policy<union vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::node>::free_list_type &)`
- `public: static unsigned int __cdecl vostok::detail::type_to_int<struct vostok::particle::world *>::get(void)`
- `public: struct IXAudio2SubmixVoice * __thiscall vostok::sound::sound_scene::get_current_effect_submix(void)`
- `public: struct XAUDIO2FX_REVERB_I3DL2_PARAMETERS * __thiscall vostok::sound::sound_scene::get_environment_params(char const *)`
- `public: struct XAUDIO2FX_REVERB_I3DL2_PARAMETERS * __thiscall vostok::sound::sound_scene::get_environment_params(unsigned int)`
- `public: struct vostok::particle::world & __thiscall vostok::render::engine::world::particle_world(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: struct vostok::particle::world & __thiscall vostok::render::scene_renderer::particle_world(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: unsigned char __thiscall survarium::damage_model::get_total_health(void)`
- `public: unsigned int __thiscall vostok::sound::ogg_file_contents::decompress(unsigned char *, unsigned int, unsigned int &, unsigned int)`
- `public: unsigned int __thiscall vostok::sound::sound_scene::get_environment_params_id(char const *)`
- `public: virtual __thiscall vostok::ai::selectors::sound_target_selector::~sound_target_selector(void)`
- `public: virtual __thiscall vostok::resources::fs_task_unmount::~fs_task_unmount(void)`
- `public: virtual __thiscall vostok::sound::ogg_file_contents::~ogg_file_contents(void)`
- `public: virtual __thiscall vostok::sound::ogg_file_contents_cook::~ogg_file_contents_cook(void)`
- `public: virtual __thiscall vostok::sound::ogg_sound::~ogg_sound(void)`
- `public: virtual __thiscall vostok::sound::ogg_sound_cook::~ogg_sound_cook(void)`
- `public: virtual __thiscall vostok::sound::sound_environment::~sound_environment(void)`
- `public: virtual __thiscall vostok::sound::wav_encoded_sound_interface::~wav_encoded_sound_interface(void)`
- `public: virtual __thiscall vostok::sound::wav_encoded_sound_interface_cook::~wav_encoded_sound_interface_cook(void)`
- `public: virtual class vostok::detail::abstract_type_helper * __thiscall vostok::detail::concrete_type_helper<struct vostok::particle::world *>::copy_helper(class vostok::mutable_buffer)`
- `public: virtual unsigned int __thiscall vostok::sound::wav_encoded_sound_interface::decompress(unsigned char *, unsigned int, unsigned int &, unsigned int)`
- `public: virtual void * __thiscall Scaleform::Render::MappedTextureBase::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall btClosestNotMeConvexResultCallback::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::damage_zone::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::generic_anomaly::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::ladder_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::player_input_handler::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::weapon_core_fire_state::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::weapon_core_shotgun_reload_start_substate::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::console_commands::cc_u32::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::memory::managed_node_owner::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::particle::particle_system_wrapper_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage_forward::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::resources::fs_task_unmount::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::sound::ogg_file_contents::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::sound::ogg_file_contents_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::sound::ogg_sound::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::sound::ogg_sound_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::sound::sound_environment::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::sound::wav_encoded_sound_interface::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::sound::wav_encoded_sound_interface_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void __thiscall vostok::sound::ogg_file_contents_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::ogg_file_contents_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall vostok::sound::ogg_sound_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::ogg_sound_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall vostok::sound::ogg_source_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::ogg_source_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall vostok::sound::sound_environment_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::sound_environment_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: virtual void __thiscall vostok::sound::wav_encoded_sound_interface_cook::delete_resource(class vostok::resources::resource_base *)`
- `public: virtual void __thiscall vostok::sound::wav_encoded_sound_interface_cook::translate_query(class vostok::resources::query_result_for_cook &)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>::allocate(void)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>::malloc_impl(unsigned int)`
- `public: void * __thiscall vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>::allocate(void)`
- `public: void __thiscall survarium::game_world_ui::initialize_resources(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)`
- `public: void __thiscall survarium::std_allocator<struct survarium::base_project::resolve_link_object>::deallocate(struct survarium::base_project::resolve_link_object *, unsigned int) const`
- `public: void __thiscall vostok::ai::fsm::add_transition(struct vostok::ai::fsm_state *, struct vostok::ai::fsm_state *, class boost::function<bool __cdecl (void)> const &)`
- `public: void __thiscall vostok::intrusive_list<class vostok::particle::particle_emitter_instance, class vostok::particle::particle_emitter_instance *, 224, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::particle::particle_emitter_instance *, bool *)`
- `public: void __thiscall vostok::intrusive_list<class vostok::sound::sound_voice, class vostok::sound::sound_voice *, 0, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::sound::sound_voice *, bool *)`
- `public: void __thiscall vostok::render::grass_patch::try_accumulate_trample(struct vostok::render::trample_desc &, struct vostok::render::grass_world *, class vostok::render::renderer *, class vostok::render::renderer_context *)`
- `public: void __thiscall vostok::render::scene::build_lpv_geometry(void)`
- `public: void __thiscall vostok::sound::effect_cross_fader::tick(unsigned int, class vostok::sound::sound_environment *)`
- `public: void __thiscall vostok::sound::new_sound_propagator::distribute_voices(unsigned int, class vostok::vectora<struct vostok::sound::sound_voice_params> const &)`
- `public: void __thiscall vostok::sound::sound_instance_proxy_internal::tick(unsigned int)`
- `public: void __thiscall vostok::sound::sound_scene::add_environment_params(char const *, struct XAUDIO2FX_REVERB_I3DL2_PARAMETERS *, unsigned int &)`
- `public: void __thiscall vostok::sound::sound_scene::insert_environment(class vostok::sound::sound_environment &, class vostok::math::float4x4const &)`
- `public: void __thiscall vostok::sound::sound_scene::tick(class vostok::sound::sound_world &, unsigned int)`
- `public: void __thiscall vostok::sound::voice_bridge::set_channel_volumes(unsigned char, float const *)`
- `public: void __thiscall vostok::sound::voice_bridge::set_sample_rate(unsigned int)`
- `public: void __thiscall vostok::variant<32>::set<struct vostok::render::static_model_instance_user_data>(struct vostok::render::static_model_instance_user_data const &)`
- `void __cdecl vostok::debug::platform::terminate(char const *, int)`
- `void __cdecl vostok::memory::delete_helper<class vostok::memory::doug_lea_allocator, class vostok::render::light const>(class vostok::memory::doug_lea_allocator &, class vostok::render::light const *&)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::doug_lea_allocator, class vostok::math::float4x4, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::doug_lea_allocator &, class vostok::math::float4x4*&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::doug_lea_allocator, struct vostok::sound::propagator_statistic, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::doug_lea_allocator &, struct vostok::sound::propagator_statistic *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy>, class vostok::sound::new_sound_propagator, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<108, class vostok::threading::single_threading_policy> &, class vostok::sound::new_sound_propagator *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy>, class vostok::sound::sound_voice, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<136, class vostok::threading::single_threading_policy> &, class vostok::sound::sound_voice *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `void __cdecl vostok::memory::detail::delete_helper_impl<class vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy>, class vostok::sound::voice_bridge, struct vostok::memory::detail::call_destructor_predicate>(class vostok::memory::single_size_buffer_allocator<28, class vostok::threading::single_threading_policy> &, class vostok::sound::voice_bridge *&, struct vostok::memory::detail::call_destructor_predicate const &)`
- `vostok::sound::compare_propagator_info_by_distance`

---

## v0.1.1c-build870 → v0.1.1e-build884
_2013-05-24 → 2013-05-28 · +47 / -58 / ~514_

### Changed (514)

| match % | function |
| ---: | --- |
| 0.00 | `[thunk]: __thiscall vostok::engine_user::world::`vcall'{20, {flat}}` |
| 0.00 | `[thunk]: __thiscall vostok::network::world::`vcall'{0, {flat}}` |
| 0.00 | `[thunk]: __thiscall vostok::sound::world::`vcall'{12, {flat}}` |
| 0.00 | `[thunk]: private: virtual char const * __thiscall vostok::engine::engine_world::get_resources_path(void) const` |
| 0.00 | `[thunk]: private: virtual void __thiscall vostok::engine::engine_world::enter_editor_mode(void)` |
| 0.00 | `[thunk]: public: virtual int __thiscall vostok::engine::engine_world::get_exit_code(void) const` |
| 0.00 | `[thunk]: public: virtual void * __thiscall vostok::engine::engine_world::`vector deleting destructor'(unsigned int)` |
| 0.00 | `[thunk]: public: virtual void __thiscall vostok::engine::engine_world::exit(int)` |
| 0.00 | `[thunk]: public: virtual void __thiscall vostok::engine::engine_world::set_exit_code(int)` |
| 0.00 | `empty_stub` |
| 0.00 | `long __cdecl vostok::threading::interlocked_decrement(long volatile &)` |
| 0.00 | `long __cdecl vostok::threading::interlocked_increment(long volatile &)` |
| 0.00 | `private: virtual void * __thiscall survarium::booby_trap::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: __thiscall boost::function0<bool>::~function0<bool>(void)` |
| 0.00 | `public: __thiscall boost::function1<void, class vostok::vfs::vfs_iterator &>::~function1<void, class vostok::vfs::vfs_iterator &>(void)` |
| 0.00 | `public: __thiscall btSoftBody::Body::Body(void)` |
| 0.00 | `public: __thiscall vostok::ai::pre_perceptors_filter::~pre_perceptors_filter(void)` |
| 0.00 | `public: __thiscall vostok::animation::mixing::animation_interval::~animation_interval(void)` |
| 0.00 | `public: __thiscall vostok::intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::~intrusive_list<struct vostok::ai::percept_memory_object, struct vostok::ai::percept_memory_object *, 40, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>(void)` |
| 0.00 | `public: __thiscall vostok::network::order::order(void)` |
| 0.00 | `public: __thiscall vostok::one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >::~one_way_threads_channel<class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4>, class vostok::intrusive_spsc_queue<class vostok::network::order, class vostok::network::order, 4> >(void)` |
| 0.00 | `public: __thiscall vostok::render::skeleton_combined_cook_data::~skeleton_combined_cook_data(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::render::material, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> const &)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(class vostok::resources::unmanaged_resource *)` |
| 0.00 | `public: __thiscall vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>::~resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base>(void)` |
| 0.00 | `public: __thiscall vostok::vectora<struct vostok::resources::request>::~vectora<struct vostok::resources::request>(void)` |
| 0.00 | `public: __thiscall vostok::vfs::query_mount_arguments::~query_mount_arguments(void)` |
| 0.00 | `public: class survarium::inventory & __thiscall survarium::inventory_holder::inventory(void)` |
| 0.00 | `public: class vostok::buffer_string const & __thiscall vostok::buffer_string::operator=(class vostok::buffer_string const &)` |
| 0.00 | `public: class vostok::vfs::query_mount_arguments & __thiscall vostok::vfs::query_mount_arguments::operator=(class vostok::vfs::query_mount_arguments const &)` |
| 0.00 | `public: enum survarium::profile_slot_enum __thiscall survarium::inventory::get_active_slot(void) const` |
| 0.00 | `public: virtual __thiscall survarium::inventory_cook::~inventory_cook(void)` |
| 0.00 | `public: virtual __thiscall vostok::console_commands::cc_u32::~cc_u32(void)` |
| 0.00 | `public: virtual bool __thiscall Scaleform::MemoryFile::Flush(void)` |
| 0.00 | `public: virtual void * __thiscall survarium::damage_protector::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::empty_hands::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::flash_external_handler::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::jump_logic_base_state::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::lobby_camera::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall survarium::player_cook::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::behaviour::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::brain_unit::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::selectors::enemy_target_selector::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::ai::sensors::smell_sensor::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::animation::mixing::addition_lexeme::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::collision::aabb_object::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::collision::box_geometry_instance::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::detail::abstract_type_helper::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::network::functor_order::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::network::functor_response::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::network::string_response::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::base_scene::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::effect_sun::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::grass_world::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::render_model_instance_impl::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::render_surface::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::speedtree_instance::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::render::speedtree_tree_component::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::sound::sound_collection::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void * __thiscall vostok::sound::sound_spl_cook::`vector deleting destructor'(unsigned int)` |
| 0.00 | `public: virtual void __thiscall survarium::game_camera::on_focus(bool)` |
| 0.00 | `vec_begin` |
| 0.00 | `vostok::animation::`dynamic initializer for 'zero''` |
| 2.05 | `public: void __thiscall vostok::render::system_renderer::draw_screen_lines(class vostok::math::float3const *, unsigned int, class vostok::math::color const &, float, unsigned int, bool, bool)` |
| 12.00 | ``vostok::math::curve_line_points<float,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float3_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,0>::sort_points_by_time'::`5'::predicate::compare` |
| 12.00 | ``vostok::math::curve_line_points<vostok::math::float4_pod,1>::sort_points_by_time'::`5'::predicate::compare` |
| 12.77 | `public: bool __thiscall vostok::render::remove_inappropriate_models::operator()(struct vostok::render::render_surface_instance *)` |
| 13.45 | `vostok::render::screen_factor` |
| 33.66 | `private: __thiscall survarium::medkit::medkit(void)` |
| 53.74 | `public: void __thiscall vostok::resources::resources_manager::init_new_query(class vostok::resources::query_result &)` |
| 57.50 | `public: void __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::resources::query_result *, bool *)` |
| 60.23 | `public: virtual __thiscall vostok::resources::query_result_for_user::~query_result_for_user(void)` |
| 63.37 | `private: virtual void __thiscall survarium::network_client::close_current_match(enum vostok::network_core::disconnect_event_types_enum)` |
| 73.70 | `public: virtual float __thiscall survarium::dz_bone_data_contact_test_predicate::add_single_result(void *, enum vostok::physics::primitive_type, class vostok::math::float4x4const &, class vostok::math::float3const &, enum vostok::physics::primitive_type, class vostok::math::float4x4const &, class vostok::math::float3const &)` |
| 77.34 | `private: void __thiscall vostok::render::device::create_d3d(void)` |
| 79.82 | `public: void __thiscall survarium::lobby_menu::on_player_reputations_arrived(void)` |
| 83.83 | `private: void __thiscall survarium::application::preinitialize(void)` |
| 84.42 | `public: virtual void __thiscall vostok::render::stage_postprocess::execute(void)` |
| 85.24 | `public: virtual void __thiscall vostok::render::stage_shadow_direct::execute(void)` |
| 89.17 | `public: __thiscall vostok::resources::query_result_for_user::query_result_for_user(void)` |
| 90.08 | `public: __thiscall vostok::render::renderer_context::~renderer_context(void)` |
| 90.10 | `public: enum vostok::render::enum_options_changes_result __thiscall vostok::render::options::end_render_options_changing(class vostok::render::vector<class vostok::fs_new::virtual_path_string> &)` |
| 91.57 | `private: void __thiscall vostok::render::game::renderer::draw_scene_impl(struct vostok::render::game::renderer::draw_scene_params const &)` |
| 92.68 | `public: __thiscall vostok::render::renderer_context::renderer_context(void)` |
| 93.24 | `private: virtual __thiscall survarium::medkit::~medkit(void)` |
| 93.40 | `public: void __thiscall vostok::render::engine::world::draw_scene(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::rectangle<class vostok::math::float2> const &, class boost::function<void __cdecl (bool)> const &, struct vostok::ui::font const *)` |
| 94.75 | `public: void __thiscall vostok::render::renderer::render(class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> const &, class vostok::math::rectangle<class vostok::math::float2> const &, class boost::function<void __cdecl (bool)> const &, bool, struct vostok::ui::font const *)` |
| 95.08 | `public: void __thiscall vostok::render::options::set_default_values(void)` |
| 95.41 | `private: void __thiscall survarium::player::detect_usable_objects(unsigned int)` |
| 95.56 | `public: void __thiscall vostok::render::options::register_console_commands(void)` |
| 95.99 | `public: void __thiscall vostok::render::system_renderer::draw_ui_vertices(struct vostok::render::vertex_formats::TL const *, unsigned int const &, int, int)` |
| 96.25 | `public: void __thiscall vostok::render::render_particle_emitter_instance::draw_debug(class vostok::math::float4x4const &, enum vostok::particle::enum_particle_render_mode)` |
| 97.23 | `public: void __thiscall vostok::resources::resources_manager::init_new_queries(class vostok::resources::query_result *)` |
| 98.57 | `public: void __thiscall survarium::game_world_ui::set_match_time(unsigned int)` |
| 99.01 | `private: void __thiscall vostok::render::device::create(void)` |
| 99.38 | `private: void __thiscall vostok::render::renderer_context::update_near_far(void)` |
| 99.44 | `public: __thiscall vostok::resources::query_result_for_cook::query_result_for_cook(class vostok::resources::queries_result *)` |
| 99.50 | `private: void __thiscall vostok::resources::query_result::add_loaded_bytes(unsigned int)` |
| 99.50 | `public: class vostok::render::scene_view * __thiscall vostok::render::renderer_context::get_scene_view(void)` |
| 99.50 | `public: class vostok::render::scene_view const * __thiscall vostok::render::renderer_context::scene_view(void) const` |
| 99.50 | `public: void __thiscall vostok::render::renderer_context::set_scene(class vostok::render::scene *)` |
| 99.50 | `public: void __thiscall vostok::resources::query_result_for_cook::set_out_of_memory(class vostok::resources::memory_type &, unsigned int)` |
| 99.54 | `private: void __thiscall vostok::resources::query_result::clear_reference(void)` |
| 99.60 | `public: void __thiscall vostok::render::renderer_context::reset_matrices(void)` |
| 99.62 | `public: __thiscall vostok::resources::query_result::query_result(unsigned short, class vostok::resources::queries_result *, class vostok::memory::base_allocator *, unsigned int, float, bool, unsigned int, enum vostok::resources::query_type_enum, enum vostok::resources::autoselect_quality_bool)` |
| 99.67 | `public: class vostok::resources::query_result_for_cook * __thiscall vostok::resources::query_result_for_cook::get_parent_query(void) const` |
| 99.67 | `public: class vostok::resources::query_result_for_user const & __thiscall vostok::resources::queries_result::operator[](unsigned int) const` |
| 99.68 | `public: void __thiscall vostok::render::renderer_context::update_eye_rays(void)` |
| 99.69 | `public: __thiscall vostok::render::stage_light_propagation_volumes::stage_light_propagation_volumes(class vostok::render::renderer *, class vostok::render::renderer_context *)` |
| 99.73 | `private: void __thiscall vostok::resources::query_result::prepare_requery(void)` |
| 99.73 | `public: class vostok::math::float4x4const & __thiscall vostok::render::renderer_context::get_view2shadow(unsigned int) const` |
| 99.75 | `private: void __thiscall vostok::resources::query_result::increase_query_end_guard(void)` |
| 99.75 | `private: void __thiscall vostok::resources::query_result::on_observed_resource_destroyed(char const *)` |
| 99.75 | `public: class vostok::resources::query_result_for_user & __thiscall vostok::resources::queries_result::operator[](unsigned int)` |
| 99.78 | `private: bool __thiscall vostok::resources::query_result::ready_to_retry_action_that_caused_out_of_memory(void)` |
| 99.79 | `public: __thiscall singletons_on_initialize::singletons_on_initialize(void)` |
| 99.80 | `private: unsigned int __thiscall vostok::resources::query_result::decrease_query_end_guard(void)` |
| 99.80 | `public: bool __thiscall vostok::resources::query_result_for_cook::is_autoselect_quality_query(void) const` |
| 99.80 | `public: virtual class vostok::mutable_buffer __thiscall vostok::resources::vfs_sub_fat_cook::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 99.81 | `public: void __thiscall vostok::render::renderer_context::push_set_p(class vostok::math::float4x4const &)` |
| 99.82 | `private: bool __thiscall vostok::resources::queries_result::quality_loaded(unsigned int)` |
| 99.82 | `private: void __thiscall vostok::resources::query_result::requery(void)` |
| 99.82 | `public: virtual void __thiscall vostok::resources::vfs_sub_fat_cook::create_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, class vostok::mutable_buffer)` |
| 99.83 | `private: void __thiscall vostok::resources::query_result::observe_resource_destruction(class vostok::resources::resource_base *)` |
| 99.83 | `private: void __thiscall vostok::resources::query_result::set_flag(unsigned int)` |
| 99.83 | `public: bool __thiscall vostok::resources::query_result_for_cook::is_helper_query_for_mount(void) const` |
| 99.83 | `public: void __thiscall vostok::render::renderer_context::clear_resources(void)` |
| 99.85 | `public: void __thiscall vostok::render::temporal_projection_matrix_modifier::pop_jittering(void)` |
| 99.86 | `private: bool __thiscall vostok::resources::game_resources_manager::try_reallocate_queue_front(class vostok::resources::memory_type *)` |
| 99.86 | `public: void __thiscall vostok::render::renderer::clear_resources(void)` |
| 99.87 | `private: void __thiscall vostok::resources::query_result::propogate_sub_fats_to_resources(void)` |
| 99.87 | `private: void __thiscall vostok::resources::query_result::init_save(class vostok::resources::save_generated_data *, class vostok::resources::query_result *)` |
| 99.87 | `public: void __thiscall vostok::render::renderer_context::set_v(class vostok::math::float4x4const &)` |
| 99.88 | `private: void __thiscall vostok::resources::query_result::unset_flag(unsigned int)` |
| 99.88 | `public: virtual __thiscall vostok::resources::query_result_for_cook::~query_result_for_cook(void)` |
| 99.88 | `public: void __thiscall vostok::render::engine::world::clear_resources(void)` |
| 99.88 | `public: void __thiscall vostok::render::renderer_context::set_w(class vostok::math::float4x4const &)` |
| 99.88 | `private: void __thiscall vostok::resources::query_result::on_refered_query_ended(class vostok::resources::query_result *)` |
| 99.89 | `private: bool __thiscall vostok::resources::game_resources_manager::try_free_or_decrease_quality(class vostok::resources::query_result *, class vostok::resources::memory_type *)` |
| 99.89 | `public: void __thiscall vostok::render::renderer_context::set_view2shadow(class vostok::math::float4x4const &, unsigned int)` |
| 99.89 | `public: bool __thiscall vostok::render::ambient_volume::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::decal_instance::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::environment_probe::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::grass_patch::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::light::is_occluded(void) const` |
| 99.89 | `public: bool __thiscall vostok::render::render_surface_instance::is_occluded(void) const` |
| 99.89 | `public: enum assert_on_fail_bool __thiscall vostok::resources::query_result_for_cook::assert_on_fail(void) const` |
| 99.89 | `public: virtual bool __thiscall vostok::render::render_particle_emitter_instance::is_occluded(void) const` |
| 99.89 | `public: void __thiscall vostok::render::world::clear_resources(void)` |
| 99.89 | `private: void __thiscall vostok::resources::resources_manager::dispatch_tasks_finished_callback(class vostok::resources::query_result *, bool)` |
| 99.89 | `private: void __thiscall vostok::resources::query_result::on_create_resource_end(void)` |
| 99.90 | `public: void __thiscall vostok::render::renderer_context::set_p(class vostok::math::float4x4const &)` |
| 99.90 | `private: bool __thiscall vostok::resources::query_result::end_query_might_destroy_this(void)` |
| 99.90 | `public: virtual bool __thiscall vostok::resources::fs_task_iterator::is_helper_query_for_mount(void) const` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::ambient_volume>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::decal_instance>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::environment_probe>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::grass_patch>` |
| 99.90 | `vostok::render::is_occluded_predicate<vostok::render::render_surface_instance>` |
| 99.90 | `private: void __thiscall vostok::resources::queries_result::mark_inconsistent_qualities_as_failed(void)` |
| 99.91 | `private: void __thiscall vostok::resources::query_result::on_save_operation_end(void)` |
| 99.91 | `private: void __thiscall vostok::render::stage_gbuffer::render_grass(bool)` |
| 99.91 | `private: void __thiscall vostok::resources::query_result::set_create_resource_result(enum vostok::resources::cook_base::result_enum, enum vostok::resources::query_result_for_user::error_type_enum)` |
| 99.91 | `public: void __thiscall vostok::resources::query_result_for_cook::clear_user_data(void)` |
| 99.91 | `vostok::render::is_occluded_predicate_light` |
| 99.91 | `public: virtual __thiscall vostok::resources::query_result::~query_result(void)` |
| 99.91 | `private: void __thiscall vostok::render::speedtree_forest::cull_and_compute_lod(class vostok::render::renderer_context *, class vostok::math::float3const &, bool)` |
| 99.91 | `private: void __thiscall vostok::resources::query_result::unpin_raw_file(class vostok::const_buffer const &)` |
| 99.92 | `public: void __thiscall vostok::resources::resources_manager::push_new_query(class vostok::resources::query_result *)` |
| 99.92 | `public: void __thiscall vostok::render::system_renderer::draw_particle_system_instance_selections(class vostok::render::vector<class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> > const &)` |
| 99.92 | `private: bool __thiscall vostok::resources::game_resources_manager::try_reallocate_queue(class vostok::resources::memory_type *)` |
| 99.92 | `private: void __thiscall vostok::render::stage_gbuffer::render_particles(bool)` |
| 99.92 | `public: virtual void __thiscall vostok::render::stage_particles::execute(void)` |
| 99.92 | `private: void __thiscall vostok::resources::query_result::bind_unmanaged_resource_buffer_to_creation_or_inline_data(void)` |
| 99.92 | `private: void __thiscall vostok::resources::query_result::lock_fat_it(void)` |
| 99.92 | `private: void __thiscall vostok::resources::query_result::unlock_fat_it(void)` |
| 99.93 | `private: class vostok::vfs::vfs_iterator __thiscall vostok::resources::query_result::get_fat_it_zero_if_physical_path_it(void) const` |
| 99.93 | `private: void __thiscall vostok::resources::resources_manager::remove_from_generate_if_no_file_queue(class vostok::resources::query_result &)` |
| 99.93 | `public: virtual class vostok::mutable_buffer __thiscall survarium::weapon_core_inactive_state_cook::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 99.93 | `public: virtual class vostok::mutable_buffer __thiscall survarium::weapon_core_shotgun_reload_state_cook::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 99.93 | `private: void __thiscall vostok::render::stage_lights::render_particle_lighting(class vostok::render::render_particle_emitter_instance *, class vostok::render::light *, unsigned int)` |
| 99.93 | `private: void __thiscall vostok::resources::query_result::on_request_iterator_ready(class vostok::vfs::vfs_iterator &, bool)` |
| 99.93 | `private: bool __thiscall vostok::resources::query_result::need_create_resource_if_no_file(void)` |
| 99.93 | `private: void __thiscall vostok::resources::query_result::on_decompressing_end(void)` |
| 99.93 | `public: virtual float __thiscall vostok::resources::query_result_for_cook::satisfaction_with(unsigned int) const` |
| 99.93 | `private: void __thiscall vostok::resources::query_result::finish_normal_query(enum vostok::resources::cook_base::result_enum)` |
| 99.94 | `private: void __thiscall vostok::resources::query_result::free_unmanaged_buffer(void)` |
| 99.94 | `public: virtual class vostok::mutable_buffer __thiscall vostok::particle::particle_system_cook::allocate_resource(class vostok::resources::query_result_for_cook &, unsigned int, unsigned int &, bool)` |
| 99.94 | `vostok::render::fill_surface` |
| 99.94 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_compressed_resource_if_needed(void)` |
| 99.94 | `private: void __thiscall vostok::resources::resources_manager::add_to_generate_if_no_file_queue(class vostok::resources::query_result &)` |
| 99.94 | `private: bool __thiscall vostok::resources::query_result::retry_action_that_caused_out_of_memory(void)` |
| 99.94 | `private: void __thiscall vostok::render::stage_lights::render_model_lighting(struct vostok::render::render_surface_instance *, class vostok::render::light *)` |
| 99.94 | `private: void __thiscall vostok::render::stage_lights::render_speedtree_lighting(struct vostok::render::lod_entry const *, class SpeedTree::CInstance const *, struct SpeedTree::SInstanceLod const *, class vostok::render::speedtree_tree_component *, class vostok::render::light *)` |
| 99.94 | `private: void __thiscall vostok::render::stage_lights::render_to_hw_shadowmap(class vostok::render::light *, unsigned int, float, unsigned int, unsigned int, class vostok::math::float4x4const &, class vostok::math::float4x4const &, unsigned int)` |
| 99.94 | `private: void __thiscall vostok::resources::query_result::on_file_operation_end(class vostok::resources::query_result *)` |
| 99.94 | `public: virtual class vostok::mutable_buffer __thiscall vostok::core::configs::binary_config_cook_impl::allocate_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, bool)` |
| 99.94 | `public: void __thiscall vostok::render::temporal_projection_matrix_modifier::push_jittering(void)` |
| 99.94 | `public: virtual void __thiscall vostok::render::stage_accumulate_distortion::execute(void)` |
| 99.94 | `private: unsigned int __thiscall vostok::resources::queries_result::calculate_fs_iterator_requests_count(void)` |
| 99.94 | `private: unsigned int __thiscall vostok::resources::query_result::allocate_thread_id(void) const` |
| 99.94 | `private: unsigned int __thiscall vostok::resources::query_result::translate_thread_id(void) const` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::ambient_volume>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::decal_instance>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::environment_probe>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::grass_patch>` |
| 99.94 | `vostok::render::is_not_occluded_predicate<vostok::render::render_surface_instance>` |
| 99.95 | `private: void __thiscall vostok::render::stage_lights::render_particle_probe_lighting(class vostok::render::render_particle_emitter_instance *, struct vostok::render::environment_probe *, unsigned int)` |
| 99.95 | `private: void __thiscall vostok::resources::query_result::do_unmanaged_create_resource(class vostok::resources::unmanaged_cook *)` |
| 99.95 | `private: void __thiscall vostok::resources::query_result::set_result_iterator(class vostok::vfs::vfs_locked_iterator const &)` |
| 99.95 | `vostok::render::is_not_occluded_predicate_light` |
| 99.95 | `private: void __thiscall survarium::medkit::load(class vostok::configs::binary_config_value)` |
| 99.95 | `private: class vostok::math::float4x4 __thiscall vostok::render::stage_pre_rain::render_rain_shadow_map(void)` |
| 99.95 | `public: void __thiscall vostok::render::speedtree_forest::tick(class vostok::render::renderer_context *)` |
| 99.95 | `private: bool __thiscall vostok::resources::device_manager::pre_allocate(class vostok::resources::query_result *)` |
| 99.95 | `private: bool __thiscall vostok::resources::queries_result::calculate_result_from_children(void)` |
| 99.95 | `private: void __thiscall vostok::render::stage_visibility::gather_statistics(void) const` |
| 99.95 | `private: void __thiscall vostok::resources::query_result::do_inplace_unmanaged_create_resource(class vostok::resources::inplace_unmanaged_cook *)` |
| 99.95 | `public: void __thiscall vostok::render::renderer::sort_models_by_distance(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, bool)` |
| 99.95 | `private: void __thiscall vostok::resources::query_result::set_deleter_object(class vostok::resources::unmanaged_resource *)` |
| 99.95 | `private: void __thiscall vostok::resources::query_result::copy_data_to_resource(class vostok::const_buffer)` |
| 99.96 | `private: void __thiscall vostok::resources::resources_manager::dispatch_decompressed_resources(void)` |
| 99.96 | `public: void __thiscall vostok::resources::resource_freeing_functionality::free_collected(void)` |
| 99.96 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_raw_unmanaged_resource_if_needed(void)` |
| 99.96 | `private: void __thiscall vostok::render::stage_lights::render_light(class vostok::render::light *, bool)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::do_inplace_managed_create_resource(class vostok::resources::inplace_managed_cook *)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::add_referrer(class vostok::resources::query_result *, bool)` |
| 99.96 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_final_managed_resource_if_needed(void)` |
| 99.96 | `private: enum vostok::resources::resource_base::creation_source_enum __thiscall vostok::resources::query_result::creation_source_for_resource(void)` |
| 99.96 | `private: void __thiscall vostok::resources::resources_manager::decompress_resource(class vostok::resources::query_result *)` |
| 99.96 | `public: void __thiscall vostok::resources::game_resources_manager::out_of_memory_callback(class vostok::resources::query_result *)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::end_query_might_destroy_this_impl(void)` |
| 99.96 | `public: virtual void __thiscall vostok::sound::panning_lut_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.96 | `public: void __thiscall vostok::render::grass_world::render(class vostok::render::renderer_context *, class vostok::math::float3const &, enum vostok::render::enum_render_stage_type, unsigned int, float, bool, class vostok::render::res_effect *, bool, unsigned int)` |
| 99.96 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_raw_managed_resource_if_needed(void)` |
| 99.96 | `private: void __thiscall vostok::resources::allocate_functionality::allocate_raw_resources(class vostok::resources::thread_local_data *, bool)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::requery_on_out_of_memory(void)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::unpin_compressed_file(class vostok::const_buffer const &)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::unpin_raw_buffer(class vostok::const_buffer const &)` |
| 99.96 | `public: void __thiscall vostok::render::radiance_volume::inject_camera_occluders(class vostok::render::renderer_context *)` |
| 99.96 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_sun_rms(class vostok::render::light *, unsigned int, class vostok::render::vector<class vostok::math::float4x4>)` |
| 99.96 | `public: __thiscall vostok::render::engine::world::~world(void)` |
| 99.96 | `public: long __thiscall vostok::resources::resources_manager::query_resources_impl(struct vostok::resources::query_resource_params const &)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::propogate_sub_fats_to_resource<class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> >(class vostok::resources::resource_ptr<class vostok::resources::managed_resource, class vostok::resources::managed_intrusive_base> &)` |
| 99.96 | `private: void __thiscall vostok::resources::query_result::propogate_sub_fats_to_resource<class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> >(class vostok::resources::resource_ptr<class vostok::resources::unmanaged_resource, class vostok::resources::unmanaged_intrusive_base> &)` |
| 99.96 | `public: void __thiscall vostok::resources::resources_manager::continue_init_new_query(class vostok::resources::query_result &)` |
| 99.96 | `public: bool __thiscall vostok::render::remove_model_if_not_lod_predicate::operator()(struct vostok::render::render_surface_instance *)` |
| 99.97 | `private: void __thiscall vostok::resources::queries_result::translate_request_paths(void)` |
| 99.97 | `private: void __thiscall vostok::resources::queries_result::push_to_grm_cache(void)` |
| 99.97 | `private: void __thiscall vostok::resources::query_result::associate_created_resource_with_fat_or_name_registry(void)` |
| 99.97 | `public: virtual void __thiscall survarium::medkit::action(bool)` |
| 99.97 | `public: void __thiscall vostok::render::renderer_context::set_scene_view(class vostok::resources::resource_ptr<struct vostok::render::base_scene_view, class vostok::resources::unmanaged_intrusive_base>)` |
| 99.97 | `private: enum vostok::resources::allocation_result_enum __thiscall vostok::resources::query_result::allocate_final_unmanaged_resource_if_needed(void)` |
| 99.97 | `private: void __thiscall vostok::resources::query_result::translate_request_path(void)` |
| 99.97 | `private: void __thiscall vostok::resources::resources_manager::save_generated_resources(void)` |
| 99.97 | `protected: virtual void __thiscall vostok::resources::query_result_for_cook::increase_quality_to_target(class vostok::resources::query_result_for_cook *)` |
| 99.97 | `private: void __thiscall vostok::resources::query_result::late_set_fat_it(class vostok::vfs::vfs_iterator)` |
| 99.97 | `public: virtual void __thiscall vostok::render::stage_translucency::execute(void)` |
| 99.97 | `private: void __thiscall vostok::resources::allocate_functionality::prepare_raw_resource_for_inplace_unmanaged_cook(class vostok::resources::query_result *)` |
| 99.97 | `public: virtual void __thiscall vostok::render::stage_sun::execute(void)` |
| 99.97 | `private: void __thiscall vostok::resources::resources_manager::init_query_with_no_fat_it(class vostok::resources::query_result &)` |
| 99.97 | `private: class vostok::const_buffer __thiscall vostok::resources::query_result::pin_raw_buffer(void)` |
| 99.97 | `public: bool __thiscall vostok::resources::hdd_manager_sorting_predicate::operator()(class vostok::resources::query_result *, class vostok::resources::query_result *)` |
| 99.97 | `private: void __thiscall vostok::resources::query_result::on_load_operation_end(class vostok::resources::query_result *)` |
| 99.97 | `private: void __thiscall vostok::resources::resources_manager::decompress_resources(void)` |
| 99.97 | `public: void __thiscall vostok::render::grass_world::process_culling(class vostok::render::renderer_context *, float)` |
| 99.97 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_rms(class vostok::math::float3const &, float, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::render::vector<class vostok::math::float4x4>, unsigned int)` |
| 99.97 | `private: bool __thiscall vostok::resources::query_result::check_file_crc(void)` |
| 99.97 | `private: enum vostok::resources::query_result::consider_with_name_registry_result_enum __thiscall vostok::resources::query_result::consider_with_name_registry_impl(char const *, enum vostok::resources::query_result::only_try_to_get_associated_resource_bool)` |
| 99.97 | `private: bool __thiscall vostok::resources::query_result::try_push_created_resource_to_manager_might_destroy_this(void)` |
| 99.97 | `private: class vostok::const_buffer __thiscall vostok::resources::query_result::pin_compressed_file(void)` |
| 99.97 | `private: class vostok::const_buffer __thiscall vostok::resources::query_result::pin_raw_file(void)` |
| 99.97 | `private: bool __thiscall vostok::resources::query_result::process_request_path(bool)` |
| 99.97 | `private: bool __thiscall vostok::resources::device_manager::do_async_operation(void **, class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &, class vostok::mutable_buffer, unsigned __int64, bool)` |
| 99.97 | `public: virtual void __thiscall vostok::render::renderer_cook::create_resource(class vostok::resources::query_result_for_cook &, class vostok::const_buffer, class vostok::mutable_buffer)` |
| 99.97 | `public: static class vostok::resources::queries_result * __cdecl vostok::resources::resources_manager::create_queries_result(struct vostok::resources::query_resource_params const &)` |
| 99.97 | `public: virtual void __thiscall vostok::render::stage_volume_fog::execute(void)` |
| 99.97 | `private: bool __thiscall vostok::resources::query_result::try_synchronous_cook_from_inline_data(void)` |
| 99.97 | `private: void __thiscall vostok::animation::animation_collection_cook::sub_animations_loaded(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::configs::binary_config_value const &)` |
| 99.97 | `private: void __thiscall vostok::render::stage_lights::make_skin_scattering_texture(struct vostok::render::render_surface_instance *, class vostok::render::light *)` |
| 99.97 | `public: void __thiscall vostok::render::renderer_context::set_target_context(class vostok::render::renderer_context_targets const *, bool)` |
| 99.98 | `private: class vostok::math::float4 __thiscall vostok::render::stage_postprocess::compute_luminance_parameters(unsigned int)` |
| 99.98 | `public: virtual void __thiscall vostok::animation::animation_collection_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.98 | `private: void __thiscall vostok::render::stage_clouds::fill_cloud_texture(unsigned int)` |
| 99.98 | `private: void __thiscall vostok::resources::device_manager::fill_pre_allocated(void)` |
| 99.98 | `public: virtual void __thiscall vostok::render::skeleton_combined_render_model_instance_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.98 | `private: static void __cdecl vostok::animation::bi_spline_skeleton_animation_impl_cook::on_resources_ready(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *const)` |
| 99.98 | `public: void __thiscall vostok::resources::resources_manager::cooker_thread_tick(void)` |
| 99.98 | `private: void __thiscall vostok::resources::queries_result::on_fs_iterator_ready(class vostok::vfs::vfs_locked_iterator const &, class vostok::resources::query_result *)` |
| 99.98 | `private: void __thiscall survarium::weapon_cook::on_weapon_subresources_ready(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class survarium::weapon_core *)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_rain::execute(void)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_ambient_occlusion::execute(void)` |
| 99.98 | `private: void __thiscall vostok::resources::resources_manager::dispatch_allocated_raw_resources(void)` |
| 99.98 | `private: void __thiscall vostok::resources::resources_manager::dispatch_created_resources(void)` |
| 99.98 | `public: void __thiscall vostok::render::stage_light_propagation_volumes::execute_impl(void)` |
| 99.98 | `private: __thiscall vostok::resources::queries_result::~queries_result(void)` |
| 99.98 | `private: bool __thiscall vostok::resources::device_manager::process_query(class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &)` |
| 99.98 | `private: bool __thiscall vostok::resources::device_manager::process_read_query(void **, class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &)` |
| 99.98 | `public: virtual void __thiscall survarium::human_npc_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_lights::execute(void)` |
| 99.98 | `private: bool __thiscall vostok::resources::device_manager::process_write_query(void **, class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &)` |
| 99.98 | `public: class vostok::fs_new::native_path_string __thiscall vostok::resources::query_result::absolute_physical_path(enum assert_on_fail_bool)` |
| 99.98 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_rms_smoothed2(class vostok::math::float3const &, float, class vostok::math::float4x4const &, class vostok::math::float4x4const &, class vostok::render::vector<class vostok::math::float4x4>, unsigned int, unsigned int, unsigned int)` |
| 99.98 | `public: void __thiscall vostok::render::stage_forward::accumulate_local_reflections(void)` |
| 99.98 | `private: bool __thiscall vostok::resources::query_result::check_fat_for_resource_reusage(void)` |
| 99.98 | `protected: void __thiscall vostok::render::render_model_cook::on_subresources_loaded(class vostok::resources::queries_result &, struct vostok::render::cook_intermediate_data *)` |
| 99.98 | `private: bool __thiscall vostok::resources::query_result::translate_query_if_needed(void)` |
| 99.98 | `public: void __thiscall vostok::render::stage_debug::render_environment_probe_preview(void)` |
| 99.98 | `private: void __thiscall vostok::resources::query_result::do_create_resource(bool *)` |
| 99.98 | `public: void __thiscall vostok::resources::resources_manager::after_resource_deleted(class vostok::resources::cook_base *, bool, class vostok::resources::query_result *const, class vostok::resources::memory_usage_type const &, enum vostok::resources::class_id_enum, char const *)` |
| 99.98 | `private: void __thiscall vostok::render::static_render_model_instance_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 99.98 | `private: bool __thiscall vostok::resources::device_manager::open_file(void ***, class vostok::resources::query_result *, class vostok::fs_new::synchronous_device_interface const &)` |
| 99.98 | `private: void __thiscall vostok::resources::query_result::replicate(void)` |
| 99.98 | `private: void __thiscall survarium::player_cook::on_hit_params_loaded(class vostok::resources::queries_result &, struct survarium::player_creation_params *)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_clouds::execute(void)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_atmosphere::execute(void)` |
| 99.98 | `public: void __thiscall vostok::render::speedtree_forest::get_visible_tree_components(class vostok::render::renderer_context *, class vostok::math::float3const &, bool, class vostok::render::vector<struct vostok::render::speedtree_forest::tree_render_info> &)` |
| 99.98 | `private: void __thiscall vostok::resources::query_result::do_create_resource_end_part(void)` |
| 99.98 | `private: void __thiscall survarium::profile_character::weapon_resources_ready(class vostok::resources::queries_result &)` |
| 99.98 | `private: void __thiscall vostok::resources::device_manager::on_query_processed(class vostok::resources::query_result *, bool)` |
| 99.98 | `public: void __thiscall vostok::animation::skeleton_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_debug::execute(void)` |
| 99.98 | `protected: void __thiscall vostok::resources::query_result_for_cook::finish_query_impl(enum vostok::resources::cook_base::result_enum, enum assert_on_fail_bool, enum vostok::resources::query_result_for_user::error_type_enum)` |
| 99.98 | `protected: void __thiscall survarium::game_world::on_project_loaded(class vostok::resources::queries_result &, unsigned int, class boost::function<void __cdecl (class vostok::resources::queries_result &)> const &)` |
| 99.98 | `private: void __thiscall survarium::project_cooker_simple::on_collision_and_visuals_loaded(class vostok::resources::queries_result &, class survarium::simple_game_project *)` |
| 99.98 | `public: void __thiscall vostok::render::stage_light_propagation_volumes::execute_smoothed_impl(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int)` |
| 99.98 | `private: void __thiscall survarium::damage_zone_cook::on_sub_resources_loaded(class vostok::resources::queries_result &, class vostok::configs::binary_config_value const &)` |
| 99.98 | `private: void __thiscall vostok::sound::sound_collection_cook::sub_sounds_loaded(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::configs::binary_config_value const &)` |
| 99.98 | `public: virtual void __thiscall vostok::render::stage_forward::execute(void)` |
| 99.98 | `public: virtual void __thiscall vostok::render::render_output_window_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.98 | `public: void __thiscall vostok::render::stage_forward::render_forward_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, unsigned int)` |
| 99.99 | `private: void __thiscall vostok::resources::resources_manager::save_generated_resource(class vostok::resources::query_result *)` |
| 99.99 | `private: void __thiscall survarium::human_npc_cook::on_subresources_loaded(class vostok::resources::queries_result &, class survarium::human_npc *const)` |
| 99.99 | `public: virtual void __thiscall vostok::sound::sound_scene_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::stage_pre_rain::execute(void)` |
| 99.99 | `private: void __thiscall vostok::resources::query_result::send_to_create_resource(void)` |
| 99.99 | `private: void __thiscall survarium::sound_player_cook::on_sounds_loaded(class vostok::resources::queries_result &, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>)` |
| 99.99 | `private: void __thiscall survarium::booby_trap_cook::on_models_ready(class vostok::resources::queries_result &, class survarium::booby_trap *)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_aimed_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_aimed_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_hide_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_reload_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::double_barreled_weapon_core_show_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_aimed_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_aimed_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_hide_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_reload_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::pistol_weapon_core_show_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_aimed_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_aimed_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_aimed_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_aimed_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_chamber_a_round_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_fire_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_hide_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_reload_state> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_finish_substate> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_one_round_substate> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_shotgun_reload_start_substate> >::config_params)` |
| 99.99 | `private: void __thiscall survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::on_subresources_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *, struct survarium::weapon_sound_events_handler_state_cook<class survarium::weapon_sound_events_handler_state<class survarium::weapon_core_show_state> >::config_params)` |
| 99.99 | `private: void __thiscall vostok::animation::single_animation_cook::on_sub_resources_loaded(class vostok::resources::queries_result &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::stage_resolve_lighting::execute(void)` |
| 99.99 | `private: void __thiscall vostok::render::stage_light_propagation_volumes::render_to_sky_rms(class vostok::render::light *, unsigned int, unsigned int, class vostok::render::vector<class vostok::math::float4x4>)` |
| 99.99 | `public: virtual void __thiscall vostok::render::stage_shadow_direct::execute_disabled(void)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::frustum_culling(void)` |
| 99.99 | `private: void __thiscall vostok::render::stage_gbuffer::z_only_pass(void)` |
| 99.99 | `public: void __thiscall vostok::render::stage_forward::render_opaque_models(void)` |
| 99.99 | `private: void __thiscall vostok::render::effect_manager::on_effects_recompiled(class vostok::vectora<struct vostok::render::effect_manager::effect_to_recompile_struct> *, class vostok::resources::queries_result &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::material_effects_instance_cook::translate_query(class vostok::resources::query_result_for_cook &)` |
| 99.99 | `public: virtual void __thiscall vostok::render::stage_light_propagation_volumes::execute(void)` |
| 99.99 | `private: void __thiscall survarium::shotgun_weapon_reload_state_cook::on_substates_ready(class vostok::resources::queries_result &, class vostok::mutable_buffer, struct survarium::weapon_state_creation_params const *)` |
| 99.99 | `private: void __thiscall survarium::player_cook::on_subresources_loaded(class vostok::resources::queries_result &, struct survarium::player_creation_params *, struct survarium::inventory_cooker_data *, struct survarium::player_parameters_cooker_data *)` |
| 99.99 | `private: void __thiscall survarium::items_cook::create_item_and_finish_query(enum survarium::item_types_enum, class vostok::resources::resource_ptr<class vostok::configs::binary_config, class vostok::resources::unmanaged_intrusive_base>, class vostok::resources::query_result_for_cook *)` |
| 99.99 | `private: void __thiscall survarium::main_menu::on_resources_ready(class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall survarium::project_cooker_simple::on_damage_zones_loaded(class survarium::simple_game_project *, class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall survarium::project_cooker_simple::on_ladders_loaded(class survarium::simple_game_project *, class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_portals(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `protected: void __thiscall vostok::render::render_model_cook::on_materials_loaded(class vostok::resources::queries_result &, struct vostok::render::cook_intermediate_data *)` |
| 99.99 | `private: void __thiscall vostok::sound::ogg_encoded_sound_interface_cook::on_ogg_resources_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *)` |
| 99.99 | `private: void __thiscall vostok::resources::query_result::set_deleter_object_if_needed(bool *)` |
| 99.99 | `public: void __thiscall vostok::resources::allocate_functionality::prepare_final_resource(class vostok::resources::query_result *)` |
| 99.99 | `private: void __thiscall survarium::profile_character::character_animation_ready(class vostok::resources::queries_result &)` |
| 99.99 | `private: void __thiscall vostok::resources::query_result::finish_translated_query(enum vostok::resources::cook_base::result_enum)` |
| 99.99 | `public: void __thiscall vostok::render::batched_geometry<struct vostok::render::lpv_vertex>::for_each_batch_render(class vostok::render::renderer_context *, class boost::function<void __cdecl (struct vostok::render::geometry_batch const &)> const &, class boost::function<void __cdecl (struct vostok::render::geometry_batch const &)> const &)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_models(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `private: void __thiscall vostok::resources::queries_result::query_fs_iterators(void)` |
| 99.99 | `protected: void __thiscall vostok::core::configs::binary_config_cook::on_fs_iterators_ready(class vostok::resources::queries_result &)` |
| 99.99 | `public: void __thiscall vostok::render::stage_shadow_direct::render_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, class vostok::math::float4x4const &, unsigned int, unsigned int, class vostok::math::float3const &, unsigned int, unsigned int)` |
| 99.99 | `private: void __thiscall vostok::render::skeleton_combined_model_cook::on_resources_loaded(class vostok::resources::queries_result &, class vostok::resources::query_result_for_cook *, struct vostok::render::skeleton_combined_cook_data *)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_particles(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `private: void __thiscall vostok::render::speedtree_cook::on_speedtree_raw_data_loaded(class vostok::resources::queries_result &, struct vostok::render::speedtree_data *)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_lights(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `private: void __thiscall vostok::resources::resources_manager::init_new_autoselect_quality_queries(void)` |
| 99.99 | `public: void __thiscall vostok::render::speedtree_billboard_parameters::set(class vostok::render::renderer_context *, class vostok::render::speedtree_tree_component *)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_grass(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `private: void __thiscall vostok::resources::allocate_functionality::prepare_raw_resource_for_managed_or_unmanaged_cook(class vostok::resources::query_result *, enum vostok::resources::reallocating_bool)` |
| 99.99 | `private: void __thiscall vostok::render::stage_lights::render_shadowed_light(class vostok::render::light *)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_ambient_volumes(class vostok::math::float4*&, unsigned int &)` |
| 99.99 | `private: void __thiscall vostok::render::stage_visibility::get_results_and_prepare_bounds_decals(class vostok::math::float4*&, unsigned int &)` |
- _...and 114 more_

### Added (47)

- `[thunk]: public: virtual void * __thiscall survarium::damage_zone::`vector deleting destructor'(unsigned int)`
- `[thunk]: public: virtual void * __thiscall survarium::game_world::`vector deleting destructor'(unsigned int)`
- `[thunk]: public: virtual void * __thiscall vostok::engine::game_console::`vector deleting destructor'(unsigned int)`
- `[thunk]: public: virtual void __thiscall vostok::engine::editor_console::on_activate(void)`
- `[thunk]: public: virtual void __thiscall vostok::engine::editor_console::on_deactivate(void)`
- `[thunk]: public: virtual void __thiscall vostok::engine::game_console::on_activate(void)`
- `[thunk]: public: virtual void __thiscall vostok::engine::game_console::on_deactivate(void)`
- `private: float __thiscall survarium::medkit::reduce_damage(char const *, char const *, float, float)`
- `private: struct survarium::medkit::damage_protection const * __thiscall survarium::medkit::find_damage_protection(char const *, char const *)`
- `private: void __thiscall survarium::medkit::active_tick(unsigned int)`
- `private: void __thiscall survarium::medkit::on_player_death(void)`
- `private: void __thiscall survarium::medkit::remove_affects(void)`
- `private: void __thiscall survarium::medkit::set_active(bool)`
- `private: void __thiscall vostok::resources::allocate_functionality::allocate_final_resources<class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> >(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> &, bool)`
- `private: void __thiscall vostok::resources::resources_manager::create_resources<class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> >(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> const &, class vostok::resources::query_result *, bool)`
- `public: __thiscall boost::_bi::storage3<class boost::_bi::value<class vostok::render::engine::world *>, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> >, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> > >::storage3<class boost::_bi::value<class vostok::render::engine::world *>, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> >, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> > >(struct boost::_bi::storage3<class boost::_bi::value<class vostok::render::engine::world *>, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_scene, class vostok::resources::unmanaged_intrusive_base> >, class boost::_bi::value<class vostok::resources::resource_ptr<struct vostok::render::base_output_window, class vostok::resources::unmanaged_intrusive_base> > > const &)`
- `public: __thiscall survarium::player_death_subscriber::player_death_subscriber(class boost::function<void __cdecl (void)> const &)`
- `public: __thiscall vostok::fs_new::virtual_path_string::ctor<char *>(char *const &)`
- `public: __thiscall vostok::render::speedtree_data::speedtree_data(void)`
- `public: class vostok::resources::query_result * __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::pop_front(void)`
- `public: class vostok::resources::query_result * __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::pop_all_and_clear(unsigned int *)`
- `public: virtual __thiscall vostok::ai::selectors::sound_target_selector::~sound_target_selector(void)`
- `public: virtual void * __thiscall Scaleform::Render::MappedTextureBase::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall btCollisionWorld::ContactResultCallback::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall btCollisionWorld::RayResultCallback::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::damage_zone::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::generic_anomaly::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::player_input_handler::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::weapon_core_shotgun_reload_start_substate::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::console_commands::cc_u32::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::core::engine::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::engine::game_console::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::particle::particle_system_wrapper_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::scene_view::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage::`vector deleting destructor'(unsigned int)`
- `public: virtual void __thiscall survarium::medkit::holder_assigned(void)`
- `public: virtual void __thiscall survarium::medkit::holder_removed(void)`
- `public: virtual void __thiscall survarium::medkit::remove(void)`
- `public: virtual void __thiscall vostok::resources::hdd_manager::grab_sorted_queries(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy> &)`
- `public: void * __thiscall boost::_bi::bind_t<void, class boost::_mfi::mf2<void, class survarium::object_wire, class vostok::resources::queries_result &, class boost::function<void __cdecl (class survarium::game_object_&)> &>, class boost::_bi::list3<class boost::_bi::value<class survarium::object_wire *>, struct boost::arg<1>, class boost::_bi::value<class boost::function<void __cdecl (class survarium::game_object_&)> > > >::`scalar deleting destructor'(unsigned int)`
- `public: void __thiscall vostok::intrusive_double_linked_list<class vostok::resources::query_result, class vostok::resources::query_result *, 624, 620, class vostok::threading::mutex, class vostok::no_size_policy, class vostok::debug_policy>::erase(class vostok::resources::query_result *)`
- `public: void __thiscall vostok::intrusive_double_linked_list<class vostok::resources::query_result, class vostok::resources::query_result *, 624, 620, class vostok::threading::mutex, class vostok::no_size_policy, class vostok::debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::render::renderer::fill_opaque_models(unsigned int, unsigned int)`
- `public: void __thiscall vostok::render::stage_shadow_direct::execute_cascade(unsigned int, unsigned int, unsigned int, unsigned int)`
- `public: void __thiscall vostok::render::stage_shadow_direct::prepare_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, class vostok::math::float4x4const &, unsigned int, unsigned int, class vostok::math::float3const &, unsigned int)`

### Deleted (58)

- `[thunk]: __thiscall survarium::booby_trap_core::`vcall'{16, {flat}}`
- `[thunk]: public: virtual void * __thiscall survarium::free_fly_camera::`vector deleting destructor'(unsigned int)`
- ``vostok::render::options::register_console_commands'::`2'::`dynamic atexit destructor for 'enabled_light_propagation_volumes_stage_cc''`
- `private: void __thiscall vostok::render::culling::portal_sector_system::draw_portals(class vostok::render::system_renderer &, unsigned int)`
- `private: void __thiscall vostok::render::culling::portal_sector_system::draw_quads(class vostok::render::system_renderer &)`
- `private: void __thiscall vostok::render::renderer::draw_frame_histogram(void) const`
- `private: void __thiscall vostok::render::renderer::draw_luminance_picker_info(struct vostok::ui::font const *)`
- `private: void __thiscall vostok::render::renderer::draw_stages_stats(struct vostok::ui::font const *)`
- `private: void __thiscall vostok::resources::allocate_functionality::allocate_final_resources<class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> >(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> &, bool)`
- `private: void __thiscall vostok::resources::resources_manager::create_resources<class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> >(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy> const &, class vostok::resources::query_result *, bool)`
- `protected: float __thiscall survarium::medkit::reduce_damage(char const *, char const *, float, float)`
- `protected: struct survarium::medkit::damage_protection const * __thiscall survarium::medkit::find_damage_protection(char const *, char const *)`
- `protected: virtual void * __thiscall Scaleform::SysAllocBase::`vector deleting destructor'(unsigned int)`
- `protected: virtual void * __thiscall survarium::booby_trap_core::`vector deleting destructor'(unsigned int)`
- `protected: void __thiscall survarium::medkit::active_tick(unsigned int)`
- `protected: void __thiscall survarium::medkit::remove_affects(void)`
- `protected: void __thiscall survarium::medkit::set_active(bool)`
- `public: __thiscall vostok::particle::lod_entry::~lod_entry(void)`
- `public: __thiscall vostok::render::render_target_instance::render_target_instance(void)`
- `public: __thiscall vostok::render::sun_cascade::sun_cascade(struct vostok::render::sun_cascade const &)`
- `public: class vostok::resources::query_result * __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 600, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::pop_front(void)`
- `public: class vostok::resources::query_result * __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::pop_all_and_clear(unsigned int *)`
- `public: class vostok::variant<32> * __thiscall vostok::resources::query_result_for_cook::user_data(void) const`
- `public: unsigned int __thiscall vostok::render::resource_manager::get_texture_video_memory_size(void)`
- `public: virtual __thiscall survarium::rifle_scope::~rifle_scope(void)`
- `public: virtual __thiscall vostok::particle::particle_system_instance::~particle_system_instance(void)`
- `public: virtual void * __thiscall Scaleform::Render::TextureFormat::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall stlp_std::runtime_error::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::artefact_base::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::game_world_object::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::global_input_handler::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::inventory_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::items_cook::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::rifle_scope::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall survarium::usable_object::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::console_impl::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::detail::concrete_type_helper<unsigned char>::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::particle::particle_system_instance_impl::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::render::stage_visibility::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::resources::managed_resource::`vector deleting destructor'(unsigned int)`
- `public: virtual void * __thiscall vostok::vfs::mounter::`vector deleting destructor'(unsigned int)`
- `public: virtual void __thiscall vostok::resources::hdd_manager::grab_sorted_queries(class vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy> &)`
- `public: void __thiscall vostok::intrusive_double_linked_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, 612, class vostok::threading::mutex, class vostok::no_size_policy, class vostok::debug_policy>::erase(class vostok::resources::query_result *)`
- `public: void __thiscall vostok::intrusive_double_linked_list<class vostok::resources::query_result, class vostok::resources::query_result *, 616, 612, class vostok::threading::mutex, class vostok::no_size_policy, class vostok::debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 600, class vostok::threading::mutex, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::intrusive_list<class vostok::resources::query_result, class vostok::resources::query_result *, 608, class vostok::threading::single_threading_policy, class vostok::size_policy, class vostok::no_debug_policy>::push_back(class vostok::resources::query_result *, bool *)`
- `public: void __thiscall vostok::render::culling::portal_sector_system::render(class vostok::render::system_renderer &, class vostok::math::float3const &, class vostok::math::float4x4const &)`
- `public: void __thiscall vostok::render::culling::sector_double_query_preventer::render(class vostok::render::system_renderer &)`
- `public: void __thiscall vostok::render::grass_world::render_debug(class vostok::render::renderer_context *)`
- `public: void __thiscall vostok::render::renderer::draw_debug(class vostok::render::scene *, class vostok::render::scene_view *, float, struct vostok::ui::font const *)`
- `public: void __thiscall vostok::render::renderer::fill_opaque_models(void)`
- `public: void __thiscall vostok::render::scene::draw_portal_system(class vostok::render::system_renderer &, class vostok::math::float3const &, class vostok::math::float4x4const &)`
- `public: void __thiscall vostok::render::stage_shadow_direct::draw_debug(unsigned int)`
- `public: void __thiscall vostok::render::stage_shadow_direct::execute_cascade(unsigned int, unsigned int, unsigned int)`
- `public: void __thiscall vostok::render::stage_shadow_direct::prepare_models(class vostok::render::vector<struct vostok::render::render_surface_instance *> &, class vostok::math::float4x4const &, unsigned int, unsigned int, class vostok::math::float3const &)`
- `vostok::render::draw_text`
- `vostok::render::draw_text_shadowed`
- `vostok::render::make_ui_vertices`
