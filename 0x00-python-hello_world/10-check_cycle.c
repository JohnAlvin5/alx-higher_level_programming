#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list : pointer to fist node
 *
 * Return: 1 if cycle present, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1 = list;
	listint_t *temp2 = list;

	while (temp1->next && temp2->next->next)
	{
		temp2 = temp2->next->next;
		if (!temp2->next)
			return (0);

		temp1 = temp1->next;
		if (temp1 == temp2)
			return (1);
	}

	return (0);
}
