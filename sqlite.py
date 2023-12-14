import os
import django
import RPi.GPIO as GPIO 
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plante.settings")  
django.setup()

from appPlante.models import Measure

GPIO.setmode(GPIO.BCM)
RELAY_PIN1 = 24
RELAY_PIN2 = 25

GPIO.setup(RELAY_PIN1, GPIO.OUT)
GPIO.setup(RELAY_PIN2, GPIO.OUT)

def check_node(num_node, relay_pin):
    node_measure = Measure.objects.filter(num_node=num_node).latest('datetime')
    current_moist = node_measure.moist

    if current_moist > 2000:
        GPIO.output(relay_pin, GPIO.HIGH)
        print(f"Node {num_node}: La plante est sèche. Arrosage en cours pendant 5 secondes")
        time.sleep(5)
        GPIO.output(relay_pin, GPIO.LOW)
        print(f"Node {num_node}: Arrêt de l'arrosage.")
    else:
        GPIO.output(relay_pin, GPIO.LOW)
        print(f"Node {num_node}: Niveau d'humidité OK. Arrêt de l'arrosage.")

try:
    while True:
        check_node(1, RELAY_PIN1)  # Adjust the node number and relay pin accordingly
        check_node(2, RELAY_PIN2)  # Adjust the node number and relay pin accordingly
        time.sleep(5)  
except KeyboardInterrupt:
    GPIO.cleanup()
