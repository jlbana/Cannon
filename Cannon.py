from Polygon import Polygon

Cannon = Polygon((1, 4),
		 (1, 2),
		 (2, 1),
		 (3, 1),
		 (5, 2),
		 (7, 2),
		 (8, 1),
		 (9, 1),
		 (9, 5),
		 (8, 5),
		 (7, 4),
		 (5, 4),
		 (3, 5),
		 (2, 5))

Cannon += (-2.5, -3)
Cannon *= 4

Support = Polygon((1, 2),
		  (2, 0),
		  (3, 0),
		  (4, 2))
Support += (-2, 0)
Support *= 6
Support += (0, 199 - 8)

