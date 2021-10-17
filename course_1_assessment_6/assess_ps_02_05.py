# Write code to count the number of characters in original_str using the accumulation pattern and assign the answer to a
# variable num_chars. Do NOT use the len function to solve the problem (if you use it while you are working on this problem,
# comment it out afterward!)

original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars = 0

for i in original_str:
    num_chars += 1

print(num_chars)
