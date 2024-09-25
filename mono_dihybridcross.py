#This is a code used to cross the gene traits of two parents and to predict the type of alleles formed
def di_arrangement(x, y):
    x1, x2 = x[0], x[1]
    y1, y2 = y[0], y[1]

    # Initialize GENE1 and GENE2
    GENE1, GENE2 = "", ""

    # Compare the first alleles
    if x1.lower() == y1.lower():
        if x1 < y1:
            GENE1 = x1 + y1
        else:
            GENE1 = y1 + x1
    else:
        GENE1 = x1 + y1  # Fallback in case they don't match

    # Compare the second alleles
    if x2.lower() == y2.lower():
        if x2 < y2:
            GENE2 = x2 + y2
        else:
            GENE2 = y2 + x2
    else:
        GENE2 = x2 + y2  # Fallback in case they don't match

    return GENE1 + GENE2

mono_di = input("Are you solving a Monohybrid Crossing?y/n ")
if mono_di == "y":
    print("Parent 1 trait")
    trait_name = input("What is the trait? ")
    conv_name = input("Does it go by conventional naming method?y/n ")
    if conv_name == "y":
        symbol1 = trait_name[0]
    if conv_name == "n":
        symbol1 = input("What letter(s) represent the trait? ")
    homo_hetero = input("Is it HOMOZYGOUS or not?y/n ")
    if homo_hetero == "y":
        t_dom = input("Is it Dominant or not?y/n ")
        if t_dom ==  "y":
            symbol1 = (symbol1+symbol1).upper()
            print(symbol1)
        if t_dom == "n":
            print("Then it is RECESSIVE!!")
            symbol1 = (symbol1+symbol1).lower()
            print(symbol1)
    if homo_hetero == "n":
        symbol1 = symbol1.upper() + symbol1.lower()
        print(symbol1)
    #Parent 2 
    print("Parent 2 trait")
    trait_name = input("What is the trait? ")
    conv_name = input("Does it go by conventional naming method?y/n ")
    if conv_name == "y":
        symbol2 = trait_name[0]
    if conv_name == "n":
        symbol2 = input("What letter(s) represent the trait? ")
    homo_hetero = input("Is it HOMOZYGOUS or not?y/n ")
    if homo_hetero == "y":
        t_dom = input("Is it Dominant or not?y/n ")
        if t_dom ==  "y":
            symbol2 = (symbol2+symbol2).upper()
            print(symbol2)
        if t_dom == "n":
            print("Then it is RECESSIVE!!")
            symbol2 = (symbol2+symbol2).lower()
            print(symbol2)
    if homo_hetero == "n":
        symbol2 = symbol2.upper() + symbol2.lower()
        print(symbol2)    

#Beginning the Gene Crossing
    P1S1 = symbol1[0]
    P1S2 = symbol1[1]
    P2S1 = symbol2[0]
    P2S2 = symbol2[1]
    if P1S1 < P2S1:
        TL = P1S1 + P2S1
    else:
        TL = P2S1 + P1S1
    if P1S2 < P2S1:
        TR = P1S2 + P2S1
    else:
        TR = P2S1 + P1S2
    if P1S1 < P2S2:
        DL = P1S1 + P2S2
    else:
        DL = P2S2 + P1S1
    if P1S2 < P2S2:
        DR = P1S2 + P2S2
    else:
        DR = P2S2 + P1S2
    print("RESULTS!!!")
    print(f'{TL}  {TR}')
    print(f'{DL}  {DR}')
if mono_di == "n":
    print("Then it must be Dihybrid. That's tough, but i've got your back :)")
    print("You want to solve the Di-hybrid crossing of two parents")
    known_traitname = input("Do you know the traits genotypes for Parent 1?y/n ")
    if known_traitname == "y":
        known_traitname = input("Input traits genotype? ")
    elif known_traitname == "n":
        print("That's fine, we'll get it together")
        trait_name = input("What is the 1st trait? ")
        conv_name = input("Does it go by conventional naming method?y/n ")
        if conv_name == "y":
            symbol1 = trait_name[0]
        if conv_name == "n":
            symbol1 = input("What letter(s) represent the trait? ")
        homo_hetero = input("Is it HOMOZYGOUS or not?y/n ")
        if homo_hetero == "y":
            t_dom = input("Is it Dominant or not?y/n ")
            if t_dom ==  "y":
                symbol1 = (symbol1+symbol1).upper()
                # print(symbol1)
            if t_dom == "n":
                print("Then it is RECESSIVE!!")
                symbol1 = (symbol1+symbol1).lower()
                # print(symbol1)
        if homo_hetero == "n":
            symbol1 = symbol1.upper() + symbol1.lower()
            # print(symbol1) 
            # TRAIT 2
        trait_name2 = input("What is the 2nd trait? ")
        conv_name = input("Does it go by conventional naming method?y/n ")
        if conv_name == "y":
            symbol2 = trait_name2[0]
        if conv_name == "n":
            symbol2 = input("What letter(s) represent the trait? ")
        homo_hetero = input("Is it HOMOZYGOUS or not?y/n ")
        if homo_hetero == "y":
            t_dom = input("Is it Dominant or not?y/n ")
            if t_dom ==  "y":
                symbol2 = (symbol2+symbol2).upper()
                # print(symbol2)
            if t_dom == "n":
                print("Then it is RECESSIVE!!")
                symbol2 = (symbol2+symbol2).lower()
                # print(symbol2)
        if homo_hetero == "n":
            symbol2 = symbol2.upper() + symbol2.lower()
            # print(symbol2) 
        known_traitname = symbol1 + symbol2
        print(known_traitname)    
    # PARENT 2
    known_traitname2 = input("Do you know the traits genotypes for Parent 2?y/n ")
    if known_traitname2 == "y":
        known_traitname2 = input("Input traits genotype? ")
    elif known_traitname2 == "n":
        print("That's fine, we'll get it together")
        trait_name = input("What is the 1st trait? ")
        conv_name = input("Does it go by conventional naming method?y/n ")
        if conv_name == "y":
            symbol1 = trait_name[0]
        if conv_name == "n":
            symbol1 = input("What letter(s) represent the trait? ")
        homo_hetero = input("Is it HOMOZYGOUS or not?y/n ")
        if homo_hetero == "y":
            t_dom = input("Is it Dominant or not?y/n ")
            if t_dom ==  "y":
                symbol1 = (symbol1+symbol1).upper()
                # print(symbol1)
            if t_dom == "n":
                print("Then it is RECESSIVE!!")
                symbol1 = (symbol1+symbol1).lower()
                # print(symbol1)
        if homo_hetero == "n":
            symbol1 = symbol1.upper() + symbol1.lower()
            # print(symbol1) 
            # TRAIT 2
        trait_name2 = input("What is the 2nd trait? ")
        conv_name = input("Does it go by conventional naming method?y/n ")
        if conv_name == "y":
            symbol2 = trait_name2[0]
        if conv_name == "n":
            symbol2 = input("What letter(s) represent the trait? ")
        homo_hetero = input("Is it HOMOZYGOUS or not?y/n ")
        if homo_hetero == "y":
            t_dom = input("Is it Dominant or not?y/n ")
            if t_dom ==  "y":
                symbol2 = (symbol2+symbol2).upper()
                # print(symbol2)
            if t_dom == "n":
                print("Then it is RECESSIVE!!")
                symbol2 = (symbol2+symbol2).lower()
                # print(symbol2)
        if homo_hetero == "n":
            symbol2 = symbol2.upper() + symbol2.lower()
            # print(symbol2) 
        known_traitname2 = symbol1 + symbol2
        print(known_traitname2)    
    # Dihybrid crossing 1st Stage : Monohybrid crossing
    # parent 1 monocrossing
    FG = known_traitname[0:2]
    SG = known_traitname[2:4]
    FG1 = FG[0]
    FG2 = FG[1]
    SG1 = SG[0]
    SG2 = SG[1]
    P1M1 = FG1 + SG1
    P1M2 = FG2 + SG1
    P1M3 = FG1 + SG2
    P1M4 = FG2 + SG2
    # parent 2 monocrossing
    FG = known_traitname2[0:2]
    SG = known_traitname2[2:4]
    P2FG1 = FG[0]
    P2FG2 = FG[1]
    P2SG1 = SG[0]
    P2SG2 = SG[1]
    P2M1 = P2FG1 + P2SG1
    P2M2 = P2FG2 + P2SG1
    P2M3 = P2FG1 + P2SG2
    P2M4 = P2FG2 + P2SG2
    S1 = di_arrangement(P1M1,P2M1)
    S2 = di_arrangement(P1M2,P2M1)
    S3 = di_arrangement(P1M3,P2M1)
    S4 = di_arrangement(P1M4,P2M1)
    S5 = di_arrangement(P1M1,P2M2)
    S6 = di_arrangement(P1M2,P2M2)
    S7 = di_arrangement(P1M3,P2M2)
    S8 = di_arrangement(P1M4,P2M2)
    S9 = di_arrangement(P1M1,P2M3)
    S10 = di_arrangement(P1M2,P2M3)
    S11 = di_arrangement(P1M3,P2M3)
    S12 = di_arrangement(P1M4,P2M3)
    S13 = di_arrangement(P1M1,P2M4)
    S14 = di_arrangement(P1M2,P2M4)
    S15 = di_arrangement(P1M3,P2M4)
    S16 = di_arrangement(P1M4,P2M4)
    print(f'{S1} {S2} {S3} {S4}')
    print(f'{S5} {S6} {S7} {S8}')
    print(f'{S9} {S10} {S11} {S12}')
    print(f'{S13} {S14} {S15} {S16}') 