from sys import argv    
from os import system 
import png
#=========================================================================
#files:
#default_env.tres =text1
#project.godot= tex2+NN+tex3
#copy icon.png
#=========================================================================
tex1='''[gd_resource type="Environment" load_steps=2 format=2]
[sub_resource type="ProceduralSky" id=1]
[resource]
background_mode = 2
background_sky = SubResource( 1 )''' 
#=========================================================================
f = open("default_env.tres", "w")
f.write(tex1)
f.close()
#=========================================================================
tex2='''; Engine configuration file.
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
tex3='''"
config/icon="res://icon.png"

[physics]

common/enable_pause_aware_picking=true

[rendering]

environment/default_environment="res://default_env.tres"'''
#=========================================================================
texNN=""
limite=len(argv)
print(argv)
contador=1
#----------------------------------
while limite>contador:
    if len(texNN)==0:
        texNN=argv[contador]
    else:
        texNN=texNN+" "+argv[contador]
    contador=contador+1
#-----------------------------------
print(texNN)
if texNN=="":
    texNN="New Project"
#=========================================================================
f = open("project.godot", "w")
f.write(tex2+texNN+tex3)
f.close()
#=========================================================================
width = 255  #creando icono
height = 255
img = []
for y in range(height):
    row = ()
    for x in range(width):
        row = row + (x, max(0, 255 - x - y), y)
    img.append(row)
with open('icon.png', 'wb') as f:
    w = png.Writer(width, height, greyscale=False)
    w.write(f, img)
#=========================================================================
system("godot -e")
#=========================================================================
print("New godot project "+texNN+" created!!")
#=========================================================================
