from datetime import datetime
import json
from time import sleep

SHOWS_FILE = "./shows.json"
TRANSACTIONS_FILE = "./transactions.txt"
TICKET_FILE = "./ticket.txt"
SALES_TAX = 0.07


def get_shows():
    with open(SHOWS_FILE) as file:
        return json.load(file)


def ticket_maker(shows, tickets, desired_show, name):
    for show in shows:
        s = "{:=^40}\n".format("=")
        s += "]" + "THE JEFFERSON".center(38, " ") + "[\n"
        s += f"]{'FEATURING...'.center(38, ' ')}[\n"
        s += "]" + "".center(38, " ") + "[\n"
        s += "]" + f"{show.get('artist')}".upper().center(38, " ") + "[\n"
        s += "]" + f"With {show.get('opener')}".center(38, " ") + "[\n"
        s += "]" + f"{show.get('date')}".center(38, " ") + "[\n"
        s += (
            "]"
            + f"Doors: {show.get('doors')}, Show: {show.get('show')}".center(38, " ")
            + "[\n"
        )
        s += "]" + "".center(38, " ") + "[\n"
        s += "]" + f"Admit: {tickets}, Code: {show.get('code')}".center(38, " ") + "[\n"
        s += "{:=^40}".format("=")
        print(s)
        if show.get("artist") == desired_show:
            with open(TICKET_FILE, "w") as file:
                file.write(s)


def save_to_all(shows, tickets, desired_show, name):
    with open(SHOWS_FILE, "w") as file:
        json.dump(shows, file)
    with open(TRANSACTIONS_FILE) as transaction_file:
        rest = transaction_file.readlines()
    for show in shows:
        if show.get("artist") == desired_show:
            price = show["price"] * tickets
            tax = price * SALES_TAX
            insertion_string = "\n" + "{}, {}, {}, {}, ${:,.2f}, ${:,.2f}, {}".format(
                name,
                show.get("artist"),
                show.get("code"),
                tickets,
                price,
                tax,
                datetime.now(),
            )
            rest.append(insertion_string)
    with open(TRANSACTIONS_FILE, "w") as transaction_file:
        transaction_file.write("".join(rest))
    ticket_maker(shows, tickets, desired_show, name)
    quit()


def make_purchase(shows, tickets, desired_show, name):
    for show in shows:
        if show.get("artist") == desired_show:
            show["tickets"] = show["tickets"] - tickets
            save_to_all(shows, tickets, desired_show, name)


def check_tickets(shows, tickets, desired_show, name):
    for show in shows:
        if show.get("artist") == desired_show:
            if show["tickets"] == "SOLD OUT":
                print("Sorry that show is sold")
                main()
            elif show.get("tickets") - tickets >= 0:
                print("You may make this purchase")
                make_purchase(shows, tickets, desired_show, name)
            else:
                print(f"No You can only buy {show.get('tickets')} tickets")
                print("Please ReRun Program!")
                sleep(2)
                main()


def proccess_begin(shows, tickets, name):
    artist_list = []
    print("What show would you like to see?")
    for show in shows:
        artist_list.append(show.get("artist"))
        print(f"{show.get('artist')}, {show.get('show')},{show.get('date')}\n")
    print("What show would you like you to attend to?")
    show_input = input("Artist Name?: ")
    if show_input in artist_list:
        check_tickets(shows, tickets, show_input, name)
    else:
        print("Invalid Response")


def main():
    print("Welcome to The Jefferson venue ticket purchasing tool!")
    name = input("Name:")
    shows = get_shows()
    while True:
        number_of_tickets = int(input("How many tickets would you like to buy?: "))
        if number_of_tickets > 4:
            print("You cannot Buy more than 4 at a time!")
        elif number_of_tickets > 0:
            proccess_begin(shows, number_of_tickets, name)
        else:
            print("Invalid Number or Response")


if __name__ == "__main__":
    main()
