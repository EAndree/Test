import re
import pandas as pd

def clean_line(line):
    #takes one line and removes tags, removes the dash (if there is one) and converts to lower case
    x = re.sub(r"\[([^\[\]]+)\]\([^\(\)]+\)", "\\1", line)
    if x[:2] == "- ":
        x = x[2:]
    return x.lower()

def clean_data(df):
    #cleans all data 
    df["message_text"] = df["message_text"].apply(clean_line).apply(lambda x: x.lower())
    return df

def untag(data_path, untagged_data_path):
    #reads in the tagged data, cleans it and saves it to a new file to the path specified
    #also deduplicates the data
    data = pd.read_csv(data_path)
    data = clean_data(data).drop_duplicates(subset="message_text")
    data.to_csv(untagged_data_path, index=False)


#first argument is the path of the file with your tagged data
#second argument is the path you want to save the new file with the clean data to
#the data needs to be in a csv file, with the messages being in a column with the name "message_text"
untag("//Users/lukastilmann/Documents/data/clean payment failed intents - cant_spend_funds.csv",
 "/users/lukastilmann/documents/data/cant_spend_funds_untagged.csv")