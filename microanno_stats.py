#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 02:11:10 2024

@author: ahmed
"""
############################################
import csv
import os
import pandas as pd
import argparse
############################################
my_parser = argparse.ArgumentParser(description='Welcome!')
print("example: $ python microanno.py -i . ")



my_parser.add_argument('-i','--input_dir',
                       action='store',
                        metavar='input_dir',
                       type=str,
                       help="input_dir")

args = my_parser.parse_args()

###########################################
path  = args.input_dir
############################################

def create_dictionary_from_file(file_path, key_column_index, value_column_index):
    data_dict = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if len(row) >= max(key_column_index, value_column_index) + 1:
                key = row[key_column_index]
                value = row[value_column_index]
                data_dict[key] = value
    return data_dict


key_column_index = 1  
value_column_index = 3  

list_of_dicts = []

#path= "/media/ahmed/CC69-620B6/00_Ph.D/DATA_results/0_accolens_prop_database_work/0_analysis/32_microbiomeannoator"
for filename in os.listdir(path):
#for filename in os.listdir():
        if filename.endswith('.tab'):
         filename = create_dictionary_from_file(filename,key_column_index,value_column_index)
         list_of_dicts.append(filename)
  


df = pd.DataFrame(list_of_dicts)


df['name'] = df['name'].str.replace('.faa.ko', ' ')
df = df.set_index('name')
df = df.rename_axis('Isolate')



#df = df.columns.str.split(',', expand=True)

df.columns = df.columns.str.replace(',', '_')
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('+', '')
df.columns = df.columns.str.replace('__', '_')
df.columns = df.columns.str.replace(':', '_')




for column in df.columns:
    df[column] = df[column].astype(float)

df = df.loc[:, (df != 0).any(axis=0)]

df = df.fillna(0)
df = df.dropna(axis=1, how='all')

df.to_csv("detailed_pathway.csv")



print("Here we collected %d detailed pathway from %d genomes!"%(df.shape[1],len(df)))



############################################


def create_dictionary_from_file(file_path, key_column_index, value_column_index):
    data_dict = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if len(row) >= max(key_column_index, value_column_index) + 1:
                key = row[key_column_index]
                value = row[value_column_index]
                if key in data_dict:
                    if not isinstance(data_dict[key], list):
                        data_dict[key] = [data_dict[key]]
                    data_dict[key].append(value)
                else:
                    data_dict[key] = value
    return data_dict

key_column_index = 2  
value_column_index = 3  

list_of_dicts = []
for filename in os.listdir(path):
#for filename in os.listdir():
        if filename.endswith('.tab'):
         filename = create_dictionary_from_file(filename,key_column_index,value_column_index)
         list_of_dicts.append(filename)
  


df = pd.DataFrame(list_of_dicts)

# Define a function to expand lists into multiple columns
def expand_list_to_columns(series, col_name):
    return pd.Series(series).apply(pd.Series).rename(columns=lambda x: f'{col_name}_{x}')

# Apply the function to each column of the DataFrame
expanded_dfs = []
for col in df.columns:
    expanded_df = df[col].apply(pd.Series).add_prefix(col + '_')
    expanded_dfs.append(expanded_df)

# Concatenate the expanded DataFrames
df = pd.concat(expanded_dfs, axis=1)


#df['name'] = df['name'].str.replace('.faa.ko', ' ')
df['pathway group_0'] = df['pathway group_0'].str.replace('.faa.ko', ' ')
#df = df.set_index('name')
df = df.set_index('pathway group_0')
df = df.rename_axis('Isolate')





for column in df.columns:
    df[column] = df[column].astype(float)

df = df.loc[:, (df != 0).any(axis=0)]

df = df.fillna(0)
df = df.dropna(axis=1, how='all')
df.columns = df.columns = [col.split('_')[0] for col in df.columns]
df.to_csv("pathway_group.csv")



print("Here we collected %d pathway group from %d genomes!"%(df.shape[1],len(df)))


