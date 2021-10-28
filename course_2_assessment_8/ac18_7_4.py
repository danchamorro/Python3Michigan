# Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to
# the list, top_three.


medals = {'Japan': 41, 'Russia': 56, 'South Korea': 21,
          'United States': 121, 'Germany': 42, 'China': 70}


def medal_val(k):
    return medals[k]


sorted_medals = sorted(medals, key=medal_val, reverse=True)

print(sorted_medals)

top_three = sorted_medals[:3]

print(top_three)
