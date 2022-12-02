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
    elf_and_pos = [max_elf,max_calorie]
    return elf_and_pos

def main():
    input = open('Day1\input.txt','r')
    elven_calories = input.read()
    input.close()
    max_elf = max_calorie_elf(elven_calories)
    print("Elf with most calories found at pos: {} with {} total calories in pack".format(max_elf[0],max_elf[1]))

if __name__ == "__main__":
    main()   