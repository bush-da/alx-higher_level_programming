#include "lists.h"

/**
 * check_cycle - checks if a linked list have cycle
 * @list: linked list to check
 * Return: 0 if doesn't have cycle, 1 if it have
 */

int check_cycle(listint_t *list)
{
	listint_t *flag = list;
	listint_t *travel = list;

	if (!flag)
	{
		return (0);
	}

	while (travel)
	{
		if (travel == flag)
			return (1);
		travel = travel->next;
	}

	return (0);
}
