with open("input.txt", "r") as file:
    sum = 0
    current_elf_calories = 0
    elf_max_calories = [0,0,0]
    for line in file: # Leer cada linea

        if line != "\n":    
            current_elf_calories += int(line)
        else:
            if current_elf_calories >= elf_max_calories[-1]:
                elf_max_calories.insert(0,current_elf_calories)
            current_elf_calories = 0
    elf_max_calories.sort(reverse=True)
    print(elf_max_calories)
    print(elf_max_calories[0]+elf_max_calories[1]+elf_max_calories[2])
