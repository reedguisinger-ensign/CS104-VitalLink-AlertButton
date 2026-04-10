import time
import requests
import RPi.GPIO as GPIO

bot_token = "8729286542:AAGaDC22Dfhb5xyetYXZVgvl30OdOXoI74s"
chat_id = "8606788019"

def send_telegram_message(text):
	url = f"https://api.telegram.org/bot8729286542:AAGaDC22Dfhb5xyetYXZVgvl30OdOXoI74s/sendMessage"
	payload = {
		"chat_id": 8606788019,
		"text": text
	}
	try:
		requests.post(url, data=payload)
	except Exception as e:
		print("Error sending message:", e)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	if GPIO.input(7) == GPIO.HIGH and not button_pressed:
		print("Someone pressed the alert button!")
		send_telegram_message("Someone pressed the alert button!")
		button_pressed = True
	elif GPIO.input(7) == GPIO.LOW:
		button_pressed = False
	time.sleep(0.1)
