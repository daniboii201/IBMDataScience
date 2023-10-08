-- Example exercises on SELECT statement

/* Retrieve the names of all films with director names 
and writer names.*/
SELECT Title, Director, Writer 
FROM FilmLocations;

/* Retrieve the names of all films released in the 21st 
century and onwards (release years after 2001 including 
2001), along with filming locations and release years. */
SELECT Title, ReleaseYear, Locations 
FROM FilmLocations 
WHERE ReleaseYear>=2001;

-- Practice exercises on SELECT statement

/* Retrieve the fun facts and filming locations of 
all films. */
SELECT Locations, FunFacts FROM FilmLocations;

/* Retrieve the names of all films released in the 20th 
century and before (release years before 2000 including
2000) that, along with filming locations and release 
years. */
SELECT Title, ReleaseYear, Locations 
FROM FilmLocations 
WHERE ReleaseYear<=2000;

/* Retrieve the names, production company names, filming 
locations, and release years of the films which are not 
written by James Cameron. */
SELECT Title, ProductionCompany, Locations, ReleaseYear 
FROM FilmLocations 
WHERE Writer<>"James Cameron";
