student = {
    "group1":{"person1 ": {"name": "praveena", "department": "cs", "semester": 5, "marks": 87, "place": "namakkal"},
              "person2": {"name": "kavitha", "department": "cs", "semester": 5, "marks": 65, "place": "salem"},
              "person3": {"name": "saranya", "department": "cs", "semester": 5, "marks": 67, "place": "erode"},
              "person4": {"name": "savitha", "department": "cs", "semester": 5, "marks": 78, "place": "chennai"},
              "person5": {"name": "saranya", "department": "cs", "semester": 5, "marks": 69, "place": "thirch"},
              "person6": {"name": "pavithra", "department": "cs", "semester": 5, "marks": 98, "place": "banglore"},
              "person7": {"name": "kavin", "department": "cs", "semester": 5, "marks": 54, "place": "mettupati"},
              "person8": {"name": "naveen", "department": "cs", "semester": 5, "marks": 59, "place": "selimanagar"},
              "person9": {"name": "shyam", "department": "cs", "semester": 5, "marks": 65, "place": "thalaivasal"},
              "person10": {"name": "arun", "department": "cs", "semester": 5, "marks": 72, "place": "seerapalli"},
             },
    "group2":{"person1": {"name": "saravana", "department": "tfd", "semester": 5, "marks": 98, "place": "banglore"},
              "person2": {"name": "karan", "department": "tfd", "semester": 5, "marks": 65, "place": "karaikal"},
              "person3": {"name": "harini", "department": "tfd", "semester": 5, "marks": 60, "place": "jaipur"},
              "person4": {"name": "harshith", "department": "tfd", "semester": 5, "marks": 84, "place": "erode"},
              "person5": {"name": "pavan", "department": "tfd", "semester": 5, "marks": 94, "place": "selimanagar"},
              "person6": {"name": "mani", "department": "tfd", "semester": 5, "marks": 82, "place": "rasipuram"},
              "person7": {"name": "manikandan", "department": "tfd", "semester": 5, "marks": 80, "place": "vennathore"},
              "person8": {"name": "kesavan", "department": "tfd", "semester": 5, "marks": 76, "place": "namagiripet"},
              "person9": {"name": "thennavan", "department": "tfd", "semester": 5, "marks": 66, "place": "salem"},
              "person10": {"name": "arjun", "department": "tfd", "semester": 5, "marks": 57, "place": "namakkal"},
              },
    "group3":{"person1": {"name": "ram", "department": "B.Tech", "semester": 5, "marks": 86, "place": "banglore"},
              "person2": {"name": "kanan", "department": "B.Tech,", "semester": 5, "marks": 65, "place": "karaikal"},
              "person3": {"name": "muguthan", "department": "B.Tech", "semester": 5, "marks": 46, "place": "jaipur"},
              "person4": {"name": "palavi", "department": "B.Tech", "semester": 5, "marks": 81, "place": "erode"},
              "person5": {"name": "thasmiya", "department": "B.Tech", "semester": 5, "marks": 84, "place": "selimanagar"},
              "person6": {"name": "sowndarya", "department": "B.Tech", "semester": 5, "marks": 72, "place": "rasipuram"},
              "person7": {"name": "thilagam", "department": "B.Tech", "semester": 5, "marks": 50, "place": "vennathore"},
              "person8": {"name": "vasuki", "department": "B.Tech", "semester": 5, "marks": 66, "place": "namagiripet"},
              "person9": {"name": "srimathi", "department": "B.Tech", "semester": 5, "marks": 96, "place": "salem"},
              "person10": {"name": "janani", "department": "B.Tech", "semester": 5, "marks": 77, "place": "namakkal"},
              },
    "group4":{"person1": {"name": "ram", "department": "B.com", "semester": 5, "marks": 86, "place": "banglore"},
              "person2": {"name": "kanan", "department": "B.com,", "semester": 5, "marks": 65, "place": "senthamagalam"},
              "person3": {"name": "prabha", "department": "B.com", "semester": 5, "marks": 46, "place": "mangalapuram"},
              "person4": {"name": "anu", "department": "B.com", "semester": 5, "marks": 81, "place": "erode"},
              "person5": {"name": "gopika", "department": "B.com", "semester": 5, "marks": 84, "place": "ponicherry"},
              "person6": {"name": "surya", "department": "B.com", "semester": 5, "marks": 72, "place": "rasipuram"},
              "person7": {"name": "tharika", "department": "B.com", "semester": 5, "marks": 50, "place": "vennathore"},
              "person8": {"name": "indhu", "department": "B.com", "semester": 5, "marks": 66, "place": "namagiripet"},
              "person9": {"name": "raje", "department": "B.com", "semester": 5, "marks": 96, "place": "salem"},
              "person10": {"name": "gopal", "department": "B.com", "semester": 5, "marks": 77, "place": "namakkal"},
            },
}
average_group = {} # here I create a empty set for store a average values of group
for group_name,group in student.items(): # for is checking a items in dictionaries that the items is present or not
                                 # |---> items is containing a key and value
    total = 0
    for person in group.values():
       total += person["marks"]
    x = len(group)
    average = total / x
    print(f"group:{group_name}") # f is used for that curley braces{}
    print("sum of all marks:",total)
    print("len(group) :" , len(group)) # len finds a content of dictionaries
    print(f"average: {average:.2f}")
    print("---" * 30) # here multiple a "---" x "30" times
    #average_group = {} in this place we give this it shows always a last printed value is high
    average_group[group_name] = average
if average_group:
    highest_group = max(average_group, key=average_group.get)
    print(f"the group with  high average mark is {highest_group} \n with an average of {average_group[highest_group]:.2f}")

