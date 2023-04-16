import pygame

def sigmoid_function(x,a=1,b=1):
    # シグモイド関数
    if abs(a) < 0.01:
        y = 0
    else:
        y = a - 1 / (1 + math.e**-(1/b*abs(x)))
    return y

def acute_angle(base_vector:pygame.math.Vector2,target_vector:pygame.math.Vector2):
    if base_vector.cross(target_vector) >= 0:
        return base_vector.angle_to(target_vector)
    if base_vector.cross(target_vector) < 0:
        return -target_vector.angle_to(base_vector)
      
up = pygame.math.Vector2(0,-1)
right = pygame.math.Vector2(1,0)
rightdown = pygame.math.Vector2(1,1)
down = pygame.math.Vector2(0,1)
left = pygame.math.Vector2(-1,0)
leftdown = pygame.math.Vector2(-1,1)


cross = up.cross(rightdown)
angle = up.angle_to(rightdown)

print(up.rotate(45))

print(cross)
print(angle)

print(360 + right.angle_to(up))