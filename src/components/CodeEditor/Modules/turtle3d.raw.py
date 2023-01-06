from turtle import *
from math import sqrt
''' NEW DEFS'''
if Turtle._goto.__name__ != '_grbl_goto':
    Turtle.__goto = Turtle._goto

Turtle.GRBL_PRUSA_START = '''; generated by PrusaSlicer 2.5.0+win64 

M73 P0 R8
M73 Q0 S8
M201 X1000 Y1000 Z200 E8000 ; sets maximum accelerations, mm/sec^2
M203 X200 Y200 Z12 E120 ; sets maximum feedrates, mm / sec
M204 P1250 R1250 T1250 ; sets acceleration (P, T) and retract acceleration (R), mm/sec^2
M205 X8.00 Y8.00 Z0.40 E4.50 ; sets the jerk limits, mm/sec
M205 S0 T0 ; sets the minimum extruding and travel feed rate, mm/sec
M107
;TYPE:Custom
M862.3 P "MK3SMMU2S" ; printer model check
M862.1 P0.4 ; nozzle diameter check
M115 U3.11.0 ; tell printer latest fw version
G90 ; use absolute coordinates
M83 ; extruder relative mode
M104 S215 ; set extruder temp
M140 S60 ; set bed temp
M190 S60 ; wait for bed temp
M109 S215 ; wait for extruder temp
G28 W ; home all without mesh bed level
G80 ; mesh bed leveling

; Send the filament type to the MMU2.0 unit.
; E stands for extruder number, F stands for filament type (0: default; 1:flex; 2: PVA)
M403 E0 F0
M403 E1 F0
M403 E2 F0
M403 E3 F0
M403 E4 F0


;go outside print area
G1 Y-3 F1000
G1 Z0.4 F1000
; select extruder
T0
; initial load
G1 X55 E29 F1073
G1 X5 E29 F1800
G1 X55 E8 F2000
M73 P1 R8
M73 Q1 S8
G1 Z0.3 F1000
G92 E0
G1 X240 E25 F2200
G1 Y-2 F1000
M73 P2 R7
M73 Q2 S7
G1 X55 E25 F1400
G1 Z0.2 F1000
M73 P4 R7
M73 Q4 S7
G1 X5 E4 F1000
G92 E0


M221 S95
G92 E0

; Don't change E values below. Excessive value can damage the printer.

M907 E538 ; set extruder motor current
G21 ; set units to millimeters
G90 ; use absolute coordinates
M83 ; use relative distances for extrusion
M900 K0.05 ; Filament gcode LA 1.5
M900 K30 ; Filament gcode LA 1.0
M107
;LAYER_CHANGE
;Z:0.2
;HEIGHT:0.2
;BEFORE_LAYER_CHANGE
G92 E0.0
;0.2


G1 E-.8 F2100
G1 Z.4 F720
;AFTER_LAYER_CHANGE
;0.2
G1 X91.527 Y73.241 F10800
G1 Z.2 F720
G1 E.8 F2100
M204 S800
;TYPE:Skirt/Brim
'''

Turtle.GRBL_PRUSA_END = '''
;TYPE:Custom
; Filament-specific end gcode
G1 Z3 F720 ; Move print head up
G1 X0 Y210 F7200 ; park
G1 Z51 F720 ; Move print head further up

G1 E2 F5000
M73 P99 R0
M73 Q99 S0
G1 E2 F5500
G1 E2 F6000
G1 E-15 F5800
G1 E-20 F5500
G1 E10 F3000
G1 E-10 F3100
G1 E10 F3150
G1 E-10 F3250
G1 E10 F3300


M140 S0 ; turn off heatbed
M107 ; turn off fan

; Unload filament
M702 C

G4 ; wait
M221 S100 ; reset flow
M900 K0 ; reset LA

M104 S0 ; turn off temperature
M84 ; disable motors
M73 P100 R0
M73 Q100 S0


; prusaslicer_config = begin
; avoid_crossing_perimeters = 0
; avoid_crossing_perimeters_max_detour = 0
; bed_custom_model = 
; bed_custom_texture = 
; bed_shape = 0x0,250x0,250x210,0x210
; bed_temperature = 60,60,60,60,90
; before_layer_gcode = ;BEFORE_LAYER_CHANGE\\nG92 E0.0\\n;[layer_z]\\n\\n
; between_objects_gcode = 
; bottom_fill_pattern = monotonic
; bottom_solid_layers = 3
; bottom_solid_min_thickness = 0.5
; bridge_acceleration = 1000
; bridge_angle = 0
; bridge_fan_speed = 100,100,100,100,50
; bridge_flow_ratio = 0.95
; bridge_speed = 25
; brim_separation = 0.1
; brim_type = outer_only
; brim_width = 0
; clip_multipart_objects = 1
; color_change_gcode = M600\\nG1 E0.4 F1500 ; prime after color change
; compatible_printers_condition_cummulative = "printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK3.*/ and nozzle_diameter[0]==0.4";"nozzle_diameter[0]!=0.8 and nozzle_diameter[0]!=0.25 and printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material";"nozzle_diameter[0]!=0.8 and nozzle_diameter[0]!=0.25 and printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material";"nozzle_diameter[0]!=0.8 and nozzle_diameter[0]!=0.25 and printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material";"nozzle_diameter[0]!=0.8 and nozzle_diameter[0]!=0.25 and printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material";"nozzle_diameter[0]!=0.8 and nozzle_diameter[0]!=0.6 and nozzle_diameter[0]!=0.25 and printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material"
; complete_objects = 0
; cooling = 1,1,1,1,1
; cooling_tube_length = 20
; cooling_tube_retraction = 40
; default_acceleration = 1000
; default_filament_profile = "Prusament PLA @MMU2"
; default_print_profile = 0.15mm QUALITY @MK3
; deretract_speed = 0,0,0,0,0
; disable_fan_first_layers = 1,1,1,1,3
; dont_support_bridges = 0
; draft_shield = disabled
; duplicate_distance = 6
; elefant_foot_compensation = 0.2
; end_filament_gcode = "; Filament-specific end gcode";"; Filament-specific end gcode";"; Filament-specific end gcode";"; Filament-specific end gcode";"; Filament-specific end gcode"
; end_gcode = {if max_layer_z < max_print_height}G1 Z{z_offset+min(max_layer_z+1, max_print_height)} F720 ; Move print head up{endif}\\nG1 X0 Y210 F7200 ; park\\n{if max_layer_z < max_print_height}G1 Z{z_offset+min(max_layer_z+49, max_print_height)} F720 ; Move print head further up{endif}\\n{if has_wipe_tower}\\nG1 E-15 F3000\\n{else}\\nG1 E2 F5000\\nG1 E2 F5500\\nG1 E2 F6000\\nG1 E-15 F5800\\nG1 E-20 F5500\\nG1 E10 F3000\\nG1 E-10 F3100\\nG1 E10 F3150\\nG1 E-10 F3250\\nG1 E10 F3300\\n{endif}\\n\\nM140 S0 ; turn off heatbed\\nM107 ; turn off fan\\n\\n; Unload filament\\nM702 C\\n\\nG4 ; wait\\nM221 S100 ; reset flow\\nM900 K0 ; reset LA\\n{if print_settings_id=~/.*(DETAIL @MK3|QUALITY @MK3|SOLUBLE|@0.25 nozzle MK3).*/}M907 E538 ; reset extruder motor current{endif}\\nM104 S0 ; turn off temperature\\nM84 ; disable motors\\n
; ensure_vertical_shell_thickness = 1
; external_perimeter_extrusion_width = 0.6
; external_perimeter_speed = 35
; external_perimeters_first = 0
; extra_loading_move = -25
; extra_perimeters = 0
; extruder_clearance_height = 20
; extruder_clearance_radius = 45
; extruder_colour = #FF8000;#DB5182;#3EC0FF;#FF4F4F;#FBEB7D
; extruder_offset = 0x0,0x0,0x0,0x0,0x0
; extrusion_axis = E
; extrusion_multiplier = 1,1,1,1,1
; extrusion_width = 0.5
; fan_always_on = 1,1,1,1,1
; fan_below_layer_time = 100,100,100,100,20
; filament_colour = #FF8000;#FF8000;#FF8000;#FF8000;#FF8000
; filament_cooling_final_speed = 2,2,2,2,1
; filament_cooling_initial_speed = 3,3,3,3,2
; filament_cooling_moves = 1,1,1,1,1
; filament_cost = 36.29,36.29,36.29,36.29,36.29
; filament_density = 1.24,1.24,1.24,1.24,1.27
; filament_diameter = 1.75,1.75,1.75,1.75,1.75
; filament_load_time = 15,15,15,15,15
; filament_loading_speed = 14,14,14,14,14
; filament_loading_speed_start = 19,19,19,19,19
; filament_max_volumetric_speed = 13,13,13,13,7
; filament_minimal_purge_on_wipe_tower = 15,15,15,15,15
; filament_notes = ;;;;
; filament_ramming_parameters = "130 120 2.70968 2.93548 3.32258 3.83871 4.58065 5.54839 6.51613 7.35484 7.93548 8.16129| 0.05 2.66451 0.45 3.05805 0.95 4.05807 1.45 5.97742 1.95 7.69999 2.45 8.1936 2.95 11.342 3.45 11.4065 3.95 7.6 4.45 7.6 4.95 7.6";"130 120 2.70968 2.93548 3.32258 3.83871 4.58065 5.54839 6.51613 7.35484 7.93548 8.16129| 0.05 2.66451 0.45 3.05805 0.95 4.05807 1.45 5.97742 1.95 7.69999 2.45 8.1936 2.95 11.342 3.45 11.4065 3.95 7.6 4.45 7.6 4.95 7.6";"130 120 2.70968 2.93548 3.32258 3.83871 4.58065 5.54839 6.51613 7.35484 7.93548 8.16129| 0.05 2.66451 0.45 3.05805 0.95 4.05807 1.45 5.97742 1.95 7.69999 2.45 8.1936 2.95 11.342 3.45 11.4065 3.95 7.6 4.45 7.6 4.95 7.6";"130 120 2.70968 2.93548 3.32258 3.83871 4.58065 5.54839 6.51613 7.35484 7.93548 8.16129| 0.05 2.66451 0.45 3.05805 0.95 4.05807 1.45 5.97742 1.95 7.69999 2.45 8.1936 2.95 11.342 3.45 11.4065 3.95 7.6 4.45 7.6 4.95 7.6";"120 140 4.70968 4.74194 4.77419 4.80645 4.83871 4.87097 4.90323 5 5.25806 5.67742 6.29032 7.06452 7.83871 8.3871| 0.05 4.72901 0.45 4.73545 0.95 4.83226 1.45 4.88067 1.95 5.05483 2.45 5.93553 2.95 7.53556 3.45 8.6323 3.95 7.6 4.45 7.6 4.95 7.6"
; filament_retract_length = nil,nil,nil,nil,1
; filament_retract_lift = nil,nil,nil,nil,0.2
; filament_settings_id = "Prusament PLA @MMU2";"Prusament PLA @MMU2";"Prusament PLA @MMU2";"Prusament PLA @MMU2";"Prusament PETG @MMU2"
; filament_soluble = 0,0,0,0,0
; filament_spool_weight = 201,201,201,201,201
; filament_toolchange_delay = 0,0,0,0,0
; filament_type = PLA;PLA;PLA;PLA;PETG
; filament_unload_time = 12,12,12,12,12
; filament_unloading_speed = 20,20,20,20,20
; filament_unloading_speed_start = 100,100,100,100,120
; filament_vendor = Prusa Polymers
; fill_angle = 45
; fill_density = 20%
; fill_pattern = grid
; first_layer_acceleration = 800
; first_layer_acceleration_over_raft = 0
; first_layer_bed_temperature = 60,60,60,60,85
; first_layer_extrusion_width = 0.42
; first_layer_height = 0.2
; first_layer_speed = 20
; first_layer_speed_over_raft = 30
; first_layer_temperature = 215,215,215,215,230
; full_fan_speed_layer = 4,4,4,4,5
; fuzzy_skin = none
; fuzzy_skin_point_dist = 0.8
; fuzzy_skin_thickness = 0.3
; gap_fill_enabled = 1
; gap_fill_speed = 40
; gcode_comments = 0
; gcode_flavor = marlin
; gcode_label_objects = 1
; gcode_resolution = 0.0125
; gcode_substitutions = 
; high_current_on_filament_swap = 0
; host_type = octoprint
; infill_acceleration = 1000
; infill_anchor = 2.5
; infill_anchor_max = 12
; infill_every_layers = 1
; infill_extruder = 1
; infill_extrusion_width = 0.5
; infill_first = 0
; infill_only_where_needed = 0
; infill_overlap = 25%
; infill_speed = 85
; interface_shells = 0
; ironing = 0
; ironing_flowrate = 15%
; ironing_spacing = 0.1
; ironing_speed = 15
; ironing_type = top
; layer_gcode = ;AFTER_LAYER_CHANGE\\n;[layer_z]
; layer_height = 0.3
; machine_limits_usage = emit_to_gcode
; machine_max_acceleration_e = 8000,8000
; machine_max_acceleration_extruding = 1250,1250
; machine_max_acceleration_retracting = 1250,1250
; machine_max_acceleration_travel = 1500,1250
; machine_max_acceleration_x = 1000,960
; machine_max_acceleration_y = 1000,960
; machine_max_acceleration_z = 200,200
; machine_max_feedrate_e = 120,120
; machine_max_feedrate_x = 200,100
; machine_max_feedrate_y = 200,100
; machine_max_feedrate_z = 12,12
; machine_max_jerk_e = 4.5,4.5
; machine_max_jerk_x = 8,8
; machine_max_jerk_y = 8,8
; machine_max_jerk_z = 0.4,0.4
; machine_min_extruding_rate = 0,0
; machine_min_travel_rate = 0,0
; max_fan_speed = 100,100,100,100,50
; max_layer_height = 0.25,0.25,0.25,0.25,0.25
; max_print_height = 210
; max_print_speed = 200
; max_volumetric_extrusion_rate_slope_negative = 0
; max_volumetric_extrusion_rate_slope_positive = 0
; max_volumetric_speed = 0
; min_bead_width = 85%
; min_fan_speed = 100,100,100,100,30
; min_feature_size = 25%
; min_layer_height = 0.07,0.07,0.07,0.07,0.07
; min_print_speed = 15,15,15,15,15
; min_skirt_length = 4
; mmu_segmented_region_max_width = 0
; notes = 
; nozzle_diameter = 0.4,0.4,0.4,0.4,0.4
; only_retract_when_crossing_perimeters = 0
; ooze_prevention = 0
; output_filename_format = {input_filename_base}_{layer_height}mm_{initial_filament_type}_{printer_model}_{print_time}.gcode
; overhangs = 1
; parking_pos_retraction = 85
; pause_print_gcode = M601
; perimeter_acceleration = 800
; perimeter_extruder = 1
; perimeter_extrusion_width = 0.5
; perimeter_generator = arachne
; perimeter_speed = 50
; perimeters = 2
; physical_printer_settings_id = 
; post_process = 
; print_settings_id = 0.30mm DRAFT @MK3
; printer_model = MK3SMMU2S
; printer_notes = Don't remove the following keywords! These keywords are used in the "compatible printer" condition of the print and filament profiles to link the particular print and filament profiles to this printer profile.\\nPRINTER_VENDOR_PRUSA3D\\nPRINTER_MODEL_MK3\\n
; printer_settings_id = Original Prusa i3 MK3S & MK3S+ MMU2S
; printer_technology = FFF
; printer_variant = 0.4
; printer_vendor = 
; raft_contact_distance = 0.2
; raft_expansion = 1.5
; raft_first_layer_density = 90%
; raft_first_layer_expansion = 3
; raft_layers = 0
; remaining_times = 1
; resolution = 0
; retract_before_travel = 1,1,1,1,1
; retract_before_wipe = 0%,0%,0%,0%,0%
; retract_layer_change = 1,1,1,1,1
; retract_length = 0.8,0.8,0.8,0.8,0.8
; retract_length_toolchange = 0,0,0,0,0
; retract_lift = 0.4,0.4,0.4,0.4,0.4
; retract_lift_above = 0,0,0,0,0
; retract_lift_below = 209,209,209,209,209
; retract_restart_extra = 0,0,0,0,0
; retract_restart_extra_toolchange = 0,0,0,0,0
; retract_speed = 35,35,35,35,35
; seam_position = aligned
; silent_mode = 1
; single_extruder_multi_material = 1
; single_extruder_multi_material_priming = 0
; skirt_distance = 2
; skirt_height = 3
; skirts = 1
; slice_closing_radius = 0.049
; slicing_mode = regular
; slowdown_below_layer_time = 15,15,15,15,15
; small_perimeter_speed = 30
; solid_infill_below_area = 0
; solid_infill_every_layers = 0
; solid_infill_extruder = 1
; solid_infill_extrusion_width = 0.5
; solid_infill_speed = 80
; spiral_vase = 0
; standby_temperature_delta = -5
; start_filament_gcode = "M900 K{if printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.6}0.12{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.8}0.06{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/}0.2{elsif nozzle_diameter[0]==0.8}0.01{elsif nozzle_diameter[0]==0.6}0.04{else}0.05{endif} ; Filament gcode LA 1.5\\n{if printer_notes=~/.*PRINTER_MODEL_MINI.*/};{elsif printer_notes=~/.*PRINTER_HAS_BOWDEN.*/}M900 K200{elsif nozzle_diameter[0]==0.6}M900 K18{elsif nozzle_diameter[0]==0.8};{else}M900 K30{endif} ; Filament gcode LA 1.0";"M900 K{if printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.6}0.12{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.8}0.06{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/}0.2{elsif nozzle_diameter[0]==0.8}0.01{elsif nozzle_diameter[0]==0.6}0.04{else}0.05{endif} ; Filament gcode LA 1.5\\n{if printer_notes=~/.*PRINTER_MODEL_MINI.*/};{elsif printer_notes=~/.*PRINTER_HAS_BOWDEN.*/}M900 K200{elsif nozzle_diameter[0]==0.6}M900 K18{elsif nozzle_diameter[0]==0.8};{else}M900 K30{endif} ; Filament gcode LA 1.0";"M900 K{if printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.6}0.12{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.8}0.06{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/}0.2{elsif nozzle_diameter[0]==0.8}0.01{elsif nozzle_diameter[0]==0.6}0.04{else}0.05{endif} ; Filament gcode LA 1.5\\n{if printer_notes=~/.*PRINTER_MODEL_MINI.*/};{elsif printer_notes=~/.*PRINTER_HAS_BOWDEN.*/}M900 K200{elsif nozzle_diameter[0]==0.6}M900 K18{elsif nozzle_diameter[0]==0.8};{else}M900 K30{endif} ; Filament gcode LA 1.0";"M900 K{if printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.6}0.12{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.8}0.06{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/}0.2{elsif nozzle_diameter[0]==0.8}0.01{elsif nozzle_diameter[0]==0.6}0.04{else}0.05{endif} ; Filament gcode LA 1.5\\n{if printer_notes=~/.*PRINTER_MODEL_MINI.*/};{elsif printer_notes=~/.*PRINTER_HAS_BOWDEN.*/}M900 K200{elsif nozzle_diameter[0]==0.6}M900 K18{elsif nozzle_diameter[0]==0.8};{else}M900 K30{endif} ; Filament gcode LA 1.0";"M900 K{if printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.6}0.12{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.8}0.06{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/}0.2{elsif nozzle_diameter[0]==0.8}0.02{elsif nozzle_diameter[0]==0.6}0.04{else}0.08{endif} ; Filament gcode LA 1.5\\n{if printer_notes=~/.*PRINTER_MODEL_MINI.*/};{elsif printer_notes=~/.*PRINTER_HAS_BOWDEN.*/}M900 K200{elsif nozzle_diameter[0]==0.6}M900 K24{elsif nozzle_diameter[0]==0.8};{else}M900 K45{endif} ; Filament gcode LA 1.0"
; start_gcode = M862.3 P "[printer_model]" ; printer model check\\nM862.1 P[nozzle_diameter] ; nozzle diameter check\\nM115 U3.11.0 ; tell printer latest fw version\\nG90 ; use absolute coordinates\\nM83 ; extruder relative mode\\nM104 S[first_layer_temperature] ; set extruder temp\\nM140 S[first_layer_bed_temperature] ; set bed temp\\nM190 S[first_layer_bed_temperature] ; wait for bed temp\\nM109 S[first_layer_temperature] ; wait for extruder temp\\nG28 W ; home all without mesh bed level\\nG80 ; mesh bed leveling\\n\\n; Send the filament type to the MMU2.0 unit.\\n; E stands for extruder number, F stands for filament type (0: default; 1:flex; 2: PVA)\\nM403 E0 F{"" + ((filament_type[0]=="FLEX") ? 1 : ((filament_type[0]=="PVA") ? 2 : 0))}\\nM403 E1 F{"" + ((filament_type[1]=="FLEX") ? 1 : ((filament_type[1]=="PVA") ? 2 : 0))}\\nM403 E2 F{"" + ((filament_type[2]=="FLEX") ? 1 : ((filament_type[2]=="PVA") ? 2 : 0))}\\nM403 E3 F{"" + ((filament_type[3]=="FLEX") ? 1 : ((filament_type[3]=="PVA") ? 2 : 0))}\\nM403 E4 F{"" + ((filament_type[4]=="FLEX") ? 1 : ((filament_type[4]=="PVA") ? 2 : 0))}\\n\\n{if not has_single_extruder_multi_material_priming}\\n;go outside print area\\nG1 Y-3 F1000\\nG1 Z0.4 F1000\\n; select extruder\\nT[initial_tool]\\n; initial load\\nG1 X55 E29 F1073\\nG1 X5 E29 F1800\\nG1 X55 E8 F2000\\nG1 Z0.3 F1000\\nG92 E0\\nG1 X240 E25 F2200\\nG1 Y-2 F1000\\nG1 X55 E25 F1400\\nG1 Z0.2 F1000\\nG1 X5 E4 F1000\\nG92 E0\\n{endif}\\n\\nM221 S{if layer_height<0.075}100{else}95{endif}\\nG92 E0\\n\\n; Don't change E values below. Excessive value can damage the printer.\\n{if print_settings_id=~/.*(DETAIL @MK3|QUALITY @MK3|SOLUBLE).*/}M907 E430 ; set extruder motor current{endif}\\n{if print_settings_id=~/.*(SPEED @MK3|DRAFT @MK3).*/}M907 E538 ; set extruder motor current{endif}
; support_material = 0
; support_material_angle = 0
; support_material_auto = 1
; support_material_bottom_contact_distance = 0
; support_material_bottom_interface_layers = 0
; support_material_buildplate_only = 0
; support_material_closing_radius = 2
; support_material_contact_distance = 0.2
; support_material_enforce_layers = 0
; support_material_extruder = 0
; support_material_extrusion_width = 0.38
; support_material_interface_contact_loops = 0
; support_material_interface_extruder = 0
; support_material_interface_layers = 2
; support_material_interface_pattern = rectilinear
; support_material_interface_spacing = 0.2
; support_material_interface_speed = 80%
; support_material_pattern = rectilinear
; support_material_spacing = 2
; support_material_speed = 45
; support_material_style = grid
; support_material_synchronize_layers = 0
; support_material_threshold = 50
; support_material_with_sheath = 0
; support_material_xy_spacing = 60%
; temperature = 205,205,205,205,230
; template_custom_gcode = 
; thick_bridges = 0
; thin_walls = 0
; threads = 8
; thumbnails = 160x120
; thumbnails_format = PNG
; toolchange_gcode = 
; top_fill_pattern = monotonic
; top_infill_extrusion_width = 0.45
; top_solid_infill_speed = 40
; top_solid_layers = 4
; top_solid_min_thickness = 0.7
; travel_speed = 180
; travel_speed_z = 12
; use_firmware_retraction = 0
; use_relative_e_distances = 1
; use_volumetric_e = 0
; variable_layer_height = 1
; wall_distribution_count = 1
; wall_transition_angle = 10
; wall_transition_filter_deviation = 25%
; wall_transition_length = 0.4
; wipe = 1,1,1,1,1
; wipe_into_infill = 0
; wipe_into_objects = 0
; wipe_tower = 1
; wipe_tower_bridging = 10
; wipe_tower_brim_width = 2
; wipe_tower_no_sparse_layers = 0
; wipe_tower_rotation_angle = 0
; wipe_tower_width = 60
; wipe_tower_x = 170
; wipe_tower_y = 125
; wiping_volumes_extruders = 70,70,70,70,70,70,70,70,70,70
; wiping_volumes_matrix = 0,140,140,140,140,140,0,140,140,140,140,140,0,140,140,140,140,140,0,140,140,140,140,140,0
; xy_size_compensation = 0
; z_offset = 0
; prusaslicer_config = end
'''

Turtle.LAYER_HEIGHT = 0.3
Turtle._elevation = Turtle.LAYER_HEIGHT - 0.1
Turtle._elevations = [0.0]
Turtle.PRUSA_OFFSET = (125, 125)
Turtle.PRUSA_DIMENSION = (250, 250, 210)
Turtle.gcodes = []
Turtle.layer_change_code = []
Turtle.history = [(0, 0)]

def _wipe(self, x, y, to_x, to_y):
    if len(self.gcodes) == 0:
        return
    dist = sqrt((to_x - x) ** 2 + (to_y - y) ** 2)
    if dist < 0.001:
        direction = (1, 0)
    else:
        direction = ((to_x - x) / dist, (to_y - y) / dist)
    if len(self.layer_change_code) > 0:
        layer_change = self.layer_change_code.pop()
    else:
        layer_change = {}
    if 'pre' in layer_change:
        self.gcodes.extend(layer_change['pre'])
    if dist < 2:
        self.gcodes.append(';WIPE_START')
        self.gcodes.append('G1 F8640')
        if dist < 0.001:
            reps = 0
        else:
            reps = 2
    else:
        self.gcodes.append('M204 S1000')
        self.gcodes.append(f'G1 X{x + self.PRUSA_OFFSET[0] + 0.2 * direction[0]:.3f} Y{y + self.PRUSA_OFFSET[1]+ 0.2 * direction[1]:.3f} F10800')
        self.gcodes.append(';WIPE_START')
        self.gcodes.append('G1 F8640')
        reps = 4
    for i in range(reps):
        offset = 0.4 * (i + 1)
        self.gcodes.append(f'G1 X{(x+ self.PRUSA_OFFSET[0] + offset * direction[0]):.3f} X{(y+ self.PRUSA_OFFSET[1] + offset * direction[1]):.3f} E-.20000')
    self.gcodes.append(';WIPE_END')
    self.gcodes.append('G1 E-.04 F2100')
    self.gcodes.append(f'G1 Z{self._elevation + self.LAYER_HEIGHT} F720')
    'after layer change'
    if 'post' in layer_change:
        self.gcodes.extend(layer_change['post'])
    
    self.gcodes.append(f'G1 X{to_x + self.PRUSA_OFFSET[0]:.3f} Y{to_y + self.PRUSA_OFFSET[1]:.3f} F10800')
    self.gcodes.append(f'G1 Z{self._elevation:.2f} F720')
    self.gcodes.append('G1 E.8 F2100')
    self.gcodes.append(';TYPE:Perimeter')
    self.gcodes.append(':WIDTH:0.419999')
    self.gcodes.append('M204 S800')
    self.gcodes.append('G1 F1200')

Turtle._wipe = _wipe

def _grbl_goto(self, x, y):
    x = float(x)
    y = float(y)
    ele = self._elevation * 4
    last_x = self._x
    last_y = self._y
    self._x = self._x + ele
    self._y = self._y + ele
    Turtle.__goto(self, x + ele, y + ele)
    self._position = (x, y)
    self._x = x
    self._y = y
    self.history.append((x, y))
    dist = sqrt((x - last_x) ** 2 + (y - last_y) ** 2)
    if self._drawing:
        if len(self.layer_change_code) > 0:
            self._wipe(x, y, x, y)        
        self.gcodes.append(f'G1 X{x + self.PRUSA_OFFSET[0]:.3f} Y{y + self.PRUSA_OFFSET[1]:.3f} E{(dist * self.LAYER_HEIGHT / 620):.5f}')
    else:
        # self.gcodes.append(f'G1 X{x:.3f} Y{y:.3f} F10800')
        self._wipe(last_x, last_y, x, y)

Turtle._goto = _grbl_goto

def _elevation(self, elevation = None):
    if elevation is None:
        return self._elevation
    if elevation < 0:
        elevation = 0.0
    if elevation == self._elevation:
        return
    last = Turtle._elevations[-1]
    self._elevation = elevation
    Turtle._elevations.append(elevation)
    pre = []
    pre.append(';LAYER_CHANGE')
    pre.append(f';Z:{self._elevation:.2f}')
    pre.append(f';HEIGHT:{elevation - last}')
    pre.append(';BEFORE_LAYER_CHANGE')
    pre.append(';G92 E0.0')
    pre.append(f';{self._elevation:.2f}')
    'WIPE'
    post = []
    post.append(';AFTER_LAYER_CHANGE')
    post.append(f';{self._elevation:.2f}')
    self.layer_change_code.append({'pre': pre, 'post': post})


    #self.goto(*self.pos())
Turtle.elevation = _elevation

def _level_up(self):
    self.elevation(self._elevation + self.LAYER_HEIGHT)
Turtle.level_up = _level_up

def _gcode(self):
    return '\n'.join([self.GRBL_PRUSA_START, *self.gcodes, self.GRBL_PRUSA_END]).replace('G1 Z0.', 'G1 Z.').replace(' E0.', ' E.')

Turtle.gcode = _gcode

'''LOCAL DEFS'''
Turtle._pen = Turtle()
def elevation(*args, **kw):
    return Turtle._pen.elevation(*args, **kw)
def level_up():
    return Turtle._pen.level_up()
def gcodes():
    return Turtle._pen.gcodes
def gcode():
    return Turtle._pen.gcode()

'''END DEFS'''
# speed(0)
# for i in range(20):
#     for j in range(4):
#         forward(8)
#         left(90)
#     penup()
#     goto(0, -20)
#     pendown()
#     setheading(0)
#     for j in range(6):
#         forward(8)
#         left(360 / 5)
#     level_up()
#     penup()
#     goto(0,0)
#     pendown()
#     setheading(0)

# print(gcode())