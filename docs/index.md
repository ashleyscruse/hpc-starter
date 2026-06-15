# HPC Starter

Welcome. By the end of this short walkthrough you will have logged into a supercomputer, moved around its files, edited a program, run it, and organized a dataset. No prior experience needed, and **you cannot break anything**.

This is about getting *comfortable* on the system. The heavy computing comes later. Today is just "I can find my way around."

## What you'll do

1. **Look around** and get your bearings
2. **Make** your own folder, by hand
3. **Clone** a ready-made setup (instead of building it by hand)
4. **Edit** a Python script with `nano`
5. **Run** your script (a hello world)
6. **Copy** a dataset into your workspace

First, a quick tour of the machine itself.

## Before you start: open a terminal on Vista

You need a terminal connected to Vista. Your instructor will walk you through logging in.

### Mac or Windows? It stops mattering once you're in

Good news: every command in this walkthrough runs on **Vista's Linux**, not on your laptop. So Mac or PC, once you're connected, everything is identical. The only thing that differs is how you open a terminal and connect:

- **Easiest for everyone:** use the terminal built into the **Tapis web portal** at [morehouse.tapis.io](https://morehouse.tapis.io). It runs in your browser, so your laptop's operating system doesn't matter at all.
- **On a Mac:** open the **Terminal** app and run this *on your laptop*:
  ```bash
  ssh taccusername@vista.tacc.utexas.edu
  ```
- **On Windows:** open **Windows Terminal** or **PowerShell** and run the same command *on your laptop*:
  ```bash
  ssh taccusername@vista.tacc.utexas.edu
  ```

Once your prompt looks something like `username@login2 $`, you're on Vista. From here on, **everyone types the exact same commands.** 🎉

## A few comforting facts

- You are on a **login node** right now. That's fine for everything in this walkthrough.
- If a command doesn't work, nothing breaks. Read the message, fix the typo, try again.
- Stuck for more than a minute? Ask. That's what we're here for.

Ready? Start with [Meet the Machine](./system-tour).
