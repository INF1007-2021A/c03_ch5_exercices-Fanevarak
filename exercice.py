#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number>=0:
        return number
    else:
        number=number+(-2)*number
        return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    results=[]
    for letter in prefixes:
        word=''
        result=letter+suffixe
        word+=result
        results.append(word)
    return results

def prime_integer_summation() -> int:
    prime=[]
    number=2
    while len(prime)<100:
        diviseur=2
        while diviseur<number and number%diviseur!=0:
            diviseur+=1
        if diviseur==number:
            prime.append(number)
        number+=1
    sum=0
    for numbers in prime:
        sum+=numbers
    return sum

def factorial(number: int) -> int:
    sum=1
    for number in range(number):
        sum*=number+1
    return sum


def use_continue() -> None:
    for number in range(10):
        if number==5:
            continue
        else: 
            print(number)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    Liste_Acceptance=[]
    for group in groups:
        Acceptance=True
        print(f'Groupe {group}')
        if len(group)>10 or len(group)<=3:
            Acceptance=False
            Liste_Acceptance.append(Acceptance)
            continue
        else:
            for age in group:
                if age==25:
                    Acceptance=True
                    break
                if age<18:
                    Acceptance=False
                    continue
                if age>70:
                    for age in group:
                        if age==50:
                            Acceptance=False
                            continue
                else: 
                    Acceptation=True
        print(Acceptance)
        Liste_Acceptance.append(Acceptance)
    return Liste_Acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
        [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
        [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
