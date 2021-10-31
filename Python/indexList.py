def indexOfSmallestElement(lst):
    temp=lst[0]
    index=0
    for i in range(0,len(lst)):
        if temp>=lst[(len(lst)-i-1)]:
            temp=lst[(len(lst)-i-1)]
            index=len(lst)-i-1
    return index
def main():
 listlength=eval(input("Please input the value of length of the list thst you are going to input"))
 List1=[]
 for i in range(0,listlength):
     value=eval(input("Please input the contents")) 
     List1.append(value)
 index=indexOfSmallestElement(List1)
 print(index)

main()