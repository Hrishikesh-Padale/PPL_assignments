info(toronto,'$50','60min').
info(paris,'$50','60min').
info(toulouse,'$40','3s0min').
info(london,'$75','80min').
info(barcelona,'$40','30min').
info(madrid,'$75','45min').

flight(toronto,london,'Air Canada',500,'360min').
flight(toronto,london,'United',450,'420min').
flight(london,barcelona,'Iberia',220,'240min').
flight(paris,toulouse,'United',35,'120min').
flight(barcelona,madrid,'Air Canada',100,'60min').
flight(barcelona,madrid,'Iberia',120,'65min').
flight(toronto,madrid,'Air Canada',900,'480min').
flight(toronto,madrid,'United',950,'540min').
flight(toronto,madrid,'Iberia',800,'480min').


airport(A,B,C) :- info(A,B,C).

flight_available(A,B) :- flight(A,B,C,D,E) ; flight(B,A,C,D,E).

flight_info(A,B,C,D,E) :- flight(A,B,C,D,E).

cheap(A,B,C,D,E) :- (flight(A,B,C,D,E) ; flight(B,A,C,D,E)) , D < 400.

two(A,B) :- (flight(A,X,C,D,E) ; flight(X,A,C,D,E)) , (flight(X,B,F,G,H) ; flight(B,X,F,G,H)).

prefer(A,B,C,D,E) :- cheap(A,B,C,D,E) ; ((flight(A,B,'Air Canada',F,G);flight(B,A,'Air Canada',F,G)) , (flight(A,B,C,D,E);flight(B,A,C,D,E)) , D < F).

exist(A,B) :- (flight(A,B,'United',D,E) ; flight(B,A,'United',D,E)) , (flight(A,B,'Air Canada',F,G) ; flight(B,A,'Air Canada',F,G)).
