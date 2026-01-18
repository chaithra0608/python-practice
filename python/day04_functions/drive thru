# Write code below 💖
# drive_thru.py

menu = {
    1: "🍔 Cheeseburger",
    2: "🍟 Fries",
    3: "🥤 Soda",
    4: "🍦 Ice Cream",
    5: "🍪 Cookie"
}

def get_item(number):
    return menu.get(number, "❌ Sorry, that item number is not on the menu.")

def welcome():
    print("🍔 Welcome to McDonald's Drive-Thru! 🍔")
    print("Here’s our menu:")
    for number, item in menu.items():
        print(f"{number}. {item}")
    print("Please enter the item number to order.\n")

# main program
if __name__ == "__main__":
    welcome()
    choice = int(input("Enter your item number: "))
    print("You ordered:", get_item(choice))

