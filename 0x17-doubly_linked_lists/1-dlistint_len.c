#include "lists.h"

/**
 * dlistint_len - retrns the num of elements in
 * a doubl linkd list
 *
 * @h: head of list
 * Return: the num of nods
 */
size_t dlistint_len(const dlistint_t *h)
{
	int count;

	count = 0;

	if (h == NULL)
		return (count);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		count++;
		h = h->next;
	}

	return (count);
}
