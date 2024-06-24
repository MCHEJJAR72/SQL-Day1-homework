
SELECT COUNT(*)
FROM actor
WHERE last_name = 'Wahlberg';
How many payments were made between $3.99 and $5.99?

SELECT COUNT(*)
FROM payment
WHERE amount BETWEEN 3.99 AND 5.99;
What film does the store have the most of? (search in inventory)

SELECT film_id, COUNT(*) AS inventory_count
FROM inventory
GROUP BY film_id
ORDER BY inventory_count DESC
LIMIT 1;
How many customers have the last name ‘William’?

SELECT COUNT(*)
FROM customer
WHERE last_name = 'William';
What store employee (get the id) sold the most rentals?

SELECT staff_id, COUNT(rental_id) AS rental_count
FROM rental
GROUP BY staff_id
ORDER BY rental_count DESC
LIMIT 1;
How many different district names are there?

SELECT COUNT(DISTINCT district)
FROM address;
What film has the most actors in it? (use film_actor table and get film_id)

SELECT film_id, COUNT(actor_id) AS actor_count
FROM film_actor
GROUP BY film_id
ORDER BY actor_count DESC
LIMIT 1;
From store_id 1, how many customers have a last name ending with ‘es’?

SELECT COUNT(*)
FROM customer
WHERE store_id = 1 AND last_name LIKE '%es';
How many payment amounts (4.99, 5.99, etc.) had a number of rentals above 250 for customers with ids between 380 and 430?

SELECT amount, COUNT(rental_id) AS rental_count
FROM payment p
JOIN rental r ON p.customer_id = r.customer_id
WHERE p.amount IN (4.99, 5.99) AND p.customer_id BETWEEN 380 AND 430
GROUP BY amount
HAVING COUNT(rental_id) > 250;
Within the film table, how many rating categories are there? And what rating has the most movies total?

-- Count of distinct rating categories
SELECT COUNT(DISTINCT rating) AS num_rating_categories
FROM film;

-- Rating with the most movies
SELECT rating, COUNT(*) AS movie_count
FROM film
GROUP BY rating
ORDER BY movie_count DESC
LIMIT 1;