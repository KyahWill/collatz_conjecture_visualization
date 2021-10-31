import json

depth = int(input("insert depth: "))
outputs = {"nodes":[],"links":[]}
stack = []
stack.append(1)
outputs["nodes"].append({"id":1,"name":bin(1)})
for i in range(depth):
    print(i+1)
    old_stack = stack
    new_stack = []
    for number in old_stack:
        if((number - 1 )%3 == 0 and ((number-1) /3) != 0 and ((number-1)/3) != 1):
            new_stack.append(int((number-1)/3))
            outputs["links"].append({"source":number,"target":(int((number-1)/3))})
            outputs["nodes"].append({"id":(number-1)/3,"name":bin(int((number-1)/3))})
        new_stack.append(number * 2)
        outputs["links"].append({"source":number,"target":(number*2)})
        outputs["nodes"].append({"id":(number*2),"name":bin(number*2)})

    stack = new_stack  
    print(len(outputs["nodes"]))

with open("collatz.json", "w") as outfile:
    json.dump(outputs, outfile)
