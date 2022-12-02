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

def sorted_elven_calories(list):
    total_calories = []
    elves = list.split('\n\n')
    for x in elves:
        total_calories.append(calorie_count(x))
    sort = sorted(total_calories,reverse=True)
    return sort

def main():
    input = open('Day1\input.txt','r')
    elven_calories = input.read()
    input.close()
    max_elf = max_calorie_elf(elven_calories)
    print("Elf with most calories found at pos: {} with {} total calories in pack".format(max_elf[0],max_elf[1]))
    top_three = sorted_elven_calories(elven_calories)[0:3]
    print("The top three elves have calories of {}, with a total calorie count of {}".format(top_three,sum(top_three)))

if __name__ == "__main__":
    main()   