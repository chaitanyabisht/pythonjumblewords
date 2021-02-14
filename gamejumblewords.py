#testing editing
def play():
    p1=input("pls enter ur name player1")
    p2=input("pls enter ur name player2")
    p1s=0
    p2s=0
    turn=0
    while(1):
        picked_word=choose()
        ques=jumble(picked_word)
        print("the jumbled word for you is ",ques)
        if (turn%2==0):
            print("this is ur turn",p1)
            ans=input("pls tell ur answer")
            turn=turn+1
            if (ans==picked_word):
                p1s=p1s+1
                print(p1," your score is ",p1s)
            else:
                print("try next time. ur score is still",p1s)
        else:
            print("this is ur turn",p2)
            ans=input("pls tell ur answer")
            turn=turn+1
            if (ans==picked_word):
                p2s=p2s+1
                print(p2," your score is ",p2s)
            else:
                print("try next time. ur score is still",p2s)
        if (turn%2==1):
            n=input("both of u",p1,"&",p2,"want to continue or not(0/1)")
            if (n==0):
                print(p1,":",p1s,"|",p2,":",p2s)
                if (p1s>p2s):
                    print(p1," is winner!!!!")
                elif (p2s>p1s):
                    print(p2," is winner!!!!")
                else (p1s=p2s):
                    print("both ",p1," & ",p2,"is winner!!!!")
                break
    print("we are out of the while loop.")
    
