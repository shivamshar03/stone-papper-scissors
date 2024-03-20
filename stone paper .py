print("*"*40)
print("-"*10,"TWO PLAYEAR GAME","-"*10)
def main():
    global playear1, playear2
    print("STONE PAPER SCISSOR \n")
    mode = int(input("Selact a mood:-\n1.One Player Mood (1) \n2.Two Player mood (2)\ninput: "))
    p1 = 0
    p2 = 0
    n = 5
    if mode ==1:
        playear1 = input("Your name:")
        playear2 = "computer"
    while 0 <= n:
        print("\n ",n," chances left")
        choice1 = input("select your choice( s:stone ; p:paper ; c:scissor) :")
        if mode == 1:
            import random
            choices = ('s', 'p', 'c')
            choice2 = random.choice(choices)
        elif mode == 2:
            choice2 = input("select choice for 2nd player( s:stone ; p:paaper ; c:scissor) :")
        else:
            print("invalid input")
            break
        if choice1 == choice2:
            print("draw")
        elif choice1 == "s" and choice2 == "c":
            p1 += 1
            print("\n",playear1," select 's' and ",playear2," select 'c' \n\n ",playear1," win!\n\n ",playear1," = ", p1, "\n ",playear2," = ", p2)
        elif choice1 == "p" and choice2 == "s":
            p1 += 1
            print("\n",playear1, " select 'p' and ", playear2, " select 's' \n\n ", playear1, " win!\n\n ", playear1, " = ", p1,
                  "\n ", playear2, "=", p2)
        elif choice1 == "c" and choice2 == "p":
            p1 += 1
            print(f"\n{playear1}  select 'c' and {playear2} select 'p' \n\n {playear1} win!\n\n {playear1} = ", p1,f"\n {playear2} = ", p2)
        else:
            p2 += 1
            print(f"\n{playear1} select ", choice1, f" and {playear2} select ", choice2, f" \n\n {playear2} win !\n\n {playear1} = ",
                  p1, f"\n {playear2} = ", p2)
        n -= 1
    print(f"\nscoreboar:\n {playear1} = ", p1, f"\n {playear2} = ", p2)
    if p1 > p2:
        print(f"\n{playear1} won the game ")
    elif p1==p2:
        print("\nmatch draw")
    else:
        print(f"\n{playear2} won the game")
    print("*"*40)
    inp = int(input("IF YOU WANT PLAY AGAIN PLEASE ENTER (1) :"))
    if inp == 1:
        main()
        '''player1           player2              result
              s                  p                   p(2)
              p                  p                   p(draaw)
              c                  p                   c(1)
              s                  s                   s(draw)
              p                  s                   p(1)
              c                  s                   s(2)
              s                  c                   s(1)
              p                  c                   c(2)
              c                  c                   c(draw)'''

main()
