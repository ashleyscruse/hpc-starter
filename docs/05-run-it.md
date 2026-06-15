# Step 4: Run Your Script

Time to run code on a supercomputer.

Try this first:

```bash
python3 hello.py
```

If you see your message, great, skip ahead. If you get `command not found`, you just need to turn Python on first:

```bash
module load python3
python3 hello.py
```

**Checkpoint.** You should see something like:

```
Hello! This is <your name> on Vista.
I am running on: login2.vista.tacc.utexas.edu
My current folder is: /work/.../hpc-starter
```

That's your code, your edit, running on the supercomputer.

**About `module load`:** software isn't all turned on by default. `module load` switches a tool on for your session. You'll use this constantly.

**One note on etiquette:** this script is tiny, so running it on the login node is fine. *Big* jobs (real training, large data) get sent to compute nodes through the scheduler. You'll learn that part later, this is just the warm-up.

Next: [Step 5: Copy a Dataset](./06-copy-data)
