#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *check_cycle - checks if a singly linked list has a cycle in it.
 *@list: Ptr to the list to be checked
 *
 *Return: 1 if there's a cycle, else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *s = list, *t = list;

	while (t && t->next)
	{
		s = s->next;
		t = t->next->next;
		if (s == t)
			return (1);
	}
	return (0);
}
