#include "lists.h"

/**
 * is_palindrome - checks if the linked list is palindrome or not
 * @head: address of head node
 * Return: 1 if linked list is palindrome 0 if it is not
 */

int is_palindrome(listint_t **head)
{
	listint_t *ch1 = *head;
	listint_t *ch2 = *head;
	listint_t *counter = *head;
	int count, middle, checker, middle2;

	if (!*head)
		return 1;

	count = 0;
	checker = 0;
	while (counter->next != NULL)
	{
		count++;
		counter = counter->next;
	}

	middle = count / 2;
	middle2 = middle;

	while (checker <= middle2)
	{
		checker++;
		ch2 = ch2->next;
	}
	checker = 0;
	while (ch2 != NULL)
	{
		while (checker < middle)
		{
			checker++;
			ch1 = ch1->next;
		}

		if (ch2->n == ch1->n)
		{
			middle--;
			checker = 0;
			ch2 = ch2->next;
			ch1 = *head;
		}
		else
			return 0;
	}

	return 1;
}
