#importing, install pygame in cmd ---> pip install pygame, or try in web
import pygame, sys, os

#importing - You need to install pytmx in terminal ---> pip install pytmx
from pytmx.util_pygame import load_pygame

# os.system('cls' if os.name == 'nt' else 'clear') - clears cmd for any os

#Creating class tile (square) - inheritet from class Sprite 
class Tile(pygame.sprite.Sprite):
    def __init__ (self, pos, surf, groups):
        super().__init__(groups)
         
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

sprite_group = pygame.sprite.Group()

pygame.init()

screen = pygame.display.set_mode((1000, 800))

#loading file
tmx_data = load_pygame(r'C:\Users\Uzivatel\PygameTiled\Practice\map.tmx')

#cycle trough all LAYERS
for layer in tmx_data.layers:
    if hasattr(layer, 'data'): #checks if object isnt empty and has info(atribute) in it
        for x, y, surf in layer.tiles():
            pos = (x * 32, y * 32) #multiplied by pixels of tile to get true coordinates
            Tile(pos = pos, surf = surf, groups = sprite_group)

#cycle trough all OBJECTS
for obj in tmx_data.objects:
    pos = obj.x, obj.y
    Tile(pos = pos, surf = obj.image, groups = sprite_group)

#---< USEFUL COMMANDS BELOW >-----------------------------

# #print(tmx_data.layers) - prints all layers except object layers

# for layer in tmx_data.visible_layers: #get only visible layers
#    print(layer)

# #print(dir(tmx_data)) 
# layer = tmx_data.get_layer_by_name('Ground')
# for x, y, surf in layer.tiles(): - #get all info about tile
#   print(f"x: {x*32}, y:{y*32}, Surface: {surf}")

# #print(layer.name, layer.id)

# object_layer = tmx_data.get_layer_by_name('Recources')
# for obj in object_layer:
#     if obj.type == 'Recources':
#         if obj.name == 'stone':
#             print(obj)
#             print(obj.x)
#             print(obj.y)
#             print(obj.width)
#             print(obj.width)
#---------------------------------------------------------
#surf - image of 2d obj, like, tile, sprite, obj, etc.
#attribute - info stored in objects

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    sprite_group.draw(screen)
    pygame.display.update()