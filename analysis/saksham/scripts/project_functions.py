import pandas
import numpy
def load_and_process(url_or_path_to_csv_file):
    df = pandas.read_csv(url_or_path_to_csv_file, encoding = 'latin1')
    return df