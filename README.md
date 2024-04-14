# MicrobeAnnotator_stats

**What is this script?**

[MicrobeAnnotator](https://github.com/cruizperez/MicrobeAnnotator) is a great tool for metabolic pathway annotation.
However, if you need to collect pathway completeness stats from a cohort of genomes into one condensed CSV (to make a heatmap), you are IN the right repo! 

**What do you need?**

You shall have the tab files in one directory

*What about dependencies?*

Pandas, csv, argparse

Then, effortlessly you can type in your beautiful terminal

```bash
python3 microanno_stats.py -i .
```
"-i /--input_dir"  is your path to the directory for your binary file. 

In my case, the script was in the same directory as the Python file. Therefore, I wrote  <code>.</code> as my input directory.


**What do you get?**

Currently, there are two files.

1. pathway_group.csv The main output is a collection in the 3rd column  which is referred  as "pathway_group" in the basic tab output of MicrobeAnnotator.
2. detailed_pathway.csv. This is simply a detailed pathway collection in the 2nd column  which is referred  to as "name" in the basic tab output of MicrobeAnnotator.

You can use the two files in your favorite visualization tool to produce a publication-ready figure.

I hope this helps.

Thanks
