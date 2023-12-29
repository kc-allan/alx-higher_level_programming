#include "lists.h"
/**
 * insert_node - inserts number into a sorted linked list
 * @head: list's starting point
 * @number: number to be inserted
 * Return: address to new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if (number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	temp = *head;
	while (temp->next != NULL && number > temp->next->n)
	{
		temp = temp->next;
	}
	new_node->next = temp->next;
	temp->next = new_node;
	return (new_node);
}
