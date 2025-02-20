import os

def display_led(intensity):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("LED Intensity Control")
    print("[" + "#" * intensity + " " * (10 - intensity) + "]", f" {intensity * 10}%")

def main():
    intensity = 5  # Start at 50%
    while True:
        display_led(intensity)
        key = input("Press '+' to increase, '-' to decrease, 'q' to quit: ")
        if key == 'q':
            break
        elif key == '+' and intensity < 10:
            intensity += 1
        elif key == '-' and intensity > 0:
            intensity -= 1

main()
