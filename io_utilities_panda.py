import pandas as pd

def read_pandas(filepath,names):
    '''
    read a csv in pandas
    returns a pandas dataframe
    '''
    df = pd.read_csv(filepath,names=names)
    return df

def main():
    filepath = './Data/iris.data'
    names = ['sepal_length','sepal_width','petal_length','petal_width','flower_name']
    df = read_pandas(filepath, names)
    print(df)
    
    #Data frame con nueva columna llamada sl+pl
    sepal_length_list=df['sepal_length'].to_list()
    df['sl+pl'] = df['sepal_length'] + df['petal_length']
    print(df.head(10))

    #Data frame donde sepal length es mayor o igual a 5
    df_filtered = df[df['sepal_length']>=5]
    print(df_filtered.head(10))

    #Using df.describe()
    percentages = [0.25, 0.5, 0.75, 0.99]
    include = ['object', 'float']
    desc = df.describe(percentiles = percentages, include=include)
    print(desc)

if __name__ == '__main__':
    main()
