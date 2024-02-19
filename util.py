
import re  
from init import model,num_neighbors
def remove_hashtags(list_of_strings):
    """
    Removes hashtags from a list of strings.
    
    Args:
        list_of_strings (list): A list of strings possibly containing hashtags.
        
    Returns:
        list: A list of strings with hashtags removed.
    """
    hashtag_regex = re.compile(r'#(\w+)')
    list_of_strings_without_hashtags = []
    for string in list_of_strings:
        updated_string = hashtag_regex.sub(r'\1', string)
        list_of_strings_without_hashtags.append(updated_string)
    
    return list_of_strings_without_hashtags



def search(query: str,p,lst) -> None:
    
    query_embedding = model.encode([query])
    
    labels, distances = p.knn_query(query_embedding, k=num_neighbors)
    nearest_words = [lst[label] for label in labels[0]]
    return nearest_words
