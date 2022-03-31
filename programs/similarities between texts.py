def word_count(text):
    counts = dict()
    words = text.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
  
def normalize(a:dict, b:dict):
    c = list(a.keys()) + list(b.keys())
    
    a_temp = a.copy()
    b_temp = b.copy()
    
    for key in c:
        if not(key in a_temp):
            a_temp[key] = 0
        if not(key in b_temp):
            b_temp[key] = 0
            
    return a_temp, b_temp

def calculate_pearson(a:dict, b:dict):
    sum_a = 0
    sum_b = 0
    sum_all = 0
    for key in a.keys():
        sum_all += (a[key])*(b[key])
        sum_a += (a[key])**2
        sum_b += (b[key])**2
    
    return sum_all/(sum_a * sum_b)**0.5


n = int(input())
texts = n*[None]

for i in range(n):
    input_string = input()
    texts[i] = word_count(input_string)

    
for i in range(n):
    min_similarity = float('-inf')
    similar_vector = -1
    for j in range(n):
        if i == j:
            continue

        a_words, b_words = normalize(texts[i], texts[j])
        similarity = calculate_pearson(a_words, b_words)
        
        if(similarity > min_similarity):
            min_similarity = similarity
            similar_vector = j
        
    print(similar_vector+1)
    
        