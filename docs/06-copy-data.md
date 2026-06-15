# Step 6: Copy a Dataset

Real work means moving data around, and real datasets are big. A dataset has been staged on the system for you: a database of about 38 million NYC taxi trips (roughly 6.3 GB). You'll copy it into your project folder.

Make sure you're in the `hpc-starter` folder (where your `my-project` lives):

```bash
cd $WORK/hpc-starter
```

Copy the dataset from the staged location into your project's data folder:

```bash
cp /work/10539/ashleyscruse/vista/gosha-sql-assignment/data/nyc_taxi.db my-project/data/
```

This file is about 6.3 GB, so give it a few seconds.

Confirm it arrived, and see how big it is:

```bash
ls -lh my-project/data/
```

✅ **Checkpoint.** You should see `nyc_taxi.db` at about `6.3G` in your project's data folder.

💡 **What just happened:** the source path `/work/10539/ashleyscruse/vista/...` is on the instructor's account. You copied a file someone else staged for you, by its full path. That is a very common HPC pattern: a shared dataset lives in one place, and everyone copies (or reads) what they need.

💡 **What's in it:** a SQLite database of NYC taxi trips. You don't need to open it today, you'll learn to query data like this later. For now, you just copied a real, multi-gigabyte dataset into your own workspace.

💡 **Bringing your own data later:** from your laptop you can upload through the Tapis web portal at [morehouse.tapis.io](https://morehouse.tapis.io), or use `scp`. Today the skill is copying a staged dataset.

Next: [More Than One Way In](./07-many-ways-in)
