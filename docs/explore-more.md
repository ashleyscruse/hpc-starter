# Explore More (Optional)

Finished early? Here are some power moves. None of these are required, they're just fun and useful.

**Make a file without opening an editor:**

```bash
echo "I was here" > note.txt
cat note.txt
```

The `>` sends a command's output into a file. You just created a file in one line.

**Search inside a file** with `grep`:

```bash
grep TX examples/cities.csv
```

That finds every line containing "TX". Try a different state.

**Connect commands with a pipe** (`|`):

```bash
ls -l | wc -l
```

This counts how many things are in the folder: `ls -l` lists them, and `|` feeds that into `wc -l`, which counts the lines. Pipes are how small commands combine into powerful ones.

**Get help on any command:**

```bash
ls --help
man ls
```

`man` opens the manual (press `q` to quit). Every command has one.

💡 **Handy keys:** up-arrow repeats your last command, `history` shows everything you've typed, `clear` wipes the screen, and `Ctrl + C` cancels a command that's running.

✅ **Checkpoint.** You created a file with `echo`, searched with `grep`, used a pipe, and found built-in help.

Next: [More Than One Way In](./07-many-ways-in)
