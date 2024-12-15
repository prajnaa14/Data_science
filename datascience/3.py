import pandas as pd
import os

def clean_book_data(filepath,savepath):
    try:
        if not os.path.exists(filepath):
            print(f"the file {filepath} is not found\n")
        df=pd.read_csv(filepath)
        print("File is imported to dataframs\n",df.head())

        df.drop(columns=['Flickr URL','Edition Statement','Corporate Contributors'],inplace=True,errors='ignore')
        print("drop is done\n",df.head())

        df.reset_index(inplace=True,drop=True)
        print("indexed dataframe\n",df.head())

        if 'Date of Publication' in df.columns:
            df['Publication Year']=df['Date of Publication'].str.extract(r'(\d{4})')
            print("Tidy up fields\n",df.head())

        if 'Author' in df.columns:
            df['Author']=df['Author'].str.strip().str.title()
            print("combine str with numpy\n ",df.head())
        df.to_csv(savepath,index=False)
        print("data is saved \n", df.head())
    except Exception as e:
        print(f"error occured {e}")

clean_book_data("C:\\Users\\PRAJNA\\Downloads\\Big_Data\\datascience\\BL-Flickr-Images-Book.csv","c:\\Users\\PRAJNA\\Downloads\\Cleaned-csv.csv")
