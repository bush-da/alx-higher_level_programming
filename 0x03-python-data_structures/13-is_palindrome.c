#include "lists.h"

/**
 * is_palindrome - checks the linked list if its palindrome or not
 * @head: pointer to head node
 * Return: 1 if it is a palindrome 0 if it is not
 */

int is_palindrome(listint_t **head)
{
	unsigned int count, check, middle, middle2, start, end, half;
	listint_t *checker = *head;
	listint_t *traveler = *head;

	if (!*head)
		return 1;

	start = checker->n;
	count = 0;
	check = 0;
	while (traveler->next != NULL)
	{
		count++;
		traveler = traveler->next;
	}
	traveler = *head;
	traveler = traveler->next;

	half = count / 2;

	while (check < half)
	{
		check++;
		checker = checker->next;
	}

	middle = checker->n;
	checker = checker->next;
	middle2 = checker->n;

	if (middle == middle2)
	{
		while (checker->next->next != NULL)
			checker = checker->next;
		end = checker->next->n;
		if (start == end)
		{
			if (checker->n == traveler->n)
				return 1;
		}
		else
			return 0;
	}
	else
	{
		return 0;
	}

	return 0;
}
