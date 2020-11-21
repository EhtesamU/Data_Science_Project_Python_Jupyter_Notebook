import pandas as pd

# adding continent
def create_continent(table):
    table['continent'] = ""
    for i in range(len(table.Region)):
        if "Europe" in table['Region'][i]:
            table['continent'][i] = "Europe"
        elif "Asia" in table['Region'][i]:
            table['continent'][i] = "Asia"
        elif "Australia " in table['Region'][i]:
            table['continent'][i] = "Oceania "
        elif "America" in table['Region'][i]:
            table['continent'][i] = "America"
        elif "Africa" in table['Region'][i]:
            table['continent'][i] = "Africa"
        else:
            table['continent'][i] = "TBD"

# adding region            
def create_region(from_table,to_table):
    to_table['Region'] = ""
    for i in range(len(to_table["Country"])):
        for j in range(len(from_table["Country"])):
            if from_table['Country'][j] == to_table['Country'][i]:
                to_table['Region'][i] = from_table['Region'][j]
                break
        else:
            to_table['Region'][i] = "TBD"

# arrange col for appending
def arrange_col_15_17(table):
    table = table[['Country','Region', 'continent','happiness_score', 'GDP_per_cap', 'Family','life_expect','Freedom', 'Generosity', 'gov_trust', 'dystopia_residual', 'Year']]

# find countries with less than `n` number of record
def find_less_than_record(table,n_record):
    dups = table.groupby('Country')
    dup_list = list()
    for dup in dups:
        if len(dup[1]) != n_record:
            dup_list.append(dup[0])
    return dup_list

#if we dont have enough record for a country (e.g missing a year), delete it
def delete_less_than_record(table,n_record):
    dup_list = find_less_than_record(table,n_record)
    print(dup_list)
    for i in range (len(table)):
        name = table.at[i,'Country']
        for item in dup_list:
            if name == item:
                table.drop([i],inplace = True)
                break

# 2018 and 2019 has slight differences in data and col therefore, need different methods
def arrange_col_18_19(table):
    table = table[['Country','happiness_score', 'GDP_per_cap', 'social_support','life_expect','Freedom', 'Generosity','corruption_perceptions' , 'Year']]

def arrange_col_15_19(table):
    table = table[['Country','Region', 'continent','happiness_score', 'GDP_per_cap','life_expect','Freedom', 'Generosity', 'Year']]

def hongkong(table, stop_when_found):
    for i in range(len(table["Country"])):
        if "Hong Kong" in table["Country"][i]:
            table["Country"][i] = "Hong Kong"
            if stop_when_found == True:
                break

def taiwan(table, stop_when_found):
    for i in range(len(table["Country"])):
        if "Taiwan" in table["Country"][i]:
            table["Country"][i] = "Taiwan"
            if stop_when_found == True:
                break
