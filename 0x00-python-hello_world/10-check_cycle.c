#include "lists.h"

/**
 * check_cycle - checks if a linked list have cycle
 * @list: linked list to check
 * Return: 0 if doesn't have cycle, 1 if it have
 */

int check_cycle(listint_t *list)
{
	listint_t *rabbit;
	listint_t *turtle;

	rabbit = list;
	turtle = list;

	while (rabbit != NULL && turtle != NULL && turtle->next != NULL)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;
		if (turtle == rabbit)
			return (1);
	}

	return (0);
}
