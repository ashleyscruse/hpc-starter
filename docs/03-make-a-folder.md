# Step 3: Make a Folder

Organizing your work is a real skill on HPC. Let's make a folder for a project.

**Create a folder:**

```bash
mkdir my-project
```

**Move into it:**

```bash
cd my-project
```

Check where you are:

```bash
pwd
```

**Make a folder inside it** for data:

```bash
mkdir data
```

Confirm it's there:

```bash
ls
```

You should see your new `data` folder.

**Go back up** one level when you're done:

```bash
cd ..
```

✅ **Checkpoint.** You created `my-project/` with a `data/` folder inside, and you can move in and out of it.

💡 **Tip:** `cd ..` means "go up one folder." `cd ~` takes you home. `cd -` jumps back to where you just were.

Next: [Step 4: Edit a Script with nano](./04-edit-with-nano)
