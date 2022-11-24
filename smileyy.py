from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = 255
g = 255
b = 255

sense.clear((r, g, b))

blue = (0, 0, 255)
yellow = (255,255,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)

sense.set_pixel(0,3,red)
sense.set_pixel(2,0,red)
sense.set_pixel(1,1,red)
sense.set_pixel(0,2,red)
sense.set_pixel(0,3,red)
sense.set_pixel(0,4,red)
sense.set_pixel(0,5,red)
sense.set_pixel(1,6,red)
sense.set_pixel(2,7,red)
sense.set_pixel(3,7,red)
sense.set_pixel(4,7,red)
sense.set_pixel(5,7,red)
sense.set_pixel(6,6,red)
sense.set_pixel(7,5,red)
sense.set_pixel(7,4,red)
sense.set_pixel(7,3,red)
sense.set_pixel(7,2,red)
sense.set_pixel(7,5,red)
sense.set_pixel(6,1,red)
sense.set_pixel(5,0,red)
sense.set_pixel(4,0,red)
sense.set_pixel(3,0,red)
sense.set_pixel(5,2,red)
sense.set_pixel(2,2,red)

sense.set_pixel(2,4,red)
sense.set_pixel(2,5,red)
sense.set_pixel(3,5,red)
sense.set_pixel(4,5,red)
sense.set_pixel(5,5,red)
sense.set_pixel(5,4,red)

#sense.set_pixel(2,4,black)
#sense.set_pixel(3,5,black)
#sense.set_pixel(4,5,black)
#sense.set_pixel(5,4,black)


#animal = "cat"
#score = 30

#sense.show_message("Hello world", text_colour=yellow, back_colour=blue, scroll_speed=0.01)
#sleep(5)
#sense.show_letter("E")
#sleep(2)
#sense.show_letter("L", red)
#sleep(1)
#sense.show_letter("a", blue)
#sleep(1)
#sense.show_letter("u", green)
#sleep(1)
#sense.show_letter("r", white)
#sleep(1)
#sense.show_letter("a", yellow)



