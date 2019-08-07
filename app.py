from flask import Flask, render_template, request, redirect, url_for, make_response
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import motors
import steering
import socket

motors.stop()
steering.straight()

# Get server ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()

app = Flask(__name__) 

@app.route('/')
def index():

	return render_template('/index.html', server_ip=server_ip)

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin) 

	if changePin == 1:
		steering.turnLeft()
	elif changePin == 2:
		steering.straight()
	elif changePin == 3:
		steering.turnRight()
	elif changePin == 4:
		motors.forward()
	elif changePin == 5:
		motors.stop()
        elif changePin == 6:
		motors.backward()
	else:
		print("Wrong command")

	response = make_response(redirect(url_for('index')))
	return(response)

app.run(debug=True, host='0.0.0.0', port=8000) 
