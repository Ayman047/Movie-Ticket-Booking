class MovieTicketBooking:
    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.seats = [[False] * self.columns for _ in range(self.rows)]

    def display_seating(self):
        print("Seats availability:")
        for row in self.seats:
            print(" ".join(["X" if seat else "O" for seat in row]))

    def book_tickets(self, num_tickets):
        available_seats = [(row, col) for row in range(1, self.rows + 1) for col in range(1, self.columns + 1) if not self.seats[row - 1][col - 1]]

        if len(available_seats) < num_tickets:
            print(f"Sorry, there are not enough consecutive seats available for {num_tickets} tickets.")
            return

        print("Available seats:")
        for seat in available_seats:
            print(seat, end=" ")
        print()

        selected_seats = []
        for _ in range(num_tickets):
            while True:
                try:
                    seat_input = input("Enter the row and seat number (e.g., '2 3'): ")
                    row, col = map(int, seat_input.split())
                    if (row, col) in available_seats:
                        selected_seats.append((row, col))
                        break
                    else:
                        print("Invalid seat. Please choose from the available seats.")
                except ValueError:
                    print("Invalid input. Please enter row and seat numbers separated by a space.")

        for row, col in selected_seats:
            self.seats[row - 1][col - 1] = True

        print(f"Tickets booked for seats: {selected_seats}")

    def check_availability(self):
        total_seats = self.rows * self.columns
        booked_seats = sum(row.count(True) for row in self.seats)
        percentage_booked = (booked_seats / total_seats) * 100

        print(f"Total Seats: {total_seats}")
        print(f"Booked Seats: {booked_seats}")
        print(f"Percentage Booked: {percentage_booked:.2f}%")

        if percentage_booked == 100:
            print("All tickets are booked. The theater is full.")
        elif percentage_booked >= 70:
            print("Seats are fast filling. Book your tickets soon!")
        else:
            print("Seats are available. Enjoy your movie!")

# Sample usage of the MovieTicketBooking class
if __name__ == "__main__":
    movie_booking = MovieTicketBooking()

    while True:
        print("\n1. Display Seating")
        print("2. Book Tickets")
        print("3. Check Availability")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            movie_booking.display_seating()
        elif choice == "2":
            num_tickets = int(input("Enter the number of tickets to book: "))
            movie_booking.book_tickets(num_tickets)
        elif choice == "3":
            movie_booking.check_availability()
        elif choice == "4":
            print("Exiting the Movie Ticket Booking System. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
