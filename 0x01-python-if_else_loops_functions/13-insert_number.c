#include "lists.h"

/**
 * insert_node - insert node in sorted singly linked list
 * @head: the head of node
 * @number: number to be inserted
 * Return: address of new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *travel = *head;
	listint_t *newNode;

	if (!head)
	{
		return NULL;
	}
	newNode = malloc(sizeof(listint_t));
	newNode->n = number;

	while (travel)
	{
		if (travel->next->n < number)
			travel = travel->next;
		else
		{
			newNode->next = travel->next;
			travel->next = newNode;
			return (newNode);
		}
	}
	return (newNode);
}
