def favourite_singer(arr):
    count_dict = {}
 
    for num in arr:
        if num in count_dict:
            count_dict[num]+=1
        else:
            count_dict[num]=1
    
    max_song_count = max(count_dict.values())
 
    fav_singer = [key for key,value in count_dict.items() if value == max_song_count]
 
    return len(fav_singer)
 
 
 
N = int(input())
arr = []
arr = list(map(int,input().split()))
result = favourite_singer(arr)
print(result)