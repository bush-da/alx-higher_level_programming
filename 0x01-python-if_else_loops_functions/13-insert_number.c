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

	newNode = malloc(sizeof(listint_t));
	newNode->n = number;
	if (*head == NULL)
	{
		*head = newNode;
		newNode->next = NULL;
		return (*head);
	}

	while (travel)
	{
		if (travel->n > number)
		{
			newNode->next = *head;
			*head = newNode;
			break;
		}
		if (travel->n < number && travel->next->n < number)
		{
			travel = travel->next;
			if (travel->next == NULL)
			{
				travel->next = newNode;
				newNode->next = NULL;
				return (newNode);
			}
		}
		else
		{
			newNode->next = travel->next;
			travel->next = newNode;
			return (newNode);
		}
	}
	return (newNode);
}
