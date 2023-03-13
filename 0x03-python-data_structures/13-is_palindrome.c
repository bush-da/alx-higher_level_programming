#include "lists.h"

/**
 * is_palindrome - checks if the linked list is palindrome or not
 * @head: address of head node
 * Return: 1 if linked list is palindrome 0 if it is not
 */

int is_palindrome(listint_t **head)
{
	if (!*head)
		return 1;

	listint_t *ch1 = *head;
	listint_t *counter = *head;
	unsigned int count, checker, middle;

	count = 0;
	checker = 0;
	while (counter->next != NULL)
	{
		count++;
		counter = counter->next;
	}

	unsigned int arr[count];

	middle = count / 2;

	while (checker <= count)
	{
		arr[checker] = ch1->n;
		checker++;
		ch1 = ch1->next;
	}
	checker = 0;

	while (checker <= middle && middle <= count)
	{
		if (arr[checker] == arr[count])
		{
			count--;
			checker++;
		}
		else
			return 0;
	}

	return 1;
}
