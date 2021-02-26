#   10. Write a program which accept name from user and display length of its name.
#   Input : Marvellous Output : 10

def Length(Name):
    return len(Name)
    
def main():
    print("Enter Name to find it's length")
    Name = input()
    
    print("Length of name {} is : {}".format(Name,Length(Name)))
    print()
    
if __name__ == "__main__":
    main()

