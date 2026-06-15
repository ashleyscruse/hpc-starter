# Step 6: Copy a Dataset

Real work means moving data around. This repo includes a small sample dataset (500 real US flights) in the `data` folder. Let's copy it into the project folder you made.

Make sure you're back in the `hpc-starter` folder:

```bash
cd $WORK/hpc-starter
```

Copy the file into your project's data folder:

```bash
cp data/flights_500.csv my-project/data/
```

The pattern is always `cp <what> <where>`.

Confirm it arrived:

```bash
ls my-project/data
```

Take a peek at the first few lines:

```bash
head my-project/data/flights_500.csv
```

✅ **Checkpoint.** You see flight rows (dates, airlines, delays) in your own project folder.

💡 **Bringing your own data later:** from your laptop you can upload files through the Tapis web portal at [morehouse.tapis.io](https://morehouse.tapis.io), or use `scp` from your terminal. For today, copying within the system is the skill.

Next: [More Than One Way In](./07-many-ways-in)
