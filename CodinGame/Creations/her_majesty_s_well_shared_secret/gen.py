#!/usr/bin/env python3

AlphaChr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
AlphaOrd = {a:i for i,a in enumerate(AlphaChr)}

B = 53  # prime

import random
random.seed(42)

def eval_poly(P,x):
    y = 0
    for c in reversed(P):
        y = (x*y+c) % B
    return y

def gen_pts(K,M):
    assert K>=2
    Coeffs = [[AlphaOrd[c]]+[random.randint(int(i==K-2),B-1) for i in range(K-1)] for c in M]
    Parts = []
    for x in range(1,10):
        s = ''.join(AlphaChr[eval_poly(P,x)] for P in Coeffs)
        Parts.append((x,s))
    return Parts

def randmsg(n):
    return ''.join(random.choice(AlphaChr) for _ in range(n))

Ks = [2,2,3,4,5,6,7,8]
Msg = ['SIS',
       'Intels_might_contain_worthwhile_information',
       'SPECTRE_means_SPecial_Executive_for_Counter_intelligence_Terrorism_Revenge_and_Extortion',
       'Jaws_appears_in_The_Spy_Who_Loved_Me_and_is_two_meters_seventeen_tall_while_Nick_Nack_from_The_Man_with_the_Golden_Gun_is_one_meter_nineteen_tall',
       'In_Moonraker_Drax_lives_in_California_in_a_castle_imported_from_France_He_did_also_buy_the_Eiffel_tower_but_the_French_government_refused_him_an_export_permit',
       'Oddjob_appears_in_Goldfinger_and_as_a_multiplayer_character_in_the_Nintendo_sixty_four_video_game_Goldeneye_Despite_not_being_a_midget_such_as_Nick_Nack_his_character_is_very_short_in_the_game_making_him_way_harder_to_hit_and_thus_giving_him_a_tremendous_advantage',
       'The_process_used_is_called_Shamir_s_Secret_Sharing',
       'This_process_is_only_worthwhile_if_one_does_need_the_threshold_Otherwise_seeing_the_secret_as_a_bitstring_it_is_enough_to_give_random_bitstrings_of_the_same_size_to_all_the_agents_but_one_and_the_bitwise_XOR_of_the_secret_with_all_these_random_bitstrings_to_the_last_one']

for i,K in enumerate(Ks):
    N = K
    if i==3 or i==6:
        N = random.randint(K+1,8)
    Parts = random.sample(gen_pts(K,Msg[i]),N)
    F = open('test%d'%i,'w')
    F.write('%d\n' % N)
    for a,s in Parts:
        F.write('00%d %s\n' % (a,s))
    F.close()
    Parts = random.sample(gen_pts(K,randmsg(len(Msg[i]))),N)
    F = open('valid%d'%i,'w')
    F.write('%d\n' % N)
    for a,s in Parts:
        F.write('00%d %s\n' % (a,s))
    F.close()
