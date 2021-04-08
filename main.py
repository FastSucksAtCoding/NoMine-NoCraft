'''
This game is just little fan made project of minecraft in python.
This game was never and never will be intended to make profit or any money from original title "Minecraft"
All rights goes to "Mojang"
Buy and download original game from: 
https://www.mincraft.net/en-us/download
'''

# Import
import time
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Game running test
running_text = "NoMine NoCraft is running succesfully."
running_text_line = "================================================================================="
print(running_text_line)
print(running_text)
print(running_text_line)


# Textures
app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
sand_texture  = load_texture('assets/sand_block.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)
block_pick = 1
time.sleep(1)
print("Textures loaded succesfully")

# Settings
window.title = "NoMine NoCraft"
window.borderless = True
window.fullscreen = True
window.fps_counter.enabled = True
window.exit_button.visible = False
time.sleep(1)
print("Settings loaded succesfully")

# UI 
Text.size = 0.05
Text.default_resolution = 1080 * Text.size
info = Text(text="V1.2")
info.x = -0.77
info.y = 0.47
info.background = True
info.visible = True

# Block pick
def update():
	global block_pick

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4
	if held_keys['5']: block_pick = 5
time.sleep(1)
print("Block pick loaded succesfully")

# Controls
class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)

	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				punch_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = sand_texture)

			if key == 'left mouse down':
				punch_sound.play()
				destroy(self)

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)
time.sleep(1)
print("Controls loaded succesfully")

# World size and spawn area
for z in range(29):
	for x in range(29):
		voxel = Voxel(position = (x,0,z))
time.sleep(1)
print("World size and spawn area loaded succesfully")

player = FirstPersonController()
sky = Sky()
hand = Hand()

# Run app
app.run()
time.sleep(1)
print("Application ran succesfully")