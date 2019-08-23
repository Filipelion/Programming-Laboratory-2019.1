total_steps = input('Insert commands: \n').upper()
f_steps = total_steps.count("F")
final_steps = (f_steps - (len(total_steps)- f_steps))

if final_steps == 0:
    print("robot doesn't move")
else:
    if final_steps > 0:
        print("robot walked %d steps"% final_steps)
    else:
        print("robot walked %d 'moonwagilker' steps"% (-final_steps)) #negative to positive with -variable