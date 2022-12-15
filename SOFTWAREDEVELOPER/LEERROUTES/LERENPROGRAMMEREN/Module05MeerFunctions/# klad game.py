# klad game


4
5
6
7
8
9
10
11
12
13
14
# Function for a Yes/No result based on the answer provided as an arguement
 
def yes_no(answer):
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
     
    while True:
        choice = raw_input(answer).lower()
        if choice in yes:
           return True
        elif choice in no:
           return False
        else:
           print quot;Please respond with 'yes' or 'no'\n


# def yes_no(answer):
#     yes = set(['yes','y',''])
#     no = set(['no','n'])
#     return answer


print("""
hello
ik ben brigitte
ik ben 17 jaar 
doei





""")