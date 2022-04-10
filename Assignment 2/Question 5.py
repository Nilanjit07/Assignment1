def main():
    character = "*"
    rows_number = int(input("Enter number of rows:"))
    while(rows_number-1):
        if not(character.endswith(" ")):    
            character+= " " 
            for i in range(rows_number):
                print(" "*i+character*(rows_number-i))
            for j in range(2, rows_number+1):
                print(" "*(rows_number-j)+character*j)
            break
if __name__ == "__main__":
    main()
