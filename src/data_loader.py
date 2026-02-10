import pandas as pd
import pandas as pd

class AnimeDataLoader: 
    def __init__(self, raw_csv_path: str, processed_csv_path: str): 
        self.original_csv = raw_csv_path 
        self.processed_csv = processed_csv_path

    def load_and_process(self):
        df = pd.read_csv(self.original_csv , encoding='utf-8' , on_bad_lines='skip').dropna()

        required_cols = {'Name' , 'Genres','synopsis'}

        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError("Missing column  in CSV File")
        
        df['combined_info'] = (
            "Title: " + df["Name"] + " Overview: " +df["synopsis"] + "Genres : " + df["Genres"]
        )

        df[['combined_info']].to_csv(self.processed_csv , index=False,encoding='utf-8')

        return self.processed_csv