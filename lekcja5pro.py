# -*- coding: utf-8 -*-

# Lekcja 5 - ćwiczenie 3

    #Skopiuj kod genetyczny do swojego skryptu i zapisz jako DNA = ACTG...

DNA = "ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAGGGTGGGGGTCCCGGGTACTGGTAGGGGTAGCCCTGACCCAGAGGCGGGGGGGCAGCCGGGTGGGGCAGCGGGGCCAGCGTGTCCTGAA-CGAAGTCCCACTGGAGCCACTGTTGAGGTTCAGGGTGGCGAGATCTGGCGGNNNAGGGTAGGTGAGGGCCGCGGAGGGGCCTCCGGCGTTCCCCTCCCCCCCGCCCTGAAACCCGAAGCCCCCACTCACTGCTGCAGAGATCCCCTGAAAACGTAGTAGCACTGCTCgagacAGGTGATCTGTTGACCTGAAACCGCAGGAAGCCGTGCTTCAGCAAGCTGCTGGCGTACTTCCGGGCCT---GCCGCTCCTTGAAGCCCTCCACGTGTGTGTACAGCCAGTCCACCACGTCCGCCCCTGGCCGGCACCAGCGGTCAGCCCGCAGCCTCGAGGCAAGCAGCCCTGCCNNTGGCACTATCCGC-CGCGGGGACGGCCACTCACCGATGACGGCATNNGCGATGGTGATCTTGAGCCACATGCGGTCGCGGATCTCCAGTCCCGAG---GGCAGCTGCATGACCCGGACGACGGCGCTCATGTCACtcaccgtcagcggcgcctcttccagCCAGCTCTGCAAAGCACAGACAGCCCCGCTTCGCCCCAGCATCTGAAAGCGGGGGACTCggcAcgCTGCACCCCCAGGGGAGCCTCTGGGCAGAGCCTGCGCCAGGGCGCAAGCTGGACGGTGCGTGACAGCAGGGCCCCGGCCCACTGCAGGATGCACCCCCGTGAGGCTGGGGCGTGAGCAGGGGGGTTGGACAtttAGTCTCCCACTTCTACAGACACTTTTCATCAGGATCCTAGGCACAAACTGGGCTGAAACCCCACCCTGCAGACCAGGAAGTAATGAGAACAGGGCAGGCCCCTTCCCCTCNNCGCATGCC-CACCCGAGAGCGCAGGCTGTTAGTCGTGTTAATGGCAGGAAGCAGAATGGAGACCTGGCCCCTGCCTCTGAA-CCGTGGGTGCTCaactggctaGCCCTACGTACATCCCCTGTTCcggCCAACACACAGACATGAGCAGGATGGGCTGCACAAGGTGGGCACGGGTGCCTGTGCACACGTCTGTGCAGGGAGTTGGGGACAGGCAACACACACGTGTCACAGCCCCATGACGGggcaattgcGCCATGCTGGCTGAATGGCAGAGACGCCCCTCCAAGCCTCGGTTTCTGCTGGGGCCCTCAGGAGCTGCCACTTACGTGGAGCACCAGGCACGGAGCTGGTTAGTGAGGAGGAGCTGGTGCGCGTGACGGCGCTGGAGCAGGGACTCGTACCGTAGCGGGGCAGGGCNNNTGTCAGTGCCGCCGTGTGGtcagcggcgatCGGCG-GGTCGATGGGCCGCACCGGGTCAGCTGGGTGNAGACACGTGGCGATGACAGGCGGACAGATGGACAGGGTGGGAGGGCAGGGTGCAGGGCACAGAGGAGAGAGGCCTTCAGGCTAGGTAGGCGCCCCCTCCCCATCCCGccccGTGTGCCCCGAGGGCCACTCACCCCGTGGGACGGTGAAGTAGCTTCG-GGCGTTGGGTCCAGCACTTGGCCACAGTGAGGCTGNAAATGGCTGCAGGAACGGTGGTCCCCCCGCAAGGCCCCCATGGTCCCACCTCCCTGCCTGGCCCCTCCCGCTCCAGCGCCNCCAGCC"
DNA = DNA.upper()
print("Zasady azotowe - ilości: \n")

    #Policz ile razy występuje w kodzie każda zasada azotowa – adenina, cytozyna, guanina, tymina.

adenina = DNA.count("A")
cytozyny = DNA.count("C")
guaniny = DNA.count("G")
tyminy = DNA.count("T")

#print("Adenina: ", adenina)
#print("Cytozyny: ", cytozyny)
#print("Guaniny: ", guaniny)
#print("Tyminy: ", tyminy, "\n")

print("Adeniny: {}, Cytozyny: {}, Guaniny: {}, Tyminy: {}, \n" .format(adenina, cytozyny, guaniny, tyminy))

    #"gdy jakość sekwencji nie pozwala dokładnie odczytać rodzaju zasady azotowej wstawiany jest znak „-” Natomiast, gdy laser sczytujący ześlizgnie się, wstawiane są litery „N”, jednocześnie ostatnia wartość zasady jest ponownie odczytywana bez ubytku zasady w tym miejscu."

print("Błędy sekwencjonowania: ")

DNA = DNA.replace(" ", "")
fails1 = DNA.count("-")
fails2 = DNA.count("N")
print("Ilość błędów: ", fails1 + fails2)

    #Policz wystąpienia sekwencji GAGA i zamień je na AGAG

print("Ilość sekwencji GAGA w kodzie: ", DNA.count("GAGA"), "\n")

DNA = DNA.replace("N", "")
DNA = DNA.replace("GAGA", "AGAG")

print(DNA, "\n")
print("Ilość sekwencji GAGA w kodzie po modyfikacji: ", DNA.count("GAGA"), "\n")

fails1 = DNA.count("-")
fails2 = DNA.count("N")

print("Ilość błędów po modyfikacji: ", fails1 + fails2, "\n")

    #Znajdź miejsce (indeks) w łańcuchu, gdzie występuje 7 guanin z rzędu, znajdź miejsce (indeks) , gdzie od końca łańcucha występuje 6 cytozyn

print("Sekwencja sześciu guanin:", DNA.find("GGGGGGG"))
print("Sekwencja sześciu cytozyn od tyłu: ", DNA.rfind("CCCCCC"), "\n")

    #Policz ile razy w kodzie pojawiła się sekwencja CTGAAA. W sekwencji CTGAAA czasem mutuje ostania litera A, wówczas jakość ostatniej litery może być wątplia. Ile sekwencji znajdziesz, jeśli weźmiesz pod uwagę wątpliwą, ostatnią adeninę?
print("Ilość sekwnecji CTGAAA w kodzie DNA: ", DNA.count("CTGAAA"))
print("Ilość sekwencji CTGAA- w kodzie DNA: ", DNA.count("CTGAA-"), "\n")

CTGAA = DNA.count("CTGAAA")
CTGA_ = DNA.count("CTGAA-")

print("Suma sekwencji CTGAAA i CTGAA-: ", CTGAA + CTGA_, "\n")

    #Oczyść DNA z wszystkich błędów. Na podstawie czystej nici utwórz odpowiadającą jej nić RNA (nić RNA w miejscu tyminy będzie mieć uracyl (U))

DNA = DNA.replace("-", "")
RNA = DNA.replace("T", "U")

print("Obliczanie kodu RNA............:")
print(RNA)









