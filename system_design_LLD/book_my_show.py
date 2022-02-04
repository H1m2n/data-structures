class City:
    def __init__(self, city_name: str):
        city_name = city_name


class Cinema:
    def __init__(self, city: City):
        city = city


from enum import Enum


class SeatType(Enum):
    Platinum = 'Platinum'
    Silver = 'Silver'
    Gold = 'Gold'


# class BookingService:
#     def __init__(self):


class Audi:
    def __init__(self, cinema: Cinema):
        cinema = cinema


class Seat:
    def __init__(self, seat_id: int, seat_type: str, booking_status: bool, audi: Audi):
        seat_id = seat_id
        seat_type = seat_type
        booking_status = booking_status
        audi = audi


class GenreType(Enum):
    SCI_FIE = 'sci_fie'
    COMEDY = 'comedy'
    ACTION = 'action'


class Movie:
    def __init__(self, genre_type: str, movie_name: str):
        pass


class ShowTiming(Enum):
    MORNING = 'morning'
    AFTERNOON = 'after_noon'
    EVENING = 'evening'


class Show:
    def __init__(self, movie: Movie, audi: Audi, show_id: int, show_timing: str):
        show_id = show_id
        movie = Movie
        audi = Audi
        show_timing = show_timing


class Customer:
    def __init__(self, cust_id: str, name: str, age: int):
        cust_id = cust_id
        name = name
        age = age
        booking_id = None  # will be set inside select_show

    def search_movies(self, movie_name: str) -> Movie:
        pass

    def select_show(self, cinema: Cinema, city: City, show_timing: str, no_of_seats: int) -> Show:
        """
        Responsible to allocate the available sheet and need to lock sheets until payment is done
        """
        pass

    def cancel_booking(self, booking_id):
        """
        If customer want to cancel the booking, then we need to
        """


class Booking:
    def __init__(self, cust_id: Customer, ):
        pass
