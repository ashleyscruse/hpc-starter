# Step 2: Clone a Setup

You just built a folder by hand. That's perfect when you want your own structure.

But often someone has already set up a project you like, and instead of rebuilding it by hand, you can copy their whole setup in one command. That's **cloning**.

Make sure you're in `$WORK`:

```bash
cd $WORK
```

Clone this starter project:

```bash
git clone https://github.com/ashleyscruse/hpc-starter.git
```

Step into the folder it created:

```bash
cd hpc-starter
```

✅ **Checkpoint.** Run `ls`. You should see something like:

```
README.md   docs   examples   hello.py
```

Now look at what you just got, without making any of it yourself.

**Read a file:**

```bash
cat examples/welcome.txt
cat hello.py
```

**Count the rows in the sample CSV:**

```bash
wc -l examples/cities.csv
```

**Scroll through a file** (press `q` to quit):

```bash
less examples/cities.csv
```

✅ **Checkpoint.** You cloned a ready-made project and explored its files, all without building it by hand.

💡 **Tip:** `git clone` only happens once. After that, the files are yours on the system.

Next: [Step 3: Edit a Script with nano](./04-edit-with-nano)
