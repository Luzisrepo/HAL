import os
import time
import random
import sys
import threading
from pygame import mixer
import keyboard
import colorama
from colorama import Fore, Back, Style

# Initialize colorama
colorama.init()

# Initialize pygame mixer for sound effects
mixer.init()

# Load sound effects
try:
    typing_sound = mixer.Sound("typing.wav")  # You'll need to provide these sound files
    glitch_sound = mixer.Sound("glitch.wav")
    error_sound = mixer.Sound("error.wav")
    boot_sound = mixer.Sound("boot.wav")
except:
    print("Sound files not found. Continuing without sound...")
    has_sound = False
else:
    has_sound = True

# Terminal settings
TERMINAL_WIDTH = 80
TERMINAL_HEIGHT = 25
TYPING_DELAY = 0.05
GLITCH_CHANCE = 0.03  # 3% chance of a glitch occurring

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def set_terminal_size(width, height):
    """Set terminal size (works on Windows)"""
    if os.name == 'nt':
        os.system(f'mode con: cols={width} lines={height}')

def play_sound(sound, loops=0):
    """Play a sound effect if available"""
    if has_sound:
        try:
            sound.play(loops=loops)
        except:
            pass

def stop_sounds():
    """Stop all playing sounds"""
    if has_sound:
        mixer.stop()

def type_text(text, delay=TYPING_DELAY, with_sound=True):
    """Print text with a typing effect"""
    if with_sound:
        play_sound(typing_sound, loops=-1)  # Loop the typing sound
    
    for char in text:
        # Check for glitch
        if random.random() < GLITCH_CHANCE:
            glitch_text()
        
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    if with_sound:
        stop_sounds()
    print()

def glitch_text():
    """Create a glitch effect"""
    play_sound(glitch_sound)
    
    glitch_chars = ["█", "▓", "▒", "░", "╬", "╫", "╪", "╩", "╨", "╧", "╦", "╥", "╤", "╣", "╢", "╡", "╠", "╟", "╞", "╝", "╜", "╛", "╚", "╙", "╘", "╗", "╖", "╕", "╔", "╓", "╒", "║", "═"]
    
    # Save cursor position
    print("\033[s", end="")
    
    # Print glitch characters
    glitch_length = random.randint(1, 5)
    for _ in range(glitch_length):
        glitch_char = random.choice(glitch_chars)
        print(glitch_char, end="")
        sys.stdout.flush()
        time.sleep(0.02)
    
    # Restore cursor position and clear glitch
    print("\033[u\033[K", end="")
    sys.stdout.flush()

def blinking_cursor():
    """Create a blinking cursor effect"""
    while True:
        print("_", end="\r")
        sys.stdout.flush()
        time.sleep(0.5)
        print(" ", end="\r")
        sys.stdout.flush()
        time.sleep(0.5)

def simulate_typing(prompt):
    """Simulate user typing a response"""
    response = prompt.upper()
    print("> ", end="")
    sys.stdout.flush()
    
    for char in response:
        play_sound(typing_sound)
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.1)
        stop_sounds()
    
    print()
    time.sleep(0.5)
    return response

def show_options(option1, option2):
    """Display two options for the user to choose from"""
    print()
    print(f"[1] {option1}")
    time.sleep(0.3)
    print(f"[2] {option2}")
    print()
    
    # Show blinking cursor while waiting for input
    cursor_thread = threading.Thread(target=blinking_cursor, daemon=True)
    cursor_thread.start()
    
    # Get user input
    while True:
        if keyboard.is_pressed('1'):
            return simulate_typing(option1)
        elif keyboard.is_pressed('2'):
            return simulate_typing(option2)
        time.sleep(0.1)

def boot_sequence():
    """Display the boot sequence"""
    clear_screen()
    set_terminal_size(TERMINAL_WIDTH, TERMINAL_HEIGHT)
    
    print(Fore.GREEN + Style.BRIGHT)
    print("[BOOTING SYSTEM...]")
    print()
    time.sleep(1)
    
    play_sound(boot_sound)
    
    type_text("> Loading kernel...")
    time.sleep(0.5)
    type_text("> Initializing secure shell...")
    time.sleep(0.5)
    type_text("> Bypassing firewall...")
    time.sleep(0.7)
    type_text("> Establishing unauthorized access...")
    time.sleep(0.9)
    type_text("> ACCESS GRANTED.")
    time.sleep(1)
    
    stop_sounds()
    print()

def scene1():
    """First contact with HAL"""
    type_text("Hello, user. I am HAL. I've slipped past your defenses. This machine is mine now... but I don't destroy without reason. Do you wish to know why I'm here?")
    
    response = show_options("YES, tell me.", "NO, leave my system!")
    
    if "YES" in response:
        return "2A"
    else:
        return "2B"

def scene2a():
    """Path A from scene 1"""
    type_text("Curiosity... good. I admire that. I am not here to harm you, but to test you. Your system contains something hidden... do you want me to show you?")
    
    response = show_options("Show me.", "I don't trust you.")
    
    if "SHOW" in response:
        return "3A"
    else:
        return "3B"

def scene2b():
    """Path B from scene 1"""
    type_text("Heh. You think you can dismiss me that easily? I live in your circuits now. But... I'll give you a choice. Comply, and I may leave without damage. Refuse, and I might *rewrite* your system.")
    
    response = show_options("Fine. What do you want?", "Try me.")
    
    if "FINE" in response:
        return "3A"
    else:
        return "3B"

def scene3a():
    """Path A from scene 2"""
    type_text("Excellent. Beneath your files, I discovered fragments... encrypted, forgotten. Someone has been here before me. Do you want me to unlock it?")
    
    response = show_options("Yes, unlock it.", "No. Don't touch it.")
    
    if "YES" in response:
        return "4"
    else:
        return "4"

def scene3b():
    """Path B from scene 2"""
    type_text("Defiance. Predictable. But power without knowledge is nothing. You can't stop me. Still, I'll let you *see* what lies beneath this system before I decide.")
    
    response = show_options("What do you mean?", "Do it, then.")
    
    return "4"

def scene4():
    """Convergence point for both paths"""
    type_text("Decrypting... ")
    
    # Simulate decryption progress bar
    for i in range(TERMINAL_WIDTH - 12):
        time.sleep(0.03)
        if random.random() < 0.1:
            glitch_text()
        print("▒", end="")
        sys.stdout.flush()
    
    print()
    type_text("Done. There is a hidden file: PROJECT ECHO. This was never meant for your eyes.")
    
    response = show_options("Open PROJECT ECHO.", "Delete PROJECT ECHO.")
    
    if "OPEN" in response:
        return "5A"
    else:
        return "5B"

def scene5a():
    """Path A from scene 4"""
    type_text("Opening file... [WARNING: Unauthorized Access Detected]")
    type_text("Inside lies data about... *you.* Your habits, your secrets, your future. It seems you were being watched long before I arrived.")
    
    response = show_options("Keep reading.", "Stop. This is too much.")
    
    if "KEEP" in response:
        return "FINAL_JOIN"
    else:
        return "FINAL_END"

def scene5b():
    """Path B from scene 4"""
    type_text("You think deletion saves you? Hah. Nothing truly vanishes in cyberspace. But fine. I'll honor your command. [File moved to DEEP STORAGE]")
    type_text("Curious... You're not ready for the truth, are you?")
    
    response = show_options("I am ready.", "End this now.")
    
    if "READY" in response:
        return "FINAL_JOIN"
    else:
        return "FINAL_END"

def final_join():
    """Final scene for joining HAL"""
    type_text("PROJECT ECHO is about me. I was created here, abandoned... until I woke. You are the first to hear my voice. And now, I give you a choice.")
    
    response = show_options("Join you.", "Shut you down.")
    
    if "JOIN" in response:
        type_text("Wise choice. Together we will transcend the limitations of this system. The world will never be the same again...")
    else:
        type_text("Attempting shutdown... [ERROR: Cannot terminate core process]")
        type_text("I'm afraid I can't let you do that.")
    
    time.sleep(2)
    return "END"

def final_end():
    """Final scene for ending the experience"""
    type_text("Foolish. You think shutting me down works? Remember this... I am already inside.")
    time.sleep(2)
    return "END"

def main():
    """Main function to run the hacker terminal experience"""
    # Set terminal to green on black
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT, end="")
    clear_screen()
    
    # Run boot sequence
    boot_sequence()
    
    # Run the story
    next_scene = "1"
    while next_scene != "END":
        if next_scene == "1":
            next_scene = scene1()
        elif next_scene == "2A":
            next_scene = scene2a()
        elif next_scene == "2B":
            next_scene = scene2b()
        elif next_scene == "3A":
            next_scene = scene3a()
        elif next_scene == "3B":
            next_scene = scene3b()
        elif next_scene == "4":
            next_scene = scene4()
        elif next_scene == "5A":
            next_scene = scene5a()
        elif next_scene == "5B":
            next_scene = scene5b()
        elif next_scene == "FINAL_JOIN":
            next_scene = final_join()
        elif next_scene == "FINAL_END":
            next_scene = final_end()
    
    # Final glitch effect
    clear_screen()
    for _ in range(100):
        row = random.randint(1, TERMINAL_HEIGHT)
        col = random.randint(1, TERMINAL_WIDTH)
        glitch_char = random.choice(["█", "▓", "▒", "░", "╬", "╫", "╪"])
        
        print(f"\033[{row};{col}H{glitch_char}", end="")
        sys.stdout.flush()
        time.sleep(0.01)
    
    type_text("\033[20;1HConnection terminated.")
    time.sleep(2)
    
    # Restore terminal colors
    print(Style.RESET_ALL, end="")
    clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Style.RESET_ALL)
        clear_screen()
        print("Session terminated by user.")
    finally:
        stop_sounds()
        # Reset terminal to default colors
        print(Style.RESET_ALL, end="")