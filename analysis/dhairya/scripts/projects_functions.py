def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file,encoding = 'latin')
          
          
      )

    range1 = range(500,len(df1))
    list1 = [i for i in range1]
 
    df1.drop([i for i in list1],inplace = True)

    # Make sure to return the latest dataframe

    return df1 