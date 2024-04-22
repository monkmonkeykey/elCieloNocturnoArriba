import RPi.GPIO as GPIO
from pythonosc import dispatcher, osc_server
import neopixel
import Adafruit_GPIO.SPI as SPI
import board
import busio
import digitalio
import time


# Define el pin GPIO que deseas utilizar para PWM (por ejemplo, GPIO 13)
pin_lillyPad1 = 26
pin_lillyPad2 = 27
pin_lillyPad3 = 22
pin_lillyPad4 = 23
pin_lillyPad5 = 19
pin_lillyPad6 = 20

GPIO.setup(pin_lillyPad1, GPIO.OUT)
GPIO.setup(pin_lillyPad2, GPIO.OUT)
GPIO.setup(pin_lillyPad3, GPIO.OUT)
GPIO.setup(pin_lillyPad4, GPIO.OUT)
GPIO.setup(pin_lillyPad5, GPIO.OUT)
GPIO.setup(pin_lillyPad6, GPIO.OUT)
pwm_lillyPad1 = GPIO.PWM(pin_lillyPad1, 100)
pwm_lillyPad2 = GPIO.PWM(pin_lillyPad2, 100)
pwm_lillyPad3 = GPIO.PWM(pin_lillyPad3, 100)
pwm_lillyPad4 = GPIO.PWM(pin_lillyPad4, 100)
pwm_lillyPad5 = GPIO.PWM(pin_lillyPad5, 100)
pwm_lillyPad6 = GPIO.PWM(pin_lillyPad6, 100)

pwm_lillyPad1.start(0)
pwm_lillyPad2.start(0)
pwm_lillyPad3.start(0)
pwm_lillyPad4.start(0)
pwm_lillyPad5.start(0)
pwm_lillyPad6.start(0)

SCK = board.SCK
MOSI = board.MOSI
LATCH = digitalio.DigitalInOut(board.D5)

number_of_boards = 1
number_of_channels = number_of_boards * 6

spi = busio.SPI(clock=SCK, MOSI=MOSI)



pins = [0]*(number_of_channels)


#neopixel

num_neopixels = [4,4,3,3]
brillo = 1.0
constelacion_beatriz = neopixel.NeoPixel(board.D21, num_neopixels[0], brightness=brillo, auto_write=False)
constelacion_reynalda = neopixel.NeoPixel(board.D12, num_neopixels[1], brightness=brillo, auto_write=False)

#constelacion_beatriz = neopixel.NeoPixel(board.D10, num_pixels, brightness=brillo, auto_write=False)
#limpia neopixels
#constelacion_reynalda.deinit()
#constelacion_reynalda.deinit()

    
#valor = 0


def custom_map(value, start1, stop1, start2, stop2):
    """
    Mapea el valor desde el rango (start1, stop1) al rango (start2, stop2).
    """
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))



# Define funciones para manejar los mensajes OSC y controlar los LEDs
def manejar_led(address, *args):
    #print(f"Recibido mensaje desde {address}: {args}")
    #Comienza Beatriz
    if address == "/neopixel1Beatriz":
        #print(args[0])
        beatriz1_r = args[0]
        beatriz1_g = args[1]
        beatriz1_b = args[2]
        beatriz1_i = args[3]
        beatriz1_r_new  = custom_map(beatriz1_i, 0, 255, 0, beatriz1_r)
        beatriz1_g_new  = custom_map(beatriz1_i, 0, 255, 0, beatriz1_g)
        beatriz1_b_new  = custom_map(beatriz1_i, 0, 255, 0, beatriz1_b)
        constelacion_beatriz[0] = (beatriz1_r_new,beatriz1_g_new, beatriz1_b_new)
        constelacion_beatriz.show()
    elif address == "/neopixel2Beatriz":
        beatriz2_r = args[0]
        beatriz2_g = args[1]
        beatriz2_b = args[2]
        beatriz2_i = args[3]
        beatriz2_r_new  = custom_map(beatriz2_i, 0, 255, 0, beatriz2_r)
        beatriz2_g_new  = custom_map(beatriz2_i, 0, 255, 0, beatriz2_g)
        beatriz2_b_new  = custom_map(beatriz2_i, 0, 255, 0, beatriz2_b)
        constelacion_beatriz[1] = (beatriz2_r_new,beatriz2_g_new, beatriz2_b_new)
        constelacion_beatriz.show()
    elif address == "/neopixel3Beatriz":
        beatriz3_r = args[0]
        beatriz3_g = args[1]
        beatriz3_b = args[2]
        beatriz3_i = args[3]
        beatriz3_r_new  = custom_map(beatriz3_i, 0, 255, 0, beatriz3_r)
        beatriz3_g_new  = custom_map(beatriz3_i, 0, 255, 0, beatriz3_g)
        beatriz3_b_new  = custom_map(beatriz3_i, 0, 255, 0, beatriz3_b)
        constelacion_beatriz[2] = (beatriz3_r_new,beatriz3_g_new, beatriz3_b_new)
        constelacion_beatriz.show()
    elif address == "/neopixel4Beatriz":
        beatriz4_r = args[0]
        beatriz4_g = args[1]
        beatriz4_b = args[2]
        beatriz4_i = args[3]
        beatriz4_r_new  = custom_map(beatriz4_i, 0, 255, 0, beatriz4_r)
        beatriz4_g_new  = custom_map(beatriz4_i, 0, 255, 0, beatriz4_g)
        beatriz4_b_new  = custom_map(beatriz4_i, 0, 255, 0, beatriz4_b)
        constelacion_beatriz[3] = (beatriz4_r_new,beatriz4_g_new, beatriz4_b_new)
        constelacion_beatriz.show()
    #Comienza Reynalda
    elif address == "/neopixel1Reynalda":
        lynnette1_r = args[0]
        lynnette1_g = args[1]
        lynnette1_b = args[2]
        lynnette1_i = args[3]
        lynnette1_r_new  = custom_map(lynnette1_i, 0, 255, 0, lynnette1_r)
        lynnette1_g_new  = custom_map(lynnette1_i, 0, 255, 0, lynnette1_g)
        lynnette1_b_new  = custom_map(lynnette1_i, 0, 255, 0, lynnette1_b)
        constelacion_reynalda[0] = (lynnette1_r_new, lynnette1_g_new, lynnette1_b_new)
        constelacion_reynalda.show()
    elif address == "/neopixel2Reynalda":
        lynnette2_r = args[0]
        lynnette2_g = args[1]
        lynnette2_b = args[2]
        lynnette2_i = args[3]
        lynnette2_r_new  = custom_map(lynnette2_i, 0, 255, 0, lynnette2_r)
        lynnette2_g_new  = custom_map(lynnette2_i, 0, 255, 0, lynnette2_g)
        lynnette2_b_new  = custom_map(lynnette2_i, 0, 255, 0, lynnette2_b)
        constelacion_reynalda[1] = (lynnette2_r_new, lynnette2_g_new, lynnette2_b_new)
        constelacion_reynalda.show()
    elif address == "/neopixel3Reynalda":
        lynnette3_r = args[0]
        lynnette3_g = args[1]
        lynnette3_b = args[2]
        lynnette3_i = args[3]
        lynnette3_r_new  = custom_map(lynnette3_i, 0, 255, 0, lynnette3_r)
        lynnette3_g_new  = custom_map(lynnette3_i, 0, 255, 0, lynnette3_g)
        lynnette3_b_new  = custom_map(lynnette3_i, 0, 255, 0, lynnette3_b)
        constelacion_reynalda[2] = (lynnette3_r_new, lynnette3_g_new, lynnette3_b_new)
        constelacion_reynalda.show()
    elif address == "/neopixel4Reynalda":
        lynnette4_r = args[0]
        lynnette4_g = args[1]
        lynnette4_b = args[2]
        lynnette4_i = args[3]
        lynnette4_r_new  = custom_map(lynnette4_i, 0, 255, 0, lynnette4_r)
        lynnette4_g_new  = custom_map(lynnette4_i, 0, 255, 0, lynnette4_g)
        lynnette4_b_new  = custom_map(lynnette4_i, 0, 255, 0, lynnette4_b)
        constelacion_reynalda[3] = (lynnette4_r_new, lynnette4_g_new, lynnette4_b_new)
        constelacion_reynalda.show()
    elif address == "/led1Beatriz":
        led1 = args[0]
        led1 = custom_map(led1,0,255,0, 100)
        pwm_lillyPad1.ChangeDutyCycle(led1)
        
    elif address == "/led2Beatriz":
        led2 = args[0]
        led2 = custom_map(led2,0,255,0, 100)
        pwm_lillyPad2.ChangeDutyCycle(led2)
        
    elif address == "/led1Reynalda":
        led3 = args[0]
        led3 = custom_map(led3,0,255,0, 100)
        pwm_lillyPad3.ChangeDutyCycle(led3)
    elif address == "/led2Reynalda":
        led4 = args[0]
        led4 = custom_map(led4,0,255,0, 100)
        pwm_lillyPad4.ChangeDutyCycle(led4)
    elif address == "/led3Reynalda":
        led5 = args[0]
        led5 = custom_map(led5,0,255,0, 100)
        pwm_lillyPad5.ChangeDutyCycle(led5)
    elif address == "/led4Reynalda":
        led6 = args[0]
        led6 = custom_map(led6,0,255,0, 100)
        pwm_lillyPad6.ChangeDutyCycle(led6)
    #time.sleep(0.001)
    
# Crea un despachador de mensajes OSC
dispatcher = dispatcher.Dispatcher()

# Mapea las direcciones OSC a la función de manejo
direcciones_osc = ["/neopixel1Reynalda","/neopixel2Reynalda","/neopixel3Reynalda","/neopixel4Reynalda","/neopixel1Beatriz","/neopixel2Beatriz","/neopixel3Beatriz","/neopixel4Beatriz","/led1Beatriz","/led2Beatriz","/led1Reynalda","/led2Reynalda","/led3Reynalda","/led4Reynalda"]
for direccion in direcciones_osc:
    dispatcher.map(direccion, manejar_led)

# Configura y corre el servidor OSC en el hilo principal
ip_escucha = "0.0.0.0"  # Escucha en todas las interfaces de red
puerto_escucha = 8000   # Puerto en el que escucha el servidor

servidor = osc_server.BlockingOSCUDPServer((ip_escucha, puerto_escucha), dispatcher)
print(f"Escuchando en {ip_escucha}:{puerto_escucha}")

# Inicia el servidor
servidor.serve_forever()

# Detiene el PWM y limpia los pines GPIO al finalizar
pwm_lillyPad1.stop()
GPIO.cleanup()
