import pandas 
def load_and_process(url_or_path_to_csv_file):
    
    df1 = (
           
          pandas.read_csv(url_or_path_to_csv_file,encoding = 'latin')
          
          
      )

    range1 = range(500,len(df1))
    list1 = [i for i in range1]
 
    df1.drop([i for i in list1],inplace = True)

    # Make sure to return the latest dataframe

    return df1 