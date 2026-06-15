# Meet the Machine

Before we work, let's see what we're on. Run these (the comments are what you'll see):

```bash
whoami        # your username
hostname      # which node you're on
nproc         # cores you can use here   ->  1
lscpu         # the machine's full spec  ->  144 cores
free -h       # memory (237 GB, shared)
module list   # software switched on right now
```

## Wait, 1 core or 144?

<div style="display:flex; gap:16px; flex-wrap:wrap; margin:18px 0;">
  <div style="flex:1; min-width:210px; border:2px solid #2e7d32; border-radius:12px; padding:18px; background:#f1f8f2;">
    <div style="font-size:.75em; letter-spacing:.08em; color:#2e7d32; font-weight:700;">THE MACHINE HAS</div>
    <div style="font-size:2.2em; font-weight:800; margin:4px 0;">144 cores</div>
    <div style="color:#555;">237 GB RAM · ARM (Grace)</div>
    <div style="font-size:.8em; color:#888; margin-top:6px;">from <code>lscpu</code></div>
  </div>
  <div style="flex:1; min-width:210px; border:2px solid #b30000; border-radius:12px; padding:18px; background:#fdf1f1;">
    <div style="font-size:.75em; letter-spacing:.08em; color:#b30000; font-weight:700;">YOU GET, RIGHT NOW</div>
    <div style="font-size:2.2em; font-weight:800; margin:4px 0;">1 core</div>
    <div style="color:#555;">you're on the login node</div>
    <div style="font-size:.8em; color:#888; margin-top:6px;">from <code>nproc</code></div>
  </div>
</div>

<div style="border-left:5px solid #C1A231; background:#fbf8ee; padding:14px 16px; margin:16px 0; border-radius:6px;">
<strong>Same machine, different access.</strong> The login node is the shared lobby. Want all 144 cores and the GPUs? You reserve a <strong>compute node</strong>. (That's why heavy work never runs here, you only have one core.)
</div>

<details>
<summary><strong>Why only 1 core?</strong> (click)</summary>
<p style="margin:8px 0;">The login node is shared by everyone logged in. The system caps each person to a sliver so no one slows it down for the class. The 144 cores are real, run <code>nproc --all</code> and you'll see all of them. You just can't use them <em>here</em>.</p>
</details>

## What's a module?

<div style="border:1px solid #ddd; border-radius:12px; padding:18px; margin:14px 0;">
<div style="font-size:1.15em; font-weight:700;">🧰 Software you switch <em>on</em> when you need it</div>
<p style="margin:8px 0 0;">The supercomputer is a workshop with every tool on locked shelves. Nothing's on by default. <code>module load python3</code> takes Python off the shelf and onto your bench. Log out, and the bench clears.</p>
</div>

<details>
<summary><strong>The module commands</strong> (click)</summary>
<table>
<tr><td><code>module avail</code></td><td>What's on the shelves?</td></tr>
<tr><td><code>module load python3</code></td><td>Put a tool on my bench</td></tr>
<tr><td><code>module list</code></td><td>What's on my bench now?</td></tr>
<tr><td><code>module purge</code></td><td>Clear the bench</td></tr>
</table>
<p style="margin:8px 0;">Modules don't stick around. Every login starts with a fresh bench, so you reload what you need.</p>
</details>

✅ **Checkpoint.** You saw the machine is huge, that you get a sliver of it on the login node, and what a module is.

Next: [Look Around](./02-look-around)
