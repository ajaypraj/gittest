import random
def play():
    ppn1=input("Enter player 1 name")
    ppn2=input("Enter player 2 name")
    pp1=0
    pp2=0
    turn=0
    def choose():
        l=["went","elephant","Python","Kindle"]
        a=random.randint(0,len(l)-1)
        return l[a]
    def jumble(word):
        a=''.join(random.sample(word,len(word)))
        return a
        
    def thank(ppn1,ppn2,pp1,pp2):
        print(ppn1,ppn2,pp1,pp2)
    while 1:
        picked_word=choose()
        
#create the question

        qn=jumble(picked_word)
        print(qn)
        if turn %2==0:
            print("Its player 1 turn and please enter your answer")
            ans=input()
            if ans==picked_word:
                pp1=pp1+1
                print("your score is ",pp1)
                
            else:
                c=input("Press 1 to continue and 0 to quit")
                if c==0:
                    thank(ppn1,ppn2,pp1,pp2)
                    break
                    
                
        else:
            print("Its player 2 turn and please enter your answer")
            ans=input()
            if ans==picked_word:
                pp2+=1
                print("your score is ",pp2)
                
            else:
                c=input("Press 1 to continue and 0 to quit")
                if c==0:
                    thank(ppn1,ppn2,pp1,pp2)
                    break
                
                
                
        turn=turn+1 
    
play()           