## Practice Match and Case statements 

color = input("Enter the color: ")

match color:
    case 'Red':
        print("STOP")
    case 'Yellow':
        print("LOOK")
    case 'Green':
        print("GO")
    case _:
        print("Invalid color")
        