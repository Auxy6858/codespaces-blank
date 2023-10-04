import random
GAMEOVER = False
    # Gives us the available options
OPTIONS = ['rock','paper','scissors']
# The option the AI chooses 
AICHOICE = str(OPTIONS[random.randrange(0,2)])
while GAMEOVER is False:
    PLAYERCHOICE = input("Choose your option: ").lower()
    #print(OPTIONS[0])
    if PLAYERCHOICE == AICHOICE:
        print(str(AICHOICE))
        print("Draw!")
# Calculates the results
    elif PLAYERCHOICE == 'rock':
        if AICHOICE == 'paper':
            print('Paper\n')
            print('You lose :(')
            print("""
                  
BGP5J?7?#@@@&&&&&&&&&&&&&&##&&&&&####&@##PG@@@&PYB@@@#BGJ?G@&#&@&BJY#GJG@&&&GYP5&B5YGJJJJJJJJ???????\n
BBBBG5?75@@&&&&&&&&&&&&##&###&&&####&&@&BBPG&@#G5#&@@BPG5?Y&&&&@&GYYBB#@&#&#5Y55&5PYBYJJJJJJJ???????\n
BBBBGP5J?B@&&@&&&&&&&&######&&&&#####@@@#BBGP##BG#@@@BYG5J?G@@@@&BGB&&@&#@&5J5YBBYGYBYJJJ??JJ???????\n
BBBBGP5Y?Y&@&@@&&&&&&&&##&&&&&&&&&###&@@@#B#BPG##&&@@#Y555?J#@@@&#&&@@##@&PJY55#Y5B5GYJJJ5PJJJ??????\n
#BGPP5YJJJG@&@&&&&&&&&&&#&&&&&&&&&&&&&&@@&#B##GP#&&@@&5YJPYJP#@&&@@@&#&@&5JYYJBPJGB5GYYPBB5JJJ??????\n
#BG5YYYJJ?JB@@&&&&&&&&&&##&&&&&&@@&#&&#@@@&#B##BPB&@@@PG5YGJYG#@@@@&#&@#5J55?PBJY#G5BBBBPGJJJJ??????\n
BBG5YYGBGPY5&@&&&@@@&&&&&&##&&&&&@@&#&#&@@&&#B##BB#@@@#G&Y5G?YB&@&##&@BYJPBYY#YJG###BG5YG5?J????????\n
GGP5YJYP&@&&&&&&&@@@&&&&&&&&&&&&&@@@@###&@&#&#B&&##@@@&G#&5PPJPB#B#@&BYJGB5JBGPB&#GP55YGBJ????????77\n
GP5YY55?YB&@&&&&@@@&&&&&&&&&&&&&&&@@@@&##&@&##&&&&&&@@@#B&#PGGGB#&@&#BG#&GJG&&&BP55PG5G&5???????7777\n
P555PPYJYY5G&@@@@&&&&&&&&&&&&&&&&&&@@@@&##&@@##&@@&##B&&G555YY5PB&#GP55#BY5##G55PGBB5G&B????77777777\n
Y55Y55Y55PJJ5B&@@@@@@@@@&&&&&&&&&&&@@@@@@&&&@@#B&G5YYPGPY55Y5PGBB##GYYYPGGBB55G##BGPB&#J7?7777777777\n
YJY5Y55555YYYY5P#@@@@@@@&&&&&&&&&&@@@@@@@@@&&&@#5Y5B#B5PP55GB##&&&&&G5P5GP5PG###BPB&&#5JJY5PY7777777\n
???JJJJYYYYYYYYP#&&@@@@@&&&&&@@@@@@@@@@@@@@@@&&55B&@&PGBGB#&&@@&@&&&BBPY##G5YG&BB&@&#GPPPGGJ77777???\n
YYJJ????JJJJYY5PGBB#&&&@@@&&@@@@@@@@@&&@@@@@&&&G#@@@&&BB&@&&&BGPG#&&##5P&&#BJP##@&G5Y5PBB57777??????\n
GGGP5YJJJJJJYY5PGBB###&&@@&&@@@@@@@@@@@@@@@@&&@&@@@@&&B&@&&#PYYYYP&&&BG&&&@BJB#&G5YPG##P?77??????JJJ\n
#BBBBBGGPP5555PPB###&&&@@@@&@@@@@@@@@@@@@@@@@@@@@@&#&&#&&&&#GYYYY5&@#P5B&&#GB#PG5GBBBGJ77????JJJJJYY\n
########BBBBBGGB##&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G5#@&&#G#&&YJ5G#&#P55P&##&B5GB##&BY????JJJJJYYYY55\n
&&&############&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@#P#G#&B5PPYG#&#BP5YG&BP&&BP&&#G5J??JJJYYYY55555PG\n
&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@BGG###B55P&#GG#BPPG5Y##BG&&#BGPYYYYY5555PPPPPPGB\n
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@&#B#&&#B#&&&BGPYYB&BGP5YYYY55555PPPGGGGGGGGGB\n
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#B#@@#JYPP5YYJYBPG&##BPY5PPPPPGGGGBBBBBBBBBB\n
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@&PYYYYYJYBGY5&&&&#YPGGGBBBBBBBBBB######\n
@@@@@@@@@@@@@@@@@@@@@@@@@&&&@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B5YYY5B&BYY5##&&&&BBBB##############&#\n
@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@P5PG#&&#55Y5G55PB#@&&#####&&&&&&&&&&&#\n
@@@@@@@@@@@@@@@@@@@@@&&&&&&&&@@@@@@@@@@@@@@@@@@@@&&&B&@@@@@@@@&&@@#G#PYBPY#&#BPYPB&&&&&&&&&&&&&&&&&&\n
@@@@@@@@@@@@@@@@@@@@@@&&&&&@@@@@@@@@@@@@@@@@@&&&&&&&BP@@@@@@@#G&&G5#BYB#G5##&&&#GYY&@&&BB#&&&&&&&&&&\n""")
            GAMEOVER = True
            break
        elif AICHOICE == 'scissors':
            print('Scissors\n')
            print('You Win')
            GAMEOVER = True
            break
    elif PLAYERCHOICE == 'paper':
        if AICHOICE == 'scissors':
            print('Scissors\n')
            print('You lose :(')
            print("""
BGP5J?7?#@@@&&&&&&&&&&&&&&##&&&&&####&@##PG@@@&PYB@@@#BGJ?G@&#&@&BJY#GJG@&&&GYP5&B5YGJJJJJJJJ???????\n
BBBBG5?75@@&&&&&&&&&&&&##&###&&&####&&@&BBPG&@#G5#&@@BPG5?Y&&&&@&GYYBB#@&#&#5Y55&5PYBYJJJJJJJ???????\n
BBBBGP5J?B@&&@&&&&&&&&######&&&&#####@@@#BBGP##BG#@@@BYG5J?G@@@@&BGB&&@&#@&5J5YBBYGYBYJJJ??JJ???????\n
BBBBGP5Y?Y&@&@@&&&&&&&&##&&&&&&&&&###&@@@#B#BPG##&&@@#Y555?J#@@@&#&&@@##@&PJY55#Y5B5GYJJJ5PJJJ??????\n
#BGPP5YJJJG@&@&&&&&&&&&&#&&&&&&&&&&&&&&@@&#B##GP#&&@@&5YJPYJP#@&&@@@&#&@&5JYYJBPJGB5GYYPBB5JJJ??????\n
#BG5YYYJJ?JB@@&&&&&&&&&&##&&&&&&@@&#&&#@@@&#B##BPB&@@@PG5YGJYG#@@@@&#&@#5J55?PBJY#G5BBBBPGJJJJ??????\n
BBG5YYGBGPY5&@&&&@@@&&&&&&##&&&&&@@&#&#&@@&&#B##BB#@@@#G&Y5G?YB&@&##&@BYJPBYY#YJG###BG5YG5?J????????\n
GGP5YJYP&@&&&&&&&@@@&&&&&&&&&&&&&@@@@###&@&#&#B&&##@@@&G#&5PPJPB#B#@&BYJGB5JBGPB&#GP55YGBJ????????77\n
GP5YY55?YB&@&&&&@@@&&&&&&&&&&&&&&&@@@@&##&@&##&&&&&&@@@#B&#PGGGB#&@&#BG#&GJG&&&BP55PG5G&5???????7777\n
P555PPYJYY5G&@@@@&&&&&&&&&&&&&&&&&&@@@@&##&@@##&@@&##B&&G555YY5PB&#GP55#BY5##G55PGBB5G&B????77777777\n
Y55Y55Y55PJJ5B&@@@@@@@@@&&&&&&&&&&&@@@@@@&&&@@#B&G5YYPGPY55Y5PGBB##GYYYPGGBB55G##BGPB&#J7?7777777777\n
YJY5Y55555YYYY5P#@@@@@@@&&&&&&&&&&@@@@@@@@@&&&@#5Y5B#B5PP55GB##&&&&&G5P5GP5PG###BPB&&#5JJY5PY7777777\n
???JJJJYYYYYYYYP#&&@@@@@&&&&&@@@@@@@@@@@@@@@@&&55B&@&PGBGB#&&@@&@&&&BBPY##G5YG&BB&@&#GPPPGGJ77777???\n
YYJJ????JJJJYY5PGBB#&&&@@@&&@@@@@@@@@&&@@@@@&&&G#@@@&&BB&@&&&BGPG#&&##5P&&#BJP##@&G5Y5PBB57777??????\n
GGGP5YJJJJJJYY5PGBB###&&@@&&@@@@@@@@@@@@@@@@&&@&@@@@&&B&@&&#PYYYYP&&&BG&&&@BJB#&G5YPG##P?77??????JJJ\n
#BBBBBGGPP5555PPB###&&&@@@@&@@@@@@@@@@@@@@@@@@@@@@&#&&#&&&&#GYYYY5&@#P5B&&#GB#PG5GBBBGJ77????JJJJJYY\n
########BBBBBGGB##&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G5#@&&#G#&&YJ5G#&#P55P&##&B5GB##&BY????JJJJJYYYY55\n
&&&############&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@#P#G#&B5PPYG#&#BP5YG&BP&&BP&&#G5J??JJJYYYY55555PG\n
&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@BGG###B55P&#GG#BPPG5Y##BG&&#BGPYYYYY5555PPPPPPGB\n
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@&#B#&&#B#&&&BGPYYB&BGP5YYYY55555PPPGGGGGGGGGB\n
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#B#@@#JYPP5YYJYBPG&##BPY5PPPPPGGGGBBBBBBBBBB\n
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@&PYYYYYJYBGY5&&&&#YPGGGBBBBBBBBBB######\n
@@@@@@@@@@@@@@@@@@@@@@@@@&&&@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B5YYY5B&BYY5##&&&&BBBB##############&#\n
@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@P5PG#&&#55Y5G55PB#@&&#####&&&&&&&&&&&#\n
@@@@@@@@@@@@@@@@@@@@@&&&&&&&&@@@@@@@@@@@@@@@@@@@@&&&B&@@@@@@@@&&@@#G#PYBPY#&#BPYPB&&&&&&&&&&&&&&&&&&\n
@@@@@@@@@@@@@@@@@@@@@@&&&&&@@@@@@@@@@@@@@@@@@&&&&&&&BP@@@@@@@#G&&G5#BYB#G5##&&&#GYY&@&&BB#&&&&&&&&&&\n""")
            GAMEOVER = True
            break
        elif AICHOICE == 'rock':
            print('Rock\n')
            print('You Win')
            GAMEOVER = True
            break
    elif PLAYERCHOICE == 'scissors':
        if AICHOICE == 'rock':
            print('Rock\n')
            print('You lose :(')
            print("""
BGP5J?7?#@@@&&&&&&&&&&&&&&##&&&&&####&@##PG@@@&PYB@@@#BGJ?G@&#&@&BJY#GJG@&&&GYP5&B5YGJJJJJJJJ???????\n
BBBBG5?75@@&&&&&&&&&&&&##&###&&&####&&@&BBPG&@#G5#&@@BPG5?Y&&&&@&GYYBB#@&#&#5Y55&5PYBYJJJJJJJ???????\n
BBBBGP5J?B@&&@&&&&&&&&######&&&&#####@@@#BBGP##BG#@@@BYG5J?G@@@@&BGB&&@&#@&5J5YBBYGYBYJJJ??JJ???????\n
BBBBGP5Y?Y&@&@@&&&&&&&&##&&&&&&&&&###&@@@#B#BPG##&&@@#Y555?J#@@@&#&&@@##@&PJY55#Y5B5GYJJJ5PJJJ??????\n
#BGPP5YJJJG@&@&&&&&&&&&&#&&&&&&&&&&&&&&@@&#B##GP#&&@@&5YJPYJP#@&&@@@&#&@&5JYYJBPJGB5GYYPBB5JJJ??????\n
#BG5YYYJJ?JB@@&&&&&&&&&&##&&&&&&@@&#&&#@@@&#B##BPB&@@@PG5YGJYG#@@@@&#&@#5J55?PBJY#G5BBBBPGJJJJ??????\n
BBG5YYGBGPY5&@&&&@@@&&&&&&##&&&&&@@&#&#&@@&&#B##BB#@@@#G&Y5G?YB&@&##&@BYJPBYY#YJG###BG5YG5?J????????\n
GGP5YJYP&@&&&&&&&@@@&&&&&&&&&&&&&@@@@###&@&#&#B&&##@@@&G#&5PPJPB#B#@&BYJGB5JBGPB&#GP55YGBJ????????77\n
GP5YY55?YB&@&&&&@@@&&&&&&&&&&&&&&&@@@@&##&@&##&&&&&&@@@#B&#PGGGB#&@&#BG#&GJG&&&BP55PG5G&5???????7777\n
P555PPYJYY5G&@@@@&&&&&&&&&&&&&&&&&&@@@@&##&@@##&@@&##B&&G555YY5PB&#GP55#BY5##G55PGBB5G&B????77777777\n
Y55Y55Y55PJJ5B&@@@@@@@@@&&&&&&&&&&&@@@@@@&&&@@#B&G5YYPGPY55Y5PGBB##GYYYPGGBB55G##BGPB&#J7?7777777777\n
YJY5Y55555YYYY5P#@@@@@@@&&&&&&&&&&@@@@@@@@@&&&@#5Y5B#B5PP55GB##&&&&&G5P5GP5PG###BPB&&#5JJY5PY7777777\n
???JJJJYYYYYYYYP#&&@@@@@&&&&&@@@@@@@@@@@@@@@@&&55B&@&PGBGB#&&@@&@&&&BBPY##G5YG&BB&@&#GPPPGGJ77777???\n
YYJJ????JJJJYY5PGBB#&&&@@@&&@@@@@@@@@&&@@@@@&&&G#@@@&&BB&@&&&BGPG#&&##5P&&#BJP##@&G5Y5PBB57777??????\n
GGGP5YJJJJJJYY5PGBB###&&@@&&@@@@@@@@@@@@@@@@&&@&@@@@&&B&@&&#PYYYYP&&&BG&&&@BJB#&G5YPG##P?77??????JJJ\n
#BBBBBGGPP5555PPB###&&&@@@@&@@@@@@@@@@@@@@@@@@@@@@&#&&#&&&&#GYYYY5&@#P5B&&#GB#PG5GBBBGJ77????JJJJJYY\n
########BBBBBGGB##&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G5#@&&#G#&&YJ5G#&#P55P&##&B5GB##&BY????JJJJJYYYY55\n
&&&############&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@#P#G#&B5PPYG#&#BP5YG&BP&&BP&&#G5J??JJJYYYY55555PG\n
&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@BGG###B55P&#GG#BPPG5Y##BG&&#BGPYYYYY5555PPPPPPGB\n
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@&#B#&&#B#&&&BGPYYB&BGP5YYYY55555PPPGGGGGGGGGB\n
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#B#@@#JYPP5YYJYBPG&##BPY5PPPPPGGGGBBBBBBBBBB\n
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@&PYYYYYJYBGY5&&&&#YPGGGBBBBBBBBBB######\n
@@@@@@@@@@@@@@@@@@@@@@@@@&&&@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B5YYY5B&BYY5##&&&&BBBB##############&#\n
@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@P5PG#&&#55Y5G55PB#@&&#####&&&&&&&&&&&#\n
@@@@@@@@@@@@@@@@@@@@@&&&&&&&&@@@@@@@@@@@@@@@@@@@@&&&B&@@@@@@@@&&@@#G#PYBPY#&#BPYPB&&&&&&&&&&&&&&&&&&\n
@@@@@@@@@@@@@@@@@@@@@@&&&&&@@@@@@@@@@@@@@@@@@&&&&&&&BP@@@@@@@#G&&G5#BYB#G5##&&&#GYY&@&&BB#&&&&&&&&&&\n""")
            GAMEOVER = True
            break
        elif AICHOICE == 'paper':
            print('Paper\n')
            print('You Win')
            GAMEOVER = True
            break
        else:
            print('Select a valid option (Rock paper or scissors)')
            GAMEOVER = False
# If something goes wrong
# I've seen this error message too many times





