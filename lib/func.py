#functions

import math
import pygame

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def isPrime(num):
	if num < 2:
		return False
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True


def drawLines(screen, screen_width, screen_height):
        pygame.draw.line(screen, WHITE, [0, 0] , [screen_width, screen_height], 5)

def advance(digit):
    if digit <= 8:
        digit += 1
        return digit
    if digit == 9:
        digit = 0
        return digit

