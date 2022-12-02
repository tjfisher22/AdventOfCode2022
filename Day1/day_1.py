def calorie_count(elf):
    total = 0
    calories = elf.split('\n')
    for x in calories:
        total += int(x)
    return total

def max_calorie_elf(list):
    max_elf = 0
    max_calorie = 0
    elves = list.split('\n\n')
    for i, x in enumerate(elves):
        if calorie_count(x) > max_calorie:
            max_calorie = calorie_count(x)
            max_elf = i + 1
    return max_elf

def main():
    input = open('Day1\input.txt','r')
    elven_calories = input.read()
    input.close()
    max_elf = max_calorie_elf(elven_calories)
    print("Elf with most calories found: {}".format(max_elf))

if __name__ == "__main__":
    main()   