# Look Around

Let's get our bearings on the system before we make anything. Three commands do most of the navigating.

**Where am I?**

```bash
pwd
```

This prints your current location (the "path").

**What's here?**

```bash
ls
ls -lh
ls -lat
```

`ls` lists files. `-lh` adds sizes in human-readable form. `-lat` sorts by most recent.

**Move between your spaces:**

```bash
cd $HOME
pwd
cd $WORK
pwd
```

`$HOME` is your small, backed-up space. `$WORK` is where your projects live. You'll spend your time in `$WORK`.

**Go up, home, or back:**

```bash
cd ..
cd ~
cd -
```

**Checkpoint.** You can see where you are and move between `$HOME` and `$WORK`.

**Tip:** Start typing a file or folder name and press **Tab**. The system finishes it for you, fewer typos, less typing.

Next: [Make a Folder](./03-make-a-folder)
