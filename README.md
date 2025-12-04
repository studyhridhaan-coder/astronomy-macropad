# astronomy-macropad

A custom 6-key macropad built specifically for astronomy and telescope workflows.
Designed for fast, night-friendly control of capture modes, tracking, plate solving and other repetitive tasks — without touching a laptop in the dark.

Features

RP2040 microcontroller for fast, low-latency input

OLED Status Display

Shows mode, capture status, focus info, etc.

RGB Underglow (low-brightness night mode)

6-Key Layout optimized for astronomy

Custom Firmware (KMK or custom Python-based firmware planned)

USB Interface for telescope software & imaging tools


 Layout Sketch

(Early concept — will refine during PCB stage)

![Sketch](assets/sketch.png)


Hardware Plan
Microcontroller

Raspberry Pi RP2040

Peripherals

0.96" OLED Display (I2C)

6 × Mechanical Switches (hot-swap optional)

RGB LED strip (WS2812/Neopixel)

USB-C connector

Custom-designed PCB

Case

3D-printed enclosure (PLA/ABS)

Top shell + bottom plate


Firmware Plan

Language: MicroPython / CircuitPython (KMK firmware)

Features planned:

Custom keymaps

OLED status rendering

RGB modes (night mode, alerts)

Telescope shortcuts (ASIAIR / NINA / DSLR capture)

Mode switching (via special key or combo)

Build Roadmap
Phase 1 — Concept & Layout

✔ Sketch
 Component selection
 First PCB draft

Phase 2 — Electronics

 Schematic
 PCB design
 Ordering PCB + parts

Phase 3 — Firmware

 Basic key input
 OLED display driver
 Telescope macro integration

Phase 4 — Enclosure

 3D model
 Print + fit testing

Phase 5 — Final Build

 Assembly
 Live testing under night sky
 Final documentation

 Demo (Coming Soon)

PCB renders

Firmware logs

Night sky workflow videos

Author
Hridhaan Sahay

