/*
 * File: 0-print_dlistint.c
 * Auth: Hillary Haggai
 */

#include "lists.h"

/**
 * print_dlistint - Prnts the elements of a dlistint_t list.
 * @h: The head of dlistint_t list.
 *
 * Return: The num of nods in the list.
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t nodes = 0;

	while (h)
	{
		nodes++;
		printf("%d\n", h->n);
		h = h->next;
	}

	return (nodes);
}
