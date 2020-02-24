def card_printer(passenger, seat, airplane, flight_number):
    message = f"| passenger: {passenger}, seat: {seat}, airplane: {airplane}, flight number: {flight_number} |"
    banner = f"+{'-' * (len(message) - 2)}+"
    empty_banner = f"|{' ' * (len(message) - 2)}|"
    final_banner = [banner, empty_banner, banner, empty_banner, message, empty_banner, banner]
    print("\n".join(final_banner))
