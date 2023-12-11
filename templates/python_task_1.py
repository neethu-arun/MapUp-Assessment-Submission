import pandas as pd

df = pd.read_csv('../datasets/dataset-1.csv')

def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    
    new_df1 = df.pivot(index='id_1', columns='id_2')
    return new_df1

generate_car_matrix(df)

def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    def car_type(value):
        if value <=15:
            return "low"
        elif value >15 and value <=25:
            return "medium"
        elif value >25:
            return "high"
        
    df['car_type'] = df['car'].map(car_type)
    #print(df.head())
    new_df2 = df.head()
    #print(new_df2)
    #print(new_df2.columns.tolist())
    #dict1 = new_df2.groupby('car_type').count().apply(lambda g:g.values.tolist()).to_dict()
    #dict1 = (new_df2.groupby('car_type')).apply(pd.DataFrame.to_dict)
   
    #dict1 = new_df2.groupby('car_type').agg(list).to_dict('index')
    #print(dict1)
    return dict()

get_type_count(df)

def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    
    check_value = 2 * df['bus'].mean()
    new_df3 = df[df['bus'] > check_value]
    new_list = (sorted(new_df3['bus'].tolist()))
    return new_list

get_bus_indexes(df)

def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    
    check_value2 = df['truck'].mean()
    #new_df4 = check_value
    #new_list2 = (sorted(new_df4['truck'].tolist()))
    
    #return new_list2

filter_routes(df)

def multiply_matrix(df)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    
    new_df5 = df.pivot(index='id_1', columns='id_2')
    
    new_df6 = new_df5.where(new_df5 > 20, round(new_df5*0.75))
    new_df6 = new_df5.where(new_df5 <= 20, round(new_df5*1.25))
    
    return new_df6

multiply_matrix(df)

def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    df2 = pd.read_csv('../datasets/dataset-2.csv')

    return pd.Series()

time_check(df)