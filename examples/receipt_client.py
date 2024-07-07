from escpos.printer import Usb
from whisper_live.client import TranscriptionClient
import os
import subprocess
import time

last_text = []

p = Usb(0x0416, 0x5011, in_ep=0x81, out_ep=0x01, profile="POS-5890")
p.set(font='a', custom_size=True, width=1, height=2, flip=False)

def print_label(text):
    text = text.strip()
    print(text)
    p.textln(text + '\n\n')

def sample_callback(text, is_final):
  global last_text
  global client

  if is_final and text != last_text:
    # print(''.join(text), flush=True)
    print_label(''.join(text))
    last_text = text

client = TranscriptionClient(
  "localhost",
  9090,
  lang="en",
  translate=False,
  model="distil-small.en",
  use_vad=True,
  callback=sample_callback
)

client()
