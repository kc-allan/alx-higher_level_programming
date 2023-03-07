#include "lists.h"
/**
 * insert_node - inserts number into a sorted linked list
 * @head: list's starting point
 * @number: number to be inserted
 * Retuen: address to new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	int *temp;


