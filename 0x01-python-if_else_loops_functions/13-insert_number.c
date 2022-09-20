#include <stdlib.h>
<<<<<<< HEAD
#include "lists.h"

/**
 * *insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to address of head of list
 * @number: integer to be include in new node
 * Return: address of new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	if (*head == NULL)
	{
		newnode->n = number;
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	else if (number <= (*head)->n)
	{
		newnode->n = number;
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	else
	{
		temp = *head;
		while (temp->next != NULL && number > temp->next->n)
		{
			temp = temp->next;
		}
		newnode->n = number;
		newnode->next = temp->next;
		temp->next = newnode;
		return (newnode);
	}
	return (NULL);
}
=======
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - Insert node in order mode to linkedlist
 * @head: head
 * @number: num to be added
 * Return: the address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *actual = *head;

	if (!new)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (actual->next)
	{
		if ((actual->next)->n >= number)
		{
			new->next = actual->next;
			actual->next = new;
			return (new);
		}
		actual = actual->next;
	}

	new->next = NULL;
	actual->next = new;

	return (new);
}
>>>>>>> 2ec5e458660d8b769d856d9ee079877bc6635f13
