import numpy as np
import pandas as pd

def yelp_reviews_data():
    yelp_reviews_data = []
    r_dtype = {"stars": np.float16,
            "useful": np.int32,
                "funny":np.int32, 
                "cool": np.int32,
                }
    with open("yelp_academic_dataset_review.json", "r", encoding="utf-8") as f:
        reader = pd.read_json(f, orient="records", lines = True, dtype=r_dtype, chunksize=1000)

        for chunk in reader:
            reduced_chunk = chunk.drop(columns =['review_id', 'user_id', 'text'])\
                .query("`date` >='2017-12-01'")   # Specifying the search from Date
            yelp_reviews_data.append(reduced_chunk)
    yelp_reviews_data =pd.concat(yelp_reviews_data, ignore_index=True)
    print(yelp_reviews_data)
    return yelp_reviews_data

def yelp_business_name_data():
    yelp_business_name_data = []
    r_dtype = {"name": np.string_,
                "address": np.string_,
                "city":np.string_, 
                "postal code": np.int32,
                "latitude": np.float16,
                "longitude": np.float16,
                "stars": np.float16,
                }
    with open("yelp_academic_dataset_business.json", "r", encoding="utf-8") as f:
        reader = pd.read_json(f, orient="records", lines = True, dtype=r_dtype, chunksize=1000)

        for chunk in reader: 
            chunk['state'] = chunk['state'].str.upper()           
            reduced_chunk = chunk.drop(columns =['review_count', 'is_open', 'attributes', 'categories', 'hours'])\
                            .query("state == 'CA'")             # Specifying the search from State
            yelp_business_name_data.append(reduced_chunk)
    yelp_business_name_data = pd.concat(yelp_business_name_data, ignore_index=True)
    print(yelp_business_name_data)
    return yelp_business_name_data
