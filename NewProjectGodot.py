


#=========================================================================
#files:
#default_env.tres =text1
#project.godot= tex2+NN+tex3
#copy icon.png
#=========================================================================
tex1:="""[gd_resource type="Environment" load_steps=2 format=2]
[sub_resource type="ProceduralSky" id=1]
[resource]
background_mode = 2
background_sky = SubResource( 1 )"""
#=========================================================================
tex2:='''; Engine configuration file.
; It's best edited using the editor UI and not directly,
; since the parameters that go here are not all obvious.
;
; Format:
;   [section] ; section goes between []
;   param=value ; assign values to parameters

config_version=4

[application]

config/name="'''
#=========================================================================
tex3:='''"
config/icon="res://icon.png"

[physics]

common/enable_pause_aware_picking=true

[rendering]

environment/default_environment="res://default_env.tres"'''
#=========================================================================








