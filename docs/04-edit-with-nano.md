# Step 3: Edit a Script with nano

`nano` is a simple text editor that lives in the terminal. No mouse, just the keyboard.

Make sure you're in the project you cloned, then open the Python script:

```bash
cd $WORK/hpc-starter
nano hello.py
```

You'll see the file, with a menu of commands at the bottom. Find this line:

```python
message = "Hello from the supercomputer!"
```

Change the text between the quotes to your own greeting, for example:

```python
message = "Hello! This is <your name> on Vista."
```

### Saving and exiting (the part everyone gets stuck on)

In nano, `^` means the **Ctrl** key.

1. **Save:** press **Ctrl + O** (the letter O, for "write Out"), then press **Enter** to confirm.
2. **Exit:** press **Ctrl + X**.

That's it. You're back at the prompt.

✅ **Checkpoint.** Run `cat hello.py` and confirm your new message is in there.

💡 **Tip:** If you ever feel trapped in a terminal editor, **Ctrl + X** (nano) gets you out. Save first if you want to keep changes.

Next: [Step 4: Run Your Script](./05-run-it)
