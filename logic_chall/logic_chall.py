#!/usr/bin/env python3

def main():
    
    q_dict = {
                "q_grav": "How much gravity to you typically prefer:\nlittle or moderate?\n",
                "q_phase": "What is your favorite physical state of matter:\nsolid, liquid, gas, or plasma?\n",
                "q_rings": "How do you like your ring system:\ngaudy or subtle?\n",
                "q_atmos": "What chemical compound do you find  easier to breath:\nammonia or methane?\n",
                "q_moons": "How many moons do you think are appropriate:\nzero, one, or two?\n",
                "q_tilt": "If you had to choose an axial tilt, would it be:\nnormal or extreme?\n"
             }

    out_txt = "You should live on"

    print("\nWhat planet should you actually live on?")

    q = 1

    a_phase = input(f"\nQuestion {q}. {q_dict['q_phase']}")

    if a_phase == "solid":
        
        q += 1

        a_grav = input(f"\nQuestion {q}. {q_dict['q_grav']}")

        if a_grav == "little":
            
            q += 1

            a_moons = input(f"\nQuestion {q}. {q_dict['q_moons']}")

            if a_moons == "zero":
                print(f"\n{out_txt} Mercury.")

            elif a_moons == "one":
                print(f"\n{out_txt} Pluto.")

            elif a_moons == "two":
                print(f"\n{out_txt} Mars.")

        elif a_grav == "moderate":
            print(f"\n{out_txt} Venus. Good luck with that.")

    elif a_phase == "gas":

        q += 1
            
        a_atmos = input(f"\nQuestion {q}. {q_dict['q_atmos']}")

        if a_atmos == "ammonia":

            q += 1
                
            a_rings = input(f"\nQuestion {q}. {q_dict['q_rings']}")

            if a_rings == "subtle":
                print(f"\n{out_txt} Jupiter.")

            elif a_rings == "gaudy":
                print(f"\n{out_txt} Saturn.")

        elif a_atmos == "methane":
                
            q += 1

            a_tilt = input(f"\nQuestion {q}. {q_dict['q_tilt']}")

            if a_tilt == "normal":
                print(f"\n{out_txt} Neptune.")

            elif a_tilt == "extreme":
                print(f"\n{out_txt} Uranus.")

    elif a_phase == "plasma":
        print(f"\n{out_txt} the Sun. Bring shades.")

    elif a_phase == "liquid":
        print(f"\n{out_txt} Earth. Lots of water there.")
    
    print("")

if __name__ == "__main__":
    main()
