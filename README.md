# datawrangling_python

This repo is for the Intro to datascience data wrangling project for openstreetmaps.

This is also a dumping ground of ideas while I am at work.

you can convert a dictionary into a data frame like this:

dict = {'jack': '503-516-9010', 'billy': '971-444-9050'}

df = pd.DataFrame()
df['Names'] = dict.keys()
df['Phone'] = dict.values()

then you can print (df)

for each tag we processes, assign a serrogate id.

Should I create an object for each tag processed?
