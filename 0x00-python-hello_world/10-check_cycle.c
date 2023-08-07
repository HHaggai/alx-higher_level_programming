#include "lists.h"

/**
 * chek_cycl - checs if a linkd list cont a cycl
 * @list: linkd list to chec
 *
 * Return: 1 if the list has a cycl, 0 if it does not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}

