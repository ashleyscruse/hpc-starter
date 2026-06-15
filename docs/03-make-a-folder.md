# Step 1: Make a Folder

Let's set up a workspace, by hand, so you see how it's done.

Go to `$WORK`, where your projects live:

```bash
cd $WORK
```

Make a project folder:

```bash
mkdir my-project
```

Move into it and check where you are:

```bash
cd my-project
pwd
```

Make a `data` folder inside it:

```bash
mkdir data
ls
```

You should see your new `data` folder.

Go back up one level:

```bash
cd ..
```

✅ **Checkpoint.** You built `my-project/` with a `data/` folder inside, in `$WORK`.

💡 **Tip:** `cd ..` goes up one folder, `cd ~` takes you home, `cd -` jumps back to where you just were.

Next: [Step 2: Clone a Setup](./01-clone)
