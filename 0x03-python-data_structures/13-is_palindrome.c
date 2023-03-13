#include "lists.h"

/**
 * is_palindrome - checks the linked list if its palindrome or not
 * @head: pointer to head node
 * Return: 1 if it is a palindrome 0 if it is not
 */

int is_palindrome(listint_t **head)
{
	if (!head)
	{
		return 1;
	}

	unsigned int count, check, middle, middle2, start, end;
	listint_t *checker = *head;
	listint_t *traveler = *head;

	start = checker->n;
	count = 0;
	check = 0;
	while (traveler->next != NULL)
	{
		count++;
		traveler = traveler->next;
	}

	if (count % 2 != 0)
	{
		while (check < (count / 2))
		{
			check++;
			checker = checker->next;
		}

		middle = checker->n;
		middle2 = checker->next->n;
		if (middle == middle2)
		{
			while (checker->next != NULL)
				checker = checker->next;
			end = checker->n;
			if (start == end)
				return 1;
			else
				return 0;
		}
		else
			return 0;
	}
	else
	{
		while (check < ((count / 2) - 1))
		{
			check++;
			checker = checker->next;
		}

		middle = checker->n;
		middle2 = checker->next->n;
		if (middle == middle2)
		{
			while (checker->next != NULL)
				checker = checker->next;
			end = checker->n;
			if (start == end)
				return 1;
			else
				return 0;
		}
		else
			return 0;
	}
	return 0;
}
