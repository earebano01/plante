################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

GPIO.setmode(GPIO.BCM)
RELAY_PIN1 = 24
RELAY_PIN2 = 25

GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
Request = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global Request
    messagetosend = bytes('HELLO WORD',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    Request = self.requestline
    Request = Request[5 : int(len(Request)-9)]
    print(Request)
    if Request == 'on':
      GPIO.output(RELAY_PIN1, GPIO.HIGH)
    if Request == 'off':
      GPIO.output(RELAY_PIN1, GPIO.LOW)
    if Request == 'oui':
      GPIO.output(RELAY_PIN2, GPIO.HIGH)
    if Request == 'non':
      GPIO.output(RELAY_PIN2, GPIO.LOW)
    return


server_address_httpd = ('192.168.1.206',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Starting')
httpd.serve_forever()
GPIO.cleanup()
