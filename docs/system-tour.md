# System Tour: Meet the Machine

Before we work, let's see what we're actually on. These commands just *show* you things, nothing to break.

**Who am I, and where am I?**

```bash
whoami
hostname
```

`whoami` is your username. `hostname` is the exact machine you're on (a login node).

**How powerful is this thing?**

```bash
nproc
lscpu
free -h
```

🔎 **Quest:** your laptop probably has around 8 cores. Run `nproc`, how many does this node have? `free -h` shows the memory. This is exactly why we don't run heavy work on the login node: you're sharing all of this with everyone else logged in right now.

**What software is available?**

```bash
module list
module avail
```

`module list` shows what's loaded right now. `module avail` shows the big catalog you can turn on with `module load` (if it scrolls, press `q` to quit).

✅ **Checkpoint.** You know your username, which node you're on, how many cores it has, and how to see available software.

Next: [Look Around](./02-look-around)
