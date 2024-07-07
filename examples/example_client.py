from whisper_live.client import TranscriptionClient
import os
import time

last_text = []

def sample_callback(text, is_final):
  global last_text
  global client

  if is_final and text != last_text:
    print(''.join(text), flush=True)
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
