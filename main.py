import random
import time
import pyautogui
import keyboard
import threading
import math


def random_click():
    x, y = pyautogui.position()
    pyautogui.click(x, y)


def check_hotkeys(keep_clicking_list, session_paused_list, delay_range):
    while True:
        if keyboard.is_pressed('f6'):
            keep_clicking_list[0] = True
            session_paused_list[0] = False  
            print("Auto-clicker enabled.")
            delay_range[0] = round(max(0.034211235631, delay_range[0] - random.uniform(0.014215356, 0.061231785)), 2)
            delay_range[1] = round(min(0.32681416132412498251, delay_range[1] + random.uniform(0.016345753, 0.041454345)), 2)
            print(f"New delay range: ({delay_range[0]}, {delay_range[1]})")
        elif keyboard.is_pressed('f7'):
            keep_clicking_list[0] = False
            print("Auto-clicker disabled.")
        time.sleep(0.1)


def start_new_session(keep_clicking_list, session_paused_list, delay_range):
    num_clicks_session = random.randint(3400, 4600)
    print(f"Auto-clicker will run for {num_clicks_session} clicks.")

    initial_min_delay = delay_range[0]
    initial_max_delay = delay_range[1]

    clicks_before_pause = random.randint(1, 95)  
    total_clicks = 0
    pause_counter = 0
    mouse_move_counter = 0  

    while total_clicks < num_clicks_session:
        if not keep_clicking_list[0]:
            break

        if total_clicks % 1 == 0 and total_clicks!= 0:
            delay_range[0] = round(max(0.0342112356, delay_range[0] + random.uniform(-0.0085716236, 0.00912451)), 2)
            delay_range[1] = round(min(0.32681416132412498251, delay_range[1] + random.uniform(-0.0084511217, 0.00926321)), 2)
            print(f"New delay range: ({delay_range[0]}, {delay_range[1]})")

        random_click()
        delay = random.uniform(delay_range[0], delay_range[1])
        time.sleep(delay)
        total_clicks += 1
        pause_counter += 1
        mouse_move_counter += 1

        if pause_counter >= clicks_before_pause:
            pause_duration = random.uniform(0.0944156793, 34.6142141907)  
            print(f"Pausing for {pause_duration:.2f} seconds...")
            time.sleep(pause_duration)
            pause_counter = 0  
            clicks_before_pause = random.randint(1, 257)  

            if mouse_move_counter >= random.randint(1, 78):
                mouse_move_counter = 0
                current_x, current_y = pyautogui.position()
                distance = random.uniform(2, 35)  
                angle = random.uniform(0, 360)  

                angle_in_radians = math.radians(angle)

                new_x = current_x + distance * math.cos(angle_in_radians)
                new_y = current_y + distance * math.sin(angle_in_radians)

                move_duration = random.uniform(0.097246531, 0.247537221)  
                pyautogui.moveTo(new_x, new_y,
                                 duration=move_duration)  
                print("Mouse slightly moved.")

    delay_range[0] = initial_min_delay
    delay_range[1] = initial_max_delay

    keep_clicking_list[0] = False  
    session_paused_list[0] = True  


keep_clicking = [False]
session_paused = [False]

delay_range = [0.0523809, 0.28557455345812]

hotkey_thread = threading.Thread(target=check_hotkeys, args=(keep_clicking, session_paused, delay_range))
hotkey_thread.daemon = True  
hotkey_thread.start()

while True:
    if keep_clicking[0]:
        start_new_session(keep_clicking, session_paused, delay_range)

    elif session_paused[0]:  
        print("Waiting for auto-clicker restart...", end='\r')
        time.sleep(0.1)  
        if keep_clicking[0]:  
            session_paused[0] = False  
            start_new_session(keep_clicking, session_paused, delay_range)

    else:
        time.sleep(0.1)
