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







 scenes = [ 
  { 'key': 'start',
    'title': 'Start',
    'story': 'Situation start... what to do?',
    'options': [
      {'key': 'c', 'next' : 'cave', 'story' : 'the dark and misty cave'},
      {'key': 'h', 'next' : 'hut', 'story' : 'the old wooden hut'},
      {'key': 't', 'next' : 'tree', 'story' : 'the thick old tree'},
    ]
  },
  { 'key': 'cave',
    'title': 'Cave',
    'story': 'Situation cave... wat te doen?',
    'options': [
      {'key': 'r', 'next' : 'river', 'story' : 'You choose to the river'},
      {'key': 'b', 'next' : 'bear-nest', 'story' : 'You choose to the bear nest'},
      {'key': 'l', 'next' : 'lava-chimney', 'story' : 'You choose to the lava chimney'},
    ]
  },
  { 'key': 'hut',
    'title': 'Hut',
    'story': 'Situation hut... wat te doen?',
    'options': [
      {'key': 'a', 'next' : 'attic', 'story' : 'You choose to the attic'},
      {'key': 'b', 'next' : 'bath room', 'story' : 'You choose to the bath room nest'},
      {'key': 'c', 'next' : 'cellar', 'story' : 'You choose to the cellar'},
    ]
  },




