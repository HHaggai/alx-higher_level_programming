#include "lists.h"

/**
 * insert_node - Inserts a num into a sortd singly-linkd list.
 * @head: A pointr to head of the linkd list.
 * @number: The num to insert.
 *
 * Return: If the funct fails - NULL.
 * Otherwise - a pointr to the new nod.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}

