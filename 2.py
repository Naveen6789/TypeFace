def create_cmu_sound_dict():

    final_sound_dict = {}

    with open('resources/c06d/c06d') as cmu_dict:
        cmu_dict = cmu_dict.read().split("\n")
        for i in cmu_dict:
            i_s = i.split()
            if len(i_s) > 1:
                word = i_s[0]
                syllables = i_s[1:]

                final_sound = ""
                final_sound_switch = 0

                for j in syllables:
                    if "1" in j:
                        final_sound_switch = 1
                        final_sound += j
                    elif final_sound_switch == 1:
                        final_sound += j

            final_sound_dict[word.lower()] = final_sound

    return final_sound_dict

lst=list(map(str,input().split()))
print(create_cmu_sound_dict(lst)
