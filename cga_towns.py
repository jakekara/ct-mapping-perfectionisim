import pandas as pd 

senate_url = "https://en.wikipedia.org/wiki/Connecticut_Senate"
house_url = "https://en.wikipedia.org/wiki/Connecticut_House_of_Representatives"

def town_list(liststr):
    ret = liststr.split(",")
    ret = map(lambda x: x.replace(" (part)","").strip(), ret)
    return ret

def chamber_df(url, town_col):
    tables = pd.read_html(url)
    for i in range(len(tables)):
        #print (i, len(tables[i]))
        pass

    df = tables[4]

    df.columns = df.iloc[0]
    df = df.reindex(df.index.drop(0))[["District","Party",town_col]]
    df.columns = "district","party","towns"
    
    df["towns"] = df["towns"].apply(town_list)
    return df

senate = chamber_df(senate_url,"Towns represented")
house = chamber_df(house_url,"Cities/towns represented")

def house_district(dist):
    return house[house["district"].astype(int) == int(dist)].iloc[0]

def senate_district(dist):
    return house[house["district"].astype(int) == int(dist)].iloc[0]
