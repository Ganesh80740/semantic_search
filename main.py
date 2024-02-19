from fastapi import FastAPI,HTTPException,status
from util import *
from schema import *
from init import *
from typing import List
app = FastAPI()


@app.post("/get_nearest_keywords",response_model=List[ResObj])
async def get_nearest_keywords(queries:Queries ):
    
    try:
        queries = [query.lower() for query in queries.hash_tags]
        
        queries_without_hashtags = remove_hashtags(queries)
        print(queries_without_hashtags)
        results = []
        for query_without_hashtag in  queries_without_hashtags:
            nearest_keywords = search(query_without_hashtag, p,hashtags)
            
            results.append({"query": query_without_hashtag, "nearest_keywords": nearest_keywords})
        return results
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
        
