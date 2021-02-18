
def Length(Name):
    return len(Name)
    
def main():
    print("Enter Name to find it's length")
    Name = input()
    
    print("Length of name {} is : {}".format(Name,Length(Name)))
    print()
    
if __name__ == "__main__":
    main()

