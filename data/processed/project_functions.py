import pandas

def genre_sales(path):

    df = (
        pandas.read_csv(path, encoding = 'latin1')
        .dropna().reset_index(drop=True)
        .drop(columns = 'Year')
            .groupby(['Genre']).sum()
        .sort_values(by = 'Global', ascending = False)
    )
    
    return df
