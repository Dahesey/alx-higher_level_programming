/**
  * check_cycle - A fucntion to check if a single list has a cycle
  * @list: Pointer to the head of the list
  * Return: 0 if there is no cycle 1 if there is a cycle
  */

#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
int check_cycle(listint_t *list)
{
	listint_t *slow_pointer = list;
	listint_t *fast_pointer = list;

	while (slow_pointer && fast_pointer && fast_pointer->next)
	{
		slow_pointer = slow_pointer->next;
		fast_pointer = fast_pointer->next->next;
		if (slow_pointer == fast_pointer)
			return (1);
	}
	return (0);
}
