#!/usr/bin/env python3
import time, random, subprocess, sys

def type_text(text, min_ms=65, max_ms=130):
    for ch in text:
        subprocess.run(["xdotool", "type", "--delay", str(random.randint(min_ms, max_ms)), ch])
        time.sleep(random.uniform(0.03, 0.09))

def backspace(count=1):
    time.sleep(0.38)
    for _ in range(count):
        subprocess.run(["xdotool", "key", "BackSpace"])
        time.sleep(0.08)
    time.sleep(0.25)

def human_type_with_typo(before_typo, typo_str, fix_str, after_text=""):
    type_text(before_typo + typo_str)
    backspace(len(typo_str))
    type_text(fix_str + after_text)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "skill"
    if mode == "skill":
        human_type_with_typo("ux-p", "resona", "ersona-builder")
    elif mode == "prompt1":
        human_type_with_typo("Identf", "iy the most obviosu", "y the most obvious customer persona and use case from the Mercury CRM data packet.")
    elif mode == "prompt2":
        human_type_with_typo("Look past the dom", "niant", "inant pattern for a non-obvious B2B customer persona and use case.")
