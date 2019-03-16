#!/usr/bin/env python3
#coding:utf-8
from midiutil import MIDIFile

track    = 0
string   = "Sur le fond de mes nuits Dieu de son doigt savant Dessine un cauchemar multiforme et sans trêve."
channel  = 0
time     = 0
duration = 1 
tempo    = 166
volume   = 100 
string = string.replace(" ", "")
string = string.upper()
array = list(string)
MyMIDI = MIDIFile(1)
for x in range(0, len(array)):
    print(ord(array[x]))
    MyMIDI.addNote(track, channel, ord(array[x]), time + x, duration, volume)

with open("Charles Baudelaire.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
print(array)

