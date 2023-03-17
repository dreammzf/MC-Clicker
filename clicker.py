from tkinter import *

import pyautogui
import pyautogui as mouse
import keyboard

cps = 10
window = Tk()
window.iconbitmap("ico.ico")
sv = StringVar()
sv.set("10")
window.title("SimpleClicker")
window.geometry('360x250')
window.configure(background="#490098")

left_button_wait_for_key = False
right_button_wait_for_key = False
left_button_is_auto_clicking = False
right_button_is_auto_clicking = False
left_button_is_clicked = False
right_button_is_clicked = False
left_auto_click_key = 'z'
right_auto_click_key = 'x'


def left_button_autoclick():
	global left_button_is_auto_clicking
	if left_button_is_auto_clicking:
		left_button_is_auto_clicking = False
	else:
		left_button_is_auto_clicking = True


def right_button_autoclick():
	global right_button_is_auto_clicking
	if right_button_is_auto_clicking:
		right_button_is_auto_clicking = False
	else:
		right_button_is_auto_clicking = True


#Setting default buttons settings
keyboard.add_hotkey('z', left_button_autoclick)
keyboard.add_hotkey('x', right_button_autoclick)


def left_button_bind_press_key(event):
	global left_auto_click_key, left_button_is_clicked, left_button_wait_for_key
	try:
		if left_button_wait_for_key == True:
			if event.keysym == right_auto_click_key:
				return
			keyboard.remove_all_hotkeys()
			keyboard.add_hotkey(event.keysym, left_button_autoclick)
			left_auto_click_key = event.keysym
			left_click_button_bind.configure(text=event.keysym)
			left_click_button_bind.unbind_all(event)
			left_button_wait_for_key = False
			left_button_is_clicked = False
	except:
		return


def right_button_bind_press_key(event):
	global right_auto_click_key, right_button_is_clicked, right_button_wait_for_key
	try:
		if right_button_wait_for_key == True:
			if event.keysym == left_auto_click_key:
				return
			keyboard.remove_all_hotkeys()
			keyboard.add_hotkey(event.keysym, right_button_autoclick)
			right_auto_click_key = event.keysym
			right_click_button_bind.configure(text=event.keysym)
			right_click_button_bind.unbind_all(event)
			right_button_wait_for_key = False
			right_button_is_clicked = False
	except:
		return


def left_button_click(event):
	global left_button_is_clicked, right_button_is_clicked, left_button_wait_for_key, left_button_is_auto_clicking
	if right_button_is_clicked:
		return
	left_button_is_clicked = True
	left_button_is_auto_clicking = False
	left_click_button_bind.configure(text="Select a key")
	left_click_button_bind.bind_all('<Key>', left_button_bind_press_key)
	left_button_wait_for_key = True


def right_button_click(event):
	global left_button_is_clicked, right_button_is_clicked, right_button_wait_for_key, right_button_is_auto_clicking
	if left_button_is_clicked:
		return
	right_button_is_clicked = True
	right_button_is_auto_clicking = False
	right_click_button_bind.configure(text="Select a key")
	right_click_button_bind.bind_all('<Key>', right_button_bind_press_key)
	right_button_wait_for_key = True


def cps_value():
	global sv, cps, left_button_is_auto_clicking, right_button_is_auto_clicking
	if left_button_is_auto_clicking or right_button_is_auto_clicking or left_button_wait_for_key or right_button_wait_for_key:
		return
	try:
		if sv.get() == "":
			cps = 1
			sv.set("1")
			return
		value = int(sv.get())
		if value > 0 and value <= 100:
			cps = value
		else:
			sv.set(str(cps))
	except:
		sv.set(str(cps))
		return

#Configuring the style
left_click_text = Label(
	window,
	text="Left Button click",
	fg="#0000ff",
	bg="#7b68ee",
	font=("Comic Sans MS", 15)
)
right_click_text = Label(
	window,
	text="Right Button click",
	fg="#0000ff",
	bg="#7b68ee",
	font=("Comic Sans MS", 15)
)
cps_text = Label(
	window,
	text="CPS",
	fg="#0000ff",
	bg="#7b68ee",
	font=("Comic Sans MS", 25)
)
left_click_button_bind = Button(
	window,
	text="z (Default)",
	fg="#0000ff",
	bg="#7b68ee",
	font=("Comic Sans MS", 10),
	justify="center"
)
right_click_button_bind = Button(
	window,
	text="x (Default)",
	fg="#0000ff",
	bg="#7b68ee",
	font=("Comic Sans MS", 10),
	justify="center"
)
cps_text_input = Entry(
	window,
	text="20",
	fg="#0000ff",
	bg="#7b68ee",
	width="3",
	font=("Comic Sans MS", 25),
	textvariable=sv,
	validate="focusin",
	validatecommand=cps_value,
	justify="center"
)

#Configuring the properties
Grid.rowconfigure(window, 0, weight=1)
Grid.rowconfigure(window, 1, weight=1)
Grid.rowconfigure(window, 2, weight=1)
Grid.columnconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 1, weight=1)
left_click_text.grid(column=0, row=0, padx=20, pady=20)
right_click_text.grid(column=0, row=1, padx=20, pady=20)
cps_text.grid(column=0, row=2, padx=20, pady=20)
left_click_button_bind.grid(column=1, row=0)
left_click_button_bind.bind('<Button-1>', left_button_click)
right_click_button_bind.grid(column=1, row=1)
right_click_button_bind.bind('<Button-1>', right_button_click)
cps_text_input.grid(column=1, row=2)

#Clicking
while True:
	pyautogui.PAUSE = 1/cps
	if left_button_is_auto_clicking and not left_button_wait_for_key and not right_button_is_auto_clicking and not right_button_wait_for_key:
		mouse.click()
	if right_button_is_auto_clicking and not left_button_wait_for_key and not left_button_is_auto_clicking and not right_button_wait_for_key:
		pyautogui.PAUSE /= 2
		mouse.rightClick()
	#Getting the set cps value
	cps_value()
	window.update()
